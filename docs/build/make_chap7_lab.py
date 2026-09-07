# -*- coding: utf-8 -*-
"""Generate lab.ipynb for chapter 07 (Statsmodels) — guided lab notebook."""
import json, os

cells = []
def md(text): cells.append({"cell_type": "markdown", "metadata": {}, "source": text})
def code(text): cells.append({"cell_type": "code", "metadata": {}, "execution_count": None,
                              "outputs": [], "source": text})

md("""# Statsmodels 上机实验（第 7 章 lab）

**要求**：按顺序运行每一格，完成所有 <code># TODO</code> 后运行 <code>检查</code> 单元；最后导出/截图提交。
环境：Python 3.10+，statsmodels ≥ 0.13（推荐 0.14+）。

---
""")

code("""import numpy as np, pandas as pd, statsmodels.api as sm, statsmodels
print("statsmodels version:", statsmodels.__version__)
print("numpy:", np.__version__, " pandas:", pd.__version__)
assert statsmodels.__version__ >= "0.13", "请升级 statsmodels"
print("环境 OK")
""")

md("""## Part 1 单因素方差分析（One-Way ANOVA）

构造三组数据（均值不同），用 <code>ols + anova_lm</code> 检验组间差异是否显著。""")

code("""# 1.1 构造三组数据
rng = np.random.default_rng(1)
n = 12
df = pd.DataFrame({
    'group': ['A']*n + ['B']*n + ['C']*n,
    'y': np.r_[rng.normal(0,1,n), rng.normal(1,1,n), rng.normal(2,1,n)]
})
print(df.groupby('group')['y'].mean().round(3))

# 1.2 方差分析
from statsmodels.formula.api import ols
model = ols('y ~ C(group)', data=df).fit()
anova_res = sm.stats.anova_lm(model, typ=1)
print(anova_res)
# TODO: 读出 F 与 P 值，判断三组均值是否显著不同（P<0.05）
""")

code("""# 跟练 1: 增加第 4 组，并用 Tukey 做两两比较
import numpy as np, pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.stats.multicomp import pairwise_tukeyhsd
rng = np.random.default_rng(7)
n = 15
g = {'A': rng.normal(50,6,n), 'B': rng.normal(55,6,n),
     'C': rng.normal(60,6,n), 'D': rng.normal(65,6,n)}
df4 = pd.DataFrame({'fertilizer': np.repeat(list(g.keys()), n),
                    'out': np.concatenate(list(g.values()))})
m4 = ols('out ~ C(fertilizer)', data=df4).fit()
a4 = sm.stats.anova_lm(m4, typ=1)
print('4组 F = %.3f  P = %.3g' % (a4['F'].iloc[0], a4['PR(>F)'].iloc[0]))
print('各组均值:', df4.groupby('fertilizer')['out'].mean().round(2).to_dict())
pt = pairwise_tukeyhsd(endog=df4['out'], groups=df4['fertilizer'], alpha=0.05)
print(pt.summary())
# TODO: 哪两组差异显著？D 组与 A 组相差多少？
""")

code("""# 变形 1: 用 scipy 的 f_oneway 交叉验证 ANOVA 结果
import numpy as np
from scipy import stats
rng = np.random.default_rng(42)
n = 15
a = rng.normal(50,6,n); b = rng.normal(55,6,n); c = rng.normal(60,6,n)
F, p = stats.f_oneway(a, b, c)
print('scipy f_oneway: F = %.3f  P = %.3g' % (F, p))
print('与 ols + anova_lm 的结果应一致（约 F=18.455, P=1.77e-06）')
# TODO: 为什么二者一致？二者各自返回什么？
""")

code("""# 综合任务 1: 不等样本量的三组方差分析 + 箱线图
import numpy as np, pandas as pd, matplotlib.pyplot as plt, os
import statsmodels.api as sm
from statsmodels.formula.api import ols
rng = np.random.default_rng(9)
sizes = {'A':20, 'B':15, 'C':10}
dfu = pd.DataFrame({'fertilizer': np.repeat(list(sizes), list(sizes.values())),
                    'out': np.r_[rng.normal(50,6,sizes['A']),
                                 rng.normal(55,6,sizes['B']),
                                 rng.normal(60,6,sizes['C'])]})
mu = ols('out ~ C(fertilizer)', data=dfu).fit()
au = sm.stats.anova_lm(mu, typ=1)
print('不等样本 F = %.3f  P = %.3g' % (au['F'].iloc[0], au['PR(>F)'].iloc[0]))
fig, ax = plt.subplots(figsize=(5.2,3.6))
ax.boxplot([dfu.loc[dfu['fertilizer']==gg, 'out'].values for gg in sizes],
           tick_labels=list(sizes))
ax.set_title('不等样本量单因素方差分析')
ax.set_xlabel('fertilizer'); ax.set_ylabel('out')
fig.tight_layout(); fig.savefig('lab_case1_box.png', dpi=150); plt.close()
print('saved lab_case1_box.png')
# TODO: 样本量不等时，方差分析还适用吗？如何解读 F 值？
""")

