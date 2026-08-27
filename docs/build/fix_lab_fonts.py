# -*- coding: utf-8 -*-
"""Uniformly inject Chinese-font rcParams into plotting cells of every lab.ipynb."""
import os, json, glob

FONT_LINES = [
    'import matplotlib.pyplot as plt\n',
    'plt.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei", "DejaVu Sans"]\n',
    'plt.rcParams["axes.unicode_minus"] = False\n',
]

def src_of(cell):
    return "".join(cell.get("source", []))

def needs_font(src):
    if "font.sans-serif" in src or "Microsoft YaHei" in src or "SimHei" in src:
        return False
    keys = ["plt.", "matplotlib", "sns.", "imshow", "savefig", "figure("]
    return any(k in src for k in keys)

def main():
    changed = 0
    for nb_path in sorted(glob.glob(os.path.join("chapters", "*", "lab", "lab.ipynb"))):
        nb = json.load(open(nb_path, encoding="utf-8"))
        cnt = 0
        for cell in nb["cells"]:
            if cell["cell_type"] != "code":
                continue
            src = src_of(cell)
            if needs_font(src):
                cell["source"] = FONT_LINES + list(cell.get("source", []))
                cnt += 1
        if cnt:
            with open(nb_path, "w", encoding="utf-8") as f:
                json.dump(nb, f, ensure_ascii=False, indent=1)
            changed += 1
            print(f"[patched] {nb_path}  ({cnt} cells)")
        else:
            print(f"[ok]      {nb_path}  (already fine)")
    print("notebooks patched:", changed)

if __name__ == "__main__":
    main()
