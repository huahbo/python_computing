# 成绩分析脚本（案例一用：这段代码有 2 个隐蔽的错误）
import numpy as np
import pandas as pd

df = pd.read_csv('data/scores.csv')
subjects = ['平时', '期中', '期末']
scores = df[subjects].to_numpy(dtype=float)

# 1) 每个学生的平均分（期望：8 个数，每个学生一个）
student_mean = scores.mean(axis=0)

# 2) 归一化到 0-1，用于画成绩对比图
norm = (scores - scores.min()) / (scores.max() - scores.min())

# 3) 加权总分：平时 20% + 期中 30% + 期末 50%
weights = np.array([0.2, 0.3, 0.5])
total = scores @ weights

print('每个学生的平均分:', np.round(student_mean, 2))
print('归一化矩阵形状:', norm.shape)
print('加权总分前 3 名:', np.round(total[:3], 2))
print('全班平均:', round(float(scores.mean()), 2))
