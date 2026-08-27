# -*- coding: utf-8 -*-
"""Generate figures for the new SciPy chapter (chap3 -> chapters/03-scipy)."""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                   "chapters", "03-scipy", "images")
os.makedirs(OUT, exist_ok=True)

plt.rcParams["figure.dpi"] = 140
plt.rcParams["savefig.bbox"] = "tight"
plt.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei", "DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False
plt.rcParams["axes.spines.top"] = False
plt.rcParams["axes.spines.right"] = False


# ---------------------------------------------------------------- 01 ODE
from scipy.integrate import odeint, solve_ivp
import numpy as np

t = np.linspace(0, 10, 200)

def second_order(y, t):
    y1, y2 = y
    return [y2, -y1]

y_ode = odeint(second_order, [1, 0], t)
sol = solve_ivp(lambda tt, y: -2 * y, (0, 10), [1], t_eval=t)

fig, axes = plt.subplots(1, 2, figsize=(9.2, 3.2))
axes[0].plot(t, y_ode[:, 0], color="#2f6fb3", lw=2)
axes[0].plot(t, np.cos(t), "--", color="#c0392b", lw=1.2)
axes[0].set_xlabel("t"); axes[0].set_ylabel("y")
axes[0].set_title("y'' + y = 0  （数值解 vs 解析解）", fontsize=10)
axes[0].grid(alpha=0.3)
axes[1].plot(t, sol.y[0], color="#3a8f4f", lw=2)
axes[1].plot(t, np.exp(-2 * t), "--", color="#666", lw=1.2)
axes[1].set_xlabel("t"); axes[1].set_ylabel("y")
axes[1].set_title("dy/dt = -2y  （solve_ivp）", fontsize=10)
axes[1].grid(alpha=0.3)
fig.tight_layout()
fig.savefig(os.path.join(OUT, "ode_solution.png"))
plt.close(fig)


# ---------------------------------------------------------------- 02 curve_fit
from scipy.optimize import curve_fit
rng = np.random.default_rng(7)
def model(x, a, b, c): return a * x**2 + b * x + c
x = np.linspace(-10, 10, 50)
y = model(x, 2, 3, 1) + rng.normal(0, 2, len(x))
popt, pcov = curve_fit(model, x, y, p0=[0, 0, 0])
fig, ax = plt.subplots(figsize=(5.8, 3.6))
ax.scatter(x, y, s=16, color="#2f6fb3", alpha=0.8, label="噪声数据")
xs = np.linspace(-10, 10, 200)
ax.plot(xs, model(xs, *popt), color="#e07b39", lw=2, label="curve_fit 拟合")
ax.set_xlabel("x"); ax.set_ylabel("y")
ax.set_title("非线性最小二乘拟合", fontsize=10)
ax.legend(fontsize=8); ax.grid(alpha=0.3)
fig.savefig(os.path.join(OUT, "optimize_fit.png"))
plt.close(fig)


# ---------------------------------------------------------------- 03 interpolation
from scipy.interpolate import CubicSpline
x = np.linspace(0, 2 * np.pi, 9)
y = np.sin(x)
xs = np.linspace(0, 2 * np.pi, 300)
cs = CubicSpline(x, y)
fig, ax = plt.subplots(figsize=(6.0, 3.6))
ax.plot(xs, np.sin(xs), "--", color="#999", lw=1.2, label="真值 sin(x)")
ax.plot(xs, cs(xs), color="#2f6fb3", lw=2, label="三次样条插值 CubicSpline")
ax.plot(x, y, "o", color="#c0392b", ms=5, label="采样点")
ax.set_xlabel("x"); ax.set_ylabel("y")
ax.set_title("一维插值：三次样条", fontsize=10)
ax.legend(fontsize=8); ax.grid(alpha=0.3)
fig.savefig(os.path.join(OUT, "interp_compare.png"))
plt.close(fig)


