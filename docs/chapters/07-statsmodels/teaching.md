# 第 7 章 教学说明（教师用）

> 面向授课教师：课时建议、重点难点、上机安排、考核建议。学生无需阅读本页。

## 1. 教学目标

- 让学生**读懂统计输出**：会解释 <code>summary()</code> 中的系数、标准误、t 值、P 值、R²、F 检验、JB 统计量；
- 建立“线性模型 + 最小二乘 + 显著性检验”的统一框架（回归 = 广义 ANOVA）；
- 能独立完成：一元/多元回归、单因素方差分析、二分类 Logit、时间序列分解与 ARIMA 预测；
- 具备基本回归诊断意识（残差正态性、异方差、自相关）。

## 2. 建议课时与安排

| 课次 | 内容 | 建议形式 | 依赖 |
| ---- | ---- | ---- | ---- |
| 第 1 次 | 01 前半：OLS 数组接口 + 公式 API + summary 解读 | 讲授 + 课堂演示 | 第 4 章 pandas |
| 第 2 次 | 01 后半：多元回归 + anova_lm + GLM | 讲授 + 上机 | 第 1 次 |
| 第 3 次 | 01 回归诊断 + WLS + 02 时间序列分解 | 讲授 + 上机 | 第 2 次 |
| 第 4 次 | 02 平稳性 + ARIMA + 03 综合案例 | 上机为主 + 讨论 | 第 3 次 |
| 课后 | 04 误区技巧自读；完成 quiz + 作业 | 自主学习 | — |

> 若课时紧张：第 4 次可合并为课堂案例演示；习题改为选做。

## 3. 重点与难点

### 重点
- <code>sm.add_constant</code> 与截距；数组/公式两种接口；
- <code>summary()</code> 各字段含义；P 值与置信区间；
- <code>C(...)</code>、<code>I(...)</code>、交互项公式写法；
- <code>anova_lm</code> 的 F/P 值解读；
- <code>seasonal_decompose</code> 的 period 与模型选择；
- <code>ARIMA</code> 的 <code>(p,d,q)</code> 与 <code>forecast</code>。

### 难点（学生常卡）
- **漏加常数列**：数组接口不自动加截距；
- **公式里 <code>*</code> 的含义**：是主效应+交互，不是数值乘法；
- **GLM predict 返回的是概率**：需要阈值才能判类别；
- **平稳性与差分**：对非平稳序列直接 ARIMA 会“伪回归”；
- **分解/建模前要等间隔、无缺失**：用 <code>dropna()</code> / 插值。

## 4. 上机（lab/）使用建议

- 每 Part 15–20 分钟；要求每格都运行并记录输出；
- Part 9 综合任务可小组完成；
- 教师可在 lab 基础上增加“隐藏检查点”用来回收（如断言 <code>anova_res['PR(>F)'][0] < 0.05</code>）；
- 强调“先 ADF 后 ARIMA”、“先看残差再下结论”。

## 5. 作业与考核建议

- **平时**：exercises 10 道（quiz.ipynb，可手动批改或自动评分）；
- **上机**：lab.ipynb 完成情况 + 03 综合案例拓展；
- **期中/期末融合**：把回归/ANOVA/时间序列并入第 8 章 sklearn 或期末大作业（例如电力负荷预测、销售预测）；
- 鼓励学生用 <code>summary()</code> 写一段 150 字以内的“业务解读”。

## 6. 易错点清单（直接用于出题）

1. 数组接口忘记 <code>add_constant</code>；
2. 公式里 <code>y ~ group</code> 未用 <code>C(group)</code>；
3. <code>GLM.predict</code> 未设阈值当分类；
4. 非平稳序列直接 ARIMA；
5. <code>seasonal_decompose</code> 的 <code>period</code> 设置错误；
6. 忘了差分后 <code>dropna()</code>；
7. 混淆 <code>params</code> 与 <code>bse</code>；
8. 只报 R² 不看 F/P/JB 诊断。

## 7. 资源包

- 讲义正文：<code>01-方差分析与回归.md</code> ~ <code>04-常见误区与技巧.md</code>
- 配图：<code>images/*.png</code>（由 <code>../../build/make_chap7_figures.py</code> 生成）
- 练习：<code>exercises/</code>；上机：<code>lab/</code>；参考：<code>references.md</code>
- 合订 PDF：<code>../../教材PDF/07-Statsmodels及其基本使用.pdf</code>（由 <code>../../build/pdf_build.py</code> 生成）

---

## 课表定位（8 周制）

- 周次：第 7 周
- 上课：2 学时（精讲 + 演示）
- 上机：4 学时（单独排课，以 lab/ 为主，含 0.5h 回顾与 0.5h 总结/quiz）
- 课后：完成 exercises/ 的 quiz 与 assignment；06 常见误区页自学
