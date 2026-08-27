# 2. SymPy 及其基本使用（新版讲义）

> 本页是第 2 章的**章首页（索引）**。正文位于 `01-符号对象与基本运算.md` ~ `04-常见误区与技巧.md`，与原版资料完全分离（原版见 `../../原始资料/chap2/`）。

## 本章概览

SymPy 是 Python 的**符号计算（symbolic computation）**核心库：它不计算具体数值，而是把 $x$、$y$、$\pi$ 当作符号进行解析推导，从而可以**精确**地求极限、导数、积分、化简、解方程与微分方程、处理符号矩阵，并给出数学上的精确解。与 NumPy 的数值解相比，SymPy 能保留 $\frac{1}{3}$、$\sqrt{2}$ 这样的精确形式，也更能反映数学本质。

本章从“如何创建符号对象”开始，逐步过渡到“用 SymPy 求解数学问题”：方程、方程组、微分方程、符号矩阵，最后用综合案例把符号推导与数值验证、可视化串起来。

## 学习目标

学完本章，你应该能够：

1. 创建并理解符号对象（`symbols` / `Symbol`），会使用 `positive`、`real`、`integer` 等假设。
2. 用 SymPy 完成符号的算术运算、表达式化简（`simplify` / `expand` / `factor` / `trigsimp`）与替换求值（`subs` / `evalf` / `N`）。
3. 求符号极限（`limit`）、导数与偏导数（`diff`）、不定/定积分与二重积分（`integrate`）。
4. 解方程与方程组：`solve`、`solveset`、`linsolve`、`nonlinsolve`，并理解 `Eq` 与“表达式=0”的约定。
5. 用 Symbolic `Matrix` 做矩阵运算、特征值、雅可比矩阵，与 NumPy 数值结果互相验证。
6. 用 `lambdify` 把符号表达式转换为可调用的 NumPy 函数，实现“符号推导 → 数值计算”的衔接。
7. 用 `dsolve` 求解一阶/二阶常微分方程及初值问题，并画出解的曲线。
8. 完成一个综合小案例（如符号求面积 + 可视化、符号导数 + 切线图），体会“精确推导 + 数值验证 + 可视化”的完整流程。

## 先修要求与运行环境

- 熟悉 Python 基础语法（变量、函数、循环；可先学 [聪明办法学 Python](https://github.com/datawhalechina/learn-python-the-smart-way-v2)）。
- 了解基本的微积分与线性代数概念（极限、导数、积分、矩阵、特征值）。
- 安装 Python 3.10+ 与 SymPy（同时建议安装 NumPy 与 Matplotlib，便于数值验证与画图）：

```bash
pip install sympy
# 若需要数值验证/可视化，再加装
pip install numpy matplotlib scipy pandas
```

> 本机已验证：Python 3.13.5，SymPy 1.13.1，NumPy 2.1.2，Matplotlib 3.10.1。统计学建模库 statsmodels 0.14.6 也已可用（本章不使用，后续章节再用）。

## 本章目录

| 小节 | 文件 | 内容 |
| ---- | ---- | ---- |
| 01 符号对象与基本运算 | [01-符号对象与基本运算.md](./01-符号对象与基本运算.md) | 符号创建、假设、算术、函数、极限、导数、积分、化简与替换 |
| 02 利用 SymPy 求解问题 | [02-利用SymPy求解问题.md](./02-利用SymPy求解问题.md) | Eq、solve/solveset/linsolve/nonlinsolve、符号矩阵、lambdify、dsolve |
| 03 综合案例 | [03-综合案例.md](./03-综合案例.md) | 符号求面积 + 可视化、符号导数 + 切线图、根的可视化（图文案例） |
| 04 常见误区与技巧 | [04-常见误区与技巧.md](./04-常见误区与技巧.md) | 易错点清单、性能技巧、调试建议 |

## 练习与上机入口

- [本章练习（exercises/）](./exercises/README.md)：作业题、自测 quiz、参考答案（从历史 `chapter_2_3_quiz` 整理出 SymPy 部分）。
- [本章上机（lab/）](./lab/README.md)：循序渐进的上机 notebook，含综合任务与检查清单。
- [本章参考与延伸阅读（references.md）](./references.md)：官方文档、精品教程、习题集、中文资料。
- [教学说明（teaching.md）](./teaching.md)：课时安排、重点难点、考核建议（教师用）。

## 建议课时

| 环节 | 学时 | 对应内容 |
| ---- | ---- | ---- |
| 讲课 | 3–4 学时 | 01–02 正文 + 03 案例讲解 |
| 上机 | 2–3 学时 | lab/ 逐题完成；课后完成 exercises/ 作业 |

## 使用说明

- **学生**：先读 01–02 正文并运行代码 → 完成 lab 上机 → 提交 exercises 作业 → 自测 quiz 检验。生词/公式不懂时，到 references.md 找官方对应章节。
- **教师**：按 teaching.md 的课时表讲；lab 可作为上机课内容；exercises 中的 quiz 带自动评分，可直接回收。
