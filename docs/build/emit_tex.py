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
import fonts

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
    # 附录：appendix 原样块 + A~F
    app_parts = []
    for ad in cfg.get("appendices") or []:
        appdir = os.path.join(ROOT, ad["dir"])
        _, files = tb.read_manifest_dir(appdir)
        for rel in files:
            if rel.lower() in ("README.md", "readme.md"):
                continue
            src = os.path.join(appdir, rel)
            if not os.path.isfile(src):
                continue
            with open(src, encoding="utf-8") as f:
                app_parts.append(f.read().strip())
    if app_parts:
        parts.append("```{=latex}\n\\appendix\n```")
        parts.append("\n\n".join(app_parts))
    return "\n\n\\newpage\n\n".join(parts)


def copy_figures(ch):
    src, dst = os.path.join(CHAPTERS_DIR, ch, "images"), os.path.join(FIGS_DIR, ch)
    if os.path.isdir(src):
        os.makedirs(dst, exist_ok=True)
        for f in os.listdir(src):
            shutil.copy2(os.path.join(src, f), os.path.join(dst, f))


def split_chapters(tex, chapters, appendix_names=None):
    """Split the standalone tex body at chapter boundaries -> chapter files.
    Returns (main_tex, chapter_chunks, appendix_chunks)."""
    bd = tex.index("\\begin{document}")
    ed = tex.index("\\end{document}")
    preamble = tex[:bd] + "\\begin{document}\n"
    body = tex[bd + len("\\begin{document}"):ed]
    appendix_names = appendix_names or []
    if appendix_names:
        marker = "\\appendix"
        app_idx = body.find(marker)
        if app_idx == -1:
            raise RuntimeError("appendix marker not found in standalone tex body")
        chapter_body = body[:app_idx]
        appendix_body = body[app_idx + len(marker):]
        pos_c = [m.start() for m in re.finditer(r"\\chapter\{", chapter_body)]
        if len(pos_c) != len(chapters):
            raise RuntimeError(f"chapter count mismatch: tex={len(pos_c)} cfg={len(chapters)}")
        chunks_c = []
        for i, p in enumerate(pos_c):
            end = pos_c[i + 1] if i + 1 < len(pos_c) else len(chapter_body)
            chunks_c.append(chapter_body[p:end].rstrip() + "\n")
        pos_a = [m.start() for m in re.finditer(r"\\chapter\{", appendix_body)]
        if len(pos_a) != len(appendix_names):
            raise RuntimeError(f"appendix count mismatch: tex={len(pos_a)} cfg={len(appendix_names)}")
        chunks_a = []
        for i, p in enumerate(pos_a):
            end = pos_a[i + 1] if i + 1 < len(pos_a) else len(appendix_body)
            chunks_a.append(appendix_body[p:end].rstrip() + "\n")
        chapter_inputs = "\n".join(["\\input{chapters/ch" + ch + ".tex}" for ch in chapters])
        appendix_inputs = "\n".join(["\\input{chapters/chapp-" + n + ".tex}" for n in appendix_names])
        main = preamble + chapter_inputs + "\n\\appendix\n" + appendix_inputs + "\n\\end{document}\n"
        return main, chunks_c, chunks_a
    pos = [m.start() for m in re.finditer(r"\\chapter\{", body)]
    if len(pos) != len(chapters):
        raise RuntimeError(f"chapter count mismatch: tex={len(pos)} cfg={len(chapters)}")
    chunks = []
    for i, p in enumerate(pos):
        end = pos[i + 1] if i + 1 < len(pos) else len(body)
        chunks.append(body[p:end].rstrip() + "\n")
    main_body = "\n".join(["\\input{chapters/ch" + ch + ".tex}\n" for ch in chapters])
    main = preamble + main_body + "\n\\end{document}\n"
    return main, chunks, []


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
    appendix_names = []
    for ad in cfg.get("appendices") or []:
        appdir = os.path.join(ROOT, ad["dir"])
        _, files = tb.read_manifest_dir(appdir)
        for rel in files:
            if rel.lower() in ("README.md", "readme.md"):
                continue
            appendix_names.append(os.path.splitext(rel)[0])
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
           *fonts.PANDOC_FONT_OPTS,
           "-V", "geometry:margin=2.2cm",
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
    main_tex, chunks, app_chunks = split_chapters(tex, chapters, appendix_names)

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

    # 3b) appendix chapter files
    for name, chunk in zip(appendix_names, app_chunks):
        out = os.path.join(CHAP_TEX_DIR, f"chapp-{name}.tex")
        write(out, chunk)
        print(f"[gen] chapters/chapp-{name}.tex")

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