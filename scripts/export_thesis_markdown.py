#!/usr/bin/env python3
"""Export thesis writing sources into one Markdown bundle for external review.

The script keeps text-centric files and skips image/binary/build artifacts. It is
intended for feeding another model with the thesis content, so each source file
is wrapped in a Markdown section with a fenced code block.
"""

from __future__ import annotations

import argparse
import datetime as dt
import re
from pathlib import Path


DEFAULT_THESIS_DIR = (
    Path(__file__).resolve().parents[1] / "SEU-master-thesis-template-master"
)

DEFAULT_FILES = [
    "main.tex",
    "chapters/abstract.tex",
    "chapters/chapter1.tex",
    "chapters/chapter2.tex",
    "chapters/chapter3.tex",
    "chapters/chapter4.tex",
    "chapters/chapter5.tex",
    "chapters/chapter6.tex",
    "chapters/appendix.tex",
    "reference.bib",
]


FIGURE_ENV_RE = re.compile(
    r"\\begin\{figure\}(?:\[[^\]]*\])?(.*?)\\end\{figure\}",
    flags=re.DOTALL,
)


def extract_figure_text(match: re.Match[str]) -> str:
    """Keep captions and labels from a figure while removing the image include."""
    body = match.group(1)
    captions = re.findall(r"\\caption\{.*?\}", body, flags=re.DOTALL)
    labels = re.findall(r"\\label\{.*?\}", body)
    kept = "\n".join(captions + labels).strip()
    if not kept:
        return "% [figure omitted: image-only figure]"
    return "% [figure omitted: image content removed]\n" + kept


def clean_for_review(text: str, strip_figures: bool) -> str:
    """Remove noisy generated comments and optionally strip image figure bodies."""
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    if strip_figures:
        text = FIGURE_ENV_RE.sub(extract_figure_text, text)
    return text.strip() + "\n"


def markdown_fence_language(path: Path) -> str:
    if path.suffix == ".bib":
        return "bibtex"
    if path.suffix == ".tex":
        return "latex"
    return "text"


def build_bundle(thesis_dir: Path, files: list[str], strip_figures: bool) -> str:
    now = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    lines = [
        "# 论文正文审阅文本包",
        "",
        f"- 生成时间：{now}",
        f"- 论文目录：`{thesis_dir}`",
        "- 说明：本文件汇总正文写作相关源文件，排除图片、PDF、编译中间文件和个人附属页。",
        "- 用途：可交给其他模型检查行文逻辑、术语一致性、章节衔接、图表引用和学术表达。",
        "",
        "## 文件清单",
        "",
    ]

    existing: list[Path] = []
    for rel in files:
        path = thesis_dir / rel
        if path.exists():
            existing.append(path)
            lines.append(f"- `{rel}`")
        else:
            lines.append(f"- `{rel}`（未找到，已跳过）")

    for path in existing:
        rel = path.relative_to(thesis_dir)
        text = path.read_text(encoding="utf-8")
        text = clean_for_review(text, strip_figures=strip_figures)
        lang = markdown_fence_language(path)
        lines.extend(
            [
                "",
                "---",
                "",
                f"## {rel}",
                "",
                f"```{lang}",
                text.rstrip(),
                "```",
            ]
        )

    lines.append("")
    return "\n".join(lines)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Export thesis writing source files into one Markdown file."
    )
    parser.add_argument(
        "--thesis-dir",
        type=Path,
        default=DEFAULT_THESIS_DIR,
        help=f"Thesis project directory. Default: {DEFAULT_THESIS_DIR}",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_THESIS_DIR / "thesis_text_bundle.md",
        help="Output Markdown path.",
    )
    parser.add_argument(
        "--keep-figure-env",
        action="store_true",
        help="Keep full LaTeX figure environments instead of stripping image bodies.",
    )
    parser.add_argument(
        "--extra-file",
        action="append",
        default=[],
        help="Extra relative file path to include. Can be used multiple times.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    thesis_dir = args.thesis_dir.resolve()
    files = DEFAULT_FILES + args.extra_file
    bundle = build_bundle(
        thesis_dir=thesis_dir,
        files=files,
        strip_figures=not args.keep_figure_env,
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(bundle, encoding="utf-8")
    print(f"Wrote {args.output}")


if __name__ == "__main__":
    main()
