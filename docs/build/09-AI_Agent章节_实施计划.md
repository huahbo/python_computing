# 第 9 章《AI Agent 编程（DeepSeek Harness）》实施计划

> 状态：**待批准**（批准后才动正文文件；本计划文件本身先落盘存档）
> 编写日期：2026-09-19
> 基线版本：dsh 0.1.5-rc.2（npm latest，2026-09-10 发布）／官方最新 tag 0.1.6-alpha.2（2026-09-17）
> 上游依据：deepseek-ai/deepseek-harness（Developer Preview，全部 tag 均为 prerelease）

---

## 0. 已确认的决策（不再讨论）

| # | 决策 | 结论 |
| --- | --- | --- |
| 1 | 章节定位 | 新增**第 9 章**（拓展章，期末大作业加速器），不挤占主线 8 周 48 学时 |
| 2 | 学时 | 2h 讲授 + 4h 上机（选做，+6 学时）；排不下时压缩为 2h 演示 + 课后自学 lab |
| 3 | Web 版／本地版 | 解读 A：npx 免安装 Web 版 vs 全局安装 CLI 版（含 headless 脚本化）；桌面版单列 |
| 4 | 模型与密钥 | 学生自备 DeepSeek API Key；教材含申请／付费／发票／安全全流程；本地 Ollama 仅作可选兜底 |
| 5 | 案例规模 | 4 个主案例 + 1 个综合案例 + 1 个教师预置「翻车现场」 |
| 6 | 是否进全书 | 进 book.yaml、_sidebar.md、学习指南、课时表、pdf_manifest.txt，出 PDF 与 TeX |
| 7 | AI 使用声明 | 要求学生提交提示词记录 + 人工修改说明 + AI 使用声明，计入评分 |
| 8 | 实测授权 | 允许实测最少案例（deepseek-flash，限轮次，预估花费 ≤ 2 元，实测后报告实际消耗） |
| 9 | 更新机制 | 版本单一事实源 + 检查脚本 + 时效标记 + **双周**定时 CI（每月 1 日、15 日）+ 更新 SOP |
| 10 | 配图 | 8 张脚本生成概念图 + 4 张真实界面截图，并提供重截手段 |

---

## 1. 目标与范围

### 做

1. 面向**第一次接触 Agent 编程**的本科生，讲清「补全 → 对话 → Agent」的差异、harness 组成、一次 Agent 循环、上下文约束、权限与安全、四种失败模式。
2. 给出**三路径安装**（免安装 Web 版／全局 CLI 版／桌面版）与 **API Key 申请—实名—充值—建 key—填入 dsh** 全流程（含价格快照、发票、退款、key 安全）。
3. 用 4 个由浅入深的案例把第 0–8 章的知识接上：**验收标准全部取自前 8 章学过的判据**（广播形状、残差与条件数、行数守恒、种子可复现、p 值与交叉验证）。
4. 交付完整教学资产：正文、案例、8 张概念图、4 张截图、exercises（quiz + assignment + answers）、lab、teaching、references、PDF/TeX 集成。
5. 交付**抗过期机制**：版本单源 + 双周检查 + 更新 SOP，让维护时每次只改一处。

### 不做（明确排除）

- 不写 dsh 插件开发（体量等同另一门课）；
- 不写本地大模型部署教程（仅在「离线兜底」小节给 Ollama + OpenAI 兼容端点的一句话选项）；
- 不做 Agent 产品横向评测（理论篇用一张表点到同类工具的存在即可）。

---

## 2. 章节身份

| 项 | 值 |
| --- | --- |
| 目录 | docs/chapters/09-agent/ |
| 章名 | AI Agent 编程：以 DeepSeek Harness 为例 |
| sidebar 条目 | - [9 AI Agent 编程](./chapters/09-agent/README.md) |
| PDF 标题（pdf_manifest.txt 的 TITLE） | AI Agent 编程（DeepSeek Harness） |
| 预期 PDF | docs/教材PDF/09-agent-AI Agent 编程（DeepSeek Harness）.pdf，24–32 页 |
| 正文字数 | 约 2.5–3.5 万字（与第 3、8 章同量级） |
| 课时定位 | 第 9 周（拓展，选做）或期末项目启动周；课表标注「选做，不占主线 48 学时」 |

