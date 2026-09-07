# -*- coding: utf-8 -*-
"""Generate figures for chapter 06 (NetworkX) -> chapters/06-networkx/images."""
import os
import numpy as np
import networkx as nx
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                   "chapters", "06-networkx", "images")
os.makedirs(OUT, exist_ok=True)
plt.rcParams["figure.dpi"] = 150
plt.rcParams["savefig.bbox"] = "tight"
plt.rcParams["axes.spines.top"] = False
plt.rcParams["axes.spines.right"] = False
plt.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei", "DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False
np.random.seed(42)

# ---------------------------------------------------------------
# 1) graph_basic.png : undirected cycle graph + directed cycle graph
# ---------------------------------------------------------------
G = nx.Graph()
G.add_nodes_from([1, 2, 3, 4])
G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 1)])

DG = nx.DiGraph()
DG.add_nodes_from([1, 2, 3, 4])
DG.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 1)])

pos = nx.circular_layout(G)
fig, axes = plt.subplots(1, 2, figsize=(9.0, 4.2))
nx.draw_networkx_nodes(G, pos, node_size=700, node_color="#cfe3f7",
                       edgecolors="#2f6fb3", ax=axes[0])
nx.draw_networkx_edges(G, pos, width=2.2, edge_color="#2f6fb3", ax=axes[0])
nx.draw_networkx_labels(G, pos, font_size=13, font_family="Microsoft YaHei", ax=axes[0])
axes[0].set_title("无向图 Graph (1-2-3-4-1)", fontsize=12)
axes[0].axis("off")

pos2 = nx.circular_layout(DG)
nx.draw_networkx_nodes(DG, pos2, node_size=700, node_color="#d9f2d0",
                       edgecolors="#3a8f4f", ax=axes[1])
nx.draw_networkx_edges(DG, pos2, width=2.2, edge_color="#3a8f4f",
                       arrowstyle="->", arrowsize=18, ax=axes[1])
nx.draw_networkx_labels(DG, pos2, font_size=13, font_family="Microsoft YaHei", ax=axes[1])
axes[1].set_title("有向图 DiGraph (1->2->3->4->1)", fontsize=12)
axes[1].axis("off")
fig.tight_layout()
fig.savefig(os.path.join(OUT, "graph_basic.png"))
plt.close(fig)

# ---------------------------------------------------------------
# 2) network_case_degree_dist.png : karate club degree distribution
# ---------------------------------------------------------------
K = nx.karate_club_graph()
degree_sequence = sorted([d for _, d in K.degree()], reverse=True)
fig, ax = plt.subplots(figsize=(6.4, 4.0))
ax.bar(range(1, len(degree_sequence) + 1), degree_sequence,
       color="#4b8bbe", edgecolor="white")
ax.set_xlabel("节点（按度降序排列）", fontsize=11)
ax.set_ylabel("度", fontsize=11)
ax.set_title("空手道俱乐部网络 度分布", fontsize=13)
ax.grid(axis="y", alpha=0.3)
mean_deg = np.mean(degree_sequence)
ax.axhline(mean_deg, color="#c0392b", ls="--", lw=1.6)
ax.text(1, mean_deg + 0.15, "平均度 = " + "%.2f" % mean_deg,
        color="#c0392b", fontsize=10)
fig.tight_layout()
fig.savefig(os.path.join(OUT, "network_case_degree_dist.png"))
plt.close(fig)

# ---------------------------------------------------------------
# 3) network_case_communities.png : communities + shortest path highlight
# ---------------------------------------------------------------
from networkx.algorithms import community as nxcom

K = nx.karate_club_graph()
comms = nxcom.greedy_modularity_communities(K)
colors = ["#4b8bbe", "#e07b39", "#3a8f4f", "#7f5fb5", "#c0392b"]
node_color = {}
for ci, cset in enumerate(comms):
    for n in cset:
        node_color[n] = colors[ci % len(colors)]

path = nx.shortest_path(K, source=0, target=33)
path_edges = list(zip(path[:-1], path[1:]))

pos = nx.spring_layout(K, seed=42)
fig, ax = plt.subplots(figsize=(8.2, 6.2))
nx.draw_networkx_edges(K, pos, alpha=0.35, edge_color="#999999",
                       width=1.0, ax=ax)
nx.draw_networkx_edges(K, pos, edgelist=path_edges, edge_color="#c0392b",
                       width=3.0, ax=ax)
nx.draw_networkx_nodes(K, pos, node_size=260,
                       node_color=[node_color[n] for n in K.nodes()],
                       edgecolors="white", linewidths=1.2, ax=ax)
labels = {n: str(n) for n in K.nodes()}
nx.draw_networkx_labels(K, pos, labels, font_size=8,
                        font_family="Microsoft YaHei", ax=ax)
