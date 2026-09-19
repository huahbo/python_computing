# -*- coding: utf-8 -*-
"""Cross-check the book indexes: sidebar / book.yaml parts / chapter dirs / manifests / PDF table.

Usage: python build/check_indexes.py
"""
import io, os, re, sys, glob
import yaml
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CH = os.path.join(ROOT, "chapters")
PDF_DIR = os.path.join(ROOT, "教材PDF")
errors, warns = [], []

def read(p):
    return io.open(p, encoding="utf-8").read()

def main():
    cfg = yaml.safe_load(read(os.path.join(ROOT, "build", "book.yaml")))
    chapters = cfg.get("chapters") or []
    parts = cfg.get("parts") or []
    dirs = sorted(d for d in os.listdir(CH)
                  if os.path.isdir(os.path.join(CH, d))
                  and os.path.exists(os.path.join(CH, d, "pdf_manifest.txt")))
    # 1) book.yaml vs actual chapter dirs
    for d in dirs:
        if d not in chapters:
            errors.append("chapter dir not in book.yaml: " + d)
    for c in chapters:
        if c not in dirs:
            errors.append("book.yaml chapter has no dir/manifest: " + c)
    # 2) parts coverage
    seen = []
    for part in parts:
        for c in (part.get("chapters") or []):
            if c not in chapters:
                errors.append("part lists unknown chapter: " + c)
            seen.append(c)
    for c in chapters:
        if parts and c not in seen:
            errors.append("chapter not covered by any part: " + c)
    dup = [c for c in set(seen) if seen.count(c) > 1]
    for c in dup:
        errors.append("chapter listed in multiple parts: " + c)
    # 3) sidebar coverage
    sb = read(os.path.join(ROOT, "_sidebar.md"))
    for c in chapters:
        if ("chapters/" + c + "/") not in sb:
            errors.append("chapter not in _sidebar.md: " + c)
    # 4) manifest entries exist
    for c in dirs:
        mf = os.path.join(CH, c, "pdf_manifest.txt")
        for line in read(mf).splitlines():
            line = line.strip()
            if not line or line.startswith("#") or line.upper().startswith("TITLE:"):
                continue
            if not os.path.exists(os.path.join(CH, c, line)):
                errors.append("manifest missing file: " + c + "/" + line)
    # 5) 教材PDF/README table vs real files
    tbl = os.path.join(PDF_DIR, "README.md")
    if os.path.exists(tbl):
        text = read(tbl)
        BT = chr(96)
        pat = BT + "([^" + BT + "]+" + chr(92) + ".pdf)" + BT
        for name in re.findall(pat, text):
            if not os.path.exists(os.path.join(PDF_DIR, name)):
                warns.append("教材PDF/README.md mentions missing file: " + name)
    # 6) chapter PDFs present (warning only until built)
    for c in chapters:
        if not glob.glob(os.path.join(PDF_DIR, c + "-*.pdf")):
            warns.append("no chapter PDF yet for: " + c)
    print("indexes: chapters=%d parts=%d sidebar_hits=%d" % (len(chapters), len(parts), len(chapters)))
    for w in warns:
        print("  [warn]", w)
    for e in errors:
        print("  [ERR]", e)
    print("check_indexes: %d error(s), %d warning(s)" % (len(errors), len(warns)))
    return 1 if errors else 0

if __name__ == "__main__":
    sys.exit(main())
