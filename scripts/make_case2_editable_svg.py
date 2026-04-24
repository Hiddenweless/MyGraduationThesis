from __future__ import annotations

import base64
import itertools
from pathlib import Path
from xml.sax.saxutils import escape


ROOT = Path(__file__).resolve().parent
FIG_DIR = ROOT / "figures"
BASE = FIG_DIR / "case2_original_base.png"
THESIS = ROOT.parent / "SEU-master-thesis-template-master"


W, H = 1600, 1114


def tsp_best():
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


def text(x, y, value, size=28, fill="#20283a", anchor="middle", weight="400", family="PingFang SC, Microsoft YaHei, Arial, sans-serif"):
    return (
        f'<text x="{x}" y="{y}" text-anchor="{anchor}" dominant-baseline="middle" '
        f'font-family="{family}" font-size="{size}" font-weight="{weight}" fill="{fill}">{escape(value)}</text>'
    )


def line(x1, y1, x2, y2, stroke="#1f2a44", width=3, opacity=1.0):
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" stroke-width="{width}" stroke-linecap="round" opacity="{opacity}"/>'


def circle(cx, cy, r, fill, stroke="#32629e", width=3):
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{width}"/>'


def rounded_rect(x, y, w, h, r=18, fill="#ffffff", stroke="#dbe5f2", width=2, opacity=1.0):
    return (
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" ry="{r}" '
        f'fill="{fill}" stroke="{stroke}" stroke-width="{width}" opacity="{opacity}"/>'
    )


def graph_svg():
    weights, (best_cost, best_path) = tsp_best()
    pos = {
        "A": (82, 284),
        "B": (225, 88),
        "C": (367, 284),
        "D": (320, 420),
        "E": (130, 420),
    }
    route_edges = {tuple(sorted((best_path[i], best_path[i + 1]))) for i in range(len(best_path) - 1)}
    offsets = {
        ("A", "B"): (-34, -18),
        ("A", "C"): (0, -24),
        ("A", "D"): (-34, 18),
        ("A", "E"): (-34, 8),
        ("B", "C"): (34, -18),
        ("B", "D"): (30, -6),
        ("B", "E"): (-32, -6),
        ("C", "D"): (35, 8),
        ("C", "E"): (30, 18),
        ("D", "E"): (0, 30),
    }
    node_colors = {"A": "#4a90e2", "B": "#ff9f4d", "C": "#69c779", "D": "#4a90e2", "E": "#ff9f4d"}

    out = ['<g id="editable-input-graph">']
    out.append(rounded_rect(36, 34, 544, 472, 18, "#fbfdff", "#dbe5f2", 2))
    for edge, cost in weights.items():
        a, b = edge
        x1, y1 = pos[a]
        x2, y2 = pos[b]
        is_route = edge in route_edges
        out.append(line(x1, y1, x2, y2, "#ee6937" if is_route else "#1f2a44", 6 if is_route else 3, 1.0 if is_route else 0.72))

    for edge, cost in weights.items():
        a, b = edge
        x1, y1 = pos[a]
        x2, y2 = pos[b]
        dx, dy = offsets[edge]
        mx, my = (x1 + x2) / 2 + dx, (y1 + y2) / 2 + dy
        out.append(
            f'<text x="{mx}" y="{my}" text-anchor="middle" dominant-baseline="middle" '
            'font-family="PingFang SC, Microsoft YaHei, Arial, sans-serif" font-size="24" '
            'fill="#20283a" stroke="#fbfdff" stroke-width="6" paint-order="stroke fill">'
            f'{cost}</text>'
        )

    for node, (x, y) in pos.items():
        out.append(circle(x, y, 31, node_colors[node]))
        out.append(text(x, y + 1, node, 34, "#000000", weight="500"))

    out.append(text(408, 93, "任务：", 28, "#20283a", anchor="start", weight="500"))
    out.append(text(408, 145, "求从 A 出发的", 24, "#20283a", anchor="start"))
    out.append(text(408, 195, "最短哈密顿", 24, "#20283a", anchor="start"))
    out.append(text(408, 237, "回路", 24, "#20283a", anchor="start"))

    out.append(rounded_rect(392, 310, 181, 178, 14, "#ffffff", "#dbe5f2", 2))
    out.append(circle(426, 345, 12, "#4a90e2", "#32629e", 2))
    out.append(text(460, 345, "节点", 20, "#20283a", anchor="start"))
    out.append(line(413, 394, 448, 394, "#1f2a44", 4))
    out.append(text(460, 394, "边（权重）", 20, "#20283a", anchor="start"))
    out.append(line(413, 446, 448, 446, "#ee6937", 6))
    out.append(text(460, 446, "最优回路", 20, "#20283a", anchor="start"))
    out.append("</g>")
    return "\n".join(out), best_path, best_cost


def answer_svg(best_path, best_cost):
    return "\n".join(
        [
            '<g id="editable-final-answer">',
            rounded_rect(1208, 734, 338, 280, 24, "#ffffff", "#b8cce5", 3),
            text(1377, 825, "A → B → C", 28, "#20283a"),
            text(1377, 875, "→ D → E → A", 28, "#20283a"),
            text(1377, 964, f"总成本 = {best_cost}", 28, "#20283a"),
            "</g>",
        ]
    )


def make_svg():
    encoded = base64.b64encode(BASE.read_bytes()).decode("ascii")
    graph, best_path, best_cost = graph_svg()
    ans = answer_svg(best_path, best_cost)
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
  <image id="original-generated-background" width="{W}" height="{H}" href="data:image/png;base64,{encoded}"/>
  {graph}
  {ans}
</svg>
'''
    targets = [
        FIG_DIR / "case2_hybrid_editable.svg",
        THESIS / "figures" / "paper" / "case2_editable.svg",
    ]
    for target in targets:
        target.write_text(svg, encoding="utf-8")
        print(f"saved: {target}")
    print("editable groups: editable-input-graph, editable-final-answer")
    print("best route:", " -> ".join(best_path), "cost =", best_cost)


if __name__ == "__main__":
    make_svg()
