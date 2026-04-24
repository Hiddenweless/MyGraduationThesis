#!/usr/bin/env python3
"""Draw Chapter 5 experiment summary figures."""

from __future__ import annotations

from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager
from matplotlib.patches import FancyBboxPatch


ROOT = Path(__file__).resolve().parents[1]
FIG_DIR = ROOT / "SEU-master-thesis-template-master" / "figures" / "paper"
PREVIEW_DIR = ROOT / "preview_figs"

COLORS = {
    "ink": "#243244",
    "muted": "#657386",
    "grid": "#D9E2EF",
    "blue": "#4F83C8",
    "blue_dark": "#2F5F9F",
    "teal": "#4BAE9F",
    "orange": "#F39B62",
    "red": "#D96B6B",
    "green": "#69B77D",
    "gray": "#B8C4D4",
    "bg": "#F8FAFD",
}


def setup() -> None:
    pingfang = Path("/System/Library/Fonts/PingFang.ttc")
    family = "PingFang HK"
    if pingfang.exists():
        font_manager.fontManager.addfont(str(pingfang))
        family = font_manager.FontProperties(fname=str(pingfang)).get_name()
    mpl.rcParams["font.family"] = [family, "Heiti TC", "Arial Unicode MS", "DejaVu Sans"]
    mpl.rcParams["axes.unicode_minus"] = False
    mpl.rcParams["svg.fonttype"] = "none"
    mpl.rcParams["pdf.fonttype"] = 42


def polish_axes(ax: plt.Axes, ylim: tuple[float, float] = (0, 105)) -> None:
    ax.set_ylim(*ylim)
    ax.spines[["top", "right", "left"]].set_visible(False)
    ax.spines["bottom"].set_color(COLORS["grid"])
    ax.tick_params(axis="y", length=0, labelsize=8.5, colors=COLORS["muted"])
    ax.tick_params(axis="x", length=0, labelsize=9, colors=COLORS["ink"])
    ax.grid(axis="y", color=COLORS["grid"], linewidth=0.8, alpha=0.75)
    ax.set_axisbelow(True)
    ax.set_ylabel("准确率（%）", fontsize=9.5, color=COLORS["muted"])


def add_value_labels(ax: plt.Axes, bars, dy: float = 1.1, fontsize: float = 7.0) -> None:
    for bar in bars:
        h = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            h + dy,
            f"{h:.1f}",
            ha="center",
            va="bottom",
            fontsize=fontsize,
            color=COLORS["muted"],
        )


def save(fig: plt.Figure, name: str) -> None:
    FIG_DIR.mkdir(parents=True, exist_ok=True)
    PREVIEW_DIR.mkdir(parents=True, exist_ok=True)
    for suffix in ["svg", "pdf"]:
        fig.savefig(FIG_DIR / f"{name}.{suffix}", bbox_inches="tight", pad_inches=0.05)
    fig.savefig(PREVIEW_DIR / f"{name}.png", dpi=230, bbox_inches="tight", pad_inches=0.05)
    plt.close(fig)


def draw_overall() -> None:
    datasets = ["GraphArena", "NLGraph", "GraphWiz", "LLM4DyG", "GraphInstruct", "平均"]
    gpt = np.array([43.50, 51.40, 47.61, 58.04, 78.18, 55.75])
    graphteam = np.array([95.49, 97.71, 88.62, 96.35, 98.33, 95.30])
    gcoder = np.array([94.80, 96.90, 90.20, 93.78, 97.39, 94.61])
    plangraph = np.array([97.88, 98.72, 97.01, 96.11, 98.74, 97.69])

    x = np.arange(len(datasets))
    width = 0.18
    fig, ax = plt.subplots(figsize=(11.6, 4.4))
    fig.patch.set_facecolor("white")
    ax.set_facecolor("white")
    polish_axes(ax, (35, 103))

    bars1 = ax.bar(x - 1.5 * width, gpt, width, label="GPT-4o", color=COLORS["gray"], edgecolor="white", linewidth=0.8)
    ax.bar(x - 0.5 * width, graphteam, width, label="GraphTeam", color=COLORS["teal"], edgecolor="white", linewidth=0.8)
    ax.bar(x + 0.5 * width, gcoder, width, label="GCoder", color=COLORS["orange"], edgecolor="white", linewidth=0.8)
    bars4 = ax.bar(x + 1.5 * width, plangraph, width, label="PlanGraph", color=COLORS["blue"], edgecolor="white", linewidth=0.8)

    ax.set_xticks(x)
    ax.set_xticklabels(datasets)
    ax.legend(ncol=4, loc="upper center", bbox_to_anchor=(0.5, 1.08), frameon=False, fontsize=9)

    add_value_labels(ax, bars4, dy=0.8, fontsize=7.2)
    for bar in bars1:
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.8, f"{bar.get_height():.0f}", ha="center", va="bottom", fontsize=6.8, color=COLORS["muted"])

    save(fig, "exp_overall_accuracy")


