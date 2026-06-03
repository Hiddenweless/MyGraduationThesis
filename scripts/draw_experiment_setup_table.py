from __future__ import annotations

import textwrap
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "outputs" / "manual-defense-ppt"
OUT_DIR.mkdir(parents=True, exist_ok=True)
OUT_PATH = OUT_DIR / "experiment_setup_table.png"
OUT_TABLE_ONLY_PATH = OUT_DIR / "experiment_setup_table_only.png"

W, H = 1600, 900
BG = "#ffffff"
BLUE = "#214a99"
BLUE_2 = "#4f73bd"
LIGHT_BLUE = "#eef4ff"
GRID = "#d6e0f2"
TEXT = "#172033"
SUBTEXT = "#4a5b75"
ORANGE = "#c96b2c"
GREEN = "#4f8d58"


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    path = "/System/Library/Fonts/STHeiti Medium.ttc" if bold else "/System/Library/Fonts/STHeiti Light.ttc"
    return ImageFont.truetype(path, size=size)


FONT_TITLE = font(44, True)
FONT_SECTION = font(28, True)
FONT_HEAD = font(19, True)
FONT_CELL = font(17)
FONT_SMALL = font(16)
FONT_TINY = font(15)


def wrap_text(text: str, width: int) -> str:
    return "\n".join(textwrap.wrap(text, width=width, break_long_words=False, replace_whitespace=False))


def wrap_text_px(draw: ImageDraw.ImageDraw, text: str, max_width: int, fnt: ImageFont.FreeTypeFont) -> str:
    """Wrap Chinese/English mixed text by rendered width."""
    lines: list[str] = []
    current = ""
    for ch in text:
        candidate = current + ch
        if draw.textlength(candidate, font=fnt) <= max_width or not current:
            current = candidate
        else:
            lines.append(current)
            current = ch
    if current:
        lines.append(current)
    return "\n".join(lines)


def rounded(draw: ImageDraw.ImageDraw, box, fill, outline=None, width=1, radius=18):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def draw_section(draw: ImageDraw.ImageDraw, box, title: str, accent=BLUE_2):
    x0, y0, x1, y1 = box
    rounded(draw, box, fill="#ffffff", outline=GRID, width=2, radius=20)
    draw.rounded_rectangle((x0, y0, x1, y0 + 54), radius=20, fill=accent)
    draw.rectangle((x0, y0 + 28, x1, y0 + 54), fill=accent)
    draw.text((x0 + 22, y0 + 13), title, font=FONT_SECTION, fill="#ffffff")


def draw_table(draw: ImageDraw.ImageDraw, box, headers, rows, col_widths, row_h):
    x0, y0, x1, _ = box
    y = y0

    # Header row
    draw.rectangle((x0, y, x1, y + row_h), fill=LIGHT_BLUE)
    x = x0
    for i, h in enumerate(headers):
        draw.text((x + 12, y + 13), h, font=FONT_HEAD, fill=BLUE)
        x += col_widths[i]
        if i < len(headers) - 1:
            draw.line((x, y, x, y + row_h), fill=GRID, width=2)
    draw.line((x0, y + row_h, x1, y + row_h), fill=GRID, width=2)
    y += row_h

    for r_i, row in enumerate(rows):
        fill = "#ffffff" if r_i % 2 == 0 else "#f8fbff"
        draw.rectangle((x0, y, x1, y + row_h), fill=fill)
        x = x0
        for c_i, cell in enumerate(row):
            f = FONT_CELL if c_i != 0 else FONT_HEAD
            max_width = col_widths[c_i] - 24
            text = wrap_text_px(draw, str(cell), max_width, f)
            color = BLUE if c_i == 0 else TEXT
            draw.multiline_text((x + 12, y + 10), text, font=f, fill=color, spacing=5)
            x += col_widths[c_i]
            if c_i < len(row) - 1:
                draw.line((x, y, x, y + row_h), fill=GRID, width=1)
        draw.line((x0, y + row_h, x1, y + row_h), fill=GRID, width=1)
        y += row_h