---

## 3. 产物清单

### 3.1 内容（docs/chapters/09-agent/）

~~~
README.md                            章首页：概览/目标/先修/案例索引/课时/资源入口
01-AI编程与Agent基础.md               理论篇
02-安装与配置.md                      三路径安装 + API Key 申请与付费 + 版本盒
03-Agent工作流与核心能力.md            工作流篇
04-案例一-读懂与修复NumPy代码.md
05-案例二-数据清洗与可视化流水线.md
06-案例三-可复现实验与自动验证.md
07-案例四-端到端小项目与报告.md
08-常见误区与科研规范.md
teaching.md                          教师用：课时/演示脚本/断网兜底/评分 rubric
references.md                        官方文档 + 教程 + 社区资料
pdf_manifest.txt                     合订清单（TITLE + 上述正文顺序）
dsh_version.yaml                     ★ 版本单一事实源（抗过期机制的输入）
exercises/README.md
exercises/quiz.ipynb                 自测 10 题（概念 4 + 审查 4 + 实操 2）
exercises/answers.ipynb              答案版
exercises/assignment.md              作业 12 题（含 AI 使用声明模板）
lab/README.md
lab/lab.ipynb                        上机：离线可跑 + 联网任务两段式
lab/data/                            演示数据（脏数据 CSV、脚本样例、故障代码）
lab/sample_agent_output/             预置「Agent 产出物」（供离线练习与断网兜底）
images/                              8 张概念图 + 4 张截图
~~~

### 3.2 脚本（docs/build/）

| 文件 | 作用 |
| --- | --- |
| make_chap9_figures.py | 生成 8 张概念图（matplotlib + fonts.py 中文字体） |
| make_chap9_lab.py | 生成 lab/lab.ipynb（离线可跑，符合 run_labs.py 约束） |
| make_chap9_quiz.py | 生成 exercises/quiz.ipynb 与 answers.ipynb |
| check_dsh_release.py | 拉 npm dist-tags + GitHub Releases 与 dsh_version.yaml 比对，输出需复核文件清单与 release notes 摘要；支持 --ci |
| capture_dsh_shots.mjs | 用 Playwright 对本地 dsh Web UI 截 4 张图（实施时先做可行性验证，不可行则降级为截图 SOP + 手工复核清单） |
| dsh_更新SOP.md | 更新标准作业流程（八步） |

### 3.3 CI

| 文件 | 作用 |
| --- | --- |
| .github/workflows/dsh-release-watch.yml | **双周**（每月 1 日、15 日 09:00 北京时间）运行检查脚本；发现新版本自动开 Issue（含更新 checklist），并上传报告 artifact |

### 3.4 集成改动（逐文件，均为小改）

| 文件 | 改动 |
| --- | --- |
| docs/_sidebar.md | 第 8 章后插入第 9 章分组（README + 8 篇正文 + 练习 + 上机 + 参考） |
| docs/0-学习指南.md | 课表加「第 9 周（拓展·选做）」行；正文列表加第 9 章 |
| docs/教学资源/课时安排总表.md | 总览加「拓展章 6 学时（选做）」；逐周表加第 9 章行；说明期末项目可用第 9 章工具链 |
| docs/build/book.yaml | chapters 末尾加 09-agent |
| docs/教材PDF/README.md | 表格加第 9 章 PDF 行（构建后填页数） |
| docs/教学资源/README.md、docs/README.md | 若有章节清单则同步（实施时逐处核对，无则不改） |

---

## 4. 内容设计

### 4.1 01-AI编程与Agent基础.md（理论篇，约 6000 字）

