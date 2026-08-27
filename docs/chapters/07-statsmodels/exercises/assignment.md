# 第 7 章 作业（assignment.md）

> 本作业共 10 题：概念理解 + 代码实现 + 简易解读。建议在完成 <code>quiz.ipynb</code> 与 <code>lab/</code> 后进行。每题后附参考答案要点。

---

## 1. 为什么数组接口要 <code>sm.add_constant</code>？

**答**：OLS 模型 <code>y = Xβ + ε</code> 中，若想在 <code>β</code> 里包含截距项，需要设计矩阵有一列全 1。<code>sm.add_constant(X)</code> 就是加这一列。公式 API（<code>ols</code>）会自动加 <code>Intercept</code>，数组 API 不会。

## 2. 读出并解释一次 OLS 的 <code>summary()</code> 中的五项

**答**（以前面一元回归为例）：

1. <code>R²=0.982</code>：模型解释约 98.2% 的方差；
2. <code>F-statistic=2613</code>、<code>Prob(F)=1.63e-43</code>：模型整体高度显著；
3. <code>const</code> 系数 0.5488、标准误 0.240、P=0.027：截距显著；
4. <code>x1</code> 系数 2.116、标准误 0.041、P=0.000：斜率显著；
5. 置信区间 <code>[0.066, 1.032]</code>（截距）与 <code>[2.033, 2.199]</code>（斜率）：均不含 0（斜率），支撑显著结论。

## 3. 单因素方差分析：F 统计量怎么算、P 值怎么判？

**答**：把总平方和分解为组间 <code>SS_b</code> 与组内 <code>SS_w</code>，自由度分别为 <code>k-1</code> 与 <code>N-k</code>，则

<code>F = (SS_b/(k-1)) / (SS_w/(N-k))</code>。

P 值由 F 分布给出；若 <code>P&lt;0.05</code>，认为组间均值不全相等。

## 4. 写出三个组 <code>A/B/C</code> 的方差分析代码（要求：样本量≥10，均值不同）

~~~python
import numpy as np, pandas as pd, statsmodels.api as sm
from statsmodels.formula.api import ols
rng = np.random.default_rng(1); n = 12
df = pd.DataFrame({'group': ['A']*n+['B']*n+['C']*n,
                   'y': np.r_[rng.normal(0,1,n), rng.normal(1,1,n), rng.normal(2,1,n)]})
model = ols('y ~ C(group)', data=df).fit()
print(sm.stats.anova_lm(model, typ=1))
~~~

**要点**：使用 <code>C(group)</code>；读 <code>PR(>F)</code> 判断显著性。

## 5. GLM(Binomial) 中 <code>predict</code> 返回什么？如何得到 0/1 分类？

**答**：默认返回**成功概率**（Logit 反变换）。要得 0/1，设阈值（如 0.5）：<code>y_pred = (proba >= 0.5).astype(int)</code>。

## 6. 回归诊断：如何判断残差是否近似正态？

**答**：看 <code>summary()</code> 中的 <code>Jarque-Bera (JB)</code> 与 <code>Prob(JB)</code>；若 <code>Prob(JB)>0.05</code>，不能拒绝正态。也可画残差 QQ 图，点越贴 45° 线越好。

## 7. 异方差与 WLS

**答**：误差方差随自变量变化时 OLS 仍无偏但效率低。用 WLS 加权重（如 <code>weights=1/x**2</code>）可校正。比较参数估计与 <code>bse</code>：通常 WLS 的 <code>bse</code> 更小。

## 8. 时间序列分解两种模型

**答**：加法 <code>y=T+S+R</code> 适合波动幅度不随水平变化；乘法 <code>y=T×S×R</code> 适合幅度随水平增长。用 <code>seasonal_decompose(series, model='additive', period=7)</code>。

## 9. ADF 检验怎么用？

**答**：<code>adfuller(series)</code> 返回 <code>(stat, pvalue, ...)</code>。若 <code>pvalue &lt; 0.05</code> 拒绝“单位根”，序列平稳；否则需差分（<code>d</code> 加 1）再检验。

## 10. ARIMA 拟合与预测

~~~python
from statsmodels.tsa.arima.model import ARIMA
mod = ARIMA(series, order=(1, 1, 1)).fit()
fc = mod.forecast(steps=5)
print(fc)
~~~

**要点**：非平稳先差分；<code>(p,d,q)</code> 由 ACF/PACF 或网格搜索 + AIC 选择；预测后要自己给未来时间轴。

---

**评分参考**：每题 10 分，概念题按要点给分；代码题看能否正确调用 API 并解读输出。
