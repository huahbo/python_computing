# -*- coding: utf-8 -*-
"""Generate concept figures for chapter 09 (AI agent coding with DeepSeek Harness)."""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "chapters", "09-agent", "images")
os.makedirs(OUT, exist_ok=True)

plt.rcParams["figure.dpi"] = 150
plt.rcParams["savefig.bbox"] = "tight"
plt.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei", "DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False

BLUE = "#2f6fb3"
ORANGE = "#e07b39"
GREEN = "#3a8f4f"
PURPLE = "#7a5bb5"
GRAY = "#5b6570"
LIGHT = "#eef4fb"
DARK = "#22303c"

def new_ax(w=11.0, h=6.0):
    fig, ax = plt.subplots(figsize=(w, h))
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis("off")
    return fig, ax

def box(ax, x, y, w, h, text, fc, tc="white", fs=11, ec=None, bold=True, r=2.2):
    ax.add_patch(FancyBboxPatch((x, y), w, h,
                                boxstyle="round,pad=0.6,rounding_size=" + str(r),
                                linewidth=1.3, edgecolor=ec or fc, facecolor=fc,
                                mutation_aspect=1.0))
    ax.text(x + w / 2.0, y + h / 2.0, text, ha="center", va="center", fontsize=fs,
            color=tc, weight="bold" if bold else "normal", linespacing=1.7)

def arrow(ax, p, q, color=GRAY, lw=1.6, rad=0.0, style="-|>", ms=13):
    ax.add_patch(FancyArrowPatch(p, q, arrowstyle=style, mutation_scale=ms,
                                 linewidth=lw, color=color,
                                 connectionstyle="arc3,rad=" + str(rad)))

def title(ax, text, sub=None):
    ax.text(50, 95, text, ha="center", va="center", fontsize=15, weight="bold", color=DARK)
    if sub:
        ax.text(50, 88.5, sub, ha="center", va="center", fontsize=10.5, color=GRAY)

def save(fig, name):
    path = os.path.join(OUT, name)
    fig.savefig(path, facecolor="white")
    plt.close(fig)
    print("[ok]", name)

def fig_agent_vs_completion():
    fig, ax = new_ax(11, 6)
    title(ax, "三代编程助手：从补全到 Agent", "同样是 AI，能做的事完全不同")
    cols = [
        ("代码补全", BLUE, "看你正在写的这一行", "猜出下一行代码", "你负责：想清楚、跑通、验证"),
        ("对话式编程", ORANGE, "你贴报错、贴片段", "给出代码与解释", "你负责：复制粘贴、串起来、验证"),
        ("Agent 编程", GREEN, "你给目标与验收标准", "读文件 / 跑命令" + chr(10) + "改代码 / 再验证", "你负责：定义问题、定验收、做终审"),
    ]
    for i, (name, color, how, what, duty) in enumerate(cols):
        x = 5 + i * 31.5
        box(ax, x, 76, 26, 10, name, color, fs=13)
        box(ax, x, 55, 26, 16, how, LIGHT, tc=DARK, fs=10.5, bold=False, ec=color)
        arrow(ax, (x + 13, 54), (x + 13, 47), color=color)
        box(ax, x, 30, 26, 15, what, color, fs=10.0)
        box(ax, x, 8, 26, 17, duty, "white", tc=DARK, fs=10, bold=False, ec=color)
    save(fig, "agent_vs_completion.png")

def fig_agent_loop():
    fig, ax = new_ax(9, 8)
    title(ax, "一次 Agent 循环的解剖", "循环直到满足验收标准，或需要人介入")
    cx, cy, R = 50, 46, 27
    nodes = [
        ("1 读", "读文件 / 看目录 / 查报错", 90),
        ("2 想", "拆解任务 / 定计划", 18),
        ("3 做", "调工具：改代码 / 跑命令", -54),
        ("4 看", "读输出：测试结果 / 报错", -126),
        ("5 判", "达标了吗？", -198),
    ]
    import math
    for label, desc, deg in nodes:
        a = math.radians(deg)
        x = cx + R * math.cos(a)
        y = cy + R * math.sin(a)
        box(ax, x - 13, y - 6, 26, 12, label, BLUE, fs=11.5)
        ax.text(x, y - 10.5, desc, ha="center", va="center", fontsize=8.5, color=GRAY)
    for deg in [90, 18, -54, -126]:
        a1 = math.radians(deg - 14)
        a2 = math.radians(deg - 58)
        arrow(ax, (cx + R * math.cos(a1), cy + R * math.sin(a1)),
              (cx + R * math.cos(a2), cy + R * math.sin(a2)), rad=-0.25, color=GRAY)
    ax.add_patch(Circle((cx, cy), 14, facecolor=LIGHT, edgecolor=BLUE, linewidth=1.4))
    ax.text(cx, cy + 2.5, "上下文", ha="center", va="center", fontsize=12, weight="bold", color=BLUE)
    ax.text(cx, cy - 3.5, "历史 + 文件 + 工具输出", ha="center", va="center", fontsize=8.5, color=GRAY)
    box(ax, 30, 3, 40, 9, "达标 → 交付：产物 + 证据 + 说明", GREEN, fs=10.5)
    arrow(ax, (36, 20), (44, 12.5), color=GREEN, rad=-0.2)
    arrow(ax, (50, 20), (50, 13), color=GREEN)
    save(fig, "agent_loop.png")

