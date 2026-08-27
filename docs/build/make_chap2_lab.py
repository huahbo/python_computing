# -*- coding: utf-8 -*-
"""Generate lab.ipynb for chapter 02 (SymPy) — guided lab notebook."""
import json, os

cells = []
def md(*lines): cells.append({"cell_type": "markdown", "metadata": {}, "source": [l + chr(10) for l in lines]})
def code(*lines): cells.append({"cell_type": "code", "metadata": {}, "execution_count": None,
                                "outputs": [], "source": [l + chr(10) for l in lines]})

md("# SymPy 上机实验（第 2 章 lab）",
   "",
   "**要求**：按顺序运行每一格，完成所有 # TODO 后运行 检查 单元；最后截图/导出 notebook 提交。",
   "环境：Python 3.10+，SymPy ≥ 1.10（推荐 1.13+）。",
   "",
   "---",
   "")

code("import sympy as sp",
     "print('SymPy version:', sp.__version__)",
     "assert float(sp.__version__.split('.')[0]) >= 1 and float(sp.__version__.split('.')[1]) >= 10, '请升级 SymPy'",
     "print('环境 OK')")

md("## Part 1 符号对象与基本运算",
   "",
   "练习：创建符号、设置假设、做四则运算。")

code("# TODO 1.1 创建符号并打印",
   "x, y = sp.symbols('x y')",
   "w = sp.Symbol('w', positive=True)",
   "print(x, y, w)",
   "print('w.is_positive =', w.is_positive)",
   "",
   "expr = x**2 + 2*x*y + y**2",
   "print(expr)")

code("# TODO 1.2 算术与函数",
   "print('x+y =', x + y)",
   "print('x*y =', x * y)",
   "print('x/y =', x / y)",
   "print('sin(x)+cos(x) =', sp.sin(x) + sp.cos(x))",
   "print('f.diff(x) =', sp.Function('f')(x).diff(x))")

md("## Part 2 极限 / 导数 / 积分")

code("# TODO 2.1 极限",
   "print('lim sin(x)/x x->0 =', sp.limit(sp.sin(x)/x, x, 0))",
   "print('lim 1/x x->oo =', sp.limit(1/x, x, sp.oo))")

code("# TODO 2.2 一元与多元导数",
   "print('d/dx x^3 =', sp.diff(x**3, x))",
   "print('d^2/dx^2 x^3 =', sp.diff(x**3, x, 2))",
   "print('d/dx sin(x)cos(x) =', sp.simplify(sp.diff(sp.sin(x)*sp.cos(x), x)))",
   "print('dh/dx =', sp.diff(x**2*y + x*y**2, x))",
   "print('dh/dy =', sp.diff(x**2*y + x*y**2, y))")

code("# TODO 2.3 积分",
   "print('int (3x^2) dx =', sp.integrate(3*x**2, x))",
   "print('int_0^1 x^2 dx =', sp.integrate(x**2, (x, 0, 1)))",
   "print('int_0^1 int_0^1 (x+y) =', sp.integrate(sp.integrate(x + y, (x, 0, 1)), (y, 0, 1)))")

md("## Part 3 化简与替换")

code("# TODO 3.1 化简、factor、expand、trigsimp",
   "expr2 = (x + 1)**2",
   "print('expand =', sp.expand(expr2))",
   "print('factor =', sp.factor(x**2 + 2*x + 1))",
   "print('trigsimp =', sp.trigsimp(sp.sin(x)**2 + sp.cos(x)**2))",
   "print('sqrt(8) =', sp.sqrt(8), ' evalf =', sp.sqrt(8).evalf())")

code("# TODO 3.2 subs 与 evalf",
   "expr = x**2 + 2*x + 1",
   "v = expr.subs(x, 2)",
   "print('subs =', v, type(v))",
   "print('evalf =', sp.N(expr.subs(x, 2)))",
   "# TODO: 把 x 替换成 3，再求 evalf")

md("## Part 4 解方程与方程组")

code("# TODO 4.1 solve / solveset",
   "print('solve x^2-5x+6 =', sp.solve(x**2 - 5*x + 6, x))",
   "print('solveset x^2-5x+6 =', sp.solveset(x**2 - 5*x + 6, x))",
   "print('solveset x^2+1 (Reals) =', sp.solveset(x**2 + 1, x, domain=sp.S.Reals))",
   "print('solveset x^2+1 (Complexes) =', sp.solveset(x**2 + 1, x, domain=sp.S.Complexes))")

code("# TODO 4.2 线性方程组（linsolve）",
   "z = sp.Symbol('z')",
   "A = sp.Matrix([[1, 1, 1], [2, -1, 1], [1, 2, 2]])",
   "b = sp.Matrix([2, -1, 3])",
   "print('linsolve =', sp.linsolve((A, b), (x, y, z)))",
   "print('solve sys =', sp.solve([x + y + z - 2, 2*x - y + z + 1, x + 2*y + 2*z - 3], (x, y, z)))")

code("# TODO 4.3 非线性方程组（nonlinsolve）",
   "print('nonlinsolve =', sp.nonlinsolve([x**2 + y**2 - 5, x - y - 1], (x, y)))")

md("## Part 5 符号矩阵与 lambdify")

