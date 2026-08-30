# 第 0 章 参考资料（环境 · Python · LaTeX）

> 本页是第 0 章的**精选参考**：官方文档为第一优先级；教程与在线平台用于加深/兜底。链接在编写时已联网核实，仍建议以官方最新版为准。

## 一、Python 环境与 VS Code（必读）

| 资料 | 链接 | 说明 | 优先级 |
| ---- | ---- | ---- | ---- |
| Python 官方教程（中文） | [链接](https://docs.python.org/zh-cn/3/tutorial/) | 语法查漏的第一权威 | ★必读 |
| 安装 Miniconda | [链接](https://docs.conda.io/en/latest/miniconda.html) | 官方下载入口（速度慢用清华镜像） | ★必读 |
| 清华 Miniconda 镜像 | [链接](https://mirrors.tuna.tsinghua.edu.cn/anaconda/miniconda/) | 国内下载加速 | 推荐 |
| 清华 Anaconda/PyPI 镜像 | [链接](https://mirrors.tuna.tsinghua.edu.cn/) | conda/pip 都从这里加速 | 推荐 |
| VS Code 官方下载 | [链接](https://code.visualstudio.com/) | 编辑器 | ★必读 |
| VS Code Python 环境官方文档 | [链接](https://code.visualstudio.com/docs/python/environments) | 解释器/虚拟环境/内核原理 | ★必读 |
| VS Code Python 入门 | [链接](https://code.visualstudio.com/docs/python/python-tutorial) | 从新建文件到运行调试 | 推荐 |
| Jupyter 官方文档 | [链接](https://docs.jupyter.org/en/latest/) | 笔记本/内核/导出 | 选读 |
| Anaconda vs Miniconda | [链接](https://www.anaconda.com/docs/getting-started/concepts/anaconda-or-miniconda) | 选型说明（课程推荐 Miniconda） | 选读 |

## 二、Python 编程强化（查漏）

| 资料 | 链接 | 说明 | 优先级 |
| ---- | ---- | ---- | ---- |
| 聪明办法学 Python v2（Datawhale） | [链接](https://github.com/datawhalechina/learn-python-the-smart-way-v2) | 前置课程：Chap0 安装、Chap1 启航、Chap2-6 基础语法 | ★推荐 |
| Python Cheat Sheet | [链接](https://www.pythoncheatsheet.org/) | 速查表 | 推荐 |
| Python 教程 · 廖雪峰（中文） | [链接](https://liaoxuefeng.com/books/python/introduction/) | 中文查漏 | 选读 |
| Learn X in Y minutes: Python | [链接](https://learnxinyminutes.com/docs/zh-cn/python3-cn/) | 半小时过一遍语法 | 选读 |

## 三、LaTeX（正文 + 在线平台）

| 资料 | 链接 | 说明 | 优先级 |
| ---- | ---- | ---- | ---- |
| Learn LaTeX 中文站 | [链接](https://www.learnlatex.org/zh-hans/) | 免费结构化课程：结构/公式/表格/插图 | ★推荐 |
| ctex 宏包文档 | [链接](https://ctan.org/pkg/ctex) | 中文排版权威 | ★必读 |
| TeX Live 下载 | [链接](https://www.tug.org/texlive/acquire-netinstall.html) | Windows 安装器 | ★必读 |
| Overleaf | [链接](https://www.overleaf.com/) | 在线编译（备选） | 推荐 |
| LoongTeX（龙文） | [链接](https://www.loongtex.com/) | 国产在线编译（备选，中文友好） | 推荐 |
| 课程 LaTeX 模板 | [./教学资源/LaTeX模板/README.md](../../教学资源/LaTeX模板/README.md) | 两种模板 + 使用说明 | ★必做 |
| Windows 装 TeX Live 图文 | [./教学资源/texlive_vscode_setup.md](../../教学资源/texlive_vscode_setup.md) | 本仓库已有详细流程 | ★推荐 |

## 四、工程与 Git（选学）

| 资料 | 链接 | 说明 |
| ---- | ---- | ---- |
| Git 官方文档 | [链接](https://git-scm.com/doc) | 书/命令/教程 |
| 廖雪峰 Git 教程（中文） | [链接](https://liaoxuefeng.com/books/git/introduction/) | 中文入门 |
| Pro Git 中文版 | [链接](https://git-scm.com/book/zh/v2) | 系统化学习 |

## 五、本仓库入口

| 资料 | 链接 |
| ---- | ---- |
| 本章练习 | [./exercises/README.md](./exercises/README.md) |
| 本章上机 | [./lab/README.md](./lab/README.md) |
| 教学说明 | [./teaching.md](./teaching.md) |

## 资源使用建议

1. **教学**：以 VS Code 官方文档 + Learn LaTeX 为主线；不要一次讲太多宏包。
2. **上机**：先跑 `check_env.py`，再按 lab 步骤完成；LaTeX 部分现场演示“保存 → 自动编译 → 预览”。
3. **备选**：机房/未装 TeX Live 的学生直接引导到 Overleaf / LoongTeX（务必切 XeLaTeX）。
4. **查错**：环境类问题先读 00-02 常见问题表；LaTeX 报错先看 00-05 常见错误表。

> 本清单整理时间：2026 年（随课程迭代可更新）。
