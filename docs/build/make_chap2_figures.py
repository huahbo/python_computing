# -*- coding: utf-8 -*-
"""Generate figures for chapter 02 (SymPy): area under curve and tangent line with symbolic derivative."""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import sympy as sp

OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                   "chapters", "02-sympy", "images")
os.makedirs(OUT, exist_ok=True)
plt.rcParams["figure.dpi"] = 150
plt.rcParams["savefig.bbox"] = "tight"
plt.rcParams["axes.spines.top"] = False
plt.rcParams["axes.spines.right"] = False
# Use a CJK-capable font if available; fall back gracefully.
plt.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei", "DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False

x_sym = sp.symbols('x')

# --- Figure 1: area under y = x^2 over [0,1] (derived by SymPy) ---
f = x_sym**2
area_exact = sp.integrate(f, (x_sym, 0, 1))
area_num = sp.N(area_exact)

xs = np.linspace(0, 1, 300)
ys = xs**2
fig, ax = plt.subplots(figsize=(5.4, 4.0))
ax.fill_between(xs, ys, color="#9ec7e8", alpha=0.55, label=f"S = ∫x²dx = {area_num:.4f}")
ax.plot(xs, ys, color="#2f6fb3", lw=2.4, label="y = x²")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("符号积分求面积并用数值验证", fontsize=11)
ax.legend(fontsize=9)
ax.grid(alpha=0.25)
fig.savefig(os.path.join(OUT, "sympy_area.png"))
plt.close(fig)

# --- Figure 2: sin(x) and its tangent at x=1 (derivative from SymPy) ---
f2 = sp.sin(x_sym)
df2 = sp.diff(f2, x_sym)
a = 1
slope = sp.N(df2.subs(x_sym, a))
tangent_expr = sp.simplify(df2.subs(x_sym, a) * (x_sym - a) + f2.subs(x_sym, a))
xn = np.linspace(-1, 3, 400)
fig, ax = plt.subplots(figsize=(5.8, 4.0))
ax.plot(xn, np.sin(xn), color="#2f6fb3", lw=2.4, label="y = sin(x)")
ax.plot(xn, np.array([float(sp.N(tangent_expr.subs(x_sym, v))) for v in xn]),
        color="#e07b39", lw=2, ls="--", label=f"切线 (斜率 ≈ {slope:.4f})")
ax.plot([a], [np.sin(a)], "o", color="#c0392b", ms=7, label=f"切点 x={a}")
ax.axhline(0, color="#666", lw=0.7)
ax.axvline(0, color="#666", lw=0.7)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("符号导数 → 切线方程", fontsize=11)
ax.legend(fontsize=9)
ax.grid(alpha=0.25)
fig.savefig(os.path.join(OUT, "sympy_tangent.png"))
plt.close(fig)

# --- Figure 3 (optional): roots of polynomial on the real axis ---
p = x_sym**2 - 5*x_sym + 4
roots = sorted(sp.solve(p, x_sym))
r_vals = [float(sp.N(r)) for r in roots]
fig, ax = plt.subplots(figsize=(5.6, 2.2))
xv = np.linspace(-1, 6, 300)
ax.plot(xv, np.array([float(sp.N(p.subs(x_sym, v))) for v in xv]), color="#3a8f4f", lw=2)
ax.axhline(0, color="#666", lw=0.8)
for rv in r_vals:
    ax.plot([rv], [0], "o", color="#c0392b", ms=8)
    ax.annotate(f"x={rv:g}", (rv, 0), textcoords="offset points", xytext=(0, 10),
                ha="center", color="#c0392b", fontsize=9)
ax.set_xlabel("x")
ax.set_ylabel("f(x)")
ax.set_title("solve / solveset 求多项式根", fontsize=11)
ax.grid(alpha=0.25)
fig.savefig(os.path.join(OUT, "sympy_roots.png"))
plt.close(fig)

print("figures saved to", OUT)
for f in sorted(os.listdir(OUT)):
    print("  ", f)
