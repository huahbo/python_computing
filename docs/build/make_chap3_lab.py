# -*- coding: utf-8 -*-
"""Generate lab.ipynb for chapter 03 (SciPy) — guided lab notebook."""
import json, os

cells = []
def md(text): cells.append({"cell_type": "markdown", "metadata": {}, "source": text})
def code(text): cells.append({"cell_type": "code", "metadata": {}, "execution_count": None,
                              "outputs": [], "source": text})

md("""# SciPy 上机实验（第 3 章 lab）

**要求**：按顺序运行每一格，完成所有 `# TODO` 后运行 `检查` 单元；最后截图/导出 notebook 提交。
环境：Python 3.10+，SciPy 1.15+（推荐 1.15.2），NumPy 2.x，Matplotlib 3.x。

---
""")

code("""import numpy as np, scipy, matplotlib
print("NumPy:", np.__version__)
print("SciPy:", scipy.__version__)
print("matplotlib:", matplotlib.__version__)
assert scipy.__version__ >= "1.15", "请升级 SciPy"
print("环境 OK")
""")

md("""## Part 1 微积分工具包

练习：数值积分与常微分方程求解。""")

code("""# 1.1 一维/二重积分与离散梯形积分
from scipy.integrate import quad, dblquad, trapezoid
import numpy as np

val, err = quad(lambda x: x**2, 0, 1)
print("quad int_0^1 x^2 dx =", val, "err =", err)

dbl = dblquad(lambda y, x: x*y, 0, 1, lambda x: 0, lambda x: x)[0]
print("dblquad =", dbl)

x = np.linspace(0, 1, 100)
print("trapezoid =", trapezoid(x**2, x))
""")

code("""# 1.2 求解二阶 ODE: y'' + y = 0, y(0)=1, y'(0)=0
from scipy.integrate import odeint

def sys2(y, t):
    y1, y2 = y
    return [y2, -y1]

t = np.linspace(0, 10, 200)
sol = odeint(sys2, [1, 0], t)
print("y(10) ≈", sol[-1, 0], "  cos(10) ≈", np.cos(10))
from scipy.integrate import solve_ivp
sol2 = solve_ivp(lambda tt, yy: -2*yy, (0,5), [1], t_eval=[5.0])
print("solve_ivp y(5) =", sol2.y[0,-1], "  e^-10 ≈", np.exp(-10))
""")

md("""## Part 2 优化工具包

练习：求根、极值、线性规划、指派、曲线拟合。""")

code("""# 2.1 求根与极小值
from scipy.optimize import brentq, brent
root_val = brentq(lambda x: x**2 - 2, 1, 2)
print("brentq sqrt2 =", root_val)
xmin = brent(lambda x: (x-1)**2, brack=(0,2))
print("brent min (x-1)^2 =", xmin)
from scipy.optimize import minimize
def rosen(v):
    x,y = v
    return (1-x)**2 + 100*(y - x**2)**2
res = minimize(rosen, [-1.2,1.0], method="BFGS")
print("rosen min =", np.round(res.x, 4), "  success =", res.success)
""")

code("""# 2.2 线性规划 + 指派问题
from scipy.optimize import linprog, linear_sum_assignment
res = linprog([1,1], A_ub=[[-1,-2]], b_ub=[-4], bounds=[(0,None),(0,None)], method="highs")
print("LP x =", res.x, "  fun =", res.fun)

cost = np.array([[4,1,3],[2,0,5],[3,2,2]])
ri, ci = linear_sum_assignment(cost)
print("assignment rows/cols =", ri, ci, "  min cost =", cost[ri, ci].sum())
""")

code("""# 2.3 曲线拟合
from scipy.optimize import curve_fit
rng = np.random.default_rng(7)
def model(x, a, b, c):
    return a*x**2 + b*x + c
x = np.linspace(-10, 10, 50)
y = model(x, 2, 3, 1) + rng.normal(0, 2, len(x))
popt, pcov = curve_fit(model, x, y, p0=[0,0,0])
perr = np.sqrt(np.diag(pcov))
print("params =", np.round(popt, 4))
print("stderr =", np.round(perr, 4))
""")

md("""## Part 3 插值工具包

练习：一维样条与多维插值。""")