def fig_harness_anatomy():
    fig, ax = new_ax(11, 6.5)
    title(ax, "harness（智能体框架）由五件事组成", "模型只是其中一件；差距往往在其余四件")
    box(ax, 30, 38, 40, 20, "Agent 循环" + chr(10) + "读 → 想 → 做 → 看 → 判", BLUE, fs=13)
    parts = [
        (2, 68, "模型 LLM", "推理与决策", ORANGE),
        (74, 68, "工具 Tools", "读写文件 / 跑命令 / 搜索", GREEN),
        (2, 12, "上下文 Context", "会话历史 + 指令 + 文件内容", PURPLE),
        (74, 12, "权限 Permission", "能不能写 / 要不要审批", "#c0392b"),
    ]
    for x, y, name, desc, color in parts:
        box(ax, x, y, 24, 16, name + chr(10) + desc, color, fs=9.5)
    box(ax, 34, 12, 32, 14, "会话 Session", "#0f7b8a", fs=11)
    ax.text(50, 9, "工作区 workspace：Agent 能看见和改动的边界", ha="center", va="center", fontsize=10, color=DARK)
    arrow(ax, (20, 76), (34, 58), color=ORANGE, rad=0.15)
    arrow(ax, (80, 76), (66, 58), color=GREEN, rad=-0.15)
    arrow(ax, (18, 28), (32, 42), color=PURPLE, rad=0.15)
    arrow(ax, (82, 28), (70, 42), color="#c0392b", rad=-0.15)
    arrow(ax, (50, 26), (50, 39), color="#0f7b8a")
    save(fig, "harness_anatomy.png")

def fig_context_window():
    fig, ax = new_ax(11, 5.5)
    title(ax, "上下文窗口：Agent 的短期记忆", "窗口再大也会满；满了就要压缩或遗忘")
    segs = [
        ("系统提示 + AGENTS.md", 18, ORANGE),
        ("对话历史", 20, BLUE),
        ("读入的文件内容", 26, GREEN),
        ("工具输出（日志 / 报错）", 22, PURPLE),
        ("剩余空间", 10, "#dfe6ee"),
    ]
    x = 2
    for name, w, color in segs:
        tc = DARK if color == "#dfe6ee" else "white"
        box(ax, x, 56, w, 12, name, color, tc=tc, fs=9.0)
        x += w
    ax.text(4, 50, "一次长任务后：上下文接近占满", ha="left", va="center", fontsize=10, color=GRAY)
    arrow(ax, (50, 46), (50, 38), color=GRAY, lw=2)
    box(ax, 8, 22, 84, 13, "压缩 compaction：保留任务目标、结论与关键证据，丢弃冗余过程", "#0f7b8a", fs=11)
    segs2 = [
        ("目标 + 约束 + 验收标准", 28, ORANGE),
        ("结论与证据", 24, GREEN),
        ("最近几轮对话", 30, BLUE),
        ("剩余空间", 14, "#dfe6ee"),
    ]
    x = 2
    for name, w, color in segs2:
        tc = DARK if color == "#dfe6ee" else "white"
        box(ax, x, 4, w, 12, name, color, tc=tc, fs=9.0)
        x += w
    save(fig, "context_window.png")

def fig_install_paths():
    fig, ax = new_ax(11, 6.5)
    title(ax, "三条安装路径：先选场景，再选命令", "版本基线 v0.1.5-rc.2；命令以官方当前版本为准")
    box(ax, 33, 72, 34, 10, "我想用 DeepSeek Harness", DARK, fs=12)
    paths = [
        (3, "只要试用 / 机房机器", "不装进系统，用完即走", "npx @deepseek-ai/dsh web", BLUE),
        (35.5, "长期使用 / 要脚本化", "可跑无界面任务、进流水线", "npm i -g @deepseek-ai/dsh", ORANGE),
        (68, "要原生窗口 / 自带运行时", "源码构建，官方无预编译包", "pnpm run package:desktop:win:x64", GREEN),
    ]
    for i, (x, scene, why, cmd, color) in enumerate(paths):
        arrow(ax, (50, 71), (x + 14, 66), color=color, rad=0.12)
        box(ax, x, 54, 29, 12, scene, color, fs=11)
        ax.text(x + 14.5, 49, why, ha="center", va="center", fontsize=9, color=GRAY)
        box(ax, x, 33, 29, 12, cmd, LIGHT, tc=DARK, fs=8.6, bold=False, ec=color)
        last = "浏览器界面" + chr(10) + "127.0.0.1:3080" if i < 2 else "原生窗口" + chr(10) + "端口 19387"
        box(ax, x, 16, 29, 13, last, "white", tc=DARK, fs=9.5, bold=False, ec=color)
    ax.text(50, 7, "共同前置：先装 Node.js（自带 npm 与 npx），要求 ^22.19.0 或 >= 24", ha="center", va="center", fontsize=10, color="#c0392b")
    save(fig, "install_paths.png")

