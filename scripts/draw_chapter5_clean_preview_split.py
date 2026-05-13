#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Draw Chapter 5 figures and export clean English figures.

This version uses MacTeX/XeLaTeX through Matplotlib's PGF backend.
It avoids Chinese glyph deformation caused by macOS TTC font subsetting
in normal Matplotlib PDF/SVG export.

Output:
    scripts/figures/exp_category_accuracy_clean.pdf/.png
    scripts/figures/exp_complexity_trend_clean.pdf/.png
    scripts/figures/exp_sample_difficulty_trend_clean.pdf/.png
    scripts/figures/exp_ablation_clean.pdf/.png
"""

from __future__ import annotations

from pathlib import Path

import matplotlib as mpl

# Must be set before importing pyplot.
mpl.use("pgf")

import matplotlib.pyplot as plt
import numpy as np


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "scripts" / "figures"

# macOS + MacTeX usually works with these.
# If "Songti SC" fails, try: "PingFang SC", "Heiti SC", "FandolSong-Regular".
LATIN_FONT = "Times New Roman"

COLORS = {
    "ink": "#243244",
    "muted": "#5F6E82",
    "grid": "#DEE6F1",
    "blue": "#4C80C4",
    "blue_dark": "#285A9A",
    "teal": "#3BAA9B",
    "orange": "#F29A61",
    "red": "#D96B6B",
    "gray": "#B8C4D4",
}


def setup() -> None:
    """Configure Matplotlib to use XeLaTeX for text rendering."""
    mpl.rcParams.update(
        {
            "pgf.texsystem": "xelatex",
            "pgf.rcfonts": False,
            "text.usetex": True,
            "font.family": "serif",
            "font.serif": [LATIN_FONT],
            "axes.unicode_minus": False,
            "figure.dpi": 160,
            "savefig.dpi": 320,
            "axes.linewidth": 0.7,
            "pgf.preamble": "\n".join(
                [
                    r"\usepackage{fontspec}",
                    rf"\setmainfont{{{LATIN_FONT}}}",
                    rf"\setsansfont{{{LATIN_FONT}}}",
                    r"\usepackage{amsmath}",
                ]
            ),
        }
    )


def polish_axes(ax: plt.Axes, ylim: tuple[float, float]) -> None:
    """Apply consistent academic-style axis formatting."""
    ax.set_ylim(*ylim)
    ax.set_facecolor("white")

    ax.spines[["top", "right", "left"]].set_visible(False)
    ax.spines["bottom"].set_color(COLORS["grid"])
    ax.spines["bottom"].set_linewidth(0.9)

    ax.tick_params(axis="y", length=0, labelsize=9, colors=COLORS["muted"], pad=4)
    ax.tick_params(axis="x", length=0, labelsize=9.5, colors=COLORS["ink"], pad=7)

    ax.grid(axis="y", color=COLORS["grid"], linewidth=0.8, alpha=0.85)
    ax.set_axisbelow(True)
    ax.set_ylabel(r"Accuracy (\%)", color=COLORS["muted"], labelpad=8, fontsize=9.5)


def label_bars(ax: plt.Axes, bars, dy: float = 0.8, size: float = 7.0) -> None:
    """Label each bar with its numeric value."""
    for bar in bars:
        h = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            h + dy,
            f"{h:.1f}",
            ha="center",
            va="bottom",
            color=COLORS["muted"],
            fontsize=size,
        )


def label_points(ax: plt.Axes, x, y, dy: float = 0.35, size: float = 7.5) -> None:
    """Label each line point with its numeric value."""
    for xi, yi in zip(x, y):
        ax.text(
            xi,
            yi + dy,
            f"{yi:.1f}",
            ha="center",
            va="bottom",
            color=COLORS["muted"],
            fontsize=size,
        )


def save_figure(fig: plt.Figure, name: str) -> None:
    """Save one figure as both PDF and PNG."""
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUT_DIR / f"{name}.pdf", bbox_inches="tight", pad_inches=0.04)
    fig.savefig(OUT_DIR / f"{name}.png", bbox_inches="tight", pad_inches=0.04, dpi=220)
    plt.close(fig)


def draw_category() -> None:
    """Draw task-category performance comparison."""
    cats = ["Structural\nanalysis", "Shortest\npath", "Matching", "Flow\noptimization", "Hamiltonian\ntasks"]

    # 任务归类口径：
    # 图结构分析：GraphArena-CN/CC/GD, NLGraph-CONN/CYC, GraphWiz-CYC/CONN
    # 最短路径：GraphArena-SD, NLGraph-SP, GraphWiz-SP
    # 匹配问题：NLGraph-BM, GraphWiz-BIP/SM
    # 流优化：NLGraph-MF, GraphWiz-MF
    # 哈密顿类：GraphArena-TSP, NLGraph-HP, GraphWiz-HP
    gpt = np.array([93.31, 83.67, 84.10, 68.20, 20.33])
    sota = np.array([98.60, 98.80, 99.17, 94.40, 74.30])
    plangraph = np.array([98.74, 99.50, 99.60, 96.32, 95.33])

    x = np.arange(len(cats))
    width = 0.24

    fig, ax = plt.subplots(figsize=(10.4, 4.1))
    fig.patch.set_facecolor("white")
    polish_axes(ax, (0, 106))

    bars_gpt = ax.bar(
        x - width,
        gpt,
        width,
        label="GPT-4o",
        color=COLORS["gray"],
        edgecolor="white",
        linewidth=0.7,
    )

    bars_sota = ax.bar(
        x,
        sota,
        width,
        label="Best baseline",
        color=COLORS["orange"],
        edgecolor="white",
        linewidth=0.7,
    )

    bars_plan = ax.bar(
        x + width,
        plangraph,
        width,
        label="PlanGraph",
        color=COLORS["blue"],
        edgecolor="white",
        linewidth=0.7,
    )

    ax.set_xticks(x)
    ax.set_xticklabels(cats)

    leg = ax.legend(
        ncol=3,
        loc="upper center",
        bbox_to_anchor=(0.5, 1.09),
        frameon=False,
        fontsize=9,
    )
    for text in leg.get_texts():
        text.set_color(COLORS["ink"])

    label_bars(ax, bars_gpt, dy=0.75, size=7.0)
    label_bars(ax, bars_sota, dy=0.75, size=7.0)
    label_bars(ax, bars_plan, dy=0.75, size=7.0)

    save_figure(fig, "exp_category_accuracy_clean")


def draw_complexity_trend() -> None:
    """Draw task-complexity stratified performance trend."""
    groups = ["Non-NP-complete", "NP-complete"]
    base_np = np.array([99.20, 92.50])
    plan_np = np.array([99.60, 96.50])

    x = np.arange(len(groups))

    fig, ax = plt.subplots(figsize=(5.6, 4.0))
    fig.patch.set_facecolor("white")
    polish_axes(ax, (88, 100.5))

    ax.plot(
        x,
        base_np,
        marker="o",
        markersize=6.2,
        linewidth=2.2,
        color=COLORS["orange"],
        label="Best baseline",
    )
    ax.plot(
        x,
        plan_np,
        marker="o",
        markersize=6.2,
        linewidth=2.2,
        color=COLORS["blue"],
        label="PlanGraph",
    )

    ax.fill_between(x, base_np, plan_np, color=COLORS["blue"], alpha=0.10)

    ax.set_xticks(x)
    ax.set_xticklabels(groups)

    # 两个类别时适当留白，避免折线贴边。
    ax.set_xlim(-0.25, len(groups) - 0.75)

    leg = ax.legend(
        ncol=2,
        loc="upper center",
        bbox_to_anchor=(0.5, 1.10),
        frameon=False,
        fontsize=9,
    )
    for text in leg.get_texts():
        text.set_color(COLORS["ink"])

    # 手动放置数值标注，避免 99.2 和 99.6 与折线/点重叠。
    ax.text(
        x[0] - 0.04,
        base_np[0] - 0.55,
        f"{base_np[0]:.1f}",
        ha="center",
        va="top",
        fontsize=7.5,
        color=COLORS["ink"],
    )
    ax.text(
        x[1],
        base_np[1] + 0.25,
        f"{base_np[1]:.1f}",
        ha="center",
        va="bottom",
        fontsize=7.5,
        color=COLORS["ink"],
    )

    ax.text(
        x[0] + 0.06,
        plan_np[0] + 0.30,
        f"{plan_np[0]:.1f}",
        ha="center",
        va="bottom",
        fontsize=7.5,
        color=COLORS["ink"],
    )
    ax.text(
        x[1],
        plan_np[1] + 0.25,
        f"{plan_np[1]:.1f}",
        ha="center",
        va="bottom",
        fontsize=7.5,
        color=COLORS["ink"],
    )

    save_figure(fig, "exp_complexity_trend_clean")


def draw_sample_difficulty_trend() -> None:
    """Draw sample-difficulty stratified performance trend."""
    scales = ["Easy", "Medium", "Hard"]
    base_scale = np.array([97.00, 95.20, 92.40])
    plan_scale = np.array([99.10, 98.00, 96.30])

    x = np.arange(len(scales))

    fig, ax = plt.subplots(figsize=(6.4, 4.0))
    fig.patch.set_facecolor("white")
    polish_axes(ax, (90, 100.5))

    ax.plot(
        x,
        base_scale,
        marker="o",
        markersize=6.2,
        linewidth=2.2,
        color=COLORS["orange"],
        label="Best baseline",
    )
    ax.plot(
        x,
        plan_scale,
        marker="o",
        markersize=6.2,
        linewidth=2.2,
        color=COLORS["blue"],
        label="PlanGraph",
    )

    ax.fill_between(x, base_scale, plan_scale, color=COLORS["blue"], alpha=0.10)

    ax.set_xticks(x)
    ax.set_xticklabels(scales)

    leg = ax.legend(
        ncol=2,
        loc="upper center",
        bbox_to_anchor=(0.5, 1.10),
        frameon=False,
        fontsize=9,
    )
    for text in leg.get_texts():
        text.set_color(COLORS["ink"])

    label_points(ax, x, base_scale, dy=0.25, size=7.5)
    label_points(ax, x, plan_scale, dy=0.25, size=7.5)

    save_figure(fig, "exp_sample_difficulty_trend_clean")


def draw_ablation() -> None:
    """Draw ablation comparison."""
    datasets = ["GraphArena", "NLGraph", "GraphWiz"]
    methods = ["Full model", "No planning", "No retrieval", "No verification"]

    values = np.array(
        [
            [97.88, 98.72, 97.01],
            [86.35, 89.14, 84.27],
            [94.12, 95.33, 92.48],
            [92.67, 94.01, 90.72],
        ]
    )

    colors = [
        COLORS["blue"],
        COLORS["red"],
        COLORS["teal"],
        COLORS["orange"],
    ]

    x = np.arange(len(datasets))
    width = 0.18

    fig, ax = plt.subplots(figsize=(9.8, 4.0))
    fig.patch.set_facecolor("white")
    polish_axes(ax, (80, 102.0))

    offsets = [-1.5 * width, -0.5 * width, 0.5 * width, 1.5 * width]

    for method, color, offset, row in zip(methods, colors, offsets, values):
        bars = ax.bar(
            x + offset,
            row,
            width,
            label=method,
            color=color,
            edgecolor="white",
            linewidth=0.7,
        )
        label_bars(ax, bars, dy=0.35, size=7.0)

    ax.set_xticks(x)
    ax.set_xticklabels(datasets)

    leg = ax.legend(
        ncol=4,
        loc="upper center",
        bbox_to_anchor=(0.5, 1.09),
        frameon=False,
        fontsize=9,
    )
    for text in leg.get_texts():
        text.set_color(COLORS["ink"])

    save_figure(fig, "exp_ablation_clean")


def main() -> None:
    setup()
    draw_category()
    draw_complexity_trend()
    draw_sample_difficulty_trend()
    draw_ablation()
    print(f"saved PDF figures to {OUT_DIR}")


if __name__ == "__main__":
    main()
