# -*- coding: utf-8 -*-
"""Generate lab.ipynb for chapter 06 (NetworkX) — guided lab notebook."""
import json, os

cells = []
def md(text): cells.append({"cell_type": "markdown", "metadata": {}, "source": text})
def code(text): cells.append({"cell_type": "code", "metadata": {}, "execution_count": None,
                              "outputs": [], "source": text})

md("""# NetworkX 上机实验（第 6 章 lab）

**要求**：按顺序运行每一格，完成所有 TODO 后运行检查单元；最后截图/导出 notebook 提交。
环境：Python 3.10+，NetworkX ≥ 3.0（推荐 3.x），matplotlib 用于绘图。

---
""")

code("""import networkx as nx
print("NetworkX version:", nx.__version__)
assert nx.__version__ >= "3.0", "请升级 NetworkX"
print("环境 OK")
""")

md("""## Part 1 创建无向图与基本属性

练习：创建无向图、添加节点/边、查看度、邻居、连通性与基本遍历。""")

code("""# TODO 1.1 创建无向图并添加节点与边
G = nx.Graph()
G.add_node(1)
G.add_nodes_from([2, 3, 4])
G.add_edge(1, 2)
G.add_edges_from([(2, 3), (3, 4), (4, 1)])

print("nodes:", G.nodes())
print("edges:", G.edges())
print("degree:", G.degree())
# TODO: 打印节点 1 的邻居
print("neighbors(1):", list(G.neighbors(1)))
""")

code("""# TODO 1.2 连通性与遍历
print("is_connected:", nx.is_connected(G))
print("dfs_preorder(1):", list(nx.dfs_preorder_nodes(G, source=1)))
print("bfs_edges(1):", list(nx.bfs_edges(G, source=1)))
# TODO: 直接打印 bfs 访问顺序（去重）
seen = set()
bfs_order = []
for u, v in nx.bfs_edges(G, source=1):
    if u not in seen:
        seen.add(u); bfs_order.append(u)
    if v not in seen:
        seen.add(v); bfs_order.append(v)
print("bfs_order:", bfs_order)
""")

md("""## Part 2 有向图：入度/出度与前驱/后继""")

code("""# TODO 2.1 创建有向图
DG = nx.DiGraph()
DG.add_nodes_from([1, 2, 3, 4])
DG.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 1)])

print("in_degree:", dict(DG.in_degree()))
print("out_degree:", dict(DG.out_degree()))
for node in DG.nodes():
    print("Node", node, "in-degree", DG.in_degree(node), "out-degree", DG.out_degree(node))
print("predecessors(2):", list(DG.predecessors(2)))
print("successors(2):", list(DG.successors(2)))
print("is_strongly_connected:", nx.is_strongly_connected(DG))
print("is_weakly_connected:", nx.is_weakly_connected(DG))
""")

md("""## Part 3 节点/边属性与加权图""")

code("""# TODO 3.1 加权图与属性
WG = nx.Graph()
WG.add_weighted_edges_from([('A','B',10), ('A','C',6), ('B','C',5)])
WG.add_node('A', role='hub', color='red')

print("nodes(data):", list(WG.nodes(data=True)))
print("edges(data):", list(WG.edges(data=True)))
print("degree:", WG.degree())
print("strength(weighted degree):", WG.degree(weight='weight'))
""")


md("""## 案例卡 1 跟练 / 变形 / 综合任务（班级社交网）

对应讲义案例卡 1：用 nx.Graph 建“班级社交网”。""")

code("""# 案例卡1 跟练：复现班级社交网，观察度与点强度
Gc = nx.Graph()
Gc.add_nodes_from([
    ('小明', {'cls':'一班', 'interest':'数学'}),
    ('小红', {'cls':'一班', 'interest':'编程'}),
    ('小刚', {'cls':'一班', 'interest':'物理'}),
    ('小丽', {'cls':'二班', 'interest':'语文'}),
    ('小华', {'cls':'二班', 'interest':'美术'}),
])
Gc.add_weighted_edges_from([
    ('小明','小红',3), ('小明','小刚',2), ('小红','小刚',4),
    ('小刚','小丽',1), ('小丽','小华',5),
])
print('nodes:', Gc.number_of_nodes(), 'edges:', Gc.number_of_edges())
print('degree:', sorted(dict(Gc.degree()).items(), key=lambda x: (-x[1], x[0])))
print('strength:', sorted(dict(Gc.degree(weight='weight')).items(), key=lambda x: (-x[1], x[0])))
# TODO: 加一条"小华--小红(权重2)"的边，再打印 degree，观察小华是否变重要
""")

