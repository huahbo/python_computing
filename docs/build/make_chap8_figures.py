# -*- coding: utf-8 -*-
"""Generate figures for chapter 08 (scikit-learn)."""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris, load_breast_cancer, load_wine
from sklearn.model_selection import cross_val_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.cluster import KMeans, DBSCAN
from sklearn.decomposition import PCA
from sklearn.datasets import make_moons

OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                   "chapters", "08-sklearn", "images")
os.makedirs(OUT, exist_ok=True)
plt.rcParams["figure.dpi"] = 150
plt.rcParams["savefig.bbox"] = "tight"
plt.rcParams["axes.spines.top"] = False
plt.rcParams["axes.spines.right"] = False
plt.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei", "DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False
np.random.seed(42)

# ---------- 1) iris pairwise scatter ----------
iris = load_iris()
X, y = iris.data, iris.target
feat = [f.split(" ")[0].replace(" (cm)", "") for f in iris.feature_names]
fig, axes = plt.subplots(4, 4, figsize=(10, 10))
colors = ["#2f6fb3", "#e07b39", "#3a8f4f"]
labels = iris.target_names
for i in range(4):
    for j in range(4):
        ax = axes[i, j]
        if i == j:
            ax.hist(X[:, i], bins=20, color="#9ec5e8", edgecolor="white")
            ax.set_yticks([])
        else:
            for c in range(3):
                ax.scatter(X[y == c, j], X[y == c, i], s=8, c=colors[c], alpha=0.7)
        if i == 3:
            ax.set_xlabel(feat[j], fontsize=8)
        if j == 0:
            ax.set_ylabel(feat[i], fontsize=8)
        ax.tick_params(labelsize=6)
fig.suptitle("Iris 数据集特征两两分布", fontsize=13)
fig.savefig(os.path.join(OUT, "iris_pairplot.png"))
plt.close(fig)

# ---------- 2) decision tree for iris ----------
clf = DecisionTreeClassifier(max_depth=3, random_state=42).fit(X, y)
fig, ax = plt.subplots(figsize=(13, 7))
plot_tree(clf, feature_names=iris.feature_names, class_names=list(iris.target_names),
          filled=True, rounded=True, ax=ax, fontsize=8)
ax.set_title("Iris 决策树（max_depth=3）", fontsize=12)
fig.savefig(os.path.join(OUT, "decision_tree_iris.png"))
plt.close(fig)

# ---------- 3) scaling effect ----------
bc = load_breast_cancer()
Xb, yb = bc.data, bc.target
def cv_mean(pipe):
    return cross_val_score(pipe, Xb, yb, cv=5).mean()
names = ["SVC 原始", "SVC 标准化", "KNN 原始", "KNN 标准化"]
vals = [cv_mean(Pipeline([("clf", SVC())])),
        cv_mean(Pipeline([("sc", StandardScaler()), ("clf", SVC())])),
        cv_mean(Pipeline([("clf", KNeighborsClassifier())])),
        cv_mean(Pipeline([("sc", StandardScaler()), ("clf", KNeighborsClassifier())]))]
fig, ax = plt.subplots(figsize=(6.4, 4.0))
bars = ax.bar(names, vals, color=["#c0392b", "#27ae60", "#c0392b", "#27ae60"], alpha=0.85)
for b, v in zip(bars, vals):
    ax.text(b.get_x() + b.get_width() / 2, v + 0.004, f"{v:.3f}", ha="center", fontsize=9)
ax.set_ylim(0.85, 1.0)
ax.set_ylabel("5 折交叉验证准确率")
ax.set_title("标准化对乳腺癌数据集上 SVC / KNN 的影响")
fig.savefig(os.path.join(OUT, "scaling_effect.png"))
plt.close(fig)

# ---------- 4) KMeans vs DBSCAN on moons ----------
moons, y_moons = make_moons(n_samples=300, noise=0.1, random_state=42)
km = KMeans(n_clusters=2, random_state=42).fit(moons)
db = DBSCAN(eps=0.2, min_samples=5).fit(moons)
fig, axes = plt.subplots(1, 2, figsize=(10, 4.2))
axes[0].scatter(moons[:, 0], moons[:, 1], c=km.labels_, cmap="viridis", s=20)
axes[0].scatter(km.cluster_centers_[:, 0], km.cluster_centers_[:, 1],
                c="red", marker="x", s=120, linewidths=2)
axes[0].set_title("KMeans(k=2)：容易被弯月形状误导")
axes[0].set_xlabel("Feature 1"); axes[0].set_ylabel("Feature 2")
u = set(db.labels_)
for k in u:
    col = "#444444" if k == -1 else plt.cm.viridis(k / (len(u) - 1) if len(u) > 1 else 0)
    m = db.labels_ == k
    axes[1].scatter(moons[m, 0], moons[m, 1], color=col, s=20, label=f"cluster {k}")
axes[1].set_title("DBSCAN：能发现任意形状簇并标记噪声(-1)")
axes[1].set_xlabel("Feature 1"); axes[1].set_ylabel("Feature 2")
axes[1].legend(fontsize=8)
fig.savefig(os.path.join(OUT, "dbscan_kmeans_moons.png"))
plt.close(fig)

# ---------- 5) wine PCA: true labels vs KMeans clusters ----------
wine = load_wine()
Xw, yw = wine.data, wine.target
Xs = StandardScaler().fit_transform(Xw)
pca = PCA(n_components=2)
Xp = pca.fit_transform(Xs)
kmw = KMeans(n_clusters=3, random_state=42).fit(Xs)
fig, axes = plt.subplots(1, 2, figsize=(10, 4.2))
for ax, lab, ttl in [(axes[0], yw, "PCA 按真实类别着色"),
                     (axes[1], kmw.labels_, "PCA 按 KMeans 聚类着色")]:
    sc = ax.scatter(Xp[:, 0], Xp[:, 1], c=lab, cmap="viridis", s=22)
    ax.set_title(ttl)
    ax.set_xlabel("PC1"); ax.set_ylabel("PC2")
    ax.grid(alpha=0.2)
axes[0].legend(handles=[plt.Line2D([], [], marker="o", ls="", color=plt.cm.viridis(i / 2),
             label=wine.target_names[i]) for i in range(3)], fontsize=8)
axes[1].legend(handles=[plt.Line2D([], [], marker="o", ls="", color=plt.cm.viridis(i / 2),
             label=f"簇 {i}") for i in range(3)], fontsize=8)
fig.savefig(os.path.join(OUT, "wine_pca_true_vs_kmeans.png"))
plt.close(fig)

# ---------- 6) wine feature importance ----------
rf = RandomForestClassifier(n_estimators=100, random_state=42).fit(Xs, yw)
imp = rf.feature_importances_
short = ["alcohol", "malic", "ash", "alcalinity", "Mg", "phenols", "flavanoids",
         "nonflavan", "proanth", "color", "hue", "OD280", "proline"]
order = np.argsort(imp)
fig, ax = plt.subplots(figsize=(7.2, 5.0))
ax.barh(np.array(short)[order], imp[order], color="#2f6fb3")
ax.set_xlabel("特征重要性")
ax.set_title("随机森林：Wine 特征重要性")
ax.grid(axis="x", alpha=0.25)
fig.savefig(os.path.join(OUT, "wine_feature_importance.png"))
plt.close(fig)

print("figures saved to", OUT)
for f in sorted(os.listdir(OUT)):
    print("  ", f)