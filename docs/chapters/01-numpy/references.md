# 第 1 章 参考资料（NumPy）

> 本页是第 1 章的**精选参考**：官方文档为第一优先级；教程与习题用于加深理解。链接在编写时已联网核实，仍建议以官方最新版为准。

## 一、官方文档（必读，授课依据）

| 资料 | 链接 | 说明 | 优先级 |
| ---- | ---- | ---- | ---- |
| NumPy：Absolute Beginner | [链接](https://numpy.org/doc/stable/user/absolute_beginners.html) | 官方“绝对入门”，覆盖创建/索引/广播 | ★必读 |
| NumPy Quickstart | [链接](https://numpy.org/doc/stable/user/quickstart.html) | 快速上手教程 | ★必读 |
| Broadcasting 官方说明 | [链接](https://numpy.org/doc/stable/user/basics.broadcasting.html) | 广播规则权威定义 | ★必读 |
| ndarray 基础 | [链接](https://numpy.org/doc/stable/user/basics.html) | 形状、索引、切片、视图/拷贝 | ★必读 |
| numpy.linalg 参考 | [链接](https://numpy.org/doc/stable/reference/routines.linalg.html) | 线性代数全部函数 | ★必读 |
| numpy.polynomial 参考 | [链接](https://numpy.org/doc/stable/reference/routines.polynomials.html) | 多项式接口 | 选读 |
| I/O 参考 | [链接](https://numpy.org/doc/stable/reference/routines.io.html) | save/loadtxt/savez | 选读 |
| 随机数（Generator） | [链接](https://numpy.org/doc/stable/reference/random/generator.html) | `default_rng` 用法 | ★必读 |
| NumPy for MATLAB users | [链接](https://numpy.org/doc/stable/user/numpy-for-matlab-users.html) | 给 MATLAB 背景学生迁移 | 选读 |

## 二、精品教程（讲得更透 / 有图示）

| 资料 | 链接 | 说明 | 优先级 |
| ---- | ---- | ---- | ---- |
| SciPy Lecture Notes – NumPy | [链接](https://scipy-lectures.org/intro/numpy/index.html) | 系统、带图，覆盖数组/广播/运算 | ★推荐 |
| Lectures on Scientific Computing (Robert Johansson) | [链接](https://github.com/jrjohansson/scientific-python-lectures) | Lecture-2-Numpy.ipynb，Notebook 形式 | ★推荐 |
| Python Data Science Handbook (Jake VanderPlas) | [链接](https://github.com/jakevdp/PythonDataScienceHandbook) | 第 2 章 NumPy，可整章对照 | ★推荐 |
| Python for Data Analysis 3rd (Wes McKinney) | 出版社/官方配套 | 偏数据方向，NumPy/Pandas 结合 | 选读 |
| NumPy 中文学习站 | [链接](https://numpy.net.cn/learn/) | 中文入门与文档镜像 | 中文补充 |

## 三、习题与实战（课堂/作业/上机素材）

| 资料 | 链接 | 说明 | 优先级 |
| ---- | ---- | ---- | ---- |
| 100 NumPy Exercises（rougier） | [链接](https://github.com/rougier/numpy-100) | 100 题带解答，适合课后 | ★推荐 |
| NumPy 习题（中文版，Data-Science-Notes） | [链接](https://github.com/fengdu78/Data-Science-Notes) | 含 numpy-100 中文整理 | 中文补充 |
| numpy_exercises by 4GeeksAcademy | [链接](https://github.com/4GeeksAcademy/numpy-100) | 在线运行版本（Binder 友好） | 选读 |
| 本章作业（本仓库 exercises/） | [./exercises/README.md](./exercises/README.md) | 20 题 + quiz 自动评分 | ★必做 |
| 本章上机（本仓库 lab/） | [./lab/README.md](./lab/README.md) | 逐点演练 + 综合任务 | ★必做 |

## 四、Datawhale 上下游

| 资料 | 链接 | 说明 |
| ---- | ---- | ---- |
| 聪明办法学 Python v2 | [链接](https://github.com/datawhalechina/learn-python-the-smart-way-v2) | 前置课程 |
| 数学建模导论 | [链接](https://github.com/datawhalechina/intro-mathmodel) | 后续课程 |
| 本项目（科学计算） | [链接](https://github.com/datawhalechina/scientific-computing) | 本书开源仓库 |

## 五、资源使用建议

1. **教学**：以官方文档为主线（一节一个知识点），讲完代码后给学生 1–2 道 numpy-100 对应题。
2. **上机**：先跑 `lab/` 再做 `exercises/`；有能力的做 05 综合案例拓展。
3. **查错**：不确定的行为以官方文档为准；不要照抄非官方博客中的“技巧”而不验证。

> 本清单整理时间：2026 年（随课程迭代可更新）。欢迎在 `references.md` 中继续补充社区文章。