code("# TODO 5.1 矩阵运算与特征值",
   "M = sp.Matrix([[2, 1], [1, 2]])",
   "print('M =', M)",
   "print('det =', M.det())",
   "print('inv =', M.inv())",
   "print('eigenvals =', M.eigenvals())",
   "print('eigenvects =', M.eigenvects())")

code("# TODO 5.2 雅可比矩阵",
   "J = sp.Matrix([x**2 + y, sp.sin(x) - y**2]).jacobian([x, y])",
   "print('J =', J)")

code("# TODO 5.3 lambdify",
   "import numpy as np",
   "x_sym = sp.symbols('x')",
   "f = sp.lambdify(x_sym, sp.sin(x_sym)**2 + x_sym, 'numpy')",
   "arr = np.linspace(0, np.pi, 5)",
   "print('f(arr) =', f(arr))",
   "print('f(1) =', f(1))")

md("## Part 6 微分方程 dsolve")

code("# TODO 6.1 一阶初值问题",
   "t = sp.symbols('t')",
   "y = sp.Function('y')(t)",
   "eq = sp.Eq(y.diff(t) + y, t)",
   "print('general =', sp.dsolve(eq, y))",
   "print('specific =', sp.dsolve(eq, y, ics={y.subs(t, 0): 1}))")

code("# TODO 6.2 二阶常系数齐次方程",
   "print('ODE2 =', sp.dsolve(sp.Eq(sp.Function('y')(x).diff(x, 2) - 2*sp.Function('y')(x).diff(x) + sp.Function('y')(x), 0)))")

md("## Part 7 综合任务：符号推导 + 数值验证 + 绘图",
   "",
   "按 03 综合案例实现：求 y=x^2 在 [0,1] 上的符号面积，并画出曲线与切线图。")

code("# TODO 7.1 符号面积 + 绘图",
   "import matplotlib.pyplot as plt",
   "import numpy as np",
   "x = sp.symbols('x')",
   "area_exact = sp.integrate(x**2, (x, 0, 1))",
   "print('精确面积 =', area_exact, ' 数值 =', float(sp.N(area_exact)))",
   "",
   "plt.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei', 'DejaVu Sans']",
   "plt.rcParams['axes.unicode_minus'] = False",
   "xs = np.linspace(0, 1, 300)",
   "plt.figure(figsize=(5.4, 4.0))",
   "plt.fill_between(xs, xs**2, color='#9ec7e8', alpha=0.55, label=f'S = {float(sp.N(area_exact)):.4f}')",
   "plt.plot(xs, xs**2, color='#2f6fb3', lw=2.4, label='y = x^2')",
   "plt.xlabel('x'); plt.ylabel('y')",
   "plt.title('符号积分求面积', fontsize=11)",
   "plt.legend(); plt.grid(alpha=0.25)",
   "plt.savefig('sympy_area_lab.png', bbox_inches='tight')",
   "print('已保存 sympy_area_lab.png')")

code("# TODO 7.2 符号导数 + 切线图",
   "x = sp.symbols('x')",
   "f = sp.sin(x)",
   "df = sp.diff(f, x)",
   "a = 1",
   "slope = float(sp.N(df.subs(x, a)))",
   "tangent = sp.simplify(df.subs(x, a)*(x - a) + f.subs(x, a))",
   "print('导数 =', df)",
   "print('斜率 =', slope)",
   "print('切线 =', tangent)",
   "",
   "f_num = sp.lambdify(x, f, 'numpy')",
   "tan_num = sp.lambdify(x, tangent, 'numpy')",
   "print('f(a) =', f_num(a), ' tangent(a) =', tan_num(a))",
   "",
   "xn = np.linspace(-1, 3, 400)",
   "plt.figure(figsize=(5.8, 4.0))",
   "plt.plot(xn, f_num(xn), color='#2f6fb3', lw=2.4, label='y = sin(x)')",
   "plt.plot(xn, tan_num(xn), color='#e07b39', lw=2, ls='--', label=f'切线 (斜率 {slope:.4f})')",
   "plt.plot([a], [f_num(a)], 'o', color='#c0392b', ms=7, label='切点')",
   "plt.xlabel('x'); plt.ylabel('y')",
   "plt.title('符号导数 -> 切线方程', fontsize=11)",
   "plt.legend(); plt.grid(alpha=0.25)",
   "plt.savefig('sympy_tangent_lab.png', bbox_inches='tight')",
   "print('已保存 sympy_tangent_lab.png')")

md("## 提交清单",
   "",
   "- [ ] 所有 TODO 均已填写并运行；",
   "- [ ] Part 4 的 solve/solveset 差异已记录；",
   "- [ ] Part 5 的 lambdify 数组输出已记录；",
   "- [ ] Part 7 已生成两张图并写 3 句结论；",
   "- [ ] 导出为 html / 保留 ipynb 提交。",
   "",
   "**延伸**：完成 exercises/ 的 11 道题与 03 的拓展任务。")

nb = {
    "cells": cells,
    "metadata": {
        "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
        "language_info": {"name": "python", "version": "3.13"}
    },
    "nbformat": 4,
    "nbformat_minor": 5,
}
out = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                   "chapters", "02-sympy", "lab", "lab.ipynb")
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
