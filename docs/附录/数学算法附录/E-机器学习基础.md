# 机器学习基础

> 本附录为第 8 章 scikit-learn 提供数学框架：学习范式、损失与优化、评估与过拟合、模型直觉；并接上附录 A（SVD/PCA）与附录 B（优化）。补上本科难点：偏差-方差分解、交叉熵直觉、正则化几何。

---

## E.1 直觉故事：为什么模型会"学偏"

用"学习时长"预测"考试成绩"，数据近似一条直线，线性回归找"斜率+截距"。

但只有 5 个学生、加了 10 个特征（连"头发长度"都算），线性回归能**完美穿过所有 5 个点**——换一批学生就崩。这就是**过拟合**：记住训练集，没学普适规律。

核心矛盾：**训练集上够准 + 新数据上也准**。靠"任务框架（损失）+ 优化 + 验证评估 + 正则化/适当复杂度"解决。

> **正文见**：[8 sklearn · 01 数据集的预处理](../../chapters/08-sklearn/01-数据集的预处理.md)、[8 sklearn · 02 有监督学习的案例](../../chapters/08-sklearn/02-有监督学习的案例.md)。

---

## E.2 学习范式与损失函数（讲解）

### E.2.1 三大任务

| 任务 | 输入/输出 | 常见模型 |
| ---- | ---- | ---- |
| 回归 | $(x,y)$，$y$ 连续 | 线性回归、Ridge/Lasso、决策树、SVR |
| 分类 | $(x,y)$，$y$ 离散 | 逻辑回归、决策树、随机森林、SVM |
| 聚类 | 只有 $x$ | k-Means、层次聚类、DBSCAN |
| 降维 | 只有 $x$ | PCA（SVD）、t-SNE、UMAP |

统一视角：**模型 = 假设集 + 损失函数 + 优化算法**。

### E.2.2 损失函数：怎么算"错得有多离谱"

- **回归·MSE**：$L=\frac{1}{n}\sum(y_i-f(x_i))^2$——对离群点敏感；RMSE 是平方根，量纲与 $y$ 一致；
- **回归·MAE**：$\frac{1}{n}\sum|y_i-f(x_i)|$——更稳健；
- **分类·交叉熵**：$L=-\sum y_i\log p_i$——鼓励"预测概率对且自信"；与逻辑回归天然搭配（sigmoid 的梯度形式漂亮）；
- **聚类·k-Means**：点到最近中心的平方距离之和（WCSS），肘部法选 $k$。

### E.2.3 优化：把损失调小

梯度下降：$\theta\gets\theta-\alpha\nabla L(\theta)$。

手算：$L(\theta)=(\theta-3)^2$，$\theta_0=1$，$\nabla L=2(\theta-3)=-4$。$\alpha=0.5$ → 一步到 3；$\alpha=2$ → 弹到 9——**学习率太大震荡**。实际还要做特征缩放（不同特征"感受"不同学习率）。

**正则化（几何视角）**：Ridge 加 $\lambda\|\theta|^2$（系数不过大）；Lasso 加 $\lambda\|\theta|_1$（鼓励稀疏）。本质是在"拟合误差"与"解的大小"之间取舍；$\lambda$ 越大越"保守"。

---

## E.3 评估与过拟合（重点、难点）

### E.3.1 训练/验证/测试

- 训练集：学参数；验证集/交叉验证：挑超参数；测试集：最后评估一次；
- 交叉验证（$k$-fold）：数据切 $k$ 份轮流验证，结果更稳；
- **别用测试集反复调参**——等于把测试集"教"给模型。

### E.3.2 偏差-方差分解（必考理解）

$$E[(f-\hat f)^2]=\underbrace{\mathrm{Bias}^2}_{\text{欠拟合}} + \underbrace{\mathrm{Var}}_{\text{过拟合}} + \sigma^2$$

- 太简单 → 高偏差（欠拟合）；太复杂 → 高方差（过拟合）；噪声 $\sigma^2$ 不可约；
- 调复杂度（深度/正则/特征数）就是找偏差-方差平衡点。

### E.3.3 指标怎么选

| 任务 | 指标 | 注意 |
| ---- | ---- | ---- |
| 回归 | MSE/RMSE/MAE/$R^2$ | 结合业务解读 |
| 分类 | 准确率/精确率/召回率/F1/ROC-AUC | 类别不平衡别只看准确率 |
| 聚类 | 轮廓系数/CH/DB | 与 $k$、距离度量有关 |
| 降维 | 解释方差比/重构误差 | 先标准化再 PCA |

