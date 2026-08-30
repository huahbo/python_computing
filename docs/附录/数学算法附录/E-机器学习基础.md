# 机器学习基础

> 一句话：机器学习就是"从数据里学一个映射"。本附录把第 8 章 scikit-learn 背后的数学框架、损失/优化、评估与过拟合、模型直觉讲清楚，并接上附录 A（SVD/PCA）与附录 B（优化）。

---

## E.1 直觉故事：为什么模型会"学偏"

假设你用"学习时长"预测"考试成绩"，数据点大致在一条斜线附近。线性回归的任务就是找到"最合适的斜率与截距"。

但换个场景：只有 5 个学生，你加了 10 个特征（连"头发长度"都算上）。线性回归可以**完美穿过所有 5 个点**——看起来成绩很漂亮，但换一批学生就崩了。这就是**过拟合**：模型记熟了训练数据，却没学到普适规律。

所以机器学习的核心矛盾是：**如何在"训练集上够准"和"新数据上也准"之间平衡。** 答案是：任务框架（损失）+ 优化算法 + 验证评估 + 正则化/恰当复杂度。

> **正文见**：[8 sklearn · 01 数据集的预处理](../../chapters/08-sklearn/01-数据集的预处理.md)（训练/测试划分、特征工程）、[8 sklearn · 02 有监督学习的案例](../../chapters/08-sklearn/02-有监督学习的案例.md)。

---

## E.2 学习范式与损失函数（讲解）

### E.2.1 三大任务

| 任务 | 输入/输出 | 常见模型 |
| ---- | ---- | ---- |
| 回归 | `(x, y)`，`y` 连续 | 线性回归、Ridge/Lasso、决策树、SVR |
| 分类 | `(x, y)`，`y` 离散 | 逻辑回归、决策树、随机森林、SVM |
| 聚类 | 只有 `x` | k-Means、层次聚类、DBSCAN |
| 降维 | 只有 `x` | PCA（SVD）、t-SNE |

统一视角：**模型 = 假设集 + 损失函数 + 优化算法**。

### E.2.2 损失函数：怎么算"错得有多离谱"

- **回归·均方误差 MSE**：`L = (1/n)Σ(y_i - f(x_i))²`。对离群点敏感；RMSE 是它的平方根，量纲与 y 一致。
- **回归·平均绝对误差 MAE**：`(1/n)Σ|y_i - f(x_i)|`，更稳健。
- **分类·交叉熵**：`L = -Σ y_i log(p_i)`。鼓励"预测概率对且自信"；与逻辑回归配合自然。
- **聚类·k-Means**：点到最近中心的平方距离之和（WCSS），肘部法看拐点选 k。

### E.2.3 优化：把损失调小

梯度下降：`θ ← θ - α·grad L(θ)`。

手算直觉：设 `L(θ) = (θ - 3)²`，`θ0 = 1`，`grad L = 2(θ-3) = -4`。取 `α = 0.5`：`θ ← 1 - 0.5×(-4) = 3`，一步到最优。取 `α = 2`：`θ ← 1 - 2×(-4) = 9`，弹到另一侧——这就是**学习率太大震荡**。实际操作中，还要做特征缩放（否则不同特征的学习率感受不同）。

**正则化**（在损失里加惩罚）：Ridge 加 `λ||θ||²`（系数不过大），Lasso 加 `λ||θ||₁`（鼓励稀疏）。本质是把"拟合"和"模型复杂度"放在一个天平上。

---

## E.3 评估与过拟合（讲解）

### E.3.1 训练/验证/测试

- **训练集**：学参数；**验证集/交叉验证**：挑超参数；**测试集**：最后评估一次。
- 交叉验证（`k-fold`）：数据切 k 份轮流当验证集，结果更稳。
- **千万别用测试集反复调参**——那等于把测试集"教"给模型。

### E.3.2 偏差-方差

总误差 ≈ 偏差² + 方差 + 噪声：
- 太简单模型：高偏差（欠拟合）；
- 太复杂模型：高方差（过拟合，训练好、测试差）；
- 调复杂度（深度/正则/特征数）就是在这两者间找平衡。

### E.3.3 指标怎么选

| 任务 | 指标 | 注意 |
| ---- | ---- | ---- |
| 回归 | MSE/RMSE/MAE/R² | 结合业务解读；R² 高≠模型好 |
| 分类 | 准确率/精确率/召回率/F1/ROC-AUC | 类别不平衡别只看准确率 |
| 聚类 | 轮廓系数/CH/DB | 与 k 和距离度量有关 |
| 降维 | 解释方差比/重构误差 | 先标准化再 PCA |

---

## E.4 常用模型直觉（讲解 + 速查）

| 模型 | 一句话直觉 | 关键超参 |
| ---- | ---- | ---- |
| 线性回归 | 找一条"最不怨"的直线 | 无；特征缩放 |
| Ridge/Lasso | 给斜率"限高" | `alpha` |
| 逻辑回归 | 线性分数 → sigmoid → 概率 | `C`（正则强度） |
| 决策树 | 按特征反复二分 | `max_depth`、`min_samples_leaf` |
| 随机森林 | 多棵随机树投票 | `n_estimators`、`max_depth` |
| SVM | 最大化分类间隔 | `kernel`、`C` |
| kNN | 看最近的 k 个邻居 | `k`、特征缩放（必须） |
| k-Means | 迭代挪中心 | `k`、`n_init`、种子 |
| PCA | 找方差最大的正交方向 | `n_components`、先标准化 |

