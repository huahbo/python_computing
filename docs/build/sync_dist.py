# -*- coding: utf-8 -*-
"""Sync generated PDFs from docs/教材PDF to a fixed local distribution folder.

Usage:
  python build/sync_dist.py                 # -> D:\\Scientific_Computing_Class\\course-dist
  python build/sync_dist.py D:/some/dir     # custom destination
"""
import os, shutil, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))   # docs/
SRC = os.path.join(ROOT, "教材PDF")
DST = sys.argv[1] if len(sys.argv) > 1 else r"D:\Scientific_Computing_Class\course-dist"


def main():
    if not os.path.isdir(SRC):
        print("[error] source not found:", SRC)
        return 1
    os.makedirs(DST, exist_ok=True)
    n = 0
    for name in sorted(os.listdir(SRC)):
        src = os.path.join(SRC, name)
        if os.path.isfile(src):
            shutil.copy2(src, os.path.join(DST, name))
            n += 1
        elif os.path.isdir(src):
            dst = os.path.join(DST, name)
            shutil.copytree(src, dst, dirs_exist_ok=True)
            n += 1
    print(f"[done] synced {n} items to {DST}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