---

## E.4 常用模型直觉（讲解 + 速查）

| 模型 | 一句话直觉 | 关键超参 |
| ---- | ---- | ---- |
| 线性回归 | 找一条"最不怨"的直线 | 无；特征缩放 |
| Ridge/Lasso | 给斜率"限高" | $\alpha$ |
| 逻辑回归 | 线性分数 → sigmoid → 概率 | $C$（正则强度） |
| 决策树 | 按特征反复二分 | $\mathrm{max_depth}$、$\mathrm{min_samples_leaf}$ |
| 随机森林 | 多棵随机树投票 | $\mathrm{n_estimators}$、$\mathrm{max_depth}$ |
| SVM | 最大化分类间隔 | $\mathrm{kernel}$、$C$ |
| kNN | 看最近的 $k$ 个邻居 | $k$、特征缩放（必须） |
| k-Means | 迭代挪中心 | $k$、$\mathrm{n_init}$、种子 |
| PCA | 找方差最大的正交方向 | $\mathrm{n_components}$、先标准化 |

> PCA 的数学就是附录 A 的 SVD：特征矩阵做 SVD，右奇异向量即主成分方向；取前 $k$ 个 = 最优低秩近似。

---

## E.5 动手例题（选做）

**例：过拟合实验**。8 个点，$\mathrm{degree}=1$（直线）与 $\mathrm{degree}=9$（9 次多项式）：

- 直线：训练 RMSE 大一点，但换数据也稳；
- 9 次：训练 RMSE 几乎为 0，但预测新点剧烈摆动——"训练好 ≠ 泛化好"。

```python
import numpy as np
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

rng = np.random.default_rng(0)
X = np.sort(rng.uniform(0, 1, 8))[:, None]
y = np.sin(6 * X[:, 0]) + rng.normal(0, 0.1, 8)
for deg in [1, 9]:
    m = make_pipeline(PolynomialFeatures(deg), LinearRegression()).fit(X, y)
    print(deg, mean_squared_error(y, m.predict(X)) ** 0.5)
```

**例：为什么先做特征缩放**。"体重(kg) 50~100" + "身高(m) 1.5~2.0"：距离/梯度被体重主导。用 `StandardScaler` 后两者同量纲，kNN/PCA/梯度类模型才可靠。

---

## E.6 Python 对应（scikit-learn 标准流程，速查）

```python
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (accuracy_score, f1_score, roc_auc_score, silhouette_score)
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

X, y = ...                                  # 先 EDA
X = StandardScaler().fit_transform(X)       # 先缩放！
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2, random_state=0)

clf = LogisticRegression(C=1.0, max_iter=1000).fit(Xtr, ytr)
print(accuracy_score(yte, clf.predict(Xte)),
      f1_score(yte, clf.predict(Xte), zero_division=0),
      roc_auc_score(yte, clf.predict_proba(Xte)[:, 1]))

cross_val_score(LogisticRegression(), X, y, cv=5)
KMeans(n_clusters=3, n_init=10, random_state=0).fit(X)
PCA(n_components=2).fit_transform(X)
```

| 你想要 | 用哪个 |
| ---- | ---- |
| 划分/缩放 | `train_test_split` / `StandardScaler` |
| 评估 | `cross_val_score` + 指标函数 |
| 聚类 | `KMeans` + `silhouette_score` |
| 降维 | `PCA` |
| 特征重要性 | 树模型 `feature_importances_` |

---

## E.7 常见误区

| 误区 | 正确 |
| ---- | ---- |
| 不看数据直接建模 | 先 EDA、缺失值、异常值、缩放 |
| 反复用测试集调参 | 用验证/交叉验证，测试集只碰一次 |
| 类别不平衡只看准确率 | 看 F1/AUC/PR |
| PCA 前不标准化 | 方差大的特征主导；先 `StandardScaler` |
| 聚类只跑一遍 | 结果与初始化有关；固定种子、多 `n_init` |
| 模型越复杂越好 | 交叉验证选"够用"的复杂度 |

---

## E.8 使用章节（双向）

