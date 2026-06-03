import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch


plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 8.5,
    "pdf.fonttype": 42,
    "ps.fonttype": 42,
})


COLORS = {
    "limitation": "#F4D8D2",
    "opportunity": "#DDEBD9",
    "challenge": "#D9E4F2",
    "design": "#EFE4C8",
    "edge": "#5C6770",
    "title": "#25313B",
}


columns = [
    (
        "Limitations",
        COLORS["limitation"],
        [
            "Serialized graph inputs\nhide topology and attributes",
            "Program generation can\nmisuse APIs or omit constraints",
            "Multi-agent coordination lacks\na stable recovery state",
        ],
    ),
    (
        "Opportunities",
        COLORS["opportunity"],
        [
            "A pseudocode plan can expose\nalgorithmic intent before coding",
            "The plan can serve as a compact\nquery for graph-algorithm knowledge",
            "Executable checks can transform\nfailures into repairable feedback",
        ],
    ),
    (
        "Challenges",
        COLORS["challenge"],
        [
            "Recover task type, graph attributes,\nconstraints, and output format",
            "Retrieve knowledge that matches\nboth algorithm and API semantics",
            "Diagnose whether failure comes\nfrom code, knowledge, or planning",
        ],
    ),
    (
        "PlanGraph Design",
        COLORS["design"],
        [
            "Task parsing and explicit\npseudocode planning",
            "Planning-guided retrieval and\nconstraint-aware grounding",
            "Executable verification,\nlocal repair, and bounded regeneration",
        ],
    ),
]


def add_box(ax, xy, width, height, text, color, lw=0.8, title=False):
    x, y = xy
    patch = FancyBboxPatch(
        (x, y),
        width,
        height,
        boxstyle="round,pad=0.018,rounding_size=0.025",
        fc=color,
        ec="#53616D",
        lw=lw,
    )
    ax.add_patch(patch)
    ax.text(
        x + width / 2,
        y + height / 2,
        text,
        ha="center",
        va="center",
        color=COLORS["title"],
        fontsize=9.5 if title else 8.2,
        weight="bold" if title else "normal",
        linespacing=1.2,
    )


def add_arrow(ax, start, end):
    ax.add_patch(
        FancyArrowPatch(
            start,
            end,
            arrowstyle="-|>",
            mutation_scale=12,
            lw=0.9,
            color=COLORS["edge"],
            shrinkA=5,
            shrinkB=5,
        )
    )


fig, ax = plt.subplots(figsize=(7.2, 3.7))
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis("off")

left = 0.035
gap = 0.025
col_w = (1 - 2 * left - 3 * gap) / 4
title_h = 0.115
box_h = 0.18
box_gap = 0.045
top_y = 0.81

for ci, (title, color, items) in enumerate(columns):
    x = left + ci * (col_w + gap)
    add_box(ax, (x, top_y), col_w, title_h, title, color, lw=1.0, title=True)
    for ri, item in enumerate(items):
        y = top_y - (ri + 1) * (box_h + box_gap)
        add_box(ax, (x, y), col_w, box_h, item, color)

for ci in range(3):
    x1 = left + ci * (col_w + gap) + col_w
    x2 = left + (ci + 1) * (col_w + gap)
    for ri in range(3):
        y = top_y - (ri + 1) * (box_h + box_gap) + box_h / 2
        add_arrow(ax, (x1, y), (x2, y))

ax.text(
    0.5,
    0.04,
    "Rationale of PlanGraph: from graph-reasoning limitations to planning-guided executable solving",
    ha="center",
    va="center",
    fontsize=8.6,
    color="#35424D",
)

plt.tight_layout(pad=0.3)
fig.savefig("figures/opportunity_rationale.pdf", bbox_inches="tight")
fig.savefig("figures/opportunity_rationale.png", dpi=300, bbox_inches="tight")