ax.set_title("空手道俱乐部：社区划分 + 0→33 最短路径（红色）", fontsize=13)
ax.axis("off")
handles = [plt.Line2D([0], [0], marker="o", color="w", markerfacecolor=colors[i % len(colors)],
                      markersize=9, label="社区 " + str(i + 1)) for i in range(len(comms))]
handles.append(plt.Line2D([0], [0], color="#c0392b", lw=3, label="最短路径"))
ax.legend(handles=handles, loc="lower right", fontsize=8)
fig.tight_layout()
fig.savefig(os.path.join(OUT, "network_case_communities.png"))
plt.close(fig)


# ---------------------------------------------------------------
# 4) case1_class_network.png : 班级社交网 (Graph + attributes + degree)
# ---------------------------------------------------------------
G = nx.Graph()
G.add_nodes_from([
    ('小明', {'cls': '一班', 'interest': '数学'}),
    ('小红', {'cls': '一班', 'interest': '编程'}),
    ('小刚', {'cls': '一班', 'interest': '物理'}),
    ('小丽', {'cls': '二班', 'interest': '语文'}),
    ('小华', {'cls': '二班', 'interest': '美术'}),
])
G.add_weighted_edges_from([
    ('小明','小红',3), ('小明','小刚',2), ('小红','小刚',4),
    ('小刚','小丽',1), ('小丽','小华',5),
])
pos = nx.spring_layout(G, seed=42, k=0.8)
fig, ax = plt.subplots(figsize=(6.4, 4.6))
nx.draw_networkx_nodes(G, pos, node_size=800, node_color='#cfe3f7', edgecolors='#2f6fb3', ax=ax)
nx.draw_networkx_edges(G, pos, width=2.0, edge_color='#4b8bbe', ax=ax)
nx.draw_networkx_labels(G, pos, font_size=11, font_family='Microsoft YaHei', ax=ax)
ax.set_title('班级社交网', fontsize=13)
ax.axis('off')
fig.tight_layout()
fig.savefig(os.path.join(OUT, 'case1_class_network.png'))
plt.close(fig)

# 5) case2_centrality.png : 三种中心性条形对比
C = nx.Graph()
C.add_edges_from([
    ('小明','小红'), ('小明','小刚'), ('小红','小刚'), ('小刚','小丽'),
    ('小丽','小华'), ('小丽','小强'), ('小华','小强'), ('小华','小芳'), ('小强','小芳'),
])
bc = nx.betweenness_centrality(C)
cc = nx.closeness_centrality(C)
names = sorted(C.nodes())
deg_v = [C.degree(n) for n in names]
bc_v = [round(bc[n],4) for n in names]
cc_v = [round(cc[n],4) for n in names]
fig, axes = plt.subplots(1, 3, figsize=(11.0, 3.6))
axes[0].bar(names, deg_v, color='#4b8bbe'); axes[0].set_ylabel('度'); axes[0].set_title('度')
axes[1].bar(names, bc_v, color='#e07b39'); axes[1].set_ylabel('介数中心性'); axes[1].set_title('介数中心性')
axes[2].bar(names, cc_v, color='#3a8f4f'); axes[2].set_ylabel('接近中心性'); axes[2].set_title('接近中心性')
for ax in axes:
    ax.tick_params(axis='x', rotation=30, labelsize=8)
fig.suptitle('班级社交网：三种中心性对比')
fig.tight_layout()
fig.savefig(os.path.join(OUT, 'case2_centrality.png'))
plt.close(fig)

# 6) case3_metro.png : 加权地铁网 + 最短时间路线
M = nx.Graph()
M.add_weighted_edges_from([
    ('中央公园','城东',3), ('中央公园','大学城',2), ('城东','大学城',1),
    ('城东','火车站',4), ('大学城','火车站',2), ('大学城','机场',1),
    ('火车站','机场',3), ('火车站','科技园',2), ('机场','科技园',4),
])
path = nx.dijkstra_path(M, '中央公园', '科技园', weight='weight')
path_edges = list(zip(path[:-1], path[1:]))
pos = nx.spring_layout(M, seed=42, k=0.9)
fig, ax = plt.subplots(figsize=(7.0, 5.0))
nx.draw_networkx_nodes(M, pos, node_size=650, node_color='#dff3e0', edgecolors='#3a8f4f', ax=ax)
nx.draw_networkx_edges(M, pos, alpha=0.35, edge_color='#999999', width=1.2, ax=ax)
nx.draw_networkx_edges(M, pos, edgelist=path_edges, edge_color='#c0392b', width=3.0, ax=ax)
nx.draw_networkx_labels(M, pos, font_size=11, font_family='Microsoft YaHei', ax=ax)
ax.set_title('地铁网：中央公园 -> 科技园 最少时间路线', fontsize=13)
ax.axis('off')
fig.tight_layout()
fig.savefig(os.path.join(OUT, 'case3_metro.png'))
plt.close(fig)


print("figures saved to", OUT)
for f in sorted(os.listdir(OUT)):
    print("  ", f)
