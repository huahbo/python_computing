#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build the full book (and single-chapter pilot) from chapters/*.md via pandoc+xelatex.

Usage:
  python build/texbook.py --chapter 01-numpy   # one chapter pilot
  python build/texbook.py --all                # full book (default)
  python build/texbook.py --check              # report chapters needing rebuild
  python build/texbook.py --full              # ignore cache
"""
import os, sys, json, re, shutil, tempfile, hashlib, subprocess
import yaml
from pypdf import PdfReader
import fonts

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))   # docs/
CHAPTERS = os.path.join(ROOT, "chapters")
OUT_DIR = os.path.join(ROOT, "教材PDF")
PILOT_DIR = os.path.join(OUT_DIR, "_pilot")
CACHE = os.path.join(ROOT, "build", ".texbook_cache.json")
BOOK_OUT = os.path.join(OUT_DIR, "Python科学计算_全书.pdf")
APPENDIX_OUT = os.path.join(OUT_DIR, "数学与算法补充.pdf")

PANDOC_OPTS = [
    "--pdf-engine=xelatex",
    *fonts.PANDOC_FONT_OPTS,
    "-V", "geometry:margin=2.2cm",
    "-V", "colorlinks=true",
    "-V", "linkcolor=blue",
    "--toc",
    "--toc-depth=2",
    "-V", "toc-title=目录",
    "--highlight-style=tango",
    "--include-in-header=" + os.path.join(ROOT, "build", "texbook_header.tex"),
    "--resource-path=" + ROOT,
]


def load_cfg():
    with open(os.path.join(ROOT, "build", "book.yaml"), encoding="utf-8") as f:
        return yaml.safe_load(f)


def read_manifest_dir(mdir):
    """从任意目录读 pdf_manifest.txt（章 / 附录通用）。"""
    p = os.path.join(mdir, "pdf_manifest.txt")
    title, files = os.path.basename(mdir), []
    with open(p, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if line.upper().startswith("TITLE:"):
                title = line.split(":", 1)[1].strip()
            else:
                files.append(line)
    return title, files


def read_manifest_dir(mdir):
    """从任意目录读 pdf_manifest.txt（章 / 附录通用）。"""
    p = os.path.join(mdir, "pdf_manifest.txt")
    title, files = os.path.basename(mdir), []
    with open(p, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if line.upper().startswith("TITLE:"):
                title = line.split(":", 1)[1].strip()
            else:
                files.append(line)
    return title, files


def read_manifest(ch):
    return read_manifest_dir(os.path.join(CHAPTERS, ch))


def md_hash(paths):
    h = hashlib.sha256()
    for p in paths:
        with open(p, "rb") as f:
            h.update(f.read())
    return h.hexdigest()


def shift_heading(text):
    """把节文件内所有标题上移一级：# -> ##, ## -> ### ..."""
    out = []
    for line in text.split("\n"):
        m = re.match(r"^(#{1,6})\s", line)
        if m:
            line = "#" * (len(m.group(1)) + 1) + line[len(m.group(1)):]
        out.append(line)
    return "\n".join(out)


def chapter_md(ch, cfg):
    title, files = read_manifest(ch)
    parts = [f"# {title}", ""]
    for rel in files:
        if rel.lower() in ("README.md", "readme.md"):
            continue  # 章首页是站点索引，不进入书正文
        src = os.path.join(CHAPTERS, ch, rel)
        if not os.path.isfile(src):
            print(f"[warn] missing {src}")
            continue
        with open(src, encoding="utf-8") as f:
            text = f.read()
        text = shift_heading(text)
        # 图片路径改写为相对 docs 根，配合 --resource-path
        text = text.replace("](./images/", f"](./chapters/{ch}/images/")
        text = text.replace("](../images/", f"](../chapters/{ch}/images/")
        text = text.replace("](images/", f"](chapters/{ch}/images/")
        parts.append(text.strip() + "\n\n")
    return "\n\n".join(parts)