code("""# 3.1 一维三次样条
from scipy.interpolate import CubicSpline
x = np.array([0,1,2,3,4,5])
y = np.array([0,0.8,0.9,0.1,-0.8,-1])
cs = CubicSpline(x, y)
print("CubicSpline(2.5) =", cs(2.5))
xn = np.linspace(0, 5, 9)
print(np.round(cs(xn), 4))
""")

code("""# 3.2 规则网格上的二维插值
from scipy.interpolate import RegularGridInterpolator
xg = [0,1,2]; yg = [0,1,2]
X, Y = np.meshgrid(xg, yg, indexing="ij")
Z = X + Y
rgi = RegularGridInterpolator((xg, yg), Z, method="linear")
print("RGI(0.5,0.5) =", rgi([[0.5, 0.5]])[0])
print("RGI(1.5,2.0) =", rgi([[1.5, 2.0]])[0])
""")

md("""## Part 4 假设检验工具包

练习：正态性检验、t 检验、方差分析。""")

code("""# 4.1 正态性检验 + t 检验
from scipy.stats import shapiro, ttest_ind
rng = np.random.default_rng(1)
data = rng.normal(0, 1, 100)
p_norm = shapiro(data)[1]
print("shapiro p =", round(p_norm, 4))
s1 = rng.normal(0, 1, 100); s2 = rng.normal(0.5, 1, 100)
t, p = ttest_ind(s1, s2)
print("ttest_ind t =", round(t,4), " p =", round(p,6))
""")

code("""# 4.2 方差分析 + Tukey 事后比较
from scipy.stats import f_oneway
g1 = rng.normal(0, 1, 60); g2 = rng.normal(0.5, 1, 60); g3 = rng.normal(1, 1, 60)
F, p = f_oneway(g1, g2, g3)
print("f_oneway F =", round(F,4), " p =", round(p,8))
try:
    import statsmodels.api as sm
    from statsmodels.stats.multicomp import pairwise_tukeyhsd
    data = np.concatenate([g1,g2,g3])
    groups = np.array(["A"]*60+["B"]*60+["C"]*60)
    print(pairwise_tukeyhsd(data, groups, alpha=0.05))
except ImportError:
    print("未安装 statsmodels，请 pip install statsmodels")
""")

md("""## Part 5 傅里叶变换与滤波

练习：频谱分析与低通滤波。""")

code("""# 5.1 rfft 频谱
from scipy.fft import rfft, rfftfreq
fs = 1000; T = 1.0; N = int(fs*T)
t = np.linspace(0, T, N, endpoint=False)
sig = 0.7*np.sin(2*np.pi*50*t) + np.sin(2*np.pi*200*t)
Y = rfft(sig); freqs = rfftfreq(N, 1/fs)
top = np.argsort(np.abs(Y))[-3:][::-1]
print("top freqs =", np.round(freqs[top], 1), "  amps =", np.round(np.abs(Y[top]), 1))
""")

code("""# 5.2 低通滤波（零相位）
from scipy.signal import butter, filtfilt
b, a = butter(3, 80/(0.5*fs), btype="low")
lp = filtfilt(b, a, sig)
ref = 0.7*np.sin(2*np.pi*50*t)
corr = np.corrcoef(lp[100:], ref[100:])[0,1]
print("低通与 50Hz 参考相关系数 =", round(float(corr), 4))
""")

md("""## Part 6 综合任务：传感器信号分析

按 06 综合案例实现：构造带缺失的数据 → 三次样条补齐 → 去趋势 FFT → curve_fit 拟合 → 积分 → t 检验。""")

