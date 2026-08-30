# 第 5 章 参考资料（Matplotlib / Seaborn）

> 本页是第 5 章的**精选参考**：官方文档为第一优先级；教程与习题用于加深理解。链接在编写时已联网核实，仍建议以官方最新版为准。

## 一、官方文档（必读，授课依据）

| 资料 | 链接 | 说明 | 优先级 |
| ---- | ---- | ---- | ---- |
| Matplotlib 快速开始 | [链接](https://matplotlib.org/stable/tutorials/introductory/quick_start.html) | 官方绝对入门，覆盖 Plot/Axes/Figure | ★必读 |
| Pyplot 教程 | [链接](https://matplotlib.org/stable/tutorials/pyplot.html) | 函数式接口与状态机说明 | ★必读 |
| 面向对象接口 | [链接](https://matplotlib.org/stable/tutorials/introductory/usage.html#the-object-oriented-interface) | Figure/Axes 对象模型权威定义 | ★必读 |
| Matplotlib 图型画廊 | [链接](https://matplotlib.org/stable/gallery/index.html) | 各类图型官方示例 | ★必读 |
| Matplotlib 文本/字体 | [链接](https://matplotlib.org/stable/users/explain/text/text_props.html) | 字体、字号、数学公式 | 选读 |
| Matplotlib Cheatsheets | [链接](https://matplotlib.org/stable/cheatsheets/index.html) | 速查表（含多子图排版） | ★推荐 |
| Seaborn 官方教程 | [链接](https://seaborn.pydata.org/tutorial.html) | 分布/箱线/热力图/分面教程 | ★必读 |
| Seaborn API | [链接](https://seaborn.pydata.org/api.html) | 函数索引 | ★必读 |

## 二、精品教程（讲得更透 / 有图示）

| 资料 | 链接 | 说明 | 优先级 |
| ---- | ---- | ---- | ---- |
| Python Data Science Handbook（Jake VanderPlas） | [链接](https://github.com/jakevdp/PythonDataScienceHandbook) | 第 4 章 Matplotlib、第 5 章 Seaborn，Notebook 形式 | ★推荐 |
| SciPy Lecture Notes | [链接](https://scipy-lectures.org/packages/10_advanced_2d_plotting.html) | Matplotlib 进阶绘图讲义 | ★推荐 |
| Matplotlib: Anatomy of a Figure | [链接](https://matplotlib.org/stable/tutorials/intermediate/tight_layout_guide.html) | 子图排版与 tight_layout 细节 | ★推荐 |
| Datawhale fantastic-matplotlib | [链接](https://github.com/datawhalechina/fantastic-matplotlib) | 中文、渐进式 Matplotlib 教程 | 中文补充 |
| Datawhale wow-plotly | [链接](https://github.com/datawhalechina/wow-plotly) | Plotly 交互式教程（对比阅读） | 选读 |

## 三、习题与实战（课堂/作业/上机素材）

| 资料 | 链接 | 说明 | 优先级 |
| ---- | ---- | ---- | ---- |
| 本章练习（本仓库 exercises/） | [./exercises/README.md](./exercises/README.md) | 14 题 quiz（自动评分）+ 作业 + 参考答案 | ★必做 |
| 本章上机（本仓库 lab/） | [./lab/README.md](./lab/README.md) | 逐点演练 + 综合任务 | ★必做 |
| Matplotlib Gallery 官方示例 | [链接](https://matplotlib.org/stable/gallery/index.html) | 每个图型含完整可运行源码 | ★推荐 |
| Seaborn 示例 | [链接](https://seaborn.pydata.org/examples/index.html) | 多分组/分面/热力图示例 | ★推荐 |
| Python数据可视化（知乎/博客） | [链接](https://www.zhihu.com/question/582168949) | 中文快速入门与经验 | 中文补充 |

## 四、中文补充

| 资料 | 链接 | 说明 |
| ---- | ---- | ---- |
| matplotlib-cn（中文文档） | [链接](https://github.com/tomdonald/matplotlib-cn) | Matplotlib 中文文档镜像 |
| Datawhale fantastic-matplotlib | [链接](https://github.com/datawhalechina/fantastic-matplotlib) | 中文精品教程，适合入门 |
| 聪明办法学 Python（前置） | [链接](https://github.com/datawhalechina/learn-python-the-smart-way-v2) | 前置 Python 课程 |
| 本项目（科学计算） | [链接](https://github.com/datawhalechina/scientific-computing) | 本书开源仓库 |

## 五、资源使用建议

1. **教学**：以官方文档为主线（一章一个知识点），讲完代码后给学生 1–2 道本仓库 quiz 对应题。
2. **上机**：先跑 `lab/` 再做 `exercises/`；有能力的做 04 综合案例拓展。
3. **查错**：不确定的行为以官方文档为准；中文显示问题参考第 2 节 `rcParams` 设置，不要照抄非官方博客。

> 本清单整理时间：2026 年（随课程迭代可更新）。
