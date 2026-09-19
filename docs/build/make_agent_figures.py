# -*- coding: utf-8 -*-
"""Generate concept figures for chapter 09 (AI agent coding with DeepSeek Harness).

所有箭头都用 patchA/patchB 锚定到方框本体，箭头端点落在方框边界外 1.5pt，
因此不会指进文字框内部；方框坐标之间保留 >= 1.5 单位间隙，避免边界重叠。
"""
import os
import math
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "chapters", "09-agent-basics", "images")
os.makedirs(OUT, exist_ok=True)

plt.rcParams["figure.dpi"] = 150
plt.rcParams["savefig.bbox"] = "tight"
plt.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei", "DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False

BLUE = "#2f6fb3"
ORANGE = "#e07b39"
GREEN = "#3a8f4f"
PURPLE = "#7a5bb5"
TEAL = "#0f7b8a"
RED = "#c0392b"
GRAY = "#5b6570"
DARK = "#22303c"
LIGHT = "#eef4fb"
PALE = "#e4e9f0"

def new_ax(w=11.0, h=6.5):
    fig, ax = plt.subplots(figsize=(w, h))
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis("off")
    return fig, ax

def box(ax, x, y, w, h, text, fc, tc="white", fs=11, ec=None, bold=True, ls="-", lw=1.3):
    p = FancyBboxPatch((x, y), w, h,
                       boxstyle="round,pad=0.6,rounding_size=2.2",
                       linewidth=lw, edgecolor=ec or fc, facecolor=fc, linestyle=ls,
                       mutation_aspect=1.0)
    ax.add_patch(p)
    p.center = (x + w / 2.0, y + h / 2.0)
    if text:
        ax.text(p.center[0], p.center[1], text, ha="center", va="center", fontsize=fs,
                color=tc, weight="bold" if bold else "normal", linespacing=1.7)
    return p

def arrow(a, b, color=GRAY, lw=1.6, rad=0.0, ms=13, ls="-"):
    ax = a.axes
    ax.add_patch(FancyArrowPatch(posA=a.center, posB=b.center, patchA=a, patchB=b,
                                 shrinkA=1.5, shrinkB=1.5, arrowstyle="-|>",
                                 mutation_scale=ms, linewidth=lw, color=color,
                                 linestyle=ls,
                                 connectionstyle="arc3,rad=" + str(rad)))

def title(ax, text, sub=None):
    ax.text(50, 95, text, ha="center", va="center", fontsize=15, weight="bold", color=DARK)
    if sub:
        ax.text(50, 88.5, sub, ha="center", va="center", fontsize=10.5, color=GRAY)

def save(fig, name):
    fig.savefig(os.path.join(OUT, name), facecolor="white")
    plt.close(fig)
    print("[ok]", name)

def fig_agent_vs_completion():
    fig, ax = new_ax(11, 6.5)
    title(ax, "三代编程助手：从补全到 Agent", "同样是 AI，能做的事完全不同")
    cols = [
        ("代码补全", BLUE, "看你正在写的这一行", "猜出下一行代码", "你负责：想清楚、跑通、验证"),
        ("对话式编程", ORANGE, "你贴报错、贴片段", "给出代码与解释", "你负责：复制粘贴、串起来、验证"),
        ("Agent 编程", GREEN, "你给目标与验收标准", "读文件 / 跑命令" + chr(10) + "改代码 / 再验证", "你负责：定义问题、定验收、做终审"),
    ]
    for i, (name, color, how, what, duty) in enumerate(cols):
        x = 3 + i * 32.5
        head = box(ax, x, 78, 29, 9, name, color, fs=13)
        hw = box(ax, x, 62, 29, 12, how, LIGHT, tc=DARK, fs=10.5, bold=False, ec=color)
        wt = box(ax, x, 44, 29, 14, what, color, fs=10.0)
        dt = box(ax, x, 26, 29, 12, duty, "white", tc=DARK, fs=10, bold=False, ec=color)
        arrow(head, hw, color=color, ms=12)
        arrow(hw, wt, color=color, ms=12)
        arrow(wt, dt, color=color, ms=12)
    save(fig, "agent_vs_completion.png")

