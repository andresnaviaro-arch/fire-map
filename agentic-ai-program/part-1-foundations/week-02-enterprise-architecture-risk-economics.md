# Week 2 — Enterprise Architecture, Risk, and Economics

**Goal:** understand the environment an agent must live in — the systems it
connects to, the data it touches, the ways it fails, and what it costs — well
enough to make credible build/don't-build decisions.

## What to learn

### Integration fundamentals
- **APIs, databases, SaaS applications, and system integrations** — how software
  talks to software; why "it's in the CRM" and "an agent can read it" are
  different statements.
- **Authentication vs. authorization** — proving who you are vs. what you are
  allowed to do. An agent acts under an identity with specific permissions;
  designing those permissions *is* designing the agent's blast radius.
- **Read-only vs. write-enabled tools** — the single most important safety lever.
  A read-only agent can embarrass you; a write-enabled agent can damage a
  system of record.

### Data fundamentals
- **Structured vs. unstructured data** — tables you can query vs. emails, PDFs,
  and call notes you must interpret.
- **System of record** — the one authoritative source for each fact (the ERP for
  orders, the CRM for opportunities). Agents read from many places but should
  write to systems of record only under tight control.
- **Data lineage and provenance** — where a number came from and what touched it
  on the way. An agent's claim is only as good as its cited source.
- **PII and confidential information** — customer data, pricing, contracts.
  Know your company's data classification before any data touches a model.

### Failure modes
- **Hallucination / unsupported claims** — fluent, confident, wrong. Mitigations:
  grounding in retrieved sources, required citations, permission to say "I don't know."
- **Prompt injection** — malicious or accidental instructions hidden inside data
  the agent reads (an email, a web page, a document) that try to redirect its
  behavior. Mitigations: treat all external content as data not instructions,
  limit tool authority, require approval for consequential actions.
- **Data exfiltration** — an agent with broad read access plus any outbound
  channel (email, web) can leak. Mitigations: least-privilege data access,
  egress controls, logging.

### Economics
- **Model and vendor selection** — capability tiers, hosted vs. via cloud
  platforms, data-use terms (does the vendor train on your data?), regional availability.
- **Latency, reliability, token consumption, and cost** — an agent that takes
  ninety seconds and $0.40 per run is fine for a daily account brief and
  unacceptable inside a live phone call. Cost scales with context size × calls
  per run × runs per day.
- **When conventional automation wins** — if inputs are structured and rules are
  stable, a script or workflow tool is cheaper, faster, and auditable. Reserve
  models for steps that genuinely need language understanding or judgment.

## The core decision rule

> **Use the least autonomous system capable of producing the required business outcome.**

Escalation ladder — always start at the top and move down only when forced:

1. A prompt template
2. A retrieval (RAG) system
3. A deterministic workflow
4. A classification model
5. A conventional rule engine
6. An AI-assisted workflow with human approval
7. A genuinely autonomous agent

## Practical assignment

For your own environment, sketch the systems an agent in your role would touch:
CRM, quoting tools, ERP visibility, email, product/pricing sources, shared
drives. For each, note: structured or unstructured? read or write needed?
what's the system of record? what data classification applies?

## Deliverable — Enterprise AI Architecture Primer

A 2–3 page document, **written in language you could present to a vice
president**, covering:

1. How enterprise AI systems connect to business systems (one diagram)
2. The three failure modes above and how each is controlled
3. The escalation ladder, with one Wesco-relevant example at each rung
4. A cost sketch: what one useful agent run costs and what it replaces

Test: hand it to a non-technical colleague. If they can retell the escalation
ladder and name the three failure modes, Week 2 is done.