md("""## Part 2 一元线性回归（statsmodels.api.OLS）

用数组接口做最小二乘回归：记得 <code>add_constant</code> 加截距。""")

code("""# 2.1 构造数据 y = 2x + 1 + 噪声
rng = np.random.default_rng(0)
x = np.linspace(0, 10, 50)
y = 2*x + 1 + rng.normal(0, 1, size=len(x))
X = sm.add_constant(x.reshape(-1, 1))
ols_model = sm.OLS(y, X).fit()
print("coef:", ols_model.params)
print("R²   :", round(ols_model.rsquared, 4))
print(ols_model.summary())
# TODO: 解释截距与斜率 x1，以及 R²、F、P 值
""")

md("""## Part 3 公式 API 与多元回归

用 <code>ols('y ~ x1 + x2', data=df)</code> 同时估计多个自变量。""")

code("""# 3.1 公式 API 一元
df2 = pd.DataFrame({'x': x, 'y': y})
fm = ols('y ~ x', data=df2).fit()
print(fm.params)

# 3.2 多元回归 y = 1 + 2*x1 - 3*x2 + 噪声
rng = np.random.default_rng(2)
x1 = rng.uniform(0, 10, 60)
x2 = rng.uniform(-3, 3, 60)
y2 = 1 + 2*x1 - 3*x2 + rng.normal(0, 1, 60)
dm = pd.DataFrame({'x1': x1, 'x2': x2, 'y': y2})
mul = ols('y ~ x1 + x2', data=dm).fit()
print(mul.params)
print(mul.pvalues)
print("R² =", round(mul.rsquared, 4))
# TODO: 判断 x1、x2 是否显著（P<0.05）
""")

code("""# 跟练 2: 加入交互项 area:age，比较 R2 与 AIC
import numpy as np, pandas as pd
from statsmodels.formula.api import ols
rng = np.random.default_rng(3)
n = 40
area = rng.uniform(30,120,n); age = rng.uniform(0,30,n)
price = 50 + 3.0*area - 1.5*age + rng.normal(0,8,n)
d2 = pd.DataFrame({'area':area,'age':age,'price':price})
m1 = ols('price ~ area + age', data=d2).fit()
m2 = ols('price ~ area + age + area:age', data=d2).fit()
print('model1 R2=%.4f AIC=%.2f' % (m1.rsquared, m1.aic))
print('model2 R2=%.4f AIC=%.2f' % (m2.rsquared, m2.aic))
print('interaction p = %.3g' % m2.pvalues['area:age'])
# TODO: 交互项显著吗？AIC 是变小还是变大？说明什么？
""")

code("""# 变形 2: 用数组接口 sm.OLS 重跑，核对系数一致
import numpy as np, pandas as pd, statsmodels.api as sm
from statsmodels.formula.api import ols
rng = np.random.default_rng(3)
n = 40
area = rng.uniform(30,120,n); age = rng.uniform(0,30,n)
price = 50 + 3.0*area - 1.5*age + rng.normal(0,8,n)
X = sm.add_constant(np.column_stack([area, age]))
arr = sm.OLS(price, X).fit()
print('array params:', arr.params.round(4))
d2 = pd.DataFrame({'area':area,'age':age,'price':price})
fm = ols('price ~ area + age', data=d2).fit()
print('formula params:', fm.params.round(4))
print('一致?', np.allclose(arr.params, fm.params, atol=1e-8))
# TODO: 为什么数组接口要手动 add_constant？公式接口如何加截距？
""")