| 章 | 哪里用到 | 链接 |
| ---- | ---- | ---- |
| 8 sklearn | 预处理/监督/无监督 | [01 数据集的预处理](../../chapters/08-sklearn/01-数据集的预处理.md) |
| 8 sklearn | 模型训练与评估 | [02 有监督学习的案例](../../chapters/08-sklearn/02-有监督学习的案例.md) |
| 8 sklearn | 聚类/PCA | [03 无监督学习的案例](../../chapters/08-sklearn/03-无监督学习的案例.md) |
| 5 Matplotlib | 评估可视化 | [01 基本绘图](../../chapters/05-matplotlib/01-基本绘图.md) |

**数学底子**：附录 A（SVD/PCA）、附录 B（优化）、附录 C（统计推断/回归）。
**下游衔接**：intro-mathmodel 第 9 章（机器学习与统计模型）。
**延伸阅读**：scikit-learn User Guide、mml-book Part II、《机器学习》周志华（见 [references.md](./references.md)）。

---

## E.11 常见考题与自查（考前 10 分钟）

| 会了吗？ | 考点 | 一句话答案 |
| ---- | ---- | ---- |
| □ | 过拟合的表现 | 训练好、测试差；高方差 |
| □ | 欠拟合 | 训练就不好；高偏差 |
| □ | 偏差-方差分解 | 总误差 = 偏差^2 + 方差 + 噪声 |
| □ | 类别不平衡看什么 | F1 / AUC，不看准确率 |
| □ | 正则化作用 | 限制系数大小，防过拟合 |
| □ | k 怎么选 | 肘部法 + 轮廓系数；固定种子多试 |
| □ | PCA 前为什么缩放 | 大数值特征主导方差 |


---

## E.10 综合案例：一次完整的建模流程（期末大作业可直接套）

**问题**：用订单数据预测"销售额"，并解释模型。

步骤：

1. **EDA**：缺失值、离群点、分布（直方图/箱线图）；
2. **特征**：类别编码、数值缩放；训练/测试 8:2，固定种子；
3. **基线**：线性回归先跑，看 RMSE 与 R^2；
4. **交叉验证**：5 折，比较线性/岭/树模型，选"够用"的；
5. **调复杂度**：对树模型调 max_depth，对岭模型调 alpha（用验证集，不动测试集）；
6. **解释**：特征重要性/系数符号、残差图，写 3 条业务结论；
7. **最终**：测试集只跑一次，报告指标与局限性。

参考要点代码：

    from sklearn.model_selection import train_test_split, cross_val_score
    from sklearn.linear_model import Ridge
    from sklearn.preprocessing import StandardScaler
    from sklearn.metrics import mean_squared_error
    Xs = StandardScaler().fit_transform(X)
    Xtr, Xte, ytr, yte = train_test_split(Xs, y, test_size=0.2, random_state=0)
    m = Ridge(alpha=1.0).fit(Xtr, ytr)
    scores = cross_val_score(Ridge(alpha=1.0), Xtr, ytr, cv=5,
                         scoring="neg_mean_squared_error")
print(scores)
    print(mean_squared_error(yte, m.predict(Xte)) ** 0.5)

**反思**：把附录 E 的"损失/评估/过拟合"变成一套可复用流程，期末大作业与科研都适用。


---

## E.9 例题集（深入练习）

**例 1：梯度下降手算 3 步**。$L(\theta)=(\theta-3)^2$，$\alpha=0.5$：$\theta_0=1$ → $\theta_1=3$（一步到最优）。若 $\alpha=0.9$：$1\to 4.6\to 2.48\to 3.42\to 2.82\to 3.07\to …$——震荡收敛。**结论**：步长太大振荡、太小慢。

**例 2：逻辑回归 sigmoid 手算**。$\theta^Tx=0\to p=0.5$（边界）；$=2\to p\approx0.88$；$=-2\to p\approx0.12$——线性分数越大，概率越接近 1。

**例 3：$R^2$ 手算**。数据 $(0,1),(1,2),(2,3)$，拟合 $\hat y=x+1$ 无残差：SSE=0，SST=2（$y$ 的方差×n），$R^2=1$。若 $\hat y=2$（常数预测）：SSE=2，SST=2，$R^2=0$——"不比平均更好"。

```python
from sklearn.metrics import r2_score
print(r2_score([1,2,3], [1,2,3]))   # 1.0
print(r2_score([1,2,3], [2,2,2]))   # 0.0
```

**例 4：交叉验证的意义**。只用一次 hold-out 可能"切巧了"；5 折交叉验证给出 5 个分数的平均与波动，更值得信。