1. 三代工具的区别：代码补全（猜下一行）／对话式编程（给片段、你自己搬）／**Agent 编程**（读文件、跑命令、看报错、改代码、再验证的闭环）。
2. harness 是什么：模型 + 工具 + 上下文 + 权限 + 会话；为什么「会调工具」与「会聊天」是两回事；同类工具一览（一张表，点到为止）。
3. 一次 Agent 循环的解剖（读 → 想 → 调工具 → 观察 → 再想 → 交付），配循环图；上下文窗口与压缩的现实约束（1M 上下文也会满）。
4. 人机分工：交给它的（样板代码、重构、写测试、查文档、批量改）／必须人管的（问题定义、验收标准、数值合理性、结论）。
5. 权限与安全：read-only／workspace-write／danger-full-access 三档 + 审批；工作区边界。
6. 四种失败模式与对策：幻觉 API、静默数值错误、过度自信的结论、改坏别处。
7. 本章学习路径图（与后面案例对应）。

### 4.2 02-安装与配置.md（约 7000 字，全章时效内容集中地）

- **章首版本盒**：基线版本／核对日期／官方来源链接／「以官方为准」声明。
- **路径决策表**：只想用 → npx 免安装；长期用或要脚本化 → 全局 CLI；要原生窗口与自带运行时 → 桌面版。
- **路径 A（免安装 Web 版）**：Node 版本要求（^22.19.0 或 >=24）→ npx @deepseek-ai/dsh web → 默认 127.0.0.1:3080、--port／--no-open；首次下载慢的原因与镜像加速提示。
- **路径 B（全局 CLI 版）**：npm i -g @deepseek-ai/dsh → dsh web／dsh --profile headless 「任务」（脚本化、无界面）／dsh --help 与 --dump-config 自查；升级与卸载。
- **路径 C（桌面版）**：明确「官方未提供预编译安装包」；源码构建（Node ≥22.19、pnpm 11.7、整仓 pnpm install + pnpm run build，再 package:desktop:win:x64／mac:arm64／mac:x64，开发启动 dev:desktop）；桌面端特性（端口 19387、自带 Python/Node/pnpm 运行时）；第三方社区安装包的风险提示。
- **API Key 申请与付费（重点节）**：注册 → 实名（个人／企业）→ 充值（支付宝／微信；对公仅企业）→ 建 key → 填入 **设置 → 模型**；价格快照表（deepseek-flash／deepseek-v4-pro，缓存命中与未命中，高峰／空闲半价）；账单、发票（按消耗或充值、普票／专票、抬头规则）、退款与余额有效期；key 安全（只显示一次、不进 git、泄漏即删重建、按 key 查用量）。
- **成本意识练习**：估算一次案例任务的 token 与花费，并对比空闲时段省钱。
- **常见安装故障排查表**（Node 版本、npm 权限、端口占用、公司代理、Windows PowerShell 执行策略、key 填错位置）。

### 4.3 03-Agent工作流与核心能力.md（约 5000 字）

- 项目级指令 AGENTS.md：写什么、放哪里、为什么比每次重复提示更可靠。
- 计划先行（plan mode）与会话管理（新建／继续／压缩，会话即上下文）。
- 权限与审批实践：先 read-only 读一遍，再放开写；高风险命令的确认习惯。
- 技能（skills）与工具（tools）的差别：能力扩展与调用方式。
- 子代理（subagent）：什么时候分工（探索、并行、评审），什么时候不用（小任务反而更贵）。
- 记忆与检索（MCP 等扩展的定位，点到为止）。
- **验证驱动工作流（本章核心）**：任务卡六件套 = 目标／约束／验收标准／证据／复核／提交；把「你怎么知道它是对的」变成固定动作。
- 提示词写法：贴数据样例、给判据、要求打印中间量、要求写测试、要求给出不确定性。

### 4.4 案例一～案例四（约 9000 字）

