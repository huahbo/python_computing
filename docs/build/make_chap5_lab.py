# -*- coding: utf-8 -*-
"""Generate lab.ipynb for chapter 05 (Matplotlib) — guided lab notebook."""
import json, os

cells = []
def md(text): cells.append({"cell_type": "markdown", "metadata": {}, "source": text})
def code(text): cells.append({"cell_type": "code", "metadata": {}, "execution_count": None,
                              "outputs": [], "source": text})

md("""# Matplotlib 上机实验（第 5 章 lab）

**要求**：按顺序运行每一格，完成所有 `# TODO` 后运行最后的综合任务；最后截图/导出 notebook 提交。
环境：Python 3.10+，NumPy ≥ 1.24，pandas ≥ 2.0，Matplotlib ≥ 3.8，seaborn ≥ 0.13。
本节使用的示例数据集（tips / flights）由 seaborn 内置提供。

---
""")

code("""import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

print("numpy", np.__version__)
print("pandas", pd.__version__)
print("matplotlib", matplotlib.__version__)
print("seaborn", sns.__version__)

# 中文字体设置：避免中文标题显示为方块
matplotlib.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei", "DejaVu Sans"]
matplotlib.rcParams["axes.unicode_minus"] = False
print("环境 OK（若上方 warning 提示字体缺失，请确认 Microsoft YaHei/SimHei 已安装）")
""")

md("""## Part 1 基础绘图

练习折线图、散点图、条形图、直方图、箱线图、饼图。""")

code("""# TODO 1.1 折线图（plot）
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)
plt.figure(figsize=(6, 3))
plt.plot(x, y, color="#2f6fb3", lw=2, label="y=sin(x)")
plt.title("折线图示例")
plt.xlabel("x"); plt.ylabel("y")
plt.grid(alpha=0.3); plt.legend()
plt.show()
""")

code("""# TODO 1.2 散点图（scatter）
rng = np.random.default_rng(0)
x = rng.normal(0, 1, 80)
y = 0.6 * x + rng.normal(0, 0.4, 80)
plt.figure(figsize=(6, 3))
plt.scatter(x, y, s=22, c="#e07b39", alpha=0.8)
plt.title("散点图示例")
plt.xlabel("x"); plt.ylabel("y")
plt.show()
""")

code("""# TODO 1.3 条形图（bar）
cats = ["A", "B", "C", "D"]
vals = [23, 45, 56, 78]
plt.figure(figsize=(5, 3))
plt.bar(cats, vals, color="#7fc59f")
plt.title("条形图示例")
plt.xlabel("类别"); plt.ylabel("数值")
plt.show()
""")

code("""# TODO 1.4 直方图（hist，并叠加理论密度曲线）
from scipy.stats import norm
data = np.random.default_rng(1).normal(0, 1, 500)
plt.figure(figsize=(6, 3))
plt.hist(data, bins=25, density=True, color="#7fc59f", edgecolor="white", alpha=0.9)
xx = np.linspace(-4, 4, 200)
plt.plot(xx, norm.pdf(xx), color="#c0392b", lw=2, label="N(0,1)")
plt.title("直方图示例")
plt.xlabel("x"); plt.ylabel("密度")
plt.legend(); plt.show()
""")

code("""# TODO 1.5 箱线图与饼图
np.random.seed(10)
data = np.random.normal(0, 1, 150)
data = np.concatenate([data, [5.0]])   # 加入一个异常值
plt.figure(figsize=(5, 3))
plt.boxplot(data)
plt.title("箱线图示例（含异常值）")
plt.show()

labels = ["甲", "乙", "丙", "丁"]
sizes = [15, 30, 45, 10]
plt.figure(figsize=(5, 3))
plt.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=140)
plt.title("饼图示例")
plt.axis("equal")
plt.show()
""")

md("""## Part 2 图窗、布局与排版

练习 figure / subplots / rcParams / 坐标轴设置 / 网格 / 图例 / 保存图像。""")

