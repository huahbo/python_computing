# 9. AI Agent 编程基础

> 本页是**第二部分（AI Agent 编程）**第 9 章的章首页。
> 基线版本：dsh 0.1.5-rc.2（npm latest，2026-09-10 发布）；教材核对日期 2026-09-19；维护件见 `docs/build/dsh_version.yaml`。

## 本章概览

第一部分教会你用 NumPy、SciPy、Pandas、Matplotlib、NetworkX、Statsmodels、scikit-learn 做科学计算；从本章开始，我们换一个视角：**当 AI 能自己读文件、跑命令、改代码、看报错时，科学计算的工作方式会变成什么样？**

本章以 DeepSeek Harness（dsh）为例——一个"一切皆插件"的开源 agent harness，讲清三件事：它是什么（概念与循环）、怎么装起来（三条路径 + API Key）、怎么安全地用（权限与数据红线）。

## 学习目标

1. 说清代码补全、对话式编程与 Agent 编程的区别，描述一次 Agent 循环的五个动作；
2. 用"五件套"（模型、工具、上下文、权限、会话）解释一个 harness 的组成；
3. 独立完成 dsh 的三条安装路径之一（npx 免安装 / 全局 CLI / 桌面版源码构建）；
4. 完成 DeepSeek API Key 的注册、实名、充值、创建与填写，并估算一次任务的花费；
5. 会用界面与斜杠命令（`/plan`、`/compact`、`/goal`、`/model`、`/permission`、`/export` 等）控制会话；
6. 说出权限三档、审批机制与数据红线，知道什么数据不能交给云端模型。

## 先修要求与运行环境

- 先修：第 0 章（终端、Python 环境）与第 1 章 NumPy（本部分案例会用 axis、广播、形状判据）；
- 运行环境：Node.js `^22.19.0 || >= 24.0.0`（npm 与 npx 随它一起安装）、一个 DeepSeek 开放平台账号与 API Key；
- 详细安装步骤见本章 02 节；无 Key 时也能完成理论、审查类练习与离线替代路径。

## 本章结构

| 小节 | 内容 | 状态 |
| ---- | ---- | ---- |
| 01 AI 编程与 Agent 基础 | 三代工具、harness 五件套、循环、上下文、人机分工、失败模式 | 已交付 |
| 02 安装与配置 | Node.js 与 npm、三条安装路径、API Key 申请与付费、价格快照、故障排查 | 已交付 |
| 03 界面与斜杠命令 | Web 界面导览、斜杠命令速查与示例（本地执行 vs 模型对话） | 已交付 |
| 04 权限、安全与数据红线 | 权限三档、审批实践、数据红线与合规 | 已交付 |

## 资源导航

| 资源 | 位置 | 说明 |
| ---- | ---- | ---- |
| 理论篇 | [01-AI编程与Agent基础.md](./01-AI编程与Agent基础.md) | 概念、循环、上下文、权限、失败模式 |
| 安装与配置 | [02-安装与配置.md](./02-安装与配置.md) | 三条路径、API Key 与付费、成本估算、故障排查 |
| 参考资料 | [references.md](./references.md) | 官方文档、平台入口、通识材料 |
| 教学说明 | [teaching.md](./teaching.md) | 教师用：课时、演示脚本、常见坑 |
| 练习 | [../11-agent-cases/exercises/README.md](../11-agent-cases/exercises/README.md) | 全部分练习统一入口（quiz + assignment） |
| 上机 | [../11-agent-cases/lab/README.md](../11-agent-cases/lab/README.md) | 全部分上机入口（离线可跑 + 联网任务） |

## 版本与时效

本章内容与 dsh 版本强相关，因此有三层防护：

1. 版本单一事实源：`docs/build/dsh_version.yaml`（基线版本、核对日期、上游链接、需复核文件清单）；
2. 时效标记：正文中易变段落以"时效内容（基线 vX / 日期）"开头，便于批量复核；
3. 双周巡检：`docs/build/check_dsh_release.py` 与 `.github/workflows/dsh-release-watch.yml` 在官方发新版时提醒，流程见 `docs/build/dsh_更新SOP.md`。

## 常见问题

| 问题 | 处理 |
| ---- | ---- |
| 没有 API Key 能学吗？ | 能：本章理论、第 10 章方法、第 11 章全部审查与离线练习都不需要 Key |
| 一定要用 DeepSeek 吗？ | 教材以 DeepSeek Harness + DeepSeek 模型为主线；dsh 也支持自定义兼容端点 |
| 会不会很贵？ | 练习任务用 `deepseek-flash`，一次通常几分钱；估算方法见 02 节 |