> PCA 的数学就是附录 A 的 SVD：特征矩阵做 SVD，右奇异向量就是主成分方向；取前 k 个 = 最优低秩近似。

---

## E.5 动手例题（选做：手算 + 验证）

**例：过拟合的直观实验**。只有 8 个点，用 @BT@degree=1@BT@（直线）和 @BT@degree=9@BT@（9 次多项式）拟合：

- 直线：训练 RMSE 大一点，但换数据也稳定；
- 9 次多项式：训练 RMSE 几乎为 0（完美穿过所有点），但预测新点会剧烈摆动。

这就是"训练好 ≠ 泛化好"。

```python
import numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

rng = np.random.default_rng(0)
X = np.sort(rng.uniform(0, 1, 8))[:, None]
y = np.sin(6 * X[:, 0]) + rng.normal(0, 0.1, 8)

for deg in [1, 9]:
    m = make_pipeline(PolynomialFeatures(deg), LinearRegression()).fit(X, y)
    print(deg, "train RMSE:", mean_squared_error(y, m.predict(X)) ** 0.5)
```

**例：为什么先做特征缩放**。特征"体重(kg)"范围 50~100，"身高(m)"范围 1.5~2.0——距离/梯度方向被体重主导。用 @BT@StandardScaler@BT@ 后两者同量纲，kNN/PCA/梯度类模型才可靠。

## E.6 Python 对应（scikit-learn 标准流程，速查）

```python
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LogisticRegression, Ridge
from sklearn.metrics import (accuracy_score, f1_score, roc_auc_score,
                             mean_squared_error, silhouette_score)
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

X, y = ...                                   # 特征/标签（先 EDA）
X = StandardScaler().fit_transform(X)        # 先缩放！
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2, random_state=0)

clf = LogisticRegression(C=1.0, max_iter=1000)
clf.fit(Xtr, ytr)
print(accuracy_score(yte, clf.predict(Xte)),
      f1_score(yte, clf.predict(Xte), zero_division=0),
      roc_auc_score(yte, clf.predict_proba(Xte)[:, 1]))

scores = cross_val_score(LogisticRegression(), X, y, cv=5)   # 交叉验证

kmeans = KMeans(n_clusters=3, n_init=10, random_state=0).fit(X)
print(silhouette_score(X, kmeans.labels_))
pca = PCA(n_components=2).fit_transform(X)
```

| 你想要 | 用哪个 |
| ---- | ---- |
| 划分/缩放 | `train_test_split` / `StandardScaler` |
| 评估 | `cross_val_score` + 指标函数 |
| 聚类 | `KMeans` + `silhouette_score` |
| 降维 | `PCA` |
| 特征重要性 | 树模型 `feature_importances_` |

---

## E.7 常见误区 + 用在哪（双向）

| 误区 | 正确 |
| ---- | ---- |
| 不看数据直接建模 | 先 EDA、缺失值、异常值、缩放 |
| 反复用测试集调参 | 用验证/交叉验证，测试集只碰一次 |
| 类别不平衡只看准确率 | 看 F1/AUC/PR |
| PCA 前不标准化 | 方差大的特征会主导；先 `StandardScaler` |
| 聚类只跑一遍 | 结果与初始化有关；固定种子、多 n_init |
| 模型越复杂越好 | 交叉验证选"够用"的复杂度（偏差-方差） |

**使用章节（可点击）**
| 章 | 哪里用到 | 链接 |
| ---- | ---- | ---- |
| 8 sklearn | 预处理/监督/无监督 | [01 数据集的预处理](../../chapters/08-sklearn/01-数据集的预处理.md) |
| 8 sklearn | 模型训练与评估 | [02 有监督学习的案例](../../chapters/08-sklearn/02-有监督学习的案例.md) |
| 8 sklearn | 聚类/PCA | [03 无监督学习的案例](../../chapters/08-sklearn/03-无监督学习的案例.md) |
| 5 Matplotlib | 评估可视化 | [01 基本绘图](../../chapters/05-matplotlib/01-基本绘图.md) |

**数学底子**：附录 A（SVD/PCA）、附录 B（优化）、附录 C（统计推断/回归）在本主题汇合。
**下游衔接**：intro-mathmodel 第 9 章（机器学习与统计模型）。
**延伸阅读**：scikit-learn User Guide、mml-book Part II、《机器学习》周志华（见 [references.md](./references.md)）。

---

## E.8 补充：模型选择地图（怎么一步步选）

| 问题 | 先试 | 再试 | 别用 |
| ---- | ---- | ---- | ---- |
| 预测连续值、特征少 | 线性回归 | Ridge/Lasso、树模型 | —— |
| 预测类别、特征多 | 逻辑回归 | 随机森林、SVM | 只在训练集上调参 |
| 没有标签、想分组 | k-Means | 层次聚类、DBSCAN | 不看轮廓系数就报 k |
| 特征太多、要可视化 | PCA | t-SNE/UMAP | 不标准化 |
| 数据不平衡 | 调权重/采样 | F1/AUC | 只看准确率 |

**决策顺序建议**：问题类型 → 特征处理（缺失/缩放/编码）→ 简单模型基线 → 评估 → 调复杂度（正则/深度）→ 交叉验证 → 最终测试一次。

