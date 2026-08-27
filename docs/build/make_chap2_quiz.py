# -*- coding: utf-8 -*-
"""Generate quiz.ipynb and answers.ipynb for chapter 02 (SymPy)."""
import json, os

BASE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                    "chapters", "02-sympy", "exercises")

def md(*lines):
    return {"cell_type": "markdown", "metadata": {}, "source": [l + "\n" for l in lines]}

def code(*lines):
    return {"cell_type": "code", "metadata": {}, "execution_count": None,
            "outputs": [], "source": [l + "\n" for l in lines]}

# Each question: (prompt_lines, hint_line, solution_lines, var, assert_expr)
Q = []
Q.append((
    ["### 题 1 ",
     "使用 SymPy 创建符号变量 x, y 并构造表达式 expr = x**2 + 2*x*y + y**2。",
     "请在代码区定义 x, y 与 expr。"],
    "提示：from sympy import symbols; x,y = symbols('x y')",
    ["import sympy as sp", "x, y = sp.symbols('x y')", "expr = x**2 + 2*x*y + y**2"],
    "_q1_expr",
    "sp.simplify(expr - (x**2 + 2*x*y + y**2)) == 0",
))
Q.append((
    ["### 题 2 ", "对上一题中的 expr 对 x 求偏导，得到 df_dx。"],
    "提示：sp.diff(expr, x)",
    ["import sympy as sp", "x, y = sp.symbols('x y')", "expr = x**2 + 2*x*y + y**2", "df_dx = sp.diff(expr, x)"],
    "_q2_df",
    "sp.simplify(df_dx - (2*x + 2*y)) == 0",
))
Q.append((
    ["### 题 3 ", "用 SymPy 求极限 lim_{x->0} sin(x)/x，保存为 lim_val。"],
    "提示：sp.limit(sp.sin(x)/x, x, 0)",
    ["import sympy as sp", "x = sp.symbols('x')", "lim_val = sp.limit(sp.sin(x)/x, x, 0)"],
    "_q3_lim",
    "lim_val == 1",
))
Q.append((
    ["### 题 4 ", "用 SymPy 求不定积分 int (3*x**2) dx，保存为 F。"],
    "提示：sp.integrate(3*x**2, x)",
    ["import sympy as sp", "x = sp.symbols('x')", "F = sp.integrate(3*x**2, x)"],
    "_q4_F",
    "sp.simplify(F - x**3) == 0",
))
Q.append((
    ["### 题 5 ", "把 expr = x**2 + 2*x + 1 用 lambdify 转成数值函数 f_num，并计算 val=f_num(1)。"],
    "提示：sp.lambdify(x, expr, 'numpy')",
    ["import sympy as sp", "x = sp.symbols('x')", "expr = x**2 + 2*x + 1",
     "f_num = sp.lambdify(x, expr, 'numpy')", "val = f_num(1)"],
    "_q5_val",
    "val == 4",
))
Q.append((
    ["### 题 6 ", "用 solveset 求 x**2 - 5*x + 6 = 0 的解集，保存为 sols。"],
    "提示：sp.solveset(expr, x)",
    ["import sympy as sp", "x = sp.symbols('x')", "sols = sp.solveset(x**2 - 5*x + 6, x)"],
    "_q6_sols",
    "sols == sp.FiniteSet(2, 3)",
))
Q.append((
    ["### 题 7 ", "用 linsolve 解 A*v=b，其中 A=Matrix([[1,1,1],[2,-1,1],[1,2,2]])、b=Matrix([2,-1,3])，把解赋给 sol_vec。"],
    "提示：sp.linsolve((A, b), (x, y, z))",
    ["import sympy as sp", "x, y, z = sp.symbols('x y z')",
     "A = sp.Matrix([[1, 1, 1], [2, -1, 1], [1, 2, 2]])",
     "b = sp.Matrix([2, -1, 3])", "sol_vec = sp.linsolve((A, b), (x, y, z))"],
    "_q7_sol_vec",
    "(1, 2, -1) in sol_vec",
))
Q.append((
    ["### 题 8 ", "用 SymPy 求矩阵 A=Matrix([[2,1],[1,2]]) 的特征值，保存到 eigs。"],
    "提示：A.eigenvals()",
    ["import sympy as sp", "A = sp.Matrix([[2, 1], [1, 2]])", "eigs = A.eigenvals()"],
    "_q8_eigs",
    "eigs[3] == 1 and eigs[1] == 1",
))
Q.append((
    ["### 题 9 ", "构造 f1=x**2+y、f2=sin(x)-y**2，用 Matrix([f1,f2]).jacobian([x,y]) 得到 J。"],
    "提示：sp.Matrix([...]).jacobian([x,y])",
    ["import sympy as sp", "x, y = sp.symbols('x y')", "f1 = x**2 + y", "f2 = sp.sin(x) - y**2",
     "J = sp.Matrix([f1, f2]).jacobian([x, y])"],
    "_q9_J",
    "sp.simplify(J - sp.Matrix([[2*x, 1], [sp.cos(x), -2*y]])) == sp.zeros(2, 2)",
))
Q.append((
    ["### 题 10 ", "用 factor 把 x**2 + 2*x + 1 分解为 (x+1)**2，保存到 fact_expr。"],
    "提示：sp.factor(expr)",
    ["import sympy as sp", "x = sp.symbols('x')", "fact_expr = sp.factor(x**2 + 2*x + 1)"],
    "_q10_fact",
    "sp.simplify(fact_expr - (x + 1)**2) == 0",
))
Q.append((
    ["### 题 11 ", "用 dsolve 求 y' + y = x 且 y(0)=1 的特解，保存到 sol_ode。"],
    "提示：Function('y')(x)、Eq、ics",
    ["import sympy as sp", "x = sp.symbols('x')", "y = sp.Function('y')(x)",
     "eq = sp.Eq(y.diff(x) + y, x)", "sol_ode = sp.dsolve(eq, y, ics={y.subs(x, 0): 1})"],
    "_q11_sol",
    "sp.simplify(sol_ode.rhs - (x - 1 + 2*sp.exp(-x))) == 0",
))

