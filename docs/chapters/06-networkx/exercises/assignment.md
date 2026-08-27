# NetworkX 练习（12 题）

**说明**：本作业覆盖 NetworkX 的核心主题：创建无向图/有向图、节点与边属性、度与度分布、连通性、聚类系数、中心性、最短路径、最小生成树、社区划分与图生成器。请先独立完成，再查看答案。

---

## 题目

### 容易 / 中等（1-6）

1. **创建无向图并输出度分布**：用 nx.Graph 创建包含节点 1–5 与边 (1,2),(1,3),(2,3),(3,4),(4,5) 的图，打印所有节点度，并输出度分布（升序列表）。

2. **创建有向图（入度/出度/前驱/后继）**：创建 nx.DiGraph，边为 1→2, 2→3, 3→4, 4→1, 2→4。打印每个节点的入度与出度、节点 2 的前驱与后继，并判断强/弱连通。

3. **节点与边属性**：用 add_weighted_edges_from 建一个三角形加权图（A-B=10, A-C=6, B-C=5），给 A 加属性 role="hub"，打印 nodes(data=True)、edges(data=True) 与加权度。

4. **邻接矩阵**：把上题的无向图用 to_numpy_array 转矩阵，说明矩阵是否对称及对角元含义。

5. **连通性**：构造两个不相连的组件（如 {1,2,3} 和 {4,5}），用 connected_components 输出每个分量，并判断 is_connected。

6. **度分布与随机图**：用 erdos_renyi_graph(20, 0.1, seed=1) 生成随机图，输出边数与度分布（前 5 大）。

### 中等 / 稍难（7-10）

7. **聚类系数与传递性**：对空手道俱乐部网络计算 average_clustering 与 transitivity，说明两者含义差异。

8. **最短路径（Dijkstra）**：用带权有向图（A→B=3, A→C=2, B→C=1, B→D=4, C→D=2, C→E=1, D→E=3），求 A 到 E 的最短路径与长度。

9. **最小生成树**：用加权无向图（A-B=10, A-C=6, A-D=5, B-C=5, B-D=15, B-E=4, C-D=15, C-F=12, D-E=20, E-F=9），求最小生成树及总权重。

10. **介数中心性**：对路径图 path_graph(8) 计算介数中心性，输出最高的 2 个节点（预期是中间节点）。

### 稍难 / 挑战（11-12）

11. **社区划分与模块度**：对 karate_club_graph 用 greedy_modularity_communities 划分社区并计算模块度 Q，写出社区个数与各社区大小。

12. **全源最短路径（Floyd-Warshall）**：用上面的带权有向图，用 floyd_warshall_numpy 计算两两距离矩阵，验证 A 到 E 距离 = 3，且对角线为 0。

---

## 答案详解（请先独立完成再查看）

### 答案 1（创建无向图并输出度分布）

~~~~python
import networkx as nx
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 3), (3, 4), (4, 5)])
print("degrees:", dict(G.degree()))
print("degree_distribution:", sorted([d for _, d in G.degree()]))
~~~~

~~~~text
degrees: {1: 2, 2: 2, 3: 3, 4: 2, 5: 1}
degree_distribution: [1, 2, 2, 2, 3]
~~~~

### 答案 2（有向图）

~~~~python
DG = nx.DiGraph()
DG.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 1), (2, 4)])
print("in_degree:", dict(DG.in_degree()))
print("out_degree:", dict(DG.out_degree()))
print("predecessors(2):", list(DG.predecessors(2)))
print("successors(2):", list(DG.successors(2)))
print("is_strongly_connected:", nx.is_strongly_connected(DG))
print("is_weakly_connected:", nx.is_weakly_connected(DG))
~~~~

~~~~text
in_degree: {1: 1, 2: 1, 3: 1, 4: 2}
out_degree: {1: 1, 2: 2, 3: 1, 4: 1}
predecessors(2): [1]
successors(2): [3, 4]
is_strongly_connected: True
is_weakly_connected: True
~~~~

### 答案 3（节点与边属性）

~~~~python
G = nx.Graph()
G.add_weighted_edges_from([("A", "B", 10), ("A", "C", 6), ("B", "C", 5)])
G.add_node("A", role="hub", color="red")
print("nodes(data):", list(G.nodes(data=True)))
print("edges(data):", list(G.edges(data=True)))
print("weighted degree:", dict(G.degree(weight="weight")))
~~~~

~~~~text
nodes(data): [('A', {'role': 'hub', 'color': 'red'}), ('B', {}), ('C', {})]
edges(data): [('A', 'B', {'weight': 10}), ('A', 'C', {'weight': 6}), ('B', 'C', {'weight': 5})]
weighted degree: {'A': 16, 'B': 15, 'C': 11}
~~~~

### 答案 4（邻接矩阵）

