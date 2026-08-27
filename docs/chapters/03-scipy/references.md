# 第 3 章 参考资料（SciPy）

> 本页是第 3 章的**精选参考**：官方文档为第一优先级；教程与习题用于加深理解。链接在编写时已联网核实，仍建议以官方最新版为准。

## 一、官方文档（必读，授课依据）

| 资料 | 链接 | 说明 | 优先级 |
| ---- | ---- | ---- | ---- |
| SciPy 主页 | https://scipy.org/ | 库介绍、版本、安装 | ★必读 |
| SciPy 参考手册（全模块） | https://docs.scipy.org/doc/scipy/reference/ | 按模块查函数签名与示例 | ★必读 |
| scipy.integrate 积分与 ODE | https://docs.scipy.org/doc/scipy/reference/integrate.html | `quad`/`odeint`/`solve_ivp`/`solve_bvp` | ★必读 |
| scipy.optimize 优化 | https://docs.scipy.org/doc/scipy/reference/optimize.html | 求根/极值/规划/拟合 | ★必读 |
| scipy.interpolate 插值 | https://docs.scipy.org/doc/scipy/reference/interpolate.html | 一维/多维/散点插值 | ★必读 |
| scipy.stats 统计 | https://docs.scipy.org/doc/scipy/reference/stats.html | 检验/分布/描述统计 | ★必读 |
| scipy.fft 傅里叶变换 | https://docs.scipy.org/doc/scipy/reference/fft.html | `fft`/`rfft`/`fftfreq` | ★必读 |
| scipy.signal 信号处理 | https://docs.scipy.org/doc/scipy/reference/signal.html | 滤波器设计、卷积 | ★必读 |
| SciPy 版本发布说明 | https://docs.scipy.org/doc/scipy/release.html | 查看函数改名/废弃 | 选读 |
| statsmodels 官方 | https://www.statsmodels.org/stable/ | 方差分析事后比较/回归 | 选读 |

## 二、精品教程（讲得更透 / 有图示）

| 资料 | 链接 | 说明 | 优先级 |
| ---- | ---- | ---- | ---- |
| SciPy Lecture Notes | https://scipy-lectures.org/ | 系统、带图，含 SciPy 章节 | ★推荐 |
| Scientific Python Lectures (GitHub) | https://github.com/jrjohansson/scientific-python-lectures | Lecture-3-Scipy.ipynb，Notebook 形式 | ★推荐 |
| SciPy Cookbook | https://scipy.github.io/old-wiki/pages/Cookbook/ | 大量实战小例子（老但仍有效） | 选读 |
| Python Data Science Handbook (Jake VanderPlas) | https://github.com/jakevdp/PythonDataScienceHandbook | 第 5 章 SciPy 相关，可对照 | ★推荐 |
| SciPy 官方教程（tutorial 目录） | https://docs.scipy.org/doc/scipy/tutorial/ | 官方讲解积分/FFT/插值 | ★推荐 |
| Optimization and Fit Cookbook | https://scipy.github.io/old-wiki/pages/Cookbook/OptimizationAndFitDemo1.html | 拟合示例详解 | 选读 |

## 三、习题与实战（课堂/作业/上机素材）

| 资料 | 链接 | 说明 | 优先级 |
| ---- | ---- | ---- | ---- |
| SciPy-lectures 练习 | https://scipy-lectures.org/ | 每节配练习 | ★推荐 |
| SciPy 官方示例库 | https://docs.scipy.org/doc/scipy/reference/ | 函数页内附示例 | ★必做 |
| 本仓库本章作业 | [./exercises/README.md](./exercises/README.md) | 16 题 + quiz 自动评分 | ★必做 |
| 本仓库本章上机 | [./lab/README.md](./lab/README.md) | 环境自检 + 逐点演练 + 综合任务 | ★必做 |
| 本章综合案例 | [./06-综合案例.md](./06-综合案例.md) | 插值+FFT+拟合+检验+积分 | ★必做 |

## 四、中文补充

| 资料 | 链接 | 说明 | 优先级 |
| ---- | ---- | ---- | ---- |
| SciPy 中文文档镜像 | https://docs.scipy.org.cn/doc/scipy/ | 中文版参考（版本可能较旧） | 中文补充 |
| 猫头虎 SciPy 入门教程 | https://cloud.tencent.cn/developer/article/2449258 | 安装/模块/用例中文入门 | 中文补充 |
| 知乎/CSDN“SciPy 教程”精选 | 搜索“SciPy 数值积分 优化 入门” | 按需筛选，注意核对版本 | 中文补充 |
| 聪明办法学 Python（前置） | https://github.com/datawhalechina/learn-python-the-smart-way-v2 | 前置课程 | 中文补充 |
| 数学建模导论（后续） | https://github.com/datawhalechina/intro-mathmodel | 大量 SciPy 建模案例 | 中文补充 |
| 本项目（科学计算） | https://github.com/datawhalechina/scientific-computing | 本书开源仓库 | 中文补充 |

## 五、资源使用建议

1. **教学**：以官方文档为主线（一节一个知识点），讲完代码后给 1–2 道练习题；
2. **上机**：先跑 `lab/` 再做 `exercises/`；有能力的做 06 综合案例拓展；
3. **查错**：版本迁移问题（如 `trapz`→`trapezoid`、`interp2d`→`RegularGridInterpolator`）以官方 release notes 为准；
4. **结合模型**：把 SciPy 放入《数学建模导论》的真实问题中，学习“把模型写成代码”的能力。

> 本清单整理时间：2026 年（随课程迭代可更新）。欢迎继续补充社区文章。
