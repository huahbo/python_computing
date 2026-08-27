# -*- coding: utf-8 -*-
"""Generate quiz.ipynb / answers.ipynb for chapter 05 (Matplotlib)."""
import json, os

BASE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                    "chapters", "05-matplotlib", "exercises")
os.makedirs(BASE, exist_ok=True)

QUESTIONS = [
("导入与创建图窗",
 "使用 import matplotlib.pyplot as plt，创建 figure 并添加一个子图。",
 """import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(111)
""",
 """total += 2
try:
    from matplotlib.figure import Figure
    assert isinstance(fig, Figure)
    assert len(fig.axes) == 1
    score += 2
    print("Q1: 2 / 2")
except Exception as e:
    print("Q1: 0 / 2", repr(e))
"""),

("折线图 + 标题/轴标签",
 "用 np.linspace 生成 x，绘制 y=sin(x) 折线图，并设置标题、x 轴与 y 轴标签。",
 """import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_title("sin(x)")
ax.set_xlabel("x")
ax.set_ylabel("y")
""",
 """total += 2
try:
    assert ax.get_title() == "sin(x)"
    assert ax.get_xlabel() == "x"
    assert ax.get_ylabel() == "y"
    score += 2
    print("Q2: 2 / 2")
except Exception as e:
    print("Q2: 0 / 2", repr(e))
"""),

("图例与网格",
 "同图绘制 sin 与 cos 两条曲线并加 label，调用 legend() 与 grid(True)。",
 """import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 2 * np.pi, 100)
fig, ax = plt.subplots()
ax.plot(x, np.sin(x), label="sin")
ax.plot(x, np.cos(x), label="cos")
ax.legend()
ax.grid(True)
""",
 """total += 2
try:
    texts = [t.get_text() for t in ax.get_legend().get_texts()]
    assert "sin" in texts and "cos" in texts
    assert any(g.get_visible() for g in ax.xaxis.get_gridlines())
    score += 2
    print("Q3: 2 / 2")
except Exception as e:
    print("Q3: 0 / 2", repr(e))
"""),

("坐标范围与刻度",
 "设置 xlim=(0,4)，ylim=(2,6)，并把 x 轴刻度设为 [0,1,2,3]。",
 """import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.plot([1, 2, 3], [4, 5, 6])
ax.set_xlim(0, 4)
ax.set_ylim(2, 6)
ax.set_xticks([0, 1, 2, 3])
""",
 """total += 2
try:
    assert ax.get_xlim() == (0, 4)
    assert ax.get_ylim() == (2, 6)
    assert list(ax.get_xticks()) == [0, 1, 2, 3]
    score += 2
    print("Q4: 2 / 2")
except Exception as e:
    print("Q4: 0 / 2", repr(e))
"""),

("颜色/线宽/线型/标记",
 "绘制一条绿色、线宽 2、虚线、方块标记、标记大小 10 的曲线。",
 """import matplotlib.pyplot as plt
fig, ax = plt.subplots()
line, = ax.plot([1, 2, 3], [4, 5, 6],
                color="green", linewidth=2, linestyle="--",
                marker="s", markersize=10)
""",
 """total += 2
try:
    assert line.get_color() == "green"
    assert line.get_linewidth() == 2
    assert line.get_linestyle() == "--"
    assert line.get_marker() == "s"
    score += 2
    print("Q5: 2 / 2")
except Exception as e:
    print("Q5: 0 / 2", repr(e))
"""),

("2×2 子图与 tight_layout",
 "用 plt.subplots(2,2, figsize=(8,6)) 创建子图并在每个子图画一条线，最后调用 tight_layout。",
 """import matplotlib.pyplot as plt
fig, axs = plt.subplots(2, 2, figsize=(8, 6))
for ax in axs.flat:
    ax.plot([1, 2], [2, 1])
fig.tight_layout()
""",
 """total += 2
try:
    assert axs.shape == (2, 2)
    assert len(axs.flat) == 4
    assert fig.get_figwidth() == 8
    score += 2
    print("Q6: 2 / 2")
except Exception as e:
    print("Q6: 0 / 2", repr(e))
"""),

("图窗大小与保存图像",
 "创建 figsize=(6,4), dpi=120 的图窗，画线并保存为 quiz_q7.png。",
 """import matplotlib.pyplot as plt
plt.figure(figsize=(6, 4), dpi=120)
plt.plot([1, 2, 3], [4, 5, 6])
plt.savefig("quiz_q7.png", dpi=150)
""",
 """total += 2
try:
    import os
    assert os.path.exists("quiz_q7.png")
    score += 2
    print("Q7: 2 / 2")
except Exception as e:
    print("Q7: 0 / 2", repr(e))
"""),

("直方图（density）",
 "用 np.random.default_rng(0) 生成 300 个标准正态数，绘制 bins=20、density=True 的直方图。",
 """import numpy as np
import matplotlib.pyplot as plt
rng = np.random.default_rng(0)
data = rng.normal(0, 1, 300)
fig, ax = plt.subplots()
counts, bins, patches = ax.hist(data, bins=20, density=True)
""",
 """total += 2
try:
    assert len(patches) == 20
    assert all(d > 0 for d in np.diff(bins))
    score += 2
    print("Q8: 2 / 2")
except Exception as e:
    print("Q8: 0 / 2", repr(e))
"""),

("饼图",
 "绘制包含 A/B/C/D 四个扇区、占比 [15,30,45,10]、startangle=140 的饼图，并带百分比标注。",
 """import matplotlib.pyplot as plt
labels = ["A", "B", "C", "D"]
sizes = [15, 30, 45, 10]
fig, ax = plt.subplots()
wedges, texts, autotexts = ax.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=140)
""",
 """total += 2
try:
    assert len(wedges) == 4
    assert len(texts) == 4
    score += 2
    print("Q9: 2 / 2")
except Exception as e:
    print("Q9: 0 / 2", repr(e))
"""),

("Seaborn 直方图+KDE",
 "加载 tips 数据集，用 sns.histplot(data=tips, x='total_bill', kde=True, ax=ax) 绘制。",
 """import seaborn as sns
import matplotlib.pyplot as plt
tips = sns.load_dataset("tips")
fig, ax = plt.subplots()
sns.histplot(data=tips, x="total_bill", kde=True, ax=ax)
""",
 """total += 2
try:
    assert hasattr(ax, "plot")
    assert len(ax.patches) > 0
    score += 2
    print("Q10: 2 / 2")
except Exception as e:
    print("Q10: 0 / 2", repr(e))
"""),

("Seaborn 箱线图",
 "用 sns.boxplot(data=tips, x='day', y='total_bill', ax=ax) 绘制箱线图。",
 """import seaborn as sns
import matplotlib.pyplot as plt
tips = sns.load_dataset("tips")
fig, ax = plt.subplots()
sns.boxplot(data=tips, x="day", y="total_bill", ax=ax)
""",
 """total += 2
try:
    assert len(ax.containers) > 0
    score += 2
    print("Q11: 2 / 2")
except Exception as e:
    print("Q11: 0 / 2", repr(e))
"""),

("Seaborn 热力图",
 "用随机 5×5 矩阵绘制 sns.heatmap，fmt='.2f'，cmap='coolwarm'。",
 """import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
rng = np.random.default_rng(1)
data = rng.normal(0, 1, (5, 5))
fig, ax = plt.subplots()
sns.heatmap(data, annot=True, fmt=".2f", cmap="coolwarm", ax=ax)
""",
 """total += 2
try:
    assert len(ax.collections) > 0 or len(ax.images) > 0
    score += 2
    print("Q12: 2 / 2")
except Exception as e:
    print("Q12: 0 / 2", repr(e))
"""),

("Seaborn FacetGrid",
 "加载 tips，用 sns.FacetGrid(col='day', col_wrap=2) 生成并 map(scatterplot, 'total_bill', 'tip')。",
 """import seaborn as sns
tips = sns.load_dataset("tips")
g = sns.FacetGrid(tips, col="day", col_wrap=2, height=2.5)
g.map(sns.scatterplot, "total_bill", "tip")
""",
 """total += 3
try:
    from seaborn.axisgrid import FacetGrid
    assert isinstance(g, FacetGrid)
    score += 3
    print("Q13: 3 / 3")
except Exception as e:
    print("Q13: 0 / 3", repr(e))
"""),

("综合应用：1×2 子图",
 "生成噪声正弦信号，在一个子图画原始与平滑曲线并加图例；在另一个子图用 seaborn 画幅值直方图+KDE。",
 """import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
rng = np.random.default_rng(3)
t = np.linspace(0, 10, 200)
y = np.sin(t) + rng.normal(0, 0.1, 200)
smooth = pd.Series(y).rolling(window=9, center=True).mean().to_numpy()
fig, axes = plt.subplots(1, 2, figsize=(10, 4))
axes[0].plot(t, y, alpha=0.6, label="raw")
axes[0].plot(t, smooth, label="smooth")
axes[0].legend()
sns.histplot(x=y, kde=True, ax=axes[1])
""",
 """total += 3
try:
    assert len(fig.axes) == 2
    assert len(axes[0].lines) == 2
    assert len(axes[1].patches) > 0
    score += 3
    print("Q14: 3 / 3")
except Exception as e:
    print("Q14: 0 / 3", repr(e))
"""),
]