code("""# 综合任务 2: 三变量回归 + 标准化系数比较
import numpy as np, pandas as pd
from statsmodels.formula.api import ols
rng = np.random.default_rng(12)
n = 60
area = rng.uniform(30,120,n); age = rng.uniform(0,30,n); rooms = rng.integers(1,6,n)
price = 40 + 2.5*area - 1.2*age + 4*rooms + rng.normal(0,6,n)
d3 = pd.DataFrame({'area':area,'age':age,'rooms':rooms,'price':price})
m3 = ols('price ~ area + age + rooms', data=d3).fit()
print('coef:')
print(m3.params.round(4))
print('pvalues:')
for k in m3.params.index:
    print('  %s  p=%.2e' % (k, m3.pvalues[k]))
zs = d3[['area','age','rooms','price']].apply(lambda s: (s-s.mean())/s.std())
ms = ols('price ~ area + age + rooms', data=zs).fit()
print('standardized coef:')
print(ms.params.round(4))
print('R2 =', round(m3.rsquared,4))
# TODO: 标准化后哪个变量影响最大？为什么面积和房间数的相对大小会变？
""")

md("""## Part 4 广义线性模型（GLM / 二分类 Logit）""")

code("""# 4.1 构造二分类数据
rng = np.random.default_rng(0)
X_raw = rng.uniform(0, 1, (100, 2))
lin = 0.5 + 1.2*X_raw[:,0] - 0.8*X_raw[:,1]
p = 1/(1+np.exp(-lin))
Y = rng.binomial(1, p)
Xg = sm.add_constant(X_raw)
glm = sm.GLM(Y, Xg, family=sm.families.Binomial()).fit()
print(glm.params)
print(glm.predict(sm.add_constant(np.array([[0.2,0.3],[0.8,0.1]]))))
# TODO: 解释两个新样本的成功概率
""")

md("""## Part 5 回归诊断：残差 QQ 图与 JB 统计量""")

code("""# 5.1 拟合 + 残差 QQ 图
import matplotlib.pyplot as plt
rng = np.random.default_rng(0)
xd = np.linspace(0, 10, 50)
yd = 3*xd + 2 + rng.normal(0, 1, 50)
Xd = sm.add_constant(xd.reshape(-1, 1))
olsd = sm.OLS(yd, Xd).fit()
sm.qqplot(olsd.resid, line='45')
plt.title("残差 QQ 图")
plt.savefig("qq_lab.png")
plt.show()
print(olsd.summary())
# TODO: 在摘要中找 Jarque-Bera (JB) 与 Prob(JB)，判断残差是否近似正态
""")

md("""## Part 6 时间序列分解（seasonal_decompose）

构造带趋势与周季节性（周期=7 天）的日序列，做加法分解。""")

code("""# 6.1 构造 180 天日序列
from statsmodels.tsa.seasonal import seasonal_decompose
rng = np.random.default_rng(0)
idx = pd.date_range('2022-01-01', periods=180, freq='D')
trend = np.linspace(0, 5, len(idx))
season = 2*np.sin(2*np.pi*np.arange(len(idx))/7)
noise = rng.normal(0, 0.5, len(idx))
s = pd.Series(10 + trend + season + noise, index=idx)
result = seasonal_decompose(s, model='additive', period=7)
print("trend head:", np.round(result.trend.head(7).values, 3))
print("seasonal head:", np.round(result.seasonal.head(7).values, 3))
print("resid std:", round(result.resid.std(), 4))
result.plot()
plt.savefig("decompose_lab.png")
plt.show()
# TODO: 观察“趋势/季节/残差”三部分，说明该序列的周期
""")

md("""## Part 7 平稳性检验（ADF 单位根检验）""")

code("""# 7.1 模拟 AR(1) 与随机游走并比较 ADF
from statsmodels.tsa.stattools import adfuller
rng = np.random.default_rng(0)
n = 300
y_ar = np.zeros(n)
for t in range(1, n):
    y_ar[t] = 0.7*y_ar[t-1] + rng.normal(0, 1)
stat1, p1, *_ = adfuller(y_ar)
print("AR(1)        ADF=%.3f p=%.3g" % (stat1, p1))

rng = np.random.default_rng(1)
rw = np.cumsum(rng.normal(0, 1, 200))
stat2, p2, *_ = adfuller(rw)
print("Random walk  ADF=%.3f p=%.3g" % (stat2, p2))
# TODO: 哪个序列更平稳？为什么随机游走 p 值大？
""")

md("""## Part 8 ARIMA(1,1,1) 拟合与预测""")

