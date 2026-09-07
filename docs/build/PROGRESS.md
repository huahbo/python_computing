# 课程重构进度（维护用）

> 由 `build/` 相关脚本与子任务协作维护；每完成一章就更新一行。

## 总目标

新版教学内容与原始内容完全分离：`chapters/` 存放新版（章首页+各节正文+综合案例+误区技巧+references+teaching+exercises+lab+配图），`原始资料/` 只读归档，PDF 构建产物放 `教材PDF/`。

## 进度

| 章 | 目录 | 状态 | 备注 |
| ---- | ---- | ---- | ---- |
| 0 前置基础 | `chapters/00-prep/` | ✅ 完成 | 3 图、15题quiz、lab 10/10、28 页 PDF（含章扉页）；配套 `教学资源/环境配置/` |
| 附录 | `附录/数学算法附录/` | ✅ 完成 | A~F 六主题（公式 LaTeX 化 + 深入难点 + 例题集/综合案例/考前自查）、附录 G 自动总参考（163 条，短链接排版）、附录 PDF 37 页、TeX 编译通过 |
| 1 NumPy | `chapters/01-numpy/` | ✅ 完成（案例卡升级） | 6 图、20题+quiz、lab 13/13、44 页 PDF（含章扉页）、11 个案例卡（标题=技术点，代码与输出已自动核验 0 问题）、validate_code --strict 通过 |
| 2 SymPy | `chapters/02-sympy/` | ✅ 完成（案例卡升级） | 案例卡3个+lab 27cell/19code（新增9cell）、30 页 PDF（含章扉页）、strict 0 |
| 3 SciPy | `chapters/03-scipy/` | ✅ 完成（案例卡升级） | 案例卡3个+lab 31cell/22code（新增9cell）、41 页 PDF（含章扉页）、strict 0 |
| 4 Pandas | `chapters/04-pandas/` | ✅ 完成（案例卡升级） | 案例卡3个+lab 32cell/22code（新增9cell）、35 页 PDF（含章扉页）、strict 0 |
| 5 Matplotlib | `chapters/05-matplotlib/` | ✅ 完成（案例卡升级） | 案例卡3个+lab 32cell/22code（新增9cell）、34 页 PDF（含章扉页）、strict 0 |
| 6 NetworkX | `chapters/06-networkx/` | ✅ 完成（案例卡升级） | 案例卡3个+lab 30cell/19code（新增9cell）、38 页 PDF（含章扉页）、strict 0 |
| 7 Statsmodels | `chapters/07-statsmodels/` | ✅ 完成（案例卡升级） | 案例卡3个+lab 30cell/19code（新增9cell）、39 页 PDF（含章扉页）、strict 0 |
| 8 scikit-learn | `chapters/08-sklearn/` | ✅ 完成（案例卡升级） | 案例卡3个+lab 26cell/17code（新增9cell）、35 页 PDF（含章扉页）、strict 0 |

## 全校验（2026 汇总）

- `python build/validate_book.py`：chapters=9、**appendices=1**、notebooks ok=29、labs=9、missing internal links=0、problems=0 ✅
- **M12（第2–8章案例卡+Lab升级）**：7 章每章 3 个精讲案例卡 + lab 新增 9 个跟练/变形/综合 cell；逐章 `validate_code --strict` = 0 问题；全书 **322 页**、附录 37 页、TeX 编译通过；CI 逐章双绿。
- 第 0 章：quiz 15 题自动评分答案 15/15；lab0 运行 10/10；全书 PDF 181 页；教材TeX main.pdf 编译通过。
- 各章 lab 均逐章执行通过；各章合订 PDF 均已生成于 `教材PDF/`。