统一采用**任务卡骨架**（与其它章的案例卡对齐，但适配 Agent）：

~~~
目标 / 场景与数据 / 给 Agent 的提示词（原文） / Agent 执行轨迹（示例，标注版本与日期）
/ 产物 / 验收标准（可执行）/ 人工复核点 / 常见坑 / 离线替代路径 / 拓展
~~~

| 案例 | 主题 | 复用章节 | 能力层级 | 验收标准（硬指标） |
| --- | --- | --- | --- | --- |
| 一（04） | 一段「能跑但结果错」的 NumPy 代码：解释错在哪 + 给最小复现 | 第 1 章 | L1 只读不改 | 复现脚本输出与手算一致；能指出 Agent 解释中的错误句 |
| 二（05） | 脏数据清洗 + 出图 + 结果表 | 第 4、5 章 | L3 多文件 | 行数守恒；缺失策略显式记录；图符合第 5 章规范、随机种子固定 |
| 三（06） | 可复现实验：假设 → 检验／建模 → 自动验证 | 第 3、7 章 | L4 项目级 | 重跑结果一致；p 值与置信区间解释正确；报告含局限与不确定性 |
| 四（07） | 端到端小项目：建模 + 评审代理 + LaTeX 报告 | 第 0、6、8 章 | L5 多角色 | 交叉验证指标 + 数据泄漏检查 + 评审意见逐条回应 + git 提交 |
| 预置「翻车现场」 | 教师给的错误结论（用错 axis／R² 当准确率／数据泄漏），学生抓错并写进报告 | 全部 | 审查 | 找出全部植入问题并说明判据 |

每个案例都提供**离线替代路径**（用 lab/sample_agent_output/ 的预置产出物做同样的审查与验收练习），保证断网、无 key、机房限流时也能上课。

### 4.5 08-常见误区与科研规范.md（约 3500 字）

- 误区清单（≥12 条）：把 Agent 当搜索引擎、不给验收标准、一次要求改太多文件、不看 diff 就接受、把敏感数据贴进去、盲信图表、混淆「跑通」与「正确」、忘记固定种子、忘记记录版本、把 key 写进 notebook、让 Agent 直接改原始数据、评审缺位。
- 科研规范：AI 使用声明模板、提示词与产物归档、可复现性三件套（版本锁定 + 种子 + 环境）、署名与贡献界定、学术诚信红线。
- 成本与效率：什么时候不该用 Agent（一行代码、明确的小改、需要严格保密的场景）。

### 4.6 练习／上机／教学／参考

- exercises/quiz.ipynb 10 题：概念 4（harness 组成、工具调用、上下文、权限）＋审查 4（给 Agent 的对话与产出，找错并说判据）＋实操 2（限时小任务，提交记录与验证脚本）。
- exercises/assignment.md 12 题：含「给我自己的任务写验收标准」「为一个科学计算任务写 AGENTS.md」「审查一份 Agent 报告」等，附 **AI 使用声明模板**。
- lab/lab.ipynb 三段式：Part A 离线（环境自检 + 审查预置产出物 + 写验收脚本，**全部可无网运行**）；Part B 联网（用 dsh 完成 3 个递进任务，以 markdown 单元记录，不参与自动执行）；Part C 综合（做成可提交的项目骨架 + 报告）。
- teaching.md：2h 讲授逐段脚本（含现场只敲 3 条命令的演示设计）、4h 上机巡场要点、断网／无 key 兜底方案、评分 rubric（正确性／验证充分性／使用规范性／报告质量）、易错点清单。
- references.md：官方文档（README、Web UI 指南、模型配置、CLI 参考、Releases）、DeepSeek 开放平台与定价页、Agent 编程通识材料、学术诚信与 AI 使用规范参考。

---

## 5. 配图清单

### 5.1 概念图（8 张，make_chap9_figures.py 生成，长期有效）

