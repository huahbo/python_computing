### 旧题库 2&3 合订（../chapter_2_3_quiz/SymPy_SciPy_test_questions.ipynb，30 题）

1. **### 题 1** :: ### 题 1 （难度：easy）  使用 SymPy 创建符号变量 x, y 并构造表达式 f(x,y)=x^2 + 2*x*y + y^2。请在代码区定义变量 x,y 和 expr 。  <details> <summary>提示（点击展开）</summary>  提示：from sympy import symbols ; x,y = symbols('x y')  </details>  请在下面的代码单元中实现（保留题中要求的变量名）。
2. **### 题 2** :: ### 题 2 （难度：easy）  对上一题中的 expr 对 x 求偏导，得到 ∂f/∂x 。在代码区定义 df_dx 。  <details> <summary>提示（点击展开）</summary>  提示：使用 diff(expr, x)  </details>  请在下面的代码单元中实现（保留题中要求的变量名）。
3. **### 题 3** :: ### 题 3 （难度：easy）  使用 SymPy 求极限：lim_{x->0} sin(x)/x。请定义 lim_val 。  <details> <summary>提示（点击展开）</summary>  提示：from sympy import limit, sin, symbols ; limit(sin(x)/x, x, 0)  </details>  请在下面的代码单元中实现（保留题中要求的变量名）。
4. **### 题 4** :: ### 题 4 （难度：easy）  用 SymPy 求不定积分 ∫ (3*x**2) dx，定义 F 。  <details> <summary>提示（点击展开）</summary>  提示：use integrate  </details>  请在下面的代码单元中实现（保留题中要求的变量名）。
5. **### 题 5** :: ### 题 5 （难度：easy）  把 SymPy 表达式 expr（x**2 + 2*x*y + y**2）用 lambdify 转换为可以接受 numpy 数组的函数 f_num，并计算 f_num(1,2)。  <details> <summary>提示（点击展开）</summary>  提示：sp.lambdify((x,y), expr, 'numpy')  </details>  请在下面的代码单元中实现（保留题中要求的变量名）。
6. **### 题 6** :: ### 题 6 （难度：easy）  使用 SciPy 的 quad 计算定积分 ∫_0^1 x^2 dx，并把结果放在 integral_val 。  <details> <summary>提示（点击展开）</summary>  提示：from scipy.integrate import quad  </details>  请在下面的代码单元中实现（保留题中要求的变量名）。
7. **### 题 7** :: ### 题 7 （难度：easy）  使用 SciPy 的 optimize.minimize_scalar 寻找 f(x)=(x-1)**2 的最小点（x=1）。定义 xmin_brent 。  <details> <summary>提示（点击展开）</summary>  提示：from scipy.optimize import minimize_scalar  </details>  请在下面的代码单元中实现（保留题中要求的变量名）。
8. **### 题 8** :: ### 题 8 （难度：easy）  使用 SciPy 的 linear_sum_assignment 解决成本矩阵 [[4,1,3],[2,0,5],[3,2,2]]，返回 row_ind, col_ind 并计算最小总成本 min_cost_val 。  <details> <summary>提示（点击展开）</summary>  提示：from scipy.optimize import linear_sum_assignment  </details>  请在下面的代码单元中实现（保留题中要求的变量名）。
9. **### 题 9** :: ### 题 9 （难度：easy）  使用 SymPy 的 solveset 求方程 x**2-5*x+6=0 的解集，并把结果放在 sols。  <details> <summary>提示（点击展开）</summary>  提示：solveset(expr, x) 或 solve  </details>  请在下面的代码单元中实现（保留题中要求的变量名）。
10. **### 题 10** :: ### 题 10 （难度：easy）  用 SymPy dsolve 求 y' + y = x 的通解（符号求解）。把结果放在 sol_dsolve 。  <details> <summary>提示（点击展开）</summary>  提示：use Function and dsolve  </details>  请在下面的代码单元中实现（保留题中要求的变量名）。
11. **### 题 11** :: ### 题 11 （难度：medium）  用 SymPy 求矩阵方程 A * v = b 的解，其中 A = Matrix([[1,1,1],[2,-1,1],[1,2,2]]) 和 b = Matrix([2,-1,3])，使用 linsolve。请把解赋予 sol_vec。  <details> <summary>提示（点击展开）</summary>  提示：from sympy import Matrix, linsolve  </details>  请在下面的代码单元中实现（保留题中要求的变量名）。
12. **### 题 12** :: ### 题 12 （难度：medium）  用 SymPy 的 nonlinsolve 解方程组 [x**2 + y**2 -2, x**3 + y**3]，并把解放在 sols_nonlin。  <details> <summary>提示（点击展开）</summary>  提示：nonlinsolve(eqs, (x,y))  </details>  请在下面的代码单元中实现（保留题中要求的变量名）。
13. **### 题 13** :: ### 题 13 （难度：medium）  用 lambdify 将 SymPy 表达式 sin(x)**2 转换为 numpy 函数并计算在数组 [0, pi/2, pi] 上的值，保存在 arr_vals。  <details> <summary>提示（点击展开）</summary>  提示：lambdify(x, expr, 'numpy')  </details>  请在下面的代码单元中实现（保留题中要求的变量名）。
14. **### 题 14** :: ### 题 14 （难度：medium）  使用 SciPy 的 odeint（或 solve_ivp）解简单二阶ODE y'' + y = 0 转为一阶组，初始条件 y(0)=1, y'(0)=0，在 t=np.linspace(0,2*pi,100) 上求解并把 y(t) 存入 y_sol。  <details> <summary>提示（点击展开）</summary>  提示：把 y1=y, y2=y'，然后使用 odeint  </details>  请在下面的代码单元中实现（保留题中要求的变量名）。
15. **### 题 15** :: ### 题 15 （难度：medium）  使用 SciPy 的 curve_fit 拟合 noisy 二次数据 y = 2*x^2 + 3*x + 1 + noise，得到拟合参数 params (a,b,c)。  <details> <summary>提示（点击展开）</summary>  提示：from scipy.optimize import curve_fit  </details>  请在下面的代码单元中实现（保留题中要求的变量名）。
16. **### 题 16** :: ### 题 16 （难度：medium）  用 SciPy 的插值方法对 x=[0,1,2], y=[0,1,0] 做三次样条插值，并计算在 x=0.5 处的插值值 interp05。  <details> <summary>提示（点击展开）</summary>  提示：使用 scipy.interpolate.CubicSpline 或 interp1d（注意：interp1d 的 'cubic' 需要至少 4 点）。  </details>  请在下面的代码单元中实现（保留题中要求的变量名）。
17. **### 题 17** :: ### 题 17 （难度：medium）  使用 SymPy 的 dsolve 解二阶常系数方程 y'' - 2*y' + y = 0 的通解（符号），并将结果存入 sol_ch2。  <details> <summary>提示（点击展开）</summary>  提示：use Function, dsolve, Eq  </details>  请在下面的代码单元中实现（保留题中要求的变量名）。
18. **### 题 18** :: ### 题 18 （难度：medium）  使用 SciPy 的 fft（scipy.fft.rfft）计算一个简单信号 sin(2*pi*5*t) 的频谱峰值对应的频率（采样 fs=100 Hz，时长1s）。把结果放入 peak_freq。  <details> <summary>提示（点击展开）</summary>  提示：使用 scipy.fft.rfft 和 scipy.fft.rfftfreq  </details>  请在下面的代码单元中实现（保留题中要求的变量名）。
19. **### 题 19** :: ### 题 19 （难度：medium）  使用 SymPy 的 Matrix 求矩阵的特征值（Eigenvalues）对 A=Matrix([[2,1],[1,2]])，并把以列表形式保存到 eigs。  <details> <summary>提示（点击展开）</summary>  提示：A.eigenvals() 或 A.eigenvects()  </details>  请在下面的代码单元中实现（保留题中要求的变量名）。
20. **### 题 20** :: ### 题 20 （难度：medium）  使用 SciPy 的 optimize.root 求解方程组 [x^2 + y - 3, x + y^2 - 3] 的一个解，初始猜测 (1,1)，把解放到 root_sol。  <details> <summary>提示（点击展开）</summary>  提示：from scipy.optimize import root  </details>  请在下面的代码单元中实现（保留题中要求的变量名）。
21. **### 题 21** :: ### 题 21 （难度：medium）  使用 SciPy 的 minimize (method='BFGS') 求最小化 Rosenbrock 函数 f(x,y)=(a-x)^2 + b*(y-x^2)^2，a=1,b=100，从起点 (-1.2,1) 开始。把最优点保存在 rosen_x。  <details> <summary>提示（点击展开）</summary>  提示：from scipy.optimize import minimize  </details>  请在下面的代码单元中实现（保留题中要求的变量名）。
22. **### 题 22** :: ### 题 22 （难度：medium）  使用 SymPy 将表达式 (x**2 + 2*x +1) 因式分解成 (x+1)**2，存入 fact_expr。  <details> <summary>提示（点击展开）</summary>  提示：sp.factor  </details>  请在下面的代码单元中实现（保留题中要求的变量名）。
23. **### 题 23** :: ### 题 23 （难度：slightly hard）  使用 SymPy 推导一个函数的雅可比矩阵：f1 = x**2 + y, f2 = sin(x) - y**2。用 Matrix([f1,f2]).jacobian([x,y]) 并保存到 J.  <details> <summary>提示（点击展开）</summary>  提示：sp.Matrix([...]).jacobian([x,y])  </details>  请在下面的代码单元中实现（保留题中要求的变量名）。
24. **### 题 24** :: ### 题 24 （难度：slightly hard）  使用 SciPy 的 solve_ivp 求 Lorenz 系统在 t in [0,2] 的数值解，参数 sigma=10, rho=28, beta=8/3，初始值 (0.,1.,0.)。把结果 sol_lorenz 保存为 solve_ivp 的返回对象。  <details> <summary>提示（点击展开）</summary>  提示：see PDFs for Lorenz code  </details>  请在下面的代码单元中实现（保留题中要求的变量名）。
25. **### 题 25** :: ### 题 25 （难度：slightly hard）  用 SymPy 求解常微分方程 d^2 y/dx^2 - y = 0 的通解（符号），并将其存在 sol_ode2。  <details> <summary>提示（点击展开）</summary>  提示：dsolve with y(x).diff(x,2) - y(x) = 0  </details>  请在下面的代码单元中实现（保留题中要求的变量名）。
26. **### 题 26** :: ### 题 26 （难度：slightly hard）  使用 SciPy 的 curve_fit，拟合一个正弦信号 y=A*sin(2*pi*f*t+phi) 的参数 A,f,phi，从 noisy 数据恢复频率 f（初估 5 Hz）并保存到 est_f。  <details> <summary>提示（点击展开）</summary>  提示：使用 curve_fit 和合理初值  </details>  请在下面的代码单元中实现（保留题中要求的变量名）。
27. **### 题 27** :: ### 题 27 （难度：slightly hard）  使用 SymPy 求解二次型约束下的最优化问题（解析）：最小化 f(x,y)=x^2 + y^2 subject to x + y - 1 = 0。用拉格朗日乘子法得到解并保存到 opt_xy。  <details> <summary>提示（点击展开）</summary>  提示：构造 L = f + lambda*(constraint) 并对 x,y,lambda 求导等于零，使用 solve  </details>  请在下面的代码单元中实现（保留题中要求的变量名）。
28. **### 题 28** :: ### 题 28 （难度：slightly hard）  使用 SciPy 的 linprog 构造并求解一个小线性规划：minimize c^T x subject to Ax<=b, x>=0，其中 A=[[1,2]], b=[4], c=[1,1]。把解放在 lp_x。  <details> <summary>提示（点击展开）</summary>  提示：scipy.optimize.linprog  </details>  请在下面的代码单元中实现（保留题中要求的变量名）。
29. **### 题 29** :: ### 题 29 （难度：slightly hard）  综合题：用 SymPy 符号推导 y = sin(x)^2 的导数并用 lambdify 生成函数，然后在 x=0.7 处与数值差商 (central difference) 验证其正确性（误差<1e-6）。  <details> <summary>提示（点击展开）</summary>  提示：diff + lambdify and central finite difference  </details>  请在下面的代码单元中实现（保留题中要求的变量名）。
30. **### 题 30** :: ### 题 30 （难度：slightly hard）  高级：使用 SymPy 的 dsolve 求解带初始条件的 logistic 方程 dx/dt = r*x*(1-x/K), x(0)=x0，并将解析解存在 sol_logistic。参数 r,K,x0 可以假设为符号或具体数值（例如 r=1, K=10, x0=0.1）。  <details> <summary>提示（点击展开）</summary>  提示：使用 Function, dsolve, Eq, 以及 ics 参数  </details>  请在下面的代码单元中实现（保留题中要求的变量名）。 || 答案是一个单独的 `ipynb` 文件，我做成了一个zip压缩包，查看需要密码，节后提供，各位童鞋国庆节快乐！

