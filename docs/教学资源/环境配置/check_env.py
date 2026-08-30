# -*- coding: utf-8 -*-
"""课程统一环境自检脚本（第 0 章配套）。

用法:
    conda activate scicomp
    python check_env.py
    # 或直接: python 教学资源/环境配置/check_env.py

打印核心库版本与 LaTeX/Git 工具是否存在；缺失必须项时退出码非 0。
"""
import importlib.metadata as md
import importlib.util
import os
import shutil
import sys

CORE_LIBS = [
    ("numpy", "2.0"), ("sympy", "1.12"), ("scipy", "1.11"),
    ("pandas", "2.0"), ("matplotlib", "3.8"), ("seaborn", "0.13"),
    ("networkx", "3.0"), ("statsmodels", "0.14"), ("scikit-learn", "1.4"),
]
TOOLS = [
    ("xelatex", True),     # （必须）LaTeX 中文编译
    ("latexmk", True),     # （必须）一键多遍编译
    ("git", False),        # （可选）版本管理
]


def ver(pkg):
    try:
        return md.version(pkg)
    except Exception:
        return None


def main():
    ok = True
    print("== 课程统一环境自检 ==")
    print("Python:", sys.version.split()[0], "| 解释器:", sys.executable)

    if sys.version_info < (3, 10):
        print("[FAIL] Python 需 >= 3.10，当前", sys.version.split()[0])
        ok = False

    for name, need in CORE_LIBS:
        v = ver(name)
        if v is None:
            print(f"[FAIL] {name:<14} 未安装")
            ok = False
        else:
            print(f"[OK  ] {name:<14} {v}")

    for name, required in TOOLS:
        p = shutil.which(name)
        if p:
            print(f"[OK  ] {name:<12} {p}")
        elif required:
            print(f"[FAIL] {name:<12} 未找到（请安装 TeX Live 并配置 PATH，或使用在线平台）")
            ok = False
        else:
            print(f"[WARN] {name:<12} 未找到（可选）")

    # 可选: 提示内核
    if not importlib.util.find_spec("ipykernel"):
        print("[WARN] ipykernel 未安装，VS Code 可能找不到内核")
    else:
        print("[OK  ] ipykernel 已安装（VS Code 选 scicomp 内核）")

    if ok:
        print("== 自检通过（必须项全部满足）==")
    else:
        print("== 自检未通过：请按 00-02 常见问题表排查 ==")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
