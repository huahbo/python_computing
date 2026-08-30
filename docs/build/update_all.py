#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""One-command update: validate -> per-chapter PDFs -> full book PDF."""
import os, sys, subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def run(cmd, name):
    print(f"\n===== {name} =====")
    p = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True,
                         encoding="utf-8", errors="replace")
    tail = p.stdout.strip()[-1500:]
    print(tail if tail else "(no stdout)")
    if p.stderr.strip():
        print("--stderr--")
        print(p.stderr.strip()[-800:])
    return p.returncode


def main():
    codes = []
    codes.append(run([sys.executable, "build/validate_book.py"], "1) validate_book (links/notebooks)"))
    codes.append(run([sys.executable, "build/gen_references.py"], "1.5) generate global references (附录 G)"))
    codes.append(run([sys.executable, "build/pdf_build.py"], "2) per-chapter PDFs"))
    codes.append(run([sys.executable, "build/texbook.py", "--full"], "3) full book PDF"))
    if "--tex" in sys.argv:
        cmd = [sys.executable, "build/emit_tex.py"]
        if "--tex-compile" in sys.argv:
            cmd.append("--compile")
        codes.append(run(cmd, "4) editable TeX project" + (" (+compile)" if "--tex-compile" in sys.argv else "")))
    print(f"\nALL DONE  exit_codes={codes}")
    return 0 if all(c == 0 for c in codes) else 1


if __name__ == "__main__":
    sys.exit(main())