---

### 新版 02 SymPy（chapters/02-sympy/exercises/quiz.ipynb，11 题）

1. **### 题 1** :: ### 题 1  使用 SymPy 创建符号变量 x, y 并构造表达式 expr = x**2 + 2*x*y + y**2。 请在代码区定义 x, y 与 expr。 || <details><summary>提示（点击展开）</summary>  提示：from sympy import symbols; x,y = symbols('x y')  </details>
2. **### 题 2** :: ### 题 2  对上一题中的 expr 对 x 求偏导，得到 df_dx。 || <details><summary>提示（点击展开）</summary>  提示：sp.diff(expr, x)  </details>
3. **### 题 3** :: ### 题 3  用 SymPy 求极限 lim_{x->0} sin(x)/x，保存为 lim_val。 || <details><summary>提示（点击展开）</summary>  提示：sp.limit(sp.sin(x)/x, x, 0)  </details>
4. **### 题 4** :: ### 题 4  用 SymPy 求不定积分 int (3*x**2) dx，保存为 F。 || <details><summary>提示（点击展开）</summary>  提示：sp.integrate(3*x**2, x)  </details>
5. **### 题 5** :: ### 题 5  把 expr = x**2 + 2*x + 1 用 lambdify 转成数值函数 f_num，并计算 val=f_num(1)。 || <details><summary>提示（点击展开）</summary>  提示：sp.lambdify(x, expr, 'numpy')  </details>
6. **### 题 6** :: ### 题 6  用 solveset 求 x**2 - 5*x + 6 = 0 的解集，保存为 sols。 || <details><summary>提示（点击展开）</summary>  提示：sp.solveset(expr, x)  </details>
7. **### 题 7** :: ### 题 7  用 linsolve 解 A*v=b，其中 A=Matrix([[1,1,1],[2,-1,1],[1,2,2]])、b=Matrix([2,-1,3])，把解赋给 sol_vec。 || <details><summary>提示（点击展开）</summary>  提示：sp.linsolve((A, b), (x, y, z))  </details>
8. **### 题 8** :: ### 题 8  用 SymPy 求矩阵 A=Matrix([[2,1],[1,2]]) 的特征值，保存到 eigs。 || <details><summary>提示（点击展开）</summary>  提示：A.eigenvals()  </details>
9. **### 题 9** :: ### 题 9  构造 f1=x**2+y、f2=sin(x)-y**2，用 Matrix([f1,f2]).jacobian([x,y]) 得到 J。 || <details><summary>提示（点击展开）</summary>  提示：sp.Matrix([...]).jacobian([x,y])  </details>
10. **### 题 10** :: ### 题 10  用 factor 把 x**2 + 2*x + 1 分解为 (x+1)**2，保存到 fact_expr。 || <details><summary>提示（点击展开）</summary>  提示：sp.factor(expr)  </details>
11. **### 题 11** :: ### 题 11  用 dsolve 求 y' + y = x 且 y(0)=1 的特解，保存到 sol_ode。 || <details><summary>提示（点击展开）</summary>  提示：Function('y')(x)、Eq、ics  </details>

