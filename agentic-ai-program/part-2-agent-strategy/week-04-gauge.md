# Week 4 — G: Gauge

**Goal:** measure business outcomes, not AI outputs — then select **one**
workflow, on evidence, and commit to it.

## The "So what?" test

Keep questioning a proposed benefit until it connects to something the
organization genuinely values. If the chain breaks, the benefit is cosmetic.

Worked example:

> Generate quotations faster.
> **So what?** Customers receive responses sooner.
> **So what?** We improve conversion and reduce lost opportunities.
> **So what?** We increase gross profit while account managers recover selling time.

That terminates in money and capacity — it passes. "The summary looks more
professional" does not terminate anywhere — it fails.

Build one "So what?" chain for each candidate workflow. Together these form
your **business-outcome tree**.

## The workflow-scoring model

Score every candidate from 1–5 on ten dimensions
(use `templates/01-scoring-matrix.md`):

| Dimension | Meaning | Higher is… |
|---|---|---|
| Business value | Revenue, margin, cost, service, or strategic impact | better |
| Frequency | How often the workflow occurs | better |
| Time burden | Human effort currently consumed | better (more to recover) |
| Repeatability | Stability of inputs and decisions | better |
| Judgment complexity | Need for contextual reasoning | *harder* |
| Data readiness | Accessibility and quality of required information | better |
| Integration readiness | Ability to connect relevant systems | better |
| Error severity | Damage caused by an incorrect action | *riskier* |
| Governance complexity | Privacy, compliance, contractual, audit concerns | *riskier* |
| Adoption readiness | Probability that employees will actually use it | better |

Roll the dimensions up into:

- **Value score** = business value + frequency + time burden
- **Feasibility score** = repeatability + data readiness + integration readiness + adoption readiness − judgment complexity
- **Risk score** = error severity + governance complexity
- Plus honest estimates of **implementation effort** and **time to measurable value**

**Selection rule:** pick the highest value × feasibility candidate whose risk
you can control with autonomy levels (Week 5) — not the most impressive one.
The first project's real job is to *prove the methodology*, so weight time-to-
measurable-value heavily.

## Candidate workflows for a Wesco/Anixter sales role

Starting points to score alongside your own inventory:

1. **Account opportunity and follow-up agent** — reviews CRM activity, open quotations, customer communications, purchasing history, and sales signals; produces prioritized next actions; drafts follow-ups but never sends without approval.
2. **Quotation intelligence workflow** — collects specifications, identifies missing information, matches products, requests internal pricing, prepares quote material, flags margin risks.
3. **English Caribbean account-planning agent** — account briefs, whitespace identification, project tracking, outreach recommendations, weekly territory priorities.
4. **Demand-generation research workflow** — monitors projects and customer developments, matches them to Wesco capabilities, produces evidence-backed opportunities.
5. **Sales-management intelligence workflow** — converts scattered account information into forecast risks, opportunity summaries, follow-up commitments, and management-ready reports.

Provisional favorite: a combined **Account Intelligence and Opportunity
Orchestrator** (1 + 3). But score first — the matrix decides, not the enthusiasm.

## Deliverables

1. **Use-case inventory** — all candidates, one line each
2. **Prioritization matrix** — completed scoring for every candidate
3. **Business-outcome tree** — the "So what?" chains
4. **Selected workflow** — one, named
5. **Problem statement** — three sentences: who suffers, what it costs today, what "better" means
6. **Baseline and target metrics** — from your Week 3 baseline table, with explicit targets (e.g., "follow-up cycle time from 4 days to 1; 3 hours/week of AM time recovered")
7. **Go/no-go recommendation** — one page, written as if to your manager

## Quality test

Read the problem statement aloud. If it mentions "AI" before it mentions the
business problem, rewrite it. The technology is the answer, not the subject.
