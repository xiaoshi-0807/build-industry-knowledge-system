---
name: build-industry-knowledge-system
description: Build a reusable, evidence-backed industry knowledge system from start to finish. First guide the user through an intake brief when the industry, professional field, role, objective, geography, audience, competitor set, platform focus, or output depth is unclear; then generate the complete system, including an industry database, competitor website deep dives, top social-content analysis, a synthesized knowledge map, and a continuous intelligence system. Use when a user asks to research or understand an industry, build an industry database or knowledge base, analyze competitors or top creator accounts, identify opportunities, create an industry map, create an industry report tailored to a role or business goal, or establish ongoing industry monitoring for any market.
---

# Build Industry Knowledge System

Build a connected decision system, not five isolated reports. Reuse facts, entities, taxonomies, and conclusions across every module.

## Start Here

1. Inspect the user's request and workspace.
2. If the request is vague, run the Guided Intake before research. If the user already supplied enough scope, skip redundant questions and proceed.
3. Determine the target industry, professional field or role, market/geography, target user, business objective, language, output root, competitor set, platform focus, and final deliverable from the request, intake answers, or workspace.
4. Browse current sources for all modern facts, rankings, prices, audience counts, companies, products, regulations, and trends. Prefer primary sources.
5. Scaffold a new project when no suitable structure exists:

```bash
python3 scripts/scaffold_industry_system.py \
  --industry "Home Fitness Equipment" \
  --market "United States" \
  --output "/absolute/path/to/project"
```

6. Read [research-standards.md](references/research-standards.md) before research.
7. Read the relevant module reference before running that module.

## Guided Intake

Use this gate when the user asks for a full industry knowledge system but has not given enough context to tailor the result. The goal is to avoid producing a generic report.

### When To Ask

Ask the guided intake if any of these are unclear and the missing answer could materially change the output:

- Industry, niche, professional field, or job role.
- Market/geography and language.
- Business objective: learning, investment, product, content, sales, career, consulting, strategy, or startup discovery.
- Target reader or decision maker.
- Target customer/user segment.
- Competitors, brands, platforms, or channels to prioritize.
- Depth and output format.
- Constraints such as budget, timeline, regulation, data sources, or excluded topics.

Do not ask an intake question when the answer is already explicit in the user's request or workspace. Do not run multiple clarification rounds unless the user asks for more refinement. After one intake response, create a research brief, make conservative assumptions for remaining gaps, and execute the requested run mode.

### User-Facing Intake Prompt

When needed, send one concise questionnaire like this. Keep it in the user's language.

```text
为了让最终行业报告贴合你的真实用途，请先回答这些问题；不确定的地方可以写“默认”或“你来判断”：

1. 你要研究的行业/细分赛道是什么？
   例：宠物行业、AI 教育、跨境女装、B2B SaaS、口腔医疗、养老服务。

2. 研究市场范围是哪里？
   例：中国、美国、东南亚、全球；是否只看一线城市/下沉市场/某个平台。

3. 你希望报告服务于什么目标？
   例：创业选方向、做产品、做内容账号、找投资机会、做竞品分析、入行学习、销售获客、岗位转型。

4. 你的身份或岗位角色是什么？
   例：创始人、产品经理、运营、投研、咨询顾问、内容博主、销售、学生、求职者。

5. 你最关心的目标用户/客户是谁？
   例：宝妈、新手养宠人、企业采购、医生、大学生、银发人群。

6. 你已有的资源或约束是什么？
   例：已有品牌/产品/账号/供应链/预算/团队/渠道；或者没有资源，从 0 开始。

7. 有哪些必须分析的竞品、品牌、网站、平台或账号？
   例：3-10 个品牌名、官网、抖音/小红书/B站账号；没有就写“你来选”。

8. 你希望重点看哪些维度？
   例：市场规模、产品机会、内容爆款、商业模式、渠道打法、SEO、社群、监管、岗位能力。

9. 报告输出要多深？
   例：快速版、标准版、深度版；是否需要文件夹知识库、单篇总报告、PPT 大纲、持续监控系统。

10. 输出语言、文件保存位置和命名有要求吗？
    例：中文，保存到当前工作区 / 行业名目录。
```

### After The User Answers

Create a short `Research Brief` before executing:

```text
Research Brief
- Industry / niche:
- Market:
- User role:
- Business objective:
- Target customer:
- Priority competitors / platforms:
- Included categories:
- Excluded categories:
- Output depth and artifacts:
- Assumptions:
```

Then proceed directly to the requested output. For a full-system request, execute Modules 1-5 and save the complete project. Do not stop at the brief unless the user explicitly asks for confirmation only.

## Output Language

Default the final generated report and all reader-facing Markdown content to Chinese (`中文`) unless the user explicitly requests another language. This includes:

- The root industry map.
- Landscape and focused records.
- Competitor deep dives.
- Social/content analysis.
- Knowledge map.
- Continuous intelligence templates.
- Final completion summary to the user.

Keep file and folder names in a stable, filesystem-friendly style. English filenames are acceptable when they improve compatibility with scripts, URLs, or existing project conventions, but the report body should remain Chinese by default.

If the user specifies another language in the intake answer, use that language for reader-facing content and record it in the `Research Brief`.

## Choose The Run Mode

- **Full system:** Execute Modules 1-5 in order.
- **Existing database:** Inspect and validate existing files, then start at the requested module. Do not overwrite useful research.
- **Single module:** Execute only that module, but connect its outputs to existing maps and records.
- **Refresh:** Preserve structure, update dated facts, identify changes, and revise conclusions only when evidence changes.
- **Guided full report:** Use the Guided Intake first, convert the answers into a Research Brief, then execute the Full system. This is the default when the user says they want a complete report, full industry cognition system, tailored industry report, or end-to-end research package.

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

- For vague full-system requests, ask the Guided Intake before browsing or scaffolding. For clear full-system requests, proceed without asking and document assumptions.
- After receiving intake answers, do not ask for permission to continue unless the scope is contradictory or impossible. Build the full requested report directly.
- Keep the user's role and objective visible in every module. For example, an investor-oriented report should emphasize market structure, growth, defensibility, and risks; a content-creator report should emphasize audience language, platforms, hooks, and content systems; a product-builder report should emphasize pain points, jobs-to-be-done, product gaps, pricing, and validation.
- Tailor competitor and content sampling to the user's market and channel focus. If the user did not provide competitors or platforms, select representative ones and label the selection rule.
- Write final reports in Chinese by default. Do not switch to English merely because source material, filenames, or competitor websites are English.
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