def main():
    img = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img)

    # Top title band matches the thesis defense deck style.
    draw.rectangle((0, 0, W, 94), fill=BLUE)
    draw.rectangle((42, 0, 46, 94), fill="#ffffff")
    draw.text((72, 24), "实验设置", font=FONT_TITLE, fill="#ffffff")

    draw.text(
        (72, 112),
        "覆盖静态图、动态图、自然语言图问题、指令式图问题与组合优化任务；对比通用模型、多智能体方法和程序生成方法。",
        font=FONT_CELL,
        fill=SUBTEXT,
    )

    # Dataset table
    dataset_box = (48, 158, 945, 824)
    draw_section(draw, dataset_box, "数据集", BLUE_2)
    dataset_rows = [
        ("GraphArena", "ICLR'25", "10", "图计算与组合优化综合评测，覆盖路径、连通性、TSP 等任务。"),
        ("NLGraph", "NeurIPS'23", "8", "自然语言图算法问题，考察从文本恢复图结构、目标和约束。"),
        ("GraphWiz", "KDD'24", "9", "指令式图计算任务，关注算法选择和规范输出能力。"),
        ("LLM4DyG", "KDD'24", "9", "动态图时空推理任务，包含时间顺序、动态边和历史状态依赖。"),
        ("GraphInstruct", "arXiv'24", "21", "图理解与图推理指令集，覆盖邻居、最短路、PageRank、最大流等。"),
    ]
    draw_table(
        draw,
        (dataset_box[0] + 18, dataset_box[1] + 72, dataset_box[2] - 18, dataset_box[3] - 18),
        ("数据集", "来源", "任务", "简介"),
        dataset_rows,
        (170, 130, 70, 575),
        100,
    )

    # Metrics table
    metric_box = (988, 158, 1552, 494)
    draw_section(draw, metric_box, "评价指标", GREEN)
    metric_rows = [
        ("EM", "主指标，输出与标准答案完全一致才计为正确。"),
        ("Hit@k / MRR", "分析检索质量，衡量相关知识是否靠前出现。"),
        ("Exec", "分析程序是否能成功执行并返回可验证结果。"),
        ("Repair / Time", "分析反馈修复轮次和端到端求解开销。"),
    ]
    draw_table(
        draw,
        (metric_box[0] + 18, metric_box[1] + 72, metric_box[2] - 18, metric_box[3] - 18),
        ("指标", "说明"),
        metric_rows,
        (170, 356),
        48,
    )

    # Baseline table
    baseline_box = (988, 526, 1552, 854)
    draw_section(draw, baseline_box, "对比基线", ORANGE)
    baseline_rows = [
        ("GPT-4o", "OpenAI", "通用大模型直接推理基线，不引入专门图推理框架。"),
        ("GraphTeam", "arXiv'24", "多智能体图推理方法，依赖历史经验知识。"),
        ("GCoder", "CIKM'25", "程序生成式图推理方法，强化代码求解能力。"),
        ("PlanGraph", "本文", "规划反馈式多智能体方法，结合检索、验证和修复。"),
    ]
    draw_table(
        draw,
        (baseline_box[0] + 18, baseline_box[1] + 72, baseline_box[2] - 18, baseline_box[3] - 18),
        ("方法", "来源", "简介"),
        baseline_rows,
        (160, 100, 266),
        49,
    )

    draw.text(
        (72, 842),
        "注：NetworkX 作为程序执行与图算法工具库使用，不作为独立对比基线。",
        font=FONT_TINY,
        fill=SUBTEXT,
    )

    img.save(OUT_PATH, "PNG")
    print(OUT_PATH)

    table_img = Image.new("RGB", (W, H), BG)
    table_draw = ImageDraw.Draw(table_img)

    dataset_box = (48, 48, 945, 782)
    draw_section(table_draw, dataset_box, "数据集", BLUE_2)
    draw_table(
        table_draw,
        (dataset_box[0] + 18, dataset_box[1] + 72, dataset_box[2] - 18, dataset_box[3] - 18),
        ("数据集", "来源", "任务", "简介"),
        dataset_rows,
        (170, 130, 70, 575),
        112,
    )

    metric_box = (988, 48, 1552, 384)
    draw_section(table_draw, metric_box, "评价指标", GREEN)
    draw_table(
        table_draw,
        (metric_box[0] + 18, metric_box[1] + 72, metric_box[2] - 18, metric_box[3] - 18),
        ("指标", "说明"),
        metric_rows,
        (170, 356),
        48,
    )

    baseline_box = (988, 430, 1552, 782)
    draw_section(table_draw, baseline_box, "对比基线", ORANGE)
    draw_table(
        table_draw,
        (baseline_box[0] + 18, baseline_box[1] + 72, baseline_box[2] - 18, baseline_box[3] - 18),
        ("方法", "来源", "简介"),
        baseline_rows,
        (160, 100, 266),
        52,
    )

    table_img.save(OUT_TABLE_ONLY_PATH, "PNG")
    print(OUT_TABLE_ONLY_PATH)


if __name__ == "__main__":
    main()