code("""# 案例卡1 变形：按属性筛选 + 转邻接矩阵验证对称
Gc.add_edge('小华', '小红', weight=2)
print('加边后 nodes/edges:', Gc.number_of_nodes(), Gc.number_of_edges())
print('一班学生:', [n for n, d in Gc.nodes(data=True) if d.get('cls')=='一班'])
A = nx.to_numpy_array(Gc, nodelist=sorted(Gc.nodes()), weight='weight')
print('邻接矩阵形状:', A.shape)
print('矩阵对称:', bool((A == A.T).all()))
""")

code("""# 案例卡1 综合任务：用生成器造不同网络并对比度
P = nx.path_graph(5)
S = nx.star_graph(4)
Cg = nx.cycle_graph(5)
print('path_graph(5)度数:', sorted(dict(P.degree()).values()))
print('star_graph(4)中心度:', dict(S.degree()))
print('cycle_graph(5)度数:', sorted(dict(Cg.degree()).values()))
centers = [n for n, d in S.degree() if d == 4]
print('star中心节点:', centers)
""")

md("""## Part 4 图的分析指标""")

code("""# TODO 4.1 度/聚类/传递性/中心性
G2 = nx.Graph()
G2.add_edges_from([(1, 2), (1, 3), (2, 3), (3, 4), (4, 5)])

print("degree:", dict(G2.degree()))
print("average_clustering:", nx.average_clustering(G2))
print("clustering(1):", nx.clustering(G2, 1))
print("transitivity:", nx.transitivity(G2))
print("triangles:", nx.triangles(G2))
print("betweenness:", nx.betweenness_centrality(G2))
print("closeness:", nx.closeness_centrality(G2))
print("average_shortest_path_length:", nx.average_shortest_path_length(G2))
print("diameter:", nx.diameter(G2))
""")


md("""## 案例卡 2 跟练 / 变形 / 综合任务（中心性分析）

对应讲义案例卡 2：谁是班里最重要的人（度/介数/接近）。""")

code("""# 案例卡2 跟练：重建"桥梁"社交网，打印度/介数/接近
Cc = nx.Graph()
Cc.add_edges_from([
    ('小明','小红'), ('小明','小刚'), ('小红','小刚'), ('小刚','小丽'),
    ('小丽','小华'), ('小丽','小强'), ('小华','小强'), ('小华','小芳'), ('小强','小芳'),
])
bc = nx.betweenness_centrality(Cc)
cc = nx.closeness_centrality(Cc)
print('degree:', dict(Cc.degree()))
print('betweenness:', {k: round(v,4) for k,v in bc.items()})
print('closeness:', {k: round(v,4) for k,v in cc.items()})
# TODO: 把"小明"和"小芳"直接连起来，观察小丽/小刚的介数如何变化
""")

code("""# 案例卡2 变形：在 karate_club 上排序，找出三种中心性的前3
Kc = nx.karate_club_graph()
bck = nx.betweenness_centrality(Kc)
cck = nx.closeness_centrality(Kc)
degk = dict(Kc.degree())
print('karate按度前3:', sorted(degk.items(), key=lambda x: (-x[1], x[0]))[:3])
print('karate按介数前3:', [(n, round(v,4)) for n,v in sorted(bck.items(), key=lambda x: (-x[1], x[0]))[:3]])
print('karate按接近前3:', [(n, round(v,4)) for n,v in sorted(cck.items(), key=lambda x: (-x[1], x[0]))[:3]])
""")

