#!/usr/bin/env python3
"""Create a reusable industry knowledge-system project skeleton."""

from __future__ import annotations

import argparse
import datetime as dt
import re
from pathlib import Path

DIMENSIONS = {
    "Brands": "Brand Landscape",
    "Products": "Product Taxonomy",
    "Pain-Points": "Consumer Pain-Point Map",
    "Keywords": "Search-Intent Map",
    "Communities": "Community Landscape",
    "Competitors": "Competitive Set",
    "Business-Models": "Business-Model Landscape",
    "Opportunities": "Opportunity Map",
}


def slug(text: str) -> str:
    value = re.sub(r"[^a-zA-Z0-9]+", "-", text).strip("-").lower()
    return value or "industry"


def frontmatter(title: str, record_type: str, industry: str, market: str) -> str:
    today = dt.date.today().isoformat()
    return (
        "---\n"
        f"title: {title}\n"
        f"type: {record_type}\n"
        f"industry: {industry}\n"
        f"market: {market}\n"
        f"updated: {today}\n"
        "status: draft\n"
        "---\n\n"
    )


def write_if_missing(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists():
        path.write_text(content, encoding="utf-8")


def landscape(title: str, industry: str, market: str, dimension: str) -> str:
    return (
        frontmatter(title, f"{slug(dimension)}-landscape", industry, market)
        + f"# {title}\n\n"
        "## Executive Takeaway\n\n"
        "> Synthesize the most decision-relevant conclusion.\n\n"
        "## Landscape\n\n"
        "| Segment | Representative nodes | Demand/job | Advantage | Weakness | Source |\n"
        "|---|---|---|---|---|---|\n"
        "| - | - | - | - | - | - |\n\n"
        "## Focus Records\n\n"
        "- [ ] Create and link focused records.\n\n"
        "## Sources And Limitations\n\n"
        "- Source:\n"
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--industry", required=True)
    parser.add_argument("--market", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    root = args.output.expanduser().resolve()
    root.mkdir(parents=True, exist_ok=True)

    root_name = f"00-{slug(args.market)}-{slug(args.industry)}.md"
    links = "\n".join(f"- [[{directory}/{title}]]" for directory, title in DIMENSIONS.items())
    write_if_missing(
        root / root_name,
        frontmatter(f"{args.market} {args.industry}", "industry-map", args.industry, args.market)
        + f"# {args.market} {args.industry}\n\n"
        "## Boundary\n\n- Included:\n- Excluded:\n\n"
        f"## Industry Map\n\n{links}\n\n"
        "## Core Dynamics\n\n1. \n\n"
        "## Research Rules\n\n- Separate facts, inferences, and recommendations.\n\n"
        "## Primary Sources\n\n- \n",
    )
    for directory, title in DIMENSIONS.items():
        write_if_missing(root / directory / f"{title}.md", landscape(title, args.industry, args.market, directory))

    write_if_missing(
        root / "knowledge-map.md",
        frontmatter(f"{args.industry} Knowledge Map", "industry-knowledge-map", args.industry, args.market)
        + f"# {args.industry} Knowledge Map\n\n"
        "## Coverage And Legend\n\n## Three-Level Map\n\n## Node Relationships\n\n"
        "## Prioritized Opportunities\n\n## Metrics To Track\n",
    )
    write_if_missing(
        root / "Content-Analysis" / "platform-top-accounts-analysis.md",
        frontmatter("Platform Top Accounts Analysis", "content-analysis", args.industry, args.market)
        + "# Platform Top Accounts Analysis\n\n"
        "## Scope And Method\n\n## Account Ranking\n\n## Content Performance\n\n"
        "## Breakout Patterns\n\n## Actionable Content Strategy\n\n## Sources And Limitations\n",
    )
    intelligence = root / "intelligence-system"
    for directory in (
        intelligence / "config",
        intelligence / "scripts",
        intelligence / "data" / "competitor-snapshots",
        intelligence / "data" / "content-snapshots",
        intelligence / "content-database" / "trending",
    ):
        directory.mkdir(parents=True, exist_ok=True)
    templates = {
        "sources.md": "# Information Source Subscriptions\n\n## Long-Form / Video\n\n## Expert Social Accounts\n\n## Newsletters\n\n## Communities\n\n## Primary Regulatory And Data Sources\n",
        "weekly-competitor-update.md": "# Weekly Competitor Update\n\n## Executive Takeaway\n\n## New Products\n\n## New Categories\n\n## New Content\n\n## Claim And Keyword Changes\n\n## Recommended Actions\n",
        "trending-log.md": "# Content Trending Log\n\n## Fastest Like Growth\n\n## Fastest Share Growth\n\n## Fastest View Growth\n\n## Emerging Narratives\n\n## Actions\n",
        "weekly-report.md": "# Industry Weekly Report\n\n## Executive Summary\n\n## What Changed\n\n## Breakout Products And Content\n\n## Company Moves\n\n## Best Opportunity\n\n## Next-Week Decisions\n",
    }
    for name, content in templates.items():
        write_if_missing(intelligence / name, content)
    print(f"Created industry knowledge-system skeleton at {root}")


if __name__ == "__main__":
    main()

