# 图论与网络

> 本附录为第 6 章 NetworkX 提供图论与算法背景：图表示、基本量、经典算法（BFS/最短路/MST/中心性/社区），并补上本科常见难点（握手定理、树的性质、模块度）。

---

## D.1 直觉故事：朋友圈里的"谁最重要"

"谁最重要"没有唯一答案：认识 10 个互相不认识的人 → 桥梁；认识 10 个彼此都认识的人 → 不是桥梁。所以：

- **度中心性**：连接数多 → "活跃"；
- **接近中心性**：到所有人平均距离短 → "信息传得快"；
- **介数中心性**：很多最短路经过它 → "枢纽/瓶颈"；
- **PageRank**：被"重要的人"指向 → "影响力"。

做网络分析第一步是**明确要问什么**，再选指标。

> **正文见**：[6 NetworkX · 02 分析图](../../chapters/06-networkx/02-分析图.md)、[6 NetworkX · 03 求解图的基本问题](../../chapters/06-networkx/03-求解图的基本问题.md)。

---

## D.2 图的基本表示（讲解 + 手算）

### D.2.1 怎么把图"喂给电脑"

| 表示 | 样子 | 适合 |
| ---- | ---- | ---- |
| 邻接矩阵 $A$ | $A[i][j]=1$（或权重） | 稠密图、矩阵运算；点多费内存 |
| 邻接表 | 每个点存邻居列表 | 稀疏大图；遍历快 |

手算例子（4 点：A-B、A-C、B-C、C-D）：

$$A=\begin{bmatrix}0&1&1&0\\1&0&1&0\\1&1&0&1\\0&0&1&0\end{bmatrix}$$

（无向图对称；`np.linalg.eigvalsh(A)` 能直接读图的性质，如连通性/谱聚类。）

### D.2.2 基本量：度、连通、树

- **度** $\deg(v)$：邻边数；有向图分**入度/出度**；
- **握手定理**：$\sum_v \deg(v)=2|E|$（每条边贡献 2 度）——检查数据是否"边数对着"；
- **路径/连通分量**：可达性；**树**：无环连通图，$n$ 个点恰 $n-1$ 条边；
- **二分图**：点分两类，边只在类间（学生-选课、用户-商品）。

### D.2.3 加权与有向

- **加权图**：边带距离/成本/强度；最短路、MST、网络流依赖这些权；
- **有向图**：边有方向（关注、引用、资金流）；PageRank/拓扑排序只在有向图上。

---

## D.3 经典算法：思路与手算

### D.3.1 遍历：BFS 与 DFS

- **BFS**：一层层扩散。无权图最短路靠它；手算：从 A 出发，A→B、C，再 C→D，路径 A→C→D 两步最短；
- **DFS**：一条路走到黑再回头；用于检测环、连通分量、拓扑排序。

### D.3.2 最短路径

| 算法 | 适用 | 思路 | 复杂度 |
| ---- | ---- | ---- | ---- |
| BFS | 无权 | 按层扩散 | $O(V+E)$ |
| Dijkstra | 非负权 | 每次取当前最近点并松弛 | $O((V+E)\log V)$（堆） |
| Bellman-Ford | 可能有负权 | 反复松弛 | $O(VE)$ |
| Floyd-Warshall | 全源 | 动态规划 | $O(V^3)$ |

手算 Dijkstra（A-B=2、A-C=5、B-C=1、C-D=4）：A=0 → B=2、C=5 → 取 B=2，松弛 C 得 3 → 取 C=3，松弛 D=7 → 得 A→B→C→D，距离 7。

### D.3.3 最小生成树（MST）

目标：总权重最小的连通子图（树）。**Kruskal**：边按权排序，用并查集"不成环就加"；最后正好 $n-1$ 条边。**Prim**：从一个点出发，每次加入"连接已选集合的最便宜边"。两者都满足"贪心 + 无环"的树性质。

### D.3.4 中心性与社区

- **介数中心性**：统计每条最短路经过某点的次数；
- **PageRank**：随机游走稳态；链接不仅"数量"还看"质量"；
- **社区发现**：把网络切成"内部紧密、外部稀疏"。**模块度**：

$$Q=\frac{1}{2m}\sum_{ij}\Big[A_{ij}-\frac{d_i d_j}{2m}\Big]\delta(c_i,c_j)$$

直觉：实际边数 - 随机网络下的期望边数（同一社区内）。**Louvain** 贪心优化模块度，快且常用；结果与分辨率/随机种子有关，**要报告方法与参数**。

---

## D.4 动手例题（选做）

**例：Dijkstra 代码验证**：

```python
import networkx as nx
G = nx.Graph()
G.add_weighted_edges_from([("A","B",2), ("A","C",5), ("B","C",1), ("C","D",4)])
print(nx.shortest_path(G, "A", "D", weight="weight"))          # ['A','B','C','D']
print(nx.shortest_path_length(G, "A", "D", weight="weight"))   # 7
```

