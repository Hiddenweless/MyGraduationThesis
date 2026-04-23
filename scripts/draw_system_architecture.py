#!/usr/bin/env python3
"""Draw the PlanGraph system architecture figure.

Outputs:
  - /Users/wtl/Desktop/我的毕业论文/scripts/figures/system_architecture.svg
  - /Users/wtl/Desktop/我的毕业论文/scripts/figures/system_architecture.pdf
  - /Users/wtl/Desktop/我的毕业论文/scripts/figures/system_architecture.png
"""

from __future__ import annotations

from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch


SCRIPT_DIR = Path(__file__).resolve().parent
FIG_DIR = SCRIPT_DIR / "figures"


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
    "ink": "#263445",
    "muted": "#687789",
    "white": "#FFFFFF",
    "panel": "#F7FAFE",
    "soft_gray": "#F8FAFC",
    "line": "#D6E0EC",
}


def setup() -> None:
    candidates = [
        "/System/Library/Fonts/PingFang.ttc",
        "/System/Library/Fonts/STHeiti Light.ttc",
        "/Library/Fonts/Arial Unicode.ttf",
    ]
    for p in candidates:
        fp = Path(p)
        if fp.exists():
            try:
                font_manager.fontManager.addfont(str(fp))
            except Exception:
                pass

    mpl.rcParams["svg.fonttype"] = "none"
    mpl.rcParams["pdf.fonttype"] = 42
    mpl.rcParams["ps.fonttype"] = 42
    mpl.rcParams["font.family"] = [
        "PingFang SC",
        "PingFang HK",
        "Heiti SC",
        "STHeiti",
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
    title: str,
    subtitle: str = "",
    fc: str = COLORS["white"],
    ec: str = COLORS["blue"],
    lw: float = 1.6,
    radius: float = 0.16,
    title_size: float = 12.0,
    sub_size: float = 8.0,
    title_color: str = COLORS["ink"],
    sub_color: str = COLORS["muted"],
    title_weight: str = "bold",
    zorder: int = 3,
) -> FancyBboxPatch:
    patch = FancyBboxPatch(
        (x, y),
        w,
        h,
        boxstyle=f"round,pad=0.02,rounding_size={radius}",
        linewidth=lw,
        facecolor=fc,
        edgecolor=ec,
        zorder=zorder,
    )
    ax.add_patch(patch)

    if subtitle:
        ax.text(
            x + w / 2,
            y + h * 0.64,
            title,
            ha="center",
            va="center",
            fontsize=title_size,
            fontweight=title_weight,
            color=title_color,
            zorder=zorder + 1,
        )
        ax.text(
            x + w / 2,
            y + h * 0.33,
            subtitle,
            ha="center",
            va="center",
            fontsize=sub_size,
            color=sub_color,
            zorder=zorder + 1,
        )
    else:
        ax.text(
            x + w / 2,
            y + h / 2,
            title,
            ha="center",
            va="center",
            fontsize=title_size,
            fontweight=title_weight,
            color=title_color,
            zorder=zorder + 1,
        )
    return patch


def frame(
    ax: plt.Axes,
    x: float,
    y: float,
    w: float,
    h: float,
    title: str,
    ec: str,
    fc: str,
    title_size: float = 12.0,
    zorder: int = 0,
) -> FancyBboxPatch:
    patch = FancyBboxPatch(
        (x, y),
        w,
        h,
        boxstyle="round,pad=0.03,rounding_size=0.24",
        facecolor=fc,
        edgecolor=ec,
        linewidth=1.7,
        zorder=zorder,
    )
    ax.add_patch(patch)
    ax.text(
        x + 0.24,
        y + h - 0.30,
        title,
        ha="left",
        va="center",
        fontsize=title_size,
        fontweight="bold",
        color=COLORS["ink"],
        zorder=zorder + 2,
    )
    return patch


