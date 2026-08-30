# 机器学习基础

> 一句话：机器学习就是"从数据里学一个映射"：输入特征 → 输出预测。本附录讲三大任务（回归/分类/聚类）的数学框架、损失与优化、评估与过拟合、常用模型直觉。

## E.1 学习范式

| 任务 | 数据 | 常见模型 |
| ---- | ---- | ---- |
| 监督·回归 | `(x, y)`，`y` 连续 | 线性回归、岭/Ridge、Lasso、决策树、SVR |
| 监督·分类 | `(x, y)`，`y` 离散 | 逻辑回归、决策树、随机森林、SVM、kNN |
| 无监督·聚类 | 只有 `x` | k-Means、层次聚类、DBSCAN |
| 无监督·降维 | 只有 `x` | PCA（SVD）、t-SNE、UMAP |
| 强化 | 状态/动作/奖励 | （本课程不展开） |

统一视角：**模型 = 假设集 + 损失函数 + 优化算法**。

## E.2 损失函数与优化

### 损失函数
- 回归：均方误差 `L = (1/n)Σ(y_i - f(x_i))²`（对离群点敏感）；平均绝对误差 MAE（稳健）。
- 分类：交叉熵 `L = -Σ y_i log(p_i)`（概率越"自信且正确"损失越小）。
- 聚类：k-Means 用"点到中心的距离平方和"。

### 优化
- 梯度下降：`θ ← θ - α·grad L(θ)`；批量（全量）、小批量、随机（SGD）。
- 收敛依赖：学习率 `α`（太大震、太小慢）、凸性、特征缩放。
- 正则化：`L2 (Ridge)` 防系数过大；`L1 (Lasso)` 鼓励稀疏；本质是加约束的优化（附录 B 的约束/拉格朗日思想）。

## E.3 评估与过拟合

### 关键概念
- **训练/测试划分**：测试集只评估一次；交叉验证（`k-fold`）更稳。
- **过拟合**：训练好但泛化差（模型太复杂/数据太少）。
- **欠拟合**：训练就不好。
- **偏差-方差**：总误差 ≈ 偏差² + 方差 + 噪声；复杂模型低偏差高方差。

### 指标
| 任务 | 指标 |
| ---- | ---- |
| 回归 | MSE、RMSE、MAE、R² |
| 分类 | 准确率、精确率、召回率、F1、ROC/AUC |
| 聚类 | 轮廓系数、CH 指数、DB 指数 |
| 降维 | 解释方差比、重构误差 |

> 类别不平衡时**不要只看准确率**：分类用 F1/AUC；回归用 RMSE 结合业务解释。

## E.4 常用模型直觉

| 模型 | 一句话直觉 | 超参数要点 |
| ---- | ---- | ---- |
| 线性回归 | 找一条拟合直线的"最可靠斜率" | 无；注意特征缩放 |
| Ridge/Lasso | 给系数加惩罚 | 正则强度 α |
| 逻辑回归 | 线性分数 → sigmoid → 概率 | C/惩罚项；特征缩放 |
| 决策树 | 按特征反复二分 | 深度/叶节点数（防过拟合） |
| 随机森林 | 多棵树投票，单树随机 | n_estimators；max_depth |
| SVM | 最大化"分类间隔" | kernel；C（容忍度） |
| kNN | 看最近的 k 个邻居 | k；特征缩放（用距离必缩放） |
| k-Means | 迭代挪中心 | k；初始化（n_init/seed） |
| PCA | 找方差最大的正交方向（SVD） | n_components；先标准化 |

## E.5 Python 对应（scikit-learn 流程）

```python
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score, roc_auc_score
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

X, y = ...                      # 特征/标签
X = StandardScaler().fit_transform(X)
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2, random_state=0)

clf = LogisticRegression(C=1.0, max_iter=1000)
clf.fit(Xtr, ytr)
print(accuracy_score(yte, clf.predict(Xte)), f1_score(yte, clf.predict(Xte)))
print(roc_auc_score(yte, clf.predict_proba(Xte)[:, 1]))

kmeans = KMeans(n_clusters=3, n_init=10, random_state=0).fit(X)
pca = PCA(n_components=2).fit_transform(X)
```

## E.6 常见误区

| 误区 | 正确 |
| ---- | ---- |
| 不看数据先调模型 | 先 EDA + 清洗 + 特征缩放 |
| 用测试集反复调参 | 用验证集/交叉验证；测试集最后用一次 |
| 类别不平衡只看准确率 | 看 F1/AUC/PR |
| 聚类 k 随便定 | 用肘部法/轮廓系数；结果与初始化有关要固定种子 |
| PCA 前不标准化 | 方差大的变量会主导；先 `StandardScaler` |
| 以为模型越复杂越好 | 交叉验证下选"够用"的复杂度 |

## E.7 使用章节与下游衔接

- 章节：8 sklearn（预处理/监督/无监督/PCA）、5 Matplotlib（评估可视化）、3 SciPy（优化）；
- 数学底子：附录 A（SVD/PCA）、附录 B（优化）、附录 C（统计推断/回归）都在这里汇合；
- 下游：intro-mathmodel 第 9 章（机器学习与统计模型）；
- 参考：scikit-learn User Guide、mml-book Part II、《机器学习》周志华（见 references.md）。
