# Week B2 — Map the Process from A to Z

**Goal:** turn the chosen workflow into a map so precise that a machine — or a
stranger — could execute it.

## What to learn

### Anatomy of a process map
For every step, name three things:
- **Action** — what happens (verb + object: "download attachment", "look up
  customer row", "send reminder")
- **Input** — what the step consumes, and *where it comes from* (which field,
  which file, which system)
- **Output** — what it produces, and *where it goes next*

Then connect: trigger at the top, outputs feeding inputs, decision diamonds
where flow branches, and a defined end state.

### Tools
Miro, draw.io, or paper — the tool doesn't matter; the discipline does. One
box per action, one diamond per decision, no box containing the word "somehow."

### The three layers most people forget
1. **Failure paths** — what happens when the attachment is missing, the API
   times out, the row isn't found, the format changed? Every automation needs a
   defined behavior for each (retry, skip + log, alert a human).
2. **Quality assurance** — where do you check the output is right? Build in a
   verification step (row count matches, total balances, required fields
   non-empty) *before* the result is used or sent.
3. **Performance & improvement** — what will you measure (runs, failures,
   minutes saved) and where do those numbers land so you actually see them?

## Exercise

Walk the current manual process once at normal speed and write down every
click, copy, and decision as you go. The map is built from this recording, not
from memory — memory smooths over exactly the exceptions that break automations.

## Playbook assignment

Produce a **detailed automation process map** for the one workflow chosen in
B1: trigger, every action with inputs/outputs, every decision as an explicit
rule, failure paths, one QA checkpoint, and the metrics you'll track. Note
which steps are pure logic and which need an AI step (interpretation,
extraction, drafting).

## Quality test

Hand the map to someone (or read it back to yourself tomorrow) and ask: could
you execute this workflow using ONLY what's on the page? Every question they
have to ask you is a hole an automation would fall through.
