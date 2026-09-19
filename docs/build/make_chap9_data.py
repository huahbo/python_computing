# -*- coding: utf-8 -*-
"""Generate demo data and the buggy script for chapter 09 (AI agent coding) lab."""
import os
import numpy as np
import pandas as pd

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "chapters", "09-agent", "lab", "data")
os.makedirs(OUT, exist_ok=True)

NAMES = ["张三", "李四", "王五", "赵六", "钱七", "孙八", "周九", "吴十"]
IDS = ["2024001", "2024002", "2024003", "2024004", "2024005", "2024006", "2024007", "2024008"]
USUAL = [82, 60, 95, 70, 88, 55, 91, 76]
MID = [90, 65, 88, 72, 76, 68, 94, 80]
FINAL = [78, 70, 92, 68, 85, 62, 89, 74]
KLASS = ["一班", "一班", "一班", "一班", "二班", "二班", "二班", "二班"]

def write_scores():
    df = pd.DataFrame({"学号": IDS, "姓名": NAMES, "班级": KLASS,
                       "平时": USUAL, "期中": MID, "期末": FINAL})
    path = os.path.join(OUT, "scores.csv")
    df.to_csv(path, index=False, encoding="utf-8-sig")
    print("[ok] scores.csv", df.shape)

def write_dirty():
    df = pd.DataFrame({"学号": IDS, "姓名": NAMES, "班级": KLASS,
                       "平时": USUAL, "期中": MID, "期末": FINAL})
    df.loc[df["姓名"] == "李四", ["期中", "期末"]] = np.nan
    df.loc[df["姓名"] == "孙八", "期末"] = 999.0
    df.loc[df["姓名"] == "王五", "姓名"] = "  王五 "
    df.loc[df["姓名"] == "周九", "班级"] = np.nan
    extra = pd.DataFrame([{"学号": "2024009 ", "姓名": "郑十一", "班级": "二班",
                           "平时": 68, "期中": 74, "期末": 71},
                          {"学号": "2024010", "姓名": "冯十二", "班级": "一班",
                           "平时": 84, "期中": 81, "期末": 86}])
    df = pd.concat([df, extra], ignore_index=True)
    df = pd.concat([df, df.iloc[[0]]], ignore_index=True)
    path = os.path.join(OUT, "scores_dirty.csv")
    df.to_csv(path, index=False, encoding="utf-8-sig")
    print("[ok] scores_dirty.csv", df.shape)

def write_sensor():
    rng = np.random.default_rng(20240919)
    t = np.arange(240)
    temp = 20.0 + 0.02 * t + 3.0 * np.sin(2 * np.pi * t / 24.0) + rng.normal(0, 0.5, t.size)
    vib = 0.50 + 0.10 * np.sin(2 * np.pi * t / 12.0 + 0.7) + rng.normal(0, 0.02, t.size)
    df = pd.DataFrame({"t": t, "温度": np.round(temp, 3), "振动": np.round(vib, 4)})
    path = os.path.join(OUT, "sensor.csv")
    df.to_csv(path, index=False, encoding="utf-8-sig")
    print("[ok] sensor.csv", df.shape)

BUGGY = [
    "# 成绩分析脚本（案例一用：这段代码有 2 个隐蔽的错误）",
    "import numpy as np",
    "import pandas as pd",
    "",
    "df = pd.read_csv('data/scores.csv')",
    "subjects = ['平时', '期中', '期末']",
    "scores = df[subjects].to_numpy(dtype=float)",
    "",
    "# 1) 每个学生的平均分（期望：8 个数，每个学生一个）",
    "student_mean = scores.mean(axis=0)",
    "",
    "# 2) 归一化到 0-1，用于画成绩对比图",
    "norm = (scores - scores.min()) / (scores.max() - scores.min())",
    "",
    "# 3) 加权总分：平时 20% + 期中 30% + 期末 50%",
    "weights = np.array([0.2, 0.3, 0.5])",
    "total = scores @ weights",
    "",
    "print('每个学生的平均分:', np.round(student_mean, 2))",
    "print('归一化矩阵形状:', norm.shape)",
    "print('加权总分前 3 名:', np.round(total[:3], 2))",
    "print('全班平均:', round(float(scores.mean()), 2))",
]

def write_buggy():
    path = os.path.join(OUT, "scores_buggy.py")
    with open(path, "w", encoding="utf-8") as f:
        f.write(chr(10).join(BUGGY) + chr(10))
    print("[ok] scores_buggy.py")

def main():
    write_scores()
    write_dirty()
    write_sensor()
    write_buggy()
    print("output dir:", OUT)

if __name__ == "__main__":
    main()
