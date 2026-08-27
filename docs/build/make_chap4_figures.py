# -*- coding: utf-8 -*-
"""Generate figures for the Pandas chapter (chap4 -> chapters/04-pandas/images)."""
import os
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                   "chapters", "04-pandas", "images")
os.makedirs(OUT, exist_ok=True)
plt.rcParams["figure.dpi"] = 150
plt.rcParams["savefig.bbox"] = "tight"
plt.rcParams["axes.spines.top"] = False
plt.rcParams["axes.spines.right"] = False
plt.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei", "DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False
np.random.seed(42)


def make_grade_data():
    """Deterministic long-format score table used in the case study."""
    rng = np.random.default_rng(42)
    classes = ["一班", "二班", "三班"]
    subjects = ["语文", "数学", "英语"]
    base = {"一班": 82, "二班": 78, "三班": 85}
    rows = []
    for i in range(1, 21):
        cls = classes[i % 3]
        for sub in subjects:
            score = rng.normal(base[cls], 6)
            rows.append({"学号": f"S{i:02d}", "姓名": f"学生{i:02d}",
                         "班级": cls, "科目": sub, "分数": round(score, 1)})
    df = pd.DataFrame(rows)
    df.loc[2, "分数"] = np.nan       # 语文缺失（S01）
    df.loc[5, "分数"] = np.nan       # 英语缺失（S02）
    df = pd.concat([df, df.iloc[[1]].copy()], ignore_index=True)  # 制造重复行
    return df


def clean_data(df):
    df = df.dropna(subset=["分数"])
    df = df.drop_duplicates()
    Q1 = df["分数"].quantile(0.25)
    Q3 = df["分数"].quantile(0.75)
    IQR = Q3 - Q1
    mask = (df["分数"] < Q1 - 1.5 * IQR) | (df["分数"] > Q3 + 1.5 * IQR)
    df.loc[mask, "分数"] = df["分数"].median()
    return df


df = make_grade_data()
df_clean = clean_data(df)
piv = df_clean.pivot_table(values="分数", index="班级", columns="科目", aggfunc="mean").round(1)
print("pivot (各班各科平均分):")
print(piv)

# --- Figure 1: grouped bar of average scores ---
fig, ax = plt.subplots(figsize=(7.2, 4.0))
subjects = piv.columns.tolist()
x = np.arange(len(piv.index))
width = 0.25
colors = ["#2f6fb3", "#e07b39", "#3a8f4f"]
for j, sub in enumerate(subjects):
    vals = piv[sub].values
    ax.bar(x + (j - 1) * width, vals, width=width, label=sub, color=colors[j])
    for xi, v in zip(x + (j - 1) * width, vals):
        ax.text(xi, v + 0.3, f"{v:.1f}", ha="center", fontsize=8)
ax.set_xticks(x)
ax.set_xticklabels(piv.index)
ax.set_ylabel("平均分")
ax.set_title("各班各科平均分（pivot_table 结果）")
ax.legend(title="科目")
ax.grid(axis="y", alpha=0.25)
fig.savefig(os.path.join(OUT, "case_scores.png"))
plt.close(fig)

# --- Figure 2: score distribution by class ---
fig, ax = plt.subplots(figsize=(7.2, 4.0))
for (cls, g), c in zip(df_clean.groupby("班级"), colors):
    ax.hist(g["分数"], bins=12, alpha=0.55, label=cls, color=c)
ax.set_xlabel("分数")
ax.set_ylabel("人数")
ax.set_title("各班成绩分布直方图")
ax.legend()
ax.grid(alpha=0.25)
fig.savefig(os.path.join(OUT, "case_distribution.png"))
plt.close(fig)

# --- Figure 3: time series resample + rolling ---
rng = np.random.default_rng(7)
idx = pd.date_range("2023-01-01", periods=60, freq="D")
# daily "到课人数": baseline 40, weekly cycle + noise
trend = np.linspace(0, 10, 60)
weekly = 5 * np.sin(2 * np.pi * np.arange(60) / 7)
count = (40 + trend + weekly + rng.normal(0, 3, 60)).round().clip(0, 60).astype(int)
ts = pd.Series(count, index=idx)
weekly_mean = ts.resample("W").mean()          # 周均
rolling7 = ts.rolling(7).mean()               # 7 日移动平均

fig, ax = plt.subplots(figsize=(8.0, 4.0))
ax.plot(ts.index, ts.values, color="#7f8c8d", lw=1.2, label="日到课人数")
ax.plot(weekly_mean.index, weekly_mean.values, color="#2f6fb3", marker="o", ms=4,
        lw=2, label="周均（resample）")
ax.plot(rolling7.index, rolling7.values, color="#e07b39", lw=2, ls="--", label="7 日移动平均")
ax.set_ylabel("人数")
ax.set_title("时间序列：日数据 → 周均与移动平均")
ax.legend()
ax.grid(alpha=0.25)
fig.autofmt_xdate()
fig.savefig(os.path.join(OUT, "case_time_series.png"))
plt.close(fig)

print("saved figures:")
for f in sorted(os.listdir(OUT)):
    print("  ", f)
