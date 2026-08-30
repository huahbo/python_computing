# 05 LaTeX 基础与编译

> 本节目标：学会“把文字、公式、表格、图片排成一张漂亮的 PDF”。先了解在线平台（Overleaf、LoongTeX）作为备选，再掌握本地 VS Code + TeX Live 的主流流程，最后用课程模板写出你的第一份报告。

## 本节目标

- 知道 LaTeX 是什么、课程报告为什么推荐用它；
- 会用 **Overleaf / LoongTeX** 在线编译（网络/机房场景备选）；
- 会安装/检查 TeX Live，并配置 VS Code LaTeX Workshop 一键编译；
- 会写一个中文文档：标题、章节、数学公式、表格、插图；
- 会用 `教学资源/LaTeX模板/` 里的两个模板写作业/实验报告。

---

## 5.1 为什么课程用 LaTeX

| 优点 | 说明 |
| ---- | ---- |
| 排版专业 | 公式、表格、引用自动排版，论文/报告通用 |
| 稳定 | 同一个源码在任何电脑编译结果基本一致 |
| 可版本管理 | `.tex` 是纯文本，可与 Git 配合 |
| 数学友好 | 科学计算报告充满公式，LaTeX 几乎是标准 |

代价：有一点点学习成本。**本章只教 4 件套**：文档骨架、公式、表格、插图 + 一键编译；其余按需查文档。

## 5.2 在线平台（备选，推荐至少注册一个）

### Overleaf

- 网址：`[链接](https://www.overleaf.com/`)
- 优点：浏览器直接写、多人协作、内置大量模板（含中文模板）、无需安装；
- 缺点：中文支持需选 `XeLaTeX` 编译器并引入 `ctex`；免费版有编译时长/协作人数限制；国际网络/访问速度一般。

### LoongTeX（龙文）

- 网址：`[链接](https://www.loongtex.com/`)
- 优点：国产、访问快、中文环境开箱即用（内置 ctex 模板）、文档/教程中文友好；
- 缺点：规模比 Overleaf 小、功能与长期稳定性需以官网为准。

### 在线 vs 本地

| 场景 | 建议 |
| ---- | ---- |
| 机房/公共机没装 TeX Live | 用在线平台应急 |
| 在家、有网、机器带宽好 | 本地 TeX Live + VS Code（本节主流程） |
| 小组协作写一份报告 | Overleaf 协作更省事 |
| 课程期末报告（要控排版） | 本地模板更可控 |

> 注意：**在线平台也要选 XeLaTeX 编译器**，否则中文会报错或乱码。

## 5.3 本地安装 TeX Live（Windows）

### 完整安装（推荐，一次到位）

1. 打开 `[链接](https://www.tug.org/texlive/acquire-netinstall.html`，下载) `install-tl-windows.exe`（约 20 MB）；
2. 运行安装程序：选择 **完整安装**（约 7–8 GB，包含 ctex、latexmk、xelatex 等）；网速慢可先在国内 CTAN 镜像下载 ISO 再安装；
3. 安装完成后验证：

```powershell
xelatex --version
latexmk --version
```

### 精简安装（硬盘小 / 网速受限）

- 安装时选择 `scheme-small` 或 `scheme-basic`，缺哪个宏包再 `tlmgr install 宏包名`；
- **至少需要**：`ctex`、`xecjk`、`amsmath`、`graphicx`、`hyperref`、`latexmk`、`xetex`。

### macOS / Linux

- macOS：`brew install --cask mactex`（或下载 MacTeX 安装包）；
- Linux（含 CI）：`sudo apt install texlive-xetex texlive-lang-chinese texlive-latex-extra latexmk fonts-noto-cjk`；
- 若安装不动，直接用 5.2 的在线平台上课。

## 5.4 配置 VS Code + LaTeX Workshop

1. 安装扩展 **LaTeX Workshop**（`james-yu.latex-workshop`）；
2. 打开设置 JSON（`Ctrl+Shift+P` → `Open Settings (JSON)`），确认/添加：

```json
{
  "latex-workshop.latex.recipes": [
    { "name": "xelatex", "tools": ["latexmk-xelatex"] }
  ],
  "latex-workshop.latex.tools": [
    {
      "name": "latexmk-xelatex",
      "command": "latexmk",
      "args": ["-xelatex", "-synctex=1", "-interaction=nonstopmode", "%DOC%"]
    }
  ],
  "latex-workshop.latex.autoBuild.run": "onSave",
  "latex-workshop.view.pdf.viewer": "tab"
}
```

