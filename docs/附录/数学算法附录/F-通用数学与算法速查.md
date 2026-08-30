# 通用数学与算法速查

> 本附录是"随手翻"的卡片：常用记号、公式、复杂度、数值稳定性、可视化原则与术语英中对照。建议上机前翻 5 分钟，期末大作业前完整过一遍。

---

## F.1 常用记号与希腊字母（速查）

| 记号 | 含义 | | 记号 | 含义 |
| ---- | ---- | ---- | ---- | ---- |
| $\sum$ | 求和 | | $\prod$ | 连乘 |
| $E[X]$ | 期望 | | $\mathrm{Var}(X)$ | 方差 |
| $x^T$ | 转置 | | $\nabla f$ | 梯度 |
| $\partial f/\partial x$ | 偏导 | | $\int$ | 积分 |
| $\lambda$ | 特征值/正则强度 | | $\alpha$ | 学习率 |
| $\theta$ | 参数/角度 | | $\varepsilon$ | 误差/小量 |
| $\approx$ | 约等于 | | $\ll$ | 远小于 |

**读公式的口诀**：先找求和/连乘范围，再看指数/对数在谁身上，最后看变量是矩阵还是标量。

---

## F.2 常用公式卡（速查）

### 微积分
- $(x^n)'=nx^{n-1}$；$(e^x)'=e^x$；$(\ln x)'=1/x$
- 泰勒：$f(x+h)\approx f(x)+f'(x)h+\tfrac12 f''(x)h^2$
- 数值微分（中心差分）：$f'(x)\approx\dfrac{f(x+h)-f(x-h)}{2h}$

### 线性代数
- $(AB)^T=B^TA^T$；$\mathrm{tr}(AB)=\mathrm{tr}(BA)$
- 最小二乘：$x^{*}=\mathrm{arg\min}_x\|Ax-b|_2^2$（数值用 `lstsq`）
- SVD：$A=U\Sigma V^T$；对称矩阵：$A=Q\Lambda Q^T$

### 概率统计
- $E[X]=\sum x\,p(x)$；$\mathrm{Var}(X)=E[X^2]-(E[X])^2$
- 样本方差：$s^2=\frac{1}{n-1}\sum(x_i-\bar{x})^2$
- 置信区间：$\bar{x}\pm t_{\alpha/2,n-1}\cdot s/\sqrt n$
- 线性回归：$y=X\beta+\varepsilon$，$\hat{\beta}=(X^TX)^{-1}X^Ty$，$R^2=1-\mathrm{SSE}/\mathrm{SST}$

### 机器学习
- 逻辑回归（sigmoid）：$p=1/(1+e^{-\theta^Tx})$；损失 = 交叉熵
- 梯度下降：$\theta\gets\theta-\alpha\nabla L$
- 正则化：Ridge $L+\lambda\|\theta|^2$；Lasso $L+\lambda\|\theta|_1$

---

## F.3 复杂度与常用算法量级（速查）

| 运算 | 复杂度 | 备注 |
| ---- | ---- | ---- |
| 矩阵乘/解方程组（$n\times n$） | $O(n^3)$ | 向量化库已优化；避免显式求逆 |
| 特征分解 / SVD | 约 $O(n^3)$ | 只求前 $k$ 个可加速 |
| FFT | $O(N\log N)$ | 比 $O(N^2)$ 直接 DFT 快得多 |
| Dijkstra | $O((V+E)\log V)$ | 堆实现 |
| Kruskal MST | $O(E\log E)$ | 排序为主 |
| k-Means 一次迭代 | $O(n\cdot k\cdot d)$ | 与样本数线性 |
| Python 纯循环 | 慢 | 用 NumPy 向量化/广播 |

**实践建议**：先写对，再量（`%timeit`）；大数据用向量化，循环只在必要时。

---

## F.4 数值稳定性（科学计算必修，讲解）

浮点数是有限精度（约 15~16 位有效小数），"数学上对的公式"在电脑上可能"崩"：

1. **比较**：别用 `==` 比浮点；用 `np.isclose` / $|a-b|<10^{-9}$；
2. **条件数**：$\mathrm{cond}(A)$ 大 → 病态，解对输入过敏；
3. **灾难性消去**：$\sqrt{x^2+1}-x$（大 $x$）→ 改写 $1/(\sqrt{x^2+1}+x)$；
4. **缩放**：优化/距离/聚类前标准化（`StandardScaler`）；
5. **对数域**：连乘小概率取 log 防下溢；分类用 `log_proba`；
6. **可复现**：固定种子（`random_state` / `default_rng(seed)`）。

