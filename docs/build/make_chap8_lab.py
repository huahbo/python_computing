# -*- coding: utf-8 -*-
"""Generate lab.ipynb for chapter 08 (scikit-learn) - guided lab notebook."""
import json, os

cells = []
def md(text): cells.append({"cell_type": "markdown", "metadata": {}, "source": text})
def code(text): cells.append({"cell_type": "code", "metadata": {}, "execution_count": None, "outputs": [], "source": text})

md("""
# scikit-learn 上机实验（第 8 章 lab）

**要求**：按顺序运行每一格，完成所有 # TODO 后运行检查单元；最后截图/导出 notebook 提交。
环境：Python 3.10+，scikit-learn >= 1.3（本机版本 1.6+），另需 numpy / pandas / matplotlib。

---
""")

code("""
import numpy as np, pandas as pd, matplotlib
import sklearn
print("sklearn", sklearn.__version__)
print("numpy", np.__version__)
print("pandas", pd.__version__)
print("matplotlib", matplotlib.__version__)
assert sklearn.__version__ >= "1.3", "please upgrade scikit-learn"
from sklearn.datasets import load_iris, load_diabetes, load_breast_cancer
print("env OK")
""")

md("""
## Part 1 数据预处理：编码、缩放、划分与交叉验证
""")

code("""
import numpy as np
from sklearn.preprocessing import OneHotEncoder, LabelEncoder, StandardScaler, MinMaxScaler

data = np.array([['male'], ['female'], ['male'], ['female']])
enc = OneHotEncoder(sparse_output=False).fit(data)
print("OneHot categories:", enc.categories_)
print(enc.transform(data))

le = LabelEncoder().fit(['male', 'female', 'male', 'female'])
print("LabelEncoder classes:", le.classes_)
print("transform:", le.transform(['male', 'male', 'female']))

X = np.array([[1, 2], [3, 4], [5, 6]])
ss = StandardScaler().fit(X)
print("StandardScaler mean:", ss.mean_, "scale:", np.round(ss.scale_, 6))
print(ss.transform(X))

mm = MinMaxScaler().fit(X)
print("MinMaxScaler data_min:", mm.data_min_, "data_max:", mm.data_max_)
print(mm.transform(X))
""")

code("""
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression

iris = load_iris(); X, y = iris.data, iris.target
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)
print("train/test shapes:", Xtr.shape, Xte.shape)
print("test class counts:", np.unique(yte, return_counts=True))

scores = cross_val_score(LogisticRegression(max_iter=1000), Xtr, ytr, cv=5)
print("5-fold scores:", np.round(scores, 4))
print("mean:", round(scores.mean(), 4))
""")

md("""
## Part 2 有监督学习：分类与回归

练习：在 Iris 上比较多个分类器；在 Diabetes 上做回归并比较 L1/L2 正则化。
""")

code("""
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report

models = {
    "KNN(k=5)": KNeighborsClassifier(n_neighbors=5),
    "LogisticRegression": LogisticRegression(max_iter=1000),
    "DecisionTree": DecisionTreeClassifier(random_state=42),
    "RandomForest(100)": RandomForestClassifier(n_estimators=100, random_state=42),
}
for name, m in models.items():
    m.fit(Xtr, ytr)
    print(name, "acc =", round(accuracy_score(yte, m.predict(Xte)), 4))

best = models["RandomForest(100)"]
print(classification_report(yte, best.predict(Xte), target_names=iris.target_names))
""")

code("""
from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

d = load_diabetes(); Xd, yd = d.data, d.target
Xd_tr, Xd_te, yd_tr, yd_te = train_test_split(Xd, yd, test_size=0.2, random_state=42)
for name, m in [("LinearRegression", LinearRegression()), ("Ridge(alpha=1)", Ridge(alpha=1.0)), ("Lasso(alpha=0.1)", Lasso(alpha=0.1, max_iter=5000))]:
    m.fit(Xd_tr, yd_tr); yp = m.predict(Xd_te)
    print(name, "MSE=", round(mean_squared_error(yd_te, yp), 2), "MAE=", round(mean_absolute_error(yd_te, yp), 2), "R2=", round(r2_score(yd_te, yp), 4))
las = Lasso(alpha=0.1, max_iter=5000).fit(Xd_tr, yd_tr)
print("Lasso nonzero coef count:", np.count_nonzero(las.coef_), "/", len(las.coef_))
""")

