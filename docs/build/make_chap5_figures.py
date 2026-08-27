# -*- coding: utf-8 -*-
"""Generate figures for the new Matplotlib chapter (chap5 -> chapters/05-matplotlib)."""
import os
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns

# ---- fixed seed for reproducibility ----
np.random.seed(2025)

OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                   "chapters", "05-matplotlib", "images")
os.makedirs(OUT, exist_ok=True)

# ---- global style: Chinese fonts, no missing glyph warnings ----
# 先 set_theme 再覆盖字体，否则 seaborn 会把 sans-serif 重置为 Arial
sns.set_theme(style="darkgrid")
sns.set_context("notebook")
plt.rcParams["figure.dpi"] = 150
plt.rcParams["savefig.bbox"] = "tight"
plt.rcParams["axes.unicode_minus"] = False
plt.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei", "DejaVu Sans"]
plt.rcParams["font.family"] = "sans-serif"

def save(fig, name):
    path = os.path.join(OUT, name)
    fig.savefig(path)
    plt.close(fig)
    print("saved", path)


# =====================================================================
# 1) basic_plots.png —— 6 种最常用基础图表
# =====================================================================
x = np.linspace(0, 10, 100)
y_line = np.sin(x)
rng = np.random.default_rng(0)
x_scatter = rng.normal(0, 1, 60)
y_scatter = 0.6 * x_scatter + rng.normal(0, 0.4, 60)
cats = ["A", "B", "C", "D"]
vals = [23, 45, 56, 78]

fig, axes = plt.subplots(2, 3, figsize=(12, 6.5))

axes[0, 0].plot(x, y_line, color="#2f6fb3", lw=2)
axes[0, 0].set_title("折线图 plot", fontsize=11)
axes[0, 0].set_xlabel("x"); axes[0, 0].set_ylabel("y")

axes[0, 1].scatter(x_scatter, y_scatter, s=28, c="#e07b39", alpha=0.8)
axes[0, 1].set_title("散点图 scatter", fontsize=11)
axes[0, 1].set_xlabel("x"); axes[0, 1].set_ylabel("y")

axes[0, 2].bar(cats, vals, color=["#7fc59f", "#4c9f70", "#2f6fb3", "#c0392b"], alpha=0.85)
axes[0, 2].set_title("条形图 bar", fontsize=11)
axes[0, 2].set_xlabel("类别"); axes[0, 2].set_ylabel("数值")

data_norm = rng.normal(0, 1, 800)
axes[1, 0].hist(data_norm, bins=30, density=True, color="#7fc59f", edgecolor="white", alpha=0.9)
from scipy.stats import norm
xx = np.linspace(-4, 4, 200)
axes[1, 0].plot(xx, norm.pdf(xx), color="#c0392b", lw=2, label="N(0,1)")
axes[1, 0].set_title("直方图 hist + 密度曲线", fontsize=11)
axes[1, 0].legend(fontsize=8)

box_data = [rng.normal(0, 1, 120), rng.normal(1, 0.7, 120),
            rng.normal(-0.5, 1.4, 120), rng.normal(0.3, 0.9, 120)]
axes[1, 1].boxplot(box_data, tick_labels=["A", "B", "C", "D"])
axes[1, 1].set_title("箱线图 boxplot", fontsize=11)
axes[1, 1].set_ylabel("数值")

pie_labels = ["甲", "乙", "丙", "丁"]
pie_sizes = [15, 30, 45, 10]
axes[1, 2].pie(pie_sizes, labels=pie_labels, autopct="%1.1f%%",
               startangle=140, pctdistance=0.75,
               colors=["#2f6fb3", "#7fc59f", "#e07b39", "#c0392b"])
axes[1, 2].set_title("饼图 pie", fontsize=11)

fig.suptitle("Matplotlib 基础图表一览", fontsize=14)
fig.tight_layout(rect=[0, 0, 1, 0.96])
save(fig, "basic_plots.png")


# =====================================================================
# 2) subplots_layout.png —— 图窗/子图/排版/样式
# =====================================================================
fig, axes = plt.subplots(2, 2, figsize=(10, 6.5))
t = np.linspace(0, 2 * np.pi, 200)

axes[0, 0].plot(t, np.sin(t), color="#2f6fb3", lw=2, label="y=sin(t)")
axes[0, 0].plot(t, np.cos(t), color="#e07b39", lw=2, ls="--", label="y=cos(t)")
axes[0, 0].set_title("折线 + 图例")
axes[0, 0].set_xlabel("t"); axes[0, 0].set_ylabel("值")
axes[0, 0].grid(alpha=0.3); axes[0, 0].legend(fontsize=8)

axes[0, 1].bar(["一", "二", "三", "四"], [30, 42, 18, 55], color="#7fc59f")
axes[0, 1].set_title("条形图")

axes[1, 0].plot(t, np.exp(-t) * np.sin(5 * t), color="#c0392b", lw=1.8,
                marker="o", markersize=3, markevery=12, label="衰减振荡")
axes[1, 0].set_title("线型/标记样式")
axes[1, 0].set_yscale("log")
axes[1, 0].grid(alpha=0.3); axes[1, 0].legend(fontsize=8)

