# 第 7 章 参考资料（Statsmodels）

> 本页是第 7 章的**精选参考**：官方文档为第一优先级；教程与习题用于加深理解。链接在编写时已联网核实，仍建议以官方最新版为准。

## 一、官方文档（必读，授课依据）

| 资料 | 链接 | 说明 | 优先级 |
| ---- | ---- | ---- | ---- |
| Statsmodels 主页 | https://www.statsmodels.org/stable/index.html | 库简介与总入口 | ★必读 |
| User Guide | https://www.statsmodels.org/stable/user-guide.html | 全书式教学指南 | ★必读 |
| API Reference | https://www.statsmodels.org/stable/api.html | 全部函数索引 | ★必读 |
| Regressions | https://www.statsmodels.org/stable/regression.html | 线性回归/GLS/WLS 总览 | ★必读 |
| Formula API | https://www.statsmodels.org/stable/formula.html | <code>ols('y ~ x', data=...)</code> 语法 | ★必读 |
| OLS | https://www.statsmodels.org/stable/generated/statsmodels.regression.linear_model.OLS.html | 最小二乘回归 | ★必读 |
| anova_lm | https://www.statsmodels.org/stable/generated/statsmodels.stats.anova.anova_lm.html | 方差分析 | ★必读 |
| GLM | https://www.statsmodels.org/stable/generated/statsmodels.genmod.generalized_linear_model.GLM.html | 广义线性模型 | ★必读 |
| WLS | https://www.statsmodels.org/stable/generated/statsmodels.regression.linear_model.WLS.html | 加权最小二乘 | 选读 |
| TSA（时间序列） | https://www.statsmodels.org/stable/tsa.html | 时间序列模块总览 | ★必读 |
| seasonal_decompose | https://www.statsmodels.org/stable/generated/statsmodels.tsa.seasonal.seasonal_decompose.html | 时间序列分解 | ★必读 |
| adfuller | https://www.statsmodels.org/stable/generated/statsmodels.tsa.stattools.adfuller.html | ADF 单位根检验 | ★必读 |
| ARIMA | https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMA.html | ARIMA/SARIMAX 模型 | ★必读 |
| Examples 总目录 | https://www.statsmodels.org/stable/examples/index.html | 官方示例（含回归与时间序列） | ★推荐 |

## 二、精品教程（讲得更透 / 有图示）

| 资料 | 链接 | 说明 | 优先级 |
| ---- | ---- | ---- | ---- |
| Python Data Science Handbook | https://jakevdp.github.io/PythonDataScienceHandbook/ | Jake VanderPlas 的《线性回归》一章对比 sklearn/statsmodels | ★推荐 |
| Lectures on Scientific Computing | https://github.com/jrjohansson/scientific-python-lectures | Lecture 4 讲 statsmodels 回归 | ★推荐 |
| Statsmodels 官方示例 Notebooks | https://www.statsmodels.org/stable/examples/index.html | 直接可跑的 notebook，含回归/诊断/时间序列 | ★推荐 |
| Statsmodels in Python (教育向) | https://www.statsmodels.org/stable/user-guide.html | 官方逐步教学 | ★必读 |
| 时间序列 STL 示例 | https://www.statsmodels.org/devel/examples/notebooks/generated/stl_decomposition.html | LOESS 季节性-趋势分解 | 选读 |

## 三、习题与实战（课堂/作业/上机素材）

| 资料 | 链接 | 说明 | 优先级 |
| ---- | ---- | ---- | ---- |
| 本章作业（本仓库） | [./exercises/README.md](./exercises/README.md) | 10 道自测题 + 答案 + 作业 | ★必做 |
| 本章上机（本仓库） | [./lab/README.md](./lab/README.md) | 环境自检→逐点演练→综合任务 | ★必做 |
| Statsmodels 官方示例（回归） | https://www.statsmodels.org/stable/examples/index.html#regression | 一整套可运行回归案例 | ★推荐 |
| Statsmodels 官方示例（时间序列） | https://www.statsmodels.org/stable/examples/index.html#time-series | 分解、ARIMA/SARIMA 案例 | ★推荐 |
| Python for Data Analysis（Wes McKinney） | https://github.com/wesm/pydata-book | 14 章包含 statsmodels 回归示例 | 选读 |

## 四、中文补充

| 资料 | 链接 | 说明 | 优先级 |
| ---- | ---- | ---- | ---- |
| Statsmodels 中文文档（ApacheCN 翻译） | https://github.com/ljtlrh/statsmodels_doc_zh | 官方文档的中文翻译 | ★推荐 |
| 本文项目（Datawhale 科学计算） | https://github.com/datawhalechina/scientific-computing | 本书开源仓库，含本章代码 | ★推荐 |
| Datawhale 时间序列相关笔记 | https://blog.csdn.net/weixin_45306755/article/details/108122794 | 时间序列特征与规则入门 | 选读 |
| 聪明办法学 Python v2 | https://github.com/datawhalechina/learn-python-the-smart-way-v2 | 前置 Python 课程（第 0 章先修） | 选读 |

## 五、资源使用建议

1. **教学**：以官方文档为主线（一节一个知识点），讲完代码后让学生跑 1–2 个官方示例；
2. **上机**：先跑 <code>lab/</code> 再做 <code>exercises/</code>；有能力的做 <code>03-综合案例.md</code> 拓展；
3. **查错**：不确定的行为以官方文档为准；不要照抄非官方博客中的“技巧”而不验证。

> 本清单整理时间：2026 年（随课程迭代可更新）。欢迎在 <code>references.md</code> 中继续补充社区文章。
