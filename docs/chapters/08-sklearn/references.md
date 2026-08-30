# 第 8 章 参考资料（scikit-learn）

> 本页是第 8 章的**精选参考**：官方文档为第一优先级；教程与习题用于加深理解。链接在编写时已联网核实，仍建议以官方最新版为准。

## 一、官方文档（必读，授课依据）

| 资料 | 链接 | 说明 | 优先级 |
| ---- | ---- | ---- | ---- |
| scikit-learn 官方主页 / 稳定版文档 | [链接](https://scikit-learn.org/stable/) | 权威 API 与用户指南入口，建议作为查错第一站 | ★必读 |
| scikit-learn 用户指南 | [链接](https://scikit-learn.org/stable/user_guide.html) | 按主题讲解预处理、监督、无监督、模型选择 | ★必读 |
| scikit-learn 入门教程 | [链接](https://scikit-learn.org/stable/tutorial/index.html) | 官方快速上手，含“选择正确评估器”参考 | ★必读 |
| scikit-learn 预处理 | [链接](https://scikit-learn.org/stable/modules/preprocessing.html) | 编码、缩放、缺失值处理 | ★必读 |
| scikit-learn 交叉验证 | [链接](https://scikit-learn.org/stable/modules/cross_validation.html) | train/test、交叉验证、调参 | ★必读 |
| scikit-learn 特征选择 | [链接](https://scikit-learn.org/stable/modules/feature_selection.html) | 过滤/包装/嵌入三类方法 | ★必读 |
| scikit-learn 模型评估 | [链接](https://scikit-learn.org/stable/modules/model_evaluation.html) | 分类/回归/聚类指标 | ★必读 |
| scikit-learn API 速查 | [链接](https://scikit-learn.org/stable/modules/classes.html) | 全部类/函数索引 | 选读 |

## 二、精品教程（讲得更透 / 有图示）

| 资料 | 链接 | 说明 | 优先级 |
| ---- | ---- | ---- | ---- |
| scikit-learn MOOC（INRIA） | [链接](https://inria.github.io/scikit-learn-mooc/) | 官方协作的免费课程，带习题与 Notebook | ★推荐 |
| Hands-On ML 3rd（Aurélien Géron） | [链接](https://github.com/ageron/handson-ml3) | 第 2 章起系统讲 sklearn，示例丰富 | ★推荐 |
| Python Data Science Handbook（Jake VanderPlas） | [链接](https://github.com/jakevdp/PythonDataScienceHandbook) | 第 5 章“Machine Learning”可整章对照 | ★推荐 |
| scikit-learn 官方示例库 | [链接](https://scikit-learn.org/stable/auto_examples/index.html) | 大量可运行示例，按算法/任务索引 | ★推荐 |
| 李宏毅机器学习（Datawhale 整理） | [链接](https://github.com/datawhalechina/leedl-tutorial) | 中文讲义，串起 ML 与 DL 的“为什么” | 选读 |

## 三、习题与实战（课堂/作业/上机素材）

| 资料 | 链接 | 说明 | 优先级 |
| ---- | ---- | ---- | ---- |
| 本章自测 quiz（本仓库） | [./exercises/quiz.ipynb](./exercises/quiz.ipynb) | 10 道 sklearn 题，含 TODO 与提示 | ★必做 |
| 本章作业 assignment.md（本仓库） | [./exercises/assignment.md](./exercises/assignment.md) | 12 道综合练习 | ★必做 |
| 本章上机 lab.ipynb（本仓库） | [./lab/README.md](./lab/README.md) | 端到端上机实验（Part 1–4） | ★必做 |
| Hands-On ML 练习 | [链接](https://github.com/ageron/handson-ml3) | 每章自带练习（含答案） | ★推荐 |
| scikit-learn MOOC 习题 | [链接](https://inria.github.io/scikit-learn-mooc/) | 在线交互 Quiz + Notebook | ★推荐 |
| Kaggle Intro to ML | [链接](https://www.kaggle.com/learn/intro-to-machine-learning) | 用真实数据练决策树/随机森林/交叉验证 | 选读 |

## 四、中文补充

| 资料 | 链接 | 说明 | 优先级 |
| ---- | ---- | ---- | ---- |
| sklearn 中文文档（社区译本） | [链接](https://github.com/casperdoudou/sklearn-doc-zh) | 中文版用户指南/API 参考，适合初读 | ★推荐 |
| 南瓜书（《机器学习》公式推导） | [链接](https://github.com/datawhalechina/pumpkin-book) | 与周志华《机器学习》配套的公式推导详解 | ★推荐 |
| 李宏毅机器学习（Datawhale） | [链接](https://github.com/datawhalechina/leedl-tutorial) | 中文讲义，机器学习到深度学习衔接 | ★推荐 |
| Datawhale 聪明办法学 Python v2 | [链接](https://github.com/datawhalechina/learn-python-the-smart-way-v2) | 前置 Python 复习 | 选读 |
| 本项目（《Python 科学计算》） | [链接](https://github.com/datawhalechina/scientific-computing) | 本书开源仓库 | 选读 |

## 五、资源使用建议

1. **教学**：以官方用户指南为主线（一节一个知识点），讲完代码后给学生 1–2 道官方示例或 MOOC 对应练习。
2. **上机**：先跑 `lab/` 再做 `exercises/`；有能力的做 04 综合案例拓展。
3. **查错**：不确定的行为以官方文档为准；不要照抄非官方博客中的“技巧”而不验证。

> 本清单整理时间：2026 年（随课程迭代可更新）。欢迎在 `references.md` 中继续补充社区文章。
