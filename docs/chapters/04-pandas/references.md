# 第 4 章 参考资料（Pandas）

> 本页是第 4 章的**精选参考**：官方文档为第一优先级；教程与习题用于加深理解。链接为编写时采用的稳定入口，仍建议以 pandas 最新版官网为准。

## 一、官方文档（必读，授课依据）

| 资料 | 链接 | 说明 | 优先级 |
| ---- | ---- | ---- | ---- |
| Pandas 官方主页 | https://pandas.pydata.org/ | 库主页、版本、安装 | ★必读 |
| Pandas 10 分钟入门 | https://pandas.pydata.org/docs/user_guide/10min.html | 一分钟建立 Series/DataFrame 心智 | ★必读 |
| Pandas 用户指南 | https://pandas.pydata.org/docs/user_guide/index.html | 索引/清洗/分组/时间序列全指南 | ★必读 |
| pandas.Series 参考 | https://pandas.pydata.org/docs/reference/api/pandas.Series.html | Series 全部方法 | ★必读 |
| pandas.DataFrame 参考 | https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html | DataFrame 全部方法 | ★必读 |
| 缺失值处理 | https://pandas.pydata.org/docs/user_guide/missing_data.html | isna/fillna/dropna/ffill/bfill | ★必读 |
| 分组（groupby） | https://pandas.pydata.org/docs/user_guide/groupby.html | 分组聚合/变换/过滤 | ★必读 |
| pivot_table 参考 | https://pandas.pydata.org/docs/reference/api/pandas.pivot_table.html | 透视表 | ★必读 |
| 时间序列指南 | https://pandas.pydata.org/docs/user_guide/timeseries.html | date_range/resample/rolling | ★必读 |
| 性能提升 | https://pandas.pydata.org/docs/user_guide/enhancingperf.html | 向量化、chunksize 等 | 选读 |

## 二、精品教程（讲得更透 / 有图示）

| 资料 | 链接 | 说明 | 优先级 |
| ---- | ---- | ---- | ---- |
| Python Data Science Handbook (Jake VanderPlas) | https://github.com/jakevdp/PythonDataScienceHandbook | 第 3 章 Pandas，体系清晰 | ★推荐 |
| Python for Data Analysis 3rd (Wes McKinney) | https://github.com/wesm/pydata-book | Pandas 作者亲著，第三版配套代码 | ★推荐 |
| Lectures on Scientific Computing (Robert Johansson) | https://github.com/jrjohansson/scientific-python-lectures | Lecture-3-Pandas，Notebook 风格 | ★推荐 |
| SciPy Lecture Notes（Pandas 章节） | https://scipy-lectures.org/ | 偏科学计算，含数据整理 | 选读 |
| Pandas Cheat Sheet（官方） | https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf | 一页速查 | ★推荐 |

## 三、习题与实战（课堂/作业/上机素材）

| 资料 | 链接 | 说明 | 优先级 |
| ---- | ---- | ---- | ---- |
| 100 Pandas Puzzles | https://github.com/ajcr/100-pandas-puzzles | 100 道 Pandas 小题带答案 | ★推荐 |
| Pandas Exercises (guipsamora) | https://github.com/guipsamora/pandas_exercises | 分主题练习（清洗/分组/时间序列） | ★推荐 |
| 本章作业（本仓库 exercises/） | [./exercises/README.md](./exercises/README.md) | 15 题作业 + 25 题 quiz + 答案 | ★必做 |
| 本章上机（本仓库 lab/） | [./lab/README.md](./lab/README.md) | 逐点演练 + 综合任务 | ★必做 |

## 四、中文补充

| 资料 | 链接 | 说明 |
| ---- | ---- | ---- |
| Pandas 中文入门（pandas.pydata.org 官方中文翻译入口） | https://pandas.pydata.org/docs/ | 官方文档，含中文化镜像 |
| numpy.net.cn（中文学习站） | https://numpy.net.cn/ | 中文科学计算入门（含 Pandas 相关） |
| Datawhale 聪明办法学 Python v2 | https://github.com/datawhalechina/learn-python-the-smart-way-v2 | 前置 Python 课程 |
| Datawhale 数学建模导论 | https://github.com/datawhalechina/intro-mathmodel | 后续课程（Pandas 实战） |
| 本项目（科学计算） | https://github.com/datawhalechina/scientific-computing | 本书开源仓库 |

## 五、资源使用建议

1. **教学**：以官方文档为主线，一节一个知识点；讲完代码给学生 1–2 道 pandas_exercises 对应题。
2. **上机**：先跑 lab/ 再做 exercises/；有能力的做 03 综合案例拓展。
3. **查错**：不确定的行为以官方文档为准；不要照抄非官方博客中的“技巧”而不验证。

> 本清单整理时间：2026 年（随课程迭代可更新）。欢迎在 references.md 中继续补充社区文章。