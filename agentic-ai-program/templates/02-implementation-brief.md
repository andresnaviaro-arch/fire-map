# Template — Agentic Workflow Implementation Brief

**The primary output of Phase One (Weeks 3–5).** Copy to
`work/implementation-brief.md`. Target length: 6–10 pages. It should let an
engineer build the right system and a VP approve it without a meeting.

---

## 1. Problem statement
*Three sentences: who suffers, what it costs today, what "better" means.
Business first — the word "AI" should not appear in this section.*

## 2. Current state (from Audit)
- Process map (attach or embed)
- Baseline performance table: volume, cycle time, touch time, error/rework rate, outcome rate
- Top 3 bottlenecks and top 3 exception types

## 3. Why this workflow (from Gauge)
- Scores: Value ___/15 · Feasibility ___/19 · Risk ___/10
- The "So what?" chain, ending in money/capacity/service
- Alternatives considered and why they lost

## 4. Future state (from Engineer)
- Redesigned process map
- Step-by-step table:

| # | Step | Disposition (eliminate / combine / deterministic / AI / human / collaborative / parallel / exception-only) | Input → Output | Tools & sources | Escalates when |
|---|---|---|---|---|---|
| | | | | | |

- Evidence requirements: what must be cited before any claim or recommendation
- Error handling: tool failure, missing data, contradictory data

## 5. Autonomy map (from Navigate)

| Decision in the workflow | Level (0 Inform / 1 Recommend / 2 Act w/ approval / 3 Bounded) | Rationale | Evidence needed to raise it |
|---|---|---|---|
| | | | |

Standing policy: customer communications, pricing commitments, contractual
statements, and consequential CRM changes start at Level ≤ 2.

## 6. Governance summary
Owners (business / technical / data / risk), authorized users, permitted and
prohibited data, allowed actions, audit logging, rollback. Full detail lives in
the Governance Charter — reference it here.

## 7. Measurement plan (from Track)

| Layer | Metric | Baseline | Target | Source |
|---|---|---|---|---|
| Business | | | | |
| Workflow | | | | |
| AI quality | | | | |
| Risk | | | | |

## 8. Scope, dependencies, and effort
- In scope / out of scope (explicit)
- Integration dependencies and their owners
- Effort estimate and time to measurable value

## 9. Recommendation
*One paragraph: build the prototype as specified above, evaluated per the
measurement plan, reviewed at [date].*
