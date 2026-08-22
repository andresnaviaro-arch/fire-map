# Week B4 — Pitch, Adoption & Guardrails

**Goal:** turn a working automation into an *adopted* automation — with
buy-in, a rollout plan, and guardrails that survive scrutiny.

## What to learn

### Getting buy-in
- **Lead with the before/after, not the technology.** "Quote status used to
  take 40 minutes every morning; now it's in your inbox at 7:00" beats any
  tool name.
- **Address the two silent fears directly**: "will this replace me?" (no — it
  removes the part of the job nobody wants) and "will I be blamed when it
  breaks?" (no — here's the error route and who owns it).
- **Recruit one visible early user** whose testimony carries more weight than
  your demo. Their workflow, their words.
- **Show the failure behavior on purpose** — trust comes from watching the
  system handle a bad input gracefully, same principle as the main program's
  demo rules.

### Implementation planning
A rollout plan that gets adopted has: a named pilot group, a start date and a
review date, a definition of success (metric + threshold), a support channel
("it broke, who do I tell?"), training (usually 15 minutes, not a course), and
an explicit rollback ("if it fails review, we return to the manual process,
documented here").

### Guardrails for responsible use
- **Oversight** — which outputs need human approval; who reviews the error log
  and how often; the kill switch (turn off the scenario, revert to manual).
- **Compliance & data** — what data flows through which third-party platform;
  data-processing terms; regional rules (for Anaeli: Ley 1581 — client data
  does not enter tools without a legal basis and safeguards).
- **Brand & tone** — anything customer-facing follows approved templates and
  language; AI-drafted ≠ AI-sent.
- **Cost control** — per-run cost ceiling, monthly budget alert, and a volume
  estimate reviewed after the pilot.

## Playbook assignment

Choose one (do the other later if this automation scales):
1. **Governance framework** — one page: owner, approved data, approval gates,
   error-log review cadence, kill switch, compliance notes. (Reuse the main
   program's governance charter template, trimmed to automation scale.)
2. **Rollout plan** — one page: pilot group, dates, success metric, training,
   support channel, rollback.

## Quality test

Pitch it in 5 minutes to a skeptic. If their first question is about the
technology, your pitch led with the wrong thing. If it's "what happens when it
breaks?" and your guardrails page already answers it — you're done.
