# -*- coding: utf-8 -*-
"""Generate figures for the new Statsmodels chapter (chap7 -> chapters/07-statsmodels)."""
import os
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy import stats

OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                   "chapters", "07-statsmodels", "images")
os.makedirs(OUT, exist_ok=True)
plt.rcParams["figure.dpi"] = 150
plt.rcParams["savefig.bbox"] = "tight"
plt.rcParams["axes.spines.top"] = False
plt.rcParams["axes.spines.right"] = False
plt.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei", "DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False


# ---------- 1) OLS linear regression example ----------
rng = np.random.default_rng(0)
x = np.linspace(0, 10, 50)
y = 2 * x + 1 + rng.normal(0, 1, size=len(x))

import statsmodels.api as sm
X = sm.add_constant(x.reshape(-1, 1))
ols = sm.OLS(y, X).fit()
xs = np.linspace(0, 10, 200)
yhat = ols.params[0] + ols.params[1] * xs

fig, ax = plt.subplots(figsize=(6.0, 3.8))
ax.scatter(x, y, s=22, color="#2f6fb3", label="观测数据")
ax.plot(xs, yhat, color="#c0392b", lw=2.4, label="OLS 拟合")
ax.plot(xs, 2 * xs + 1, color="#7f8c8d", ls="--", lw=1.4, label="真实线 y=2x+1")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("一元线性回归 OLS 示例（R²=%.3f）" % ols.rsquared, fontsize=10)
ax.legend(fontsize=8)
ax.grid(alpha=0.25)
fig.savefig(os.path.join(OUT, "regression_ols.png"))
plt.close(fig)

# ---------- 2) One-way ANOVA boxplot ----------
rng = np.random.default_rng(1)
n = 12
groups = {"A": rng.normal(0, 1, n), "B": rng.normal(1, 1, n), "C": rng.normal(2, 1, n)}
data = [groups[k] for k in ["A", "B", "C"]]
fig, ax = plt.subplots(figsize=(5.2, 3.8))
bp = ax.boxplot(data, tick_labels=["A", "B", "C"], patch_artist=True)
for patch, c in zip(bp["boxes"], ["#a8d5f2", "#f5b971", "#a9d9a8"]):
    patch.set_facecolor(c)
means = [np.mean(v) for v in data]
ax.plot(range(1, 4), means, marker="o", color="#c0392b", ls="", label="组均值")
ax.set_xlabel("Group")
ax.set_ylabel("y")
ax.set_title("单因素方差分析：三组均值比较", fontsize=10)
ax.legend(fontsize=8)
ax.grid(alpha=0.25)
fig.savefig(os.path.join(OUT, "anova_boxes.png"))
plt.close(fig)

# ---------- 3) QQ plot of residuals ----------
rng = np.random.default_rng(0)
xd = np.linspace(0, 10, 50)
yd = 3 * xd + 2 + rng.normal(0, 1, 50)
Xx = sm.add_constant(xd.reshape(-1, 1))
resid = sm.OLS(yd, Xx).fit().resid
fig, ax = plt.subplots(figsize=(4.6, 4.2))
(stats.probplot(resid, dist="norm", plot=ax))
ax.set_title("残差 QQ 图（正态性诊断）", fontsize=10)
ax.grid(alpha=0.25)
fig.savefig(os.path.join(OUT, "qq_resid.png"))
plt.close(fig)

# ---------- 4) daily seasonal decomposition ----------
rng = np.random.default_rng(0)
idx = pd.date_range("2022-01-01", periods=180, freq="D")
trend = np.linspace(0, 5, len(idx))
season = 2 * np.sin(2 * np.pi * np.arange(len(idx)) / 7)
noise = rng.normal(0, 0.5, len(idx))
y = 10 + trend + season + noise
s = pd.Series(y, index=idx)
from statsmodels.tsa.seasonal import seasonal_decompose
res = seasonal_decompose(s, model="additive", period=7)
fig, axes = plt.subplots(4, 1, figsize=(9, 6.4), sharex=True)
for ax, name, series in zip(axes, ["观测值", "趋势", "季节性", "残差"],
                            [s, res.trend, res.seasonal, res.resid]):
    ax.plot(series.index, series.values, lw=1.2, color="#2f6fb3")
    ax.set_ylabel(name, fontsize=9)
    ax.grid(alpha=0.2)
axes[0].set_title("日用电量序列的加法分解（周期=7 天）", fontsize=11)
fig.tight_layout()
fig.savefig(os.path.join(OUT, "decompose_daily.png"))
plt.close(fig)