def fig_agent_loop():
    fig, ax = new_ax(9.5, 8)
    title(ax, "一次 Agent 循环的解剖", "未达标就继续下一轮，达标才交付；必要时请人介入")
    cx, cy, R = 50, 48, 28
    nodes = [
        ("1 读", "读文件 / 看目录 / 查报错", 90),
        ("2 想", "拆解任务 / 定计划", 18),
        ("3 做", "调工具：改代码 / 跑命令", -54),
        ("4 看", "读输出：测试结果 / 报错", -126),
        ("5 判", "达标了吗？", -198),
    ]
    boxes = []
    for label, desc, deg in nodes:
        a = math.radians(deg)
        x = cx + R * math.cos(a)
        y = cy + R * math.sin(a)
        boxes.append(box(ax, x - 14, y - 7.5, 28, 15,
                         label + chr(10) + desc, BLUE, fs=9.5))
    for i in range(5):
        arrow(boxes[i], boxes[(i + 1) % 5], color=GRAY, rad=-0.22, ms=12)
    core = Circle((cx, cy), 11, facecolor=LIGHT, edgecolor=BLUE, linewidth=1.4)
    ax.add_patch(core)
    core.center = (cx, cy)
    ax.text(cx, cy + 2.6, "上下文", ha="center", va="center", fontsize=12, weight="bold", color=BLUE)
    ax.text(cx, cy - 3.4, "历史 + 文件" + chr(10) + "+ 工具输出", ha="center", va="center", fontsize=8.5, color=GRAY, linespacing=1.5)
    done = box(ax, 27, 5, 46, 10, "达标 → 交付：产物 + 证据 + 说明", GREEN, fs=11)
    arrow(core, done, color=GREEN, ms=12)
    ax.text(51.2, 34, "达标", ha="left", va="center", fontsize=9, color=GREEN)
    save(fig, "agent_loop.png")

def fig_harness_anatomy():
    fig, ax = new_ax(11, 6.5)
    title(ax, "harness（智能体框架）由五件事组成", "模型只是其中一件；差距往往在其余四件")
    core = box(ax, 30, 40, 40, 18, "Agent 循环" + chr(10) + "读 → 想 → 做 → 看 → 判", BLUE, fs=13)
    m = box(ax, 2, 68, 24, 14, "模型 LLM" + chr(10) + "推理与决策", ORANGE, fs=10)
    t = box(ax, 74, 68, 24, 14, "工具 Tools" + chr(10) + "读写文件 / 跑命令", GREEN, fs=10)
    c = box(ax, 2, 14, 24, 14, "上下文 Context" + chr(10) + "历史 + 指令 + 文件", PURPLE, fs=9.5)
    p = box(ax, 74, 14, 24, 14, "权限 Permission" + chr(10) + "能不能写 / 要审批", RED, fs=9.5)
    s = box(ax, 36, 14, 28, 14, "会话 Session" + chr(10) + "全程记录可回看", TEAL, fs=10)
    arrow(m, core, color=ORANGE, rad=0.12)
    arrow(t, core, color=GREEN, rad=-0.12)
    arrow(c, core, color=PURPLE, rad=0.12)
    arrow(p, core, color=RED, rad=-0.12)
    arrow(s, core, color=TEAL)
    ax.text(50, 8, "工作区 workspace：Agent 能看见和改动的边界", ha="center", va="center", fontsize=10, color=DARK)
    save(fig, "harness_anatomy.png")

