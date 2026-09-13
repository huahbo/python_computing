# 教材PDF（构建产物，已入库）

本目录存放由 `build/pdf_build.py` 从新版 md 生成的各章合订 PDF（pandoc + xelatex，pypdf 合并并校验页数）。

> 这些 PDF 虽由脚本/CI 重新生成，但已**提交进本仓库**（不再被 `.gitignore` 忽略），便于离线阅读与直接下载。

| 文件 | 章节 | 页数 |
| ---- | ---- | ---- |
| `00-prep-前置基础：环境、编程与 LaTeX.pdf` | 0 前置基础 | 24 页 |
| `01-numpy-Numpy及其基本使用.pdf` | 1 NumPy | 24 页 |
| `02-sympy-Sympy及其基本使用.pdf` | 2 SymPy | 20 页 |
| `03-scipy-Scipy及其基本使用.pdf` | 3 SciPy | 29 页 |
| `04-pandas-Pandas及其基本使用.pdf` | 4 Pandas | 23 页 |
| `05-matplotlib-Matplotlib及其基本使用.pdf` | 5 Matplotlib | 22 页 |
| `06-networkx-Networkx及其基本使用.pdf` | 6 NetworkX | 24 页 |
| `07-statsmodels-Statsmodels及其基本使用.pdf` | 7 Statsmodels | 22 页 |
| `08-sklearn-Sklearn及其基本使用.pdf` | 8 scikit-learn | 22 页 |

## 重新构建

```bash
python build/pdf_build.py            # 全部（有 pdf_manifest.txt 的章）
python build/pdf_build.py 01-numpy   # 单章
python build/pdf_build.py --list     # 查看清单
```

## 说明

- 源文件：`chapters/章节/pdf_manifest.txt`（TITLE 行 + 按序 md）；
- 图片：`chapters/章节/images/*.png` 会被 pandoc 内嵌。