xx2 = np.linspace(-3, 3, 200)
axes[1, 1].plot(xx2, xx2 ** 2, color="#7b5ea7", lw=2, label="x^2")
axes[1, 1].plot(xx2, xx2 ** 3, color="#2f6fb3", lw=2, ls="-.", label="x^3")
axes[1, 1].set_title("坐标范围/刻度")
axes[1, 1].set_xlim(-3, 3); axes[1, 1].set_ylim(-5, 8)
axes[1, 1].set_xticks([-3, -1.5, 0, 1.5, 3])
axes[1, 1].legend(fontsize=8)

fig.suptitle("图窗布局与排版：2×2 子图 + 样式", fontsize=14)
fig.tight_layout(rect=[0, 0, 1, 0.95])
save(fig, "subplots_layout.png")


# =====================================================================
# 3) seaborn_style.png —— seaborn 统计图 / 美化
# =====================================================================
tips = sns.load_dataset("tips")
flights = sns.load_dataset("flights")
flights_pivot = flights.pivot_table(index="month", columns="year", values="passengers", observed=False)

fig, axes = plt.subplots(2, 2, figsize=(12, 8))
sns.histplot(data=tips, x="total_bill", kde=True, ax=axes[0, 0])
axes[0, 0].set_title("histplot + KDE")
sns.boxplot(data=tips, x="day", y="total_bill", ax=axes[0, 1])
axes[0, 1].set_title("boxplot")
sns.violinplot(data=tips, x="day", y="total_bill", ax=axes[1, 0])
axes[1, 0].set_title("violinplot")
sns.heatmap(flights_pivot, ax=axes[1, 1], cmap="YlGnBu", fmt=".0f", annot=True,
            annot_kws={"fontsize": 6}, linewidths=0.4)
axes[1, 1].set_title("heatmap")
fig.suptitle("Seaborn 统计图与美化", fontsize=14)
fig.tight_layout(rect=[0, 0, 1, 0.95])
save(fig, "seaborn_style.png")


# =====================================================================
# 4) case_study.png —— 综合案例：数据分析报告图（串起 01/02/03 的知识）
# =====================================================================
# 合成“传感器信号 + 分组测量数据”
n = 400
t = np.linspace(0, 20, n)
signal = 3 * np.sin(2 * np.pi * 0.25 * t) + 0.6 * np.cos(2 * np.pi * 1.1 * t) + 0.8
noise = rng.normal(0, 0.5, n)
y = signal + noise
smoothed = pd.Series(y).rolling(window=15, center=True).mean().to_numpy()

rng2 = np.random.default_rng(1)
group = rng2.choice(["对照组", "实验组"], size=250, p=[0.5, 0.5])
val = np.where(group == "实验组",
               rng2.normal(5.2, 1.1, 250), rng2.normal(4.0, 1.0, 250))

# 相关矩阵（用 DataFrame 的 corr 得到）
df_corr = pd.DataFrame({
    "x1": rng2.normal(0, 1, 300),
    "x2": rng2.normal(0, 1, 300),
    "x3": rng2.normal(0, 1, 300),
})
df_corr["x4"] = 0.8 * df_corr["x1"] + rng2.normal(0, 0.6, 300)

fig, axes = plt.subplots(2, 2, figsize=(12, 8.5))
fig.suptitle("综合案例：传感器信号观测与分组分析", fontsize=15)

axes[0, 0].plot(t, y, color="#c8d8e8", lw=1, label="带噪声原始信号")
axes[0, 0].plot(t, smoothed, color="#c0392b", lw=2.2, label="滑动平均(窗口=15)")
axes[0, 0].set_title("时间序列：原始信号 vs 平滑")
axes[0, 0].set_xlabel("时间 t"); axes[0, 0].set_ylabel("幅值")
axes[0, 0].legend(fontsize=8); axes[0, 0].grid(alpha=0.3)

sns.histplot(x=y, kde=True, color="#2f6fb3", ax=axes[0, 1])
axes[0, 1].set_title("信号幅值分布（直方图+KDE）")
axes[0, 1].set_xlabel("幅值")

axes[1, 0].scatter(group[group == "对照组"], val[group == "对照组"],
                   color="#7fc59f", s=22, alpha=0.75, label="对照组")
axes[1, 0].scatter(group[group == "实验组"], val[group == "实验组"],
                   color="#e07b39", s=22, alpha=0.75, label="实验组")
axes[1, 0].set_title("分组散点图")
axes[1, 0].set_xlabel("分组"); axes[1, 0].set_ylabel("测量值")
axes[1, 0].legend(fontsize=8); axes[1, 0].grid(alpha=0.3)

corr = df_corr.corr()
sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", vmin=-1, vmax=1,
            ax=axes[1, 1], annot_kws={"fontsize": 9})
axes[1, 1].set_title("变量间相关矩阵热力图")

fig.tight_layout(rect=[0, 0, 1, 0.95])
save(fig, "case_study.png")


# =====================================================================
# list all created figures
# =====================================================================
print("\nfigures in", OUT)
for f in sorted(os.listdir(OUT)):
    print("   ", f)
