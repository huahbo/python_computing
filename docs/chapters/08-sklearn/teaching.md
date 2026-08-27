# 第 8 章 教学说明（教师用）

> 面向授课教师：课时建议、重点难点、上机安排、考核建议。学生无需阅读本页。

## 1. 教学目标

- 让学生**会查 sklearn 官方文档**并独立完成“预处理 → 建模 → 评估”闭环；
- 建立“fit/predict/transform/score 统一接口 + Pipeline 防泄漏”的心智模型；
- 能区分分类/回归/聚类/降维，并会选合适模型与指标；
- 能读懂特征重要性、混淆矩阵、ROC-AUC、R²、轮廓系数、ARI 等结果。

## 2. 建议课时与安排

| 课次 | 内容 | 建议形式 | 依赖 |
| ---- | ---- | ---- | ---- |
| 第 1 次 | 01 数据预处理（编码/缩放/切分/交叉验证） | 讲授 + 课堂演示 | 第 1–6 章 |
| 第 2 次 | 01 特征选择 + 02 分类（Iris/乳腺癌） | 讲授 + 上机 | 第 1 次 |
| 第 3 次 | 02 回归（Diabetes）+ 评估指标 | 讲授 + 上机 | 第 2 次 |
| 第 4 次 | 03 无监督（KMeans/DBSCAN/PCA/LDA） | 讲授 + 上机 | 第 2 次 |
| 第 5 次 | 04 综合案例（Wine 端到端） | 上机为主 + 讨论 | 第 3、4 次 |
| 课后 | 05 误区技巧自读；quiz + assignment + lab | 自主学习 | — |

> 若课时紧张：第 4 次可合并到第 5 次，重点讲 PCA/KMeans；习题改为选做。

## 3. 重点与难点

### 重点
- `fit` / `transform` / `fit_transform` 的区别与 `Pipeline` 用法；
- `StandardScaler` 与 `MinMaxScaler`；为什么距离类算法要缩放；
- `train_test_split` + `cross_val_score` + `GridSearchCV`；
- 分类指标（accuracy / confusion / precision / recall / F1 / AUC）与回归指标（MSE / MAE / R²）；
- PCA（无监督）与 LDA（有监督）的差异。

### 难点（学生常卡）
- **数据泄漏**：缩放器在测试集上 `fit`，或网格搜索里复用测试集；用 Pipeline 演示最直观。
- **独热编码 vs 标签编码**：用“颜色/有无顺序”的例子讲清。
- **KMeans vs DBSCAN**：在 `make_moons` 上对比，说明“凸形簇假设”与“密度簇”。
- **PCA 主成分解释**：`explained_variance_ratio_` 与累计解释方差；让学生读“降维丢多少信息”。
- **过拟合/泛化**：用 04 案例的一次 test 精度 vs 5 折均值对比来讲。

## 4. 上机（lab/）使用建议

- 每部分 10–15 分钟；要求每格代码都运行并记录输出；
- Part 4 综合任务可小组完成，最终提交 `wine_lab_pca.png`；
- 教师可在 lab 基础上增加“隐藏检查点”（如要求输出 `silhouette_score>0.3` 或 `ARI>0.85`）。

## 5. 作业与考核建议

- **平时**：exercises 10 题 quiz（自动评分）+ assignment.md 12 题；
- **上机**：lab.ipynb 完成情况 + 04 综合案例拓展；
- **期中/期末融合**：把 sklearn 知识点并入期末大作业（如“给定数据，完成预处理 → 分类/回归 → 评估 → 可视化”）。

## 6. 易错点清单（直接用于出题）

1. `scaler.fit_transform(X_test)` 泄漏；
2. `r2_score(y_pred, y_test)` 参数反；
3. 分类用 R²；`predict_proba` 与 `predict` 混淆；
4. `load_boston` 已移除；
5. `OneHotEncoder(sparse=False)` 过时参数；
6. `RFE(estimator, 5)` 位置参数报错；
7. KMeans / DBSCAN 参数（`random_state`、`eps`、`min_samples`）；
8. 把 PCA 当“只用 X 的 LDA”，忽略 LDA 需要 y。

## 7. 资源包

- 讲义正文：`01-数据集的预处理.md` ~ `05-常见误区与技巧.md`
- 配图：`images/*.png`（由 `../../build/make_chap8_figures.py` 生成）
- 练习：`exercises/`；上机：`lab/`；参考：`references.md`
- 合订 PDF：`../../教材PDF/08-Sklearn及其基本使用.pdf`（由 `../../build/pdf_build.py` 生成）

---

## 课表定位（8 周制）

- 周次：第 8 周
- 上课：2 学时（精讲 + 演示）
- 上机：4 学时（单独排课，以 lab/ 为主，含 0.5h 回顾与 0.5h 总结/quiz）
- 课后：完成 exercises/ 的 quiz 与 assignment；06 常见误区页自学
