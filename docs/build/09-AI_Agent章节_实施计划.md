# 第 9–12 章《AI Agent 编程》第二部分 实施计划 v2

> 状态：**已批准执行**（2026-09-19 用户确认两项结构决策与三项细节）
> 基线版本：dsh 0.1.5-rc.2（npm latest，2026-09-10）；教材核对日期 2026-09-19
> 上游：deepseek-ai/deepseek-harness（Developer Preview，全部 tag 均为 prerelease）

## 0. 已确认决策（不再讨论）

| # | 决策 | 结论 |
| --- | --- | --- |
| 1 | 教材结构 | **两部分**：第一部分 Python 科学计算（第 0–8 章 + 附录）；第二部分 AI Agent 编程（第 9–12 章） |
| 2 | 第二部分章数 | **4 章**：基础 / 工作流与验证 / 案例实战 / 工程化与持续演进 |
| 3 | 实现方案 | **A′**：4 个章节目录 + `book.yaml` 的 `parts` 分组 |
| 4 | 章节编号 | **全局连续 第 9–12 章** |
| 5 | 学时定位 | **2 周 12 学时**独立模块（可压缩为 6 学时选修） |
| 6 | 新增 Project 3 | 与期末大作业并列 |
| 7 | 斜杠命令 | 作为**第 9 章新增小节**（速查表 + 3 例 + 2 坑），纳入版本复核清单 |
| 8 | 案例深化 | **三层结构**（基础 / 变体 / 挑战）+ 实验记录（耗时与花费）；不设页数上限 |
| 9 | 目录名 | `09-agent-basics` / `10-agent-workflow` / `11-agent-cases` / `12-agent-engineering` |
| 10 | 索引防线 | 新增 `build/check_indexes.py`，纳入 `update_all.py` 与 CI |
| 11 | 维护件归位 | `dsh_version.yaml` 迁到 `docs/build/`（教材正文保留学生可见"版本盒"） |
| 12 | 收尾待办 | 实施全部完成后，修复 Hindsight 记忆库 401（API key required）问题 |

## 1. 目标与范围

### 做

1. 把原有 AI Agent 章节拆成 4 个章节目录（见第 2 节映射表），教材升级为两部分结构；
2. 第二部分四章：基础（含安装、API Key、桌面版、界面与斜杠命令、权限安全）、工作流与验证（AGENTS.md、计划、任务卡、验收标准库、误区与科研规范）、案例实战（四个案例三层深化 + 翻车现场 + 实验记录）、工程化与持续演进（版本与时效管理、成本协作合规、综合项目 Project 3）；
3. 构建链支持 `\part`、部分封面与**部分合并 PDF**；
4. 索引防线：`check_indexes.py` 交叉核对 sidebar / book.yaml / 章节目录 / manifest / 教材PDF 表格 / 实际 PDF；
5. 更新机制（版本巡检 + 双周 CI + SOP）落地，并成为第 12 章 01 节的教学内容。

### 不做

- dsh 插件开发；本地大模型部署教程；Agent 产品横向评测（理论篇一张表点到为止）。

## 2. 章节身份与文件映射

| 章 | 目录 | 文件 | 来源 |
| --- | --- | --- | --- |
| 9 AI Agent 编程基础 | `09-agent-basics/` | README · 01-AI编程与Agent基础 · 02-安装与配置 · 03-界面与斜杠命令 · 04-权限安全与数据红线 · references · teaching · images · pdf_manifest | 01/02/图搬入；03/04 新写 |
| 10 Agent 工作流与验证方法 | `10-agent-workflow/` | README · 01-项目级指令与计划模式 · 02-任务卡与验收标准库 · 03-子代理技能与工具 · 04-常见误区与科研规范 · references · teaching · images · pdf_manifest | 由原 03 拆分 + 新写 04 |
| 11 案例实战 | `11-agent-cases/` | README · 01–04 四个案例 · 05-翻车现场与对抗练习 · 06-实验记录与成本 · exercises/ · lab/ · references · teaching · images · pdf_manifest | 04–07 搬入并深化；lab/data 与 sample_agent_output 搬入 |
| 12 工程化与持续演进 | `12-agent-engineering/` | README · 01-版本与时效管理 · 02-成本协作与合规 · 03-综合项目 Project 3 · references · teaching · pdf_manifest | 全新 |

**命名硬规则**：目录 `NN-英文短名`；章内文件 `NN-中文标题.md`（两位数字前缀是 `validate_code` 扫描依据）；跨章引用一律写"第 N 章 NN 节"；图片权威副本在第 9 章 `images/`，由生成脚本复制到需要它的章。

## 3. 索引风险与防线

