# 第 5 章 作业题（Matplotlib / Seaborn）

> 本题 14 道，覆盖基础绘图、布局排版、Seaborn 美化与综合应用。每题给出提示与答案要点；完整可运行代码见 `answers.ipynb`。

## 题 1（易）：基础折线图

用 `np.linspace` 生成 `x`，绘制 `y = sin(x)` 折线图，并加上标题、`x`/`y` 轴标签。

**答案要点**：`plt.plot(x, y)`；`plt.title('sin(x)')`；`plt.xlabel('x')`；`plt.ylabel('y')`。

## 题 2（易）：多条曲线与图例、网格

在同一张图绘制 `sin` 与 `cos` 两条曲线，加 `label`、`legend()` 与 `grid(True)`。

**答案要点**：`ax.plot(x, np.sin(x), label='sin')`；`ax.plot(x, np.cos(x), label='cos')`；`ax.legend()`；`ax.grid(True)`。

## 题 3（易）：坐标范围与刻度

设置 `xlim=(0,4)`、`ylim=(2,6)`，并把 `x` 轴刻度设为 `[0,1,2,3]`。

**答案要点**：`ax.set_xlim(0, 4)`；`ax.set_ylim(2, 6)`；`ax.set_xticks([0,1,2,3])`。

## 题 4（易）：样式参数

绘制一条绿色、线宽 2、虚线、方块标记、标记大小 10 的曲线。

**答案要点**：`ax.plot(..., color='green', lw=2, ls='--', marker='s', ms=10)`。

## 题 5（易）：2×2 子图

用 `plt.subplots(2, 2, figsize=(8,6))` 创建子图，在每个子图画一条线，最后 `fig.tight_layout()`。

**答案要点**：`for ax in axs.flat: ax.plot(...)`；`fig.tight_layout()`。

## 题 6（易）：保存图像

创建 `figsize=(6,4), dpi=120` 的图窗，画线并保存为 `quiz_q6.png`。

**答案要点**：`plt.savefig('quiz_q6.png', dpi=150)`。

## 题 7（中）：直方图（density）

用 `default_rng(0)` 生成 300 个标准正态数，绘制 `bins=20`、`density=True` 的直方图。

**答案要点**：`counts, bins, patches = ax.hist(data, bins=20, density=True)`。

## 题 8（中）：中文字体

设置全局字体为 `Microsoft YaHei` / `SimHei`，并让负号正常显示，画一张带中文标题的图。

**答案要点**：`mpl.rcParams['font.sans-serif'] = ['Microsoft YaHei','SimHei','DejaVu Sans']`；`mpl.rcParams['axes.unicode_minus'] = False`。

## 题 9（中）：饼图

绘制 A/B/C/D 四个扇区、占比 `[15,30,45,10]`、`startangle=140` 的饼图，并显示百分比。

**答案要点**：`wedges, texts, autotexts = ax.pie(...)`；`autopct='%1.1f%%'`。

## 题 10（中）：Seaborn 直方图 + KDE

加载 `tips`，用 `sns.histplot(data=tips, x='total_bill', kde=True, ax=ax)` 绘制。

**答案要点**：`sns.histplot(...)` 返回 `Axes`；记得在 `sns.set_theme` 后重设中文字体。

## 题 11（中）：Seaborn 箱线图与提琴图

用 `tips` 画 `day` 分组的 `boxplot` 与 `violinplot` 对比图（1×2 子图）。

**答案要点**：`sns.boxplot(data=tips, x='day', y='total_bill', ax=axes[0])`；`sns.violinplot(..., ax=axes[1])`。

## 题 12（中）：Seaborn 热力图

用随机 5×5 矩阵绘制 `sns.heatmap`，`fmt='.2f'`，`cmap='coolwarm'`。

**答案要点**：`sns.heatmap(data, annot=True, fmt='.2f', cmap='coolwarm', ax=ax)`。

## 题 13（难）：FacetGrid 分面

加载 `tips`，用 `FacetGrid(col='day', col_wrap=2)` 并按 `total_bill`/`tip` 画散点图。

**答案要点**：`g = sns.FacetGrid(tips, col='day', col_wrap=2); g.map(sns.scatterplot, 'total_bill', 'tip')`。

## 题 14（综合）：数据报告图

生成一段噪声正弦信号，在一个子图里画“原始 + 平滑”曲线并加图例；在另一个子图用 Seaborn 画幅值直方图 + KDE（1×2 子图）。

**答案要点**：`smooth = pd.Series(y).rolling(window=9, center=True).mean()`；`fig, axes = plt.subplots(1, 2, figsize=(10,4))`；上 `plot`、下 `sns.histplot(..., ax=axes[1])`。

## 评分建议

- 每题按“能运行 + 关键参数正确”给分；
- 题 1–6 每题 1 分，题 7–12 每题 1.5 分，题 13–14 每题 2 分，满分 19 分。
