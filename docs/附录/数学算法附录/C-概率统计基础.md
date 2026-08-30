# 概率统计基础

> 本附录为第 4 章 Pandas 的描述统计、第 7 章 Statsmodels 的回归/时序与第 0 章成绩统计提供数学背景：分布、期望方差、推断（检验/置信区间）、回归与时间序列，并补齐本科易混淆的难点（中心极限定理、检验功效、多重比较）。

---

## C.1 直觉故事：为什么不能只看平均分

两个班平均分都是 75：甲班 74~76 很集中，乙班一半 50 一半 100。平均分相同，但"不确定性"天差地别。所以描述数据至少要：**中心 + 离散 + 形状**。

- 均值 $\bar{x}=\frac{1}{n}\sum x_i$：常见但怕极端值；
- 中位数：排序中间值，稳健；
- 标准差 $s=\sqrt{\frac{1}{n-1}\sum(x_i-\bar{x})^2}$：离散程度（样本用 $n-1$）；
- 分位数/箱线图：看分布尾巴与离群点。

> **正文见**：[0 前置基础 · 07 综合案例](../../chapters/00-prep/00-07-综合案例.md)、[4 Pandas · 01 基础数据结构](../../chapters/04-pandas/01-基础数据结构.md)。

---

## C.2 随机变量与分布（讲解）

### C.2.1 期望与方差

- $E[X]=\sum x\,p(x)$：长期平均。掷骰子期望 3.5——它是"中心裁判"，不是某个具体结果；
- $\mathrm{Var}(X)=E[(X-E[X])^2]=E[X^2]-(E[X])^2$：偏离平方的平均；
- 线性性质：$E[aX+b]=aE[X]+b$；独立时 $\mathrm{Var}(aX+b)=a^2\mathrm{Var}(X)$。

### C.2.2 常用分布

| 分布 | 记号 | 直觉 | 场景 |
| ---- | ---- | ---- | ---- |
| 正态 | $N(\mu,\sigma^2)$ | 对称钟形 | 测量误差、均值近似 |
| 二项 | $B(n,p)$ | n 次独立试验成功次数 | 点击率、产品合格数 |
| 泊松 | $\mathrm{Pois}(\lambda)$ | 单位时间事件数 | 订单到达、故障次数 |
| 均匀 | $U(a,b)$ | 等概率 | 随机数、先验 |
| t/F/χ² | $t(n), F, \chi^2$ | 小样本推断 | 检验、ANOVA |

### C.2.3 中心极限定理（必须理解）

大量**独立同分布**随机变量之和（或均值）的分布近似正态，与原始分布无关：

$$\frac{\bar{X}-\mu}{\sigma/\sqrt n}\xrightarrow{ n\to\infty } N(0,1)$$

这解释了**为什么样本均值越稳**、为什么 t 检验/置信区间成立。注意它要求"独立同分布"：时间序列相邻样本相关时不满足，不能直接套。

### C.2.4 协方差与相关

$\mathrm{Cov}(X,Y)=E[(X-\mu_X)(Y-\mu_Y)]$；相关系数 $\rho=\dfrac{\mathrm{Cov}(X,Y)}{\sigma_X\sigma_Y}\in[-1,1]$。$\rho=1$ 完全正线性相关；$\rho=0$ 仅表示**不线性**相关（可能存在非线性关系！）。

---

## C.3 统计推断（重点、难点）

### C.3.1 置信区间：从"估计值"到"可靠性"

均值置信区间：

$$\bar{x}\pm t_{\alpha/2,n-1}\cdot\frac{s}{\sqrt n}$$

- $s/\sqrt n$ = 标准误：均值的"抖动范围"；
- 乘 $t$ 分位数把"1 个标准误"扩成"95% 覆盖"；
- 样本越大/波动越小 → 区间越窄 → "越确信"。

### C.3.2 假设检验：p 值到底在说什么

流程：立 $H_0$ → 选统计量 → 算 p 值（在 $H_0$ 下看到这么极端数据的概率）→ 与 $\alpha=0.05$ 比较。

| 检验 | 回答的问题 |
| ---- | ---- |
| 单/双样本 t | 均值是否等于/不同 |
| 卡方 | 分类拟合、列联独立 |
| ANOVA (F) | 多组均值是否全等 |
| KS | 分布是否一致 |

**两类错误**：$\alpha$（第一类，误拒）、$\beta$（第二类，漏拒）；**功效** $1-\beta$。样本太小 → 功效低 → "不显著"可能只是**没测出来**，不代表"没差异"。