def build(show_answers):
    cells = []
    cells.append(md("# SymPy 作业 - 测验版", "",
        "说明：本 Notebook 采用自动评分，每题下面有一个测试单元，运行测试会将得分追加到 _GRADES 列表。",
        "请按顺序运行单元。", ""))
    cells.append(code("# 自动评分初始化", "_GRADES = []", "import sympy as sp", ""))
    for i, (prompt, hint, sol, var_name, assert_expr) in enumerate(Q, start=1):
        cells.append(md(*prompt, ""))
        cells.append(md("<details><summary>提示（点击展开）</summary>", "", hint, "", "</details>", ""))
        if show_answers:
            cells.append(code(*sol, ""))
        else:
            cells.append(code("# 在此单元格实现题目 %d 的答案，然后运行下面的测试单元格进行自测。" % i,
                              "# 注意：请不要修改测试单元格的变量名或输出格式。", "",
                              "### YOUR ANSWER HERE", ""))
        test_src = [
            "# Q%d test (2 points)" % i,
            "try:",
            "    pts = 2",
            "    assert %s" % assert_expr,
            "    score = pts; note='OK'",
            "except Exception as e:",
            "    score = 0; note=str(e)",
            "_GRADES.append((%d, score, pts, note))" % i,
            "print('Q%d:', score, '/', pts, note)" % i,
        ]
        cells.append(code(*test_src))
    cells.append(code("# 汇总评分",
        "total = sum(x[1] for x in _GRADES)",
        "max_total = sum(x[2] for x in _GRADES)",
        "print('Detailed per-question results:')",
        "for q, s, m, note in _GRADES:",
        "    print(f'Q{q}: {s}/{m} - {note}')",
        "print('Total score:', total, '/', max_total)", ""))
    return {"cells": cells,
            "metadata": {"kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
                          "language_info": {"name": "python", "version": "3.13"}},
            "nbformat": 4, "nbformat_minor": 5}

def write_nb(name, nb):
    with open(os.path.join(BASE, name), "w", encoding="utf-8") as f:
        json.dump(nb, f, ensure_ascii=False, indent=1)
    print("saved", name, "cells:", len(nb["cells"]))

write_nb("quiz.ipynb", build(show_answers=False))
write_nb("answers.ipynb", build(show_answers=True))
