#!/usr/bin/env python3
from pathlib import Path
import csv
import re


ROOT = Path(__file__).resolve().parents[1]
EVALUATION_DIR = ROOT / "evaluation"
RESULTS_DIR = ROOT / "src" / "results"
EVALUATION_CSV = EVALUATION_DIR / "evaluation.csv"
OUTPUT_CSV = EVALUATION_DIR / "aggregate.csv"
CONDITIONS = ("Baseline", "Simple DAG", "Perfect Info")


def aggregate_tokens() -> dict[str, dict[str, int]]:
    totals: dict[str, dict[str, int]] = {}

    for path in sorted(RESULTS_DIR.glob("task*.md")):
        in_table = False
        for line in path.read_text().splitlines():
            if line.startswith("| Condition | Input Tokens | Output Tokens | Total |"):
                in_table = True
                continue
            if not in_table:
                continue
            if not line.startswith("|"):
                break
            if re.match(r"\|\s*:?-+", line):
                continue

            cells = [cell.strip() for cell in line.strip("|").split("|")]
            if len(cells) != 4:
                continue

            condition, input_tokens, output_tokens, total_tokens = cells
            row = totals.setdefault(condition, {"tasks": 0, "input_tokens": 0, "output_tokens": 0, "total_tokens": 0})
            row["tasks"] += 1
            row["input_tokens"] += int(input_tokens)
            row["output_tokens"] += int(output_tokens)
            row["total_tokens"] += int(total_tokens)

    return totals


def aggregate_correctness() -> dict[str, dict[str, int]]:
    totals = {condition: {"correct": 0, "total": 0} for condition in CONDITIONS}

    with EVALUATION_CSV.open(newline="") as file:
        for row in csv.DictReader(file):
            condition = row["condition"]
            if condition not in totals:
                continue
            totals[condition]["correct"] += int(row["correct"])
            totals[condition]["total"] += 1

    return totals


def build_rows() -> list[dict[str, int | float | str]]:
    token_totals = aggregate_tokens()
    correctness_totals = aggregate_correctness()
    rows = []

    for condition in CONDITIONS:
        tokens = token_totals[condition]
        correctness = correctness_totals[condition]
        total_tasks = correctness["total"]
        correct = correctness["correct"]
        total_tokens = tokens["total_tokens"]

        rows.append(
            {
                "condition": condition,
                "tasks": total_tasks,
                "correct": correct,
                "pass_rate_percent": round(correct / total_tasks * 100, 2),
                "input_tokens": tokens["input_tokens"],
                "output_tokens": tokens["output_tokens"],
                "total_tokens": total_tokens,
                "tokens_per_task": round(total_tokens / total_tasks, 2),
                "tokens_per_correct": round(total_tokens / correct, 2) if correct else "",
            }
        )

    return rows


def write_csv(rows: list[dict[str, int | float | str]]) -> None:
    fieldnames = [
        "condition",
        "tasks",
        "correct",
        "pass_rate_percent",
        "input_tokens",
        "output_tokens",
        "total_tokens",
        "tokens_per_task",
        "tokens_per_correct",
    ]
    with OUTPUT_CSV.open("w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    rows = build_rows()
    write_csv(rows)
    print(f"Wrote {OUTPUT_CSV.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
