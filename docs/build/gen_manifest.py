# -*- coding: utf-8 -*-
"""自动生成/校验各章 pdf_manifest.txt（README + 编号 md，按文件名排序）。

用法:
  python build/gen_manifest.py            # 更新所有章（保留 TITLE）
  python build/gen_manifest.py --dry-run  # 只打印差异
  python build/gen_manifest.py --check    # 有差异则返回 1（供 CI/update_all 调用）
  python build/gen_manifest.py 01-numpy   # 只处理一章
"""
import os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHAPTERS = os.path.join(ROOT, "chapters")


def current_manifest(path):
    title, files = None, []
    if os.path.exists(path):
        with open(path, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                if line.upper().startswith("TITLE:"):
                    title = line.split(":", 1)[1].strip()
                elif not line.startswith("#"):
                    files.append(line)
    return title, files


def generated(ch, title):
    lines = []
    head = f"# 第 {int(ch[:2])} 章 PDF 合订清单（build/pdf_build.py 读取）" if ch[:2].isdigit() else "# PDF 合订清单（build/pdf_build.py 读取）"
    lines.append(head)
    lines.append(f"TITLE: {title if title else ch}")
    lines.append("README.md")
    md_files = sorted(f for f in os.listdir(os.path.join(CHAPTERS, ch))
                      if f.endswith(".md") and re.match(r"^[0-9]{2}-", f))
    lines.extend(md_files)
    return "\n".join(lines) + "\n"


def build(ch, dry=False, check=False):
    d = os.path.join(CHAPTERS, ch)
    mf = os.path.join(d, "pdf_manifest.txt")
    title, _ = current_manifest(mf)
    gen = generated(ch, title)
    if dry or check:
        if not os.path.exists(mf):
            return False, gen, None
        old = open(mf, encoding="utf-8").read()
        return old == gen, gen, old
    with open(mf, "w", encoding="utf-8") as f:
        f.write(gen)
    return True, gen, None


def main():
    args = sys.argv[1:]
    dry = "--dry-run" in args
    check = "--check" in args
    wanted = [a for a in args if not a.startswith("--")]
    if wanted:
        chapters = [a for a in wanted if os.path.isdir(os.path.join(CHAPTERS, a))]
    else:
        chapters = sorted(d for d in os.listdir(CHAPTERS)
                          if os.path.isdir(os.path.join(CHAPTERS, d))
                          and os.path.exists(os.path.join(CHAPTERS, d, "pdf_manifest.txt")))
    bad = 0
    for ch in chapters:
        ok, gen, old = build(ch, dry=dry or check, check=check)
        if dry or check:
            if ok:
                print(f"[ok] {ch}")
            else:
                bad += 1
                if old is not None:
                    print(f"[diff] {ch}")
                    import difflib
                    for line in list(difflib.unified_diff(old.splitlines(), gen.splitlines(), lineterm=""))[:20]:
                        print("   ", line)
                else:
                    print(f"[new] {ch}: would create {gen.splitlines()[1]}")
        else:
            print(f"[gen] {ch} -> {os.path.relpath(os.path.join(CHAPTERS, ch, 'pdf_manifest.txt'), ROOT)}")
    sys.exit(1 if (check and bad) else 0)


if __name__ == "__main__":
    main()