code("""# 案例卡2 综合任务：中心性与社区结合，找"桥"节点
from networkx.algorithms import community as nxcom
Kc = nx.karate_club_graph()
comms = nxcom.greedy_modularity_communities(Kc)
print('社区数:', len(comms), '大小:', [len(c) for c in comms])
bck = nx.betweenness_centrality(Kc)
top_bridge = sorted(bck.items(), key=lambda x: (-x[1], x[0]))[0]
print('介数最高节点:', top_bridge)
n0 = top_bridge[0]
print('它的邻居:', sorted(list(Kc.neighbors(n0))))
# TODO: 判断该节点是否"跨社区"（其邻居分布在多个社区）
""")

md("""## Part 5 遍历、最短路径与最小生成树""")

code("""# TODO 5.1 遍历与无权最短路径（6.3 遍历问题）
G3 = nx.Graph()
G3.add_edges_from([(1, 2), (1, 3), (2, 4), (3, 4), (4, 5)])
print("dfs:", list(nx.dfs_preorder_nodes(G3, source=1)))
print("bfs_edges:", list(nx.bfs_edges(G3, source=1)))
print("shortest_path(1,5):", nx.shortest_path(G3, 1, 5))
print("shortest_path_length:", nx.shortest_path_length(G3, 1, 5))
""")

code("""# TODO 5.2 带权最短路径（Dijkstra）
DG2 = nx.DiGraph()
for u, v, w in [('A','B',3), ('A','C',2), ('B','C',1), ('B','D',4),
                ('C','D',2), ('C','E',1), ('D','E',3)]:
    DG2.add_edge(u, v, weight=w)
print("dijkstra_path:", nx.dijkstra_path(DG2, 'A', 'E', weight='weight'))
print("dijkstra_path_length:", nx.dijkstra_path_length(DG2, 'A', 'E', weight='weight'))
# 所有点对最短路径矩阵
import numpy as np
fwl = nx.floyd_warshall_numpy(DG2, weight='weight')
print("floyd-warshall matrix shape:", fwl.shape)
""")

code("""# TODO 5.3 最小生成树（MST）
Mw = nx.Graph()
Mw.add_weighted_edges_from([
    ('A','B',10), ('A','C',6), ('A','D',5), ('B','C',5), ('B','D',15),
    ('B','E',4), ('C','D',15), ('C','F',12), ('D','E',20), ('E','F',9)
])
T = nx.minimum_spanning_tree(Mw)
print("MST edges:", sorted(T.edges(data='weight')))
print("MST total weight:", sum(w for _, _, w in T.edges(data='weight')))
print("MST edge count:", T.number_of_edges())
""")


md("""## 案例卡 3 跟练 / 变形 / 综合任务（加权最短路径）

对应讲义案例卡 3：地铁换乘总时间最少路线。""")

code("""# 案例卡3 跟练：地铁加权网 + Dijkstra 最少时间
Mc = nx.Graph()
Mc.add_weighted_edges_from([
    ('中央公园','城东',3), ('中央公园','大学城',2), ('城东','大学城',1),
    ('城东','火车站',4), ('大学城','火车站',2), ('大学城','机场',1),
    ('火车站','机场',3), ('火车站','科技园',2), ('机场','科技园',4),
])
print('dijkstra_path:', nx.dijkstra_path(Mc, '中央公园', '科技园', weight='weight'))
print('dijkstra_len:', nx.dijkstra_path_length(Mc, '中央公园', '科技园', weight='weight'))
print('single_source:', {k: round(v,4) for k,v in sorted(nx.single_source_dijkstra_path_length(Mc,'中央公园',weight='weight').items())})
# TODO: 新增"机场-城东"直连(2分钟)，看看最短路会不会变
""")

code("""# 案例卡3 变形：无权 vs 带权；Floyd-Warshall 全源矩阵
print('无权最短路径:', nx.shortest_path(Mc, '中央公园', '科技园'))
print('无权最短边数:', nx.shortest_path_length(Mc, '中央公园', '科技园'))
FW = nx.floyd_warshall_numpy(Mc, weight='weight')
names = sorted(Mc.nodes())
print('Floyd矩阵形状:', FW.shape)
print('中央公园->科技园:', FW[names.index('中央公园'), names.index('科技园')])
# TODO: 比较"边数最少"与"时间最少"两条路线是否一致
""")

