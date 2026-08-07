# Week 5 — E, N, T: Engineer, Navigate, Track

**Goal:** redesign the selected workflow from a blank page, decide exactly how
much authority the system gets, and define how success and safety will be
measured. The week ends with the **Agentic Workflow Implementation Brief** —
the primary output of Phase One.

---

## E — Engineer: redesign from a blank page

Do **not** start from "add AI to the current process." Start from the outcome
and design backward. For every step in the current-state map, make one of eight
decisions:

1. **Eliminate it** — it exists for historical reasons
2. **Combine it** — with an adjacent step
3. **Automate it deterministically** — script/workflow tool; no model needed
4. **Delegate it to AI** — language understanding or judgment required
5. **Keep it human** — relationship, accountability, or regulation demands it
6. **Make it collaborative** — AI drafts, human decides
7. **Perform it in parallel** — it only ran sequentially out of habit
8. **Convert it to exception-only** — automate the 90% case; humans see the rest

Then, for the redesigned workflow, define:

- **Agent roles** — what each AI component is responsible for
- **Inputs and outputs** — per step, with formats
- **Knowledge sources** — which documents/systems ground which answers
- **Tools** — each capability the agent can invoke, read or write
- **Decision rules** — what is rule-based (deterministic) vs. judgment (model)
- **State transitions** — the workflow's stages and what moves work between them
- **Escalation conditions** — precisely when the agent must stop and ask a human
- **Error handling** — what happens on tool failure, missing data, contradiction
- **Evidence requirements** — what the agent must cite before any claim or recommendation

---

## N — Navigate: autonomy and governance

Assign **every decision** in the redesigned workflow one of four autonomy levels:

| Level | Name | Agent authority |
|---|---|---|
| 0 | Inform | Finds and organizes information |
| 1 | Recommend | Proposes an action; human decides |
| 2 | Act with approval | Prepares execution; human authorizes it |
| 3 | Bounded autonomy | Acts independently inside explicit limits |

**Initial policy:** customer communications, pricing commitments, contractual
statements, and consequential CRM changes start at Level 2 or below. Autonomy
is *earned* with evaluation evidence (Week 9) and pilot history — never granted
by default.

Governance must name (fill in `templates/03-governance-charter.md`):

- Business owner · Technical owner · Data owner · Risk owner
- Authorized users
- Permitted data · Prohibited data
- Allowed actions · Approval requirements
- Escalation rules
- Audit logs
- Incident handling · Rollback mechanism
- Periodic review cadence

---

## T — Track: four measurement layers

| Layer | Measures | Examples for a sales workflow |
|---|---|---|
| **Business** | Does the organization gain? | Revenue, conversion, margin, service level, AM hours recovered |
| **Workflow** | Does the process improve? | Cycle time, queue time, rework, completion rate |
| **AI quality** | Is the system good? | Accuracy, completeness, groundedness (claims traceable to sources), tool-use success |
| **Risk** | Is the system safe? | Harmful actions, policy violations, unauthorized disclosure, human override rate |

Rules of thumb:

- Every metric needs a **baseline** (Week 3) and a **target** (Week 4).
- The override rate is a feature, not an embarrassment — a falling override
  rate is your evidence for raising autonomy levels later.
- If you can only track one AI-quality metric at first, track **groundedness**.

---

## Deliverable — Agentic Workflow Implementation Brief

Fill in `templates/02-implementation-brief.md`. It packages everything from
Weeks 3–5: the audited current state, the scored selection, the redesigned
future state, autonomy and governance, and the measurement plan.

**Quality test:** the brief should let a competent engineer who has never met
you start building the right system — and let a risk-minded VP approve it
without a meeting.