code("""# TODO 2.1 子图 + 样式 + 图例
t = np.linspace(0, 2 * np.pi, 200)
fig, axes = plt.subplots(2, 2, figsize=(9, 6))
axes[0, 0].plot(t, np.sin(t), label="sin")
axes[0, 0].plot(t, np.cos(t), ls="--", label="cos")
axes[0, 0].set_title("sin / cos")
axes[0, 0].set_xlabel("t"); axes[0, 0].legend(); axes[0, 0].grid(alpha=0.3)

axes[0, 1].bar(["一", "二", "三", "四"], [30, 42, 18, 55])
axes[0, 1].set_title("bar")

axes[1, 0].plot(t, np.exp(-t) * np.sin(5 * t), marker="o", markersize=3, markevery=12)
axes[1, 0].set_title("衰减振荡")
axes[1, 0].set_yscale("log")

axes[1, 1].plot(t, np.cos(3 * t), color="#7b5ea7")
axes[1, 1].set_title("网格与刻度")
axes[1, 1].set_xticks([0, 1.57, 3.14, 4.71, 6.28])
axes[1, 1].set_xticklabels(["0", "π/2", "π", "3π/2", "2π"], fontsize=8)
axes[1, 1].grid(alpha=0.4)

fig.tight_layout()
plt.show()
""")

code("""# TODO 2.2 全局 rcParams 与保存图像
import matplotlib
matplotlib.rcParams["font.size"] = 12
plt.figure(figsize=(6, 3), dpi=120)
plt.plot([1, 2, 3], [4, 3, 2], color="red", lw=2, label="demo")
plt.title("保存图像示例"); plt.legend()
plt.savefig("lab_demo.png", dpi=150)     # 保存为 PNG
print("已保存 lab_demo.png")
plt.show()
""")

md("""## Part 3 Seaborn 美化

使用 seaborn 的统计图接口与内置数据集。""")

code("""# TODO 3.1 histplot + boxplot + violinplot + heatmap
import seaborn as sns
sns.set_theme(style="darkgrid")
# 注意：set_theme 会覆盖字体，需重新设置
import matplotlib as mpl
mpl.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei", "DejaVu Sans"]
mpl.rcParams["axes.unicode_minus"] = False

tips = sns.load_dataset("tips")
flights = sns.load_dataset("flights")
flights_pivot = flights.pivot_table(index="month", columns="year", values="passengers", observed=False)

fig, axes = plt.subplots(2, 2, figsize=(11, 7))
sns.histplot(data=tips, x="total_bill", kde=True, ax=axes[0, 0])
axes[0, 0].set_title("histplot + KDE")
sns.boxplot(data=tips, x="day", y="total_bill", ax=axes[0, 1])
axes[0, 1].set_title("boxplot")
sns.violinplot(data=tips, x="day", y="total_bill", ax=axes[1, 0])
axes[1, 0].set_title("violinplot")
sns.heatmap(flights_pivot, ax=axes[1, 1], cmap="YlGnBu", fmt=".0f", annot=True,
            annot_kws={"fontsize": 6})
axes[1, 1].set_title("heatmap")
fig.tight_layout()
plt.show()
""")

code("""# TODO 3.2 FacetGrid 分面图
tips = sns.load_dataset("tips")
g = sns.FacetGrid(tips, col="day", col_wrap=2, height=2.6, aspect=1.4)
g.map(sns.scatterplot, "total_bill", "tip")
g.add_legend()
plt.show()
""")

md("""## Part 4 综合任务：传感器信号分析报告图

串起 01–03 的知识：时间序列折线 + 平滑、幅值分布、分组散点、相关矩阵热力图。""")

code("""# TODO 4.1 生成信号并做滑动平均
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

rng = np.random.default_rng(2)
n = 400
t = np.linspace(0, 20, n)
signal = 3 * np.sin(2 * np.pi * 0.25 * t) + 0.6 * np.cos(2 * np.pi * 1.1 * t) + 0.8
y = signal + rng.normal(0, 0.5, n)
smoothed = pd.Series(y).rolling(window=15, center=True).mean().to_numpy()
print("信号长度:", n, " 均值:", round(y.mean(), 3), " 标准差:", round(y.std(), 3))
# TODO: 调整窗口大小（5 / 15 / 31），观察平滑效果并记录结论
""")

