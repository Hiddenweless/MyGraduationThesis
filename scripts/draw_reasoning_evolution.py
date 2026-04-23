#!/usr/bin/env python3
"""Draw Figure 2-2: evolution of LLM reasoning enhancement methods."""

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
    "green": "#69B77D",
    "green_dark": "#34764A",
    "green_light": "#EDF8F0",
    "purple": "#8F7AC8",
    "purple_dark": "#6651A6",
    "purple_light": "#F1EEFF",
    "ink": "#253244",
    "muted": "#617184",
    "line": "#D4DEE9",
    "white": "#FFFFFF",
    "panel": "#F7FAFE",
}


def setup() -> None:
    for path in [
        "/System/Library/Fonts/PingFang.ttc",
        "/System/Library/Fonts/STHeiti Light.ttc",
        "/System/Library/Fonts/STHeiti Medium.ttc",
        "/Library/Fonts/Arial Unicode.ttf",
    ]:
        font_path = Path(path)
        if font_path.exists():
            try:
                font_manager.fontManager.addfont(str(font_path))
            except Exception:
                pass

    mpl.rcParams["pdf.fonttype"] = 42
    mpl.rcParams["ps.fonttype"] = 42
    mpl.rcParams["svg.fonttype"] = "none"
    mpl.rcParams["font.family"] = [
        "Heiti TC",
        "Arial Unicode MS",
        "DejaVu Sans",
    ]
    mpl.rcParams["axes.unicode_minus"] = False


def rounded_box(
    ax: plt.Axes,
    x: float,
    y: float,
    w: float,
    h: float,
    fc: str,
    ec: str,
    lw: float = 1.5,
    radius: float = 0.14,
    zorder: int = 2,
) -> FancyBboxPatch:
    patch = FancyBboxPatch(
        (x, y),
        w,
        h,
        boxstyle=f"round,pad=0.018,rounding_size={radius}",
        linewidth=lw,
        facecolor=fc,
        edgecolor=ec,
        zorder=zorder,
    )
    ax.add_patch(patch)
    return patch


def arrow(
    ax: plt.Axes,
    start: tuple[float, float],
    end: tuple[float, float],
    color: str,
    lw: float = 2.4,
    mutation_scale: float = 17,
    rad: float = 0.0,
    zorder: int = 3,
) -> None:
    ax.add_patch(
        FancyArrowPatch(
            start,
            end,
            arrowstyle="-|>",
            mutation_scale=mutation_scale,
            linewidth=lw,
            color=color,
            connectionstyle=f"arc3,rad={rad}",
            shrinkA=3,
            shrinkB=3,
            zorder=zorder,
        )
    )


def label_pill(
    ax: plt.Axes,
    x: float,
    y: float,
    text: str,
    fc: str,
    ec: str,
    width: float = 1.12,
) -> None:
    rounded_box(ax, x, y, width, 0.24, fc, ec, lw=1.0, radius=0.065, zorder=5)
    ax.text(
        x + width / 2,
        y + 0.12,
        text,
        ha="center",
        va="center",
        fontsize=7.8,
        fontweight="bold",
        color=COLORS["ink"],
        zorder=6,
    )


def draw_stage(
    ax: plt.Axes,
    x: float,
    y: float,
    w: float,
    h: float,
    index: str,
    title: str,
    subtitle: str,
    methods: list[str],
    boundary: str,
    fc: str,
    ec: str,
    dark: str,
) -> None:
    rounded_box(ax, x, y, w, h, fc, ec, lw=1.7, radius=0.20, zorder=2)
    ax.add_patch(Circle((x + 0.38, y + h - 0.38), 0.20, facecolor=dark, edgecolor=dark, lw=1.0, zorder=5))
    ax.text(
        x + 0.38,
        y + h - 0.38,
        index,
        ha="center",
        va="center",
        fontsize=10.8,
        fontweight="bold",
        color=COLORS["white"],
        zorder=6,
    )
    ax.text(
        x + 0.72,
        y + h - 0.34,
        title,
        ha="left",
        va="center",
        fontsize=14.5,
        fontweight="bold",
        color=COLORS["ink"],
        zorder=6,
    )
    ax.text(
        x + 0.72,
        y + h - 0.70,
        subtitle,
        ha="left",
        va="center",
        fontsize=8.9,
        color=COLORS["muted"],
        zorder=6,
    )

    ax.text(
        x + 0.30,
        y + 1.28,
        "代表方法",
        ha="left",
        va="center",
        fontsize=8.8,
        fontweight="bold",
        color=dark,
        zorder=6,
    )
    pill_x = x + 0.30
    for i, method in enumerate(methods):
        label_pill(ax, pill_x + i * 1.22, y + 0.93, method, COLORS["white"], ec, width=1.05)

    rounded_box(ax, x + 0.28, y + 0.24, w - 0.56, 0.42, COLORS["white"], COLORS["line"], lw=0.9, radius=0.08, zorder=4)
    ax.text(
        x + w / 2,
        y + 0.45,
        boundary,
        ha="center",
        va="center",
        fontsize=8.6,
        fontweight="bold",
        color=COLORS["muted"],
        zorder=6,
    )


def draw_icon_prompt(ax: plt.Axes, cx: float, cy: float, dark: str) -> None:
    for i, txt in enumerate(["思考", "分解", "投票"]):
        x = cx - 0.85 + i * 0.85
        rounded_box(ax, x, cy - 0.12, 0.56, 0.24, COLORS["white"], dark, lw=1.1, radius=0.055, zorder=6)
        ax.text(x + 0.28, cy, txt, ha="center", va="center", fontsize=7.4, fontweight="bold", color=COLORS["ink"], zorder=7)
        if i < 2:
            arrow(ax, (x + 0.56, cy), (x + 0.82, cy), dark, lw=1.2, mutation_scale=9, zorder=6)


