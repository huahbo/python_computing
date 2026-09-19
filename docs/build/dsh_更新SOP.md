# dsh 更新 SOP（八步）

> 目标：官方发布新版本后，用**固定流程**在 30 分钟内完成教材复核与更新，避免遗漏与返工。
> 触发方式：双周自动巡检 Issue（`.github/workflows/dsh-release-watch.yml`）或手动执行。

## 0. 触发与分工

| 项 | 说明 |
| ---- | ---- |
| 触发 | 双周巡检（每月 1、15 日 09:00 北京时间）自动开 Issue；或手动 `python docs/build/check_dsh_release.py` |
| 执行人 | 教材维护者（任课教师或其指定助教） |
| 产出 | 更新后的正文 + `dsh_version.yaml` + 重建的 PDF + 关闭 Issue |

## 步骤 1：跑巡检脚本

```bash
cd docs
python build/check_dsh_release.py            # 人类可读报告
python build/check_dsh_release.py --ci       # 写报告文件；有新版本时退出码 3
```

关注三点：npm `latest` 是否变化、Release notes 里的**破坏性变更**、以及报告列出的"需要复核的文件"。

## 步骤 2：读 Release notes，标记影响面

打开报告的"最新一条更新说明（节选）"，把条目分成三类：

| 类别 | 例子 | 处理 |
| ---- | ---- | ---- |
| 命令与参数 | 新增/改名某个 CLI 参数 | 必须改第 9 章 02/03 节 |
| 界面与菜单 | 设置项位置、斜杠菜单分组 | 改第 9 章 03 节，并重截截图 |
| 模型与价格 | 模型上下线、调价 | 改第 9 章 02 节价格快照与第 12 章成本节 |
| 与教学无关 | 内部重构、插件开发 API | 记录一句即可，不改正文 |

## 步骤 3：一次找出所有时效内容

```bash
grep -rn "时效内容（基线" chapters/ | cut -d: -f1 | sort -u
```

这些文件就是"必须复核"的清单，与 `dsh_version.yaml` 的 `review_on_change` 相互印证。

## 步骤 4：按清单修改正文

- 命令与界面：以官方文档站为准；
- 价格：以官方定价页为准，注明核对日期；
- 版本号：正文中的基线版本统一替换。

## 步骤 5：更新版本单一事实源

编辑 `docs/build/dsh_version.yaml`：

| 字段 | 改成 |
| ---- | ---- |
| baseline.version | 新的 `latest` 版本号 |
| baseline.released_at | 该版本发布日期 |
| baseline.checked_at | 本次核对日期 |
| review_on_change | 如章节结构调整，同步更新路径 |

## 步骤 6：复核 / 重截截图

第 9 章 03 节的 4 张界面截图：用干净演示工作区重截，图注更新为新的基线版本与日期。

## 步骤 7：重建与自检

```bash
cd docs
python build/pdf_build.py                     # 或指定章：python build/pdf_build.py 09-agent-basics
python build/part_pdf.py                      # 部分合并 PDF
python build/texbook.py --full                # 全书
python build/validate_book.py
python build/validate_code.py 09-agent-basics --strict
python build/check_indexes.py
python build/check_pdf_layout.py              # 版式自检：越界图片 / 超行
```

八项全绿才算完成；`check_pdf_layout` 报错时先修排版再提交。

## 步骤 8：提交并关闭 Issue

- 提交信息模板：`dsh 版本更新 vX → vY：正文/版本盒/截图/构建`；
- 附巡检报告（或粘贴关键片段）；
- 关闭巡检 Issue，并在 `PROGRESS.md` 记一行。

## 附：常见情况处理

| 情况 | 处理 |
| ---- | ---- |
| 新版是 alpha/next 渠道 | 一般**不追**，只记录；等 `latest` 变化再更新 |
| 新版破坏兼容（命令改名） | 正文加"迁移提示"，并在第 12 章 01 节补充案例 |
| 巡检脚本查询失败（网络/限流） | 手工执行步骤 1 的三条命令（`npm view` + Releases 页） |
| 只改价格 | 走步骤 4/5/7，无需重截截图 |