def md(text): return {"cell_type": "markdown", "metadata": {}, "source": text}
def code(text): return {"cell_type": "code", "metadata": {}, "execution_count": None,
                         "outputs": [], "source": text}

def build(is_answer):
    cells = []
    title = "Matplotlib 习题自测（第 5 章）" + ("（参考答案版）" if is_answer else "（学生提交版）")
    cells.append(md("# " + title + """

**说明**：共 14 题，覆盖基础绘图、布局排版、Seaborn 美化与综合应用。
每题：题目 → 隐藏提示（点击展开） → 答案代码单元 → 自动测试单元。
完成全部后运行最后的汇总单元查看得分。

---
"""))
    cells.append(code("""# 自动评分初始化
score = 0
total = 0
"""))
    for i, (title, hint, answer, test) in enumerate(QUESTIONS, start=1):
        cells.append(md("### 题 {}（{}）\n\n".format(i, title) + hint + """

<details><summary>提示（点击展开）</summary>

""" + hint + """

</details>

"""))
        if is_answer:
            cells.append(code(answer))
        else:
            cells.append(code("# --- 请在此处填写代码 ---\n# 示例：\n# import matplotlib.pyplot as plt\n# ...\n\n# TODO: 实现题目要求\n\npass"))
        cells.append(code("# 题 {} 自动测试（{} 分）\n".format(i, "3" if i >= 13 else "2") + test))
    cells.append(md("## 汇总与自测\n\n运行下面的单元查看成绩。"))
    cells.append(code("""# 汇总
print("总分:", score, "/", total)
if total:
    print("得分率: %.1f%%" % (100 * score / total))
"""))
    return cells

for is_answer, fname in [(False, "quiz.ipynb"), (True, "answers.ipynb")]:
    cells = build(is_answer)
    nb = {"cells": cells,
          "metadata": {"kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
                       "language_info": {"name": "python", "version": "3.10"}},
          "nbformat": 4, "nbformat_minor": 5}
    out = os.path.join(BASE, fname)
    with open(out, "w", encoding="utf-8") as f:
        json.dump(nb, f, ensure_ascii=False, indent=1)
    print("saved", out, "cells:", len(cells))
