# 第 9 章 教学说明（教师用）

> 面向授课教师：课时建议、重点难点与考核建议。学生无需阅读本页。

## 1. 教学目标

1. 说清三代编程助手的差别与 Agent 循环；
2. 完成 dsh 安装（三条路径任选其一）；
3. 完成 API Key 申请、充值、配置与第一个任务；
4. 掌握权限三档与数据红线。

## 2. 建议课时

上课 2 学时（概念 + 安装演示）；上机 2 学时（环境与第一个任务）。

## 3. 重点与难点

- 环境前置（Node.js 与 npm）是本部分最大的上手门槛；
- 权限三档与审批的实践顺序；
- API Key 与计费概念（token、缓存命中、高峰与空闲）。

## 4. 常见坑（课堂重点提醒）

- 学生卡在 Node 版本或 PATH：课前收集 `node -v` / `npm -v` 截图；
- 未实名导致充值失败：提前一天发指引；
- 把练习写成"必须用 Agent"：明确无 Key 也能完成理论与审查作业。

## 5. 资源包

- 正文：01、02 节（03、04 节陆续交付）；
- 配图：images/（8 张概念图）；
- 参考资料：references.md；
- 版本盒：`docs/build/dsh_version.yaml`。

## 6. 课堂演示脚本（2 学时）

| 时段 | 内容 | 现场只敲这几条 |
| ---- | ---- | ---- |
| 0–15 min | 三代工具对比 + Agent 循环（01 节） | —— |
| 15–45 min | 现场安装：`npx @deepseek-ai/dsh web`（用备份环境演示） | `npx @deepseek-ai/dsh web` |
| 45–70 min | 配置模型 + 第一个任务（只读审阅仓库） | `/permission`（read-only） |
| 70–90 min | 斜杠命令速查 + 常见坑 | `/plan`、`/compact`、`/export` |
| 课后 | 提交环境自检输出 + 第一个任务的截图 | `node -v` / `npm -v` / `dsh --version` |

## 7. 时间不够时的压缩方案

- 只讲 01 节 + 02 节的路径 A（npx 免安装），桌面版与 headless 留给自学；
- 04 节（权限与数据红线）压缩为 10 分钟三条红线提醒；
- 斜杠命令只演示 `/plan`、`/compact`、`/export` 三条。

## 9. 可选：第 4 张界面截图（会话时间线）

现有 3 张界面图（首屏 / 设置→模型 / 工作区选择器）已足够支撑 03 节；若想再加一张"会话时间线"（一次真实任务里读文件→跑命令→看结果的流水），步骤：

1. 用**干净的演示环境**启动（已预置 Key 与一个演示工作区，不含个人会话）：

```powershell
$env:DSH_HOME = "C:/Users/Administrator/AppData/Local/Temp/dsh-demo/home"
cd C:/Users/Administrator/AppData/Local/Temp/dsh-demo/workspace
dsh web --port 3099
```

2. 在输入框左侧点「选择工作区」→ 选 `dsh-demo`；
3. 发一句只读任务（例如「读取 data/scores.csv，按行算每个学生平均分并打印」）；
4. 截取**对话区域**（不要包含左侧会话列表），存为 `images/shot_session_timeline.png`；
5. 重建：`python build/pdf_build.py 09-agent-basics && python build/part_pdf.py && python build/texbook.py --full`，并更新 `教材PDF/README.md` 页数。

> 说明：自动化脚本能完成前 3 张（`build/capture_dsh_shots.cjs`），但"选择工作区"的下拉菜单在无头浏览器里点不中，因此第 4 张需要人工截一次。