# ---------- 5) ARIMA forecast ----------
rng = np.random.default_rng(0)
n = 200
steps = rng.normal(0, 1, n).cumsum() + np.linspace(0, 10, n)
si = pd.Series(steps, index=pd.date_range("2020-01-01", periods=n, freq="D"))
from statsmodels.tsa.arima.model import ARIMA
mod = ARIMA(si, order=(1, 1, 1)).fit()
fc = mod.forecast(steps=5)
fig, ax = plt.subplots(figsize=(9, 3.8))
ax.plot(si.index[-30:], si.values[-30:], color="#2f6fb3", label="历史数据")
fc_idx = pd.date_range(si.index[-1] + pd.Timedelta(days=1), periods=5, freq="D")
ax.plot(fc_idx, fc.values, marker="o", color="#c0392b", label="ARIMA(1,1,1) 预测")
ax.axvline(si.index[-1], color="#7f8c8d", ls=":", lw=1.2)
ax.set_xlabel("日期")
ax.set_ylabel("y")
ax.set_title("ARIMA(1,1,1) 未来 5 步预测", fontsize=10)
ax.legend(fontsize=8)
ax.grid(alpha=0.25)
fig.savefig(os.path.join(OUT, "arima_forecast.png"))
plt.close(fig)

# ---------- 6/7) comprehensive case: consistent 城市日负荷 dataset ----------
rng = np.random.default_rng(7)
m = 140
date = pd.date_range("2023-01-01", periods=m, freq="D")
trendc = np.linspace(0, 15, m)
seasonc = 5 * np.sin(2 * np.pi * np.arange(m) / 7) + 2 * np.cos(2 * np.pi * np.arange(m) / 7)
noisec = rng.normal(0, 3, m)
weekend = (date.dayofweek >= 5).astype(int)
temp = 25 + 6 * np.sin(2 * np.pi * np.arange(m) / 7) + rng.normal(0, 2, m)
load = 300 + 4 * temp + 20 * weekend + trendc + seasonc + noisec
dfc = pd.DataFrame({"date": date, "load": load, "weekend": weekend, "temp": temp})

# regression diagnostic figure
olm = sm.OLS(dfc["load"], sm.add_constant(dfc[["temp", "weekend"]])).fit()
fig, axes = plt.subplots(1, 2, figsize=(9.5, 3.8))
axes[0].scatter(dfc["temp"], dfc["load"], s=14, color="#2f6fb3", alpha=0.7)
xs = np.linspace(dfc["temp"].min(), dfc["temp"].max(), 100)
axes[0].plot(xs, olm.params.iloc[0] + olm.params.iloc[1] * xs, color="#c0392b", lw=2,
             label="OLS（控制 weekend）")
axes[0].set_xlabel("温度"); axes[0].set_ylabel("负荷")
axes[0].set_title("负荷 vs 温度 与 OLS 拟合", fontsize=10)
axes[0].legend(fontsize=8); axes[0].grid(alpha=0.25)
axes[1].hist(olm.resid, bins=18, color="#a9d9a8", edgecolor="white")
axes[1].set_xlabel("残差"); axes[1].set_ylabel("频数")
axes[1].set_title("回归残差分布", fontsize=10)
axes[1].grid(alpha=0.25)
fig.tight_layout()
fig.savefig(os.path.join(OUT, "case_regression_diag.png"))
plt.close(fig)

# time-series decomposition + ARIMA forecast figure
load_s = pd.Series(dfc["load"].values, index=date)
decomp = seasonal_decompose(load_s, model="additive", period=7)
modc = ARIMA(load_s, order=(1, 1, 1)).fit()
fcc = modc.forecast(steps=7)
fig, axes = plt.subplots(2, 1, figsize=(9.5, 6.2))
axes[0].plot(load_s.index, load_s.values, color="#2f6fb3", lw=1.2, label="日负荷")
axes[0].plot(decomp.trend.index, decomp.trend.values, color="#c0392b", lw=1.6, label="趋势")
axes[0].set_title("城市日负荷序列与趋势", fontsize=10)
axes[0].legend(fontsize=8); axes[0].grid(alpha=0.25)
fcc_idx = pd.date_range(load_s.index[-1] + pd.Timedelta(days=1), periods=7, freq="D")
axes[1].plot(load_s.index[-21:], load_s.values[-21:], color="#2f6fb3", label="历史（近3周）")
axes[1].plot(fcc_idx, fcc.values, marker="o", color="#c0392b", label="ARIMA 未来 7 天")
axes[1].axvline(load_s.index[-1], color="#7f8c8d", ls=":", lw=1.2)
axes[1].set_title("ARIMA(1,1,1) 一周预测", fontsize=10)
axes[1].legend(fontsize=8); axes[1].grid(alpha=0.25)
fig.tight_layout()
fig.savefig(os.path.join(OUT, "case_ts_forecast.png"))
plt.close(fig)

print("figures saved to", OUT)
for f in sorted(os.listdir(OUT)):
    print("  ", f)
