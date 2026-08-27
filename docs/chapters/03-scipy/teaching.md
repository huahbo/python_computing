# 第 3 章 教学说明（教师用）

> 面向授课教师：课时建议、重点难点、上机安排、考核建议。学生无需阅读本页。

## 1. 教学目标

- 让学生能“把数学模型翻译成 SciPy 函数调用”，独立完成数值积分、ODE 求解、优化、插值、统计检验、FFT 与滤波；
- 建立“何时用哪个工具包”的选题思维（积分→integrate，拟合→optimize，补点→interpolate，检验→stats，频域→fft/signal）；
- 能正确解读数值结果（收敛标志、p 值、参数协方差、频谱峰值），并排查常见数值陷阱（初值、归一化、版本迁移）。

## 2. 建议课时与安排

| 课次 | 内容 | 建议形式 | 依赖 |
| ---- | ---- | ---- | ---- |
| 第 1 次 | 01 微积分：数值积分（quad/dblquad/trapezoid），一阶 ODE | 讲授 + 课堂演示 | 第 1 章 NumPy |
| 第 2 次 | 01 后段：二阶/高阶 ODE、solve_ivp、solve_bvp | 讲授 + 上机 | 第 1 次 |
| 第 3 次 | 02 优化：求根、brent/fmin/minimize、linprog、linear_sum_assignment | 讲授 + 上机 | 第 1 次 |
| 第 4 次 | 02 曲线拟合（leastsq/curve_fit）+ 03 插值（CubicSpline/RegularGridInterpolator/griddata） | 讲授 + 上机 | 第 3 次 |
| 第 5 次 | 04 假设检验（shapiro/t检验/卡方/ANOVA/Tukey） | 讲授 + 上机 | 第 3 次 |
| 第 6 次 | 05 傅里叶变换与滤波（fft/rfft/butter/lfilter） | 讲授 + 上机 | 第 1 次 |
| 第 7 次 | 06 综合案例 + 07 误区技巧 | 上机为主 + 讨论 | 前 6 次 |
| 课后 | 07 误区技巧自读；完成 quiz + 作业 | 自主学习 | — |

> 若课时紧张：可将 01–02 合并讲 1 次，05 与 06 合并，习题改为选做。

## 3. 重点与难点

### 重点
- `scipy.integrate`：`quad`、`trapezoid`、`odeint`/`solve_ivp` 的签名与适用场景；
- `scipy.optimize`：`brentq` vs `brent`、`minimize` 约束、`curve_fit` 的 `p0` 与 `pcov`；
- `scipy.interpolate`：插值 vs 拟合、`CubicSpline`/`RegularGridInterpolator`/`griddata` 的选择；
- `scipy.stats`：p 值解读、独立/配对 t 检验、卡方、ANOVA 与 Tukey；
- `scipy.fft`：单边频谱、归一化、频率轴；
- `scipy.signal`：`Wn` 归一化、`lfilter` vs `filtfilt`。

### 难点（学生常卡）
- **ODE 参数顺序**：`odeint(y,t)` vs `solve_ivp(t,y)`；
- **高阶 ODE 降阶**：要化成多个一阶方程；
- **非线性拟合初值**：`curve_fit` 初值不良导致不收敛或收敛到错误参数；
- **优化约束方向**：`ineq` 是 `fun(x)>=0`，与直觉相反；
- **`fft` 幅值归一化**：学生常把 350 当成幅度 0.7；
- **p 值误读**：把“统计显著”当“实际重要”。

## 4. 上机（lab/）使用建议

- 每部分 10–15 分钟；要求每格代码都运行并记录输出；
- 综合任务（传感器信号分析）可小组完成；
- 教师可要求学生在 lab 中额外完成“低通滤波后重新拟合”作为隐藏检查点；
- 强调版本：`trapz`→`trapezoid`、`interp2d`→`RegularGridInterpolator`。

## 5. 作业与考核建议

- **平时**：exercises 16 题（quiz.ipynb 自动评分）；
- **上机**：lab.ipynb 完成情况 + 06 综合案例拓展；
- **期中/期末融合**：把 SciPy 知识点并入第 7 章 statsmodels（方差分析回归）或期末大作业（信号/数据建模）；
- **加分项**：用 `curve_fit` 拟合真实数据集并评估参数标准误，写 3 句结论。

## 6. 易错点清单（直接用于出题）

1. `trapz` 已改名 `trapezoid`（版本迁移）；
2. `odeint` 与 `solve_ivp` 参数顺序相反；
3. `quad` 返回 `(value, err)` 元组；
4. `brent` 求极小值、`brentq` 求根；
5. `linprog` 默认最小化；
6. `curve_fit` 需要 `p0`；
7. `interp2d` 废弃，用 `RegularGridInterpolator`；
8. `butter` 的 `Wn` 是归一化频率；
9. `fft` 幅值未除以 N；
10. `ttest_ind` 用于独立样本、`ttest_rel` 用于配对；
11. ANOVA 显著后需 Tukey 两两比较；
12. 随机统计模拟必须固定种子。

## 7. 资源包

- 讲义正文：`01-微积分工具包.md` ~ `07-常见误区与技巧.md`
- 配图：`images/*.png`（由 `../../build/make_chap3_figures.py` 生成）
- 练习：`exercises/`；上机：`lab/`；参考：`references.md`
- 合订 PDF：`../../教材PDF/03-Scipy及其基本使用.pdf`（由 `../../build/pdf_build.py` 生成）

---

## 课表定位（8 周制）

- 周次：第 3 周
- 上课：2 学时（精讲 + 演示）
- 上机：4 学时（单独排课，以 lab/ 为主，含 0.5h 回顾与 0.5h 总结/quiz）
- 课后：完成 exercises/ 的 quiz 与 assignment；06 常见误区页自学
