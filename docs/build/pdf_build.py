#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build chapter PDFs from markdown sources in chapters/NN-xxx/.

Usage:
    python build/pdf_build.py                 # build all chapters having pdf_manifest.txt
    python build/pdf_build.py 01-numpy        # build one chapter
    python build/pdf_build.py --list          # list chapters with manifests

Requires: pandoc + xelatex (TeX Live) for md->pdf, pypdf for merging.
Output: docs/教材PDF/<序号>-<标题>.pdf
"""
import os
import sys
import shutil
import subprocess
import tempfile

from pypdf import PdfReader, PdfWriter
import fonts

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # docs/
CHAPTERS_DIR = os.path.join(ROOT, "chapters")
OUT_DIR = os.path.join(ROOT, "教材PDF")

PANDOC_OPTS = [
    "--pdf-engine=xelatex",
    *fonts.PANDOC_FONT_OPTS,
    "-V", "geometry:margin=2.2cm",
    "-V", "colorlinks=true",
    "-V", "linkcolor=blue",
]


def list_chapters():
    if not os.path.isdir(CHAPTERS_DIR):
        return []
    out = []
    for d in sorted(os.listdir(CHAPTERS_DIR)):
        p = os.path.join(CHAPTERS_DIR, d)
        if os.path.isdir(p) and os.path.exists(os.path.join(p, "pdf_manifest.txt")):
            out.append(d)
    return out


def read_manifest(chapter):
    path = os.path.join(CHAPTERS_DIR, chapter, "pdf_manifest.txt")
    title = chapter
    files = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if line.upper().startswith("TITLE:"):
                title = line.split(":", 1)[1].strip()
                continue
            files.append(line)
    return title, files


def md_to_pdf(md_path, out_pdf):
    resource_dir = os.path.dirname(os.path.abspath(md_path))
    cmd = (["pandoc", md_path, "-o", out_pdf,
            "--resource-path=" + resource_dir] + PANDOC_OPTS)
    subprocess.run(cmd, check=True)


def merge_pdfs(parts, out_path):
    writer = PdfWriter()
    total = 0
    for part in parts:
        reader = PdfReader(part)
        for page in reader.pages:
            writer.add_page(page)
        total += len(reader.pages)
    with open(out_path, "wb") as f:
        writer.write(f)
    return total


def build_chapter(chapter):
    title, manifest = read_manifest(chapter)
    if not manifest:
        print(f"[skip] {chapter}: pdf_manifest.txt is empty")
        return None

    tmp = tempfile.mkdtemp(prefix="pdfbuild_")
    try:
        parts = []
        for rel in manifest:
            src = os.path.join(CHAPTERS_DIR, chapter, rel)
            if not os.path.isfile(src):
                print(f"[warn] missing source: {src}")
                continue
            name = os.path.splitext(os.path.basename(src))[0] + ".pdf"
            part = os.path.join(tmp, name)
            print(f"[pandoc] {chapter}/{rel} -> {name}")
            md_to_pdf(src, part)
            parts.append(part)

        if not parts:
            print(f"[skip] {chapter}: nothing converted")
            return None

        os.makedirs(OUT_DIR, exist_ok=True)
        out_path = os.path.join(OUT_DIR, f"{chapter}-{title}.pdf")
        total = merge_pdfs(parts, out_path)

        # validation: output page count == sum of part page counts
        reader = PdfReader(out_path)
        if len(reader.pages) != total:
            print(f"[error] {chapter}: page count mismatch "
                  f"({len(reader.pages)} vs {total})")
            return None
        print(f"[done] {chapter} -> {out_path} "
              f"({total} pages, {len(parts)} sections)")
        return out_path
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def main():
    args = sys.argv[1:]
    if args and args[0] == "--list":
        for ch in list_chapters():
            title, files = read_manifest(ch)
            print(f"{ch}: {title} ({len(files)} files)")
        return

    chapters = list_chapters()
    if args:
        chapters = [a for a in args if a in chapters]
    if not chapters:
        print("No chapters with pdf_manifest.txt found (or wrong argument).")
        print("Try: python build/pdf_build.py --list")
        return

    for ch in chapters:
        try:
            build_chapter(ch)
        except Exception as e:
            print(f"[error] {ch}: {type(e).__name__}: {e}")


if __name__ == "__main__":
    main()