def draw_icon_tool(ax: plt.Axes, cx: float, cy: float, dark: str) -> None:
    rounded_box(ax, cx - 0.95, cy - 0.35, 0.88, 0.70, COLORS["white"], dark, lw=1.2, radius=0.09, zorder=5)
    ax.text(cx - 0.51, cy + 0.10, "LLM", ha="center", va="center", fontsize=9.5, fontweight="bold", color=dark, zorder=7)
    ax.text(cx - 0.51, cy - 0.14, "规划", ha="center", va="center", fontsize=7.3, color=COLORS["muted"], zorder=7)
    rounded_box(ax, cx + 0.10, cy - 0.35, 0.88, 0.70, COLORS["white"], dark, lw=1.2, radius=0.09, zorder=5)
    ax.text(cx + 0.54, cy + 0.10, "工具", ha="center", va="center", fontsize=9.2, fontweight="bold", color=dark, zorder=7)
    ax.text(cx + 0.54, cy - 0.14, "执行", ha="center", va="center", fontsize=7.3, color=COLORS["muted"], zorder=7)
    arrow(ax, (cx - 0.05, cy), (cx + 0.10, cy), dark, lw=1.4, mutation_scale=10, zorder=7)


def draw_icon_system(ax: plt.Axes, cx: float, cy: float, dark: str) -> None:
    nodes = [
        (cx, cy + 0.28, "规划"),
        (cx - 0.68, cy - 0.22, "检索"),
        (cx + 0.68, cy - 0.22, "验证"),
    ]
    for sx, sy, _ in nodes:
        ax.plot([cx, sx], [cy + 0.02, sy], color=COLORS["line"], lw=1.1, zorder=4)
    for sx, sy, text in nodes:
        ax.add_patch(Circle((sx, sy), 0.26, facecolor=COLORS["white"], edgecolor=dark, lw=1.2, zorder=6))
        ax.text(sx, sy, text, ha="center", va="center", fontsize=7.3, fontweight="bold", color=COLORS["ink"], zorder=7)
    arrow(ax, (cx + 0.42, cy - 0.34), (cx - 0.42, cy - 0.34), dark, lw=1.2, mutation_scale=9, rad=-0.35, zorder=6)


def draw() -> None:
    setup()
    FIG_DIR.mkdir(parents=True, exist_ok=True)
    PREVIEW_DIR.mkdir(parents=True, exist_ok=True)

    fig, ax = plt.subplots(figsize=(12.6, 4.6))
    ax.set_xlim(0, 12.6)
    ax.set_ylim(0, 4.6)
    ax.axis("off")
    fig.patch.set_facecolor("white")

    stages = [
        (
            0.35,
            "提示增强阶段",
            "通过显式中间步骤提升单模型推理稳定性",
            ["CoT", "SC", "ToT"],
            "核心：让模型想得更清楚",
            COLORS["blue_light"],
            COLORS["blue"],
            COLORS["blue_dark"],
            draw_icon_prompt,
        ),
        (
            4.38,
            "工具接入阶段",
            "把精确计算、检索和 API 调用交给外部环境",
            ["PAL", "ReAct", "Toolformer"],
            "核心：把计算交给可靠工具",
            COLORS["orange_light"],
            COLORS["orange"],
            COLORS["orange_dark"],
            draw_icon_tool,
        ),
        (
            8.41,
            "系统化协同阶段",
            "以多智能体、规划、验证和修复组织完整求解链路",
            ["CAMEL", "MetaGPT", "PlanGraph"],
            "核心：形成可追踪闭环",
            COLORS["teal_light"],
            COLORS["teal"],
            COLORS["teal_dark"],
            draw_icon_system,
        ),
    ]

    y, w, h = 0.72, 3.48, 3.22
    for i, stage in enumerate(stages, start=1):
        x, title, subtitle, methods, boundary, fc, ec, dark, icon_func = stage
        draw_stage(ax, x, y, w, h, str(i), title, subtitle, methods, boundary, fc, ec, dark)
        icon_func(ax, x + w / 2, y + 1.86, dark)

    arrow(ax, (3.86, 2.34), (4.32, 2.34), COLORS["blue_dark"], lw=3.0, mutation_scale=20)
    arrow(ax, (7.89, 2.34), (8.35, 2.34), COLORS["blue_dark"], lw=3.0, mutation_scale=20)

    rounded_box(ax, 0.88, 0.18, 10.85, 0.32, COLORS["panel"], COLORS["line"], lw=0.9, radius=0.09, zorder=1)
    ax.text(
        6.30,
        0.34,
        "演进主线：从提示设计到外部工具，再到规划、检索、执行与验证的一体化协同",
        ha="center",
        va="center",
        fontsize=9.6,
        fontweight="bold",
        color=COLORS["ink"],
        zorder=5,
    )

    fig.savefig(FIG_DIR / "reasoning_evolution.pdf", bbox_inches="tight", pad_inches=0.04)
    fig.savefig(FIG_DIR / "reasoning_evolution.png", dpi=300, bbox_inches="tight", pad_inches=0.04)
    fig.savefig(PREVIEW_DIR / "reasoning_evolution.png", dpi=230, bbox_inches="tight", pad_inches=0.04)
    plt.close(fig)


if __name__ == "__main__":
    draw()