# ---------------------------------------------------------------- 04 stats
from scipy.stats import f_oneway
rng = np.random.default_rng(1)
g1 = rng.normal(0, 1, 60); g2 = rng.normal(0.5, 1, 60); g3 = rng.normal(1, 1, 60)
data = [g1, g2, g3]
fig, ax = plt.subplots(figsize=(5.8, 3.6))
bp = ax.boxplot(data, labels=["组 A", "组 B", "组 C"], patch_artist=True)
for patch, c in zip(bp["boxes"], ["#cfe3f7", "#e0f0d9", "#fde4cf"]):
    patch.set_facecolor(c)
F, p = f_oneway(g1, g2, g3)
ax.set_ylabel("观测值")
ax.set_title(f"三组比较 (单因素 ANOVA, F={F:.2f}, p={p:.2e})", fontsize=10)
ax.grid(alpha=0.3)
fig.savefig(os.path.join(OUT, "stats_boxplot.png"))
plt.close(fig)


# ---------------------------------------------------------------- 05 FFT
from scipy.fft import rfft, rfftfreq
fs = 1000; T = 1.0; N = int(fs * T)
t = np.linspace(0, T, N, endpoint=False)
sig = 0.7 * np.sin(2 * np.pi * 50 * t) + np.sin(2 * np.pi * 200 * t)
Y = rfft(sig); f = rfftfreq(N, 1 / fs)
fig, axes = plt.subplots(1, 2, figsize=(9.0, 3.2))
axes[0].plot(t[:300], sig[:300], color="#2f6fb3", lw=1.5)
axes[0].set_xlabel("t (s)"); axes[0].set_ylabel("信号")
axes[0].set_title("时域信号（前 0.3 s）", fontsize=10)
axes[0].grid(alpha=0.3)
axes[1].plot(f, np.abs(Y), color="#c0392b", lw=1.5)
axes[1].set_xlim(0, 300)
axes[1].set_xlabel("频率 (Hz)"); axes[1].set_ylabel("|Y(f)|")
axes[1].set_title("单边频谱（50/200 Hz 峰值）", fontsize=10)
axes[1].grid(alpha=0.3)
fig.tight_layout()
fig.savefig(os.path.join(OUT, "fft_spectrum.png"))
plt.close(fig)


# ---------------------------------------------------------------- 06 case
from scipy.interpolate import CubicSpline as _cs
from scipy.fft import rfft as _rfft, rfftfreq as _rfftfreq
from scipy.optimize import curve_fit as _cf
from scipy.integrate import trapezoid as _trap
from scipy.stats import ttest_ind as _tt

rng = np.random.default_rng(42)
fs = 500; T = 5.0; N = int(fs * T)
tt = np.linspace(0, T, N, endpoint=False)
def true_signal(t):
    return 2 + 0.5 * t + 1.2 * np.sin(2 * np.pi * 5 * t) + 0.3 * np.sin(2 * np.pi * 12 * t)
y_true = true_signal(tt)
y_raw = y_true + rng.normal(0, 0.2, N)
y_obs = y_raw.copy(); y_obs[150:160] = np.nan
mask = ~np.isnan(y_obs)
cs = _cs(tt[mask], y_obs[mask])
y_filled = y_obs.copy(); y_filled[150:160] = cs(tt[150:160])

coef = np.polyfit(tt, y_filled, 1)
detrend = y_filled - np.polyval(coef, tt)
Y = _rfft(detrend); fr = _rfftfreq(N, 1 / fs)
amps = np.abs(Y)

def model2(t, c1, c2, A1, f1, p1, A2, f2, p2):
    return c1 + c2 * t + A1 * np.sin(2 * np.pi * f1 * t + p1) + A2 * np.sin(2 * np.pi * f2 * t + p2)
