# 第 11 章 上机实验（lab/）

> 本页是**第二部分上机的统一入口**。lab 采用三段式设计，保证"有网能练、断网也能练"。

| 段落 | 时长 | 内容 | 是否需要网络 |
| ---- | ---- | ---- | ---- |
| Part A 离线 | 1h | 环境自检、审查 `sample_agent_output/` 的预置产出物、为案例写验收脚本 | 否 |
| Part B 联网 | 2h | 用 dsh 完成三个递进任务（修 bug / 清洗出图 / 可复现实验） | 是（需 API Key） |
| Part C 综合 | 1h | 项目骨架 + 报告 + AI 使用声明 | 可选 |

## 目录说明

| 路径 | 内容 |
| ---- | ---- |
| `lab.ipynb` | 上机主文件（Part A 的代码单元可离线执行） |
| `data/` | 演示数据与待修脚本：`scores.csv`、`scores_dirty.csv`、`sensor.csv`、`scores_buggy.py` |
| `sample_agent_output/` | 一次真实运行的产物与脱敏会话记录：`scores_fixed.py`、`run_fix_session.txt` |

## 提交要求

- Part A：审查结论 + 你写的验收脚本 + 运行输出；
- Part B：每个任务的提示词、关键轨迹截图、最终产物与验证结果；
- Part C：项目目录 + 报告（LaTeX PDF）+ AI 使用声明。
