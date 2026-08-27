# 5. Matplotlib 及其基本使用（新版讲义）

> 本页是第 5 章的**章首页（索引）**。正文位于 `01-基本绘图.md` ~ `05-常见误区与技巧.md`，与原版资料完全分离（原版见 `../../原始资料/chap5/`）。

## 本章概览

Matplotlib 是 Python 科学计算中最常用的可视化库：它把“数据→图形”变成一系列可组合的对象（Figure、Axes、Label、Line、Patch），支持折线图、散点图、条形图、直方图、箱线图、饼图、热力图、3D 图等。Seaborn 则在其上封装了更贴统计学语境的接口与主题，用于快速完成带分组的统计图形。本章将带你从“画出第一条线”走到“用 Seaborn 做一组带分面/分组的统计报告图”，为后续 Pandas、Statsmodels、sklearn 各章的图表输出打下基础。

## 学习目标

学完本章，你应该能够：

1. 使用 `matplotlib.pyplot` 绘制折线图、散点图、条形图、饼图、直方图、箱线图、热力图与误差棒图；
2. 理解 Figure/Axes 对象模型，会用 `plt.subplots` 创建并管理多子图，调整 `figsize/dpi/tight_layout/subplots_adjust`；
3. 设置全局与局部字体、标题、轴标签、刻度、范围、网格、图例，以及颜色/线型/线宽/标记等样式参数；
4. 用 `plt.savefig` 输出高分辨率图片，并知道常见图片格式与 DPI 语义；
5. 使用 Seaborn 的内置主题、`histplot`、`boxplot`、`violinplot`、`heatmap`、`FacetGrid` 与 `pairplot` 快速做统计可视化；
6. 完成一个“绘图最佳实践”综合案例，把多子图、样式、平滑与分组分析、相关矩阵热力图串起来。

## 先修要求与运行环境

- 熟悉 Python 基础语法；熟悉 NumPy 数组；了解 Pandas 的 DataFrame 会更轻松（第 4 章内容）。
- 安装 Python 3.10+ 与可视化相关库：

```bash
pip install matplotlib seaborn pandas numpy
# 若需要做更多统计图（本教材第 7 章会用到），可再加装
pip install statsmodels
```

- 示例数据集（tips / flights）由 Seaborn 内置，首次使用会自动下载；请确保能访问 GitHub 或在本地已缓存。

## 本章目录

| 小节 | 文件 | 内容 |
| ---- | ---- | ---- |
| 01 基本绘图 | [01-基本绘图.md](./01-基本绘图.md) | 折线/散点/条形/饼图/直方图/箱线图/热力图/误差棒/极坐标/3D/等高线 |
| 02 图窗布局与排版 | [02-图窗布局与排版.md](./02-图窗布局与排版.md) | Figure/Axes、subplots、figsize/dpi、字体、坐标轴、网格、图例、savefig |
| 03 Seaborn 美化 | [03-Seaborn美化.md](./03-Seaborn美化.md) | 主题、统计图、FacetGrid/PairGrid、heatmap 等 |
| 04 综合案例 | [04-综合案例.md](./04-综合案例.md) | 传感器信号分析报告图（多子图+Seaborn） |
| 05 常见误区与技巧 | [05-常见误区与技巧.md](./05-常见误区与技巧.md) | 高频易错点、性能/调试/自测清单 |

## 练习与上机入口

- [本章练习（exercises/）](./exercises/README.md)：作业题、自测 quiz（14 题、自动评分）、参考答案。
- [本章上机（lab/）](./lab/README.md)：循序渐进的上机 notebook，含综合任务与检查清单。
- [本章参考与延伸阅读（references.md）](./references.md)：官方文档、精品教程、习题集、中文资料。
- [教学说明（teaching.md）](./teaching.md)：课时安排、重点难点、考核建议（教师用）。

## 建议课时

| 环节 | 学时 | 对应内容 |
| ---- | ---- | ---- |
| 讲课 | 3–4 学时 | 01–03 正文 + 04 案例讲解 |
| 上机 | 2–3 学时 | lab/ 逐题完成；课后完成 exercises/ 作业 |

## 使用说明

- **学生**：先读 01–03 正文并运行代码 → 完成 lab 上机 → 提交 exercises 作业 → 自测 quiz 检验。遇到中文字体问题时，用正文第 2 节的 `rcParams` 设置。
- **教师**：按 teaching.md 的课时表讲；lab 可作为上机课内容；exercises 中的 quiz 带自动评分，可直接回收。
