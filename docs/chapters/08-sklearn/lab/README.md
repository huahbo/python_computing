# 第 8 章 上机实验（lab/）

> 本目录是第 8 章的**上机实验**：一份可独立完成的 `lab.ipynb`，覆盖从环境自检到综合任务的完整流程。

## 文件

| 文件 | 说明 |
| ---- | ---- |
| `lab.ipynb` | 上机实验 notebook（14 个单元：4 个 Part，含 TODO 与检查项） |
| `wine_lab_pca.png` | 运行 Part 4 后生成的图（示例/输出） |

## 如何开始

1. 打开 `lab.ipynb`（JupyterLab / VS Code）；
2. 按顺序运行 Part 1 → Part 4；
3. 完成所有 `# TODO`，记录输出；
4. 在末尾 `提交清单` 逐项打钩；
5. 导出（可选）后提交 `.ipynb`。

## 各部分用时建议

| Part | 内容 | 建议时间 |
| ---- | ---- | ---- |
| 环境自检 | 打印 sklearn/numpy/pandas/matplotlib 版本 | 5 min |
| 1 | 数据预处理（编码 / 缩放 / 切分 / 交叉验证） | 15 min |
| 2 | 有监督（Iris 分类 + Diabetes 回归） | 15 min |
| 3 | 无监督（KMeans / DBSCAN / PCA / LDA） | 15 min |
| 4 | 综合任务（Wine 端到端 + 保存图） | 20 min |

## 教师说明

- 可作为一次 2–3 学时的上机课；
- 检查重点：Part 1 的 `fit_transform` 泄漏、Part 2 的分类/回归指标、Part 3 的 KMeans vs DBSCAN、Part 4 的 `wine_lab_pca.png` 与 3 句结论；
- 可要求学生把每个 Part 的输出截图附在报告里。

## 配套

- 讲义：`../01-数据集的预处理.md` … `../05-常见误区与技巧.md`
- 作业：`../exercises/`
- 综合案例参考：`../04-综合案例.md`