3. 在 `.tex` 文件首行写魔法注释：`% !TeX program = xelatex`；
4. 保存后应自动编译并在 VS Code 内预览 PDF；`Ctrl+Alt+B` 手动构建，`Ctrl+Alt+V` 看 PDF。

> 也可以直接用课程模板自带的 `.vscode/settings.json`（模板目录 latex_vscode_template/），拷贝进你的项目即可。

## 5.5 第一份中文文档（最小可编译示例）

```latex
% !TeX program = xelatex
\documentclass{ctexart}
\usepackage{amsmath}
\usepackage{graphicx}
\usepackage{hyperref}

\title{课程实验报告}
\author{张三\ 20230001}
\date{2026 年秋季}

\begin{document}
\maketitle

\section{实验目的}
学会用 XeLaTeX 编译中文文档。

\section{结果}
平均分公式：
\begin{equation}
  \bar{x} = \frac{1}{n}\sum_{i=1}^{n} x_i
\end{equation}

表格示例：
\begin{table}[h]
  \centering
  \begin{tabular}{|l|c|r|}
    \hline
    姓名 & Python & 数学 \\
    \hline
    张三 & 88 & 92 \\
    李四 & 76 & 81 \\
    \hline
  \end{tabular}
  \caption{成绩表}
\end{table}

图片示例：
\begin{figure}[h]
  \centering
  \includegraphics[width=0.6\textwidth]{example.png}
  \caption{结果示意图}
\end{figure}

\end{document}
```

> 说明：`ctexart` 让文档支持中文；`xelatex` 负责字体；`\begin{equation}...\end{equation}` 是编号公式；`tabular` 是表格；`includegraphics` 插图。

## 5.6 编译方法与常见错误

### 编译命令

```powershell
cd 报告目录
latexmk -xelatex main.tex       # 推荐：自动多遍
# 或手动四连：xelatex main.tex && bibtex main && xelatex main.tex && xelatex main.tex
```

### 常见错误表

| 报错/警告 | 原因与解决 |
| ---- | ---- |
| `! Package ctex Error` | 没开 XeLaTeX（用了 pdflatex）→ 改用 `latexmk -xelatex` |
| `Missing character: There is no ...` | 字体缺字/空格命令错误；中文必须 xelatex + ctex |
| `! LaTeX Error: File `xxx.sty' not found` | 宏包未安装 → `tlmgr install xxx` |
| `! Undefined control sequence` | 命令拼写错，或忘了引宏包（如 `amsmath`） |
| `! Undefined references` | 需要多编译几遍；用 `latexmk` 自动处理 |
| 图片显示不出 | 图片路径相对 `.tex` 所在目录；用 `\includegraphics` 且文件存在 |
| 编译卡住/内存 | 关闭 `-synctex`；删掉 `.aux` 后再编译 |

## 5.7 使用课程模板

- **最简模板** `latex_simple/`：一个 `example.tex`，看标题/公式/列表/表格/结论；
- **完整模板** `latex_vscode_template/`：含 `references.bib` 参考文献与 `figures/` 示例图，适合课程讲义/实验报告/期末大作业。

用法（以作业报告为例）：

```text
1. 把 latex_vscode_template 复制为你的报告目录（如 report/week0/）
2. 改 main.tex 标题、作者、日期
3. 写 section{实验目的} section{方法} section{结果} section{结论}
4. 插入公式/表格/图片（见 5.5）
5. 保存 → 自动编译 → 导出 main.pdf 提交
```

> 注意：**不要手改模板里的宏包配置**，先照抄；想加宏包再按文档加 `\usepackage`。

## 5.8 在线平台的快速入门（备选）

- Overleaf：New Project → 选 `ctexart` 或任何中文模板 → 把编译器切到 `XeLaTeX`（Menu → Compiler）→ 编辑左侧源码、右侧实时 PDF；
- LoongTeX：注册 → 新建项目（默认中文模板）→ 粘贴 5.5 示例 → 编译即可；文档帮助见官网教程。

## 本节小结与思考题

1. 为什么中文必须 XeLaTeX？（提示：字体与编码）
2. 用课程模板写一个 5 行的小报告：标题、一段话、一个公式、一个表格，编译成 PDF。
3. 如果机房电脑装不了 TeX Live，你准备用哪条备选路径？
