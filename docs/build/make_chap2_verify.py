# -*- coding: utf-8 -*-
"""Run SymPy chapter code examples to capture real outputs. Named make_chap2_* for policy."""
import sympy as sp
print("sympy", sp.__version__)

cases = [
    ("symbols_arith", '''x, y, z = sp.symbols('x y z')
print(x + y + z)'''),
    ("symbol_basic", '''x = sp.Symbol('x')
print(x)
positive_x = sp.Symbol('x', positive=True)
print(positive_x)'''),
    ("symbol_assume", '''real_x = sp.Symbol('x', real=True)
integer_n = sp.Symbol('n', integer=True)
print(real_x)
print(integer_n)'''),
    ("symbol_range", '''n = 3
xs = sp.symbols(f'x_1:{n+1}')
print(xs)'''),
    ("symbol_list", '''x_symbols = [sp.Symbol(f'x_{i+1}') for i in range(3)]
print(x_symbols)'''),
    ("arith", '''x, y = sp.symbols('x y')
print(x + y)
print(x - y)
print(x * y)
print(x / y)'''),
    ("func", '''x = sp.symbols('x')
f = sp.Function('f')(x)
print(f)
print(f.diff(x))'''),
    ("trig_import", '''x = sp.symbols('x')
sin_x = sp.sin(x)
cos_x = sp.cos(x)
print(sin_x)
print(cos_x)
print(sin_x + cos_x)'''),
    ("limit1", '''x = sp.symbols('x')
print(sp.limit(sp.sin(x)/x, x, 0))'''),
    ("limit2", '''x = sp.symbols('x')
print(sp.limit(1/x, x, sp.oo))'''),
    ("limit3", '''x = sp.symbols('x')
print(sp.limit(1/x, x, 0, dir='-'))'''),
    ("limit4", '''x = sp.symbols('x')
f = x**3 + 3*x**2 + sp.exp(-2*x)
print(sp.limit(f, x, 0.5))'''),
    ("diff1", '''x, y, z = sp.symbols('x y z')
f = x**2 + 3*x + 2
print(sp.diff(f, x))'''),
    ("diff2", '''x = sp.symbols('x')
g = sp.sin(x)*sp.cos(x)
print(sp.diff(g, x))
print(sp.simplify(sp.diff(g, x)))'''),
    ("diff3", '''x, y = sp.symbols('x y')
h = x**2 + x*y + y**2
print(sp.diff(h, x))
print(sp.diff(h, y))'''),
    ("diff4", '''x = sp.symbols('x')
f = x**3
print(sp.diff(f, x, 2))'''),
    ("integ1", '''x = sp.symbols('x')
f = x**2 + 2*x + 1
print(sp.integrate(f, x))'''),
    ("integ2", '''x = sp.symbols('x')
print(sp.integrate(x**2, (x, 0, 1)))'''),
    ("integ3", '''x, y = sp.symbols('x y')
f = x + y
print(sp.integrate(sp.integrate(f, (x, 0, 1)), (y, 0, 1)))'''),
    ("simplify", '''x = sp.symbols('x')
expr = (x**2 + 2*x + 1)
print(sp.factor(expr))
print(sp.expand((x+1)**2))
print(sp.simplify(sp.sin(x)**2 + sp.cos(x)**2))
print(sp.trigsimp(sp.sin(x)**2 + sp.cos(x)**2))
print(sp.sqrt(8))
print(sp.sqrt(8).evalf())
print((x**2 + 2*x + 1).subs(x, 2))'''),
    ("series", '''x = sp.symbols('x')
print(sp.series(sp.sin(x), x, 0, 6))'''),
    ("eq1", '''x = sp.symbols('x')
equation = sp.Eq(x**2, 4)
print(sp.solveset(equation, x))'''),
    ("eq2", '''x = sp.symbols('x')
print(sp.solveset(x**2 - 4, x))'''),
    ("solve1", '''x = sp.symbols('x')
print(sp.solve(3*x + 4 - 10, x))'''),
    ("solve2", '''x = sp.symbols('x')
print(sp.solve(x**2 + 5*x + 4, x))'''),
    ("solveset_quad", '''x = sp.symbols('x')
print(sp.solveset(x**2 - 5*x + 6, x))
print(sp.solveset(2*x**2 + 4*x + 2, x))
print(sp.solveset(x**2 + 1, x, domain=sp.S.Complexes))'''),
    ("solve_sys", '''x, y = sp.symbols('x y')
eqs = [2*x + 3*y - 5, 4*x - 2*y - 10]
print(sp.solve(eqs, (x, y)))'''),
    ("solve_nonlin", '''x, y = sp.symbols('x y')
eqs = [x**2 + y - 4, x - y**2 - 1]
print(sp.solve(eqs, (x, y)))'''),
    ("linsolve1", '''x, y, z = sp.symbols('x y z')
eqs = [x + y + z - 2, 2*x - y + z + 1, x + 2*y + 2*z - 3]
print(sp.linsolve(eqs, (x, y, z)))'''),
    ("linsolve2", '''x, y, z = sp.symbols('x y z')
A = sp.Matrix([[1, 1, 1], [2, -1, 1], [1, 2, 2]])
b = sp.Matrix([2, -1, 3])
print(sp.linsolve((A, b), (x, y, z)))'''),
    ("nonlinsolve", '''x, y = sp.symbols('x y')
eqs = [x**2 + y**2 - 2, x**3 + y**3]
print(sp.nonlinsolve(eqs, (x, y)))'''),
    ("lambdify", '''import sympy as sp
x = sp.symbols('x')
expr = x**2 + 2*x + 1
f = sp.lambdify(x, expr, 'numpy')
print(f(1))
print(f(2))
f_basic = sp.lambdify(x, expr)
print(f_basic(1))'''),
    ("lambdify_array", '''import sympy as sp, numpy as np
x = sp.symbols('x')
f = sp.lambdify(x, sp.sin(x)**2, 'numpy')
print(f(np.array([0, np.pi/2, np.pi])))'''),
    ("dsolve1", '''x = sp.symbols('x')
y = sp.Function('y')(x)
eq = sp.Eq(y.diff(x) + y, x)
print(sp.dsolve(eq, y))'''),
    ("dsolve2", '''x = sp.symbols('x')
y = sp.Function('y')(x)
eq = sp.Eq(y.diff(x, 2) - 2*y.diff(x) + y, 0)
print(sp.dsolve(eq, y))'''),
    ("dsolve_sys", '''t = sp.symbols('t')
x = sp.Function('x')(t)
y = sp.Function('y')(t)
eq1 = sp.Eq(x.diff(t), y)
eq2 = sp.Eq(y.diff(t), -x)
print(sp.dsolve((eq1, eq2), (x, y), dict=True))'''),
    ("dsolve_logistic", '''import sympy as sp
x = sp.symbols('x', cls=sp.Function)
x0, t, r, K = sp.symbols('x0 t r K', real=True, positive=True)
sol = sp.dsolve(sp.Eq(x(t).diff(t), r*x(t)*(1 - x(t)/K)), ics={x(0): x0})
print(sol)'''),
    ("dsolve_ics", '''import sympy as sp
x = sp.symbols('x')
y = sp.Function('y')(x)
eq = sp.Eq(y.diff(x) + y, x)
print(sp.dsolve(eq, y, ics={y.subs(x, 0): 1}))'''),
    ("matrix_eig", '''import sympy as sp
A = sp.Matrix([[2, 1], [1, 2]])
print(A.eigenvals())
print(A.eigenvects())'''),
    ("matrix_ops", '''import sympy as sp
A = sp.Matrix([[1, 2], [3, 4]])
B = sp.Matrix([[5, 6], [7, 8]])
print(A + B)
print(A * B)
print(A.det())
print(A.inv())
print(A.solve(sp.Matrix([1, 2])))
print(A**2)'''),
    ("jacobian", '''import sympy as sp
x, y = sp.symbols('x y')
f1 = x**2 + y
f2 = sp.sin(x) - y**2
J = sp.Matrix([f1, f2]).jacobian([x, y])
print(J)'''),
    ("comprehensive_case", '''import sympy as sp
x = sp.symbols('x')
f = x**2
area = sp.integrate(f, (x, 0, 1))
print(area)
print(sp.N(area))'''),
    ("tangent", '''import sympy as sp
x = sp.symbols('x')
f = sp.sin(x)
df = sp.diff(f, x)
print(df)
a = 1
slope = sp.N(df.subs(x, a))
print(slope)
tangent = sp.simplify(df.subs(x, a) * (x - a) + f.subs(x, a))
print(tangent)'''),
]

for label, code in cases:
    print("\n===== " + label + " =====")
    try:
        exec(compile(code, label, "exec"), {"sp": sp})
    except Exception as e:
        print("ERROR:", type(e).__name__, e)
