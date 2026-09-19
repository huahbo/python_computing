# 成绩分析脚本（修复版）
# 相对 scores_buggy.py 的四处修改：
# 1) 学生平均分：mean(axis=0) 求的是「每门课的平均分」（3 个数），
#    应改为 axis=1，得到每个学生一个平均分（8 个数）；
# 2) 归一化：原来用全局 min/max，会把不同科目混在一起比较，
#    应改为逐列（每个科目分别）归一化；
# 3) 前 3 名：原来 total[:3] 只是前 3 个人，应按总分降序取前三并带上姓名；
# 4) 增加三条 assert 自检。
from pathlib import Path

import numpy as np
import pandas as pd

# 兼容两种运行方式：在项目根目录运行 python data/scores_fixed.py，
# 或直接运行 python scores_fixed.py
csv_path = Path(__file__).with_name('scores.csv')
if not csv_path.exists():
    csv_path = Path('data/scores.csv')

df = pd.read_csv(csv_path)
subjects = ['平时', '期中', '期末']
scores = df[subjects].to_numpy(dtype=float)

# 1) 每个学生的平均分（期望：8 个数，每个学生一个）—— 按行求均值
student_mean = scores.mean(axis=1)

# 2) 逐列归一化到 0-1（每个科目分别归一化），用于画成绩对比图
col_min = scores.min(axis=0)
col_max = scores.max(axis=0)
norm = (scores - col_min) / (col_max - col_min)

# 3) 加权总分：平时 20% + 期中 30% + 期末 50%
weights = np.array([0.2, 0.3, 0.5])
total = scores @ weights

names = df['姓名'].to_numpy()

print('每个学生的平均分（共 %d 个）:' % student_mean.size)
for name, value in zip(names, student_mean):
    print('  %-4s %.2f' % (name, value))

print('归一化矩阵形状:', norm.shape)
print('逐列归一化范围: min=%s max=%s'
      % (np.round(norm.min(axis=0), 4), np.round(norm.max(axis=0), 4)))

print('加权总分前 3 名:')
for rank, idx in enumerate(np.argsort(-total)[:3], start=1):
    print('  第 %d 名 %-4s 加权总分 %.2f' % (rank, names[idx], total[idx]))

print('全班平均:', round(float(scores.mean()), 2))

# ---------------- 自检 ----------------
# 自检 1（形状）：平均分是 8 个数（每生一个），归一化矩阵与原成绩矩阵同为 (8, 3)
assert student_mean.shape == (len(df),), student_mean.shape
assert norm.shape == scores.shape == (8, 3), norm.shape

# 自检 2（逐列归一化范围）：每一列的最小值为 0、最大值为 1，且整体落在 [0, 1]
assert np.allclose(norm.min(axis=0), 0.0), norm.min(axis=0)
assert np.allclose(norm.max(axis=0), 1.0), norm.max(axis=0)
assert np.all((norm >= 0.0) & (norm <= 1.0)), norm

# 自检 3（加权总分最高分是王五）
best = int(np.argmax(total))
assert names[best] == '王五', names[best]
assert float(total[best]) == float(total.max()), total[best]

print('自检通过：形状 / 逐列归一化范围 / 加权总分最高分为王五')