code("""# 6.1 综合任务（可参考 ../06-综合案例.md）
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline
from scipy.fft import rfft, rfftfreq
from scipy.optimize import curve_fit
from scipy.integrate import trapezoid
from scipy.stats import ttest_ind

rng = np.random.default_rng(42)
fs = 500; T = 5.0; N = int(fs*T)
t = np.linspace(0, T, N, endpoint=False)
def true_signal(t):
    return 2 + 0.5*t + 1.2*np.sin(2*np.pi*5*t) + 0.3*np.sin(2*np.pi*12*t)
y_true = true_signal(t)
y_raw = y_true + rng.normal(0, 0.2, N)
y_obs = y_raw.copy(); y_obs[150:160] = np.nan
mask = ~np.isnan(y_obs)
cs = CubicSpline(t[mask], y_obs[mask])
y_filled = y_obs.copy(); y_filled[150:160] = cs(t[150:160])
print("插值前 NaN 数 =", int(np.isnan(y_obs).sum()))

coef = np.polyfit(t, y_filled, 1)
detrend = y_filled - np.polyval(coef, t)
Yf = rfft(detrend); fr = rfftfreq(N, 1/fs)
top = np.argsort(np.abs(Yf))[-2:][::-1]
print("FFT 主频 =", np.round(fr[top], 2), "Hz")

def model(t, c1, c2, A1, f1, p1, A2, f2, p2):
    return c1 + c2*t + A1*np.sin(2*np.pi*f1*t+p1) + A2*np.sin(2*np.pi*f2*t+p2)
popt, pcov = curve_fit(model, t, y_filled, p0=[2,0.5,1.2,5,0,0.3,12,0], maxfev=50000)
print("拟合 f1/f2 =", round(popt[3],3), round(popt[6],3))

area = trapezoid(y_filled, t)
g1 = y_filled[(t>=0)&(t<1)]; g2 = y_filled[(t>=4)&(t<5)]
tt = ttest_ind(g1, g2)
print("area =", round(float(area),4), "  ttest p =", float(tt.pvalue))

plt.figure(figsize=(7,3.2))
plt.plot(t, y_filled, lw=1.2, label="补齐后信号")
plt.plot(t, model(t, *popt), "--", lw=1.5, label="拟合曲线")
plt.xlabel("t (s)"); plt.ylabel("信号"); plt.legend(); plt.title("综合任务：信号拟合")
plt.tight_layout(); plt.savefig("sensor_lab.png")
print("已保存 sensor_lab.png")
""")

md("""## Part 7 案例卡跟练（新增）

复现 01–03 三个精讲案例卡：每个案例含“跟练 cell”（复现+改参数）、“变形 cell”（换数据/场景）、“综合任务 cell”（串 2 个技术点）。""")

code("""# 案例 1 跟练：复现 quad + trapezoid，换成高斯被积函数
import numpy as np
from scipy.integrate import quad, trapezoid

def g(x):
    return np.exp(-x**2)

val, err = quad(g, 0, 1)
x = np.linspace(0, 1, 1000)
trap = trapezoid(g(x), x)
print("quad =", round(val, 6), "  err =", round(err, 6))
print("trapezoid n=1000 =", round(trap, 6))
""")

code("""# 案例 1 变形：自由落体速度 v=gt，用 quad 求位移
import numpy as np
from scipy.integrate import quad

g = 9.8
def v(t):
    return g*t

dist, err = quad(v, 0, 3)
print("位移 =", round(float(dist), 4), "  理论 =", round(0.5*g*9, 4))
""")

code("""# 案例 1 综合：trapezoid + quad + curve_fit（积分 + 拟合）
import numpy as np
from scipy.integrate import quad, trapezoid
from scipy.optimize import curve_fit

rng = np.random.default_rng(11)
t = np.linspace(0, 5, 50)
def v(t, a, v0):
    return a*t + v0
y = v(t, 2.0, 0.5) + rng.normal(0, 0.1, t.size)
popt, _ = curve_fit(v, t, y, p0=[1, 0])
print("拟合 a, v0 =", np.round(popt, 4))
area_raw = trapezoid(y, t)
def vfit(x):
    return popt[0]*x + popt[1]
area_fit, _ = quad(vfit, 0, 5)
print("trapezoid 位移 =", round(float(area_raw), 4))
print("quad 拟合位移   =", round(float(area_fit), 4))
""")

code("""# 案例 2 跟练：复现指数衰减拟合，换成 A=3, k=2, C=0
import numpy as np
from scipy.optimize import curve_fit

def decay(t, A, k, C):
    return A*np.exp(-k*t) + C

rng = np.random.default_rng(12)
t = np.linspace(0, 5, 40)
y = decay(t, 3, 2, 0) + rng.normal(0, 0.05, t.size)
popt, pcov = curve_fit(decay, t, y, p0=[1, 1, 0.2])
perr = np.sqrt(np.diag(pcov))
print("A,k,C =", np.round(popt, 4), "  标准误 =", np.round(perr, 4))
""")

