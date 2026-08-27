# -*- coding: utf-8 -*-
"""Mode B: emit an editable/compilable LaTeX project 教材TeX/ from chapters/*.md.

Strategy: build ONE standalone .tex via pandoc (template auto-detects tables/code-hl),
then split its body at \\chapter boundaries into chapters/chNN.tex and make main.tex
\\input those fragments. Reliable to compile with latexmk -xelatex.

User-editable: user_style.tex / user_meta.yaml (never overwritten).
Usage:
  python build/emit_tex.py            # regenerate project
  python build/emit_tex.py --check    # list chapters whose md changed
  python build/emit_tex.py --compile  # also latexmk -xelatex main.tex
"""
import os, sys, re, json, shutil, subprocess, hashlib
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import texbook as tb

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEX_DIR = os.path.join(ROOT, "教材TeX")
CHAPTERS_DIR = os.path.join(ROOT, "chapters")
FIGS_DIR = os.path.join(TEX_DIR, "figures")
CHAP_TEX_DIR = os.path.join(TEX_DIR, "chapters")
USER_STYLE = os.path.join(TEX_DIR, "user_style.tex")
USER_META = os.path.join(TEX_DIR, "user_meta.yaml")
CACHE = os.path.join(ROOT, "build", ".tex_emit_cache.json")
MAIN_TEX = os.path.join(TEX_DIR, "main.tex")
MAIN_FULL = os.path.join(TEX_DIR, ".main_full.tex")
BACKUP_DIR = os.path.join(TEX_DIR, "_manual_backup")
NOTE = "%% 由 build/emit_tex.py 生成（生成物，勿手改）；定制请放 user_style.tex / user_meta.yaml"


def md_hash(paths):
    h = hashlib.sha256()
    for p in paths:
        with open(p, "rb") as f:
            h.update(f.read())
    return h.hexdigest()


def chapter_meta(ch):
    title, files = tb.read_manifest(ch)
    srcs = [os.path.join(CHAPTERS_DIR, ch, f) for f in files
            if os.path.exists(os.path.join(CHAPTERS_DIR, ch, f))]
    return title, srcs


def merged_book_md(cfg):
    parts = []
    for ch in cfg["chapters"]:
        title, _ = chapter_meta(ch)
        body = [f"# {title}", ""]
        title0, files = tb.read_manifest(ch)
        for rel in files:
            if rel.lower() in ("README.md", "readme.md"):
                continue
            src = os.path.join(CHAPTERS_DIR, ch, rel)
            if not os.path.isfile(src):
                continue
            with open(src, encoding="utf-8") as f:
                text = tb.shift_heading(f.read())
            text = text.replace("./images/", f"figures/{ch}/")
            text = text.replace("../images/", f"figures/{ch}/")
            text = text.replace("images/", f"figures/{ch}/")
            body.append(text.strip() + "\n\n")
        parts.append("\n\n".join(body))
    return "\n\n\\newpage\n\n".join(parts)


def copy_figures(ch):
    src, dst = os.path.join(CHAPTERS_DIR, ch, "images"), os.path.join(FIGS_DIR, ch)
    if os.path.isdir(src):
        os.makedirs(dst, exist_ok=True)
        for f in os.listdir(src):
            shutil.copy2(os.path.join(src, f), os.path.join(dst, f))


def split_chapters(tex, chapters):
    """Split the standalone tex body at \\chapter boundaries -> chapter files."""
    bd = tex.index("\\begin{document}")
    ed = tex.index("\\end{document}")
    preamble = tex[:bd] + "\\begin{document}\n"
    body = tex[bd + len("\\begin{document}"):ed]
    pos = [m.start() for m in re.finditer(r"\\chapter\{", body)]
    if len(pos) != len(chapters):
        raise RuntimeError(f"chapter count mismatch: tex={len(pos)} cfg={len(chapters)}")
    chunks = []
    for i, p in enumerate(pos):
        end = pos[i + 1] if i + 1 < len(pos) else len(body)
        chunks.append(body[p:end].rstrip() + "\n")
    main_body = "\n".join(["\\input{chapters/ch" + ch + ".tex}\n" for ch in chapters])
    main = preamble + main_body + "\n\\end{document}\n"
    return main, chunks