**例：中心性完全不同**。星型网络（中心 A 连 5 个叶子）：A 的介数中心性远高于叶子；但每个叶子的度都是 1——"度中心性"看不出谁是枢纽。

---

## D.5 Python 对应（速查）

```python
import networkx as nx
G = nx.Graph()
G.add_edges_from([("A","B",{"w":2}), ("A","C",{"w":5}),
                  ("B","C",{"w":1}), ("C","D",{"w":4})])

nx.shortest_path(G, "A", "D", weight="w")      # Dijkstra
nx.shortest_path_length(G, "A", "D", weight="w")
nx.minimum_spanning_tree(G, weight="w")
nx.degree_centrality(G); nx.betweenness_centrality(G)
nx.pagerank(G)
nx.community.louvain_communities(G)
nx.draw(G, with_labels=True)
```

| 你想要 | 用哪个 |
| ---- | ---- |
| 最短路 | `nx.shortest_path`（加权传 `weight`） |
| MST | `nx.minimum_spanning_tree` |
| 中心性 | `degree / closeness / betweenness / pagerank` |
| 社区 | `nx.community` |
| 可视化 | `nx.draw`（或结合 Matplotlib） |

---

## D.6 常见误区

| 误区 | 正确 |
| ---- | ---- |
| 以为图只能是邻接矩阵 | 稀疏大图用 NetworkX 的邻接表实现 |
| 无向图当成有向图算 | `Graph` 与 `DiGraph` 分开 |
| 用最短路回答"谁最重要" | 先明确"重要"的定义 |
| 忽略权重 | 加权算法要传 `weight` |
| 社区数量随便定 | 社区发现与分辨率有关；试多组参数并看模块度 |
| 握手定理没验证 | 先看 `sum deg(v) == 2*|E|` 排查数据 |

---

## D.7 使用章节（双向）

| 章 | 哪里用到 | 链接 |
| ---- | ---- | ---- |
| 6 NetworkX | 建图/分析/最短路 | [01 创建图](../../chapters/06-networkx/01-创建图.md) |
| 6 NetworkX | 中心性/社区 | [02 分析图](../../chapters/06-networkx/02-分析图.md) |
| 6 NetworkX | 综合案例 | [04 综合案例](../../chapters/06-networkx/04-综合案例.md) |

**下游衔接**：intro-mathmodel 第 4 章（复杂网络与图论模型）。
**延伸阅读**：NetworkX 官方教程、图论教材、[references.md](./references.md)。

---

## D.10 常见考题与自查（考前 10 分钟）

| 会了吗？ | 考点 | 一句话答案 |
| ---- | ---- | ---- |
| □ | BFS 与 DFS 适用 | BFS 无权最短路；DFS 环/连通/拓扑 |
| □ | Dijkstra 前提 | 边权非负 |
| □ | MST 贪心 | Kruskal/Prim 每次选不形成环的最便宜边 |
| □ | 度 vs 介数中心性 | 度=活跃；介数=桥梁/瓶颈 |
| □ | 模块度 | 社区内实际边 - 随机期望，越大越"像社区" |
| □ | 握手定理 | 度之和 = 2×边数 |


---

## D.9 综合案例：给一个小网络做"体检"

**问题**：给定学校 20 人社交网络，找出"信息传播最快的人"、"最容易被绕过的人"与"天然小团伙"。

步骤：

1. 建图：读边表，检查握手定理（度之和 = 2×边数）；
2. 最短路：无权图用 BFS，加权用 Dijkstra；
3. 中心性：同时看度/接近/介数/PageRank，画四张图对比（结论不同是正常的，要把定义说清）；
4. 社区：Louvain 跑几组分辨率，报告模块度与参数；
5. 输出："若做疫情通报，优先通知介数中心性最高的人；若做班委选举，关注度中心性与 PageRank 都高的人。"

参考要点代码：

    import networkx as nx
    G = nx.read_edgelist("edges.txt")
    print(sum(d for _, d in G.degree()) == 2 * G.number_of_edges())
    print(nx.betweenness_centrality(G)); print(nx.pagerank(G))
    from networkx.algorithms.community import louvain_communities
    print(louvain_communities(G, seed=0))

**反思**：图分析"结论"依赖指标定义；把"问什么"和"用什么"一起写进报告。


---

## D.8 例题集（深入练习）

**例 1：Kruskal 手算**。边（A-B=2, A-C=5, B-C=1, C-D=4）：排序 B-C(1) → A-B(2) → C-D(4) → A-C(5)。依次加入不成环的边：B-C、A-B、C-D；此时 4 点 3 边成树，总权 7。A-C 会成环，跳过。

**例 2：PageRank 三点手算**（有向环 A→B→C→A 加自环简化不计）：稳态分布与转移矩阵最大特征向量相同——直观上"每个点的权重等于流入它的点的权重之和"。

**例 3：BFS 手算**。图 A-B、A-C、B-D、C-D：BFS 从 A 出发的层序：0 层 A；1 层 B、C；2 层 D。因此 A 到 D 最短路为 2（经 B 或 C），无权图最短路 = 层数。

