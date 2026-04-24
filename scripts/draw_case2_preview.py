from __future__ import annotations

import itertools
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.patches import Circle, FancyArrowPatch, FancyBboxPatch, Rectangle


ROOT = Path(__file__).resolve().parent
OUT_DIR = ROOT / "figures"


def pick_font() -> font_manager.FontProperties:
    candidates = [
        "/System/Library/Fonts/PingFang.ttc",
        "/System/Library/Fonts/Hiragino Sans GB.ttc",
        "/Library/Fonts/Arial Unicode.ttf",
        "/System/Library/Fonts/STHeiti Light.ttc",
        "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc",
    ]
    for path in candidates:
        if Path(path).exists():
            return font_manager.FontProperties(fname=path)
    return font_manager.FontProperties(family="sans-serif")


FONT = pick_font()
MONO = font_manager.FontProperties(family="DejaVu Sans Mono")

COLORS = {
    "blue": "#2f78d4",
    "blue_dark": "#1456a8",
    "green": "#15947f",
    "orange": "#f47c2d",
    "orange_light": "#ffd39d",
    "paper": "#f8fbff",
    "border": "#d8e3f1",
    "ink": "#20283a",
    "muted": "#52637a",
    "line": "#1f2a44",
    "gray": "#edf3f9",
    "route": "#ef6c35",
}


def add_text(ax, x, y, text, size=18, color=None, ha="center", va="center", weight="normal", **kwargs):
    ax.text(
        x,
        y,
        text,
        fontproperties=FONT,
        fontsize=size,
        color=color or COLORS["ink"],
        ha=ha,
        va=va,
        fontweight=weight,
        **kwargs,
    )


def rounded(ax, x, y, w, h, fc="white", ec=None, lw=1.2, r=0.18, alpha=1.0):
    box = FancyBboxPatch(
        (x, y),
        w,
        h,
        boxstyle=f"round,pad=0.02,rounding_size={r}",
        facecolor=fc,
        edgecolor=ec or COLORS["border"],
        linewidth=lw,
        alpha=alpha,
    )
    ax.add_patch(box)
    return box


def header_card(ax, x, y, w, h, title, color, body_lines, icon=None, title_size=18, body_size=16, icon_size=22):
    rounded(ax, x, y, w, h, fc="white", ec=COLORS["border"], lw=1.2, r=0.16)
    ax.add_patch(
        FancyBboxPatch(
            (x, y + h - 0.58),
            w,
            0.58,
            boxstyle="round,pad=0.02,rounding_size=0.16",
            facecolor=color,
            edgecolor=color,
            linewidth=0,
        )
    )
    ax.add_patch(Rectangle((x, y + h - 0.58), w, 0.25, facecolor=color, edgecolor=color, linewidth=0))
    add_text(ax, x + w / 2, y + h - 0.29, title, title_size, "white", weight="bold")
    if icon:
        add_text(ax, x + w / 2, y + h * 0.56, icon, icon_size, color, weight="bold")
    for i, line in enumerate(body_lines):
        add_text(ax, x + w / 2, y + 0.44 + i * 0.34, line, body_size, COLORS["ink"])


def arrow(ax, x1, y1, x2, y2, color="#1f83c5", dashed=False, lw=2.0):
    arr = FancyArrowPatch(
        (x1, y1),
        (x2, y2),
        arrowstyle="-|>",
        mutation_scale=18,
        linewidth=lw,
        color=color,
        linestyle=(0, (4, 4)) if dashed else "solid",
        connectionstyle="arc3,rad=0",
    )
    ax.add_patch(arr)
    return arr


def tsp_best_route():
    nodes = list("ABCDE")
    weights = {
        tuple(sorted(edge)): cost
        for edge, cost in {
            ("A", "B"): 2,
            ("B", "C"): 4,
            ("C", "D"): 3,
            ("D", "E"): 6,
            ("E", "A"): 3,
            ("A", "C"): 8,
            ("A", "D"): 7,
            ("B", "D"): 6,
            ("B", "E"): 9,
            ("C", "E"): 5,
        }.items()
    }
    start = "A"
    best = None
    for perm in itertools.permutations([n for n in nodes if n != start]):
        path = (start, *perm, start)
        cost = sum(weights[tuple(sorted((path[i], path[i + 1])))] for i in range(len(path) - 1))
        if best is None or cost < best[0]:
            best = (cost, path)
    return weights, best


