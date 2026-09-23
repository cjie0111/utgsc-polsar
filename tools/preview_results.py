"""Display a released CSV as Markdown. No model or training dependencies."""

import argparse
import csv
from pathlib import Path


def markdown_cell(value):
    return value.replace("|", "\\|").replace("\r", " ").replace("\n", " ")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "csv_file", nargs="?", type=Path,
        default=Path(__file__).resolve().parents[1] / "results" / "main_table_summary.csv",
    )
    args = parser.parse_args()
    with args.csv_file.open(newline="", encoding="utf-8-sig") as stream:
        rows = csv.reader(stream)
        header = next(rows)
        print("| " + " | ".join(map(markdown_cell, header)) + " |")
        print("| " + " | ".join("---" for _ in header) + " |")
        for row in rows:
            print("| " + " | ".join(map(markdown_cell, row)) + " |")


if __name__ == "__main__":
    main()
