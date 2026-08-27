# SciPy 进阶练习（16 题） — 第 3 章

**说明**：覆盖 `scipy.integrate`、`scipy.optimize`、`scipy.interpolate`、`scipy.stats`、`scipy.fft`/`scipy.signal`。请先独立完成题目，再查看答案。所有代码在 SciPy 1.15.2 环境验证。

---

## 题目（共 16 题）

### 容易（1–5）

1. **一维定积分**：用 `scipy.integrate.quad` 计算 $\int_0^1 x^2 dx$，结果放在 `integral_val`，并验证它接近 $1/3$。

2. **二重积分**：用 `dblquad` 计算 $\int_0^1\int_0^x xy\,dy\,dx$，结果放在 `dbl_val`。

3. **一阶 ODE**：用 `solve_ivp`（或 `odeint`）求解 $dy/dt=-2y,\ y(0)=1$ 在 $t\in[0,5]$ 上的解，把 $y(5)$ 放在 `y_end`，验证接近 $e^{-10}$。

4. **一维求根**：用 `brentq` 求 $x^2-2=0$ 在 $[1,2]$ 的根，放在 `root_val`。

5. **一维极小值**：用 `brent`（或 `minimize_scalar`）求 $f(x)=(x-1)^2$ 的极小值点，放在 `xmin`。

### 中等（6–11）

6. **指派问题**：用 `linear_sum_assignment` 对成本矩阵 `[[4,1,3],[2,0,5],[3,2,2]]` 求最小总成本，放在 `min_cost`。

7. **线性规划**：用 `linprog` 最小化 $x_1+x_2$，约束 $x_1+2x_2\ge4$，$x_1,x_2\ge0$，最优解放在 `lp_x`。

8. **Rosenbrock 无约束优化**：用 `minimize(method='BFGS')` 从 $(-1.2,1)$ 出发最小化 $f=(1-x)^2+100(y-x^2)^2$，最优点放在 `rosen_x`。

9. **曲线拟合**：生成 $y=2x^2+3x+1+\varepsilon$（`default_rng(0)`，噪声 `0.2`），用 `curve_fit` 拟合参数，放在 `params`（长度为 3）。

10. **一维插值**：对 `x=[0,1,2], y=[0,1,0]` 用 `CubicSpline` 计算 $x=0.5$ 处的插值，放在 `interp05`。

11. **多维插值**：用 `RegularGridInterpolator` 对网格 `x=[0,1,2], y=[0,1,2]`、$z=x+y$ 计算点 $(0.5,0.5)$ 处的值，放在 `grid_val`。

### 中偏难（12–16）

12. **正态性检验**：用 `default_rng(1)` 生成 100 个标准正态样本，做 `shapiro` 检验，把 p 值放在 `p_norm`，验证 $p>0.05$。

13. **独立样本 t 检验**：生成两组正态样本（均值 0 与 0.5，标准差 1，各 100 个），做 `ttest_ind`，把 p 值放在 `p_tt`，验证 $p<0.05$。

14. **卡方独立性检验**：对列联表 `[[10,20],[30,40]]` 做 `chi2_contingency`，把 p 值放在 `p_chi`。

15. **FFT 主频**：生成 $\sin(2\pi\cdot5t)$，采样率 $fs=100$ Hz、时长 1 s，用 `rfft`/`rfftfreq` 找峰值频率，放在 `peak_freq`。

16. **低通滤波**：构造 $0.7\sin(2\pi\cdot50t)+\sin(2\pi\cdot200t)$（$fs=1000$ Hz、1 s），用 `butter`+`filtfilt`（零相位）设计 3 阶、截止 80 Hz 的低通，计算滤波输出与“纯 50 Hz 参考信号”的相关系数，放在 `corr_lp`，验证大于 0.9。

---

## 答案

### 答案 1
```python
import numpy as np
from scipy.integrate import quad
integral_val = quad(lambda x: x**2, 0, 1)[0]
print(integral_val)
# 0.33333333333333337
```

### 答案 2
```python
from scipy.integrate import dblquad
dbl_val = dblquad(lambda y, x: x*y, 0, 1, lambda x: 0, lambda x: x)[0]
print(dbl_val)   # 0.125
```

### 答案 3
```python
from scipy.integrate import solve_ivp
import numpy as np
def deriv(t, y): return -2*y
sol = solve_ivp(deriv, (0,5), [1], t_eval=[5.0])
y_end = sol.y[0,-1]
print(y_end)   # 4.572378941563548e-05, 与 e^-10≈4.54e-5 一致
```

### 答案 4
```python
from scipy.optimize import brentq
root_val = brentq(lambda x: x**2-2, 1, 2)
print(root_val)   # 1.4142135623731364
```

### 答案 5
```python
from scipy.optimize import brent
xmin = brent(lambda x: (x-1)**2, brack=(0,2))
print(xmin)   # 0.9999999999999998
```

### 答案 6
```python
import numpy as np
from scipy.optimize import linear_sum_assignment
cost = np.array([[4,1,3],[2,0,5],[3,2,2]])
ri, ci = linear_sum_assignment(cost)
min_cost = int(cost[ri, ci].sum())
print(ri, ci, min_cost)   # [0 1 2] [1 0 2] 5
```

### 答案 7
```python
from scipy.optimize import linprog
res = linprog([1,1], A_ub=[[-1,-2]], b_ub=[-4], bounds=[(0,None),(0,None)], method='highs')
lp_x = list(res.x)
print(lp_x)   # [0.0, 2.0], 目标值 2.0
```

