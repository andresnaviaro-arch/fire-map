# Week B1 — Spot Automation Opportunities

**Goal:** learn what automation is (and isn't), and find the workflows in your
own job where it pays off fastest.

## What to learn

### Key concepts
- **Automation vs. AI vs. agentic AI** — automation executes fixed steps;
  AI adds interpretation (read this email, classify this document); agentic AI
  decides *which* steps to take. Most business value hides in the first two.
- **Trigger → action** thinking — every automation is "when X happens, do Y
  (and Z, and W)". Triggers: a form submission, a new email, a schedule, a new
  row, a file upload, a webhook.
- **The integration layer** — no-code platforms (Make.com, Zapier, n8n) are
  glue between apps you already use: email, sheets, WhatsApp, calendars, CRMs,
  drives. AI enters as one step in the chain, not the whole chain.
- **Where automation helps most** — recurring reports, data moved between
  systems by hand, monitoring (pipelines, portals, inboxes) for changes,
  notifications and reminders, document generation from templates.

### The problem-solving mindset
Algorithmic thinking: take a fuzzy chore and force it into explicit steps —
inputs, transformations, outputs, decision points. If every decision point can
be written as a rule ("if amount > X", "if status = pending"), the whole thing
automates. If a decision point hides judgment ("if the customer seems upset"),
that step needs AI — or a human.

## Exercise — mine your inventories

Open your command-center inventories (all three projects) and tag each
workflow:

- **AUTOMATE** — fixed steps, rule decisions only (e.g., quote-status refresh,
  registration-expiry alerts, expediente portal sweep, report assembly)
- **AI-ASSIST** — fixed flow with 1–2 interpretation steps (e.g., classify
  incoming request, extract fields from a PDF, draft a templated reply)
- **AGENT** — genuine multi-step judgment (stays on the main-program track)

Automation candidates are usually the workflows that scored **high frequency +
high repeatability + low judgment complexity** in the scoring matrix.

## Playbook assignment

Write a **one-page automation brief** identifying 2–3 workflows to automate.
For each: the trigger, the current manual steps, the systems touched, hours
lost per month, what "done" looks like, and which single one you'll map in B2.

## Quality test

Show the brief to someone who knows your work. If they say "yes, and also
[fourth workflow]" — the brief communicated. If they ask "but how would that
work?" — you described a wish, not a workflow. Sharpen the trigger and steps.
