# 章节样板模板（用于第 2–8 章复制与后续增补）

> 第 1 章（`chapters/01-numpy/`）是已更新的样板：正文 + 案例卡 + 自动代码核验。复制到其他章时，按本清单替换主题与内容即可。

## 目录结构（每章）

```
chapters/NN-主题/
├─ README.md              # 章首页：概览、案例索引、目标、目录、练习/上机入口、课时
├─ 01-小节.md … 06-小节.md   # 正文（含目标/先修/案例卡/误区/思考题/练习/延伸阅读）
├─ 05-综合案例.md         # 至少 1 个综合案例（含配图）
├─ 06-常见误区与技巧.md   # 易错点表 + 性能/调试
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
└─ pdf_manifest.txt       # 可由 build/gen_manifest.py 自动生成（保留 TITLE）
```

## 案例卡模板（重要：小标题 = 技术点）

每个案例统一用下列骨架，保证“标题↔内容↔代码”一一对应：

```markdown
## 案例卡 N：<技术点>——<一句话场景>

### 目标

<要解决什么问题、用哪个技术点>

### 代码

```python
<可直接运行；开头带 import + np.set_printoptions(precision=4, suppress=True)>
```

### 运行结果（已运行核验）

```text
<与 python 实际输出逐行一致>
```

### 讲解

<逐段解释：变量含义、为什么这样写、结果说明什么>

### 主要用法 / API

<表格或列表：这个案例覆盖了哪些函数/参数>

### 常见错误

<学生常踩的 2–4 个坑>

### 拓展

<修改/深挖方向 3–4 条>
```

## 复制步骤

1. **迁移原始内容**：确认 `原始资料/chapN` 已在（原样保留）。
2. **建目录**：`chapters/NN-主题/{images, exercises, lab}`。
3. **写正文**：以 `原始资料/chapN` 对应小节为底本，套用 01 章模板结构；不必拘泥原版结构，以“学生能看懂、能运行”为准。
4. **写案例卡**：每节至少 1 个，标题必须写清技术点；代码先跑通再抄输出。
5. **写综合案例与误区页**：每章至少 1 个能串起本章知识的案例；附 matplotlib 图。
6. **整理练习**：把原 quiz 移动/改写为 `exercises/` 唯一入口；若原 quiz 缺失，参照 `build/make_chap1_lab.py` 的 JSON 结构编写。
7. **写 lab**：参照 `build/make_chap1_lab.py` 生成 `lab.ipynb`。
8. **写 references / teaching / README**：注意官方链接与版本信息；README 更新“案例索引”表。
9. **PDF**：运行 `python build/gen_manifest.py` 自动刷新 `pdf_manifest.txt`，再 `python build/pdf_build.py NN-主题`。
10. **验收**：`python build/validate_code.py --strict NN-主题` + `python build/validate_book.py`；运行 lab 各 cell；检查配图与链接。

## 日常增补/修改工作流（一键式）

```bash
# 1) 只改 md / 图片 / 案例后：
python build/gen_manifest.py            # 自动同步 pdf_manifest.txt（新增文件自动进书）
python build/validate_code.py --quiet --strict NN-主题   # 自动跑代码 + 核对输出
python build/update_all.py --tex --tex-compile            # 校验→每章PDF→全书PDF→TeX工程
# 2) 验证 + 同步到本地课程目录：
python build/sync_dist.py
# 3) 推送后 GitHub Actions 自动重出 PDF 并部署网页
```

规则：

- 新增小节：新建 `NN-小节.md`（两位数字开头），运行 `gen_manifest.py` 即可自动进全书/单章/TeX，无需手工改清单。
- 修改代码：先改 ```python``` 块，再运行 `validate_code.py --strict`；若输出变了，同步更新后面的 ```text``` 块。
- 修改标题：**案例标题必须包含具体技术点**（如“SVD 低秩近似”“argsort 排名”），避免“案例 1：某某应用”这种与代码脱节的标题。

## 通用要求

- 所有代码**实际运行验证**后再写入文档；
- 结论以官方文档为准；引用外部资源给出链接与优先级；
- 正文中文为主，代码/术语中英混用；
- 配图统一放 `images/`，命名见 `build/make_chap1_figures.py` 示例；
- 不修改 `原始资料/` 中任何内容；
- 生成物（教材PDF/教材TeX）不手改；手改需保留 custom `user_style.tex`/`user_meta.yaml`。

## 命名约定

| 章 | 目录 | 建议 TITLE |
| ---- | ---- | ---- |
| 1 | 01-numpy | Numpy及其基本使用（已完成案例卡升级） |
| 2 | 02-sympy | Sympy及其基本使用 |
| 3 | 03-scipy | Scipy及其基本使用 |
| 4 | 04-pandas | Pandas及其基本使用 |
| 5 | 05-matplotlib | Matplotlib及其基本使用 |
| 6 | 06-networkx | Networkx及其基本使用 |
| 7 | 07-statsmodels | Statsmodels及其基本使用 |
| 8 | 08-sklearn | Sklearn及其基本使用 |
