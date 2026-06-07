#!/usr/bin/env python3
"""Audit whether an industry knowledge-system project has core artifacts."""

from __future__ import annotations

import argparse
from pathlib import Path

REQUIRED_DIRS = [
    "Brands",
    "Products",
    "Pain-Points",
    "Keywords",
    "Communities",
    "Competitors",
    "Business-Models",
    "Opportunities",
    "Content-Analysis",
    "intelligence-system",
]
REQUIRED_INTELLIGENCE = [
    "sources.md",
    "weekly-competitor-update.md",
    "trending-log.md",
    "weekly-report.md",
]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("project", type=Path)
    args = parser.parse_args()
    root = args.project.expanduser().resolve()
    problems: list[str] = []
    root_maps = list(root.glob("00-*.md"))
    if not root_maps:
        problems.append("Missing root industry map: 00-*.md")
    if not (root / "knowledge-map.md").exists():
        problems.append("Missing knowledge-map.md")
    for directory in REQUIRED_DIRS:
        path = root / directory
        if not path.is_dir():
            problems.append(f"Missing directory: {directory}")
        elif not list(path.rglob("*.md")) and directory != "intelligence-system":
            problems.append(f"No Markdown records in: {directory}")
    for name in REQUIRED_INTELLIGENCE:
        if not (root / "intelligence-system" / name).exists():
            problems.append(f"Missing intelligence output: {name}")
    if problems:
        print("AUDIT: INCOMPLETE")
        for problem in problems:
            print(f"- {problem}")
        raise SystemExit(1)
    print("AUDIT: CORE STRUCTURE COMPLETE")


if __name__ == "__main__":
    main()