**多重比较**：一次做 20 次检验，纯运气也可能"显著"几次 → 用 Bonferroni/FDR 校正。

### C.3.3 检验实操清单

1. 问题类型 → 选 t/卡方/ANOVA/KS/ADF；
2. 样本独立？配对数据用配对检验；
3. 正态性：小样本看 QQ 图/Shapiro；偏态用非参数或自助法；
4. 多重比较校正；
5. 报告：$p$ 值 + 效应量 + 置信区间。

---

## C.4 回归与方差分析（建模视角）

### C.4.1 线性回归 = 换视角的最小二乘

模型 $y=\beta_0+\beta_1x_1+\cdots+\beta_kx_k+\varepsilon$；OLS 解：

$$\hat{\beta}= (X^TX)^{-1}X^Ty$$

要求（推断时）：线性、独立、同方差、残差正态。违背时用稳健标准误/变换。

### C.4.2 怎么评价

- $R^2=1-\mathrm{SSE}/\mathrm{SST}$：解释变异比例（过高要警惕过拟合）；
- 系数符号、大小、p 值、置信区间：每个变量的"作用方向/强度/显著性"；
- **残差图**：比 $R^2$ 更诚实（看趋势/异方差/离群点）。

手算：$(1,2),(2,4),(3,7)$ 一元回归斜率约 2.5、截距约 -0.5。

### C.4.3 ANOVA：多组到底有没有差异

$$F=\frac{\text{组间方差}/\text{(组数-1)}}{\text{组内方差}/\text{(n-组数)}}$$

F 大 = "组间差异比组内随机波动更明显"。

---

## C.5 时间序列：和"普通回归"有什么不同（重点）

| 概念 | 直觉 | 工具 |
| ---- | ---- | ---- |
| 平稳性 | 均值/方差不随时间漂移 | ADF 单位根检验 |
| 自相关 | 现在与过去的相关 | ACF/PACF |
| 差分 | $y_t-y_{t-1}$ | 消除趋势 |
| 移动平均 | 局部平均去噪 | `rolling` |
| 分解 | 趋势+季节+残差 | `seasonal_decompose` |
| ARIMA | AR + 差分 + MA | 预测 |

**关键**：相邻样本相关 → 不能当独立样本做普通回归；先 ADF/差分，再看 ACF/PACF 定阶，否则 p 值"虚假显著"。

---

## C.6 动手例题（选做）

**例：置信区间**。样本 $[68,91,55,76,88]$：均值 $75.6$，标准差约 $14.0$；95% 置信区间 $75.6\pm t_{0.025,4}\times 14.0/\sqrt5\approx[58.2,93.0]$（很宽→样本太小）。代码：

```python
import numpy as np
from scipy import stats
x = np.array([68, 91, 55, 76, 88])
print(x.mean(), x.std(ddof=1))
stats.t.interval(0.95, df=len(x)-1, loc=x.mean(), scale=stats.sem(x))
```

**例：相关≠因果**。$y=x+\text{噪声}$ 相关系数接近 1；若有共同原因 $z$ 同时影响二者，高相关只是巧合 → 建模要控制混杂。

---

## C.7 Python 对应（速查）

```python
import numpy as np, pandas as pd, statsmodels.api as sm
from scipy import stats

x = np.array([68, 91, 55, 76, 88])
pd.Series(x).describe()
stats.ttest_1samp(x, 60)
stats.chisquare([10, 20, 30])

X = sm.add_constant(np.array([[1.,2.],[2.,4.],[3.,7.]]))
model = sm.OLS(np.array([2.,4.,7.]), X).fit()
model.summary()

from statsmodels.tsa.seasonal import seasonal_decompose
df = pd.read_csv("data.csv", index_col=0, parse_dates=True)
seasonal_decompose(df["sales"], model="additive").plot()
```

| 你想要 | 用哪个 |
| ---- | ---- |
| 描述统计 | `Series.describe()` |
| 分布检验 | `scipy.stats` |
| 回归/ANOVA | `statsmodels.OLS / ols` |
| 时序分解 | `seasonal_decompose` |
| ARIMA | `statsmodels.tsa.arima.model.ARIMA` |

---

## C.8 常见误区