code("""# 案例卡3 综合任务：MST 与最短路径对比 + 保存路线图
T = nx.minimum_spanning_tree(Mc, weight='weight')
print('MST边:', sorted(T.edges(data='weight')))
print('MST总权重:', sum(w for _, _, w in T.edges(data='weight')))
print('最短路径 vs MST 目标不同')
path = nx.dijkstra_path(Mc, '中央公园', '科技园', weight='weight')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False
pos = nx.spring_layout(Mc, seed=42, k=0.9)
plt.figure(figsize=(6.0, 4.4))
nx.draw_networkx_edges(Mc, pos, alpha=0.3, edge_color='#999999', width=1.2)
nx.draw_networkx_edges(Mc, pos, edgelist=list(zip(path[:-1], path[1:])), edge_color='#c0392b', width=3.0)
nx.draw_networkx_nodes(Mc, pos, node_size=500, node_color='#dff3e0', edgecolors='#3a8f4f')
nx.draw_networkx_labels(Mc, pos, font_size=10, font_family='Microsoft YaHei')
plt.title('地铁最少时间路线')
plt.axis('off'); plt.tight_layout(); plt.savefig('case3_metro_lab.png')
print('已保存 case3_metro_lab.png')
""")

md("""## Part 6 综合任务：空手道俱乐部

用 nx.karate_club_graph() 完成：社区划分（贪心模块度）、计算模块度、求 0 号与 33 号之间的最短路径，并绘制度分布与社区图。""")

code("""# TODO 6 综合任务
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei", "DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False
from networkx.algorithms import community as nxcom
from networkx.algorithms.community.quality import modularity

K = nx.karate_club_graph()
print("nodes/edges:", K.number_of_nodes(), K.number_of_edges())

comms = nxcom.greedy_modularity_communities(K)
Q = modularity(K, comms)
print("communities:", len(comms), " sizes:", [len(c) for c in comms])
print("modularity Q:", round(Q, 4))

path = nx.shortest_path(K, source=0, target=33)
print("shortest path 0->33:", path)

deg = [d for _, d in K.degree()]
plt.figure(figsize=(5.4, 3.2))
plt.hist(deg, bins=range(0, max(deg) + 2), color="#4b8bbe", edgecolor="white")
plt.xlabel("度"); plt.ylabel("节点数")
plt.title("空手道俱乐部 度分布")
plt.tight_layout(); plt.savefig("karate_degree_lab.png")
print("已保存 karate_degree_lab.png")
""")

md("""## 提交清单

- [ ] 所有 TODO 均已填写并运行；
- [ ] Part 4 的 betweenness / closeness 已输出；
- [ ] Part 5 的 Dijkstra 最短路径与 MST 总权重已记录；
- [ ] Part 6 已生成 karate_degree_lab.png 并写出社区数与模块度；
- [ ] 导出为 html / 保留 ipynb 提交。

**延伸**：完成 exercises/ 的自测题与 04-综合案例.md 的拓展任务。""")

nb = {
    "cells": cells,
    "metadata": {
        "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
        "language_info": {"name": "python", "version": "3.10"}
    },
    "nbformat": 4,
    "nbformat_minor": 5,
}
out = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                   "chapters", "06-networkx", "lab", "lab.ipynb")
os.makedirs(os.path.dirname(out), exist_ok=True)
with open(out, "w", encoding="utf-8") as f:
    # 统一为中文字体设置（所有绘图单元注入微软雅黑）
    NL = chr(10)
    for _c in nb["cells"]:
        if _c["cell_type"] == "code":
            _src = "".join(_c.get("source", []))
            if (("plt." in _src) or ("sns." in _src) or ("matplotlib" in _src)
                    or ("savefig" in _src)) and ("font.sans-serif" not in _src):
                _c["source"] = [
                    "import matplotlib.pyplot as plt" + NL,
                    'plt.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei", "DejaVu Sans"]' + NL,
                    'plt.rcParams["axes.unicode_minus"] = False' + NL,
                ] + list(_c.get("source", []))
    json.dump(nb, f, ensure_ascii=False, indent=1)
print("saved", out, "cells:", len(cells))