def fig_context_window():
    fig, ax = new_ax(11, 5.8)
    title(ax, "上下文窗口：Agent 的短期记忆", "窗口再大也会满；满了就要压缩或遗忘")
    segs = [
        ("系统提示 + AGENTS.md", 18, ORANGE),
        ("对话历史", 20, BLUE),
        ("读入的文件内容", 26, GREEN),
        ("工具输出（日志 / 报错）", 22, PURPLE),
        ("剩余", 10, PALE),
    ]
    x = 2
    for name, w, color in segs:
        tc = DARK if color == PALE else "white"
        box(ax, x, 62, w - 1.2, 12, name, color, tc=tc, fs=8.5, r=1.0) if False else box(ax, x, 62, w - 1.2, 12, name, color, tc=tc, fs=8.5)
        x += w
    ax.text(2, 54, "一次长任务后：上下文接近占满", ha="left", va="center", fontsize=10, color=GRAY)
    mid = box(ax, 46, 40, 8, 8, "压缩", TEAL, fs=10)
    comp = box(ax, 4, 24, 92, 12, "压缩 compaction：保留任务目标、结论与关键证据，丢弃冗余过程", TEAL, fs=11)
    arrow(mid, comp, color=TEAL, ms=12)
    segs2 = [
        ("目标 + 约束 + 验收标准", 28, ORANGE),
        ("结论与证据", 24, GREEN),
        ("最近几轮对话", 30, BLUE),
        ("剩余", 14, PALE),
    ]
    x = 2
    for name, w, color in segs2:
        tc = DARK if color == PALE else "white"
        box(ax, x, 6, w - 1.2, 12, name, color, tc=tc, fs=8.5)
        x += w
    save(fig, "context_window.png")

def fig_install_paths():
    fig, ax = new_ax(11, 6.8)
    title(ax, "三条安装路径：先选场景，再选命令", "版本基线 v0.1.5-rc.2；命令以官方当前版本为准")
    top = box(ax, 31, 74, 38, 10, "我想用 DeepSeek Harness", DARK, fs=12)
    paths = [
        (3, "只要试用 / 机房机器", "不装进系统，用完即走", "npx @deepseek-ai/dsh web", BLUE),
        (35.5, "长期使用 / 要脚本化", "可跑无界面任务、进流水线", "npm i -g @deepseek-ai/dsh", ORANGE),
        (68, "要原生窗口 / 自带运行时", "源码构建，官方无预编译包", "pnpm run package:desktop:win:x64", GREEN),
    ]
    for x, scene, why, cmd, color in paths:
        h = box(ax, x, 54, 29, 12, scene, color, fs=11)
        c = box(ax, x, 34, 29, 12, cmd, LIGHT, tc=DARK, fs=8.4, bold=False, ec=color)
        r = box(ax, x, 16, 29, 12, why, "white", tc=GRAY, fs=9, bold=False, ec=color)
        arrow(top, h, color=color, rad=0.10, ms=12)
        arrow(h, c, color=color, ms=11)
        arrow(c, r, color=color, ls=":", ms=10)
    ax.text(50, 8, "共同前置：先装 Node.js（自带 npm 与 npx），要求 ^22.19.0 或 >= 24", ha="center", va="center", fontsize=10, color=RED)
    save(fig, "install_paths.png")

def fig_permission_flow():
    fig, ax = new_ax(11, 6.2)
    title(ax, "权限档位与审批：把风险关在笼子里", "默认从最小权限开始，按需放开")
    tiers = [
        ("read-only", "只读：能看不能改", BLUE),
        ("workspace-write", "只能改工作区内的文件", ORANGE),
        ("danger-full-access", "全盘可写、命令直通（慎用）", RED),
    ]
    for i, (name, desc, color) in enumerate(tiers):
        box(ax, 2, 68 - i * 18, 34, 13, name + chr(10) + desc, color, fs=9.5)
    a = box(ax, 44, 66, 24, 11, "Agent 请求动作", DARK, fs=10.5)
    b = box(ax, 44, 44, 24, 11, "权限判定", PURPLE, fs=10.5)
    c = box(ax, 74, 66, 24, 11, "只读范围" + chr(10) + "直接执行", GREEN, fs=10)
    d = box(ax, 74, 44, 24, 11, "写 / 跑命令" + chr(10) + "弹窗审批", ORANGE, fs=10)
    e = box(ax, 74, 22, 24, 11, "你决定：" + chr(10) + "允许 / 拒绝", RED, fs=10)
    arrow(a, b, color=GRAY)
    arrow(a, c, color=GREEN)
    arrow(b, d, color=ORANGE)
    arrow(d, e, color=RED)
    box(ax, 40, 6, 58, 9, "所有动作写进会话记录，随时可回看与追责", LIGHT, tc=DARK, fs=10, bold=False, ec=GRAY)
    save(fig, "permission_flow.png")

