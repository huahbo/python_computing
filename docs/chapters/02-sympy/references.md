# 第 2 章 参考资料（SymPy）

> 本页是第 2 章的**精选参考**：官方文档为第一优先级；教程与习题用于加深理解。链接在编写时已联网核实，仍建议以官方最新版为准。

## 一、官方文档（必读，授课依据）

| 资料 | 链接 | 说明 | 优先级 |
| ---- | ---- | ---- | ---- |
| SymPy Tutorials（总目录） | https://docs.sympy.org/latest/tutorials/index.html | 官方入门教程入口，含基础与进阶 | ★必读 |
| SymPy Calculus（求导/积分/极限） | https://docs.sympy.org/latest/tutorials/intro-tutorial/calculus.html | 极限、diff、integrate 的权威说明 | ★必读 |
| SymPy Solvers | https://docs.sympy.org/latest/modules/solvers/index.html | solve/solveset/linsolve/nonlinsolve 参考 | ★必读 |
| SymPy Matrices | https://docs.sympy.org/latest/modules/matrices/index.html | 符号矩阵、特征值、分解 | ★必读 |
| SymPy lambdify | https://docs.sympy.org/latest/modules/utilities/lambdify.html | 符号→数值函数的关键工具 | ★必读 |
| SymPy ODE (dsolve) | https://docs.sympy.org/latest/modules/solvers/ode.html | 微分方程符号求解 | ★必读 |
| SymPy Gotchas（常见坑） | https://docs.sympy.org/latest/tutorial/gotchas.html | 官方 FAQ，避开符号计算陷阱 | 选读 |

## 二、精品教程（讲得更透 / 有图示）

| 资料 | 链接 | 说明 | 优先级 |
| ---- | ---- | ---- | ---- |
| SciPy Lectures – SymPy | https://scipy-lectures.org/packages/sympy.html | 系统、带例子，覆盖符号计算核心 | ★推荐 |
| Lectures on Scientific Computing (Robert Johansson) | https://github.com/jrjohansson/scientific-python-lectures | Lecture 含 SymPy 的 Notebook，可对照 | ★推荐 |
| SymPy 官方 1.13 文档 | https://docs.sympy.org/latest/index.html | 完整 API 参考 | ★必读 |
| Python Data Science Handbook（符号计算附录） | https://github.com/jakevdp/PythonDataScienceHandbook | 第 5 章 SymPy 简介，适合数据方向学生 | 选读 |

## 三、习题与实战（课堂/作业/上机素材）

| 资料 | 链接 | 说明 | 优先级 |
| ---- | ---- | ---- | ---- |
| NTNU：Exercises and solutions in symbolic mathematics (SymPy) | https://www.ntnu.no/wiki/spaces/imtsoftware/pages/148770976/Exercises+and+solutions+symbolic+mathematics+in+Python | 含 SymPy 符号计算练习题与答案 | ★推荐 |
| SymPy 官方 doc 中的 Examples | https://docs.sympy.org/latest/tutorials/intro-tutorial/ | 每条均可上机复现 | ★必做 |
| 本章作业（本仓库 exercises/） | [./exercises/README.md](./exercises/README.md) | 10+ 题，含 quiz 自动评分与答案 | ★必做 |
| 本章上机（本仓库 lab/） | [./lab/README.md](./lab/README.md) | 逐点演练 + 综合任务 | ★必做 |

## 四、中文补充

| 资料 | 链接 | 说明 |
| ---- | ---- | ---- |
| ZetCode 中文教程：SymPy | https://zetcode.cn/python/sympy/ | 中文入门，含符号运算示例 |
| 知乎专栏：SymPy 入门与实战 | https://zhuanlan.zhihu.com/p/111573239 | 中文文章，带代码与截图 |
| 腾讯云开发者社区：Python 科学计算之 SymPy | https://cloud.tencent.cn/developer/article/2510103 | 中文案例集合 |
| 聪明办法学 Python v2 | https://github.com/datawhalechina/learn-python-the-smart-way-v2 | 前置 Python 课程 |
| 本项目（科学计算） | https://github.com/datawhalechina/scientific-computing | 本书开源仓库 |

## 五、资源使用建议

1. **教学**：以官方文档为主线（一节一个知识点），讲完代码后给学生 1–2 道练习，让其用 SymPy 得到同样的精确结果；
2. **上机**：先跑 `lab/` 再做 `exercises/`；有能力的做 03 综合案例拓展；
3. **查错**：不确定的行为以官方文档为准；不要照抄非官方博客中的“技巧”而不验证（例如 `lambdify` 返回值的类型）。

> 本清单整理时间：2026 年（随课程迭代可更新）。欢迎在 `references.md` 中继续补充社区文章。