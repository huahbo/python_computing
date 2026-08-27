# -*- coding: utf-8 -*-
"""Generate lab.ipynb for chapter 04 (Pandas) — guided lab notebook."""
import json, os

cells = []
def md(text):
    cells.append({"cell_type": "markdown", "metadata": {}, "source": text})
def code(text):
    cells.append({"cell_type": "code", "metadata": {}, "execution_count": None,
                  "outputs": [], "source": text})

md("""# Pandas 上机实验（第 4 章 lab）

**要求**：按顺序运行每一格，完成所有 TODO 后运行「检查」单元；最后导出 notebook 提交。
环境：Python 3.10+，pandas ≥ 2.0（推荐 2.2+），numpy ≥ 1.24，matplotlib ≥ 3.7。

---
""")

code("""import pandas as pd
import numpy as np
print("pandas:", pd.__version__)
print("numpy :", np.__version__)
assert pd.__version__ >= "2.0", "请升级 pandas"
print("环境 OK")
""")

md("""## Part 1 Series 与 DataFrame 创建

练习：用列表 / NumPy 数组 / 字典创建 Series 和 DataFrame，并查看基本属性。""")

code("""# TODO 1.1 Series
s = pd.Series([10, 20, 30, 40], index=["a", "b", "c", "d"])
print(s)
print("index:", s.index.tolist(), "values:", s.values.tolist())
print("s['b']:", s["b"])
print("s.iloc[1]:", s.iloc[1])
""")

code("""# TODO 1.2 DataFrame
df = pd.DataFrame({"姓名": ["张三", "李四", "王五"],
                   "语文": [85, 90, 78],
                   "数学": [92, 88, 95]},
                  index=["r0", "r1", "r2"])
print(df)
print("shape:", df.shape, "columns:", df.columns.tolist())
print("df.loc['r1','数学']:", df.loc["r1", "数学"])
print("df.iloc[1,1]:", df.iloc[1, 1])
""")

md("""## Part 2 索引、切片与条件筛选

练习：`.loc` 按标签、`.iloc` 按位置；布尔索引组合 `&` / `|` / `~`。""")

code("""# TODO 2.1 loc / iloc
df = pd.DataFrame({"A": [1, 2, 3, 4, 5],
                   "B": [10, 20, 30, 40, 50],
                   "C": ["a", "b", "a", "b", "c"]})
print("loc 第0行:", df.loc[0].to_dict())
print("iloc 前2行:", df.iloc[:2].to_dict("records"))
print("loc 行0-1,列A-C:", df.loc[0:1, ["A", "C"]].to_dict("records"))
""")

code("""# TODO 2.2 布尔筛选
f1 = df[(df["A"] > 2) & (df["B"] < 50)]
f2 = df[(df["A"] > 3) | (df["C"] == "b")]
f3 = df[~ (df["C"] == "a")]
print("A>2 且 B<50:")
print(f1)
print("A>3 或 C=='b':")
print(f2)
print("C 不为 'a':")
print(f3)
""")

md("""## Part 3 重复、缺失与异常值

练习：`drop_duplicates`、`isna`/`fillna`/`dropna`、用 IQR 找异常值并替换。""")

code("""# TODO 3.1 重复与缺失
df = pd.DataFrame({"A": [1, 2, 2, np.nan, 4, 4],
                   "B": [10, 20, 20, 30, np.nan, 40]})
print("原表:")
print(df)
print("重复行数:", df.duplicated().sum())
print("缺失值:")
print(df.isna().sum())
print("dropna():")
print(df.dropna())
print("ffill():")
print(df.ffill())
print("fillna(0):")
print(df.fillna(0))
""")

code("""# TODO 3.2 用 IQR 处理异常值
df = pd.DataFrame({"Value": [1, 2, 3, 4, 5, 6, 100]})
Q1 = df["Value"].quantile(0.25)
Q3 = df["Value"].quantile(0.75)
IQR = Q3 - Q1
lo, hi = Q1 - 1.5 * IQR, Q3 + 1.5 * IQR
mask = (df["Value"] < lo) | (df["Value"] > hi)
print("Q1,Q3,IQR:", Q1, Q3, IQR, "界限:", lo, hi)
print("异常值:", df.loc[mask, "Value"].tolist())
df.loc[mask, "Value"] = df["Value"].median()
print("替换后:")
print(df)
""")

md("""## Part 4 分组与透视

练习：`groupby` 聚合、`pivot_table`。""")