def appendix_md_for_dir(rel_dir):
    """把某个附录目录下的 md 原样拼接（不升标题；文件内 # 即一级标题）。"""
    appdir = os.path.join(ROOT, rel_dir)
    title, files = read_manifest_dir(appdir)
    parts = []
    for rel in files:
        if rel.lower() in ("README.md", "readme.md"):
            continue
        src = os.path.join(appdir, rel)
        if not os.path.isfile(src):
            print("[warn] missing", src)
            continue
        with open(src, encoding="utf-8") as f:
            parts.append(f.read().strip())
    return "\n\n".join(parts)


def build_appendix_pdf():
    cfg = load_cfg()
    ads = cfg.get("appendices") or []
    if not ads:
        print("[skip] no appendices configured")
        return True
    parts = []
    for ad in ads:
        parts.append(appendix_md_for_dir(ad["dir"]))
    md = "```{=latex}\n\\appendix\n```\n\n" + "\n\n\\newpage\n\n".join(parts)
    tmp = os.path.join(ROOT, "build", "_tmp_appendix.md")
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(md)
    ok = run_pandoc(tmp, APPENDIX_OUT, title=cfg.get("appendix_title", "数学与算法补充"))
    os.remove(tmp)
    if not ok:
        return False
    r = PdfReader(APPENDIX_OUT)
    print(f"[done] APPENDIX -> {APPENDIX_OUT} ({len(r.pages)} pages)")
    return True


def appendix_md_for_dir(rel_dir):
    """把某个附录目录下的 md 原样拼接（不升标题；文件内 # 即一级标题）。"""
    appdir = os.path.join(ROOT, rel_dir)
    title, files = read_manifest_dir(appdir)
    parts = []
    for rel in files:
        if rel.lower() in ("README.md", "readme.md"):
            continue
        src = os.path.join(appdir, rel)
        if not os.path.isfile(src):
            print("[warn] missing", src)
            continue
        with open(src, encoding="utf-8") as f:
            parts.append(f.read().strip())
    return "\n\n".join(parts)


def build_appendix_pdf():
    cfg = load_cfg()
    ads = cfg.get("appendices") or []
    if not ads:
        print("[skip] no appendices configured")
        return True
    parts = []
    for ad in ads:
        parts.append(appendix_md_for_dir(ad["dir"]))
    md = "```{=latex}\n\\appendix\n```\n\n" + "\n\n\\newpage\n\n".join(parts)
    tmp = os.path.join(ROOT, "build", "_tmp_appendix.md")
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(md)
    ok = run_pandoc(tmp, APPENDIX_OUT, title=cfg.get("appendix_title", "数学与算法补充"))
    os.remove(tmp)
    if not ok:
        return False
    r = PdfReader(APPENDIX_OUT)
    print(f"[done] APPENDIX -> {APPENDIX_OUT} ({len(r.pages)} pages)")
    return True


def run_pandoc(md_path, out_pdf, title=None):
    cmd = ["pandoc", md_path, "-o", out_pdf] + PANDOC_OPTS
    if title:
        cmd += ["-V", f"title={title}"]
    proc = subprocess.run(cmd, capture_output=True, text=True,
                          encoding="utf-8", errors="replace")
    warn = 0
    for key in ("Missing character", "Missing $", "Error producing PDF",
                "Could not fetch resource", "replacing image"):
        warn += proc.stderr.count(key)
    if proc.returncode != 0:
        print("[error] pandoc failed:", proc.stderr[-1200:])
        return False
    if warn:
        print(f"[warn] pandoc warnings: {warn} occurrences")
        for line in proc.stderr.splitlines():
            if any(k in line for k in ("Missing character", "Missing $",
                                       "Could not fetch", "replacing image",
                                       "Error producing")):
                print("   ", line[:160])
    return True


