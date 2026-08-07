# Agentic AI Leadership Program

A self-directed, 12-week program that reconstructs the learning outcomes of an
executive agentic-AI course — strategy, workflow redesign, prototype build,
governance, and rollout — applied to one real workflow inside Wesco/Anixter.

This is **original material**. It covers the same competencies as commercial
programs (an Audit → Gauge → Engineer → Navigate → Track strategy cycle plus a
build studio) but is written from public research, official technical
documentation, and your real organizational context. No proprietary course
content is reproduced.

## The three capabilities this develops

1. **AI strategist** — identifying where AI produces genuine organizational value.
2. **Agent designer** — converting human workflows into reliable human-agent systems.
3. **AI implementation leader** — governing, evaluating, demonstrating, and scaling them.

## Structure

| Part | Weeks | Outcome | Folder |
|---|---|---|---|
| Foundations | 1–2 | Understand LLMs, agents, tools, workflows, data, autonomy, and risk | `part-1-foundations/` |
| A.G.E.N.T. Strategy | 3–5 | Select and completely redesign one valuable workflow | `part-2-agent-strategy/` |
| B.U.I.L.D. Studio | 6–10 | Architect, build, test, and document a working prototype | `part-3-build-studio/` |
| Enterprise Adoption | 11–12 | Business case, governance package, demo, and rollout roadmap | `part-4-adoption/` |

## The two frameworks

**A.G.E.N.T. — the strategy cycle (Weeks 3–5)**

- **A — Audit**: map how the work actually happens, not how the manual says it happens.
- **G — Gauge**: score candidate workflows on value, feasibility, and risk; apply the "So what?" test until a benefit connects to something the organization genuinely values.
- **E — Engineer**: redesign the workflow from a blank page — eliminate, combine, automate, delegate, keep human, or make collaborative.
- **N — Navigate**: assign autonomy levels, ownership, permissions, escalation, and audit requirements.
- **T — Track**: measure at four layers — business, workflow, AI quality, and risk.

**B.U.I.L.D. — the implementation studio (Weeks 6–10)**

Our own transparent implementation framework (the commercial one is not publicly
documented, so we built one we can fully stand behind):

- **B — Blueprint**: architecture, boundaries, data flows, trust boundaries, failure modes.
- **U — Unite**: connect the minimum necessary systems, read-only first, synthetic or redacted data first.
- **I — Implement**: the smallest end-to-end vertical slice, with human approval and full logging.
- **L — Learn**: build the evaluation set *before* broad use; measure correctness, grounding, abstention, escalation, cost.
- **D — Deploy**: staged progression — offline eval → shadow → sandbox → pilot → supervised → bounded production → rollout.

## The Command Center

`command-center/index.html` is an interactive HUD for running this program —
and for reusing the methodology on future projects ("learn once, build many").
It tracks the 12-week timeline, hosts a per-project workflow inventory, computes
the Week-4 scoring matrix live, and tracks each project's deliverables portfolio.
Open it via GitHub Pages at `/<repo>/agentic-ai-program/command-center/` or
locally with `python3 -m http.server`. All data stays in your browser
(localStorage) — nothing you type is committed or uploaded; use its Export
button for backups.

## How to work through it

1. Start with `PROGRESS.md` — it is the master checklist.
2. Do the weeks in order; each week file contains what to learn, the exercise, and the deliverable.
3. Deliverables are produced by filling in the files in `templates/` — copy each template into a `work/` folder as you go (keep templates clean for reuse when you train others).
4. **Your first assignment is `templates/00-workflow-inventory.md`** — an inventory of 10–15 recurring workflows from your job. Everything downstream depends on it.

## Core operating principle

> Use the least autonomous system capable of producing the required business outcome.

A workflow does not need an "agent" simply because AI is involved. The right
answer is sometimes a prompt template, a retrieval system, a deterministic
workflow, a classifier, a rule engine, an AI-assisted step with human approval —
and only sometimes a genuinely autonomous agent.

## Time commitment

- 5–7 hours weekly during strategy (Weeks 1–5)
- 8–10 hours weekly during the build (Weeks 6–10)
- ~100–120 total hours
- One real organizational workflow, one working prototype, one executive presentation, one complete implementation portfolio
