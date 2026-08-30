# 线性代数与矩阵

> 本附录讲科学计算里最常用的线性代数：向量/矩阵的直觉、关键定义、分解与算法（重点是特征值与 SVD）、数值稳定性，以及 Python 对应。学完你应能用"线性变换"的眼光看第 1 章 NumPy 的线性代数与第 8 章 sklearn 的降维。

---

## A.1 直觉故事：矩阵到底在干什么

很多同学背熟了矩阵乘法，却不知道它在"算什么"。从一个具体问题开始：

> 一家店卖两种套餐：A 套餐（米饭 1 份 + 鸡肉 2 份），B 套餐（米饭 2 份 + 鸡肉 1 份）。卖出 3 份 A、2 份 B，一共用了多少米饭和鸡肉？

卖出数量写成向量 $x=(3,2)$；A、B 套餐用料写成列向量 $(1,2)$ 与 $(2,1)$。总用料就是**线性组合**：

$$\text{米饭} = 3\times 1 + 2\times 2 = 7,\qquad \text{鸡肉} = 3\times 2 + 2\times 1 = 8$$

写成矩阵：

$$\begin{bmatrix} 1 & 2 \\ 2 & 1 \end{bmatrix} \begin{bmatrix} 3 \\ 2 \end{bmatrix} = \begin{bmatrix} 7 \\ 8 \end{bmatrix}$$

这个例子说明三件事：

1. **向量是"配比"**：一行数据、一份订单、一个状态，都可以是一个向量；
2. **矩阵是"线性变换的约定"**：$A$ 的每一列是一种"原料配方"，$Ax$ 就是按 $x$ 的比例把各列混合起来；
3. **矩阵乘法 = 复合变换**：先做 $B$ 再做 $A$，顺序不能换——所以一般 $AB\ne BA$。

> **正文见**：[1 NumPy · 03 线性代数](../../chapters/01-numpy/03-线性代数.md)、[1 NumPy · 04 多项式与拟合](../../chapters/01-numpy/04-多项式与拟合.md)。

---

## A.2 关键概念讲解：把名词翻译成人话

### A.2.1 转置、内积与范数

| 概念 | 定义 | 人话 |
| ---- | ---- | ---- |
| 转置 | $A^T$ | 行列互换；$(AB)^T=B^TA^T$ |
| 内积 | $x\cdot y = x^Ty$ | 两个向量有多"同向" |
| 范数 | $\|x|_2=\sqrt{x^Tx}$ | 向量长度 |

例子：$x=(1,2)$，$y=(3,4)$，则 $x\cdot y = 1\times 3+2\times 4 = 11$，$\|x|_2=\sqrt{5}\approx 2.24$。内积大且同向 → 相似度高：这是余弦相似度、皮尔逊相关、注意力机制的底层直觉。

### A.2.2 逆、行列式与秩：能否把变换"倒回去"

- **逆** $A^{-1}$：把变换倒着做一遍，$A^{-1}A=I$；
- **行列式** $\det(A)$：变换后"体积"放大的倍数；$\det(A)=0$ 表示被压扁（不可逆）；
- **秩** $\mathrm{rank}(A)$：变换后空间的真正维度（列向量中线性无关的个数）；满秩方阵才可逆。

例子：$A=\begin{bmatrix}2&1\\1&2\end{bmatrix}$。$\det(A)=4-1=3\ne 0$，可逆；$A^{-1}=\frac{1}{3}\begin{bmatrix}2&-1\\-1&2\end{bmatrix}$。而 $B=\begin{bmatrix}1&2\\2&4\end{bmatrix}$ 两列成比例，$\mathrm{rank}(B)=1$，$\det(B)=0$——它把平面压成一条线，$Bx=b$ 要么无解要么无穷多解。

### A.2.3 特征值与特征向量：变换的"不动轴"

定义：若 $Av=\lambda v$（$v\ne 0$），则 $v$ 是特征向量，$\lambda$ 是特征值。人话：**有的方向被矩阵只"拉伸"不"拐弯"，拉伸倍数是特征值**。

对 $A$ 手算：$\det(A-\lambda I)=(A-\lambda I)$ 展开得 $\lambda_1=3$（方向 $(1,1)$）、$\lambda_2=1$（方向 $(1,-1)$）。即：沿对角线方向放 3 倍、沿反对角线方向不动。