popt, pcov = _cf(model2, tt, y_filled, p0=[2, 0.5, 1.2, 5, 0, 0.3, 12, 0], maxfev=50000)
resid = y_filled - model2(tt, *popt)
area = _trap(y_filled, tt)
g1 = y_filled[(tt >= 0) & (tt < 1)]
g2 = y_filled[(tt >= 4) & (tt < 5)]
tt_res = _tt(g1, g2)

# case figure 1: signal + missing + filled
fig, ax = plt.subplots(figsize=(7.2, 3.6))
ax.plot(tt, y_raw, color="#bfbfbf", lw=1.0, label="原始观测（含噪声）")
ax.plot(tt, y_true, "--", color="#2f6fb3", lw=1.2, label="真实信号")
ax.plot(tt, y_filled, color="#e07b39", lw=1.6, label="插值补齐后")
ax.scatter(tt[150:160], y_filled[150:160], color="#c0392b", s=14, zorder=5, label="缺失段补点")
ax.set_xlabel("时间 t (s)"); ax.set_ylabel("信号值")
ax.set_title("案例：含缺失段的传感器信号插值补齐", fontsize=10)
ax.legend(fontsize=8); ax.grid(alpha=0.3)
fig.tight_layout()
fig.savefig(os.path.join(OUT, "case_signal.png"))
plt.close(fig)

# case figure 2: spectrum
fig, ax = plt.subplots(figsize=(6.4, 3.6))
ax.plot(fr, amps, color="#2f6fb3", lw=1.5)
ax.set_xlim(0, 30)
ax.set_xlabel("频率 (Hz)"); ax.set_ylabel("|Y(f)|")
ax.set_title("去趋势后频谱（5 Hz 与 12 Hz 峰值）", fontsize=10)
k = int(5 * N / fs)
ax.annotate("5 Hz", xy=(5, amps[k]), xytext=(7, amps[k] * 0.85),
            arrowprops=dict(arrowstyle="->", color="#c0392b"))
k2 = int(12 * N / fs)
ax.annotate("12 Hz", xy=(12, amps[k2]), xytext=(14, amps[k2] * 0.85),
            arrowprops=dict(arrowstyle="->", color="#c0392b"))
ax.grid(alpha=0.3)
fig.tight_layout()
fig.savefig(os.path.join(OUT, "case_fft.png"))
plt.close(fig)

# case figure 3: fit + residual
fig, axes = plt.subplots(2, 1, figsize=(7.2, 5.2), sharex=True)
axes[0].plot(tt, y_filled, color="#bfbfbf", lw=0.8, label="插值后数据")
axes[0].plot(tt, model2(tt, *popt), color="#2f6fb3", lw=1.8, label="双正弦+趋势拟合")
axes[0].set_ylabel("信号值")
axes[0].set_title("案例：非线性最小二乘拟合", fontsize=10)
axes[0].legend(fontsize=8); axes[0].grid(alpha=0.3)
axes[1].plot(tt, resid, color="#c0392b", lw=0.9)
axes[1].set_ylabel("残差"); axes[1].set_xlabel("时间 t (s)")
axes[1].grid(alpha=0.3)
fig.tight_layout()
fig.savefig(os.path.join(OUT, "case_fit.png"))
plt.close(fig)

# case figure 4: first vs last segment boxplot
fig, ax = plt.subplots(figsize=(4.8, 3.4))
ax.boxplot([g1, g2], labels=["前 1 s", "后 1 s"], patch_artist=True)
ax.set_ylabel("信号值")
ax.set_title(f"两段均值比较 (t-test p≈{float(tt_res.pvalue):.1e})", fontsize=10)
ax.grid(alpha=0.3)
fig.savefig(os.path.join(OUT, "case_stats.png"))
plt.close(fig)

print("figures saved to", OUT)
print("f1=%.2f f2=%.2f area=%.4f tt=%.3f p=%.3e" % (popt[3], popt[6], area, tt_res.statistic, tt_res.pvalue))
for f in sorted(os.listdir(OUT)):
    print("  ", f)
