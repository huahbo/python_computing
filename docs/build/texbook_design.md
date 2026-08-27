# 《Python 科学计算》全书 LaTeX 构建流程设计（可维护版）

> 目标：**内容经常更新时，全书 LaTeX 版能一键、可靠地跟随更新**。本设计把“内容源”与“排版产物”彻底分离，LaTeX 书是**生成物**，不允许手工改 .tex。

---

## 1. 设计原则（针对“经常更新”的答案）

1. **单一事实源（Single Source of Truth）**：`chapters/NN-xxx/*.md` 是唯一内容源；`images/` 是唯一图源。LaTeX 书、每章 PDF 都从它生成。
2. **生成物 vs 源码**：`教材PDF/` 下的所有 PDF 都是构建产物；任何修改只发生在 md / 图 / 配置 / 模板，然后重跑构建。
3. **可复现**：同一份源码 + 同一份 `book.yaml` + 固定字体/工具链 → 同一份书。结果可哈希校验。
4. **增量**：只重建“变了的内容”，支持 `--chapter` 单章预览、`--check` 只报告过期章节。
5. **可验收**：每次构建后自动校验（页数、目录、缺字/LaTeX 错误、内部链接），保证流程不崩。

---

## 2. 数据流

```
chapters/NN-xxx/*.md  ─┐
chapters/NN-xxx/images/*.png ─┐
book.yaml（章节顺序/标题/作者） ─┤
build/latex/（模板+样式，唯一手工维护的“版式”） ─┤
build/texbook.py ──────────────┘
        │
        ├── 标题层级归一：README #=章；节文件 #→##
        ├── pandoc → 每章 .tex → xelatex 单章/合并
        ├── 增量缓存 .texbook_cache.json（md/图/模板 hash）
        └── 校验 + 报告 build/_build_report.json
                │
                ▼
  教材PDF/Python科学计算_全书.pdf  ← 每次更新自动重生成
  教材PDF/NN-主题.pdf（每章 PDF 同源同生）
```

## 3. 更新流程（日常只需 2 步）

1. **改内容**：编辑 `chapters/NN-xxx/…md`，或替换 `images/*.png`，或改 `book.yaml`（章节增减/顺序）。
2. **出书**：

```bash
python build/texbook.py                 # 全书（自动仅重建变化的章节）
python build/texbook.py --chapter 03-scipy   # 只预览某章
python build/texbook.py --check              # 只列出“需要重建”的章节
python build/texbook.py --full              # 强制全量重建
```

> 推荐再加一个总入口：`python build/update_all.py`（校验链接 → 重生成配图(可选) → 每章 PDF → 全书 PDF → 出报告），一条命令完成“上课物料全家桶”。

## 4. 关键机制

| 机制 | 说明 | 解决什么问题 |
| ---- | ---- | ---- |
| `book.yaml` | 章节顺序、标题、作者、是否含 exercises/lab 附录；章节内文件清单**复用 `pdf_manifest.txt`** | 章节经常增删/换序时只改一处元数据 |
| 标题层级归一 | README 的 `#`=章；各节文件 `#`→`##`（pandoc `--shift-heading-level-by=1` 只作用于节文件） | 全书目录层级正确 |
| 资源路径 | 每章传送 `--resource-path=<章目录>` | 图片跟随章节 md |
| 中文/公式 | xelatex + Microsoft YaHei + `$…$`/`$$…$$`（已验证：8 章每章 PDF 均已成功） | 中文、数学公式 |
| 增量缓存 | `.texbook_cache.json` 记录每个 md/图/模板的 hash | 高频更新时秒级重建 |
| 版本戳 | PDF metadata 写 `Title/Author/生成时间/源码 hash`；报告写 `_build_report.json` | 知道“这份 PDF 对应哪个版本内容” |
| 自动校验 | 编译后：页数>0、无 `Missing $ inserted`、无 `Missing character`（解析 pandoc 日志）、目录页存在；并复用 `build/validate_book.py` | 更新出错立刻暴露 |
| md 语法 lint | `build/lint_md_for_tex.py`：检测 `<details>`、裸 `\(\)`、emoji、docsify 专属语法并自动修复/报错 | 防止“新写内容在网页正常、LaTeX 翻车” |

## 5. 修订后的阶段（每期给你验收）