md("""
## Part 3 无监督学习：聚类与降维
""")

code("""
from sklearn.cluster import KMeans, DBSCAN
from sklearn.datasets import make_blobs, make_moons
from sklearn.metrics import silhouette_score, adjusted_rand_score

Xb, _ = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=0)
km = KMeans(n_clusters=4, random_state=0).fit(Xb)
print("KMeans inertia:", round(km.inertia_, 3))
print("KMeans silhouette:", round(silhouette_score(Xb, km.labels_), 4))

Xm, ym = make_moons(n_samples=300, noise=0.1, random_state=42)
db = DBSCAN(eps=0.2, min_samples=5).fit(Xm)
print("DBSCAN n_clusters:", len(set(db.labels_)) - (1 if -1 in db.labels_ else 0))
print("noise ratio:", round(np.mean(db.labels_ == -1), 4))
print("DBSCAN ARI:", round(adjusted_rand_score(ym, db.labels_), 4))
""")

code("""
from sklearn.decomposition import PCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA

pca = PCA(n_components=2)
Xp = pca.fit_transform(X)
print("PCA cum var:", np.round(np.cumsum(pca.explained_variance_ratio_), 4))

lda = LDA(n_components=2)
Xl = lda.fit_transform(X, y)
print("LDA explained var:", np.round(lda.explained_variance_ratio_, 4))
""")

md("""
## Part 4 综合任务：Wine 数据的“预处理 -> 分类 -> 聚类 -> 降维”端到端流程

请参照 04-综合案例.md，完成下面流程，并把最终图保存为 wine_lab_pca.png。
""")

code("""
import matplotlib.pyplot as plt
from sklearn.datasets import load_wine
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.metrics import adjusted_rand_score

wine = load_wine(); Xw, yw = wine.data, wine.target
Xs = StandardScaler().fit_transform(Xw)

lr_pipe = Pipeline([("sc", StandardScaler()), ("clf", LogisticRegression(max_iter=1000))])
rf_pipe = Pipeline([("sc", StandardScaler()), ("clf", RandomForestClassifier(n_estimators=100, random_state=42))])
print("LogisticRegression 5-fold mean:", round(cross_val_score(lr_pipe, Xw, yw, cv=5).mean(), 4))
print("RandomForest 5-fold mean:", round(cross_val_score(rf_pipe, Xw, yw, cv=5).mean(), 4))

kmw = KMeans(n_clusters=3, random_state=42).fit(Xs)
print("KMeans ARI vs true:", round(adjusted_rand_score(yw, kmw.labels_), 4))
print("KMeans cluster sizes:", np.bincount(kmw.labels_))

pca = PCA(n_components=2)
Xp = pca.fit_transform(Xs)
fig, axes = plt.subplots(1, 2, figsize=(10, 4))
axes[0].scatter(Xp[:, 0], Xp[:, 1], c=yw, cmap="viridis", s=22)
axes[0].set_title("PCA by true labels")
axes[1].scatter(Xp[:, 0], Xp[:, 1], c=kmw.labels_, cmap="viridis", s=22)
axes[1].set_title("PCA by KMeans")
for ax in axes:
    ax.set_xlabel("PC1"); ax.set_ylabel("PC2")
fig.tight_layout()
fig.savefig("wine_lab_pca.png", dpi=150)
print("saved wine_lab_pca.png")
""")

md("""
## 提交清单

- [ ] 环境自检通过；
- [ ] Part 1 输出编码/缩放结果，说出 OneHot 与 Label 编码的适用场景；
- [ ] Part 2 记录 4 个分类器准确率，并说明三类指标含义；
- [ ] Part 3 比较 KMeans 与 DBSCAN 在 moons 上的表现并解释原因；
- [ ] Part 4 已保存 wine_lab_pca.png 并写 3 句结论；
- [ ] 导出为 html / 保留 ipynb 提交。

**延伸**：完成 exercises/quiz.ipynb 与 assignment.md；阅读 05-常见误区与技巧.md。
""")

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
                   "chapters", "08-sklearn", "lab", "lab.ipynb")
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