---

### 新版 03 SciPy（chapters/03-scipy/exercises/quiz.ipynb，16 题）

1. **### 题 1** :: ### 题 1：一维定积分  用 `quad` 求 ∫0^1 x^2 dx，取 `[0]`。  请在下面的代码单元中实现（保留题中要求的变量名）。 || <details><summary>提示（点击展开）</summary>  用 `quad` 求 ∫0^1 x^2 dx，取 `[0]`。  </details>
2. **### 题 2** :: ### 题 2：二重积分  `dblquad` 的签名：内层上下限是函数。  请在下面的代码单元中实现（保留题中要求的变量名）。 || <details><summary>提示（点击展开）</summary>  `dblquad` 的签名：内层上下限是函数。  </details>
3. **### 题 3** :: ### 题 3：一阶 ODE  `solve_ivp(deriv, (0,5), [1], t_eval=[5])`，取 `sol.y[0,-1]`。  请在下面的代码单元中实现（保留题中要求的变量名）。 || <details><summary>提示（点击展开）</summary>  `solve_ivp(deriv, (0,5), [1], t_eval=[5])`，取 `sol.y[0,-1]`。  </details>
4. **### 题 4** :: ### 题 4：一维求根  `brentq(f, 1, 2)` 求 x^2-2。  请在下面的代码单元中实现（保留题中要求的变量名）。 || <details><summary>提示（点击展开）</summary>  `brentq(f, 1, 2)` 求 x^2-2。  </details>
5. **### 题 5** :: ### 题 5：一维极小值  `brent(f, brack=(0,2))` 求 (x-1)^2。  请在下面的代码单元中实现（保留题中要求的变量名）。 || <details><summary>提示（点击展开）</summary>  `brent(f, brack=(0,2))` 求 (x-1)^2。  </details>
6. **### 题 6** :: ### 题 6：指派问题  `linear_sum_assignment` 返回行/列索引，用 `cost[ri, ci].sum()`。  请在下面的代码单元中实现（保留题中要求的变量名）。 || <details><summary>提示（点击展开）</summary>  `linear_sum_assignment` 返回行/列索引，用 `cost[ri, ci].sum()`。  </details>
7. **### 题 7** :: ### 题 7：线性规划  最小化 x1+x2，约束 x1+2x2>=4；`linprog` 用 `A_ub`<= 形式，需取负。  请在下面的代码单元中实现（保留题中要求的变量名）。 || <details><summary>提示（点击展开）</summary>  最小化 x1+x2，约束 x1+2x2>=4；`linprog` 用 `A_ub`<= 形式，需取负。  </details>
8. **### 题 8** :: ### 题 8：Rosenbrock 优化  `minimize(rosen, [-1.2, 1.0], method='BFGS')`。  请在下面的代码单元中实现（保留题中要求的变量名）。 || <details><summary>提示（点击展开）</summary>  `minimize(rosen, [-1.2, 1.0], method='BFGS')`。  </details>
9. **### 题 9** :: ### 题 9：曲线拟合  `curve_fit(model, xdata, ydata, p0=[1,1,1])`，真实参数 (2,3,1)。  请在下面的代码单元中实现（保留题中要求的变量名）。 || <details><summary>提示（点击展开）</summary>  `curve_fit(model, xdata, ydata, p0=[1,1,1])`，真实参数 (2,3,1)。  </details>
10. **### 题 10** :: ### 题 10：一维插值  `CubicSpline([0,1,2],[0,1,0])`，在 0.5 处取值。  请在下面的代码单元中实现（保留题中要求的变量名）。 || <details><summary>提示（点击展开）</summary>  `CubicSpline([0,1,2],[0,1,0])`，在 0.5 处取值。  </details>
11. **### 题 11** :: ### 题 11：多维插值  `RegularGridInterpolator((x,y), Z)`，点 (0.5,0.5)。  请在下面的代码单元中实现（保留题中要求的变量名）。 || <details><summary>提示（点击展开）</summary>  `RegularGridInterpolator((x,y), Z)`，点 (0.5,0.5)。  </details>
12. **### 题 12** :: ### 题 12：正态性检验  `shapiro(rng.normal(0,1,100))` 取 p 值。  请在下面的代码单元中实现（保留题中要求的变量名）。 || <details><summary>提示（点击展开）</summary>  `shapiro(rng.normal(0,1,100))` 取 p 值。  </details>
13. **### 题 13** :: ### 题 13：独立样本 t 检验  两组正态，均值 0 / 0.5，用 `ttest_ind` 取 p 值。  请在下面的代码单元中实现（保留题中要求的变量名）。 || <details><summary>提示（点击展开）</summary>  两组正态，均值 0 / 0.5，用 `ttest_ind` 取 p 值。  </details>
14. **### 题 14** :: ### 题 14：卡方独立性检验  `chi2_contingency(np.array([[10,20],[30,40]]))` 取 p 值。  请在下面的代码单元中实现（保留题中要求的变量名）。 || <details><summary>提示（点击展开）</summary>  `chi2_contingency(np.array([[10,20],[30,40]]))` 取 p 值。  </details>
15. **### 题 15** :: ### 题 15：FFT 主频  `rfft` + `rfftfreq`，找 `argmax`。  请在下面的代码单元中实现（保留题中要求的变量名）。 || <details><summary>提示（点击展开）</summary>  `rfft` + `rfftfreq`，找 `argmax`。  </details>
16. **### 题 16** :: ### 题 16：低通滤波  `butter(3, 80/(0.5*fs), btype='low')` + `filtfilt`，与 50 Hz 参考求相关系数。  请在下面的代码单元中实现（保留题中要求的变量名）。 || <details><summary>提示（点击展开）</summary>  `butter(3, 80/(0.5*fs), btype='low')` + `filtfilt`，与 50 Hz 参考求相关系数。  </details>