def write(path, text, header=True):
    if header:
        text = NOTE + "\n" + text
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def main():
    args = sys.argv[1:]
    os.makedirs(TEX_DIR, exist_ok=True)
    os.makedirs(CHAP_TEX_DIR, exist_ok=True)
    os.makedirs(FIGS_DIR, exist_ok=True)
    cfg = tb.load_cfg()
    chapters = cfg["chapters"]
    cache = {}
    if os.path.exists(CACHE):
        with open(CACHE, encoding="utf-8") as f:
            cache = json.load(f)

    # --check
    if "--check" in args:
        stale = []
        for ch in chapters:
            _, srcs = chapter_meta(ch)
            if cache.get(ch, {}).get("hash") != md_hash(srcs):
                stale.append(ch)
        print("stale chapters:", stale if stale else "none")
        return

    # 1) merged md -> standalone tex
    md = merged_book_md(cfg)
    tmp = os.path.join(ROOT, "build", "_emit_all.md")
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(md)
    cmd = ["pandoc", tmp, "-o", MAIN_FULL, "-s", "-t", "latex",
           "--top-level-division=chapter",
           "-V", "documentclass=ctexbook",
           "-V", "mainfont=Microsoft YaHei", "-V", "CJKmainfont=Microsoft YaHei",
           "-V", "monofont=Consolas", "-V", "geometry:margin=2.2cm",
           "-V", "colorlinks=true", "-V", "linkcolor=blue",
           "--toc", "--toc-depth=2", "-V", "toc-title=目录",
           "--highlight-style=tango",
           "--include-in-header=" + os.path.join(ROOT, "build", "texbook_header.tex"),
           "--metadata", f"title={cfg.get('title','Python 科学计算')}",
           "--metadata", f"author={cfg.get('author','')}",
           "--metadata", f"date={cfg.get('date','')}"]
    for extra, flag in ((USER_STYLE, "--include-in-header"), (USER_META, "--metadata-file")):
        if os.path.exists(extra):
            cmd += [flag, extra]
    p = subprocess.run(cmd, capture_output=True, encoding="utf-8", errors="replace")
    os.remove(tmp)
    if p.returncode != 0 or not os.path.exists(MAIN_FULL):
        print("[error] standalone tex failed:", p.stderr[-600:])
        sys.exit(1)
    with open(MAIN_FULL, encoding="utf-8") as f:
        tex = f.read()

    # 2) split
    main_tex, chunks = split_chapters(tex, chapters)

    # 3) per-chapter files + manual protection + cache
    for ch, chunk in zip(chapters, chunks):
        out = os.path.join(CHAP_TEX_DIR, f"ch{ch}.tex")
        _, srcs = chapter_meta(ch)
        h = md_hash(srcs)
        old = cache.get(ch, {})
        if os.path.exists(out):
            with open(out, encoding="utf-8") as f:
                cur = f.read()
            cur_h = hashlib.sha256(cur.encode("utf-8")).hexdigest()
            if old.get("tex_hash") and cur_h != old.get("tex_hash") and old.get("hash") == h:
                print(f"[manual-preserved] {ch} (md unchanged)")
                cache[ch] = old
                copy_figures(ch)
                continue
            if cur_h != old.get("tex_hash"):
                os.makedirs(BACKUP_DIR, exist_ok=True)
                shutil.copy2(out, os.path.join(BACKUP_DIR, f"ch{ch}.tex.{int(datetime.now().timestamp())}"))
        write(out, chunk)
        cache[ch] = {"hash": h, "tex_hash": hashlib.sha256(chunk.encode("utf-8")).hexdigest()}
        copy_figures(ch)
        print(f"[gen] chapters/ch{ch}.tex (+figures/{ch})")

    # 4) main.tex + meta
    write(MAIN_TEX, main_tex, header=True)
    os.remove(MAIN_FULL)
    write(os.path.join(TEX_DIR, "book_meta.yaml"),
          f"title: {cfg.get('title','')}\nauthor: {cfg.get('author','')}\ndate: {cfg.get('date','')}\nchapters: {', '.join(chapters)}\n")
    write(os.path.join(TEX_DIR, "references.bib"), "% 预留：可从未来 references 生成\n")
    write(os.path.join(TEX_DIR, "README.md"),
          "# 教材TeX（可编译 LaTeX 工程）\n\n"
          "- 由 build/emit_tex.py 生成；章节/正文/图均来自 chapters/。\n"
          "- 可手改：user_style.tex（宏包/页眉/封面）、user_meta.yaml（标题/作者/日期）。\n"
          "- 编译：cd 教材TeX && latexmk -xelatex main.tex。\n"
          "- 刷新：python build/emit_tex.py [--check|--compile]。\n"
          "- 手改且 md 未变的章节会保留（备份 _manual_backup/）。\n")
    with open(CACHE, "w", encoding="utf-8") as f:
        json.dump(cache, f, ensure_ascii=False, indent=1)
    print("[done] 教材TeX project:", TEX_DIR)

    if "--compile" in args:
        q = subprocess.run(["latexmk", "-xelatex", "-interaction=nonstopmode", "main.tex"],
                           cwd=TEX_DIR, capture_output=True, encoding="utf-8", errors="replace")
        if q.returncode != 0 or not os.path.exists(os.path.join(TEX_DIR, "main.pdf")):
            print("[compile-failed]", q.stdout[-600:], q.stderr[-400:])
            sys.exit(1)
        print("[compile-ok]", os.path.join(TEX_DIR, "main.pdf"))


if __name__ == "__main__":
    main()