用途：
- **对称矩阵**：$A=Q\Lambda Q^T$（$Q$ 正交），坐标轴转成"特征方向"后问题立刻解耦——PCA 就是找这些方向；
- **幂迭代 / PageRank / 马尔可夫链稳态**：都在找最大特征值对应的特征向量。

> 手算展开式：$\begin{vmatrix}2-\lambda & 1\\1 & 2-\lambda\end{vmatrix}=(2-\lambda)^2-1=0$，即 $\lambda=1$ 或 $3$。

### A.2.4 条件数：解有多"敏感"

$$\mathrm{cond}(A)=\|A|\cdot\|A^{-1}|$$

直觉：$b$ 变化一点点，$x$ 可能变化很多倍。条件数大（病态）≠ 无解，而是**数值上很难算准**，做模型/拟合前值得看一眼。

> **正文见**：[1 NumPy · 03 线性代数](../../chapters/01-numpy/03-线性代数.md)（条件数/病态）、[3 SciPy · 02 优化工具包](../../chapters/03-scipy/02-优化工具包.md)。

---

## A.3 深入：分解与算法（重点、难点）

### A.3.1 解方程组：高斯消元与 LU

求解 $Ax=b$ 最直接是高斯消元（上三角 + 回代）。消元等价于 $A=LU$：**一次分解、多次求解**，解多组 $b$ 时很划算。

- 复杂度 $O(n^3)$；必须**部分主元**（选最大元素当主元），避免小除数放大误差；
- 代码：`np.linalg.solve`（带主元的 LU），**不要**用 `np.linalg.inv(A) @ b`。

### A.3.2 特征值分解：对称矩阵为什么"好"

- 一般方阵：$A=V\Lambda V^{-1}$（可对角化时）。特征向量可能不正交，且可能是复数；
- **对称矩阵**：$A=A^T$ 时特征值全是实数，特征向量可正交归一：$A=Q\Lambda Q^T$。此时 $A^k=Q\Lambda^k Q^T$，求幂、求逆、判断正定都极简单；
- 用途：二次型分析（$x^TAx$ 的正定性 => 凸性）、PCA、谱聚类、稳定性分析。

### A.3.3 SVD：最重要的一段（本科必会）

**定理（SVD）**：任意 $m\times n$ 矩阵 $A$ 可写成

$$A = U\Sigma V^T$$

其中 $U$（$m\times m$）、$V$（$n\times n$）是正交矩阵，$\Sigma$ 是 $m\times n$ 的"对角矩阵"，对角线元素 $\sigma_1\ge\sigma_2\ge\cdots\ge 0$ 叫**奇异值**。

**几何解读（三步）**：先旋转（$V^T$）→ 逐方向缩放（$\Sigma$）→ 再旋转（$U$）。奇异值 = 每个方向的"重要性/能量"。

**与特征值的关系**：$A^TA$ 的特征值是 $\sigma_i^2$，$V$ 是 $A^TA$ 的特征向量；$AA^T$ 给出 $U$。所以 SVD"任意矩阵都能做"，是特征分解的"万能推广"。

**三个用途（考试/作业高频）**：

1. **最优低秩近似**（Eckart–Young）：保留前 $k$ 大奇异值得到 $A_k$，是所有秩 $k$ 矩阵中与 $A$ 的 Frobenius 距离最小者。$$\|A-A_k|_F^2 = \sum_{i>k}\sigma_i^2$$ —— 图像压缩、去噪、推荐系统都靠它。
2. **PCA**：对数据中心化后的矩阵做 SVD，$V$ 的前 $k$ 列就是主成分方向；奇异值平方占比 = 解释方差比。
3. **伪逆与最小二乘**：$A^{+}=V\Sigma^{-1}U^T$（$\Sigma^{-1}$ 取非零奇异值的倒数），比正规方程 $(A^TA)^{-1}A^Tb$ 数值更稳（避免把条件数平方）。

**数值上怎么算**：实际用 QR 迭代/分治法（库内实现），复杂度约 $O(mn^2)$（薄 SVD）。代码只需 `np.linalg.svd`。

### A.3.4 最小二乘与正则化

超定方程组 $Ax\approx b$ 的最小二乘解：

