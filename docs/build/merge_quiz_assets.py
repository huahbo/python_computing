# -*- coding: utf-8 -*-
"""M1.3: append old-quiz challenge questions to ch2/ch3 assignment.md + README notes."""
import io, os

CH2_EXTRA = """

---

## 补充题（来自旧题库，仅作挑战/选做）

> 来源：`docs/原始资料/chapter_2_3_quiz`（已归档）。以下题目未纳入 quiz.ipynb 自动评分，可作为课堂挑战或额外练习；每题给答案要点。

### 补充 1（nonlinsolve 解非线性方程组）
用 SymPy 的 `nonlinsolve` 解方程组 `[x**2 + y**2 - 2, x**3 + y**3]`，解保存到 `sols_nonlin`。
**答案要点**：`x, y = symbols('x y'); sols_nonlin = nonlinsolve([x**2 + y**2 - 2, x**3 + y**3], [x, y])`。

### 补充 2（二阶常系数 ODE 通解）
用 `dsolve` 求 `y'' - 2*y' + y = 0` 的通解，保存到 `sol2`。
**答案要点**：`y = Function('y')(x); sol2 = dsolve(Eq(y.diff(x, 2) - 2*y.diff(x) + y, 0), y)`。

### 补充 3（拉格朗日乘子法：解析最优化）
最小化 `f(x, y) = x**2 + y**2`，约束 `x + y - 1 = 0`。用拉格朗日乘子法得到解 `opt_xy`。
**答案要点**：构造 `L = f + lam*(x + y - 1)`，对 `x, y, lam` 求导并 `solve`；结果为 `x = y = 1/2`，`opt_xy = (1/2, 1/2)`。

### 补充 4（符号导数 + 数值差商验证）
用 SymPy 推导 `y = sin(x)**2` 的导数并 `lambdify`，在 `x = 0.7` 处与中心差商比较（误差 < 1e-6）。
**答案要点**：`dy = diff(sin(x)**2, x)`；`f = lambdify(x, dy, 'numpy')`；中心差商 `(sin(0.7+h)**2 - sin(0.7-h)**2)/(2*h)`，取 `h=1e-5` 验证。

### 补充 5（Logistic 微分方程解析解）
用 `dsolve` 求解 `dx/dt = r*x*(1 - x/K)`，初值 `x(0) = x0`（r、K、x0 可取符号或数值，例如 r=1, K=10, x0=0.1），解析解保存到 `sol_logistic`。
**答案要点**：`x = Function('x')(t); sol_logistic = dsolve(Eq(x.diff(t), r*x*(1 - x/K)), x, ics={x.subs(t, 0): x0})`。
"""

CH3_EXTRA = """

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
"""

def append_if_absent(path, text, marker):
    if not os.path.exists(path):
        print("[missing]", path); return
    with io.open(path, encoding="utf-8") as f:
        content = f.read()
    if marker in content:
        print("[skip ]", path); return
    with io.open(path, "a", encoding="utf-8") as f:
        f.write(text)
    print("[append]", path)

append_if_absent("chapters/02-sympy/exercises/assignment.md", CH2_EXTRA, "补充题（来自旧题库")
append_if_absent("chapters/03-scipy/exercises/assignment.md", CH3_EXTRA, "补充题（来自旧题库")

NOTE2 = """

## 旧题库说明

- 旧题库 `docs/原始资料/chapter_2_3_quiz`（SymPy & SciPy 30 题）已仅归档，不再作为教学入口；
- 其中未进入本 quiz 的挑战题（nonlinsolve、二阶 ODE、拉格朗日乘子、导数+数值验证、Logistic 等）已并入 `assignment.md` 的“补充题”。
"""
append_if_absent("chapters/02-sympy/exercises/README.md", NOTE2, "旧题库说明")

NOTE3 = """

## 旧题库说明

- 旧题库 `docs/原始资料/chapter_2_3_quiz`（SymPy & SciPy 30 题）已仅归档，不再作为教学入口；
- 其中未进入本 quiz 的挑战题（二阶 ODE 转一阶组、`optimize.root`、Lorenz、正弦 `curve_fit` 等）已并入 `assignment.md` 的“补充题”。
"""
append_if_absent("chapters/03-scipy/exercises/README.md", NOTE3, "旧题库说明")
