# 第 4 章 作业题（Pandas，15 题）

> 建议用时 2–3 小时。所有题目用 pandas（+ numpy、matplotlib）作答；答案可参考 `answers.ipynb` 中对应题号。

## 第一部分：基础数据结构（1–6）

**1. 创建 Series**：用列表 `[10, 20, 30, 40]` 创建 Series，并分别用 `index=['a','b','c','d']` 指定标签。打印：`s['b']`、`s.iloc[1]`、`s.index.tolist()`。

**2. 创建 DataFrame**：用字典创建三行三列的 DataFrame（含姓名、语文、数学），指定行索引 `['r0','r1','r2']`。打印 `shape`、`columns`，并用 `df.loc['r1','数学']` 与 `df.iloc[1,1]` 取出同一位置的值。

**3. loc vs iloc**：对同一个 DataFrame（A、B、C 三列），分别用 `.loc[0:1, ['A','C']]` 和 `.iloc[:2, [0,2]]` 取出第 0、1 行的 A、C 列。说明为什么两个结果相同。

**4. 布尔筛选**：构造 `A=[1..5], B=[10..50], C=['a','b','a','b','c']`。分别筛选：
  - `A>2 且 B<50`；
  - `A>3 或 C=='b'`；
  - `C != 'a'`。

**5. 切片与排序**：用 `sort_values` 按 `B` 列降序排序；用 `df['A'][::-1]` 反转顺序，并与 `.sort_values('A', ascending=False)` 比较。

**6. 合并与连接**：构造两个 DataFrame（left: key,x；right: key,y），用 `pd.merge(..., on='key', how='left')` 左连接；再用 `pd.concat([df1, df2], ignore_index=True)` 纵向拼接。

## 第二部分：数据清洗与预处理（7–11）

**7. 重复值**：构造含一行重复的 DataFrame，用 `df.duplicated().sum()` 统计，并用 `df.drop_duplicates()` 与 `df.drop_duplicates(subset=['A','B'], keep='last')` 对比。

**8. 缺失值**：构造含 `np.nan` 的两列，打印 `df.isna().sum()`；分别用 `df.dropna()`、`df.fillna(0)`、`df.ffill()`、`df.bfill()` 处理并说明差异。

**9. 用中位数填充**：对缺失列用 `df.fillna(df.median())` 填充，并验证均值变化。

**10. IQR 异常值**：对 `Value=[1,2,3,4,5,6,100]`，计算 Q1、Q3、IQR，找出小于 `Q1-1.5*IQR` 或大于 `Q3+1.5*IQR` 的异常值，并用中位数替换。

**11. 数据规约**：对 `feature=[1..5]`，计算 Min-Max 规约（映射到 [0,1]）与 Z-Score 规约；验证 Z-Score 的均值约 0、标准差约 1。

## 第三部分：统计、分组与透视（12–13）

**12. 统计描述**：对两列数值 DataFrame 调用 `df.describe()`，解释 count/mean/std/min/25%/50%/75%/max 的含义；再对含字符串列调用 `df.describe(include='all')`。

**13. groupby 与 pivot_table**：对 `班级/科目/分数` 长表：
  - 用 `groupby('班级')['分数'].agg(['mean','sum','count'])` 分组；
  - 用 `pivot_table(values='分数', index='班级', columns='科目', aggfunc='mean', fill_value=0)` 做透视；
  - 筛选出均值 > 85 的组。

## 第四部分：时间序列与性能（14–15）

**14. 时间序列**：用 `pd.date_range('2023-01-01', periods=60, freq='D')` 生成日期索引，配合随机数生成日数据；分别用 `ts.resample('W').mean()` 与 `ts.rolling(7).mean()` 得到周均与 7 日移动平均；解释两者的差异。

**15. apply vs 向量化**：对 200 万个数的 Series，分别用 `s.apply(lambda x: x*2+1)` 与 `s*2+1`，计时并比较（本机实测向量化约快 40–50 倍）。解释为什么。

---

## 评分要点

| 题号 | 考察点 | 分值建议 |
| ---- | ---- | ---- |
| 1–6 | 基础索引、布尔筛选、合并 | 40% |
| 7–11 | 清洗与规约 | 30% |
| 12–13 | 统计、分组、透视 | 20% |
| 14–15 | 时间序列、性能 | 10% |

> 达成判据：每题代码能运行、输出正确；第 15 题应能说出“向量化利用 C 底层/避免逐行 Python 调用”的结论。