def arrow(
    ax: plt.Axes,
    start: tuple[float, float],
    end: tuple[float, float],
    color: str = COLORS["blue"],
    lw: float = 2.0,
    dashed: bool = False,
    rad: float = 0.0,
    label: str | None = None,
    label_offset: tuple[float, float] = (0.0, 0.0),
    mutation_scale: float = 13.0,
    zorder: int = 2,
) -> None:
    arr = FancyArrowPatch(
        start,
        end,
        arrowstyle="-|>",
        mutation_scale=mutation_scale,
        linewidth=lw,
        color=color,
        linestyle=(0, (5, 4)) if dashed else "solid",
        connectionstyle=f"arc3,rad={rad}",
        shrinkA=3,
        shrinkB=3,
        zorder=zorder,
    )
    ax.add_patch(arr)

    if label:
        mx = (start[0] + end[0]) / 2 + label_offset[0]
        my = (start[1] + end[1]) / 2 + label_offset[1]
        ax.text(
            mx,
            my,
            label,
            ha="center",
            va="center",
            fontsize=7.8,
            color=color,
            bbox=dict(boxstyle="round,pad=0.16", fc="white", ec="none", alpha=0.92),
            zorder=zorder + 2,
        )


def module(
    ax: plt.Axes,
    x: float,
    y: float,
    w: float,
    h: float,
    title: str,
    subtitle: str = "",
    fc: str = COLORS["white"],
    ec: str = COLORS["blue"],
    title_size: float = 10.0,
    sub_size: float = 7.2,
    lw: float = 1.35,
    radius: float = 0.12,
    zorder: int = 3,
) -> None:
    rounded_box(
        ax,
        x,
        y,
        w,
        h,
        title,
        subtitle,
        fc=fc,
        ec=ec,
        lw=lw,
        radius=radius,
        title_size=title_size,
        sub_size=sub_size,
        zorder=zorder,
    )


