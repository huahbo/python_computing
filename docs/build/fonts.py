# -*- coding: utf-8 -*-
"""Cross-platform font selection for pandoc/xelatex builds (Windows / Linux CI).

Windows: Microsoft YaHei + Consolas (local default).
Linux (GitHub Actions): pick installed Noto CJK families via fc-list,
fallback to DejaVu Sans / DejaVu Sans Mono if Noto not found.
"""
import os, shutil, subprocess, sys


def _families():
    if not shutil.which("fc-list"):
        return set()
    try:
        out = subprocess.run(["fc-list", ":", "family"],
                             capture_output=True, encoding="utf-8",
                             errors="replace", timeout=20).stdout
    except Exception:
        return set()
    fams = set()
    for line in out.splitlines():
        fams.update(p.strip() for p in line.split(",") if p.strip())
    return fams


def _pick(candidates, fallback):
    fams = _families()
    if fams:
        for c in candidates:
            if c in fams:
                return c
        for c in candidates:
            if any(c.lower() in f.lower() for f in fams):
                return c
    return fallback


_WIN = sys.platform.startswith("win")
MAIN = "Microsoft YaHei" if _WIN else _pick(
    ["Noto Sans CJK SC", "Noto Serif CJK SC"], "DejaVu Sans")
MONO = "Consolas" if _WIN else _pick(
    ["Noto Sans Mono CJK SC", "DejaVu Sans Mono"], "DejaVu Sans Mono")

PANDOC_FONT_OPTS = [
    "-V", "mainfont=" + MAIN,
    "-V", "CJKmainfont=" + MAIN,
    "-V", "monofont=" + MONO,
]
