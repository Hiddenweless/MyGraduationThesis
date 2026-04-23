#!/usr/bin/env python3
"""Draw Figure 2-1: difficulty propagation chain in graph reasoning."""

from __future__ import annotations

from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.patches import Circle, FancyArrowPatch, FancyBboxPatch


ROOT = Path(__file__).resolve().parents[1]
FIG_DIR = ROOT / "SEU-master-thesis-template-master" / "figures" / "paper"
PREVIEW_DIR = ROOT / "preview_figs"

COLORS = {
    "blue": "#4F83C8",
    "blue_dark": "#2F5F9F",
    "blue_light": "#EAF3FF",
    "teal": "#4BAE9F",
    "teal_dark": "#237C72",
    "teal_light": "#E9F7F4",
    "orange": "#F39B62",
    "orange_dark": "#B96A33",
    "orange_light": "#FFF0E4",
    "red": "#D96B6B",
    "red_light": "#FFF1F1",
    "green": "#69B77D",
    "green_light": "#EDF8F0",
    "ink": "#263445",
    "muted": "#687789",
    "line": "#CFD9E6",
    "white": "#FFFFFF",
}


def setup() -> None:
    pingfang = Path("/System/Library/Fonts/PingFang.ttc")
    family = "PingFang HK"
    if pingfang.exists():
        font_manager.fontManager.addfont(str(pingfang))
        family = font_manager.FontProperties(fname=str(pingfang)).get_name()
    mpl.rcParams["svg.fonttype"] = "none"
    mpl.rcParams["pdf.fonttype"] = 42
    mpl.rcParams["font.family"] = [family, "Heiti TC", "Arial Unicode MS", "DejaVu Sans"]
    mpl.rcParams["axes.unicode_minus"] = False


def rounded_box(
    ax: plt.Axes,
    x: float,
    y: float,
    w: float,
    h: float,
    title: str,
    subtitle: str,
    fc: str,
    ec: str,
    title_size: float = 10.5,
    sub_size: float = 7.2,
    lw: float = 1.5,
    radius: float = 0.13,
    z: int = 3,
) -> None:
    patch = FancyBboxPatch(
        (x, y),
        w,
        h,
        boxstyle=f"round,pad=0.018,rounding_size={radius}",
        linewidth=lw,
        facecolor=fc,
        edgecolor=ec,
        zorder=z,
    )
    ax.add_patch(patch)
    ax.text(x + w / 2, y + h * 0.66, title, ha="center", va="center", fontsize=title_size, fontweight="bold", color=COLORS["ink"], zorder=z + 1)
    ax.text(x + w / 2, y + h * 0.36, subtitle, ha="center", va="center", fontsize=sub_size, color=COLORS["muted"], linespacing=1.08, zorder=z + 1)


def stage_card(
    ax: plt.Axes,
    x: float,
    y: float,
    w: float,
    h: float,
    title: str,
    caption: str,
    fc: str,
    ec: str,
) -> None:
    patch = FancyBboxPatch(
        (x, y),
        w,
        h,
        boxstyle="round,pad=0.018,rounding_size=0.13",
        linewidth=1.7,
        facecolor=fc,
        edgecolor=ec,
        zorder=3,
    )
    ax.add_patch(patch)
    ax.text(
        x + w / 2,
        y + h - 0.34,
        title,
        ha="center",
        va="center",
        fontsize=15.6,
        fontweight="bold",
        color="#1F2B3A",
        zorder=6,
    )
    ax.text(
        x + w / 2,
        y + 0.43,
        caption,
        ha="center",
        va="center",
        fontsize=10.2,
        fontweight="bold",
        color="#4B596B",
        linespacing=1.28,
        zorder=6,
    )


def arrow(
    ax: plt.Axes,
    start: tuple[float, float],
    end: tuple[float, float],
    color: str = COLORS["blue_dark"],
    lw: float = 2.2,
    dashed: bool = False,
    rad: float = 0.0,
) -> None:
    ax.add_patch(
        FancyArrowPatch(
            start,
            end,
            arrowstyle="-|>",
            mutation_scale=19,
            linewidth=lw,
            color=color,
            linestyle=(0, (5, 4)) if dashed else "solid",
            connectionstyle=f"arc3,rad={rad}",
            shrinkA=3,
            shrinkB=3,
            zorder=2,
        )
    )


def draw_graph_icon(ax: plt.Axes, cx: float, cy: float, scale: float = 1.0) -> None:
    pts = {
        "A": (-0.45, 0.06),
        "B": (-0.08, 0.32),
        "C": (0.28, 0.15),
        "D": (0.36, -0.28),
        "E": (-0.28, -0.25),
    }
    edges = [("A", "B"), ("A", "E"), ("B", "C"), ("C", "D"), ("D", "E"), ("A", "C"), ("B", "D")]
    for a, b in edges:
        x1, y1 = pts[a]
        x2, y2 = pts[b]
        ax.plot([cx + x1 * scale, cx + x2 * scale], [cy + y1 * scale, cy + y2 * scale], color="#52677D", lw=1.7, zorder=5)
    colors = ["#6FA8DC", "#F6B37F", "#7BCFA6", "#6FA8DC", "#F6B37F"]
    for (name, (x, y)), c in zip(pts.items(), colors):
        ax.add_patch(Circle((cx + x * scale, cy + y * scale), 0.12 * scale, fc=c, ec=COLORS["ink"], lw=0.9, zorder=6))
        ax.text(cx + x * scale, cy + y * scale, name, ha="center", va="center", fontsize=7.0 * scale, color=COLORS["ink"], fontweight="bold", zorder=7)


