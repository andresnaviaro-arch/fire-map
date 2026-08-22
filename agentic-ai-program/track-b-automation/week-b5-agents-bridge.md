# Week B5 — Bonus Workshop: From Automation to Agents

**Goal:** understand precisely where automation ends and agency begins, add an
agent step to your working automation, and know the limits — this week hands
off into Part III of the main program.

## What to learn

### AI step vs. AI agent vs. agentic workflow
- An **AI step** answers one question inside a fixed flow (classify, extract,
  draft). The flow decides what happens next.
- An **AI agent** is given a goal and tools, and *itself* decides which steps
  to take, in a loop, until done.
- An **agentic workflow** mixes both: deterministic rails for the fixed parts,
  an agent for the genuinely open-ended parts, approval gates between them.

The design question is never "should I use an agent?" but "which single step
in this flow actually needs one?" Usually it's the step your B2 map couldn't
reduce to a rule.

### Explore the platforms (hands-on hour)
Try goal-directed AI in the tools available to you — browser-using assistant
modes, computer-use agents, agent nodes in Make/n8n, and Claude (Projects,
scheduled tasks, Claude Code). Give each the same small real task (e.g.,
"check these two sources and compile a table") and note: where it shines,
where it stalls, what it cost, and what you had to verify afterward.

### Upgrade your B3 automation with one agent step
Take the working automation and replace its most rule-resistant step with an
agent call. Example upgrades:
- Quote digest → agent *prioritizes* the follow-up list and drafts the top-3
  messages (Wesco)
- Listing generator → agent researches comparable machines and suggests price
  positioning (InterNavia)
- Expediente notifier → agent summarizes the new actuación and proposes the
  response with the computed deadline (Anaeli — lawyer approves)

Keep the rails: structured output, validation gate, human approval on anything
outward-facing.

### Limits and guardrails (the honest list)
- **Data privacy** — an agent step sees more context than a rule step; apply
  the same data rules as B4, stricter for legal/client data.
- **API costs** — agents loop; loops multiply tokens. Set per-run and monthly
  ceilings before enabling, then measure.
- **Reliability** — agents fail creatively, not just mechanically. The
  validation gate and error route are MORE important, not less.
- **Human-in-the-loop** — autonomy levels from the main program apply verbatim;
  an agent inside an automation starts at Level ≤ 2.

## Playbook assignment

Ship the **upgraded workflow** (automation + one agent step) plus a half-page
**limits assessment**: what the agent step costs per run, how it fails, what
gate catches it, and what evidence would justify raising its autonomy.

## Exit — into the main program

You now have: a working automation, a working agent step inside it, and the
scar tissue of debugging both. Part III (B.U.I.L.D.) is this same discipline
at full scale: blueprint, minimal integrations, vertical slice, evaluation
set, staged deployment. Your B-track build is a legitimate head start —
log it in the relevant project's VAULT.
