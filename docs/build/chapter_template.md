# 章节样板模板（用于第 2–8 章复制）

> 第 1 章（`chapters/01-numpy/`）是已验证的样板。复制到其他章时，按本清单替换主题与内容即可。

## 目录结构（每章）

```
chapters/NN-主题/
├─ README.md              # 章首页：概览、目标、目录、练习/上机入口、课时
├─ 01-小节.md … 06-小节.md   # 正文（含目标/先修/官方文档/误区/思考题/练习/延伸阅读）
├─ 05-综合案例.md         # 新增：至少 1 个综合案例（含配图）
├─ 06-常见误区与技巧.md   # 新增：易错点表 + 性能/调试
├─ references.md          # 官方文档 + 教程 + 习题 + 中文补充
├─ teaching.md            # 教师用：课时、重点难点、考核
├─ exercises/
│   ├─ README.md
│   ├─ quiz.ipynb         # 自测（自动评分）
│   ├─ assignment.md      # 作业
│   ├─ answers.ipynb      # 答案
│   └─ (可选) quiz_hidden_answers.ipynb
├─ lab/
│   ├─ README.md
│   └─ lab.ipynb          # 上机：环境自检→逐点演练→综合任务
├─ images/                # 配图（用 build/make_chapN_figures.py 生成）
└─ pdf_manifest.txt       # PDF 合订清单（TITLE: 章名）
```

## 复制步骤

1. **迁移原始内容**：确认 `原始资料/chapN` 已在（原样保留）。
2. **建目录**：`chapters/NN-主题/{images, exercises, lab}`。
3. **写正文**：以 `原始资料/chapN` 对应小节为底本，套用 01 章模板结构。
4. **写综合案例与误区页**：每章至少 1 个能串起本章知识的案例；附 matplotlib 图。
5. **整理练习**：把原 has quiz 移动/改写为 `exercises/` 唯一入口；若原 quiz 缺失，参照 `build/make_chap1_lab.py` 的 JSON 结构编写。
6. **写 lab**：参照 `build/make_chap1_lab.py` 生成 `lab.ipynb`。
7. **写 references / teaching / README**：注意官方链接与版本信息。
8. **PDF**：写 `pdf_manifest.txt`，运行 `python build/pdf_build.py NN-主题`。
9. **验收**：`python build/validate_book.py`；运行 lab 各 cell；检查配图与链接。

## 通用要求

- 所有代码**实际运行验证**后再写入文档；
- 结论以官方文档为准；引用外部资源给出链接与优先级；
- 正文中文为主，代码/术语中英混用；
- 配图统一放 `images/`，命名见 `build/make_chap1_figures.py` 示例；
- 不修改 `原始资料/` 中任何内容。

## 命名约定

| 章 | 目录 | 建议 TITLE |
| ---- | ---- | ---- |
| 1 | 01-numpy | Numpy及其基本使用（已完成） |
| 2 | 02-sympy | Sympy及其基本使用 |
| 3 | 03-scipy | Scipy及其基本使用 |
| 4 | 04-pandas | Pandas及其基本使用 |
| 5 | 05-matplotlib | Matplotlib及其基本使用 |
| 6 | 06-networkx | Networkx及其基本使用 |
| 7 | 07-statsmodels | Statsmodels及其基本使用 |
| 8 | 08-sklearn | Sklearn及其基本使用 |
