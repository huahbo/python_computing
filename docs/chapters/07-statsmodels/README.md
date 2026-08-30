# 7. Statsmodels 及其基本使用（新版讲义）

> 本页是第 7 章的**章首页（索引）**。正文位于 <code>01-方差分析与回归.md</code> ~ <code>04-常见误区与技巧.md</code>，与原版资料分离（原版见 <code>../../原始资料/chap7/</code>）。

## 本章概览

Statsmodels 是 Python 中一个面向**统计建模与计量经济学**的库：它在 Pandas/NumPy 之上提供了回归、方差分析、广义线性模型、时间序列分解与 ARIMA 预测等经典统计工具，并给出完整、规范的**统计推断结果**（系数标准误、t 值、P 值、R²、F 检验、假设检验统计量等）。与主要面向**预测/机器学习**的 scikit-learn 不同，Statsmodels 更强调**模型的可解释性、诊断与显著性检验**，非常适合教学、论文与业务归因分析。

本章内容：

- 用 <code>OLS</code> / <code>ols</code> 做**线性回归**，并把公式 API 与数组 API 对比；
- 用 <code>anova_lm</code> 做**单因素方差分析**，理解它与回归的统一框架；
- 用 <code>GLM</code> 做**广义线性模型**（以二分类 Logit 为例）；
- 用 <code>seasonal_decompose</code> 做**时间序列分解**；
- 用 <code>adfuller</code> 做**平稳性检验**；
- 用 <code>ARIMA</code> 做**时间序列预测**。

## 学习目标

学完本章，你应该能够：

1. 用 <code>statsmodels.api.OLS</code> 完成一元/多元最小二乘回归，读懂 <code>summary()</code> 中的系数、标准误、t 值、P 值、R²、F 检验。
2. 使用公式 API <code>ols('y ~ x1 + x2', data=df)</code> 进行回归，并理解 <code>C(...)</code>、<code>I(...)</code> 等公式写法。
3. 用 <code>anova_lm</code> 做单因素方差分析，解读 F 统计量与 P 值，说明 ANOVA 与回归的统一性。
4. 用 <code>GLM</code> + <code>Binomial/Logit</code> 拟合二分类数据，并用 <code>predict</code> 得到概率。
5. 用 <code>seasonal_decompose</code> 分解时间序列为趋势、季节、残差；用 <code>adfuller</code> 判断平稳性。
6. 用 <code>ARIMA</code> 拟合并预测未来值，能读懂 <code>SARIMAX Results</code> 摘要。

## 先修要求与运行环境

- 熟悉 Python 基础语法、NumPy 数组与 Pandas DataFrame（前几章内容）。
- 安装 Statsmodels（与安装 NumPy/Pandas 一起）：

~~~bash
pip install statsmodels
# 国内镜像（更快）
pip install statsmodels -i https://pypi.tuna.tsinghua.edu.cn/simple
~~~

- 本章还需要 matplotlib（绘图）与 scipy（统计），若未安装请一并安装：

~~~bash
pip install matplotlib scipy
~~~

- 推荐在 JupyterLab / VS Code 中打开 <code>.ipynb</code> 练习；命令行列出的脚本保存为 <code>.py</code> 运行即可。

> 本仓库已在 <code>statsmodels 0.14.6</code>、NumPy 2.1.2、Pandas 2.2.3 环境下验证全部示例。

## 本章目录

| 小节 | 文件 | 内容 |
| ---- | ---- | ---- |
| 01 方差分析与回归 | [01-方差分析与回归.md](./01-方差分析与回归.md) | OLS 回归、公式 API、anova_lm、GLM、诊断、WLS |
| 02 时间序列预测 | [02-时间序列预测.md](./02-时间序列预测.md) | seasonal_decompose、ADF、ARIMA |
| 03 综合案例 | [03-综合案例.md](./03-综合案例.md) | 城市日负荷：方差分析 + 回归 + 时间序列预测 |
| 04 常见误区与技巧 | [04-常见误区与技巧.md](./04-常见误区与技巧.md) | 易错点表格、性能/调试/自测清单 |

## 数学预备与附录

本章的统计背景已集中到附录《数学与算法补充》：

- **C 概率统计基础**：C.3 统计推断（检验/置信区间）、C.4 回归与方差分析、C.5 时间序列；
- [打开附录 C](./../../附录/数学算法附录/C-概率统计基础.md) ｜ [附录索引](./../../附录/数学算法附录/README.md)

> 讲回归/ANOVA/时序前，用 C.4/C.5 讲 5 分钟“模型假设”；期末大作业前回看。

## 练习与上机入口

- [本章练习（exercises/）](./exercises/README.md)：10 道自测题、作业、参考答案。
- [本章上机（lab/）](./lab/README.md)：10 个代码单元、4 个大 Part，含综合任务。
- [本章参考与延伸阅读（references.md）](./references.md)：官方文档、精品教程、习题集、中文资料。
- [教学说明（teaching.md）](./teaching.md)：课时安排、重点难点、考核建议（教师用）。

## 建议课时

| 环节 | 学时 | 对应内容 |
| ---- | ---- | ---- |
| 讲课 | 3–4 学时 | 01–02 正文 + 03 案例讲解 |
| 上机 | 2–3 学时 | lab/ 逐题完成；课后完成 exercises/ 作业 |

## 使用说明

- **学生**：先读 01–02 正文并运行代码 → 完成 lab/ 上机 → 提交 exercises/ 作业 → 用 quiz 自测。统计概念/公式不清楚时，到 <code>references.md</code> 找官方对应章节。
- **教师**：按 <code>teaching.md</code> 的课时表讲；lab 可作为上机课内容；<code>quiz.ipynb</code> 可回收批改；<code>03-综合案例.md</code> 可作课堂讨论。
