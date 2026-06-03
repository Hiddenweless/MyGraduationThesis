from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager


OUT = Path(__file__).with_name("表5-3_不同检索查询方式知识命中效果折线图.png")

font_candidates = [
    "/System/Library/Fonts/PingFang.ttc",
    "/System/Library/Fonts/STHeiti Light.ttc",
    "/Library/Fonts/Arial Unicode.ttf",
    "/System/Library/Fonts/Supplemental/Songti.ttc",
]
for font_path in font_candidates:
    if Path(font_path).exists():
        font_manager.fontManager.addfont(font_path)
        plt.rcParams["font.family"] = font_manager.FontProperties(fname=font_path).get_name()
        break

plt.rcParams["axes.unicode_minus"] = False

queries = [
    "Q1\n原始问题文本",
    "Q2\n任务类型+关键词",
    "Q3\n规划步骤查询",
    "Q4\n规划步骤+约束标签",
]

metrics = {
    "Hit@1": [42.6, 68.9, 76.4, 82.1],
    "Hit@3": [61.8, 84.7, 90.8, 94.2],
    "Hit@5": [72.9, 92.1, 96.3, 98.0],
    "MRR": [51.4, 76.3, 83.5, 88.4],
}

colors = {
    "Hit@1": "#02409A",
    "Hit@3": "#5B8FF9",
    "Hit@5": "#70AD47",
    "MRR": "#ED7D31",
}
markers = {"Hit@1": "o", "Hit@3": "s", "Hit@5": "^", "MRR": "D"}

x = np.arange(len(queries))
fig, ax = plt.subplots(figsize=(11.8, 6.6), dpi=220)
fig.patch.set_facecolor("white")
ax.set_facecolor("#F8FAFD")

for name, values in metrics.items():
    ax.plot(
        x,
        values,
        label=name,
        color=colors[name],
        marker=markers[name],
        linewidth=2.6,
        markersize=7,
    )
    for xi, yi in zip(x, values):
        ax.text(
            xi,
            yi + 1.2,
            f"{yi:.1f}%",
            ha="center",
            va="bottom",
            fontsize=9.5,
            color=colors[name],
        )

ax.set_ylabel("指标值（%）", fontsize=13)
ax.set_xticks(x)
ax.set_xticklabels(queries, fontsize=12)
ax.set_ylim(35, 104)
ax.set_yticks(np.arange(40, 105, 10))
ax.grid(axis="y", linestyle="--", linewidth=0.8, alpha=0.35)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_color("#9AA9BD")
ax.spines["bottom"].set_color("#9AA9BD")
ax.legend(loc="lower right", ncol=2, frameon=True, framealpha=0.95, edgecolor="#D9E2EF", fontsize=11)

plt.tight_layout(pad=1.2)
fig.savefig(OUT, bbox_inches="tight")
print(OUT)
