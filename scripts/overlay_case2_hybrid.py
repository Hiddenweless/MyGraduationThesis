from __future__ import annotations

import itertools
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parent
THESIS = ROOT.parent / "SEU-master-thesis-template-master"
BASE = THESIS / "figures" / "paper" / "case2.pdf.png"
OUT_DIR = ROOT / "figures"


COLORS = {
    "ink": (24, 31, 48, 255),
    "muted": (70, 82, 100, 255),
    "border": (219, 229, 242, 255),
    "route": (238, 105, 55, 255),
    "line": (34, 42, 65, 170),
    "white": (255, 255, 255, 255),
    "panel": (250, 252, 255, 255),
    "blue": (75, 144, 226, 255),
    "green": (105, 199, 121, 255),
    "orange": (255, 159, 77, 255),
}


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    candidates = [
        "/System/Library/Fonts/PingFang.ttc",
        "/System/Library/Fonts/Hiragino Sans GB.ttc",
        "/System/Library/Fonts/STHeiti Light.ttc",
        "/Library/Fonts/Arial Unicode.ttf",
    ]
    for path in candidates:
        if Path(path).exists():
            return ImageFont.truetype(path, size=size, index=0)
    return ImageFont.load_default()


F16 = font(16)
F20 = font(20)
F24 = font(24)
F28 = font(28)
F34 = font(34)
F40 = font(40)


def centered(draw: ImageDraw.ImageDraw, xy, text: str, fnt, fill=COLORS["ink"]):
    x, y = xy
    bbox = draw.textbbox((0, 0), text, font=fnt)
    draw.text((x - (bbox[2] - bbox[0]) / 2, y - (bbox[3] - bbox[1]) / 2), text, font=fnt, fill=fill)


def best_tsp():
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


def draw_graph(draw: ImageDraw.ImageDraw):
    weights, (best_cost, best_path) = best_tsp()
    # Redraw the inner area of the original task panel while keeping its outer shape.
    draw.rounded_rectangle((36, 34, 580, 506), radius=18, fill=COLORS["panel"], outline=COLORS["border"], width=2)

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
    for edge, cost in weights.items():
        a, b = edge
        p1, p2 = pos[a], pos[b]
        is_route = edge in route_edges
        draw.line((p1, p2), fill=COLORS["route"] if is_route else COLORS["line"], width=6 if is_route else 3)
        mx, my = (p1[0] + p2[0]) // 2, (p1[1] + p2[1]) // 2
        dx, dy = offsets[edge]
        tx, ty = mx + dx, my + dy
        bbox = draw.textbbox((0, 0), str(cost), font=F24)
        draw.text(
            (tx - (bbox[2] - bbox[0]) / 2, ty - (bbox[3] - bbox[1]) / 2),
            str(cost),
            font=F24,
            fill=COLORS["ink"],
            stroke_width=3,
            stroke_fill=COLORS["panel"],
        )

    node_colors = {"A": COLORS["blue"], "B": COLORS["orange"], "C": COLORS["green"], "D": COLORS["blue"], "E": COLORS["orange"]}
    for node, (x, y) in pos.items():
        r = 31
        draw.ellipse((x - r, y - r, x + r, y + r), fill=node_colors[node], outline=(50, 98, 158, 255), width=3)
        centered(draw, (x, y + 1), node, F34, (0, 0, 0, 255))

    draw.text((408, 78), "任务：", font=F28, fill=COLORS["ink"])
    draw.text((408, 130), "求从 A 出发的", font=F24, fill=COLORS["ink"])
    draw.text((408, 180), "最短哈密顿", font=F24, fill=COLORS["ink"])
    draw.text((408, 222), "回路", font=F24, fill=COLORS["ink"])

    draw.rounded_rectangle((392, 310, 573, 488), radius=14, fill=COLORS["white"], outline=COLORS["border"], width=2)
    draw.ellipse((414, 333, 438, 357), fill=COLORS["blue"], outline=(50, 98, 158, 255), width=2)
    draw.text((460, 326), "节点", font=F20, fill=COLORS["ink"])
    draw.line((413, 394, 448, 394), fill=COLORS["line"], width=4)
    draw.text((460, 380), "边（权重）", font=F20, fill=COLORS["ink"])
    draw.line((413, 446, 448, 446), fill=COLORS["route"], width=6)
    draw.text((460, 431), "最优回路", font=F20, fill=COLORS["ink"])
    return best_path, best_cost


def draw_answer(draw: ImageDraw.ImageDraw, best_path, best_cost):
    # Overwrite only the inner result card, preserving the generated outer card.
    draw.rounded_rectangle((1208, 734, 1546, 1014), radius=24, fill=COLORS["white"], outline=(184, 204, 229, 255), width=3)
    route1 = "A → B → C"
    route2 = "→ D → E → A"
    centered(draw, (1377, 825), route1, F28)
    centered(draw, (1377, 875), route2, F28)
    centered(draw, (1377, 964), f"总成本 = {best_cost}", F28)


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    img = Image.open(BASE).convert("RGBA")
    draw = ImageDraw.Draw(img)
    best_path, best_cost = draw_graph(draw)
    draw_answer(draw, best_path, best_cost)
    png = OUT_DIR / "case2_hybrid_preview.png"
    pdf = OUT_DIR / "case2_hybrid_preview.pdf"
    img.save(png)
    img.convert("RGB").save(pdf, "PDF", resolution=300.0)
    print(f"saved: {png}")
    print(f"saved: {pdf}")
    print("best route:", " -> ".join(best_path), "cost =", best_cost)


if __name__ == "__main__":
    main()