def draw_serial_icon(ax: plt.Axes, x: float, y: float, w: float) -> None:
    labels = ["边(A,B,2)", "边(B,C,4)", "约束: 回路"]
    colors = [COLORS["blue_light"], COLORS["teal_light"], COLORS["orange_light"], COLORS["green_light"]]
    for i, (lab, fc) in enumerate(zip(labels, colors)):
        yy = y - i * 0.22
        rect = FancyBboxPatch((x, yy), w, 0.14, boxstyle="round,pad=0.01,rounding_size=0.035", fc=fc, ec=COLORS["line"], lw=0.9, zorder=5)
        ax.add_patch(rect)
        ax.text(x + w / 2, yy + 0.07, lab, ha="center", va="center", fontsize=7.4, fontweight="bold", color="#566678", zorder=6)


def draw_reasoning_icon(ax: plt.Axes, cx: float, cy: float) -> None:
    ax.add_patch(Circle((cx, cy + 0.08), 0.34, fc=COLORS["blue_light"], ec=COLORS["blue"], lw=1.5, zorder=5))
    ax.text(cx, cy + 0.08, "LLM", ha="center", va="center", fontsize=13.8, color=COLORS["blue_dark"], fontweight="bold", zorder=7)
    steps = [("识别", cx - 0.72, cy - 0.44, COLORS["orange"]), ("算法", cx, cy - 0.64, COLORS["teal"]), ("验证", cx + 0.72, cy - 0.44, COLORS["green"])]
    for label, px, py, c in steps:
        ax.plot([cx, px], [cy - 0.16, py + 0.12], color=COLORS["line"], lw=1.1, zorder=4)
        ax.add_patch(FancyBboxPatch((px - 0.30, py - 0.11), 0.60, 0.22, boxstyle="round,pad=0.01,rounding_size=0.06", fc=COLORS["white"], ec=c, lw=1.2, zorder=6))
        ax.text(px, py, label, ha="center", va="center", fontsize=7.4, color=COLORS["ink"], fontweight="bold", zorder=7)


def draw_risk_icon(ax: plt.Axes, x: float, y: float) -> None:
    risks = [("幻觉", COLORS["red"]), ("漏约束", COLORS["orange"]), ("格式错", COLORS["blue"])]
    for i, (lab, c) in enumerate(risks):
        yy = y - i * 0.28
        ax.add_patch(FancyBboxPatch((x, yy), 1.08, 0.17, boxstyle="round,pad=0.01,rounding_size=0.045", fc=COLORS["white"], ec=c, lw=1.1, zorder=5))
        ax.text(x + 0.54, yy + 0.085, lab, ha="center", va="center", fontsize=7.7, color=c, fontweight="bold", zorder=6)


def draw() -> None:
    setup()
    FIG_DIR.mkdir(parents=True, exist_ok=True)
    PREVIEW_DIR.mkdir(parents=True, exist_ok=True)

    fig, ax = plt.subplots(figsize=(12.8, 3.8))
    ax.set_xlim(0, 13.2)
    ax.set_ylim(0, 3.8)
    ax.axis("off")
    fig.patch.set_facecolor("white")

    # Main cards.
    cards = [
        (0.45, 0.54, 2.55, 2.72, "混杂输入", "节点、边、权重、约束\n混入自然语言描述", COLORS["orange_light"], COLORS["orange"]),
        (3.70, 0.54, 2.55, 2.72, "序列化压平", "图拓扑转为文本序列\n邻接关系逐渐弱化", COLORS["blue_light"], COLORS["blue"]),
        (6.95, 0.54, 2.55, 2.72, "耦合式推理", "识别、选型、生成、验证\n压缩在一次回答中", COLORS["teal_light"], COLORS["teal"]),
        (10.20, 0.54, 2.55, 2.72, "错误输出风险", "幻觉、漏约束、格式错\n在链路末端集中暴露", COLORS["red_light"], COLORS["red"]),
    ]
    for c in cards:
        stage_card(ax, *c)

    # Visual icons inside each card.
    draw_graph_icon(ax, 1.73, 2.00, 0.95)
    draw_serial_icon(ax, 4.52, 2.18, 0.92)
    draw_reasoning_icon(ax, 8.22, 2.13)
    draw_risk_icon(ax, 10.93, 2.24)

    # Main propagation arrows.
    arrow(ax, (3.02, 1.90), (3.68, 1.90), COLORS["blue_dark"], lw=3.0)
    arrow(ax, (6.27, 1.90), (6.93, 1.90), COLORS["blue_dark"], lw=3.0)
    arrow(ax, (9.52, 1.90), (10.18, 1.90), COLORS["blue_dark"], lw=3.0)

    for suffix in ["svg", "pdf"]:
        fig.savefig(FIG_DIR / f"graph_reasoning_challenge.{suffix}", bbox_inches="tight", pad_inches=0.04)
    fig.savefig(PREVIEW_DIR / "graph_reasoning_challenge.png", dpi=230, bbox_inches="tight", pad_inches=0.04)
    plt.close(fig)


if __name__ == "__main__":
    draw()
