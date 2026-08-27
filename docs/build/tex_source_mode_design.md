# 双模式设计：md→PDF 与 md→TeX 工程（分离不耦合）

> 目标：**内容源永远只有 `docs/chapters/**/*.md`**；两种产出（PDF、可编辑 LaTeX 工程）彼此独立；
> 你优先用 md→PDF；同时提供“快速/自动刷新 TeX 工程”的能力。

---

## 1. 双模式总览

```
                       ┌──────────────────────────────┐
                       │  唯一内容源 chapters/**/*.md   │
                       │  （+ images/ + pdf_manifest）  │
                       └──────────────┬───────────────┘
                                      │
              ┌───────────────────────┴───────────────────────┐
              ▼                                               ▼
  模式 A（优先）                                  模式 B（可选）
  build/pdf_build.py + texbook.py               build/emit_tex.py
  → 教材PDF/（每章 PDF + 全书 PDF）              → 教材TeX/（可编译 .tex 工程）
  pandoc → latex → xelatex（临时 tex 不落盘）      pandoc → 每章 .tex 落盘 + main.tex
  产物为“二进制交付物”，不手改                   产物为“可读可编译源码工程”，可审阅/微调
```

**分离原则**：
1. 两模式各自有独立脚本、独立缓存、独立输出目录；互不读写对方产物。
2. 都从同一 md 读取，因此内容永远一致；改 md 后两个模式各自重跑即可。
3. 删掉任何一个目录，不影响另一个；重新生成即可恢复。

---

## 2. 模式 B 输出结构（`docs/教材TeX/`）

```
教材TeX/
├─ main.tex                 # 生成物：文档class(ctexbook)、toc、include 各章、样式引用
├─ book_meta.yaml           # 生成物：标题/作者/日期/章节顺序（由 build/book.yaml 派生）
├─ user_style.tex           # ★ USER 可编辑：宏包/页眉/封面/自定义命令；生成时不覆盖
├─ user_meta.yaml           # ★ USER 可编辑：覆盖标题/作者/日期等（优先级最高）
├─ chapters/
│   ├─ ch01-numpy.tex       # 生成物：每章一个 chapter{...}（含该章 01–0N 节）
│   ├─ ch02-sympy.tex
│   └─ ...                  # 可与 main.tex 一起用 latexmk/yatex 编译
├─ figures/                 # 生成物：从 chapters/NN/images/ 复制（自包含，推荐）
│   └─ 01-numpy/… / 08-sklearn/…
├─ references.bib           # 生成物（当前 md 无引用，预留；可从未来 references 生成）
└─ README.md                # 生成物：说明“哪些可手改、如何再生成/编译”
```

**手改策略（关键）**：正文章节 `chapters/*.tex` 均为**生成物**（头部有“由 emit_tex.py 生成，勿手改”警告）；
所有“自定义版式”统一放到 `user_style.tex` 与 `user_meta.yaml`（不会被覆盖）。这样既能自动刷新，
又不会丢失你的手工定制；若你想改某章文字，请改 md（保持单一事实源）。

---

## 3. 自动/快速刷新 TeX 工程

```bash
python build/emit_tex.py                    # 全量重新生成 教材TeX/（含复制 figures）
python build/emit_tex.py --check            # 只报告“md 变化 → 需要重新生成的章节”
python build/emit_tex.py --chapter 01-numpy # 只生成某一章
python build/emit_tex.py --compile          # 生成后顺手用 latexmk -xelatex 编译 main.tex
python build/emit_tex.py --watch            # 监听 chapters/**/*.md 变化，自动重生成对应章节（可选）
```

**增量机制**：`build/.tex_emit_cache.json` 记录每个 md 的 sha256；只有变化的章节 .tex 被重写，
未变化章节保留原文件（便于对比/审阅）。若某章 .tex 被手改（检测到 hash 与上次生成不一致且 md 未变化），
生成器会**跳过并提示**（把改动备份到 `教材TeX/_manual_backup/`），避免自动更新覆盖你的手写内容。

**与模式 A 的关系**：`update_all.py` 增加可选开关（默认只跑模式 A）：
`python build/update_all.py --tex`  = 模式 A 全家桶 + 模式 B 刷新（两者独立串行执行，互不依赖）。

---

## 4. 建议的 git 策略

- `docs/教材TeX/`：**纳入版本管理**（它是源码工程，值得审阅/对比/回滚）；`_manual_backup/`、`*.aux/*.log/*.fdb_latexmk` 忽略。
- `docs/教材PDF/`：默认**不进 git**（生成物大）；如需发布，由 CI/手动输出 artifact。
- 两个输出目录都不作为“内容源”，不会参与 md 的增量判断。

---

## 5. 待确认项（讨论后实施）

1. **手改策略**：是否接受“章节 .tex 为生成物、手改只放 `user_style.tex`/`user_meta.yaml`”？
   （若你希望“章节 .tex 可手改且自动更新保留手改”，我会改为“md 未变时保留手改、md 变了则提示冲突并备份”，
   复杂度会高一些——二选一。）
2. **目录/命名**：`教材TeX/` + 工程内 `main.pdf`（推荐）；是否还要在 `教材PDF/` 放一个“TeX 版全书”副本？我建议**不放**，保持分离。
3. **图片**：复制进 `教材TeX/figures/`（自包含，推荐）还是引用原路径（省空间但不自包含）？
4. **编译产物**：`--compile` 默认开还是手动开？我建议默认手动（`--compile` 显式传），因为自动编译会让“刷新”变慢。
5. **`--watch`**：是否需要后台监听自动重生成？（可先不加，用 `--check` + 一条命令即可；若你要“保存即更新”，再加。）
6. **CI**：是否让 GitHub Actions 同时生成 TeX 工程 artifact（只产 .tex 不编译也行）？

---

## 已实现（Mode B，实测通过）

- `build/emit_tex.py`：md → `docs/教材TeX/` 可编译工程（main.tex + chapters/chNN.tex + figures/ + user_style.tex/user_meta.yaml 定制入口）。
- 关键技术：先 pandoc standalone 生成整书 .tex（保证 longtable/Shaded/Highlighting 宏齐全），再按 `\chapter` 边界拆分、main.tex 用 `\input` 引用；`--top-level-division=chapter` + ctexbook。
- 实测：`python build/emit_tex.py --compile` → `教材TeX/main.pdf`（230 页）编译通过；`update_all.py --tex --tex-compile` 全链路 exit 0。
- 分离保证：教材PDF（模式A）与教材TeX（模式B）目录/缓存独立；共用只读源码逻辑。