$$x^{*} = \arg\min_x\|Ax-b|_2^2 \quad\Longrightarrow\quad A^TAx = A^Tb$$

- 几何：把 $b$ 投影到 $A$ 的列空间，误差向量与列空间垂直；
- 数值：优先 $A^{+}b$（SVD）或 QR；直接求 $(A^TA)^{-1}$ 会平方条件数；
- 加惩罚 $\lambda\|x|^2$（岭回归）：在"拟合"与"不放大"之间取舍——这就是第 8 章正则化的数学原型。

### A.3.5 数值稳定性：本科最易踩的坑

| 坑 | 例子 | 正确做法 |
| ---- | ---- | ---- |
| 灾难性消去 | $\sqrt{x^2+1}-x$（大 $x$） | 改写 $1/(\sqrt{x^2+1}+x)$ |
| 显式求逆 | $A^{-1}b$ | $Ax=b$ 用 `np.linalg.solve` |
| 病态不检查 | 条件数 $10^{12}$ 硬解 | 先看 $\mathrm{cond}(A)$，换模型/加正则 |
| 忘记缩放 | PCA/距离计算被大数值特征主导 | 先标准化 |

---

## A.4 动手例题（选做：手算 + 验证）

**例 1：解方程组**。$2x+y=1$、$x+2y=2$。代入得 $x=0, y=1$。验证：`np.linalg.solve([[2,1],[1,2]],[1,2]) = [0, 1]`。

**例 2：SVD 手算 2×2**。$A=\begin{bmatrix}1&1\\1&-1\end{bmatrix}$。$A^TA=\begin{bmatrix}2&0\\0&2\end{bmatrix}$，奇异值 $\sigma_1=\sigma_2=\sqrt{2}$；$V=I$，$U=\frac{1}{\sqrt2}A$。这说明对称正交型矩阵"只缩放不旋转"，是 SVD 最简单的例子。

```python
import numpy as np
A = np.array([[1., 1.], [1., -1.]])
U, S, Vt = np.linalg.svd(A, full_matrices=False)
print(S, U @ np.diag(S) @ Vt)      # 还原 A
```

---

## A.5 Python 对应（速查）

```python
import numpy as np, sympy as sp
A = np.array([[2, 1], [1, 2]]); b = np.array([[1], [2]])

np.linalg.solve(A, b)                  # 解方程组
np.linalg.det(A); np.linalg.matrix_rank(A)
np.linalg.eig(A)                       # 特征值/特征向量
np.linalg.eigh(A) if (A == A.T).all() else None
np.linalg.svd(A, full_matrices=False)  # U, S, Vt（S 是向量！）
np.linalg.lstsq(A, b, rcond=None)
np.linalg.cond(A); np.linalg.pinv(A)
sp.Matrix(A).eigenvects()              # SymPy 符号版
```

| 你想要 | 用哪个 |
| ---- | ---- |
| 解方阵方程组 | `np.linalg.solve` |
| 最小二乘 | `np.linalg.lstsq` |
| 特征值（对称） | `np.linalg.eigh` |
| SVD | `np.linalg.svd`（注意 `S` 是向量） |
| 判断病态 | `np.linalg.cond` |

---

## A.6 常见误区

| 误区 | 正确 |
| ---- | ---- |
| `A * B` 当矩阵乘 | `*` 是逐元素；矩阵乘用 `A @ B` |
| 用 `inv(A) @ b` | 用 `solve` / `lstsq` |
| 以为 `S` 是矩阵 | SVD 返回奇异值**向量**，需 `np.diag(S)` |
| 忽略条件数 | 病态时解会"抖"，先看 `cond` |
| 非对称矩阵用 `eigh` | `eigh` 要求对称；否则用 `eig` |
| 以为 $\Sigma$ 全为正 | 非负奇异值；若出现 0 说明有"压扁"方向（降秩） |

---

## A.7 使用章节（双向）

| 章 | 哪里用到 | 链接 |
| ---- | ---- | ---- |
| 1 NumPy | 03 线性代数、05 SVD 压缩 | [正文](../../chapters/01-numpy/03-线性代数.md) |
| 2 SymPy | 矩阵与特征值 | [正文](../../chapters/02-sympy/01-符号对象与基本运算.md) |
| 3 SciPy | 优化/插值中的矩阵 | [正文](../../chapters/03-scipy/02-优化工具包.md) |
| 8 sklearn | PCA/降维 | [正文](../../chapters/08-sklearn/03-无监督学习的案例.md) |