def draw_tsp_graph(ax, ox, oy, scale=1.0):
    weights, (best_cost, best_path) = tsp_best_route()
    pos = {
        "A": (ox + 0.00 * scale, oy + 1.15 * scale),
        "B": (ox + 1.25 * scale, oy + 2.15 * scale),
        "C": (ox + 2.55 * scale, oy + 1.18 * scale),
        "D": (ox + 2.05 * scale, oy - 0.22 * scale),
        "E": (ox + 0.52 * scale, oy - 0.22 * scale),
    }
    route_edges = {tuple(sorted((best_path[i], best_path[i + 1]))) for i in range(len(best_path) - 1)}
    offsets = {
        ("A", "B"): (-0.08, 0.08),
        ("A", "C"): (0.0, 0.16),
        ("A", "D"): (-0.10, -0.02),
        ("A", "E"): (-0.18, -0.04),
        ("B", "C"): (0.10, 0.08),
        ("B", "D"): (0.09, 0.02),
        ("B", "E"): (-0.08, 0.00),
        ("C", "D"): (0.17, -0.02),
        ("C", "E"): (0.08, 0.06),
        ("D", "E"): (0.0, -0.14),
    }

    for edge, cost in weights.items():
        a, b = edge
        x1, y1 = pos[a]
        x2, y2 = pos[b]
        is_route = edge in route_edges
        ax.plot(
            [x1, x2],
            [y1, y2],
            color=COLORS["route"] if is_route else COLORS["line"],
            linewidth=3.0 if is_route else 1.35,
            alpha=0.92 if is_route else 0.50,
            zorder=1,
        )
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2
        dx, dy = offsets[edge]
        rounded(ax, mx + dx - 0.11, my + dy - 0.10, 0.22, 0.20, fc="white", ec="white", lw=0, r=0.03)
        add_text(ax, mx + dx, my + dy, str(cost), 12.5, COLORS["ink"], weight="bold")

    node_colors = {"A": "#4a90e2", "B": "#ff9f4d", "C": "#69c779", "D": "#4a90e2", "E": "#ff9f4d"}
    for node, (x, y) in pos.items():
        ax.add_patch(Circle((x, y), 0.23, facecolor=node_colors[node], edgecolor="#416a9b", linewidth=1.2, zorder=3))
        add_text(ax, x, y, node, 19, "#101828", weight="bold")

    return best_path, best_cost