1. agent_vs_completion.png —— 补全／对话／Agent 三代对比
2. agent_loop.png —— 一次 Agent 循环解剖
3. harness_anatomy.png —— harness 五大件
4. context_window.png —— 上下文窗口与压缩
5. install_paths.png —— 三路径安装决策树
6. permission_flow.png —— 权限档位与审批流
7. api_key_flow.png —— API Key 获取到配置链路
8. subagent_split.png —— 案例四的子代理分工

### 5.2 截图（4 张，随版本可能过期）

1. shot_web_home.png —— Web UI 首屏／工作区选择
2. shot_settings_model.png —— 设置 → 模型（填 key）
3. shot_permission_dialog.png —— 权限审批弹窗
4. shot_session_timeline.png —— 会话工具调用时间线

要求：使用**干净演示工作区**（不含个人路径与会话内容）；每张图注标注「基线版本 + 截图日期」；集中在 02／03 章使用。

---

## 6. 抗过期机制

1. **单一事实源** docs/chapters/09-agent/dsh_version.yaml：基线版本、渠道、发布日期、核对日期、Node 要求、上游 URL（npm／GitHub／文档站／定价页）、需复核文件清单。
2. **时效标记**：所有易变段落统一加一行「⏱ 时效内容（基线 v0.1.5-rc.2 / 2026-09-19）」，更新时一次搜索列全。
3. **检查脚本** check_dsh_release.py：对比 npm dist-tags（latest／next／alpha）与 GitHub Releases，输出新版本、日期、release notes 摘要、命中时效标记的文件清单；--ci 模式供流水线使用。
4. **双周 CI**：每月 1 日、15 日 09:00（北京时间）运行；有新版本则开 Issue（标题含版本号，正文附更新 checklist），并上传报告 artifact；已存在同名开启 Issue 时不重复创建。
5. **更新 SOP** dsh_更新SOP.md：八步（跑脚本 → 读 release notes → 改 02 章与版本盒 → 复核／重截 4 张截图 → 重跑关键示例 → 更新 dsh_version.yaml → 重出 PDF/TeX → 提交并关闭 Issue）。
6. **写作分层**：概念（01 章，几乎不变）／工作流（03、08 章，半年级）／命令界面价格（02 章，月级），降低更新面。

---

## 7. 写作与校验规范（硬约束）

1. **只让可离线运行的学生侧脚本使用 python 围栏**：validate_code.py 会顺序执行章节内所有 python 块并比对紧随其后的输出块；因此 Agent 提示词一律用 text 围栏，命令行用 sh 围栏，Agent 输出用 text 围栏且不与 python 块配对。
2. Agent 输出**不承诺逐行可复现**，统一写成「示例输出（基线 vX / 日期）」，并在章首声明；可复现的是**验收脚本与结论**。
3. lab/lab.ipynb 的所有 code 单元必须能在无网络、无 dsh、无 API Key 的环境下执行（run_labs.py 用 exec 直接跑全部 code 单元）；联网任务只放在 markdown 单元说明。
4. 所有事实性数字（版本号、价格、限额）标注来源与核对日期；价格与政策一律「快照 + 官方链接」。
5. 术语首次出现给中英对照（agent harness／tool call／context／compaction／permission／MCP／skill／subagent）。
6. **写入方式约定**（规避本机工具链的转义坑）：本轮已确认 run_code 写入文本时不能直接携带三反引号，故实施阶段生成含围栏的正文时，一律用 chr(96) 拼接或占位符后替换（仓库既有脚本 pdf_build.py 就是这么做的），并在每次写入后用校验脚本确认围栏数量与 validate_code 识别结果一致。

---

## 8. 里程碑与验收

