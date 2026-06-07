---
name: build-industry-knowledge-system
description: Build a reusable, evidence-backed industry knowledge system from start to finish, including an industry database, competitor website deep dives, top social-content analysis, a synthesized knowledge map, and a continuous intelligence system. Use when a user asks to research or understand an industry, build an industry database or knowledge base, analyze competitors or top creator accounts, identify opportunities, create an industry map, or establish ongoing industry monitoring for any market.
---

# Build Industry Knowledge System

Build a connected decision system, not five isolated reports. Reuse facts, entities, taxonomies, and conclusions across every module.

## Start Here

1. Determine the target industry, market/geography, target user, business objective, language, and output root from the request or workspace.
2. Inspect the workspace before asking questions. If important scope remains ambiguous, state a conservative assumption and proceed unless it risks researching the wrong industry.
3. Browse current sources for all modern facts, rankings, prices, audience counts, companies, products, regulations, and trends. Prefer primary sources.
4. Scaffold a new project when no suitable structure exists:

```bash
python3 scripts/scaffold_industry_system.py \
  --industry "Home Fitness Equipment" \
  --market "United States" \
  --output "/absolute/path/to/project"
```

5. Read [research-standards.md](references/research-standards.md) before research.
6. Read the relevant module reference before running that module.

## Choose The Run Mode

- **Full system:** Execute Modules 1-5 in order.
- **Existing database:** Inspect and validate existing files, then start at the requested module. Do not overwrite useful research.
- **Single module:** Execute only that module, but connect its outputs to existing maps and records.
- **Refresh:** Preserve structure, update dated facts, identify changes, and revise conclusions only when evidence changes.

## The Five Modules

### Module 1: Build The Industry Database

Read [module-1-database.md](references/module-1-database.md).

Create the industry root map and eight connected research dimensions:

`Brands`, `Products`, `Pain-Points`, `Keywords`, `Communities`, `Competitors`, `Business-Models`, `Opportunities`.

Required result:

- One root industry map with boundary, dynamics, research rules, and primary sources.
- One landscape/MOC per dimension.
- Focused records for the highest-value nodes.
- Explicit links between demand, products, competitors, channels, and opportunities.

### Module 2: Deep-Dive A Competitor Website

Read [module-2-competitor.md](references/module-2-competitor.md).

Analyze the site as a commercial system: navigation, collections/categories, products, offers, conversion path, trust, content/SEO, social distribution, business model, and exploitable gaps. Label all inferred traffic or strategy conclusions as inference.

### Module 3: Analyze Top Social Accounts And Content

Read [module-3-content.md](references/module-3-content.md).

Define the ranking universe before producing a Top N. Capture account-level and content-level metrics, classify content jobs, identify breakout structures, and convert findings into an actionable content strategy. Do not infer sales from engagement.

### Module 4: Synthesize The Knowledge Map

Read [module-4-knowledge-map.md](references/module-4-knowledge-map.md).

Generate a three-level industry map from the database. Show node relationships, competition intensity, growth signals, content/research gaps, opportunity priorities, and metrics to keep tracking. If the database is incomplete, say so and distinguish database-backed conclusions from new public research.

### Module 5: Build Continuous Intelligence

Read [module-5-intelligence.md](references/module-5-intelligence.md).

Create a sustainable operating system containing:

- Curated source subscriptions.
- Weekly competitor change monitoring.
- Daily content trend tracking.
- A weekly report that converts signals into decisions.

Where useful, create runnable scripts and configuration rather than only describing automation.

## Execution Rules

- Keep a task plan for full-system runs and complete each module end to end before moving on.
- Save findings continuously; do not wait until the end to write files.
- Use Markdown with stable frontmatter and internal links where the project is a knowledge base.
- Use the exact source URL near each consequential fact or in a clear sources section.
- Record the observation date for volatile metrics.
- Separate:
  - **Observed fact:** directly supported by a source.
  - **Inference:** reasoned interpretation from facts.
  - **Recommendation:** proposed action.
- Treat anecdotal community content as demand-language evidence, not efficacy proof.
- Include regulatory, safety, ethical, or platform-policy boundaries relevant to the industry.
- Prefer narrow, defensible opportunity theses over generic trend summaries.

## Completion Gate

Before finishing a full-system run, verify:

- The root map links to all eight dimensions.
- Landscape records link to focused records.
- Competitor and content analysis update or reference the database.
- The knowledge map includes relationships and prioritized opportunities, not only a tree.
- The intelligence system has templates, inputs, cadence, owners/decision use, and archive paths.
- Current facts include dates and sources.
- Limitations and missing data are explicit.

Run the bundled audit:

```bash
python3 scripts/audit_industry_system.py /absolute/path/to/project
```

Use [output-contract.md](references/output-contract.md) for the full required file structure.
Use [task-prompts.md](references/task-prompts.md) when the user wants reusable prompts or to delegate the five modules separately.

