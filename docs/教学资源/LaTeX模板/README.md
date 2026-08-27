# LaTeX 模板（教学配套）

> 用途：作业报告 / 课程讲义 / 论文排版的起点。**中文必须用 XeLaTeX（+ctex）编译**。

## 目录

| 模板 | 说明 |
| ---- | ---- |
| `latex_simple/` | 最简示例（`example.tex`，ctexart，一篇文章骨架：标题/公式/列表/表格/结论） |
| `latex_vscode_template/` | 较完整模板（`main.tex`，a4 article + ctex + amsmath + graphicx + hyperref + cite；含 `references.bib` 参考文献与 `figures/` 图片示例） |

## 环境要求

- TeX Live（或 MiKTeX）+ **XeLaTeX** + `ctex` 宏包；
- 推荐 VS Code + LaTeX Workshop（项目自带 `.vscode/settings.json` 使用 latexmk -xelatex）。

## 编译命令

```bash
# 简单模板
cd latex_simple
xelatex example.tex

# 完整模板（含参考文献，交给 latexmk 自动多遍）
cd latex_vscode_template
latexmk -xelatex main.tex
# 或手动：xelatex main.tex && bibtex main && xelatex main.tex && xelatex main.tex
```

## 三种用法

1. **作业/实验报告**：复制 `latex_simple`，改标题作者，把结论换成你的报告小节，插入实验图。
2. **课程讲义**：复制 `latex_vscode_template`，用 `\section`/\subsection\ 组织；图片可从 `../../chapters/章节/images/` 复制或 `\includegraphics` 引用。
3. **论文/综述**：在完整模板上补充 `references.bib` 条目，用 `\cite{...}` 引用。

## 注意事项

- 中文正文用 `xelatex`；不要用 `pdflatex` 编译含中文文件；
- 原来 `figures/example.png` 为 0 字节导致编译失败，本目录已替换为可显示示例图（原始根目录模板请自行修复）；
- 编译产物（`*.pdf`）建议加入 .gitignore，模板只保留 `.tex`/`.bib`/图源。
