# -*- coding: utf-8 -*-
"""Append the fixed 8-week schedule position to each chapter's teaching.md."""
import os, io

WEEKS = {
    "01-numpy": 1, "02-sympy": 2, "03-scipy": 3, "04-pandas": 4,
    "05-matplotlib": 5, "06-networkx": 6, "07-statsmodels": 7, "08-sklearn": 8,
}
for ch, week in WEEKS.items():
    p = os.path.join("chapters", ch, "teaching.md")
    if not os.path.exists(p):
        print("[missing]", p); continue
    with io.open(p, encoding="utf-8") as f:
        text = f.read()
    if "课表定位" in text:
        print("[skip]", p); continue
    block = f"""
---

## 课表定位（8 周制）

- 周次：第 {week} 周
- 上课：2 学时（精讲 + 演示）
- 上机：4 学时（单独排课，以 lab/ 为主，含 0.5h 回顾与 0.5h 总结/quiz）
- 课后：完成 exercises/ 的 quiz 与 assignment；06 常见误区页自学
"""
    with io.open(p, "a", encoding="utf-8") as f:
        f.write(block)
    print("[appended]", p)