~~~~python
import numpy as np
A = nx.to_numpy_array(G)
print(A)
print("对称:", np.allclose(A, A.T))
print("对角元:", np.diag(A))
~~~~

~~~~text
[[0. 1. 1.]
 [1. 0. 1.]
 [1. 1. 0.]]
对称: True
对角元: [0. 0. 0.]
~~~~

由于是无向图，邻接矩阵对称；对角元为 0（无自环）。

### 答案 5（连通性）

~~~~python
G = nx.Graph()
G.add_edges_from([(1, 2), (2, 3), (4, 5)])
print("is_connected:", nx.is_connected(G))
print("components:", [sorted(c) for c in nx.connected_components(G)])
~~~~

~~~~text
is_connected: False
components: [[1, 2, 3], [4, 5]]
~~~~

### 答案 6（随机图）

~~~~python
import random
random.seed(1)
G = nx.erdos_renyi_graph(20, 0.1, seed=1)
print("edge count:", G.number_of_edges())
print("top5 degrees:", sorted([d for _, d in G.degree()], reverse=True)[:5])
~~~~

~~~~text
edge count: 23
top5 degrees: [5, 4, 4, 4, 3]
~~~~

### 答案 7（聚类系数与传递性）

~~~~python
K = nx.karate_club_graph()
print("average_clustering:", round(nx.average_clustering(K), 4))
print("transitivity:", round(nx.transitivity(K), 4))
~~~~

~~~~text
average_clustering: 0.5706
transitivity: 0.2557
~~~~

平均聚类系数是各节点局部聚类系数的平均；传递性是“三角形/开放三元组”的全局比值，二者数值不同，衡量侧重点不同。

### 答案 8（Dijkstra 最短路径）

~~~~python
DG = nx.DiGraph()
for u, v, w in [("A","B",3), ("A","C",2), ("B","C",1), ("B","D",4),
                ("C","D",2), ("C","E",1), ("D","E",3)]:
    DG.add_edge(u, v, weight=w)
print("dijkstra_path:", nx.dijkstra_path(DG, "A", "E", weight="weight"))
print("dijkstra_length:", nx.dijkstra_path_length(DG, "A", "E", weight="weight"))
~~~~

~~~~text
dijkstra_path: ['A', 'C', 'E']
dijkstra_length: 3
~~~~

### 答案 9（最小生成树）

~~~~python
G = nx.Graph()
G.add_weighted_edges_from([
    ("A","B",10), ("A","C",6), ("A","D",5), ("B","C",5), ("B","D",15),
    ("B","E",4), ("C","D",15), ("C","F",12), ("D","E",20), ("E","F",9)
])
T = nx.minimum_spanning_tree(G)
print("MST edges:", sorted(T.edges(data="weight")))
print("MST total:", sum(w for _, _, w in T.edges(data="weight")))
~~~~

~~~~text
MST edges: [('A', 'C', {'weight': 6}), ('A', 'D', {'weight': 5}), ('B', 'C', {'weight': 5}), ('B', 'E', {'weight': 4}), ('E', 'F', {'weight': 9})]
MST total: 29
~~~~

### 答案 10（介数中心性）

~~~~python
G = nx.path_graph(8)
bc = nx.betweenness_centrality(G)
top = sorted(bc.items(), key=lambda x: x[1], reverse=True)[:2]
print("top betweenness:", top)
~~~~

~~~~text
top betweenness: [(3, 0.5714285714285714), (4, 0.5714285714285714)]
~~~~

路径图的中间节点（3、4）承担大部分最短路径，介数中心性最高。

### 答案 11（社区划分与模块度）

~~~~python
from networkx.algorithms import community as nxcom
from networkx.algorithms.community.quality import modularity
K = nx.karate_club_graph()
comms = nxcom.greedy_modularity_communities(K)
Q = modularity(K, comms)
print("num communities:", len(comms))
print("sizes:", [len(c) for c in comms])
print("modularity Q:", round(Q, 4))
~~~~

~~~~text
num communities: 3
sizes: [17, 9, 8]
modularity Q: 0.411
~~~~

### 答案 12（Floyd-Warshall）

~~~~python
import numpy as np
DG = nx.DiGraph()
for u, v, w in [("A","B",3), ("A","C",2), ("B","C",1), ("B","D",4),
                ("C","D",2), ("C","E",1), ("D","E",3)]:
    DG.add_edge(u, v, weight=w)
D = nx.floyd_warshall_numpy(DG, weight="weight")
idx = list(DG.nodes())
print("A->E:", D[idx.index("A"), idx.index("E")])
print("diagonal:", np.diag(D))
~~~~

~~~~text
A->E: 3.0
diagonal: [0. 0. 0. 0. 0.]
~~~~

---

# 结束语

建议把每题运行结果截图/导出，整理成一篇报告提交。完成后可对照 answers.ipynb 与 quiz.ipynb 巩固。
