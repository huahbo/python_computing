# -*- coding: utf-8 -*-
"""Generate Chapter 0 lab notebook + practice data.

Run: python build/make_chap0_lab.py
"""
import json, os, random, csv

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LAB = os.path.join(ROOT, "chapters", "00-prep", "lab")
DATA = os.path.join(LAB, "data")
os.makedirs(DATA, exist_ok=True)

def md(src):
    return {"cell_type": "markdown", "metadata": {}, "source": [s + "\n" for s in src.split("\n")]}

def code(src):
    return {"cell_type": "code", "execution_count": None, "metadata": {},
            "outputs": [], "source": [s + "\n" for s in src.split("\n")]}

# ---------- data ----------
random.seed(2026)
names = ["张三", "李四", "王五", "赵六", "钱七", "孙八", "周九", "吴十",
         "郑一", "冯二", "陈三", "褚四", "卫五", "蒋六", "沈七", "韩八",
         "杨九", "朱十", "秦一", "许二"]
rows = []
for i, n in enumerate(names, 1):
    rows.append({
        "学号": f"2023{i:04d}",
        "姓名": n,
        "Python": random.randint(55, 99),
        "数学": random.randint(52, 98),
        "英语": random.randint(50, 97),
    })
with open(os.path.join(DATA, "scores.csv"), "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
    w.writeheader()
    w.writerows(rows)
print("wrote", os.path.join(DATA, "scores.csv"), len(rows), "rows")

# ---------- notebook ----------
CELLS = []
CELLS.append(md(r"""# 第 0 章 上机实验（lab0）

> 目标：环境自检 + Python 热身 + 数据统计 + 第一份 LaTeX 报告。
> 使用方法：从上到下运行每个单元格；带 “TODO” 的单元格请先填空再运行。
"""))
CELLS.append(code(r"""import os, sys, csv, shutil
print("Python:", sys.version.split()[0])
print("当前目录:", os.getcwd())

BASE = "chapters/00-prep/lab" if os.path.isdir("chapters/00-prep/lab") else "."
DATA = os.path.join(BASE, "data", "scores.csv")
OUT = os.path.join(BASE, "output") if BASE != "." else "output"
os.makedirs(OUT, exist_ok=True)
print("数据文件:", DATA)
print("输出目录:", OUT)
"""))
CELLS.append(md(r"""## Part A：环境自检（0.5h）

依次运行以下单元格，确认 Python 核心库与 LaTeX 工具都在；把输出保存为 `env_check.txt` 提交。
"""))
CELLS.append(code(r"""# A1 核心库检查
import numpy, sympy, scipy, pandas, matplotlib, seaborn, networkx, statsmodels, sklearn
for m in [numpy, sympy, scipy, pandas, matplotlib, seaborn, networkx, statsmodels, sklearn]:
    print(f"OK  {m.__name__:>12}  {m.__version__}")

# A2 LaTeX 工具检查
for tool in ["xelatex", "latexmk", "git"]:
    p = shutil.which(tool)
    print(("OK  " if p else "WARN") + f"  {tool:>10}  {p or '未找到（可选/见讲义）'}")

# A3 保存环境自检输出（在终端命令行执行更完整：python check_env.py）
print("提示：完整自检请在终端运行 python 教学资源/环境配置/check_env.py")
"""))
CELLS.append(md(r"""## Part B：Python 热身（1.5h）

按 00-04 的查漏内容，完成下面的小任务。
"""))
CELLS.append(code(r"""# B1 切片与推导式
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
scores = [68, 91, 55, 76, 88, 73]
print("偶数位:", nums[::2])
print("反转:", nums[::-1])
print("60~89 分:", [round(s) for s in scores if 60 <= s <= 89])
"""))
CELLS.append(code(r"""# B2 字典、zip、函数默认值
names = ["张三", "李四", "王五"]
avgs = [86.3, 78.0, 71.5]
d = dict(zip(names, avgs))
print(d, "→ 王五:", d.get("王五", 0))

def safe_add(a, lst=None):
    lst = [] if lst is None else lst
    lst.append(a)
    return lst

a_list = safe_add(1)
b_list = safe_add(2)
print(a_list, b_list, "互不共享:", a_list is not b_list)

def total(*values):
    return sum(values)
print("total(1, 2, 3) =", total(1, 2, 3))
"""))
CELLS.append(code(r"""# B3 异常与文件读写（写入 output/demo.txt 再读回）
try:
    with open(os.path.join(OUT, "demo.txt"), "w", encoding="utf-8") as f:
        f.write("第一行\n第二行 42\n")
    with open(os.path.join(OUT, "demo.txt"), encoding="utf-8") as f:
        print(f.read())
except FileNotFoundError as e:
    print("目录不存在:", e)

def read_float(path):
    vals = []
    with open(path, encoding="utf-8") as f:
        for i, line in enumerate(f, 1):
            try:
                vals.append(float(line.strip()))
            except ValueError:
                print("跳过第", i, "行")
    return vals

print("demo 数值行:", read_float(os.path.join(OUT, "demo.txt")))
"""))
CELLS.append(md(r"""## Part C：数据统计（1h）

读取 `data/scores.csv`，完成统计并输出 `result.txt` 与一张简图。
"""))
CELLS.append(code(r"""# C1 读取数据与基础统计
assert os.path.exists(DATA), "找不到 scores.csv，请确认把 data/ 放在 lab/ 下"
with open(DATA, encoding="utf-8") as f:
    rows = list(csv.DictReader(f))
print("学生数:", len(rows), "字段:", list(rows[0].keys()))

for r in rows:
    r["Python"] = float(r["Python"])
    r["数学"] = float(r["数学"])
    r["英语"] = float(r["英语"])
    r["总分"] = r["Python"] + r["数学"] + r["英语"]
    r["平均分"] = round(r["总分"] / 3, 1)

ranked = sorted(rows, key=lambda r: r["平均分"], reverse=True)
print("前 3 名:")
for r in ranked[:3]:
    print(" ", r["姓名"], r["平均分"])
print("后 3 名:")
for r in ranked[-3:]:
    print(" ", r["姓名"], r["平均分"])
"""))
CELLS.append(code(r"""# C2 统计结果写入 result.txt
lines = ["== 课程成绩统计 ==", ""]
lines.append(f"人数: {len(rows)}")
for col in ["Python", "数学", "英语"]:
    vals = [r[col] for r in rows]
    lines.append(f"{col} 平均 {sum(vals)/len(vals):.1f}  最高 {max(vals):.0f}  最低 {min(vals):.0f}")
lines.append("")
lines.append("排名前 3：")
for r in ranked[:3]:
    lines.append(f"  {r['姓名']} 平均 {r['平均分']}")
with open(os.path.join(OUT, "result.txt"), "w", encoding="utf-8") as f:
    f.write("\n".join(lines) + "\n")
print("已写入", os.path.join(OUT, "result.txt"))
print(open(os.path.join(OUT, "result.txt"), encoding="utf-8").read())
"""))
CELLS.append(code(r"""# C3 画一张简图（预告第 5 章）
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei", "DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False

names = [r["姓名"] for r in ranked]
avgs = [r["平均分"] for r in ranked]
plt.figure(figsize=(9, 4))
plt.bar(names, avgs)
plt.axhline(60, color="red", linestyle="--", label="及格线 60")
plt.ylabel("平均分"); plt.title("课程平均分分布")
plt.legend()
path = os.path.join(OUT, "avg_scores.png")
plt.savefig(path, dpi=120, bbox_inches="tight")
plt.close()
print("已保存", path)
"""))
CELLS.append(md(r"""## Part D：LaTeX 报告（1h）

用课程模板（`教学资源/LaTeX模板/latex_vscode_template/`）复制成你的报告目录，按 00-07 写报告。下面的单元格会生成一份**最小模板** `output/report_template.tex` 供参考（真正的练习请用课程完整模板）。
"""))
CELLS.append(code(r"""# D1 生成最小 LaTeX 模板供参考
tex = r'''% !TeX program = xelatex
\documentclass{ctexart}
\usepackage{amsmath}
\usepackage{graphicx}
\title{课程成绩统计报告}
\author{你的姓名 学号}
\date{2026 年秋季}
\begin{document}
\maketitle
\section{数据与方法}
数据来自 20 名学生的 3 门课程成绩，使用 Python 统计平均分。
\section{结果}
平均分公式：
\begin{equation}
  \bar{x} = \frac{1}{n}\sum_{i=1}^{n} x_i
\end{equation}
\begin{tabular}{|l|c|}
\hline
姓名 & 平均分 \\
\hline
张三 & 86.3 \\
\hline
\end{tabular}

\begin{figure}[h]
  \centering
  \includegraphics[width=0.6\textwidth]{avg_scores.png}
  \caption{平均分分布}
\end{figure}
\end{document}
'''
with open(os.path.join(OUT, "report_template.tex"), "w", encoding="utf-8") as f:
    f.write(tex)
print("已生成", os.path.join(OUT, "report_template.tex"))
print("下一步：复制 教学资源/LaTeX模板/latex_vscode_template/ 为你的报告目录，改 main.tex 后 latexmk -xelatex main.tex")
"""))
CELLS.append(md(r"""## 提交清单（自检）

- [ ] Part A 环境自检通过，保存 `env_check.txt`
- [ ] Part B 三个热身任务全部能运行
- [ ] Part C 生成 `result.txt` 与 `avg_scores.png`
- [ ] Part D 编译出 PDF 报告
- [ ] 命名：`学号_姓名_第0章_...` 提交

### 汇总
运行下面单元格查看本 lab 生成的产物。
"""))
CELLS.append(code(r"""# 汇总
print("产物列表:")
for root, dirs, files in os.walk(OUT):
    for fn in sorted(files):
        print(" ", os.path.join(root, fn).replace(os.getcwd() + os.sep, ""))
print("完成 lab0：环境 / Python / 数据 / LaTeX 一条龙 ✓")
"""))

nb = {"cells": CELLS, "metadata": {"kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
        "language_info": {"name": "python", "version": "3.12"}},
      "nbformat": 4, "nbformat_minor": 5}
p = os.path.join(LAB, "lab.ipynb")
with open(p, "w", encoding="utf-8") as f:
    json.dump(nb, f, ensure_ascii=False, indent=1)
print("wrote", p)
