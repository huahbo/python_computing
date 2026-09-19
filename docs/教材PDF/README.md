# 教材PDF（构建产物，已入库）

本目录存放由 `build/pdf_build.py` 从新版 md 生成的各章合订 PDF（pandoc + xelatex，pypdf 合并并校验页数）。

> 这些 PDF 虽由脚本/CI 重新生成，但已**提交进本仓库**（不再被 `.gitignore` 忽略），便于离线阅读与直接下载。

## 第一部分：Python 科学计算（第 0–8 章）

| 文件 | 章节 | 页数 |
| ---- | ---- | ---- |
| `00-prep-前置基础：环境、编程与 LaTeX.pdf` | 0 前置基础 | 28 页 |
| `01-numpy-Numpy及其基本使用.pdf` | 1 NumPy | 43 页 |
| `02-sympy-Sympy及其基本使用.pdf` | 2 SymPy | 29 页 |
| `03-scipy-Scipy及其基本使用.pdf` | 3 SciPy | 38 页 |
| `04-pandas-Pandas及其基本使用.pdf` | 4 Pandas | 33 页 |
| `05-matplotlib-Matplotlib及其基本使用.pdf` | 5 Matplotlib | 32 页 |
| `06-networkx-Networkx及其基本使用.pdf` | 6 NetworkX | 37 页 |
| `07-statsmodels-Statsmodels及其基本使用.pdf` | 7 Statsmodels | 37 页 |
| `08-sklearn-Sklearn及其基本使用.pdf` | 8 scikit-learn | 34 页 |

## 第二部分：AI Agent 编程（第 9–12 章）

| 文件 | 章节 | 页数 |
| ---- | ---- | ---- |
| `09-agent-basics-AI Agent 编程基础.pdf` | 9 AI Agent 编程基础 | 25 页 |
| `10-agent-workflow-Agent 工作流与验证方法.pdf` | 10 Agent 工作流与验证方法 | 7 页（编写中） |
| `11-agent-cases-案例实战：从修 bug 到端到端项目.pdf` | 11 案例实战 | 15 页（编写中） |
| `12-agent-engineering-工程化与持续演进.pdf` | 12 工程化与持续演进 | 2 页（编写中） |
| `第二部分-AI-Agent编程.pdf` | 第二部分合并（含部分封面） | 50 页 |

## 全书与附录

| 文件 | 内容 | 页数 |
| ---- | ---- | ---- |
| `Python科学计算_全书.pdf` | 全书（第 0–12 章 + 附录 A–G，含两部分分隔页） | 359 页 |
| `数学与算法补充.pdf` | 附录 A–G | 38 页 |

## 排版约定（自动生效，无需手改正文）

- **图片**：`\floatplacement{figure}{tp}` + 高度上限 `0.70\textheight`，图片只排在页顶或独立页，**不会被页面下沿裁切**；
- **代码块**：`fvextra` 自动折行（`breaklines` + `breakanywhere`），长注释与长命令不再溢出页边；
- **正文**：`xurl` + `hyphenat[htt]` + `\sloppy` + `\emergencystretch=3em`，长 URL 与长等宽串可断行；
- 以上规则统一写在 `build/texbook_header.tex`，对每章 PDF、全书 PDF 与 TeX 工程同时生效；
- 生成后自检：`python build/check_pdf_layout.py`（检测越界图片与超出右边界的文本行），已接入 `update_all.py` 与 CI。

## 重新构建

```bash
python build/pdf_build.py                 # 全部章节（有 pdf_manifest.txt 的章）
python build/pdf_build.py 09-agent-basics # 单章
python build/part_pdf.py                  # 按部分合并（含部分封面）
python build/pdf_build.py --list          # 查看清单
python build/check_indexes.py             # 校验索引一致性（sidebar / book.yaml / manifest / 本表）
```

## 说明

- 源文件：`chapters/章节/pdf_manifest.txt`（TITLE 行 + 按序 md）；
- 图片：`chapters/章节/images/*.png` 会被 pandoc 内嵌；
- 部分划分与部分 PDF 名称：`build/book.yaml` 的 `parts` 段。
