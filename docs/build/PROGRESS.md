# 课程重构进度（维护用）

> 由 `build/` 相关脚本与子任务协作维护；每完成一章就更新一行。

## 总目标

新版教学内容与原始内容完全分离：`chapters/` 存放新版（章首页+各节正文+综合案例+误区技巧+references+teaching+exercises+lab+配图），`原始资料/` 只读归档，PDF 构建产物放 `教材PDF/`。

## 进度

| 章 | 目录 | 状态 | 备注 |
| ---- | ---- | ---- | ---- |
| 0 前置基础 | `chapters/00-prep/` | ✅ 完成 | 3 图、15题quiz、lab 10/10、24 页 PDF；配套 `教学资源/环境配置/` |
| 1 NumPy | `chapters/01-numpy/` | ✅ 完成 | 6 图、20题+quiz、lab 13/13、24 页 PDF |
| 2 SymPy | `chapters/02-sympy/` | ✅ 完成 | 3 图、10题+11题quiz、lab 18/18、20 页 PDF |
| 3 SciPy | `chapters/03-scipy/` | ✅ 完成 | 9 图、16题quiz、lab 13/13、29 页 PDF |
| 4 Pandas | `chapters/04-pandas/` | ✅ 完成 | 3 图、15题+25题quiz、lab 13/13、23 页 PDF |
| 5 Matplotlib | `chapters/05-matplotlib/` | ✅ 完成 | 4 图、14题quiz、lab 13/13、22 页 PDF |
| 6 NetworkX | `chapters/06-networkx/` | ✅ 完成 | 3 图、10题quiz+12题作业、lab 10/10、24 页 PDF |
| 7 Statsmodels | `chapters/07-statsmodels/` | ✅ 完成 | 7 图、10题quiz+10题作业、lab 10/10、22 页 PDF |
| 8 scikit-learn | `chapters/08-sklearn/` | ✅ 完成 | 6 图、10题quiz+12题作业、lab 8/8、22 页 PDF |

## 全校验（2026 汇总）

- `python build/validate_book.py`：chapters=9、notebooks ok=29、labs=9、missing internal links=0、problems=0 ✅
- 第 0 章：quiz 15 题自动评分答案 15/15；lab0 运行 10/10；全书 PDF 181 页；教材TeX main.pdf 编译通过。
- 各章 lab 均逐章执行通过；各章合订 PDF 均已生成于 `教材PDF/`。