def draw() -> None:
    setup()
    FIG_DIR.mkdir(parents=True, exist_ok=True)

    fig, ax = plt.subplots(figsize=(14.2, 7.6))
    ax.set_xlim(0, 14.2)
    ax.set_ylim(0, 7.6)
    ax.axis("off")
    fig.patch.set_facecolor("white")

    flow = COLORS["blue"]
    flow_light = COLORS["blue_dark"]
    feedback = COLORS["orange"]
    support = COLORS["teal_dark"]
    state_color = COLORS["green_dark"]

    # 1. 输入区
    rounded_box(
        ax,
        0.75,
        6.38,
        3.45,
        0.62,
        "输入与任务建模",
        "问题、图数据与约束条件",
        fc=COLORS["blue_light"],
        ec=COLORS["blue"],
        lw=1.5,
        radius=0.11,
        title_size=10.0,
        sub_size=7.0,
    )

    # 2. 主控调度器
    rounded_box(
        ax,
        4.80,
        6.08,
        4.60,
        1.08,
        "主控调度器",
        "阶段推进  |  事件路由  |  预算控制  |  恢复决策",
        fc=COLORS["blue_light"],
        ec=COLORS["blue"],
        lw=2.0,
        radius=0.18,
        title_size=13.2,
        sub_size=8.7,
    )

    arrow(ax, (4.20, 6.69), (4.80, 6.62), color=flow, lw=2.1)

    # 3. 执行层
    frame(
        ax,
        0.75,
        3.22,
        10.95,
        1.54,
        "多智能体执行层",
        ec=COLORS["orange"],
        fc="#FFFBF7",
        title_size=12.3,
    )

    stage_y = 3.66
    stage_h = 0.62
    stage_w = 2.05
    stage_xs = [1.10, 3.45, 5.80, 8.15]
    stages = [
        ("理解与规划", "问题解析 + 规划生成"),
        ("知识与工具调用", "图谱检索 + 外部知识 + 程序生成"),
        ("执行与验证", "运行结果校验与一致性检查"),
        ("结果输出", "答案组织与结果返回"),
    ]

    for (title, sub), sx in zip(stages, stage_xs):
        module(
            ax,
            sx,
            stage_y,
            stage_w,
            stage_h,
            title,
            sub,
            fc=COLORS["orange_light"],
            ec=COLORS["orange"],
            title_size=9.1,
            sub_size=6.6,
            lw=1.35,
            radius=0.12,
        )

    for i in range(len(stage_xs) - 1):
        arrow(
            ax,
            (stage_xs[i] + stage_w, stage_y + stage_h / 2),
            (stage_xs[i + 1], stage_y + stage_h / 2),
            color=flow,
            lw=1.8,
            mutation_scale=12.5,
        )

    # 调度指令
    arrow(ax, (7.10, 6.08), (7.10, 4.76), color=flow, lw=3.0, mutation_scale=14)
    ax.text(
        7.30,
        5.26,
        "调度指令",
        ha="left",
        va="center",
        fontsize=8.2,
        color=flow_light,
    )

    # 4. 恢复控制（嵌入式，不再悬空）
    frame(
        ax,
        12.00,
        3.22,
        1.55,
        1.54,
        "恢复控制",
        ec=COLORS["orange"],
        fc="#FFF8F1",
        title_size=10.4,
    )
    module(
        ax,
        12.18,
        3.93,
        1.18,
        0.33,
        "错误路由",
        "",
        fc=COLORS["orange_light"],
        ec=COLORS["orange"],
        title_size=7.8,
        lw=1.15,
        radius=0.08,
    )
    module(
        ax,
        12.18,
        3.48,
        1.18,
        0.33,
        "恢复动作",
        "",
        fc=COLORS["orange_light"],
        ec=COLORS["orange"],
        title_size=7.8,
        lw=1.15,
        radius=0.08,
    )

    arrow(
        ax,
        (9.95, 3.97),
        (12.00, 3.97),
        color=feedback,
        lw=1.9,
        mutation_scale=12,
    )
    arrow(
        ax,
        (12.76, 4.76),
        (8.95, 6.08),
        color=feedback,
        lw=1.9,
        dashed=True,
        rad=0.12,
        mutation_scale=12,
    )
    ax.text(
        11.58,
        5.28,
        "失败反馈",
        ha="left",
        va="center",
        fontsize=7.7,
        color=COLORS["orange_dark"],
        rotation=17,
    )

    # 5. 底层支撑区：状态 + 资源
    frame(
        ax,
        1.20,
        1.18,
        9.90,
        1.42,
        "共享状态与支撑资源层",
        ec=COLORS["green"],
        fc="#F7FCF8",
        title_size=12.3,
    )

    module(
        ax,
        1.65,
        1.60,
        4.35,
        0.62,
        "共享状态层",
        "黑板事件 · 工件存储 · 缓存复用 · 日志追踪",
        fc=COLORS["green_light"],
        ec=COLORS["green"],
        title_size=9.3,
        sub_size=6.6,
        lw=1.35,
        radius=0.12,
    )
    module(
        ax,
        6.35,
        1.60,
        3.95,
        0.62,
        "外部知识与工具资源",
        "知识图谱 · 算法接口 · 实现片段",
        fc=COLORS["teal_light"],
        ec=COLORS["teal"],
        title_size=9.1,
        sub_size=6.6,
        lw=1.35,
        radius=0.12,
    )

    # 从执行层到支撑层
    arrow(
        ax,
        (5.00, 3.22),
        (4.20, 2.60),
        color=state_color,
        lw=1.8,
        mutation_scale=12,
        label="读写状态",
        label_offset=(-0.10, -0.02),
    )
    arrow(
        ax,
        (6.85, 3.22),
        (8.25, 2.60),
        color=support,
        lw=1.7,
        mutation_scale=12,
        label="调用资源",
        label_offset=(0.10, -0.02),
    )

    # 调度器与状态层的轻连接
    arrow(
        ax,
        (6.10, 6.08),
        (5.10, 2.60),
        color=COLORS["green"],
        lw=1.35,
        dashed=True,
        rad=0.03,
        mutation_scale=11.5,
    )

    # 6. 底部说明条
    rounded_box(
        ax,
        1.75,
        0.42,
        8.70,
        0.42,
        "PlanGraph 以主控调度器协调多智能体执行，并通过共享状态与外部知识资源实现可恢复的图推理流程",
        "",
        fc=COLORS["soft_gray"],
        ec=COLORS["line"],
        lw=1.0,
        radius=0.10,
        title_size=8.7,
        title_weight="normal",
        zorder=1,
    )

    for suffix in ["svg", "pdf", "png"]:
        save_kwargs = {"bbox_inches": "tight", "pad_inches": 0.04}
        if suffix == "png":
            save_kwargs["dpi"] = 240
        fig.savefig(FIG_DIR / f"system_architecture.{suffix}", **save_kwargs)

    plt.close(fig)


if __name__ == "__main__":
    draw()