手算直觉：$x=10^8$ 时 $\sqrt{x^2+1}-x$ 双精度算出来约 0（真值约 $5\times 10^{-9}$）——不是数学错了，是浮点"看不见"那么小的差。

---

## F.5 关键词索引（速查）

| 你想查 | 去哪 |
| ---- | ---- |
| 矩阵/分解/最小二乘 | [附录 A](./A-线性代数与矩阵.md) |
| 导数/积分/优化/插值/FFT/ODE | [附录 B](./B-微积分与数值方法.md) |
| 分布/检验/回归/时序 | [附录 C](./C-概率统计基础.md) |
| 图/路径/中心性/社区 | [附录 D](./D-图论与网络.md) |
| 损失/评估/模型/过拟合 | [附录 E](./E-机器学习基础.md) |
| 记号/公式/复杂度/稳定性 | 本附录 F |
| 全书目 | [附录 G · 全书总参考文献](./G-全书参考文献.md) |

---

## F.6 使用章节（双向）

| 章 | 用法 | 链接 |
| ---- | ---- | ---- |
| 0 前置基础 | 成绩统计公式 | [07 综合案例](../../chapters/00-prep/00-07-综合案例.md) |
| 1 NumPy | 数值稳定性/向量化 | [02 数组运算](../../chapters/01-numpy/02-数组运算.md) |
| 3 SciPy | 优化/插值上下界 | [02 优化工具包](../../chapters/03-scipy/02-优化工具包.md) |
| 5 Matplotlib | 可视化原则 | [01 基本绘图](../../chapters/05-matplotlib/01-基本绘图.md) |
| 8 sklearn | 特征缩放/评估 | [01 数据集的预处理](../../chapters/08-sklearn/01-数据集的预处理.md) |

**可视化原则（配合第 5 章）**：一图一信息；坐标轴标清楚；柱状看类别、直方看分布、散点看关系、折线看趋势；标注单位/图例/样本量；颜色兼顾色盲。

---

## F.7 术语英中对照（速查）

| 英文 | 中文 | 出现在 |
| ---- | ---- | ---- |
| matrix / vector | 矩阵 / 向量 | 附录 A |
| eigenvalue / singular value | 特征值 / 奇异值 | 附录 A、E |
| least squares | 最小二乘 | 附录 A、C、E |
| gradient / Hessian | 梯度 / 黑塞矩阵 | 附录 B、E |
| interpolation / fitting | 插值 / 拟合 | 附录 B |
| hypothesis test / p-value | 假设检验 / p 值 | 附录 C |
| confidence interval | 置信区间 | 附录 C |
| central limit theorem | 中心极限定理 | 附录 C |
| shortest path / MST | 最短路 / 最小生成树 | 附录 D |
| centrality / community | 中心性 / 社区 | 附录 D |
| loss / regularization | 损失 / 正则化 | 附录 E |
| overfitting / cross-validation | 过拟合 / 交叉验证 | 附录 E |
| complexity / numerical stability | 复杂度 / 数值稳定性 | 附录 F |

**一句话总结**：遇到不认识的名词，先查这张表，再进对应主题读"直觉故事"。

---

## F.9 考前 10 分钟清单（全附录）

1. 记号：$\sum$、$E[X]$、$\nabla$、$A^T$——见 F.1；
2. 公式：导数/积分/最小二乘/置信区间/正则化——见 F.2；
3. 复杂度：矩阵乘 $O(n^3)$、FFT $O(N\log N)$、Dijkstra $O((V+E)\log V)$——见 F.3；
4. 数值稳定性：条件数、灾难消去、缩放、对数域——见 F.4；
5. 关键词索引：哪类问题看哪个附录——见 F.5；
6. 术语英中：matrix、loss、p-value……——见 F.7；
7. 常用技巧：向量化、log 域、日志坐标、NaN 处理、种子——见 F.8。

**最后一句**：先看"直觉故事"建立画面，再用"速查表"拿公式，最后用"例题集"练手。


---

## F.8 数值小技巧（速查）

1. 求和/连乘尽量用向量化；避免 Python 循环里重复分配大数组；
2. 概率乘积取对数：`np.log` + `np.sum`；
3. 画图前把大数值日志化（`plt.yscale("log")`）；
4. 长序列先 `np.fft.fft` 看谱，再决定滤波/平滑；
5. 拟合前先 `np.nan_to_num`/去掉缺失，避免 NaN 传染；
6. 复现：所有随机过程给 `random_state`/种子，并写进报告。

