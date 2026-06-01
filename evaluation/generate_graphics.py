#!/usr/bin/env python3
from pathlib import Path
import csv
import math


ROOT = Path(__file__).resolve().parents[1]
EVALUATION_DIR = ROOT / "evaluation"
INPUT_CSV = EVALUATION_DIR / "aggregate.csv"
OUTPUT_DIR = EVALUATION_DIR / "grafics"
OUTPUT_FILE = OUTPUT_DIR / "accuracy_vs_tokens_consumption.svg"
COLORS = {
    "Baseline": "#f87171",
    "Simple DAG": "#60a5fa",
    "Perfect Info": "#4ade80",
}


def read_rows() -> list[dict[str, float | str]]:
    with INPUT_CSV.open(newline="") as file:
        return [
            {
                "condition": row["condition"],
                "pass_rate_percent": float(row["pass_rate_percent"]),
                "tokens_per_task": float(row["tokens_per_task"]),
            }
            for row in csv.DictReader(file)
        ]


def esc(value: object) -> str:
    return str(value).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def fmt(value: float) -> str:
    if value >= 1000:
        return f"{value:,.0f}"
    return f"{value:.0f}"


def log_scale(domain_min: float, domain_max: float, range_min: float, range_max: float):
    log_min = math.log10(domain_min)
    log_max = math.log10(domain_max)

    def scale(value: float) -> float:
        return range_min + (math.log10(value) - log_min) / (log_max - log_min) * (range_max - range_min)

    return scale


def linear_scale(domain_min: float, domain_max: float, range_min: float, range_max: float):
    def scale(value: float) -> float:
        return range_min + (value - domain_min) / (domain_max - domain_min) * (range_max - range_min)

    return scale


def log_ticks(min_value: float, max_value: float) -> list[float]:
    ticks = []
    base = 10 ** math.floor(math.log10(min_value))
    while base <= max_value * 1.02:
        for factor in (1, 2, 5):
            value = base * factor
            if min_value <= value <= max_value * 1.02:
                ticks.append(value)
        base *= 10
    return ticks


def render_chart(rows: list[dict[str, float | str]]) -> str:
    width, height = 1100, 760
    x0, y0, plot_w, plot_h = 150, 80, 700, 485

    x_values = [float(row["tokens_per_task"]) for row in rows]
    x_min = min(x_values) * 0.72
    x_max = max(x_values) * 1.28
    x_scale = log_scale(x_min, x_max, x0, x0 + plot_w)
    y_scale = linear_scale(0, 100, y0 + plot_h, y0)

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        '<rect width="100%" height="100%" fill="#000000"/>',
        "<style>",
        'text { font-family: "SF Pro Display", -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; fill: #f9fafb; }',
        ".axis { stroke: #f9fafb; stroke-width: 1.6; }",
        ".grid { stroke: #27272a; stroke-width: 1; }",
        ".tick { stroke: #f9fafb; stroke-width: 1; }",
        ".label { font-size: 26px; fill: #f3f4f6; }",
        ".small { font-size: 24px; fill: #d1d5db; }",
        ".axislabel { font-size: 28px; fill: #f3f4f6; }",
        ".ticklabel { font-size: 22px; fill: #d1d5db; }",
        ".legend { font-size: 24px; fill: #f9fafb; }",
        "</style>",
    ]

    for tick in log_ticks(x_min, x_max):
        tx = x_scale(tick)
        parts += [
            f'<line x1="{tx:.2f}" y1="{y0}" x2="{tx:.2f}" y2="{y0 + plot_h}" class="grid"/>',
            f'<line x1="{tx:.2f}" y1="{y0 + plot_h}" x2="{tx:.2f}" y2="{y0 + plot_h + 6}" class="tick"/>',
            f'<text x="{tx:.2f}" y="{y0 + plot_h + 34}" text-anchor="middle" class="ticklabel">{fmt(tick)}</text>',
        ]

    for tick in [0, 20, 40, 60, 80, 100]:
        ty = y_scale(tick)
        parts += [
            f'<line x1="{x0}" y1="{ty:.2f}" x2="{x0 + plot_w}" y2="{ty:.2f}" class="grid"/>',
            f'<line x1="{x0 - 6}" y1="{ty:.2f}" x2="{x0}" y2="{ty:.2f}" class="tick"/>',
            f'<text x="{x0 - 18}" y="{ty + 8:.2f}" text-anchor="end" class="ticklabel">{tick}</text>',
        ]

    parts += [
        f'<line x1="{x0}" y1="{y0 + plot_h}" x2="{x0 + plot_w}" y2="{y0 + plot_h}" class="axis"/>',
        f'<line x1="{x0}" y1="{y0}" x2="{x0}" y2="{y0 + plot_h}" class="axis"/>',
        f'<text x="{x0 + plot_w / 2}" y="{y0 + plot_h + 78}" text-anchor="middle" class="axislabel">Total tokens per request (log scale)</text>',
        f'<text x="{x0 - 104}" y="{y0 + plot_h / 2}" text-anchor="middle" class="axislabel" transform="rotate(-90 {x0 - 104} {y0 + plot_h / 2})">Pass rate (%)</text>',
    ]

    for row in rows:
        condition = str(row["condition"])
        cx = x_scale(float(row["tokens_per_task"]))
        cy = y_scale(float(row["pass_rate_percent"]))
        color = COLORS[condition]
        if condition == "Simple DAG":
            text_x = cx - 26
            anchor = "end"
        else:
            text_x = cx + 26
            anchor = "start"
        parts += [
            f'<circle cx="{cx:.2f}" cy="{cy:.2f}" r="14" fill="{color}" stroke="#ffffff" stroke-width="2"/>',
            f'<text x="{text_x:.2f}" y="{cy - 22:.2f}" text-anchor="{anchor}" class="label">{esc(condition)}</text>',
            f'<text x="{text_x:.2f}" y="{cy + 8:.2f}" text-anchor="{anchor}" class="small">{fmt(float(row["pass_rate_percent"]))}% pass</text>',
            f'<text x="{text_x:.2f}" y="{cy + 38:.2f}" text-anchor="{anchor}" class="small">{fmt(float(row["tokens_per_task"]))} tokens/request</text>',
        ]

    parts.append("</svg>")
    return "\n".join(parts) + "\n"


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(render_chart(read_rows()))
    print(f"Wrote {OUTPUT_FILE.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