code("""# 案例 2 变形：药物浓度模型 C(t)=C0*exp(-k*t)
import numpy as np
from scipy.optimize import curve_fit

rng = np.random.default_rng(13)
t = np.linspace(0, 8, 40)
def conc(t, C0, k):
    return C0*np.exp(-k*t)
y = conc(t, 10, 0.4) + rng.normal(0, 0.2, t.size)
popt, pcov = curve_fit(conc, t, y, p0=[1, 1])
print("C0, k =", np.round(popt, 4))
print("半衰期 =", round(-np.log(0.5)/popt[1], 4), "小时")
""")

code("""# 案例 2 综合：先 CubicSpline 补缺失，再 curve_fit（拟合 + 插值）
import numpy as np
from scipy.interpolate import CubicSpline
from scipy.optimize import curve_fit

rng = np.random.default_rng(21)
t = np.linspace(0, 5, 20)
def decay(t, A, k, C):
    return A*np.exp(-k*t) + C
y = decay(t, 4, 1.2, 0.3) + rng.normal(0, 0.05, t.size)
y2 = y.copy(); y2[[5, 9]] = np.nan
mask = ~np.isnan(y2)
cs = CubicSpline(t[mask], y2[mask])
y2_filled = y2.copy(); y2_filled[~mask] = cs(t[~mask])
popt, pcov = curve_fit(decay, t, y2_filled, p0=[1, 1, 0])
print("样条补全后 A,k,C =", np.round(popt, 4))
""")

code("""# 案例 3 跟练：复现 CubicSpline vs polyfit 补缺失，换缺失位置
import numpy as np
from scipy.interpolate import CubicSpline

rng = np.random.default_rng(3)
x = np.linspace(0, 2*np.pi, 10)
y_true = np.sin(x)
y_obs = y_true + rng.normal(0, 0.05, x.size)
mask_ok = np.ones(x.size, dtype=bool)
mask_ok[[2, 7]] = False
x_ok = x[mask_ok]; y_ok = y_obs[mask_ok]
cs = CubicSpline(x_ok, y_ok)
print("缺失点 =", np.round(x[~mask_ok], 4))
print("CubicSpline 补全 =", np.round(cs(x[~mask_ok]), 4))
""")

code("""# 案例 3 变形：日气温数据缺失，用 CubicSpline 补全
import numpy as np
from scipy.interpolate import CubicSpline

t = np.arange(0, 24, 1)
T = 18 + 6*np.sin(2*np.pi*(t-8)/24)   # 简化日变化
T_obs = T.copy(); T_obs[10] = np.nan
mask = ~np.isnan(T_obs)
cs = CubicSpline(t[mask], T_obs[mask])
print("t=10 补全 =", round(float(cs(10)), 4), "  真值 =", round(float(T[10]), 4))
""")

code("""# 案例 3 综合：CubicSpline 补缺失后 rfft 找主频（插值 + FFT）
import numpy as np
from scipy.interpolate import CubicSpline
from scipy.fft import rfft, rfftfreq

fs = 200; T = 1.0; N = int(fs*T)
t = np.linspace(0, T, N, endpoint=False)
y = np.sin(2*np.pi*5*t)
y_obs = y.copy(); y_obs[100:103] = np.nan
mask = ~np.isnan(y_obs)
cs = CubicSpline(t[mask], y_obs[mask])
y_fill = y_obs.copy(); y_fill[~mask] = cs(t[~mask])
Y = rfft(y_fill); freqs = rfftfreq(N, 1/fs)
top = np.argsort(np.abs(Y))[-1:][::-1]
print("补全后主频 =", round(float(freqs[top[0]]), 2), "Hz")
""")

md("""## 提交清单

- [ ] 所有 TODO 均已填写并运行；
- [ ] Part 1 的 solve_ivp 输出已记录；
- [ ] Part 2 的 Rosenbrock / curve_fit 结果已记录；
- [ ] Part 4 的 Tukey 表已记录（若安装 statsmodels）；
- [ ] Part 5 的高通滤波 TODO 已完成；
- [ ] Part 6 已生成 sensor_lab.png 并写 3 句结论；
- [ ] Part 7 的 9 个跟练/变形/综合 cell 已运行；
- [ ] 导出为 html / 保留 ipynb 提交。

**延伸**：完成 exercises/ 的 16 道题与 06 的拓展任务。""")

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
                   "chapters", "03-scipy", "lab", "lab.ipynb")
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
