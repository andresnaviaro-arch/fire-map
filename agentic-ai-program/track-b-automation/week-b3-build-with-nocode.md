# Week B3 — Build It with No-Code Tools + AI

**Goal:** ship a working end-to-end automation of a real workflow — connecting
at least two tools with an AI step in the chain.

## What to learn

### Choosing the platform

| Platform | Strengths | Watch out for |
|---|---|---|
| **Zapier** | Easiest start; widest app catalog; great for linear "when X do Y" | Costs scale with task volume; limited branching on lower tiers |
| **Make.com** | Visual scenarios, powerful branching/iteration, good price/volume | Steeper learning curve; error handling needs deliberate setup |
| **n8n** | Self-hostable (data stays yours — relevant for Anaeli/legal data), code steps when needed, generous execution model | You operate it; hosting/updates are on you |

Decision shortcut: start on whichever your data-sensitivity allows. Public/low
sensitivity → Zapier/Make for speed. Confidential (client legal data, pricing)
→ n8n self-hosted, or keep that data out of the flow entirely.

### The AI step
Every platform can call an AI model mid-flow (via native AI modules or an HTTP
call to an API). Use it for the 1–2 interpretation steps your B2 map flagged:
classify, extract fields, summarize, draft. Rules for AI-in-automation:
- **Structured output only** — force JSON with named fields; parse and validate
  before the next step consumes it.
- **Validation gate after every AI step** — required fields present? value in
  allowed range? If not → error path, never silent continuation.
- **Draft, don't send** — anything customer-facing lands as a draft for human
  approval (this is the autonomy map from the main program, applied here).

### Troubleshooting discipline
- Test with **real messy samples**, not clean ones — the weird email, the PDF
  with the missing field.
- Run steps one at a time; inspect the data payload between every pair of steps
  (most failures are shape mismatches: wrong field name, array vs. single).
- Add an **error route**: on failure → log the payload + notify you. An
  automation that fails silently is worse than no automation.
- Watch quotas and costs: task/operation counts, API pricing per run × runs/day.

## Playbook assignment

**Build and document a functional automation** for your B2-mapped workflow:
- Connects ≥ 2 tools (e.g., email → sheet, portal check → WhatsApp/Telegram
  notification, form → document → drive)
- Includes ≥ 1 AI step with a validation gate
- Has an error route and one QA checkpoint
- Documentation: one page — trigger, flow diagram (screenshot is fine), AI
  prompt used, failure behavior, cost per run, minutes saved per week

Good first candidates from your projects: quote-status digest (Wesco),
registration-expiry alerts (Wesco), listing generation from a machine record
(InterNavia), expediente-change notification (Anaeli — mind data residency).

## Quality test

Let it run unattended for one week. Zero silent failures, and you touched the
workflow only at approval gates? It's real. You "just checked it quickly" every
day? The error route isn't trustworthy yet — fix that before adding more flows.
