# -*- coding: utf-8 -*-
"""Generate figures for the new NumPy chapter (chap1 -> chapters/01-numpy)."""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                   "chapters", "01-numpy", "images")
os.makedirs(OUT, exist_ok=True)
plt.rcParams["figure.dpi"] = 150
plt.rcParams["savefig.bbox"] = "tight"
plt.rcParams["axes.spines.top"] = False
plt.rcParams["axes.spines.right"] = False
plt.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei", "DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False
np.random.seed(42)


def grid_ax(ax, values, title, cmap=None, annotate=True):
    a = np.asarray(values, dtype=float)
    if cmap is None:
        cmap = "Blues"
    im = ax.imshow(a, cmap=cmap, vmin=a.min() if a.size else 0, vmax=a.max() if a.size else 1)
    if annotate:
        for i in range(a.shape[0]):
            for j in range(a.shape[1]):
                ax.text(j, i, f"{a[i, j]:g}", ha="center", va="center",
                        fontsize=9, color="black" if a[i, j] != a.min() else "white")
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title(title, fontsize=10)
    return im


# 1) reshape: [0 1 2 3 4 5] -> 2x3
fig, ax = plt.subplots(1, 1, figsize=(5.2, 2.0))
ax.set_xlim(-0.5, 5.5)
ax.set_ylim(-1.2, 0.8)
for k in range(6):
    ax.add_patch(FancyBboxPatch((k - 0.4, -0.4), 0.8, 0.8,
                                boxstyle="round,pad=0.02", fc="#cfe3f7", ec="#2f6fb3"))
    ax.text(k, 0.0, str(k), ha="center", va="center", fontsize=12)
ax.text(2.5, 0.95, "np.reshape(2, 3)", ha="center", fontsize=10, color="#2f6fb3")
ax.set_xticks([]); ax.set_yticks([])
ax.spines[:].set_visible(False)
for i in range(2):
    for j in range(3):
        v = i * 3 + j
        ax.add_patch(FancyBboxPatch((j + 0.1, i - 1.25), 0.8, 0.8,
                                    boxstyle="round,pad=0.02", fc="#d9f2d0", ec="#3a8f4f"))
        ax.text(j + 0.5, i - 0.85, str(v), ha="center", va="center", fontsize=12)
ax.text(2.5, -2.15, "2 × 3", ha="center", fontsize=10, color="#3a8f4f")
fig.savefig(os.path.join(OUT, "reshape.png"))
plt.close(fig)

# 2) broadcast: A(2,3) + b(3) -> result
A = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([10, 20, 30])
R = A + b
fig, axes = plt.subplots(1, 3, figsize=(9.6, 2.6))
grid_ax(axes[0], A, "A (2,3)")
grid_ax(axes[1], b.reshape(1, 3), "b (3,)  ->  (1,3)", cmap="Oranges", annotate=True)
grid_ax(axes[2], R, "A + b", cmap="Greens")
for ax, t in zip(axes, ["原始数组", "沿行广播", "结果 (2,3)"]):
    ax.set_title(ax.get_title() + "\n" + t, fontsize=9)
fig.savefig(os.path.join(OUT, "broadcast.png"))
plt.close(fig)

# 3) vector ops
fig, ax = plt.subplots(figsize=(4.8, 4.2))
origin = np.array([0, 0])
a = np.array([2, 3]); bvec = np.array([3, 1]); s = a + bvec
for v, c, lb in [(a, "#2f6fb3", "a=(2,3)"), (bvec, "#e07b39", "b=(3,1)"), (s, "#3a8f4f", "a+b=(5,4)")]:
    ax.add_patch(FancyArrowPatch(origin, v, arrowstyle="->", mutation_scale=16,
                                 lw=2.4, color=c))
    ax.text(v[0] + 0.05, v[1] + 0.05, lb, color=c, fontsize=10)
ax.plot([0, s[0]], [0, s[1]], ls=":", color="#999", lw=1)
ax.set_xlim(-0.5, 6.0); ax.set_ylim(-0.5, 5.2)
ax.set_xlabel("x"); ax.set_ylabel("y")
ax.set_aspect("equal"); ax.grid(alpha=0.25)
fig.savefig(os.path.join(OUT, "vector_ops.png"))
plt.close(fig)

# 4) polynomial fit illustration
def f(x): return 2 * x ** 2 - 3 * x + 1
x = np.linspace(-2, 3, 40)
y = f(x) + np.random.default_rng(7).normal(0, 2, x.size)
fig, ax = plt.subplots(figsize=(5.8, 3.6))
ax.scatter(x, y, s=16, color="#2f6fb3", label="data (with noise)", alpha=0.8)
xs = np.linspace(-2, 3, 200)
for deg, c, ls in [(1, "#999", "--"), (3, "#e07b39", "-."), (5, "#3a8f4f", "-")]:
    coef = np.polyfit(x, y, deg)
    ax.plot(xs, np.polyval(coef, xs), color=c, ls=ls, lw=2, label=f"poly deg {deg}")
ax.set_xlabel("x"); ax.set_ylabel("y")
ax.legend(fontsize=8)
ax.set_title("numpy.polyfit example", fontsize=10)
fig.savefig(os.path.join(OUT, "polyfit.png"))
plt.close(fig)

# 5) SVD image compression (synthetic "photo")
x = np.linspace(0, 1, 120); y = np.linspace(0, 1, 120)
X, Y = np.meshgrid(x, y)
img = (np.sin(6 * X) * np.cos(6 * Y) + np.exp(-((X - 0.4) ** 2 + (Y - 0.6) ** 2) * 40)
       + 0.6 * X - 0.4 * Y)
img = (img - img.min()) / (img.max() - img.min())
U, S, Vt = np.linalg.svd(img, full_matrices=False)
ranks = [2, 6, 20]
fig, axes = plt.subplots(1, len(ranks) + 1, figsize=(11, 2.6))
axes[0].imshow(img, cmap="gray"); axes[0].set_title("original", fontsize=9)
axes[0].axis("off")
for ax, r in zip(axes[1:], ranks):
    approx = U[:, :r] @ np.diag(S[:r]) @ Vt[:r, :]
    ax.imshow(approx, cmap="gray")
    ax.set_title(f"rank {r}  (keep {r}/{len(S)})", fontsize=9)
    ax.axis("off")
for ax in axes:
    ax.set_xticks([]); ax.set_yticks([])
fig.savefig(os.path.join(OUT, "svd_compression.png"))
plt.close(fig)

# 6) condition number sensitivity
A = np.array([[1, 2, 3], [2, 4.0001, 6], [1, 0.9999, 2]])
b0 = np.array([1, 2, 3])
x0 = np.linalg.solve(A, b0)
eps = np.linspace(0, 1e-4, 50)
dx = []
for e in eps:
    x = np.linalg.solve(A, b0 + np.array([0, 0, e]))
    dx.append(np.linalg.norm(x - x0))
fig, ax = plt.subplots(figsize=(5.2, 3.0))
ax.plot(eps, dx, color="#c0392b", lw=2)
ax.set_xlabel("perturbation of b (added to 3rd entry)")
ax.set_ylabel("||x - x0||")
ax.set_title(f"cond(A) ≈ {np.linalg.cond(A):.2e}", fontsize=10)
ax.grid(alpha=0.25)
fig.savefig(os.path.join(OUT, "cond_sensitivity.png"))
plt.close(fig)

print("figures saved to", OUT)
for f in sorted(os.listdir(OUT)):
    print("  ", f)
