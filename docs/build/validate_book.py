# -*- coding: utf-8 -*-
"""Validate all chapters: manifests, md internal links, ipynb JSON.

Usage: python build/validate_book.py
"""
import os, re, glob, json

ROOT = os.getcwd()
CHAPTERS = os.path.join(ROOT, "chapters")
PATTERN = r'\[([^\]]*)\]\(([^)]+)(?:\s+"[^"]+")?\)'


def check_md_links(md, missing):
    with open(md, encoding="utf-8") as f:
        text = f.read()
    base = os.path.dirname(md)
    for m in re.finditer(PATTERN, text):
        target = m.group(2)
        if target.startswith(("http://", "https://", "#", "mailto:")):
            continue
        full = os.path.normpath(os.path.join(base, target.split("#")[0]))
        if not os.path.exists(full):
            missing.append((md, target))


def main():
    chapters = sorted(d for d in os.listdir(CHAPTERS)
                      if os.path.isdir(os.path.join(CHAPTERS, d)))
    missing, problems, nb_count, lab_count = [], [], 0, 0

    for ch in chapters:
        cdir = os.path.join(CHAPTERS, ch)
        mf = os.path.join(cdir, "pdf_manifest.txt")
        if not os.path.exists(mf):
            problems.append(f"{ch}: missing pdf_manifest.txt")
        else:
            with open(mf, encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if not line or line.startswith("#") or line.upper().startswith("TITLE:"):
                        continue
                    if not os.path.exists(os.path.join(cdir, line)):
                        problems.append(f"{ch}: manifest missing file {line}")
        for md in glob.glob(os.path.join(cdir, "*.md")):
            check_md_links(md, missing)
        for nb in glob.glob(os.path.join(cdir, "**", "*.ipynb"), recursive=True):
            try:
                json.load(open(nb, encoding="utf-8"))
                nb_count += 1
            except Exception as e:
                problems.append(f"{ch}: bad notebook {nb}: {e}")
        if os.path.exists(os.path.join(cdir, "lab", "lab.ipynb")):
            lab_count += 1

    for md in ["README.md", "绪论.md", "0-学习指南.md", "_sidebar.md",
               "教学资源/README.md", "原始资料/说明.md"]:
        check_md_links(md, missing)

    print(f"chapters: {len(chapters)}  notebooks ok: {nb_count}  labs: {lab_count}")
    print(f"missing internal links: {len(missing)}")
    for md, t in missing[:30]:
        print("  ", md, "->", t)
    print(f"problems: {len(problems)}")
    for p in problems[:30]:
        print("  ", p)
    return 0 if (not missing and not problems) else 1

if __name__ == "__main__":
    raise SystemExit(main())
