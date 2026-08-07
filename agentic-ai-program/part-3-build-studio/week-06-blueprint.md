# Week 6 — B: Blueprint

**Goal:** turn the implementation brief into a technical design you can defend —
before writing any code or prompts.

## What to produce

### 1. Architecture diagram
One page. Show: the user, the agent loop, the model, each tool, each data
source, the approval gate, and the log store. Arrows show data direction —
every arrow into the model is a potential injection path; every arrow out is a
potential action or leak.

### 2. System boundaries
State explicitly what is **inside** the system (the agent controls it), what is
**outside** (the agent reads it or requests it), and what is **out of scope**
entirely (the agent never touches it — e.g., order entry in the ERP).

### 3. Data-flow diagram
For each data element (customer name, pricing, quote history, email content):
where it originates, where it travels, where it is stored, where it leaves the
system. Mark PII and confidential pricing. This diagram is what your security
and data colleagues will actually review.

### 4. Tool inventory
For each tool the agent can call:

| Field | Example |
|---|---|
| Name | `get_open_quotes` |
| Purpose | List open quotations for an account |
| Read/Write | Read |
| Data touched | Quote headers, values, ages — no line-item cost |
| Failure behavior | Return empty + error flag; agent must report "could not verify" |
| Autonomy level required | 0 |

Write tools get two extra fields: **approval requirement** and **rollback method**.

### 5. Agent and human roles
Which reasoning steps belong to the model, which decisions belong to the human,
and the exact artifact that crosses between them (e.g., "a structured
recommendation with citations, presented for approval").

### 6. Trust boundaries
Mark where untrusted content enters (emails, web pages, customer documents).
Everything crossing a trust boundary is **data, never instructions**. Note the
mitigation at each crossing.

### 7. Failure-mode analysis
For at least eight failure modes (wrong data, stale data, hallucinated claim,
injection attempt, tool outage, partial completion, wrong customer matched,
over-eager recommendation): likelihood, impact, detection, response.

### 8. Technology decision record
For each choice (model/vendor, orchestration approach, where it runs, where
logs live): the decision, the alternatives considered, and why. Two or three
sentences each — future-you and IT will both thank you.

## Build-tool guidance

Prefer the simplest stack that IT can live with. Practical order to evaluate:
an enterprise-approved AI platform your company already licenses → a low-code
workflow tool with AI steps → a small custom script using a vendor SDK. The
blueprint should make switching stacks cheap: tools, prompts, and policies are
the assets; the plumbing is replaceable.

## Quality test

Give the blueprint to someone technical for fifteen minutes. If they can name
what the agent can and cannot do, and where a bad outcome would be caught, it
is done.