| 里程碑 | 内容 | 验收命令／证据 |
| --- | --- | --- |
| **M1 理论与安装** | 01、02（含 API Key 付费、桌面版）、dsh_version.yaml、8 张概念图 | python build/make_chap9_figures.py 成功出图；人工试读安装章按步骤可跑通（我在本机实测两条路径） |
| **M2 工作流与案例** | 03、04–07（含 2 个最小案例实测记录与花费报告） | 案例中的 python 验收脚本可跑；实测记录含版本、日期、耗时、token 与花费 |
| **M3 练习与教学资产** | exercises/*、lab/*、teaching.md、references.md、08 | python build/run_labs.py 09-agent 通过；notebook JSON 合法 |
| **M4 构建集成** | _sidebar.md、0-学习指南.md、课时安排总表.md、book.yaml、pdf_manifest.txt、教材PDF/README.md | gen_manifest.py + validate_book.py + validate_code.py --strict 09-agent 全绿；pdf_build.py 09-agent 出 PDF；update_all.py --tex 出全书 PDF 与 TeX |
| **M5 更新机制** | check_dsh_release.py、dsh-release-watch.yml、dsh_更新SOP.md | 本地运行脚本输出正确比对结果；workflow 语法校验通过（首次手动触发验证） |
| **M6 截图与总验收** | 4 张截图 + 全文校验 + 推送 | 截图落地且图注含版本日期；validate_code --strict 与 validate_book 全绿；出 PDF；push 后三条 workflow 绿（pages／texbook／dsh-release-watch） |

> 实施顺序为 M1→M6；每个里程碑完成后我汇报一次（含命令输出摘要与截图），你随时可叫停。

---

## 9. 风险与回滚

| 风险 | 影响 | 对策 |
| --- | --- | --- |
| dsh 版本迭代导致命令与界面变化 | 02 章与截图过期 | 版本盒 + 时效标记 + 双周 CI + SOP；改动集中在一章一节 |
| Agent 输出非确定性 | 与全书「输出逐行核验」约定冲突 | 章首声明 + 只核验 python 验收脚本 + 示例输出标注版本日期 |
| CI 无 API Key | 无法自动跑 Agent 案例 | Agent 案例不进 CI；CI 只跑离线脚本、PDF 构建与版本巡检 |
| 截图包含隐私信息 | 泄漏个人路径与会话 | 专用干净演示工作区；截图前人工复核 |
| 实测花费超预期 | 额度消耗 | 仅 2 个最小案例、deepseek-flash、限制轮次，预估 ≤ 2 元，实测后报告 |
| Playwright 重截脚本不可用 | 截图无法一键重做 | 实施时先做 10 分钟可行性验证；不可用则降级为截图 SOP + 手工复核清单 |
| 本机 pandoc／xelatex 缺失 | 出不了 PDF | M4 第一步先探测工具链，缺失则改为纯 Markdown 验收 + 交给 CI 出 PDF |

**回滚**：本计划全部改动集中在新增目录 docs/chapters/09-agent/ 与少量集成文件；如需回退，git revert 对应提交或删除该目录并还原 5 个集成文件即可，不影响第 0–8 章。

---

## 10. 工作量估算

| 阶段 | 主要产物 | 预估 |
| --- | --- | --- |
| M1 | 2 篇正文 + 1 个配置文件 + 1 个图脚本（8 图） | 1 个工作会话 |
| M2 | 1 篇工作流 + 4 个案例 + 实测 | 1–2 个工作会话 |
| M3 | quiz／answers／assignment／lab + teaching + references + 规范篇 | 1 个工作会话 |
| M4 | 集成改动 + 构建 + 修校验 | 0.5 个工作会话 |
| M5 | 检查脚本 + CI + SOP | 0.5 个工作会话 |
| M6 | 截图 + 总验收 + 推送 | 0.5 个工作会话 |

合计约 4.5–5.5 个工作会话，新增正文 2.5–3.5 万字、脚本约 800–1000 行、图 12 张。

---

## 11. 待批准

请确认本计划（尤其第 2 节的章节身份、第 4 节的内容切分、第 8 节的里程碑顺序）。批准后我从 **M1** 开始，逐里程碑汇报；未获批准前不创建任何第 9 章正文文件。
