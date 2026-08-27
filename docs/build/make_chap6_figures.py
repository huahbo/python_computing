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

print("figures saved to", OUT)
for f in sorted(os.listdir(OUT)):
    print("  ", f)
