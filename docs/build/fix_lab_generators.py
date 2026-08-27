# -*- coding: utf-8 -*-
"""Fix the broken font-injection block in every build/make_chapN_lab.py."""
import glob, io, re

START = "    # 统一为中文字体设置"
END = '] + list(_c.get("source", []))'

NEW_BLOCK = """    # 统一为中文字体设置（所有绘图单元注入微软雅黑）
    NL = chr(10)
    for _c in nb["cells"]:
        if _c["cell_type"] == "code":
            _src = "".join(_c.get("source", []))
            if (("plt." in _src) or ("sns." in _src) or ("matplotlib" in _src)
                    or ("savefig" in _src)) and ("font.sans-serif" not in _src):
                _c["source"] = [
                    "import matplotlib.pyplot as plt" + NL,
                    'plt.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei", "DejaVu Sans"]' + NL,
                    'plt.rcParams["axes.unicode_minus"] = False' + NL,
                ] + list(_c.get("source", []))
"""

pat = re.compile(re.escape(START) + r".*?" + re.escape(END), re.S)

for path in sorted(glob.glob("build/make_chap*_lab.py")):
    with io.open(path, encoding="utf-8") as f:
        text = f.read()
    if not pat.search(text):
        print("[skip] no broken block in", path)
        continue
    text = pat.sub(lambda m: NEW_BLOCK.rstrip("\n"), text, count=1)
    with io.open(path, "w", encoding="utf-8") as f:
        f.write(text)
    print("[fixed]", path)