code("""# 8.1 构造非平稳序列（随机游走+趋势）
from statsmodels.tsa.arima.model import ARIMA
rng = np.random.default_rng(0)
n = 200
steps = rng.normal(0, 1, n).cumsum() + np.linspace(0, 10, n)
si = pd.Series(steps, index=pd.date_range('2020-01-01', periods=n, freq='D'))
mod = ARIMA(si, order=(1, 1, 1)).fit()
print(mod.summary())
fc = mod.forecast(steps=5)
print("forecast:", np.round(fc.values, 4))
# 绘图
plt.figure(figsize=(9, 3.5))
plt.plot(si.index[-30:], si.values[-30:], label="历史")
fc_idx = pd.date_range(si.index[-1] + pd.Timedelta(days=1), periods=5, freq='D')
plt.plot(fc_idx, fc.values, marker='o', label="预测")
plt.axvline(si.index[-1], color='gray', ls=':')
plt.legend(); plt.savefig("arima_lab.png"); plt.show()
# TODO: 给出未来 5 天预测值，并判断模型参数是否显著
""")

code("""# 跟练 3: 对随机游走做 ADF，并比较差分前后
import numpy as np, pandas as pd
from statsmodels.tsa.stattools import adfuller
rng = np.random.default_rng(5)
n = 200
rw = np.cumsum(rng.normal(0,1,n))
s = pd.Series(rw)
a0 = adfuller(s)
print('raw  ADF=%.3f p=%.3g' % (a0[0], a0[1]))
d = s.diff().dropna()
a1 = adfuller(d)
print('diff ADF=%.3f p=%.3g' % (a1[0], a1[1]))
# TODO: 为什么随机游走差分后 p 值明显变小？
""")

code("""# 变形 3: 用 AIC 对 (p,q) 网格搜索选阶
import numpy as np, pandas as pd, warnings
warnings.filterwarnings('ignore')
from statsmodels.tsa.arima.model import ARIMA
rng = np.random.default_rng(11); n=300
e = rng.normal(0,1,n); x=np.zeros(n)
for t in range(1,n):
    x[t]=0.6*x[t-1]+e[t]+0.3*e[t-1]
ser = pd.Series(np.cumsum(x)+100)
best=None
for p in range(3):
    for q in range(3):
        try:
            m=ARIMA(ser, order=(p,1,q)).fit()
            if best is None or m.aic<best[0]: best=(m.aic,p,q)
        except Exception: pass
print('best order (p,d,q):', best[1],1,best[2],'AIC=%.3f'%best[0])
print('候选表:')
for p in range(3):
    for q in range(3):
        try:
            m=ARIMA(ser, order=(p,1,q)).fit()
            print('  (%d,1,%d) AIC=%.2f'%(p,q,m.aic))
        except Exception:
            print('  (%d,1,%d) failed'%(p,q))
# TODO: 哪些阶数 AIC 接近？为什么不能只看 AIC？
""")

code("""# 综合任务 3: 拟合最优模型，做残差诊断并画预测图
import numpy as np, pandas as pd, warnings, matplotlib.pyplot as plt, os
warnings.filterwarnings('ignore')
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.stats.diagnostic import acorr_ljungbox
from statsmodels.stats.stattools import jarque_bera
rng = np.random.default_rng(11); n=300
e = rng.normal(0,1,n); x=np.zeros(n)
for t in range(1,n):
    x[t]=0.6*x[t-1]+e[t]+0.3*e[t-1]
vals = np.cumsum(x)+100
idx = pd.date_range('2020-01-01', periods=n, freq='D')
ser = pd.Series(vals, index=idx)
best=None
for p in range(3):
    for q in range(3):
        try:
            m=ARIMA(ser, order=(p,1,q)).fit()
            if best is None or m.aic<best[0]: best=(m.aic,p,q)
        except Exception: pass
final = ARIMA(ser, order=(best[1],1,best[2])).fit()
resid = final.resid.iloc[10:]
print('order (p,d,q):', best[1],1,best[2])
print('AR:', np.round(final.arparams,4), ' MA:', np.round(final.maparams,4))
print('Ljung-Box p = %.4f' % acorr_ljungbox(resid,lags=[10],return_df=True)['lb_pvalue'].iloc[0])
print('Jarque-Bera p = %.4f' % jarque_bera(resid)[1])
fc = final.forecast(5)
print('forecast:', np.round(fc.values,3))
plt.figure(figsize=(8,3.5))
plt.plot(ser.index[-40:], ser.values[-40:], label='历史')
fidx = pd.date_range(ser.index[-1]+pd.Timedelta(days=1), periods=5, freq='D')
plt.plot(fidx, fc.values, marker='o', label='预测')
plt.axvline(ser.index[-1], color='gray', ls=':')
plt.legend(); plt.title('ARIMA 最优模型预测')
plt.savefig('lab_case3_forecast.png', dpi=150); plt.close()
print('saved lab_case3_forecast.png')
# TODO: 根据 Ljung-Box 与 JB 判断模型是否合格
""")

