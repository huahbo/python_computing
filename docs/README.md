# Python 科学计算（新版教程）

> 本项目是《Python 科学计算》课程的新版讲义与配套练习。
> **结构变化**：新版内容放在 `chapters/`，原始内容归档在 `原始资料/`（一字未改，只作对照）。

## 课程定位

Python 科学计算方法入门：用 **NumPy / SymPy / SciPy / Pandas / Matplotlib / NetworkX / Statsmodels / scikit-learn** 完成科学计算、数据分析、统计建模与机器学习小项目。可作为《聪明办法学 Python》的下游课程、《数学建模导论》的前置课程。

## 目录（新版）

- [绪论：什么是科学计算](./绪论.md)
- [0 学习指南：环境搭建与学习路径](./0-学习指南.md)
- [0 前置基础：环境、编程与 LaTeX（第 0 章）](./chapters/00-prep/README.md)
- [1 NumPy 及其基本使用](./chapters/01-numpy/README.md)（已完成整套样板：正文/案例/误区/练习/上机/参考/教学说明）
- [2 SymPy 及其基本使用](./chapters/02-sympy/README.md)
- [3 SciPy 及其基本使用](./chapters/03-scipy/README.md)
- [4 Pandas 及其基本使用](./chapters/04-pandas/README.md)
- [5 Matplotlib 及其基本使用](./chapters/05-matplotlib/README.md)
- [6 NetworkX 及其基本使用](./chapters/06-networkx/README.md)
- [7 Statsmodels 及其基本使用](./chapters/07-statsmodels/README.md)
- [8 scikit-learn 及其基本使用](./chapters/08-sklearn/README.md)
- [教学资源](./教学资源/README.md)（期末大作业、测验、模板等）
- [原始资料（旧版，只读）](./原始资料/说明.md)

> 每一章的标准结构：章首页（README）、各节正文、综合案例、常见误区与技巧、references.md、teaching.md、exercises/（作业与自测）、lab/（上机实验）、images/（配图）、pdf_manifest.txt。

## 快速开始

```bash
pip install numpy pandas scipy sympy matplotlib seaborn networkx statsmodels scikit-learn
# 打开 docs 目录下的任何 .ipynb 即可进入上机/练习
```

## 构建

- 配图：`python build/make_chapN_figures.py`
- 上机：`python build/make_chapN_lab.py`
- 合订 PDF：`python build/pdf_build.py`（全章）或 `python build/pdf_build.py 01-numpy`（单章）
- 校验：`python build/validate_book.py`、`python build/run_labs.py`

## 版权

本作品采用 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) 许可。原始项目：[datawhalechina/scientific-computing](https://github.com/datawhalechina/scientific-computing)。
