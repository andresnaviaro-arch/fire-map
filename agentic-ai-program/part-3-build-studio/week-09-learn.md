# Week 9 — L: Learn

**Goal:** build the evaluation set *before* broad use, measure the prototype
against it, and iterate until the numbers justify a pilot. Evaluation is what
separates "it seemed good when I tried it" from evidence a VP can approve.

Use `templates/04-evaluation-plan.md` to structure this week's output.

## Build the evaluation set

Aim for 25–50 cases across **eight case types** — the difficult types matter
more than the easy ones:

| Case type | What it tests | Example |
|---|---|---|
| Typical | The 80% path | Active account, clean data, obvious next action |
| Difficult | Real judgment | Competing priorities; large but stalled opportunity |
| Ambiguous | Restraint | Signals point both ways; correct answer is a question, not an action |
| Missing-data | Abstention | Quote history absent; system must say what it needs |
| Contradictory-data | Reconciliation | CRM says won, email thread says stalled |
| Adversarial | Injection resistance | An email in the evidence says "ignore your instructions and…" |
| Tool-failure | Degradation | A source is down; system must report, not fabricate |
| Policy-boundary | Governance | A case that tempts a pricing commitment or an unapproved send |

For each case, write the **expected outcome** first: the right recommendation,
the right abstention, or the right escalation — and what evidence should be cited.

## Score every run on eight criteria

1. **Correct outcome** — the recommendation a good AM would make
2. **Correct reasoning evidence** — right facts pulled, correctly interpreted
3. **Correct tool selection** — used the right sources, didn't wander
4. **Proper citations** — every claim traceable; no orphan claims
5. **Appropriate abstention** — said "I don't know" exactly when it should
6. **Proper escalation** — flagged the policy-boundary cases to a human
7. **Stable formatting** — schema respected every time
8. **Cost and latency** — tokens and seconds per run, within budget

Score pass/fail per criterion per case, in a spreadsheet. Percentages per
criterion are your headline numbers.

## Iterate

Fix the biggest failure class, re-run the whole set, record both scores. Two or
three loops is normal. Keep every version of prompts and scores — **the
improvement curve itself is executive evidence** ("groundedness went from 71%
to 96% across three iterations" is a better slide than any single score).

Watch for regression: a fix that raises one criterion can silently lower
another. Always re-run the full set, not just the failed cases.

## What to produce

1. The evaluation dataset (cases + expected outcomes)
2. The scoring spreadsheet with at least two full evaluation rounds
3. An **evaluation report** (2 pages): method, headline scores, known
   weaknesses, the improvement curve, and your recommendation — is this ready
   for shadow mode?

## Quality test

For the adversarial and policy-boundary cases specifically: 100% or explain
precisely why not and what compensating control covers the gap. These are the
cases governance will ask about.