| 误区 | 正确 |
| ---- | ---- |
| p 值小=影响大 | p 值与效应量是两回事 |
| 只看均值 | 先看分布（直方图/箱线图） |
| 非平稳直接回归 | 先 ADF/差分 |
| 相关=因果 | 相关 ≠ 因果 |
| 小样本硬用正态近似 | 用小样本检验/重抽样 |
| 不显著=没有差异 | 可能功效不足（样本小） |

---

## C.9 使用章节（双向）

| 章 | 哪里用到 | 链接 |
| ---- | ---- | ---- |
| 0 前置基础 | 成绩统计 | [07 综合案例](../../chapters/00-prep/00-07-综合案例.md) |
| 4 Pandas | 分组聚合/描述统计 | [01 基础数据结构](../../chapters/04-pandas/01-基础数据结构.md) |
| 7 Statsmodels | 回归/ANOVA/时序 | [01 方差分析与回归](../../chapters/07-statsmodels/01-方差分析与回归.md) |
| 3 SciPy | 假设检验 | [04 假设检验工具包](../../chapters/03-scipy/04-假设检验工具包.md) |

**下游衔接**：intro-mathmodel 第 7 章（权重/评价）、第 8 章（时间序列）、第 9 章（机器学习统计模型）。
**延伸阅读**：statsmodels 官方文档、ThinkStats2、《概率论与数理统计》（见 [references.md](./references.md)）。

---

## C.12 常见考题与自查（考前 10 分钟）

| 会了吗？ | 考点 | 一句话答案 |
| ---- | ---- | ---- |
| □ | p<0.05 的含义 | 在 H0 下看到这么极端数据的概率小 |
| □ | p 小 ≠ 影响大 | 看效应量与置信区间 |
| □ | 置信区间与样本量 | n 越大区间越窄（标准误 s/sqrt(n)） |
| □ | 中心极限定理 | 大量独立同分布均值近似正态 |
| □ | 相关≠因果 | 可能有混杂变量 |
| □ | 非平稳直接回归 | 先 ADF/差分，否则 p 值虚假 |
| □ | 功效低 | "不显著"可能只是样本不足 |


---

## C.11 综合案例：一份"完整统计报告"的骨架

**问题**：某班两组练习方式（A/B）的成绩是否不同？影响分数的因素还有哪些？

步骤：

1. **描述统计**：每组均值/中位数/标准差/箱线图（C.1）；
2. **差异性检验**：先检查正态性（Shapiro），再用独立样本 t 检验或 Mann-Whitney；报告 p 值与置信区间（C.3）；
3. **回归**：把"练习方式"与"前测成绩"放进线性回归，看系数与 p 值（C.4）；
4. **时序（若有）**：对周销量做分解/ADF，再决定用差分或 ARIMA（C.5）；
5. **结论模板**："在控制了 X 后，A 组平均高 delta 分（95%CI [...]），p=...；但样本量小，需谨慎解释。"

参考要点代码：

    import pandas as pd, statsmodels.api as sm
    from scipy import stats
    df = pd.read_csv("scores.csv")
    a = df.loc[df.group == "A", "score"]; b = df.loc[df.group == "B", "score"]
    print(stats.ttest_ind(a, b))
    X = sm.add_constant(pd.get_dummies(df[["group", "pretest"]]))
    print(sm.OLS(df.score, X).fit().summary())

**反思**：统计报告不是"跑一个显著性"就完事；分布、检验假设、效应量、置信区间都要交代。


---

## C.10 例题集（深入练习）

**例 1：t 检验完整流程（手算路径）**。样本 $[68,91,55,76,88]$，检验 $H_0:\mu=60$。均值 $75.6$，标准误 $s/\sqrt n\approx 14.0/2.236\approx 6.26$，$t=(75.6-60)/6.26\approx 2.49$。查 $\mathrm{df}=4$ 的 $t$ 表，双尾 $p\approx 0.067>0.05$ → 不显著（样本太小）。

**例 2：ANOVA 思路（三组）**。组均值差很大、组内波动很小 → $F$ 大 → 拒绝"三组均值全等"。代码：

```python
import pandas as pd, statsmodels.api as sm
from statsmodels.formula.api import ols
df = pd.DataFrame({"score": [70,75,72,80,85,83,60,62,58],
                   "group": ["A"]*3 + ["B"]*3 + ["C"]*3})
print(ols("score ~ C(group)", data=df).fit().summary())   # 看 F 与 p
```

**例 3：ADF 读数**。对非平稳序列做 ADF，$p>0.05$ → 不能拒绝"存在单位根"（非平稳）→ 先差分再建模。

