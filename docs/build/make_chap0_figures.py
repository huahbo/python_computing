# -*- coding: utf-8 -*-
"""Generate figures for Chapter 0 (chapters/00-prep/images)."""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                   "chapters", "00-prep", "images")
os.makedirs(OUT, exist_ok=True)
plt.rcParams["figure.dpi"] = 150
plt.rcParams["savefig.bbox"] = "tight"
plt.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei", "DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False


def box(ax, x, y, w, h, text, fc="#e8f1fb", ec="#2f6fb3", fs=10):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02",
                                fc=fc, ec=ec, lw=1.2))
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", fontsize=fs)


# 1) course_map: 第0章 + 8 章
fig, ax = plt.subplots(figsize=(11, 2.4))
ax.set_xlim(0, 10); ax.set_ylim(0, 2.2); ax.axis("off")
labels = ["第0章 前置", "1 NumPy", "2 SymPy", "3 SciPy", "4 Pandas",
          "5 Matplotlib", "6 NetworkX", "7 Stats", "8 sklearn"]
for i, lab in enumerate(labels):
    fc = "#ffe6c7" if i == 0 else "#e4f0e4"
    ec = "#c07a2f" if i == 0 else "#3a8f4f"
    box(ax, i * 1.05 + 0.15, 0.7, 0.95, 0.75, lab, fc=fc, ec=ec, fs=8.5)
    if i < len(labels) - 1:
        ax.add_patch(FancyArrowPatch((i * 1.05 + 1.12, 1.07),
                                     ((i + 1) * 1.05 + 0.14, 1.07),
                                     arrowstyle="-|>", mutation_scale=10, color="#888888"))
ax.text(5, 1.95, "课程主线：第 0 章打基础，1~8 章递进", ha="center", fontsize=11)
ax.text(5, 0.25, "(第 0 章 不改变 8 周主线编号)", ha="center", fontsize=9, color="#666666")
fig.savefig(os.path.join(OUT, "course_map.png"))
plt.close(fig)

# 2) env_stack
fig, ax = plt.subplots(figsize=(6.6, 4.4))
ax.set_xlim(0, 6); ax.set_ylim(0, 6.6); ax.axis("off")
layers = [
    ("你的项目：chapters/ / lab / report", "#eef3fb"),
    ("编辑器：VS Code（Python / Jupyter / LaTeX Workshop）", "#e8f1fb"),
    ("内核：ipykernel（Jupyter）", "#e4f0e4"),
    ("环境：Miniconda scicomp", "#e0eee0"),
    ("依赖：numpy sympy scipy pandas matplotlib networkx statsmodels sklearn", "#d9ecd9"),
    ("系统：Windows 10/11（macOS/Linux 备注）", "#f5f5f5"),
]
y = 0.6
for i, (text, fc) in enumerate(layers):
    h = 0.85
    box(ax, 0.5, y, 5.0, h, text, fc=fc, ec="#5b7fb3" if i < 4 else "#999999", fs=9.5)
    y += h + 0.18
ax.text(3, 6.25, "课程统一环境（第 0 章搭建）", ha="center", fontsize=12, color="#2f6fb3")
fig.savefig(os.path.join(OUT, "env_stack.png"))
plt.close(fig)

# 3) latex_flow
fig, ax = plt.subplots(figsize=(9, 2.6))
ax.set_xlim(0, 9); ax.set_ylim(0, 2.4); ax.axis("off")
steps = [
    ("写 .tex", "ctexart + 公式/表格/图", "#e8f1fb"),
    ("保存", "LaTeX Workshop 自动构建", "#e4f0e4"),
    ("latexmk -xelatex", "中文多遍编译", "#e0eee0"),
    ("PDF 预览", "VS Code 内查看", "#d9ecd9"),
]
for i, (t, sub, fc) in enumerate(steps):
    x = 0.4 + i * 2.2
    ax.add_patch(FancyBboxPatch((x, 0.5), 1.9, 1.1, boxstyle="round,pad=0.03", fc=fc, ec="#3a8f4f"))
    ax.text(x + 0.95, 1.35, t, ha="center", fontsize=11, color="#1f5c2f")
    ax.text(x + 0.95, 0.85, sub, ha="center", fontsize=8.5, color="#555555")
    if i < len(steps) - 1:
        ax.add_patch(FancyArrowPatch((x + 1.95, 1.05), (x + 2.25, 1.05),
                                     arrowstyle="-|>", mutation_scale=12, color="#888888"))
ax.text(4.5, 2.1, "LaTeX 编译流程（在线平台同理：编辑 → 编译 → PDF）", ha="center", fontsize=11)
fig.savefig(os.path.join(OUT, "latex_flow.png"))
plt.close(fig)

print("wrote figures to", OUT)
