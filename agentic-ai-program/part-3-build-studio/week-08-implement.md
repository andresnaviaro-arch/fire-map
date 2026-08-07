# Week 8 — I: Implement

**Goal:** build the smallest end-to-end **vertical slice** — one thin path all
the way through the workflow, working for real, rather than many half-built parts.

## The six-step slice

Whatever your selected workflow, the slice has the same shape:

1. **Accept a real workflow trigger** — e.g., "weekly review of account X" or
   "new quote request received"
2. **Collect the required evidence** — via the Week 7 connections
3. **Perform one useful analysis** — e.g., identify stalled quotes and rank
   follow-up priority; or find the gaps in a specification
4. **Generate a structured recommendation** — fixed format, every claim cited
   to its source, confidence stated, unknowns listed
5. **Request human approval** — the recommendation is presented; the human
   approves, edits, or rejects; nothing external happens without that
6. **Log the complete process** — inputs, retrieved evidence, model outputs,
   tool calls, the human's decision, timestamps

If step 4 works but step 6 doesn't exist, the slice is not done. Logging is
what turns a demo into evidence.

## Prompt and policy registry

Keep every prompt in version control (a folder of numbered markdown files is
fine). Each entry records:

- The prompt/policy text itself
- What changed from the previous version and why
- The system's role, tone, and hard rules (what it must never claim or do)
- Required output schema

This registry is a first-class deliverable — it is how your work becomes
reproducible and how a future team maintains the system.

## Design rules for the slice

- **Structured output everywhere.** The recommendation is a schema (fields:
  account, finding, evidence with citations, proposed action, urgency,
  confidence, missing information) — not free prose. Structure is what makes
  evaluation (Week 9) possible.
- **Abstention is a feature.** The system must be able to output "insufficient
  evidence — here is what's missing" and be *rewarded* for it. An agent that
  always answers is an agent that sometimes invents.
- **Citations are mandatory.** Every factual claim points at a retrieved
  record. No citation → the claim is flagged, not shown as fact.
- **One workflow, one account type, one trigger.** Resist scope. Breadth comes
  after the slice survives evaluation.

## What to produce

1. The working slice, runnable on demand
2. The prompt and policy registry (initial versions)
3. Three recorded end-to-end runs: one typical case, one difficult case, one
   missing-data case — with their logs
4. A 5-minute demo you can give from a clean start

## Quality test

Run the slice on an account you know cold. Would you act on its recommendation?
Where it's wrong, can the log show you *why* it was wrong? Both yes → Implement
is done.