def draw_category() -> None:
    cats = ["图结构分析", "最短路径", "匹配问题", "流优化", "哈密顿类"]
    gpt = np.array([86.20, 75.50, 46.80, 68.20, 20.33])
    sota = np.array([98.75, 97.10, 95.40, 97.53, 81.35])
    plangraph = np.array([99.43, 99.12, 99.40, 96.82, 95.33])

    x = np.arange(len(cats))
    width = 0.24
    fig, ax = plt.subplots(figsize=(10.4, 4.3))
    fig.patch.set_facecolor("white")
    ax.set_facecolor("white")
    polish_axes(ax, (0, 106))

    ax.bar(x - width, gpt, width, label="GPT-4o", color=COLORS["gray"], edgecolor="white", linewidth=0.8)
    ax.bar(x, sota, width, label="SOTA", color=COLORS["orange"], edgecolor="white", linewidth=0.8)
    bars = ax.bar(x + width, plangraph, width, label="PlanGraph", color=COLORS["blue"], edgecolor="white", linewidth=0.8)
    ax.set_xticks(x)
    ax.set_xticklabels(cats)
    ax.legend(ncol=3, loc="upper center", bbox_to_anchor=(0.5, 1.08), frameon=False, fontsize=9)
    add_value_labels(ax, bars, dy=1.0, fontsize=7.3)

    save(fig, "exp_category_accuracy")


def draw_difficulty_scale() -> None:
    groups = ["非 NP-hard", "NP-hard"]
    base_np = np.array([99.20, 92.50])
    plan_np = np.array([99.60, 96.50])

    scales = ["小规模", "中规模", "大规模"]
    base_scale = np.array([97.00, 95.20, 92.40])
    plan_scale = np.array([99.10, 98.00, 96.30])

    fig, axes = plt.subplots(1, 2, figsize=(11.0, 4.2), gridspec_kw={"wspace": 0.28})
    fig.patch.set_facecolor("white")

    ax = axes[0]
    polish_axes(ax, (88, 101.5))
    x = np.arange(len(groups))
    width = 0.28
    ax.bar(x - width / 2, base_np, width, label="最优基线", color=COLORS["orange"], edgecolor="white", linewidth=0.8)
    bars = ax.bar(x + width / 2, plan_np, width, label="PlanGraph", color=COLORS["blue"], edgecolor="white", linewidth=0.8)
    ax.set_xticks(x)
    ax.set_xticklabels(groups)
    ax.set_title("任务复杂度分层", fontsize=12.2, fontweight="bold", color=COLORS["ink"], pad=16)
    add_value_labels(ax, bars, dy=0.25, fontsize=7.2)
    for i, gain in enumerate(plan_np - base_np):
        ax.text(i, min(plan_np[i] + 1.25, 101.0), f"+{gain:.1f}", ha="center", va="center", fontsize=8.5, color=COLORS["blue_dark"], fontweight="bold")

    ax = axes[1]
    polish_axes(ax, (90, 101))
    x = np.arange(len(scales))
    ax.plot(x, base_scale, marker="o", markersize=6.5, linewidth=2.4, color=COLORS["orange"], label="最优基线")
    ax.plot(x, plan_scale, marker="o", markersize=6.5, linewidth=2.4, color=COLORS["blue"], label="PlanGraph")
    ax.fill_between(x, base_scale, plan_scale, color=COLORS["blue"], alpha=0.10)
    ax.set_xticks(x)
    ax.set_xticklabels(scales)
    ax.set_title("图规模分层", fontsize=12.2, fontweight="bold", color=COLORS["ink"], pad=16)
    for i, gain in enumerate(plan_scale - base_scale):
        ax.text(i, plan_scale[i] + 0.45, f"+{gain:.1f}", ha="center", va="bottom", fontsize=8.2, color=COLORS["blue_dark"], fontweight="bold")

    handles, labels = axes[1].get_legend_handles_labels()
    fig.legend(handles, labels, ncol=2, loc="upper center", bbox_to_anchor=(0.5, 1.02), frameon=False, fontsize=9)

    save(fig, "exp_difficulty_scale")


def draw_ablation() -> None:
    datasets = ["GraphArena", "NLGraph", "GraphWiz"]
    methods = ["完整模型", "去除规划", "去除检索", "去除验证"]
    values = np.array(
        [
            [97.88, 98.72, 97.01],
            [86.35, 89.14, 84.27],
            [94.12, 95.33, 92.48],
            [92.67, 94.01, 90.72],
        ]
    )
    colors = [COLORS["blue"], COLORS["red"], COLORS["teal"], COLORS["orange"]]

    x = np.arange(len(datasets))
    width = 0.18
    fig, ax = plt.subplots(figsize=(9.8, 4.2))
    fig.patch.set_facecolor("white")
    ax.set_facecolor("white")
    polish_axes(ax, (80, 101.5))

    offsets = [-1.5 * width, -0.5 * width, 0.5 * width, 1.5 * width]
    for i, (method, color, offset) in enumerate(zip(methods, colors, offsets)):
        bars = ax.bar(x + offset, values[i], width, label=method, color=color, edgecolor="white", linewidth=0.8)
        if i == 0:
            add_value_labels(ax, bars, dy=0.35, fontsize=7.2)

    ax.set_xticks(x)
    ax.set_xticklabels(datasets)
    ax.legend(ncol=4, loc="upper center", bbox_to_anchor=(0.5, 1.08), frameon=False, fontsize=9)

    save(fig, "exp_ablation")


def main() -> None:
    setup()
    draw_overall()
    draw_category()
    draw_difficulty_scale()
    draw_ablation()


if __name__ == "__main__":
    main()
