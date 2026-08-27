# 第 8 章 作业（scikit-learn，12 题）

**说明**：完成前请先读 `../01-数据集的预处理.md` ~ `../04-综合案例.md`，并跑通 `lab/`。下列题目分**简答 / 编程 / 综合**三档。

---

## 一、概念与简答（1–4）

1. **fit / transform / fit_transform**：三者的区别是什么？为什么在训练/测试数据切分后，不能用 `fit_transform` 直接处理测试集？

2. **编码**：对“颜色（红/绿/蓝）”和“学历（本科/硕士/博士）”这两类特征，分别应选 `OneHotEncoder` 还是 `OrdinalEncoder`？说明理由。

3. **缩放**：`StandardScaler` 与 `MinMaxScaler` 分别适用什么场景？为什么 SVM、KNN、KMeans 通常建议先缩放，而决策树/随机森林通常不需要？

4. **指标**：分类问题常用哪些指标？回归问题常用哪些指标？`accuracy_score` 与 `roc_auc_score` 各衡量什么？

---

## 二、编程（5–9）

5. **OneHot + 缩放**：用 `OneHotEncoder` 把 `['M','F','M','F']` 编码成稠密矩阵，再用 `StandardScaler` 对数值矩阵 `[[1,2],[3,4],[5,6]]` 缩放，分别打印结果。

6. **交叉验证**：在 `load_iris()` 上做 80/20 切分（`random_state=42`、`stratify=y`），用 `LogisticRegression(max_iter=1000)` 做 5 折 `cross_val_score`，打印每折分数与均值。

7. **特征选择 + 分类**：用 `SelectKBest(mutual_info_classif, k=2)` 在 Iris 上选 2 个特征，放入 `Pipeline` 后接 `LogisticRegression`，计算 5 折平均准确率。

8. **回归**：在 `load_diabetes()` 上用 `LinearRegression` 与 `Lasso(alpha=0.1)` 拟合，输出测试集 `MSE` 与 `R²`，并打印 Lasso 的非零系数个数。

9. **聚类与降维**：用 `make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=0)` 做 `KMeans(n_clusters=4, random_state=0)`，打印 `inertia_` 与 `silhouette_score`；再对 `load_iris()` 做 `PCA(n_components=2)`，打印累计解释方差比。

---

## 三、综合（10–12）

10. **端到端分类**：在 `load_breast_cancer()` 上，用 `Pipeline`（`StandardScaler` + `SVC`）做 5 折交叉验证；再与“不缩放”的 `SVC` 比较，给出结论。

11. **模型调参**：在 `load_iris()` 上用 `RandomForestClassifier` 与 `GridSearchCV` 搜索 `n_estimators ∈ {50,100}`、`max_depth ∈ {None,3,5}`，输出最佳参数与最佳 5 折得分。

12. **综合案例**：参照 `../04-综合案例.md`，对 Wine 数据完成“缩放 + 分类 + KMeans + PCA”，输出：分类器的 5 折均值、KMeans 的 ARI、PCA 前两主成分累计方差，并写 3 句结论。

---

## 参考答案要点

1. `fit` 学习统计量，`transform` 应用，`fit_transform` 一步完成；测试集只能用训练集学到的统计量（否则泄漏），放进 `Pipeline` 最稳妥。
2. 颜色无序 → `OneHotEncoder`；学历有序 → `OrdinalEncoder`（并显式 `categories`）。
3. `StandardScaler` 对异常值更稳健；`MinMaxScaler` 强制到区间；距离类算法依赖量纲故需缩放，树模型按阈值切分不依赖量纲。
4. 分类：accuracy / precision / recall / F1 / confusion_matrix / ROC-AUC；回归：MSE / MAE / R² / explained_variance。`accuracy` 看“命中率”，`AUC` 看“排序能力”，不平衡时 AUC 更稳。
5. 参考 01 节输出；注意 OneHot 用 `sparse_output=False`。
6. 参考 01 节：`cross_val_score` 各折约 0.95–1，均值约 0.97。
7. 参考 01 节：选到特征索引 `[2,3]`，5 折均值约 0.96。
8. 参考 02 节：LinearRegression `MSE≈2900.19, R²≈0.4526`；Lasso `R²≈0.4719`，非零系数 7 个。
9. 参考 03 节：KMeans `inertia≈212.006, silhouette≈0.682`；Iris PCA 累计解释方差 `[0.9246, 0.9777]`。
10. 参考 05/02 节：不缩放 `SVC` 5 折均值约 0.91，缩放后约 0.97；说明“距离类模型先缩放”。
11. 参考 quiz 题 25：最佳参数通常 `{'max_depth': None, 'n_estimators': 50}`，最佳分约 0.9667。
12. 参考 04 节：LR 5 折约 0.9832、KMeans ARI≈0.8975、PCA 累计方差 `[0.362, 0.5541]`。