def fig_api_key_flow():
    fig, ax = new_ax(11, 5.2)
    title(ax, "API Key：从注册到填进 dsh", "价格与政策会变，以官方页面为准")
    steps = [
        ("1 注册", "开放平台账号", BLUE),
        ("2 实名认证", "个人 / 企业", ORANGE),
        ("3 充值", "支付宝 / 微信", GREEN),
        ("4 创建 API Key", "只显示一次", PURPLE),
        ("5 填入 dsh", "设置 → 模型", TEAL),
    ]
    prev = None
    for i, (name, desc, color) in enumerate(steps):
        x = 3 + i * 19.6
        cur = box(ax, x, 56, 16.4, 16, name + chr(10) + desc, color, fs=9.0)
        if prev is not None:
            arrow(prev, cur, color=GRAY, ms=10)
        prev = cur
    box(ax, 6, 30, 40, 14, "账单与发票：按消耗或充值开票" + chr(10) + "普票 / 专票；未消费可退款", LIGHT, tc=DARK, fs=9.5, bold=False, ec=BLUE)
    box(ax, 54, 30, 40, 14, "安全习惯：不进 git / 不截图" + chr(10) + "泄漏立即删除并重建", LIGHT, tc=DARK, fs=9.5, bold=False, ec=RED)
    ax.text(50, 16, "记住：API 调用按 token 计费，先估算再开跑", ha="center", va="center", fontsize=10.5, color=DARK)
    save(fig, "api_key_flow.png")

def fig_subagent_split():
    fig, ax = new_ax(11, 6.2)
    title(ax, "子代理分工：主代理负责合并与验收", "适合探索、并行、评审；小任务不必拆")
    main = box(ax, 3, 42, 22, 16, "主代理" + chr(10) + "定计划 / 合并 / 验收", DARK, fs=10.5)
    frame = FancyBboxPatch((44, 18), 36, 52, boxstyle="round,pad=0.6,rounding_size=2.5",
                           linewidth=1.3, edgecolor=PURPLE, facecolor=LIGHT, linestyle="--")
    ax.add_patch(frame)
    ax.text(63, 67.5, "统一上下文（主代理维护）", ha="center", va="center", fontsize=9.5, color=PURPLE)
    subs = [
        (52, "探索代理" + chr(10) + "读代码 / 查资料", BLUE),
        (36, "实现代理" + chr(10) + "写脚本 / 改代码 / 跑测试", ORANGE),
        (20, "评审代理" + chr(10) + "找错 / 提反例 / 查泄漏", GREEN),
    ]
    for y, name, color in subs:
        s = box(ax, 47, y, 30, 12, name, color, fs=9.0)
        arrow(main, s, color=color, rad=0.10, ms=11)
        arrow(s, main, color=color, rad=0.10, ms=9, lw=1.1, ls=":")
    box(ax, 6, 4, 74, 9, "产物：脚本 + 测试 + 报告 + 记录（人类终审）", LIGHT, tc=DARK, fs=10.5, bold=False, ec=GRAY)
    save(fig, "subagent_split.png")

def main():
    fig_agent_vs_completion()
    fig_agent_loop()
    fig_harness_anatomy()
    fig_context_window()
    fig_install_paths()
    fig_permission_flow()
    fig_api_key_flow()
    fig_subagent_split()
    import shutil
    for ch in ("10-agent-workflow", "11-agent-cases"):
        dst = os.path.join(ROOT, "chapters", ch, "images")
        os.makedirs(dst, exist_ok=True)
        shutil.copy2(os.path.join(OUT, "subagent_split.png"), os.path.join(dst, "subagent_split.png"))
    print("output dir:", OUT)

if __name__ == "__main__":
    main()