def draw_generated_code(ax, x, y, w, h):
    header_card(ax, x, y, w, h, "生成的代码", COLORS["blue"], [], None, title_size=17)
    rounded(ax, x + 0.18, y + 0.34, w - 0.36, h - 0.98, fc="#fbfdff", ec=COLORS["border"], lw=1.0, r=0.12)
    code = "tour = traveling_\nsalesman_problem(G,\n    cycle=True)\n\nprint(tour)"
    ax.text(x + 0.34, y + h - 1.00, code, fontproperties=MONO, fontsize=12.6, color="#1f2937", ha="left", va="top", linespacing=1.48)


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    fig, ax = plt.subplots(figsize=(16, 11.1), dpi=160)
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 11.1)
    ax.axis("off")
    fig.patch.set_facecolor("white")

    # Top-left task panel.
    rounded(ax, 0.25, 5.75, 5.55, 5.15, fc="#fbfdff", ec=COLORS["border"], lw=1.4, r=0.18)
    best_path, best_cost = draw_tsp_graph(ax, 0.65, 7.10, 1.18)
    add_text(ax, 3.72, 10.05, "任务：", 18, COLORS["ink"], ha="left", weight="bold")
    add_text(ax, 3.72, 9.50, "求从 A 出发的", 15.2, COLORS["ink"], ha="left")
    add_text(ax, 3.72, 9.06, "最短哈密顿回路", 15.2, COLORS["ink"], ha="left")
    rounded(ax, 3.76, 6.58, 1.72, 1.35, fc="white", ec=COLORS["border"], r=0.12)
    ax.add_patch(Circle((4.03, 7.46), 0.10, facecolor="#4a90e2", edgecolor="#416a9b"))
    add_text(ax, 4.35, 7.46, "节点", 12.8, COLORS["ink"], ha="left")
    ax.plot([3.93, 4.22], [7.02, 7.02], color=COLORS["line"], lw=2.0)
    add_text(ax, 4.35, 7.02, "边（权重）", 12.8, COLORS["ink"], ha="left")
    ax.plot([3.93, 4.22], [6.73, 6.73], color=COLORS["route"], lw=3.0)
    add_text(ax, 4.35, 6.73, "最优回路", 12.8, COLORS["ink"], ha="left")

    # Top-right system pipeline.
    rounded(ax, 6.05, 5.55, 9.65, 5.35, fc="#fbfdff", ec=COLORS["border"], lw=1.4, r=0.18)
    header_card(ax, 6.25, 8.50, 2.45, 2.05, "问题智能体", COLORS["blue"], ["抽取任务与图结构"], "解析", title_size=17, body_size=14.8, icon_size=21)
    header_card(ax, 9.05, 8.50, 3.55, 2.05, "检索模块", COLORS["green"], ["检索到的 API"], "检索", title_size=17, body_size=14.8, icon_size=21)
    header_card(ax, 12.95, 8.50, 2.45, 2.05, "推理模块", COLORS["blue"], ["生成代码", "执行验证", "输出答案"], None, title_size=17, body_size=14.8)

    rounded(ax, 6.25, 5.95, 2.45, 2.10, fc="#fff8ef", ec="#ffd6a8", lw=1.0, r=0.14)
    ax.add_patch(Rectangle((6.25, 7.45), 2.45, 0.60, facecolor=COLORS["orange_light"], edgecolor="none"))
    add_text(ax, 7.48, 7.74, "规划智能体", 17, "#6d3d00", weight="bold")
    add_text(ax, 7.48, 6.83, "生成伪代码规划", 16, COLORS["ink"])
    add_text(ax, 7.48, 7.18, "规划", 20, "#f2a121", weight="bold")

    arrow(ax, 7.48, 8.50, 7.48, 8.10, COLORS["blue"])
    arrow(ax, 8.70, 7.00, 9.05, 7.00, COLORS["green"])
    arrow(ax, 12.60, 7.00, 12.95, 7.00, COLORS["green"], dashed=True)

    for i, api in enumerate(["Graph()", "add_weighted_edges_from()", "traveling_salesman_problem()"]):
        y = 7.82 - i * 0.68
        add_text(ax, 9.35, y, "API", 12, COLORS["green"], ha="left", weight="bold")
        ax.text(9.82, y, api, fontproperties=MONO, fontsize=13.8, color=COLORS["ink"], ha="left", va="center")

    # Downstream execution panel.
    rounded(ax, 0.25, 0.25, 15.45, 4.95, fc="#fbfdff", ec=COLORS["border"], lw=1.4, r=0.18)
    add_text(ax, 8.00, 4.77, "代码执行与验证", 24, COLORS["ink"], weight="bold")

    draw_generated_code(ax, 0.60, 0.78, 3.35, 3.45)
    header_card(ax, 4.35, 0.78, 3.20, 3.45, "在测试图上运行", COLORS["green"], ["通过测试"], "通过", title_size=16.2, body_size=14.2, icon_size=20)
    header_card(ax, 8.05, 0.78, 3.35, 3.45, "在真实图上执行", COLORS["orange"], ["计算回路"], "执行", title_size=16.2, body_size=14.2, icon_size=20)
    header_card(ax, 11.85, 0.78, 3.45, 3.45, "最终答案", COLORS["blue"], [], None, title_size=16.5)
    rounded(ax, 12.18, 1.20, 2.78, 2.15, fc="white", ec="#b9c9dd", lw=1.5, r=0.13)
    route = " → ".join(best_path[:3]) + "\n→ " + " → ".join(best_path[3:])
    add_text(ax, 13.57, 2.65, route, 17, COLORS["ink"])
    add_text(ax, 13.57, 1.75, f"总成本 = {best_cost}", 17, COLORS["ink"], weight="bold")
    add_text(ax, 15.02, 1.30, "通过", 14, "#2bb262", weight="bold")

    arrow(ax, 3.95, 2.50, 4.35, 2.50, COLORS["blue"])
    arrow(ax, 7.55, 2.50, 8.05, 2.50, COLORS["blue"])
    arrow(ax, 11.40, 2.50, 11.85, 2.50, COLORS["blue"])
    arrow(ax, 2.20, 0.78, 5.95, 0.78, "#2886c8", dashed=True, lw=1.4)
    arrow(ax, 5.95, 0.78, 5.95, 0.95, "#2886c8", dashed=True, lw=1.4)
    arrow(ax, 5.95, 0.78, 9.72, 0.78, COLORS["orange"], dashed=True, lw=1.4)
    arrow(ax, 9.72, 0.78, 9.72, 0.95, COLORS["orange"], dashed=True, lw=1.4)
    arrow(ax, 9.72, 0.78, 13.60, 0.78, COLORS["route"], dashed=True, lw=1.4)
    arrow(ax, 13.60, 0.78, 13.60, 1.00, COLORS["route"], dashed=True, lw=1.4)

    fig.savefig(OUT_DIR / "case2_redraw_preview.pdf", bbox_inches="tight")
    fig.savefig(OUT_DIR / "case2_redraw_preview.png", bbox_inches="tight", dpi=180)
    plt.close(fig)
    print(f"saved: {OUT_DIR / 'case2_redraw_preview.pdf'}")
    print(f"saved: {OUT_DIR / 'case2_redraw_preview.png'}")
    print("best route:", " -> ".join(best_path), "cost =", best_cost)


if __name__ == "__main__":
    main()