### 答案 8
```python
import numpy as np
from scipy.optimize import minimize
def rosen(v):
    x, y = v
    return (1-x)**2 + 100*(y-x**2)**2
res = minimize(rosen, [-1.2, 1.0], method='BFGS')
rosen_x = list(res.x)
print(rosen_x)   # ≈ [1.0, 1.0]
```

### 答案 9
```python
import numpy as np
from scipy.optimize import curve_fit
np.random.seed(0)
def model(x, a, b, c): return a*x**2 + b*x + c
xdata = np.linspace(-5, 5, 100)
ydata = model(xdata, 2, 3, 1) + np.random.normal(0, 0.2, xdata.shape)
params, pcov = curve_fit(model, xdata, ydata, p0=[1,1,1])
print(params)   # 接近 [2,3,1]
```

### 答案 10
```python
from scipy.interpolate import CubicSpline
import numpy as np
cs = CubicSpline([0,1,2], [0,1,0])
interp05 = float(cs(0.5))
print(interp05)   # 0.75（三次样条的合理值）
```

### 答案 11
```python
import numpy as np
from scipy.interpolate import RegularGridInterpolator
x = [0,1,2]; y = [0,1,2]
X, Y = np.meshgrid(x, y, indexing='ij')
Z = X + Y
rgi = RegularGridInterpolator((x, y), Z)
grid_val = float(rgi([[0.5,0.5]])[0])
print(grid_val)   # 1.0
```

### 答案 12
```python
import numpy as np
from scipy.stats import shapiro
rng = np.random.default_rng(1)
data = rng.normal(0, 1, 100)
p_norm = shapiro(data)[1]
print(p_norm)   # 0.137
```

### 答案 13
```python
import numpy as np
from scipy.stats import ttest_ind
rng = np.random.default_rng(1)
s1 = rng.normal(0, 1, 100); s2 = rng.normal(0.5, 1, 100)
p_tt = ttest_ind(s1, s2)[1]
print(p_tt)   # ≈0.0026
```

### 答案 14
```python
import numpy as np
from scipy.stats import chi2_contingency
p_chi = chi2_contingency(np.array([[10,20],[30,40]]))[1]
print(p_chi)   # 0.504
```

### 答案 15
```python
import numpy as np
from scipy.fft import rfft, rfftfreq
fs = 100; T = 1.0
t = np.linspace(0, T, fs, endpoint=False)
sig = np.sin(2*np.pi*5*t)
Y = rfft(sig); freqs = rfftfreq(len(t), 1/fs)
peak_freq = float(freqs[np.argmax(np.abs(Y))])
print(peak_freq)   # 5.0
```

### 答案 16
```python
import numpy as np
from scipy.signal import butter, lfilter
fs = 1000; T = 1.0
t = np.linspace(0, T, int(fs*T), endpoint=False)
sig = 0.7*np.sin(2*np.pi*50*t) + np.sin(2*np.pi*200*t)
from scipy.signal import filtfilt
b, a = butter(3, 80/(0.5*fs), btype='low')
lp = filtfilt(b, a, sig)   # 零相位滤波，避免相位延迟
ref = 0.7*np.sin(2*np.pi*50*t)
corr_lp = float(np.corrcoef(lp[100:], ref[100:])[0,1])
print(corr_lp)   # >0.9（约 0.996）
```

---

## 结束语

完成以上题目后再做 `lab/` 上机与 `06-综合案例.md`，即可把本章知识串成一条完整流水线。


---

## 补充题（来自旧题库，仅作挑战/选做）

> 来源：`docs/原始资料/chapter_2_3_quiz`（已归档）。以下题目未纳入 quiz.ipynb 自动评分，可作为课堂挑战或额外练习；每题给答案要点。

### 补充 1（二阶 ODE 转一阶组求解）
把 `y'' + y = 0`（`y(0)=1, y'(0)=0`）转为一阶方程组，用 `odeint`/`solve_ivp` 在 `t = np.linspace(0, 2*pi, 100)` 上求解，结果存入 `y_sol`。
**答案要点**：令 `y1=y, y2=y'`，`dy1 = y2, dy2 = -y1`；初值 `[1, 0]`。

### 补充 2（optimize.root 解非线性方程组）
用 `scipy.optimize.root` 求解 `[x**2 + y - 3, x + y**2 - 3]`，初值 `(1, 1)`，解保存到 `root_sol`。
**答案要点**：`root(lambda z: [z[0]**2 + z[1] - 3, z[0] + z[1]**2 - 3], [1, 1])`。

### 补充 3（Lorenz 系统数值解）
用 `solve_ivp` 求 Lorenz 系统 `sigma=10, rho=28, beta=8/3`，初值 `(0., 1., 0.)`，`t\in[0,2]`，结果保存为 `sol_lorenz`。
**答案要点**：标准 Lorenz 方程 `dx = sigma*(y-x), dy = x*(rho-z)-y, dz = x*y - beta*z`，用 `solve_ivp(fun, [0, 2], [0., 1., 0.], t_eval=...)`。

### 补充 4（正弦信号 curve_fit 恢复频率）
拟合 `y = A*sin(2*pi*f*t + phi)`，从含噪数据恢复频率 `f`（初估 5 Hz），保存到 `est_f`。
**答案要点**：`curve_fit(model, t, y, p0=[1, 5, 0])`，其中 `model(t, A, f, phi)`；`est_f = popt[1]`。