def fig_permission_flow():
    fig, ax = new_ax(11, 6)
    title(ax, "权限档位与审批：把风险关在笼子里", "默认从最小权限开始，按需放开")
    tiers = [
        ("read-only", "只读：能看不能改", BLUE),
        ("workspace-write", "只能改工作区内的文件", ORANGE),
        ("danger-full-access", "全盘可写、命令直通（慎用）", "#c0392b"),
    ]
    for i, (name, desc, color) in enumerate(tiers):
        y = 66 - i * 17
        box(ax, 3, y, 34, 12, name + chr(10) + desc, color, fs=9.5)
    box(ax, 45, 62, 24, 12, "Agent 请求动作", DARK, fs=11)
    box(ax, 45, 40, 24, 12, "权限判定", PURPLE, fs=11)
    arrow(ax, (57, 61), (57, 53), color=GRAY)
    box(ax, 74, 62, 23, 12, "只读范围" + chr(10) + "直接执行", GREEN, fs=10)
    box(ax, 74, 40, 23, 12, "写 / 跑命令" + chr(10) + "弹窗审批", ORANGE, fs=10)
    arrow(ax, (69, 68), (73, 68), color=GREEN)
    arrow(ax, (69, 46), (73, 46), color=ORANGE)
    box(ax, 74, 18, 23, 12, "你决定：允许 / 拒绝", "#c0392b", fs=10)
    arrow(ax, (85.5, 39), (85.5, 31), color="#c0392b")
    box(ax, 40, 10, 62, 8, "所有动作写进会话记录，随时可回看与追责", LIGHT, tc=DARK, fs=10, bold=False, ec=GRAY)
    save(fig, "permission_flow.png")

def fig_api_key_flow():
    fig, ax = new_ax(11, 5)
    title(ax, "API Key：从注册到填进 dsh", "价格与政策会变，以官方页面为准")
    steps = [
        ("1 注册", "开放平台账号", BLUE),
        ("2 实名认证", "个人 / 企业", ORANGE),
        ("3 充值", "支付宝 / 微信", GREEN),
        ("4 创建 API Key", "只显示一次", PURPLE),
        ("5 填入 dsh", "设置 → 模型", "#0f7b8a"),
    ]
    for i, (name, desc, color) in enumerate(steps):
        x = 2 + i * 19.6
        box(ax, x, 52, 18.4, 16, name + chr(10) + desc, color, fs=9.5)
        if i < 4:
            arrow(ax, (x + 18.4, 60), (x + 19.6, 60), color=GRAY, ms=11)
    box(ax, 6, 26, 40, 14, "账单与发票：按消耗或充值开票" + chr(10) + "普票 / 专票；未消费可退款", LIGHT, tc=DARK, fs=9.5, bold=False, ec=BLUE)
    box(ax, 54, 26, 40, 14, "安全习惯：不进 git / 不截图" + chr(10) + "泄漏立即删除并重建", LIGHT, tc=DARK, fs=9.5, bold=False, ec="#c0392b")
    ax.text(50, 12, "记住：API 调用按 token 计费，先估算再开跑", ha="center", va="center", fontsize=10.5, color=DARK)
    save(fig, "api_key_flow.png")

def fig_subagent_split():
    fig, ax = new_ax(11, 6)
    title(ax, "子代理分工：主代理负责合并与验收", "适合探索、并行、评审；小任务不必拆")
    box(ax, 3, 40, 24, 18, "主代理" + chr(10) + "定计划 / 合并 / 验收", DARK, fs=11)
    subs = [
        (52, "探索代理", "读代码 / 查资料 / 摸清数据", BLUE),
        (36, "实现代理", "写脚本 / 改代码 / 跑测试", ORANGE),
        (20, "评审代理", "找错 / 提反例 / 查数据泄漏", GREEN),
    ]
    for y, name, desc, color in subs:
        box(ax, 48, y, 30, 13, name + chr(10) + desc, color, fs=10)
        arrow(ax, (27.5, 52), (47, y + 10), color=color, rad=0.12, ms=11)
        arrow(ax, (47, y + 3), (27.5, 46), color=color, rad=0.12, ms=11, style="-|>")
    box(ax, 84, 24, 14, 28, "统一" + chr(10) + "上下文", PURPLE, fs=10.5)
    box(ax, 6, 10, 74, 9, "产物：脚本 + 测试 + 报告 + 记录（人类终审）", LIGHT, tc=DARK, fs=10.5, bold=False, ec=GRAY)
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
    print("output dir:", OUT)

if __name__ == "__main__":
    main()
