# -*- coding: utf-8 -*-
"""自动运行各章正文 Python 代码并核对相邻 text 输出块。

用法:
  python build/validate_code.py                # 全部章节
  python build/validate_code.py 01-numpy       # 指定章
  python build/validate_code.py --quiet        # 只报告错误/差异
"""
import os, re, sys, json, textwrap, subprocess, tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHAPTERS = os.path.join(ROOT, "chapters")
BT = chr(96)
FENCE = BT * 3

def parse_blocks(text):
    blocks = []
    cur = None  # (kind, lines)
    for line in text.split("\n"):
        s = line.strip()
        if s.startswith(FENCE):
            if cur is None:
                lang = s[3:].strip()
                kind = "code" if lang.startswith("python") else ("text" if lang.startswith("text") else "other")
                cur = [kind, []]
            else:
                blocks.append((cur[0], "\n".join(cur[1])))
                cur = None
        elif cur is not None:
            cur[1].append(line)
    if cur is not None:
        blocks.append((cur[0], "\n".join(cur[1])))
    return blocks

def norm_output(s):
    lines = [ln.rstrip() for ln in s.replace("\r\n", "\n").split("\n")]
    while lines and not lines[-1].strip():
        lines.pop()
    return "\n".join(lines)

def run_file(path):
    text = open(path, encoding="utf-8").read()
    blocks = parse_blocks(text)
    code_i = [i for i, (k, _) in enumerate(blocks) if k == "code"]
    if not code_i:
        return None
    code_blocks = [textwrap.dedent(blocks[i][1]).strip() for i in code_i]
    driver = [
        "import io, sys, contextlib, json, textwrap, traceback",
        "BLOCKS = json.loads(r'''" + json.dumps(code_blocks, ensure_ascii=False) + "''')",
        "ns = {'__name__': '__main__'}",
        "exec('import numpy as np', ns)",
        "outputs = []",
        "errors = []",
        "for i, code in enumerate(BLOCKS):",
        "    code = textwrap.dedent(code).strip()",
        "    buf = io.StringIO()",
        "    try:",
        "        with contextlib.redirect_stdout(buf):",
        "            exec(compile(code, '<block%d>' % i, 'exec'), ns)",
        "    except Exception as e:",
        "        errors.append((i, repr(e)))",
        "    outputs.append(buf.getvalue())",
        "print(json.dumps({'outputs': outputs, 'errors': errors}, ensure_ascii=False))",
    ]
    driver_path = os.path.join(tempfile.gettempdir(), "_code_check_driver.py")
    with open(driver_path, "w", encoding="utf-8") as f:
        f.write("\n".join(driver))
    env = dict(os.environ)
    env["MPLBACKEND"] = "Agg"
    env["PYTHONIOENCODING"] = "utf-8"
    try:
        p = subprocess.run([sys.executable, driver_path], capture_output=True,
                           text=True, encoding="utf-8", errors="replace",
                           cwd=tempfile.gettempdir(), env=env, timeout=180)
    except subprocess.TimeoutExpired:
        return {"error": "timeout"}
    last = (p.stdout or "").strip().splitlines()
    if not last:
        return {"error": (p.stderr or "")[-500:]}
    try:
        obj = json.loads(last[-1])
    except Exception:
        return {"error": (p.stdout or "")[-500:]}
    return obj

def main():
    args = sys.argv[1:]
    quiet = "--quiet" in args
    strict = "--strict" in args
    wanted = [a for a in args if not a.startswith("--")]
    if wanted:
        chapters = [a for a in wanted if os.path.isdir(os.path.join(CHAPTERS, a))]
    else:
        chapters = sorted(d for d in os.listdir(CHAPTERS)
                          if os.path.isdir(os.path.join(CHAPTERS, d))
                          and os.path.exists(os.path.join(CHAPTERS, d, "pdf_manifest.txt")))
    problems = 0
    for ch in chapters:
        cdir = os.path.join(CHAPTERS, ch)
        files = sorted(f for f in os.listdir(cdir) if re.match(r"^[0-9]{2}-.*\.md$", f))
        for fname in files:
            res = run_file(os.path.join(cdir, fname))
            if res is None:
                continue
            if "error" in res:
                problems += 1
                print(f"[ERR] {ch}/{fname}: {res['error']}")
                continue
            errs = res.get("errors") or []
            if errs:
                problems += 1
                print(f"[ERR] {ch}/{fname}: {len(errs)} runtime errors")
                for i, e in errs[:5]:
                    print(f"    block {i+1}: {e}")
            text = open(os.path.join(cdir, fname), encoding="utf-8").read()
            blocks = parse_blocks(text)
            for idx, (kind, body) in enumerate(blocks):
                if kind != "code":
                    continue
                if idx + 1 >= len(blocks) or blocks[idx + 1][0] != "text":
                    continue
                code_ord = sum(1 for k, _ in blocks[:idx] if k == "code")
                if code_ord >= len(res.get("outputs", [])):
                    continue
                actual = norm_output(res["outputs"][code_ord])
                expected = norm_output(blocks[idx + 1][1])
                if actual != expected:
                    problems += 1
                    print(f"[DIFF] {ch}/{fname} block {code_ord+1}")
                    exp_lines = expected.split("\n")
                    act_lines = actual.split("\n")
                    for k in range(max(len(exp_lines), len(act_lines))):
                        e = exp_lines[k] if k < len(exp_lines) else "<end>"
                        a = act_lines[k] if k < len(act_lines) else "<end>"
                        if e != a:
                            print(f"    line {k+1}: expected={e!r} actual={a!r}")
                            if k > 8:
                                break
    print(f"\n===== validate_code: {problems} problem(s)=====" + ("" if strict else " (warnings, use --strict to fail)"))
    sys.exit(1 if (problems and strict) else 0)

if __name__ == "__main__":
    main()
