# -*- coding: utf-8 -*-
"""Generate lab.ipynb for chapter 01 (NumPy) — guided lab notebook."""
import json, os

cells = []
def md(text): cells.append({"cell_type": "markdown", "metadata": {}, "source": text})
def code(text): cells.append({"cell_type": "code", "metadata": {}, "execution_count": None,
                              "outputs": [], "source": text})

md("""# NumPy 上机实验（第 1 章 lab）

**要求**：按顺序运行每一格，完成所有 `# TODO` 后运行 `检查` 单元；最后截图/导出 notebook 提交。
环境：Python 3.10+，NumPy ≥ 1.24（推荐 1.26+）。

---
""")

code("""import numpy as np
print("NumPy version:", np.__version__)
# 环境自检：能正常导入即可
assert np.__version__ >= "1.24", "请升级 NumPy"
print("环境 OK")
""")

md("""## Part 1 数组创建与属性

练习：创建多种数组并打印 `shape / dtype / size`。""")

code("""# TODO 1.1 创建以下数组并打印属性
a = np.zeros((2, 3))          # 全 0
b = np.ones((3, 2))           # 全 1
c = np.full((2, 2), 7)        # 全 7
d = np.arange(0, 10, 2)       # 等差数列
e = np.linspace(0, 1, 5)      # 均匀 5 点
f = np.eye(3)                 # 单位阵
g = np.diag([1, 2, 3])        # 对角阵

for name, arr in [("a", a), ("b", b), ("c", c), ("d", d), ("e", e), ("f", f), ("g", g)]:
    print(f"{name}: shape={arr.shape}, dtype={arr.dtype}, size={arr.size}")
""")

code("""# TODO 1.2 把一个数组改成 2x5 并验证视图/拷贝
x = np.arange(10)
y = x.reshape(2, 5)
print("y.base is x ?", y.base is x)      # 预期 True（视图）
z = x.copy()
print("z 与 x 相互独立 ?", z.base is None or z.base is not x)  # 预期 True
# TODO: 修改 y[0,0]=99，观察 x 是否变化；再修改 z[0]=-1，观察 x 是否变化
""")

md("""## Part 2 索引、切片与布尔掩码""")

code("""# TODO 2.1 完成下列筛选
m = np.array([[1, -2, 3], [4, -5, 6], [-7, 8, 9]])
pos = m[m > 0]                 # 所有正数
row = m[(m[:, 0] > 0)]         # 第一列为正的整行
replaced = np.where(m < 0, 0, m)   # 负数置 0
print("pos =", pos)
print("row =", row)
print("replaced =", replaced)
""")

code("""# TODO 2.2 花式索引
X = np.arange(24).reshape(4, 6)
cross = X[np.ix_([0, 2], [1, 4])]   # 第 0,2 行 × 第 1,4 列
print(cross)
""")

md("""## Part 3 广播练习

规则：从右向左对齐；相等或一维为 1 即可广播。""")

code("""# TODO 3.1 手工判断形状并验证
A = np.zeros((4, 1, 6))
B = np.zeros((3, 6))
print("A+B shape =", (A + B).shape)      # 预期 (4,3,6)
# TODO 3.2 下面两行哪些可广播？分别运行并解释
# print((np.zeros((3,)) + np.zeros((4,))).shape)   # 预期报错
# print((np.zeros((3,1)) + np.zeros((3,))).shape)  # 预期报错
print(np.zeros((3, 1)) + np.zeros((1, 3)))        # 预期 (3,3)
""")

md("""## Part 4 向量 / 矩阵运算与统计""")

code("""# TODO 4.1 完成运算
v = np.array([2, 3]); w = np.array([3, 1])
print("v+w =", v + w)          # 逐元素
print("v·w =", v @ w)          # 点积
print("2v  =", 2 * v)

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print("A*B =", A * B)          # ⚠️ 逐元素
print("A@B =", A @ B)          # 矩阵乘
""")

code("""# TODO 4.2 统计
S = np.array([[85, 90, 80], [78, 85, 90], [90, 95, 85]])
print("每列和 =", S.sum(axis=0))        # 三门课总分
print("每行和 =", S.sum(axis=1))        # 每个学生总分
print("每列均值 =", S.mean(axis=0))
print("全体标准差 =", S.std())
""")

md("""## Part 5 线性代数

用 `np.linalg` 解方程、看条件数、做 SVD。""")

