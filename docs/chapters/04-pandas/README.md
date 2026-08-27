# 4. Pandas 及其基本使用（新版讲义）

> 本页是第 4 章的**章首页（索引）**。正文位于 01-基础数据结构.md ~ 04-常见误区与技巧.md，与原版资料完全分离（原版见 ../../原始资料/chap4/）。

## 本章概览

Pandas 是 Python 数据分析的事实标准：它以 `Series`（一维带标签数组）和 `DataFrame`（二维表格）两种核心结构，把 Excel/SQL 式的“表格数据操作”搬到编程环境里。它建立在 NumPy 之上，既保留向量化运算的高性能，又提供索引、筛选、分组、透视、缺失值处理、时间序列等丰富能力。本章先讲清两种基础数据结构的创建与索引，再介绍数据清洗（重复/缺失/异常值）、数据规约（Min-Max / Z-Score）、统计描述、分组聚合、透视表与时间序列，最后用综合案例把知识串起来。

## 学习目标

学完本章，你应该能够：

1. 熟练创建并操作 `Series` 与 `DataFrame`，理解 `index`、`columns`、`dtype`、`shape` 等属性。
2. 正确区分 `.loc`（按标签）与 `.iloc`（按位置），并能用布尔索引（`&`/`|`/`~`）做复杂筛选。
3. 完成数据清洗：去重（`drop_duplicates`）、缺失值处理（`isna`/`fillna`/`dropna`/`ffill`/`bfill`）、用 IQR 识别并处理异常值。
4. 掌握数据规约：Min-Max 归一化与 Z-Score 标准化，并能说出适用场景。
5. 会用 `describe`、`groupby`、`agg`、`pivot_table`、`merge`/`concat` 做统计、分组与透视分析。
6. 会用 `date_range`、`resample`、`rolling` 处理时间序列数据，并能用 matplotlib 把分析结果可视化。

## 先修要求与运行环境

- 熟悉 Python 基础语法与 NumPy（第 1 章）；建议先学 [聪明办法学 Python](https://github.com/datawhalechina/learn-python-the-smart-way-v2) 与第 1 章 numpy。
- 安装 Python 3.10+ 与 Pandas：

```bash
pip install pandas numpy matplotlib
# 需要读写 Excel 时再装
pip install openpyxl xlrd
```

- 推荐在 JupyterLab / VS Code 中打开 .ipynb 练习；命令行列出的脚本直接保存为 .py 运行即可。

## 本章目录

| 小节 | 文件 | 内容 |
| ---- | ---- | ---- |
| 01 基础数据结构 | [01-基础数据结构.md](./01-基础数据结构.md) | Series 创建/访问/运算、DataFrame 创建/索引/切片/筛选、date_range |
| 02 数据分析 | [02-数据分析.md](./02-数据分析.md) | 重复/缺失/异常值、规约、统计描述、groupby、pivot_table、时间序列 |
| 03 综合案例 | [03-综合案例.md](./03-综合案例.md) | 学生成绩分析：清洗→分组/透视→可视化（3 张配图） |
| 04 常见误区与技巧 | [04-常见误区与技巧.md](./04-常见误区与技巧.md) | 易错点表、loc/iloc 辨析、性能与调试、自测清单 |

## 练习与上机入口

- [本章练习（exercises/）](./exercises/README.md)：作业题（15 题）、自测 quiz（25 题）、参考答案。
- [本章上机（lab/）](./lab/README.md)：循序渐进的上机 notebook，含综合任务与检查清单。
- [本章参考与延伸阅读（references.md）](./references.md)：官方文档、精品教程、习题集、中文资料。
- [教学说明（teaching.md）](./teaching.md)：课时安排、重点难点、考核建议（教师用）。

## 建议课时

| 环节 | 学时 | 对应内容 |
| ---- | ---- | ---- |
| 讲课 | 3–4 学时 | 01–02 正文 + 03 案例讲解 |
| 上机 | 2–3 学时 | lab/ 逐题完成；课后完成 exercises/ 作业 |

## 使用说明

- **学生**：先读 01–02 正文并运行代码 → 完成 lab 上机 → 提交 exercises 作业 → 自测 quiz 检验。遇到 `loc`/`iloc`、`fillna` 等细节时，回看 01/02 正文，或到 references.md 找官方章节。
- **教师**：按 teaching.md 的课时表讲；lab 可作为上机课内容；exercises 中的 quiz 已整理为 Pandas 专项，可直接回收；03 综合案例配图用于课堂演示。