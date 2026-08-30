# 02 利用 SymPy 求解问题：方程、矩阵、lambdify 与微分方程

> 本节对应原版 2.2 的内容，并增补学习目标、常见误区、思考题与延伸阅读。
> 所有代码输出均为实际运行结果（SymPy 1.13.1）。

## 本节目标

- 会用 `Eq` 表示等式，理解“把表达式当作等于 0”的约定；
- 掌握 `solve`、`solveset`、`linsolve`、`nonlinsolve` 解方程与方程组；
- 会用 Symbolic `Matrix` 做矩阵运算、求特征值、计算雅可比矩阵；
- 会用 `lambdify` 把符号表达式转成可调用的 NumPy 函数，实现符号→数值的对接；
- 会用 `dsolve` 求一阶、二阶常微分方程的通解与初值解。

## 先修

- 01 节全部内容（符号创建、极限、微分、积分）；
- 线性代数基础（矩阵乘法、行列式、逆、特征值）。

## 官方文档/参考入口

- SymPy 官方 Solvers：[链接](https://docs.sympy.org/latest/modules/solvers/index.html)
- SymPy 官方 lambdify：[链接](https://docs.sympy.org/latest/modules/utilities/lambdify.html)
- SymPy 官方 ODE：[链接](https://docs.sympy.org/latest/modules/solvers/ode.html)

---

## 2.1 用 SymPy 解方程

### 2.1.1 用 `Eq` 表示等式

```python
x = sp.symbols('x')
equation = sp.Eq(x**2, 4)
print(sp.solveset(equation, x))
```

```text
{-2, 2}
```

> 如果不写 `Eq`，直接把表达式传给求解函数，SymPy 默认认为该表达式等于 0：

```python
x = sp.symbols('x')
print(sp.solveset(x**2 - 4, x))
```

```text
{-2, 2}
```

### 2.1.2 `solve` 解一元方程

```python
x = sp.symbols('x')
print(sp.solve(3*x + 4 - 10, x))          # 3x+4=10 -> x=2
print(sp.solve(x**2 + 5*x + 4, x))        # x^2+5x+4=0 -> -4, -1
```

```text
[2]
[-4, -1]
```

### 2.1.3 `solveset` 与解集/复数域

```python
x = sp.symbols('x')
print(sp.solveset(x**2 - 5*x + 6, x))                       # {2,3}
print(sp.solveset(2*x**2 + 4*x + 2, x))                     # 重根
print(sp.solveset(x**2 + 1, x, domain=sp.S.Complexes))      # 复数域
```

```text
{2, 3}
{-1}
{-I, I}
```

| 函数 | 返回 | 特点 |
| ---- | ---- | ---- |
| `solve` | 列表 `[...]` | 传统易读，适合大多数方程 |
| `solveset` | 集合 `{...}` | 解集表达更严谨，支持 domain |

### 2.1.4 解方程组

解 $\begin{cases} 2x+3y=5 \\ 4x-2y=10\end{cases}$：

```python
x, y = sp.symbols('x y')
eqs = [2*x + 3*y - 5, 4*x - 2*y - 10]
print(sp.solve(eqs, (x, y)))
```

```text
{x: 5/2, y: 0}
```

解非线性方程组 $\begin{cases} x^2+y^2=5 \\ x-y=1\end{cases}$：

```python
x, y = sp.symbols('x y')
eqs = [x**2 + y**2 - 5, x - y - 1]
print(sp.solve(eqs, (x, y)))
```

```text
[(-1, -2), (2, 1)]
```

> 复杂的非线性方程组可能返回复数解、`RootOf` 对象或空列表，需要结合题目与 `domain` 参数判断。

### 2.1.5 `linsolve` 解线性方程组

```python
x, y, z = sp.symbols('x y z')
eqs = [x + y + z - 2, 2*x - y + z + 1, x + 2*y + 2*z - 3]
print(sp.linsolve(eqs, (x, y, z)))
```

```text
{(1, 2, -1)}
```

也可以用系数矩阵 $A$ 与常数向量 $b$：

```python
A = sp.Matrix([[1, 1, 1], [2, -1, 1], [1, 2, 2]])
b = sp.Matrix([2, -1, 3])
print(sp.linsolve((A, b), (x, y, z)))
```

```text
{(1, 2, -1)}
```

### 2.1.6 `nonlinsolve` 解非线性方程组

```python
x, y = sp.symbols('x y')
eqs = [x**2 + y**2 - 2, x**3 + y**3]
print(sp.nonlinsolve(eqs, (x, y)))
```

```text
{(-1, 1), (1, -1), ((-1 - sqrt(3)*I)*sqrt(1 - sqrt(3)*I)/2, -sqrt(1 - sqrt(3)*I)), ((1 - sqrt(3)*I)*sqrt(1 + sqrt(3)*I)/2, sqrt(1 - sqrt(3)*I)), ...}
```

> 该结果包含两个实数解 $(-1,1)$、$(1,-1)$ 和若干复数解。实际题目若只关心实数解，可在此基础上筛选。

## 2.2 用 Symbolic `Matrix` 做矩阵运算

### 2.2.1 基本运算

```python
A = sp.Matrix([[1, 2], [3, 4]])
B = sp.Matrix([[5, 6], [7, 8]])
print(A + B)
print(A * B)
print(A.det())
print(A.inv())
print(A.solve(sp.Matrix([1, 2])))
print(A**2)
```

```text
Matrix([[6, 8], [10, 12]])
Matrix([[19, 22], [43, 50]])
-2
Matrix([[-2, 1], [3/2, -1/2]])
Matrix([[0], [1/2]])
Matrix([[7, 10], [15, 22]])
```

### 2.2.2 特征值

```python
A = sp.Matrix([[2, 1], [1, 2]])
print(A.eigenvals())
print(A.eigenvects())
```

```text
{3: 1, 1: 1}
[(1, 1, [Matrix([
[-1],
[ 1]])]), (3, 1, [Matrix([
[1],
[1]])])]
```

### 2.2.3 雅可比矩阵

```python
x, y = sp.symbols('x y')
f1 = x**2 + y
f2 = sp.sin(x) - y**2
J = sp.Matrix([f1, f2]).jacobian([x, y])
print(J)
```

```text
Matrix([[2*x, 1], [cos(x), -2*y]])
```

## 2.3 用 `lambdify` 把符号表达式变成数值函数

`lambdify` 是 SymPy 与 NumPy 之间的“桥梁”：把符号表达式编译成可调用的 Python/NumPy 函数，便于对大数组做高效数值计算。

```python
import sympy as sp
x = sp.symbols('x')
expr = x**2 + 2*x + 1
f = sp.lambdify(x, expr, 'numpy')
print(f(1))
print(f(2))
f_basic = sp.lambdify(x, expr)
print(f_basic(1))
```

```text
4
9
4
```

传入 NumPy 数组：

```python
import sympy as sp, numpy as np
x = sp.symbols('x')
f = sp.lambdify(x, sp.sin(x)**2, 'numpy')
print(f(np.array([0, np.pi/2, np.pi])))
```

```text
[0.00000000e+00 1.00000000e+00 1.49975978e-32]
```

> **注意**：`lambdify` 生成的是数值函数，返回的是 NumPy 数组或标量；`f(1)` 返回 4（不是原文档里误写的 3）。

## 2.4 用 `dsolve` 解常微分方程

### 2.4.1 一阶线性微分方程 $y'+y=x$

```python
x = sp.symbols('x')
y = sp.Function('y')(x)
eq = sp.Eq(y.diff(x) + y, x)
print(sp.dsolve(eq, y))
```

```text
Eq(y(x), C1*exp(-x) + x - 1)
```

### 2.4.2 二阶常系数齐次方程 $y''-2y'+y=0$

```python
x = sp.symbols('x')
y = sp.Function('y')(x)
eq = sp.Eq(y.diff(x, 2) - 2*y.diff(x) + y, 0)
print(sp.dsolve(eq, y))
```

```text
Eq(y(x), (C1 + C2*x)*exp(x))
```

### 2.4.3 初值问题（`ics` 参数）

```python
x = sp.symbols('x')
y = sp.Function('y')(x)
eq = sp.Eq(y.diff(x) + y, x)
print(sp.dsolve(eq, y, ics={y.subs(x, 0): 1}))
```

```text
Eq(y(x), x - 1 + 2*exp(-x))
```

### 2.4.4 微分方程组

$$\begin{cases} \frac{dx}{dt}=y \\ \frac{dy}{dt}=-x\end{cases}$$

```python
t = sp.symbols('t')
xf = sp.Function('x')(t)
yf = sp.Function('y')(t)
eq1 = sp.Eq(xf.diff(t), yf)
eq2 = sp.Eq(yf.diff(t), -xf)
print(sp.dsolve([eq1, eq2], dict=True))
```

```text
[Eq(x(t), C1*sin(t) + C2*cos(t)), Eq(y(t), C1*cos(t) - C2*sin(t))]
```

### 2.4.5 逻辑斯蒂模型（含初值）

$$\frac{dx}{dt}=r x\left(1-\frac{x}{K}\right),\ x(0)=x_0$$

```python
import sympy as sp
x = sp.symbols('x', cls=sp.Function)
x0, t, r, K = sp.symbols('x0 t r K', real=True, positive=True)
sol = sp.dsolve(sp.Eq(x(t).diff(t), r*x(t)*(1 - x(t)/K)), ics={x(0): x0})
print(sol)
```

```text
Eq(x(t), K*x0*exp(r*t)/((-K + x0)*(x0*exp(r*t)/(-K + x0) - 1)))
```

> 注：`dsolve` 求解的是**解析解**；对无法解析求解的复杂方程，应改用 SciPy 的 `solve_ivp`/`odeint` 做数值解（详见后续章节）。

## 常见误区

1. **混淆 `solve` 与 `solveset` 的返回类型**：`solve` 返回列表，`solveset` 返回集合；两者都不一定能给出闭式解。
2. **忘记 `Eq` 的两种写法**：`sp.Eq(x**2, 4)` 与直接传 `x**2 - 4` 等价，但若写成 `[x**2, y**2]` 会被当成“两个方程都等于 0”。
3. **把 `lambdify` 的结果当符号**：它是数值函数，输入是数字/数组，输出是数值；不要再对它调用 `diff`、`subs`。
4. **用 `Matrix` 做逐元素乘法**：SymPy 的 `A * B` 是**矩阵乘法**，而 `A.dot(B)` 也做矩阵乘；没有 NumPy 里的 `*` 逐元素语义。
5. **`dsolve` 的 `ics` 用错格式**：初值应写成字典，如 `{y.subs(x, 0): 1}`（y 需先定义为 `Function('y')(x)`）。
6. **以为 `linsolve` 总能给唯一解**：无解返回 `EmptySet`，无穷多解返回带参数的解集。

## 思考题

1. 为什么 `sp.solve([x**2 + y**2 - 5, x - y - 1], (x, y))` 会返回列表而不是字典？它与 2.1.4 的线性方程组返回字典有何不同？
2. `lambdify` 的第三个参数为什么建议用 `'numpy'`？不指定时对数组输入会怎样？
3. 用 `Matrix.solve` 与 `linsolve` 解同一个方程，结果形式有何区别？
4. `dsolve` 返回的通解中 $C_1$、$C_2$ 是什么？如何用 `ics` 消去它们？

## 动手练习（详见 lab）

- 用 `solve` 与 `solveset` 分别解 $x^3-6x^2+11x-6=0$，比较返回形式；
- 用 `linsolve` 解一个三元欠定方程组（无穷多解）并观察输出；
- 用 `lambdify` 把 $f(x,y)=x^2+xy+y^2$ 转成可接受二维数组的函数；
- 用 `dsolve` 求 $y''+4y=0$ 的通解并写出含 $\sin(2x)$、$\cos(2x)$ 的形式。

## 延伸阅读

- SymPy 官方 Solvers 文档：[链接](https://docs.sympy.org/latest/modules/solvers/index.html)
- SymPy 官方 Matrix 文档：[链接](https://docs.sympy.org/latest/modules/matrices/index.html)
- SymPy 官方 lambdify 参考：[链接](https://docs.sympy.org/latest/modules/utilities/lambdify.html)
- SymPy 官方 ODE（dsolve）文档：[链接](https://docs.sympy.org/latest/modules/solvers/ode.html)
