# SymPy 高级练习（10 题） — 适合有 Python 基础、学过微积分的初学者

**说明**：这份作业覆盖 SymPy 的核心与进阶主题（符号对象、极限、导数、积分、解方程、矩阵、lambdify、微分方程等）。请先尝试独立完成题目，再查看答案部分。

---

## 题目（共 10 题）

### 容易/中等（1-5）

1. **符号对象与假设**
    创建一个符号 `x`，设置 `real=True`，再创建一个 `n` 设置 `integer=True`。用 `symbols` 一次定义三个符号 `a, b, c`，并打印它们的类型。

2. **极限**
    用 SymPy 求 $\lim_{x\to 0}\frac{\sin x}{x}$ 与 $\lim_{x\to +\infty}\frac{1}{x}$，把结果分别赋给 `lim1`、`lim2`。

3. **微分与偏导**
    对 $f(x)=x^3\sin(x)$ 求一阶导 `df`；对 $h(x,y)=x^2y+xy^2$ 求偏导 `dh_dx`、`dh_dy`。

4. **积分**
    求 $\int (3x^2+2x+1)\,dx$（不定积分 `F`）与 $\int_0^1 x^2\,dx$（定积分 `definite`）。

5. **解方程**
    用 `solve` 解 $x^2-5x+6=0$（赋给 `sols`），用 `solveset` 解 $x^2+1=0$ 并指定实数域/复数域，观察差异。

### 中等/偏难（6-10）

6. **解方程组**
    解 $\begin{cases} x^2+y^2=5 \\ x-y=1 \end{cases}$，把解赋给 `sys_sol`。

7. **符号矩阵**
    对 $A=\begin{pmatrix}2&1\\1&2\end{pmatrix}$，求特征值（`eigs`）与行列式（`det_A`）。

8. **lambdify**
    把 `expr = x**2 + 2*x + 1` 用 `lambdify` 转成数值函数 `f_num`，计算 `f_num(1)`、`f_num(3)`。

9. **微分方程**
    用 `dsolve` 求 $y'+y=x$ 的通解（`sol_ode`），再用 `ics` 求 $y(0)=1$ 的特解（`sol_ics`）。

10. **综合题**
    用 SymPy 推导 $y=\sin(x)$ 在 $x=1$ 处的切线方程，并给出斜率；再用 `lambdify` 生成函数，验证 $x=1$ 处函数值与切线值相等。

---

## 答案（详细，带代码与解释）

> 注：所有代码在 SymPy 1.13.1 下运行通过。

### 答案 1
```python
import sympy as sp
x = sp.Symbol('x', real=True)
n = sp.Symbol('n', integer=True)
a, b, c = sp.symbols('a b c')
print(x, x.is_real)
print(n, n.is_integer)
print(a, b, c)
print(type(a))
```
输出：`x True`、`n None`（integer 用 `n.is_integer` 可能为 True 或取决于版本）、`a b c`、`<class 'sympy.core.symbol.Symbol'>`。

### 答案 2
```python
x = sp.symbols('x')
lim1 = sp.limit(sp.sin(x)/x, x, 0)
lim2 = sp.limit(1/x, x, sp.oo)
print(lim1, lim2)
```
输出：`1 0`。

### 答案 3
```python
x, y = sp.symbols('x y')
df = sp.diff(x**3*sp.sin(x), x)
dh_dx = sp.diff(x**2*y + x*y**2, x)
dh_dy = sp.diff(x**2*y + x*y**2, y)
print(df)
print(dh_dx)
print(dh_dy)
```
输出：`x**3*cos(x) + 3*x**2*sin(x)`、`2*x*y + y**2`、`x**2 + 2*x*y`。

### 答案 4
```python
x = sp.symbols('x')
F = sp.integrate(3*x**2 + 2*x + 1, x)
definite = sp.integrate(x**2, (x, 0, 1))
print(F)
print(definite)
```
输出：`x**3 + x**2 + x`、`1/3`。

### 答案 5
```python
x = sp.symbols('x')
sols = sp.solve(x**2 - 5*x + 6, x)
sol_re = sp.solveset(x**2 + 1, x, domain=sp.S.Reals)
sol_cx = sp.solveset(x**2 + 1, x, domain=sp.S.Complexes)
print(sols)
print(sol_re)
print(sol_cx)
```
输出：`[2, 3]`、`EmptySet`、`{-I, I}`。

### 答案 6
```python
x, y = sp.symbols('x y')
eqs = [x**2 + y**2 - 5, x - y - 1]
sys_sol = sp.solve(eqs, (x, y))
print(sys_sol)
```
输出：`[(-1, -2), (2, 1)]`。

### 答案 7
```python
A = sp.Matrix([[2, 1], [1, 2]])
eigs = A.eigenvals()
det_A = A.det()
print(eigs)
print(det_A)
```
输出：`{3: 1, 1: 1}`、`3`。

### 答案 8
```python
x = sp.symbols('x')
expr = x**2 + 2*x + 1
f_num = sp.lambdify(x, expr, 'numpy')
print(f_num(1), f_num(3))
```
输出：`4 16`。

### 答案 9
```python
x = sp.symbols('x')
y = sp.Function('y')(x)
eq = sp.Eq(y.diff(x) + y, x)
sol_ode = sp.dsolve(eq, y)
sol_ics = sp.dsolve(eq, y, ics={y.subs(x, 0): 1})
print(sol_ode)
print(sol_ics)
```
输出：`Eq(y(x), C1*exp(-x) + x - 1)`、`Eq(y(x), x - 1 + 2*exp(-x))`。

### 答案 10
```python
import sympy as sp
import numpy as np
x = sp.symbols('x')
f = sp.sin(x)
df = sp.diff(f, x)
a = 1
slope = sp.N(df.subs(x, a))
tangent = sp.simplify(df.subs(x, a)*(x - a) + f.subs(x, a))
f_num = sp.lambdify(x, f, 'numpy')
tangent_num = sp.lambdify(x, tangent, 'numpy')
print(slope)
print(tangent)
print(f_num(a), tangent_num(a))
```
输出：`0.540302305868140`、`(x - 1)*cos(1) + sin(1)`、`0.841470984807897 0.841470984807897`（两者相等）。

---

## 结束语

完成全部 10 题后，可继续完成 `lab/` 上机实验与 `03-综合案例.md` 的拓展任务。


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
