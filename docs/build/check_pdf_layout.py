# -*- coding: utf-8 -*-
"""PDF layout self-check: image overflow beyond page edges + text lines past the right margin.

Usage:
  python build/check_pdf_layout.py            # check every PDF under 教材PDF/
  python build/check_pdf_layout.py --basics   # only chapter PDFs
  python build/check_pdf_layout.py --book     # only 全书 + 部分合并 + 附录

Exit code 1 when a page has an overflowing image, or a text line overshoots the right text
edge by more than HARD_TOL pt while containing ASCII (i.e. a real token overflow).
CJK punctuation hanging (xeCJK 标点悬挂) is reported as [hang] info only and never fails.
"""
import glob, os, re, sys
import fitz

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PDF_DIR = os.path.join(ROOT, "教材PDF")
MARGIN = 62.0        # geometry:margin=2.2cm (pt)
EDGE_TOL = 10.0      # images closer than this to a page edge are suspicious
HARD_TOL = 10.0      # real overflow threshold (pt)
SOFT_TOL = 3.0       # report threshold (pt)
ASCII = re.compile(r"[A-Za-z0-9_/.#\\-]")
HANG = "，。、；：？！）》】”’…—·"

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")


def classify(text, over):
    t = text.rstrip()
    if not t:
        return "hang"
    if not ASCII.search(t) and len(t.strip()) <= 3:
        return "hang"          # punctuation-only tail (hanging punctuation)
    if t and t[-1] in HANG and over <= 8.0:
        return "hang"
    return "hard" if over > HARD_TOL else ("soft" if over > SOFT_TOL else "hang")


def check_pdf(path):
    doc = fitz.open(path)
    bad_img, hard, soft = [], [], []
    for i, page in enumerate(doc):
        r = page.rect
        for im in page.get_images(full=True):
            try:
                rects = page.get_image_rects(im[0])
            except Exception:
                rects = []
            for rc in rects:
                if rc.y1 > r.y1 - EDGE_TOL or rc.y0 < EDGE_TOL or rc.x1 > r.x1 - EDGE_TOL or rc.x0 < EDGE_TOL:
                    bad_img.append((i + 1, round(rc.x0), round(rc.y0), round(rc.x1), round(rc.y1)))
        right_edge = r.x1 - MARGIN
        d = page.get_text("dict")
        for blk in d.get("blocks", []):
            if blk.get("type") != 0:
                continue
            for line in blk.get("lines", []):
                for span in line.get("spans", []):
                    over = span["bbox"][2] - right_edge
                    if over <= SOFT_TOL:
                        continue
                    kind = classify(span.get("text", ""), over)
                    item = (i + 1, round(over, 1), span.get("text", "")[:44])
                    if kind == "hard":
                        hard.append(item)
                    elif kind == "soft":
                        soft.append(item)
    return doc.page_count, bad_img, hard, soft


def main():
    args = sys.argv[1:]
    if "--basics" in args:
        pdfs = sorted(glob.glob(os.path.join(PDF_DIR, "0*-*.pdf"))) + sorted(glob.glob(os.path.join(PDF_DIR, "1*-*.pdf")))
    elif "--book" in args:
        pdfs = [os.path.join(PDF_DIR, "Python科学计算_全书.pdf"),
                os.path.join(PDF_DIR, "数学与算法补充.pdf")] + sorted(glob.glob(os.path.join(PDF_DIR, "第二部分*.pdf")))
    else:
        pdfs = sorted(glob.glob(os.path.join(PDF_DIR, "*.pdf")))
    errors = 0
    for p in pdfs:
        if not os.path.exists(p):
            continue
        pages, bad_img, hard, soft = check_pdf(p)
        name = os.path.basename(p)[:44]
        status = "OK" if not (bad_img or hard) else "PROBLEM"
        print("%-44s pages=%3d  overflow_img=%2d  hard=%2d  soft=%2d  [%s]" % (name, pages, len(bad_img), len(hard), len(soft), status))
        for it in bad_img[:3]:
            print("      img  page %d bbox=%s" % (it[0], it[1:]))
        for it in hard[:3]:
            print("      hard page %d  +%.1fpt  %s" % it)
        for it in soft[:2]:
            print("      soft page %d  +%.1fpt  %s" % it)
        if bad_img or hard:
            errors += 1
    print("check_pdf_layout: %d file(s) with layout problems" % errors)
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