| # | 类别 | 处理 |
| --- | --- | --- |
| 1 | 文件内相对链接（图 / 练习 / 上机 / 参考） | 迁移脚本重写；`validate_book` 卡口（missing links 必须为 0） |
| 2 | 正文交叉引用（"下一节：02-…"、"见 02 节第 5 小节"） | 统一改写为"第 N 章 NN 节"；末尾 grep 复核 |
| 3 | 脚本硬编码路径（`make_chap9_figures.py` / `make_chap9_data.py`） | 脚本改名并指向新目录 |
| 4 | 构建索引（book.yaml / manifest / 附录 G / 教材PDF 表 / CI artifact glob） | 逐一补齐；**CI glob 现漏 10/11/12 章 PDF，必须修** |
| 5 | 导航索引（sidebar / 学习指南 / 课表 / 根 README / 绪论） | 改为两部分结构 |
| 6 | 维护件位置（`dsh_version.yaml`） | 迁到 `docs/build/`，同步巡检脚本与正文引用 |
| 7 | 图片归属（跨章复用） | 权威副本第 9 章；脚本复制 |
| 8 | 附录 G 章名行 | `gen_references.py` 自动生成，确认排序 09–12 接在 08 之后 |

**三道防线**

1. `validate_book.py` + `validate_code.py --strict`（现成）；
2. `build/check_indexes.py`（新增）：交叉核对 `_sidebar.md` ↔ `book.yaml(parts)` ↔ `chapters/*` ↔ 各章 `pdf_manifest.txt` ↔ `教材PDF/README.md` 表格 ↔ 实际 PDF 文件；
3. 里程碑前后各跑一次全量命令并对比输出（贴给用户）。

## 4. 构建链改动

| 文件 | 改动 |
| --- | --- |
| `book.yaml` | 新增 `parts:`（第一部分 0–8 章；第二部分 9–12 章）；`chapters` 保持为权威扁平列表（向后兼容） |
| `texbook.py` | 按 `parts` 在每部分首章前插入 `\part{标题}` |
| `emit_tex.py` | 同上；`split_chapters()` 处理 `\part{` 边界，避免部分标题被切进上一章 |
| `part_pdf.py`（新增） | 合并某一部分各章 PDF + 生成部分封面页 → `教材PDF/第二部分-AI-Agent编程.pdf` |
| `update_all.py` | 编排中插入 `check_indexes.py` 与部分 PDF 步骤 |
| `.github/workflows/texbook.yml` | artifact glob 修正为覆盖 `1*-*.pdf`（10/11/12 章） |

## 5. 里程碑

| 里程碑 | 内容 | 验收 |
| --- | --- | --- |
| **M2.5 结构迁移** | 4 目录；文件搬运与重命名；book.yaml parts；`\part` 支持；CI glob；sidebar/学习指南/课表/教材PDF README；`check_indexes.py`；`dsh_version.yaml` 迁位 | **内容零改动**；6 条命令全绿；`check_indexes` 通过 |
| **M2.6 内容增补与深化** | 第 9 章 03/04 两节；第 10 章拆分与验收标准库；第 11 章案例三层深化 + 05/06；第 12 章三节 | 各章 `validate_code --strict` 通过；实测记录（预计 < 0.05 元） |
| **M3 练习与教学** | `11-agent-cases/exercises`（quiz 10 + assignment 12 + 答案）、`lab/`（三段式、离线可跑）、4×teaching、4×references | `run_labs.py` 通过；notebook JSON 合法 |
| **M4 构建集成** | 4 章 PDF + 部分 PDF + 全书 PDF + TeX（含 `\part`） | `pdf_build` / `update_all --tex` 通过；`教材PDF/README.md` 回填页数 |
| **M5 更新机制** | `check_dsh_release.py` + 双周 CI + SOP（成为第 12 章 01 节教学内容） | 脚本本地跑通；CI 手动触发成功 |
| **M6 截图与总验收** | 4 张界面截图 + 全量校验 + push | 三条 workflow 绿；索引检查通过 |
| **M7 综合项目** | Project 3 说明与模板（并入 `教学资源/期末大作业/`） | 与第 11 章 lab 打通、链接可点 |
| **M8 收尾** | 修复 Hindsight 401；复盘与文档同步 | 记忆库可用；`PROGRESS.md` 更新 |

## 6. 风险与回滚

| 风险 | 对策 |
| --- | --- |
| 拆分导致交叉引用大批失效 | 迁移脚本 + `validate_book` + `check_indexes` + 末尾 grep 复核 |
| 构建链改动引入回归 | 先做最小实现（parts + `\part`），跑通 `update_all.py --tex` 再迁移内容 |
| 第二部分稀释科学计算主线 | 第 11 章每案强制复用第 1–8 章判据；第 10 章明确"方法课，不是工具课" |
| 时效性（dsh 迭代快） | 第 12 章把维护机制制度化；版本盒 + 双周巡检 + 更新 SOP |

**回滚**：M2.5 为纯搬迁，可 `git revert` 单次提交回退；M2.6 之后按章回退，不影响第一部分。