def build_one(ch, out_pdf):
    cfg = load_cfg()
    md = chapter_md(ch, cfg)
    tmp = os.path.join(ROOT, "build", "_tmp_book.md")
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(md)
    title, _ = read_manifest(ch)
    ok = run_pandoc(tmp, out_pdf, title="第 " + str(int(ch[:2])) + " 章 · " + title)
    os.remove(tmp)
    if not ok:
        return False
    r = PdfReader(out_pdf)
    print(f"[done] {ch} -> {out_pdf} ({len(r.pages)} pages)")
    return True


def build_book(full=False):
    cfg = load_cfg()
    chapters = cfg["chapters"]
    cache = {}
    if os.path.exists(CACHE):
        with open(CACHE, encoding="utf-8") as f:
            cache = json.load(f)
    parts = []
    changed = []
    for ch in chapters:
        title, files = read_manifest(ch)
        srcs = [os.path.join(CHAPTERS, ch, f) for f in files if os.path.exists(os.path.join(CHAPTERS, ch, f))]
        h = md_hash(srcs)
        if not full and cache.get(ch) == h and os.path.exists(BOOK_OUT):
            print(f"[up-to-date] {ch}")
        else:
            changed.append(ch)
        parts.append(chapter_md(ch, cfg))
        cache[ch] = h
    # 附录：appendix 后原样拼接（数学与算法补充）
    app_parts = []
    for ad in cfg.get("appendices") or []:
        appdir = os.path.join(ROOT, ad["dir"])
        srcs = []
        _, files = read_manifest_dir(appdir)
        for rel in files:
            if rel.lower() in ("README.md", "readme.md"):
                continue
            p = os.path.join(appdir, rel)
            if os.path.isfile(p):
                srcs.append(p)
        h = md_hash(srcs)
        if not full and cache.get("__app__" + ad["dir"]) == h and os.path.exists(BOOK_OUT):
            print("[up-to-date] appendix", ad["dir"])
        else:
            changed.append(ad["dir"])
        app_parts.append(appendix_md_for_dir(ad["dir"]))
        cache["__app__" + ad["dir"]] = h
    if app_parts:
        parts.append("```{=latex}\n\\appendix\n```")
        parts.extend(app_parts)
    body = "\n\n\\newpage\n\n".join(parts)
    tmp = os.path.join(ROOT, "build", "_tmp_book_all.md")
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(body)
    ok = run_pandoc(tmp, BOOK_OUT, title=cfg.get("title", "Python 科学计算"))
    os.remove(tmp)
    if not ok:
        return False
    with open(CACHE, "w", encoding="utf-8") as f:
        json.dump(cache, f, ensure_ascii=False, indent=1)
    r = PdfReader(BOOK_OUT)
    print(f"[done] BOOK -> {BOOK_OUT} ({len(r.pages)} pages; rebuilt {len(changed)} chapters)")
    return True


def check_only():
    cfg = load_cfg()
    cache = {}
    if os.path.exists(CACHE):
        with open(CACHE, encoding="utf-8") as f:
            cache = json.load(f)
    stale = []
    for ch in cfg["chapters"]:
        title, files = read_manifest(ch)
        srcs = [os.path.join(CHAPTERS, ch, f) for f in files]
        srcs = [p for p in srcs if os.path.exists(p)]
        if cache.get(ch) != md_hash(srcs):
            stale.append(ch)
    print("stale chapters:", stale if stale else "none")


def main():
    args = sys.argv[1:]
    os.makedirs(OUT_DIR, exist_ok=True)
    os.makedirs(PILOT_DIR, exist_ok=True)
    if "--check" in args:
        check_only(); return
    if "--chapter" in args:
        ch = args[args.index("--chapter") + 1]
        out = os.path.join(PILOT_DIR, f"{ch}-pilot.pdf")
        ok = build_one(ch, out)
        sys.exit(0 if ok else 1)
    ok = build_book(full="--full" in args)
    if ok:
        ok = build_appendix_pdf()
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()