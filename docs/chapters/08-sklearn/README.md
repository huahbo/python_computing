# 8. scikit-learn 及其基本使用（新版讲义）

> 本页是第 8 章的**章首页（索引）**。正文位于 `01-数据集的预处理.md` ~ `05-常见误区与技巧.md`，与原版资料完全分离（原版见 `../../原始资料/chap8/`）。

## 本章概览

scikit-learn（简称 sklearn）是 Python 最常用的机器学习库：它把“数据预处理 → 模型训练 → 模型评估 → 模型调参 → 可视化”这一整套流程统一成一套简洁、一致的接口（`fit` / `predict` / `score` / `transform`）。本章以经典数据集（Iris 鸢尾花、Wine 红酒、Diabetes 糖尿病、乳腺癌等）为例，带你从**特征编码、缩放、切分、交叉验证、特征选择**讲起，再分别讲解**有监督学习**（分类、回归）与**无监督学习**（KMeans/DBSCAN 聚类、PCA/LDA 降维），最后用一个 Wine 端到端案例把全部知识串起来。

> sklearn 聚焦“经典机器学习”，接口统一、算法丰富、与 NumPy/Pandas/Matplotlib 无缝配合，是《Python 科学计算》课程最后一块重要拼图。

## 学习目标

学完本章，你应该能够：

1. 说清**有监督学习**（分类、回归）与**无监督学习**（聚类、降维）的区别，并能在 sklearn 中选对模型。
2. 用 `OneHotEncoder` / `LabelEncoder` 做特征编码，用 `StandardScaler` / `MinMaxScaler` 做特征缩放，理解“为什么距离类算法要缩放”。
3. 用 `train_test_split` 切分数据，并用 `cross_val_score` / `LeaveOneOut` 评估模型泛化能力，避免数据泄漏。
4. 用 `VarianceThreshold`、`SelectKBest`、`RFE`、`SelectFromModel`、`Lasso` 做特征筛选。
5. 完成一个分类任务（Iris/乳腺癌）与一个回归任务（Diabetes），会用 `accuracy_score`、`classification_report`、`roc_auc_score`、`mean_squared_error`、`r2_score` 等指标评估。
6. 完成 KMeans 与 DBSCAN 聚类、PCA 与 LDA 降维，会用 `silhouette_score`、`adjusted_rand_score`、`explained_variance_ratio_` 评估结果。
7. 用 `Pipeline` + `ColumnTransformer` 把预处理与模型串成一条流水线，避免训练集/测试集信息泄漏。
8. 完成一个 Wine 端到端案例：预处理 → 分类 → 聚类 → 降维 → 可视化，并读懂其中的特征重要性。

## 先修要求与运行环境

- 熟悉 Python 基础语法；建议先学完本课程第 1–6 章（NumPy、SymPy、SciPy、Pandas、Matplotlib、NetworkX）。
- 了解基本的矩阵/向量代数与统计概念（均值、方差、相关系数等）即可，不要求先修研究生水平的机器学习课程。
- 安装与升级（建议 Python 3.10+）：

```bash
pip install --upgrade pip
pip install numpy pandas matplotlib scipy scikit-learn
# 第 7 章统计建模（可选）
pip install statsmodels -i https://pypi.tuna.tsinghua.edu.cn/simple
```

- 推荐在 JupyterLab / VS Code 中打开 `.ipynb` 练习；sklearn ≥ 1.3 即可运行本章代码（本仓库在 sklearn 1.6.1 下验证）。

## 本章目录

| 小节 | 文件 | 内容 |
| ---- | ---- | ---- |
| 01 数据集的预处理 | [01-数据集的预处理.md](./01-数据集的预处理.md) | 特征编码、特征缩放、数据集切分、交叉验证、特征选择与降维概览 |
| 02 有监督学习的案例 | [02-有监督学习的案例.md](./02-有监督学习的案例.md) | Iris 分类、乳腺癌二分类、Diabetes 回归、决策树可视化、评估指标 |
| 03 无监督学习的案例 | [03-无监督学习的案例.md](./03-无监督学习的案例.md) | KMeans / DBSCAN 聚类、PCA / LDA 降维、聚类与降维评估 |
| 04 综合案例 | [04-综合案例.md](./04-综合案例.md) | Wine 数据端到端：预处理→分类→聚类→降维→可视化（配图） |
| 05 常见误区与技巧 | [05-常见误区与技巧.md](./05-常见误区与技巧.md) | 易错点表格、性能/调试/自测清单 |

## 数学预备与附录

本章的机器学习背景已集中到附录《数学与算法补充》：

- **E 机器学习基础**：E.1 学习范式、E.2 损失与优化、E.3 评估与过拟合、E.4 常用模型直觉、E.5 sklearn 流程；
- **A 线性代数与矩阵**：A.3 SVD/PCA（降维）；
- [打开附录 E](./../../附录/数学算法附录/E-机器学习基础.md) ｜ [打开附录 A](./../../附录/数学算法附录/A-线性代数与矩阵.md) ｜ [附录索引](./../../附录/数学算法附录/README.md)

> 课堂先讲 E.1~E.3（约 15 分钟），再进各模型；PCA 课回看 A.3。

## 练习与上机入口

- [本章练习（exercises/）](./exercises/README.md)：10 道自测 quiz（自动评分）+ 一章作业 assignment.md + 参考答案 answers.ipynb。
- [本章上机（lab/）](./lab/README.md)：循序渐进的上机 notebook（Part 1–4），含综合任务与提交清单。
- [本章参考与延伸阅读（references.md）](./references.md)：官方文档、精品教程、习题实战、中文补充。
- [教学说明（teaching.md）](./teaching.md)：课时安排、重点难点、考核建议（教师用）。

## 建议课时

| 环节 | 学时 | 对应内容 |
| ---- | ---- | ---- |
| 讲课 | 4–5 学时 | 01–03 正文 + 04 综合案例讲解 |
| 上机 | 3–4 学时 | lab/ 逐题完成；课后完成 exercises/ 作业 |

## 使用说明

- **学生**：先读 01–03 正文并运行代码 → 完成 lab 上机 → 做 exercises 作业 → 自测 quiz 检验。生词/公式不懂时，到 references.md 找官方对应章节。
- **教师**：按 teaching.md 的课时表讲；lab 可作为上机课内容；exercises 中的 quiz 带自动评分，可直接回收。
