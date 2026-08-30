# 第 0 章 上机实验（lab/）

> 本章上机（4 学时）目标单一：把环境打通 + 把 Python 用起来 + 写出第一份 LaTeX 报告。

## 文件说明

| 文件 | 用途 |
| ---- | ---- |
| `lab.ipynb` | 上机主线：A 环境自检 → B Python 热身 → C 数据统计 → D LaTeX 报告 |
| `data/scores.csv` | 练习数据（20 名学生 × 3 门课，由生成脚本产生，可复现） |
| `output/` | 你在本目录下新建，存放 `result.txt`、`avg_scores.png` |

## 上机流程（建议 4 学时）

| 阶段 | 时间 | 任务 | 交付 |
| ---- | ---- | ---- | ---- |
| A 环境自检 | 0.5h | 运行 `教学资源/环境配置/check_env.py` | `env_check.txt` / 截图 |
| B Python 热身 | 1.5h | 完成 lab 1~8 小任务（切片/推导式/函数/文件/csv） | notebook 运行通过 |
| C 数据统计 | 1h | 读 `scores.csv`，统计、排名、写 `result.txt`、画简图 | `result.txt` + `avg_scores.png` |
| D LaTeX 报告 | 1h | 用课程模板写《成绩单统计报告》并编译 | `报告.pdf` |

## 提交清单

```text
学号_姓名_第0章_env_check.txt
学号_姓名_第0章_lab0.ipynb
学号_姓名_第0章_result.txt
学号_姓名_第0章_报告.pdf
```

## 常见提醒

- 先 `conda activate scicomp` 再跑 notebook；
- 图片保存用 `matplotlib.use("Agg")` 或 `plt.savefig`（机房无界面必备）；
- LaTeX 编译若失败，先看 00-05 常见错误表：大概率是没切 xelatex 或宏包没装；
- 全部完成后建议“重启内核并全部运行”一遍再提交。