code("""# TODO 5.1 解线性方程组
A = np.array([[3, 1], [1, 2]])
b = np.array([9, 8])
x = np.linalg.solve(A, b)
print("解 =", x)
print("验证 =", A @ x)          # 应等于 b
print("行列式 =", np.linalg.det(A))
print("条件数 =", np.linalg.cond(A))
""")

code("""# TODO 5.2 SVD 低秩近似
M = np.array([[1., 2., 3.], [4., 5., 6.], [7., 8., 9.], [10., 11., 12.]])
U, S, Vt = np.linalg.svd(M, full_matrices=False)
print("U", U.shape, "S", S.shape, "Vt", Vt.shape)   # (4,3) (3,) (3,3)
# 重构并比较
recon = U @ np.diag(S) @ Vt
print("重构误差 =", np.linalg.norm(M - recon))
# TODO: 只用前 2 个奇异值重建，比较误差
recon2 = U[:, :2] @ np.diag(S[:2]) @ Vt[:2, :]
print("rank2 误差 =", np.linalg.norm(M - recon2))
""")

md("""## Part 6 多项式与拟合""")

code("""# TODO 6.1 poly1d 运算
p = np.poly1d([2, 3, 1])     # 2x^2+3x+1
print("p(5) =", p(5))
print("导数 =", p.deriv())
print("积分 =", p.integ())
q = np.poly1d([1, -1])
quotient, remainder = p / q    # poly1d 直接除返回 (商, 余数)
print("商 =", quotient)
print("余 =", remainder)
""")

code("""# TODO 6.2 拟合与过拟合观察
import numpy as np
rng = np.random.default_rng(7)
x = np.linspace(-2, 3, 40)
y_true = 2 * x**2 - 3 * x + 1
y = y_true + rng.normal(0, 2, x.size)

for deg in (1, 2, 5):
    coef = np.polyfit(x, y, deg)
    rmse = np.sqrt(np.mean((np.polyval(coef, x) - y) ** 2))
    print(f"deg={deg}  coeff={np.round(coef,3)}  trainRMSE={rmse:.3f}")
# TODO: 手动划分 train/test（前 28 训练、后 12 测试），比较 deg2 与 deg5 的测试 RMSE
""")

md("""## Part 7 综合任务：SVD 图像压缩

按 05 综合案例实现：生成 120×120 合成图 → SVD → 保留 rank=2/6/20 → 计算 MSE 与压缩率。""")

code("""# TODO 7.1 综合任务（可参考 05-综合案例.md）
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 1, 120); y = np.linspace(0, 1, 120)
X, Y = np.meshgrid(x, y)
img = (np.sin(6*X)*np.cos(6*Y) + np.exp(-((X-0.4)**2 + (Y-0.6)**2)*40)
       + 0.6*X - 0.4*Y)
img = (img - img.min()) / (img.max() - img.min())
U, S, Vt = np.linalg.svd(img, full_matrices=False)

for k in (2, 6, 20):
    A_k = U[:, :k] @ np.diag(S[:k]) @ Vt[:k, :]
    mse = np.mean((img - A_k) ** 2)
    params = k * (img.shape[0] + 1 + img.shape[1])
    print(f"rank={k}  MSE={mse:.5f}  压缩率={100*params/img.size:.1f}%")

plt.figure(figsize=(8, 2.4))
for i, k in enumerate([2, 6, 20]):
    plt.subplot(1, 3, i+1)
    plt.imshow(U[:, :k] @ np.diag(S[:k]) @ Vt[:k, :], cmap="gray")
    plt.title(f"rank {k}")
    plt.axis("off")
plt.tight_layout(); plt.savefig("svd_compression_lab.png")
print("已保存 svd_compression_lab.png")
""")

md("""## 提交清单

- [ ] 所有 TODO 均已填写并运行；
- [ ] Part 5 的 rank2 误差已输出；
- [ ] Part 6 的 train/test 对比已记录；
- [ ] Part 7 已生成 svd_compression_lab.png 并写 3 句结论；
- [ ] 导出为 html / 保留 ipynb 提交。

**延伸**：完成 exercises/ 的 20 道题与 05 的拓展任务。""")

nb = {
    "cells": cells,
    "metadata": {
        "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
        "language_info": {"name": "python", "version": "3.10"}
    },
    "nbformat": 4,
    "nbformat_minor": 5,
}
out = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                   "chapters", "01-numpy", "lab", "lab.ipynb")
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
