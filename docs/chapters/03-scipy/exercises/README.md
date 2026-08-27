# 第 3 章 练习题（exercises/）

> 本章练习的**唯一入口**。原有历史 quiz（SymPy+SciPy 混合）保存在 `../../chapter_2_3_quiz/`，已整理为本章 SciPy 专用 16 题自动评分版。

## 文件说明

| 文件 | 用途 | 说明 |
| ---- | ---- | ---- |
| `assignment.md` | 作业题（16 题） | 覆盖积分、ODE、求根、极值、线性规划、指派、曲线拟合、插值、统计检验、FFT、滤波；含详细答案解析 |
| `quiz.ipynb` | 学生自测/提交版 | 题面 + 空白答案单元 + **自动评分**（`_GRADES`） |
| `answers.ipynb` | 教学答案版 | 每题含提示 + 可展开答案 + 自动评分 |

## 使用方法

1. **作业**：打开 `quiz.ipynb`，按题号完成 `YOUR ANSWER HERE` 单元，运行全部单元后查看 `_GRADES` 汇总。
2. **自测**：先不看答案完成 `assignment.md` 的 16 题，再用 `answers.ipynb` 对照。
3. **课堂**：教师可用 `answers.ipynb` 现场演示；每题自带提示与自动测试。

## 建议完成顺序

1. 读 01–05 正文 → 2. `lab/` 上机 → 3. 做 `assignment.md` 1–6（易） → 4. 7–12（中） → 5. 13–16（中偏难/挑战）。

## 题目范围（16 题）

| 题号 | 知识点 | 难度 |
| ---- | ---- | ---- |
| 1–3 | 数值积分与 ODE | easy |
| 4–9 | 求根、极值、线性规划、指派、curve_fit、minimize | easy–medium |
| 10–11 | 一维/多维插值 | medium |
| 12–14 | 正态性/卡方/t 检验 | medium |
| 15–16 | FFT 主频、滤波 | medium |

## 可选增补题（教师视情况布置）

1. **约束优化**：用 `minimize` SLSQP 求带不等式约束的二次规划，并解释 `ineq` 方向；
2. **Tukey HSD**：对三组数据做 `f_oneway` + `pairwise_tukeyhsd`，比较 ANOVA 与两两比较；
3. **频谱泄漏**：构造非整数周期正弦，加汉宁窗比较峰值旁瓣；
4. **solve_bvp**：求解 $y''=6x,\ y(0)=0,\ y(1)=1$ 并与 $y=x^3$ 比较。

## 评分建议

- `quiz.ipynb` 自动评分至 16 题；建议占总评 15–20%；
- 上机 `lab/` 占总评 10–15%；
- 综合案例报告（06 拓展）可作为期中/项目加分项。


## 旧题库说明

- 旧题库 `docs/原始资料/chapter_2_3_quiz`（SymPy & SciPy 30 题）已仅归档，不再作为教学入口；
- 其中未进入本 quiz 的挑战题（二阶 ODE 转一阶组、`optimize.root`、Lorenz、正弦 `curve_fit` 等）已并入 `assignment.md` 的“补充题”。