| 阶段 | 内容 | 验收点 |
| ---- | ---- | ---- |
| **A 模板包** | 整理 `latex_simple`/`latex_vscode_template` → `教学资源/LaTeX模板/` + README + 可编译 sample | 你本地一条命令编译出 sample |
| **B1 单章 pilot** | `texbook.py` + `book.yaml` + 标题归一 + 编译第 1 章为“书内一章”（含封面/目录骨架） | 单章 PDF 通过、目录层级正确 |
| **B2 全 8 章** | 全书合成 + 封面/目录 + 增量缓存 + 自动校验 + `--check` | 全书 PDF、增删一章只重建受影响部分 |
| **C 打磨 + 自动化** | 版式（页眉页脚/代码高亮/公式/参考文献 bib/附录：习题答案与 quiz 汇总）+ `update_all.py` + **GitHub Actions 工作流**（push 到 `chapters/` 或手动触发自动重建） | 视觉审查 + 改一个 md → push → CI 自动出新书 |

## 6. 风险与对策

| 风险 | 对策 |
| ---- | ---- |
| 新内容用 docsify 专属语法导致 LaTeX 崩 | `lint_md_for_tex.py` 前置检查；B1 阶段先审计全部 md（已初步审计：无 `<details>`；`~~~` 围栏 pandoc 可解析） |
| 有人手改 LaTeX 造成与 md 漂移 | 所有生成文件头部写“由 texbook.py 生成，勿手改”；`--full` 会覆盖 |
| 章节增删导致目录/编号乱 | 只用 `book.yaml` 排序；构建时自动编号，md 中不写死章节编号 |
| 更新频繁、构建慢 | 增量缓存 + 单章预览 + CI 缓存 `.texbook_cache.json` |
| 某章编译失败拖垮全书 | 单章先编译；失败则全书构建中止并明确报哪一章、哪个 md |

## 7. 一个“日常更新”示例

> 修改 `chapters/03-scipy/01-微积分工具包.md` → 运行 `python build/texbook.py`：
> 1) 检测 03-scipy 相关 md hash 变化；2) 仅重编译第 3 章；3) 重新合并全书；4) 校验页数/缺字/目录；5) 更新 `教材PDF/Python科学计算_全书.pdf` 并在报告里记录“03-scipy v2, 时间戳”。
> 若启用 CI：push 后自动执行同样流程，不用任何人手动跑。

## 8. 结论

**可以满足“经常更新”**，前提就是：**内容永远改 md，书永远由 `texbook.py` 生成**；更新=改 md+一条命令（或一次 push）；构建带增量、校验、版本戳，任何环节出错都有明确报错。
---

## 实测记录（build/texbook.py 已实现，2026 更新）

- 配置：`docs/build/book.yaml`（标题/作者/章节顺序）；章节内容与标题复用 `pdf_manifest.txt`（TITLE + 文件清单），**章首页 README 不进入书正文**。
- 标题归一：`chapter_md()` 对节文件所有 `#{1,6}` 标题 +1（章=1 级、节=2 级、小节=3 级）。
- 图片路径：`](./images/…`、`](../images/…`、`](images/…` 三种写法的前缀全部改写为 `./chapters/<dir>/images/` + `--resource-path=<docs根>`。
- pandoc 参数：`--toc --toc-depth=2 -V toc-title=目录 --highlight-style=tango --include-in-header=build/texbook_header.tex`（fancyhdr 页眉左标题/右页码）。
- 命令：
  - `python build/texbook.py` 全书；`--chapter 01-numpy` 单章；`--check` 增量；`--full` 全量；
  - `python build/update_all.py` = validate + 每章 PDF + 全书（exit codes 全 0 已验证）。
- 产物：`教材PDF/Python科学计算_全书.pdf`（162 页，8 章）；`教材PDF/_pilot/01-numpy-pilot.pdf`（21 页）。
- 告警检测：Missing character / Missing $ / Could not fetch resource / replacing image / Error producing PDF。
- CI：`.github/workflows/texbook.yml`（push 到 docs/chapters/build 或手动触发；Ubuntu + pandoc + texlive-xetex + texlive-lang-chinese + fonts-noto-cjk；**尚未在 GitHub 云端试跑**，如字体/包差异可调）.