**下游衔接**：intro-mathmodel 第 1 章（Numpy 与线性代数）、第 3 章（线性规划→非线性规划）。
**延伸阅读**：mml-book 第 2~4 章、SciPy Lectures、numpy.linalg 官方文档（见 [references.md](./references.md)）。

---

## A.10 常见考题与自查（考前 10 分钟）

| 会了吗？ | 考点 | 一句话答案 |
| ---- | ---- | ---- |
| □ | det=0 意味着什么 | 列线性相关，变换压扁，不可逆 |
| □ | 特征向量的几何含义 | 只被拉伸不改方向，拉伸倍数是特征值 |
| □ | SVD 与 PCA 的关系 | 中心化后 SVD 的右奇异向量 = 主成分方向 |
| □ | 条件数干什么 | 衡量解对输入扰动的敏感度 |
| □ | 最小二乘的几何 | 把 b 投影到列空间，残差垂直列空间 |
| □ | 为什么不用 (A^T A)^-1 | 会平方条件数，数值不稳 |
| □ | 手算 2×2 特征值 | 特征多项式 det(A - λI) = 0 |


---

## A.9 综合案例：SVD 图像压缩（串联全附录）

**目标**：把一张灰度图当作矩阵 A，用 SVD 保留前 k 个奇异值，观察压缩率与重构误差。

完整流程：

1. 读灰度图 → 数值矩阵 A（m 行 n 列）；
2. 做薄 SVD：A = U S Vt（S 是奇异值向量）；
3. 取前 k 个：A_k = U[:, :k] @ diag(S[:k]) @ Vt[:k, :]；
4. 比较：存储量从 m*n 降到 k*(m+n)；误差 = 被丢弃奇异值的平方和。

手算小例：2×2 矩阵 A = [[1,1],[1,-1]]，奇异值都是 sqrt(2)。若保留 k=1：A_1 = U1 * sqrt(2) * V1^T，会丢掉"反对角信息"——对这张图来说信息全无，说明"前 k 个"要按奇异值落差选。

参考要点代码（四空格缩进可直接运行）：

    import numpy as np, matplotlib.pyplot as plt
    A = np.random.default_rng(0).random((60, 60))
    U, S, Vt = np.linalg.svd(A, full_matrices=False)
    for k in [5, 15, 30]:
        Ak = U[:, :k] @ np.diag(S[:k]) @ Vt[:k, :]
        print(k, "MSE:", np.mean((A - Ak) ** 2), "压缩比:", A.size / (k * (A.shape[0] + A.shape[1])))

**反思**：SVD 是"数据驱动压缩"的数学核心；学完写一句结论："奇异值大的方向 = 主要信息；保留它们的低秩近似 = 最优压缩。"


---

## A.8 例题集（深入练习）

**例 1：特征值代入法**。$A=\begin{bmatrix}2&1\\1&2\end{bmatrix}$，特征多项式 $\det(A-\lambda I)=\begin{vmatrix}2-\lambda&1\\1&2-\lambda\end{vmatrix}=(2-\lambda)^2-1=0$，得 $\lambda=1,3$。代入 $\lambda=3$：$\begin{bmatrix}-1&1\\1&-1\end{bmatrix}v=0$ → $v=(1,1)$。这就是"先求特征值、再解齐次方程组"的标准流程。

**例 2：条件数实验（为什么不能直接求逆）**。构造接近奇异的 $A=\begin{bmatrix}1&1\\1&1.001\end{bmatrix}$，条件数约 $4000$：$b$ 稍微变动，解差很大。代码：

```python
import numpy as np
A = np.array([[1., 1.], [1., 1.001]])
print(np.linalg.cond(A))          # 约 4000（病态）
b1 = np.array([1., 1.]); b2 = np.array([1., 1.00001])
print(np.linalg.solve(A, b1), np.linalg.solve(A, b2))   # 解差异大
```

**例 3：SVD 压缩手算**。对 $A=\begin{bmatrix}1\\0\\0\\1\end{bmatrix}$：奇异值 $1,1$，任意正交 $U,V$。去掉一个奇异值得到零矩阵——说明"信息量全在奇异值里"。