code("""# TODO 4.1 groupby
df = pd.DataFrame({"班级": ["A", "B", "A", "B", "C", "A"],
                   "科目": ["语文", "数学", "数学", "语文", "英语", "英语"],
                   "分数": [85, 90, 88, 78, 70, 92]})
g = df.groupby("班级")["分数"].agg(["mean", "sum", "count"])
print(g)
print("分数均值 > 85 的组:")
print(g[g["mean"] > 85])
""")

code("""# TODO 4.2 pivot_table
pt = df.pivot_table(values="分数", index="班级", columns="科目", aggfunc="mean", fill_value=0)
print(pt)
""")

md("""## Part 5 数据规约与统计描述

练习：Min-Max、Z-Score、describe。""")

code("""# TODO 5.1 规约
df = pd.DataFrame({"feature": [1, 2, 3, 4, 5]})
df["minmax"] = (df["feature"] - df["feature"].min()) / (df["feature"].max() - df["feature"].min())
df["zscore"] = (df["feature"] - df["feature"].mean()) / df["feature"].std()
print(df)
print("zscore 均值(≈0):", df["zscore"].mean(), "标准差(≈1):", df["zscore"].std())
""")

code("""# TODO 5.2 describe
df2 = pd.DataFrame({"A": [1, 2, 3, 4, 5], "B": [10, 20, 30, 40, 50]})
print(df2.describe())
""")

md("""## Part 6 时间序列：date_range / resample / rolling

练习：生成日期索引，做周重采样与 7 日移动平均。""")

code("""# TODO 6.1 时间序列基础
rng = np.random.default_rng(0)
idx = pd.date_range("2023-01-01", periods=30, freq="D")
ts = pd.Series(rng.normal(50, 5, 30), index=idx)
print("前 5 项:")
print(ts.head())
print("resample('W').mean() 前 3 项:")
print(ts.resample("W").mean().head(3))
print("rolling(7).mean() 最后 3 项:")
print(ts.rolling(7).mean().tail(3))
""")

md("""## Part 7 综合任务：学生成绩分析与可视化

把 Parts 1–6 串起来：造数据 → 清洗 → 分组透视 → matplotlib 画图。""")

code("""# TODO 7.1 综合任务（可参考 ../03-综合案例.md）
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei", "DejaVu Sans"]
matplotlib.rcParams["axes.unicode_minus"] = False
rng = np.random.default_rng(42)
classes = ["一班", "二班", "三班"]
subjects = ["语文", "数学", "英语"]
rows = []
for i in range(1, 21):
    cls = classes[i % 3]
    base = {"一班": 82, "二班": 78, "三班": 85}[cls]
    for sub in subjects:
        rows.append({"学号": f"S{i:02d}", "姓名": f"学生{i:02d}",
                     "班级": cls, "科目": sub,
                     "分数": round(rng.normal(base, 6), 1)})
df = pd.DataFrame(rows)
df.loc[2, "分数"] = np.nan
df.loc[5, "分数"] = np.nan
df = pd.concat([df, df.iloc[[1]].copy()], ignore_index=True)

df = df.dropna(subset=["分数"]).drop_duplicates()
Q1, Q3 = df["分数"].quantile([0.25, 0.75])
IQR = Q3 - Q1
mask = (df["分数"] < Q1 - 1.5 * IQR) | (df["分数"] > Q3 + 1.5 * IQR)
df.loc[mask, "分数"] = df["分数"].median()

piv = df.pivot_table(values="分数", index="班级", columns="科目", aggfunc="mean").round(1)
print(piv)

fig, ax = plt.subplots(figsize=(7, 3.8))
np_x = np.arange(len(piv.index))
for j, sub in enumerate(subjects):
    vals = piv[sub].values
    ax.bar(np_x + (j - 1) * 0.25, vals, width=0.25, label=sub,
           color=["#2f6fb3", "#e07b39", "#3a8f4f"][j])
ax.set_xticks(np_x); ax.set_xticklabels(piv.index)
ax.set_ylabel("平均分"); ax.set_title("各班各科平均分")
ax.legend(); ax.grid(axis="y", alpha=0.25)
plt.tight_layout()
plt.savefig("case_scores_lab.png")
print("已保存 case_scores_lab.png")
""")

md("""## 提交清单

- [ ] 所有 TODO 均已填写并运行；
- [ ] Part 2 的三个布尔筛选结果已输出；
- [ ] Part 3 的 IQR 异常值处理已输出；
- [ ] Part 6 的 resample / rolling 结果已输出；
- [ ] Part 7 已生成 case_scores_lab.png 并写 3 句结论；
- [ ] 导出为 html / 保留 ipynb 提交。

**延伸**：完成 exercises/ 的 quiz 与 assignment；阅读 ../06-常见误区与技巧.md。""")

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
                   "chapters", "04-pandas", "lab", "lab.ipynb")
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