code("""# TODO 4.2 生成分组测量数据与相关矩阵
rng2 = np.random.default_rng(1)
group = rng2.choice(["对照组", "实验组"], size=250, p=[0.5, 0.5])
val = np.where(group == "实验组", rng2.normal(5.2, 1.1, 250), rng2.normal(4.0, 1.0, 250))

df_corr = pd.DataFrame({
    "x1": rng2.normal(0, 1, 300),
    "x2": rng2.normal(0, 1, 300),
    "x3": rng2.normal(0, 1, 300),
})
df_corr["x4"] = 0.8 * df_corr["x1"] + rng2.normal(0, 0.6, 300)
corr = df_corr.corr()
print("对照组均值:", round(val[group == "对照组"].mean(), 3))
print("实验组均值:", round(val[group == "实验组"].mean(), 3))
print(corr.round(2))
""")

code("""# TODO 4.3 绘制 2×2 报告图并保存
import matplotlib
matplotlib.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei", "DejaVu Sans"]
matplotlib.rcParams["axes.unicode_minus"] = False

fig, axes = plt.subplots(2, 2, figsize=(12, 8.5))
fig.suptitle("综合案例：传感器信号观测与分组分析", fontsize=15)

axes[0, 0].plot(t, y, color="#c8d8e8", lw=1, label="原始信号")
axes[0, 0].plot(t, smoothed, color="#c0392b", lw=2.2, label="滑动平均(窗口=15)")
axes[0, 0].set_title("时间序列：原始信号 vs 平滑")
axes[0, 0].set_xlabel("时间 t"); axes[0, 0].set_ylabel("幅值")
axes[0, 0].legend(fontsize=8); axes[0, 0].grid(alpha=0.3)

sns.histplot(x=y, kde=True, color="#2f6fb3", ax=axes[0, 1])
axes[0, 1].set_title("信号幅值分布")
axes[0, 1].set_xlabel("幅值")

axes[1, 0].scatter(group[group == "对照组"], val[group == "对照组"],
                   color="#7fc59f", s=22, alpha=0.75, label="对照组")
axes[1, 0].scatter(group[group == "实验组"], val[group == "实验组"],
                   color="#e07b39", s=22, alpha=0.75, label="实验组")
axes[1, 0].set_title("分组散点图")
axes[1, 0].set_xlabel("分组"); axes[1, 0].set_ylabel("测量值")
axes[1, 0].legend(fontsize=8); axes[1, 0].grid(alpha=0.3)

sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", vmin=-1, vmax=1, ax=axes[1, 1],
            annot_kws={"fontsize": 9})
axes[1, 1].set_title("变量间相关矩阵热力图")

fig.tight_layout(rect=[0, 0, 1, 0.95])
fig.savefig("lab_case_report.png", dpi=150)
print("已保存 lab_case_report.png")
plt.show()
""")

md("""## 提交清单

- [ ] 所有 TODO 均已填写并运行；
- [ ] Part 2 已保存 `lab_demo.png`；
- [ ] Part 3 的 histplot / boxplot / violinplot / heatmap / FacetGrid 均已输出；
- [ ] Part 4 已保存 `lab_case_report.png` 并写 3 句结论；
- [ ] 导出为 html / 保留 ipynb 提交。

**延伸**：完成 exercises/ 的习题与本仓库 `04-综合案例.md` 的拓展任务。""")

nb = {
    "cells": cells,
    "metadata": {
        "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
        "language_info": {"name": "python", "version": "3.10"}
    },
    "nbformat": 4,
    "nbformat_minor": 5,
}
out = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                   "chapters", "05-matplotlib", "lab", "lab.ipynb")
os.makedirs(os.path.dirname(out), exist_ok=True)
with open(out, "w", encoding="utf-8") as f:
    # 统一为中文字体设置（所有绘图单元注入微软雅黑）
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
    json.dump(nb, f, ensure_ascii=False, indent=1)
print("saved", out, "cells:", len(cells))
