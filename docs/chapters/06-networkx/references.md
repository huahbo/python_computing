# 第 6 章 参考资料（NetworkX）

> 本页是第 6 章的**精选参考**：官方文档为第一优先级；教程与习题用于加深理解。链接在编写时已联网核实，仍建议以官方最新版为准。

## 一、官方文档（必读，授课依据）

| 资料 | 链接 | 说明 | 优先级 |
| ---- | ---- | ---- | ---- |
| NetworkX Tutorial（官方教程） | https://networkx.org/documentation/stable/tutorial.html | 从零创建图、访问节点边、常用操作 | ★必读 |
| 图类型（Graph / DiGraph 等） | https://networkx.org/documentation/stable/reference/classes/index.html | Graph / DiGraph / MultiGraph 接口 | ★必读 |
| 图生成器 | https://networkx.org/documentation/stable/reference/generators.html | path/cycle/complete/karate/随机图 | ★必读 |
| 算法总览 | https://networkx.org/documentation/stable/reference/algorithms/index.html | 全部算法模块入口 | ★必读 |
| 最短路径算法 | https://networkx.org/documentation/stable/reference/algorithms/shortest_paths.html | Dijkstra / Bellman-Ford / Floyd-Warshall | ★必读 |
| 最小生成树 | https://networkx.org/documentation/stable/reference/algorithms/tree.html | minimum_spanning_tree 等 | ★必读 |
| 中心性算法 | https://networkx.org/documentation/stable/reference/algorithms/centrality.html | 介数/接近/度中心性 | ★必读 |
| 连通性 | https://networkx.org/documentation/stable/reference/algorithms/connectivity.html | is_connected / 强连通 / 分量 | ★必读 |
| 社区检测与模块度 | https://networkx.org/documentation/stable/reference/algorithms/community.html | greedy_modularity / louvain / modularity | ★必读 |
| 绘图 API | https://networkx.org/documentation/stable/reference/drawing.html | draw / spring_layout / 自定义 | 选读 |
| 图与 NumPy/SciPy 互转 | https://networkx.org/documentation/stable/reference/convert.html | to_numpy_array / to_scipy_sparse_array | 选读 |

## 二、精品教程（讲得更透 / 有图示）

| 资料 | 链接 | 说明 | 优先级 |
| ---- | ---- | ---- | ---- |
| SciPy Lecture Notes（网络章节） | https://scipy-lectures.org/ | 科学计算整体，含图与网络 | ★推荐 |
| Complex Network Analysis in Python（官方示例） | https://networkx.org/documentation/stable/auto_examples/index.html | 官方示例集，覆盖绘图/社区/路径 | ★推荐 |
| Lectures on Scientific Computing (Robert Johansson) | https://github.com/jrjohansson/scientific-python-lectures | Notebook 形式，含 NetworkX | ★推荐 |
| Python Data Science Handbook | https://github.com/jakevdp/PythonDataScienceHandbook | 数据科学视角，可作延伸 | 选读 |
| NetworkX 3.x 迁移/新特性 | https://networkx.org/documentation/stable/release/release_3.3.html | 版本更新说明 | 选读 |

## 三、习题与实战（课堂/作业/上机素材）

| 资料 | 链接 | 说明 | 优先级 |
| ---- | ---- | ---- | ---- |
| 本章自测题（本仓库 exercises/） | [./exercises/README.md](./exercises/README.md) | 10 题 quiz + 答案 | ★必做 |
| 本章上机（本仓库 lab/） | [./lab/README.md](./lab/README.md) | 逐点演练 + 综合任务 | ★必做 |
| 官方示例：空手道俱乐部 | https://networkx.org/documentation/stable/auto_examples/graph/plot_karate_club.html | 经典社区网络可视化 | ★推荐 |
| NetworkX 社区（Discussions/Stack Overflow） | https://networkx.org/documentation/stable/faq.html | 常见问题与讨论入口 | 选读 |
| Grape-book（图深度学习） | https://datawhalechina.github.io/grape-book | 图神经网络进阶（延伸） | 选读 |

## 四、中文补充

| 资料 | 链接 | 说明 | 优先级 |
| ---- | ---- | ---- | ---- |
| NetworkX 中文文档镜像 | https://networkx.cn/documentation/stable/ | 中文版官方文档（有翻译） | ★推荐 |
| 华为云/CSDN NetworkX 教程 | https://blog.csdn.net/Rocky006/article/details/148866312 | 中文使用详解，含代码 | 选读 |
| 知乎：复杂网络建模（Python+NetworkX） | https://zhuanlan.zhihu.com/p/591617257 | 复杂网络建模课程代码（中文） | 选读 |
| Datawhale 图深度学习（葡萄书） | https://github.com/datawhalechina/grape-book | 中文开源书，进阶图神经网络 | 选读 |

## 五、资源使用建议

1. **教学**：以官方文档为主线（一节一个知识点），讲完代码后给学生 1–2 道选择题或编程题。
2. **上机**：先跑 lab/ 再做 exercises/；有能力的做 04 综合案例的拓展任务。
3. **查错**：不确定的行为以官方文档为准；不要照抄非官方博客中的“技巧”而不验证。

> 本清单整理时间：2026 年（随课程迭代可更新）。欢迎在 references.md 中继续补充社区文章。
