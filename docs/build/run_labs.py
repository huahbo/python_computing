# -*- coding: utf-8 -*-
"""Execute all code cells of every chapters/NN-xxx/lab/lab.ipynb.

Usage: python build/run_labs.py [chapter-substring]
"""
import os, sys, json, glob, io, contextlib

# 强制非交互后端，避免 plt.show() 在无界面环境阻塞
import matplotlib
matplotlib.use("Agg")

ROOT = os.getcwd()
CHAPTERS = os.path.join(ROOT, "chapters")


def run_notebook(path):
    nb = json.load(open(path, encoding="utf-8"))
    g = {"__name__": "__main__"}
    buf = io.StringIO()
    n = 0
    with contextlib.redirect_stdout(buf):
        for i, cell in enumerate(nb["cells"]):
            if cell["cell_type"] != "code":
                continue
            src = "".join(cell["source"])
            n += 1
            try:
                exec(compile(src, f"<{os.path.basename(path)}:{i}>", "exec"), g)
            except Exception as e:
                return False, f"cell {i} ({type(e).__name__}): {e}", n
    return True, "ok", n


def main():
    sub = sys.argv[1] if len(sys.argv) > 1 else ""
    labs = sorted(p for p in glob.glob(os.path.join(CHAPTERS, "*", "lab", "lab.ipynb"))
                  if sub in p)
    cnt = 0
    for p in labs:
        ok, msg, n = run_notebook(p)
        rel = os.path.relpath(p)
        print(f"[{'OK' if ok else 'FAIL'}] {rel}  code cells={n}  {msg if not ok else ''}")
        cnt += 1 if ok else 0
    print(f"passed {cnt}/{len(labs)} labs")
    return 0 if cnt == len(labs) else 1

if __name__ == "__main__":
    raise SystemExit(main())