md("""## Part 9 综合任务：城市日负荷分析

把本章的**回归 + 方差分析 + 时间序列**串起来：对模拟的城市日负荷数据，做
① 工作日/周末差异的方差分析；② 负荷对温度的 OLS 回归；③ 时间序列分解与 ARIMA 预测。""")

code("""# 9.1 生成综合数据
rng = np.random.default_rng(7)
m = 140
date = pd.date_range('2023-01-01', periods=m, freq='D')
trendc = np.linspace(0, 15, m)
seasonc = 5*np.sin(2*np.pi*np.arange(m)/7) + 2*np.cos(2*np.pi*np.arange(m)/7)
noisec = rng.normal(0, 3, m)
weekend = (date.dayofweek >= 5).astype(int)
temp = 25 + 6*np.sin(2*np.pi*np.arange(m)/7) + rng.normal(0, 2, m)
load = 300 + 4*temp + 20*weekend + trendc + seasonc + noisec
dfc = pd.DataFrame({'date': date, 'load': load, 'weekend': weekend, 'temp': temp})

# 9.2 工作日 vs 周末 方差分析
dfc['wd'] = np.where(dfc['weekend'] == 1, '周末', '工作日')
ano = ols('load ~ C(wd)', data=dfc).fit()
print(sm.stats.anova_lm(ano, typ=1))

# 9.3 负荷对温度的 OLS 回归（控制周末哑变量）
olm = sm.OLS(dfc['load'], sm.add_constant(dfc[['temp','weekend']])).fit()
print("回归系数:", olm.params)
print("R² =", round(olm.rsquared, 4))

# 9.4 时间序列：分解 + ARIMA 预测 7 天
load_s = pd.Series(dfc['load'].values, index=date)
decomp = seasonal_decompose(load_s, model='additive', period=7)
modc = ARIMA(load_s, order=(1, 1, 1)).fit()
fcc = modc.forecast(steps=7)
print("未来 7 天预测:", np.round(fcc.values, 2))

plt.figure(figsize=(9, 4))
plt.plot(load_s.index, load_s.values, lw=1.2, label="日负荷")
plt.plot(decomp.trend.index, decomp.trend.values, lw=1.8, label="趋势")
plt.legend(); plt.title("城市日负荷与趋势"); plt.savefig("case_load.png"); plt.show()
print("已保存 case_load.png")
# TODO: 写 3 句结论：①ANOVA 是否显著；②温度/周末对负荷的影响方向与大小；③ARIMA 一周预测趋势
""")

md("""## 提交清单

- [ ] 所有 Part 均运行并通过，无异常；
- [ ] Part 1 已读取 F 与 P 值并判断显著性；
- [ ] Part 5 已读取 JB 与 Prob(JB)；
- [ ] Part 7 已说明 AR(1) 与随机游走的 ADF 差异；
- [ ] Part 9 已写出 3 句结论并生成 case_load.png；
- [ ] 案例卡 C1/C2/C3 的“跟练、变形、综合任务”均已运行并回答 TODO；
- [ ] 导出为 html / 保留 ipynb 提交。

**延伸**：完成 exercises/ 的 10 道自测题与 <code>03-综合案例.md</code>、<code>04-常见误区与技巧.md</code>。""")

nb = {
    "cells": cells,
    "metadata": {
        "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
        "language_info": {"name": "python", "version": "3.13"}
    },
    "nbformat": 4,
    "nbformat_minor": 5,
}
out = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                   "chapters", "07-statsmodels", "lab", "lab.ipynb")
with open(out, "w", encoding="utf-8") as f:
    # 统一为中文字体设置（所有绘图单元注入微软雅黑）
    NL = chr(10)
    for _c in nb["cells"]:
        if _c["cell_type"] == "code":
            _src = "".join(_c.get("source", []))
            if (("plt." in _src) or ("sns." in _src) or ("matplotlib" in _src)
                    or ("savefig" in _src)) and ("font.sans-serif" not in _src):
                _c["source"] = [
                    "import matplotlib.pyplot as plt" + NL,
                    'plt.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei", "DejaVu Sans"]' + NL,
                    'plt.rcParams["axes.unicode_minus"] = False' + NL,
                ] + list(_c.get("source", []))
    json.dump(nb, f, ensure_ascii=False, indent=1)
print("saved", out, "cells:", len(cells))
