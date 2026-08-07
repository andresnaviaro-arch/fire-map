# Week 10 — D: Deploy

**Goal:** move from "working prototype" to "governed pilot" through staged
exposure. Deployment is a ladder, not a switch — each rung earns the next with
evidence.

## The seven-stage ladder

| Stage | What runs | Who sees it | Exit criterion |
|---|---|---|---|
| 1. Offline evaluation | Eval set only | You | Week 9 scores meet targets |
| 2. Shadow mode | Real triggers, outputs recorded but **not used** | You | Shadow outputs match/beat what you actually did, over 2+ weeks |
| 3. Internal sandbox | On demand, synthetic + own accounts | You + 1–2 trusted colleagues | Colleagues find it useful without coaching |
| 4. Limited pilot | Real workflow, few users, few accounts | Named pilot group | Pilot metrics vs. baseline favorable; no risk incidents |
| 5. Supervised use | Broader use, human approval on every action | Pilot group + manager visibility | Override rate low and stable |
| 6. Bounded production | Level-3 autonomy on the narrow, proven action set | Authorized users | Governance sign-off with eval + pilot evidence |
| 7. Broader rollout | More users, territories, adjacent workflows | Organization | Repeatable onboarding + training exists |

This program takes you through stage 4 (limited pilot proposal). Stages 5–7
belong to the 90-day roadmap and require organizational approval.

**Shadow mode is the highest-value, lowest-risk stage — do not skip it.** Two
weeks of "here's what the agent would have told you, next to what you actually
did" is the most persuasive artifact you can put in front of management.

## Phase Two deliverables — the complete portfolio

By the end of Week 10, you should hold all twelve:

1. **Working prototype** (the vertical slice, iterated through evaluation)
2. **Architecture specification** (Week 6 blueprint, updated to as-built)
3. **Prompt and policy registry** (versioned)
4. **Tool specifications** (the Week 6 inventory, as-built)
5. **Evaluation dataset**
6. **Evaluation report** (with improvement curve)
7. **Risk and controls register** — each failure mode → its control → its evidence
8. **Operating procedure** — how to run it, check it, and stop it (the rollback/kill switch, in writing)
9. **User guide** — one page, for an AM who has never seen it
10. **Demo script** — the 10-minute version with a typical case and a graceful-failure case
11. **Pilot results** (or shadow-mode results, if the pilot awaits approval)
12. **90-day implementation roadmap** — stages 4→6, integration unlocks from Week 7's dependency list, owners, and decision points

Complete `templates/03-governance-charter.md` now if not already done — the
charter is what converts stage 4 into stages 5–6.

## Quality test

The kill-switch question: if this system misbehaved on a Tuesday morning, who
turns it off, how, in how many minutes, and what happens to in-flight work?
If the operating procedure answers that in one paragraph, you are ready for
Part IV.
