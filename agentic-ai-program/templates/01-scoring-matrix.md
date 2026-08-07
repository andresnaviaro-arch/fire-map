# Template — Workflow Scoring Matrix (Week 4, Gauge)

Score every candidate workflow **1–5** on each dimension. Copy to
`work/scoring-matrix.md` (or rebuild as a spreadsheet — the math is easier).

## Dimension definitions

| Dimension | 1 means | 5 means |
|---|---|---|
| Business value | Cosmetic improvement | Direct revenue/margin/service impact |
| Frequency | A few times a year | Many times a day |
| Time burden | Minutes a week | Hours a day |
| Repeatability | Every instance is unique | Inputs and decisions highly stable |
| Judgment complexity | Pure rules | Deep contextual judgment throughout |
| Data readiness | Data scattered, unreliable, inaccessible | Clean, accessible, trustworthy |
| Integration readiness | No API/export path to key systems | Everything connectable today |
| Error severity | Mistake is trivially caught/fixed | Mistake damages customer or books |
| Governance complexity | No sensitive data or compliance angle | Heavy privacy/contractual/audit load |
| Adoption readiness | Users skeptical, workflow contested | Users asking for this already |

## Scoring table

| Candidate | Biz value | Freq | Time | Repeat | Judgment | Data | Integr. | Error sev. | Govern. | Adoption |
|---|---|---|---|---|---|---|---|---|---|---|
| 1. | | | | | | | | | | |
| 2. | | | | | | | | | | |
| 3. | | | | | | | | | | |
| 4. | | | | | | | | | | |
| 5. | | | | | | | | | | |

## Roll-ups

For each candidate compute:

- **Value score** = Business value + Frequency + Time burden _(max 15)_
- **Feasibility score** = Repeatability + Data readiness + Integration readiness + Adoption readiness − Judgment complexity _(max 19)_
- **Risk score** = Error severity + Governance complexity _(max 10; lower is safer)_

| Candidate | Value /15 | Feasibility /19 | Risk /10 | Effort (S/M/L) | Time to measurable value | Priority |
|---|---|---|---|---|---|---|
| 1. | | | | | | |
| 2. | | | | | | |

## Selection rule

Pick the highest **Value × Feasibility** whose **Risk** you can control with
autonomy levels — weighting **time to measurable value** heavily, because the
first project's job is to prove the methodology.

## Decision record

- **Selected workflow:**
- **Runner-up (and why it lost):**
- **What would change this decision:**
