# -*- coding: utf-8 -*-
"""Merge each part's chapter PDFs into one part PDF with a generated cover page.

Usage: python build/part_pdf.py
"""
import glob, os, subprocess, sys, tempfile
import yaml
from pypdf import PdfReader, PdfWriter
import pdf_build as pb
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PDF_DIR = os.path.join(ROOT, "教材PDF")
BS = chr(92)

def load_cfg():
    with open(os.path.join(ROOT, "build", "book.yaml"), encoding="utf-8") as f:
        return yaml.safe_load(f)

def chapter_pdf(ch):
    hits = sorted(glob.glob(os.path.join(PDF_DIR, ch + "-*.pdf")))
    return hits[0] if hits else None

def make_cover(title, out_pdf, tmpdir):
    md = os.path.join(tmpdir, "_part_cover.md")
    tex = ("```{=latex}" + chr(10) +
           BS + "thispagestyle{empty}" + chr(10) +
           BS + "vspace*{4cm}" + chr(10) +
           BS + "begin{center}" + chr(10) +
           BS + "Huge" + BS + "bfseries " + title + chr(10) +
           BS + "end{center}" + chr(10) +
           BS + "clearpage" + chr(10) + "```" + chr(10))
    with open(md, "w", encoding="utf-8") as f:
        f.write(tex)
    subprocess.run(["pandoc", md, "-o", out_pdf] + pb.PANDOC_OPTS, check=True)
    return out_pdf

def merge(paths, out_path):
    w = PdfWriter()
    total = 0
    for p in paths:
        r = PdfReader(p)
        for page in r.pages:
            w.add_page(page)
        total += len(r.pages)
    with open(out_path, "wb") as f:
        w.write(f)
    return total

def main():
    cfg = load_cfg()
    parts = cfg.get("parts") or []
    if not parts:
        print("[skip] no parts configured")
        return 0
    tmpdir = tempfile.mkdtemp(prefix="partpdf_")
    for part in parts:
        chs = part.get("chapters") or []
        outname = part.get("file")
        if not outname or len(chs) < 2:
            continue
        pdfs, missing = [], []
        for ch in chs:
            p = chapter_pdf(ch)
            if p:
                pdfs.append(p)
            else:
                missing.append(ch)
        if missing:
            print("[warn] missing chapter PDFs for", outname, missing)
            continue
        out = os.path.join(PDF_DIR, outname)
        cover = make_cover(part.get("title", "部分"), os.path.join(tmpdir, "_cover.pdf"), tmpdir)
        pages = merge([cover] + pdfs, out)
        print("[done] PART ->", out, "(" + str(pages) + " pages)")
    return 0

if __name__ == "__main__":
    sys.exit(main())
