# Week 1 — From Generative AI to Agentic Systems

**Goal:** build the mental model that everything else in the program hangs on.
By the end of this week you should be able to draw an agentic system on a
whiteboard and say precisely which parts are probabilistic and which are not.

## What to learn

### The model layer
- **What transformers and language models do** — next-token prediction over a
  context; why that produces fluent text and why it also produces confident errors.
- **Tokens** — the unit of both cost and capacity. A context window is a hard
  budget; everything the model "knows" about your task must fit in it or be retrieved into it.
- **Inference** — each response is a fresh computation. The model has no memory
  between calls unless you supply it.
- **Embeddings** — text mapped to vectors so "similar meaning" becomes "nearby
  points"; the mechanism behind semantic search and RAG.
- **Multimodality** — models that read images, documents, and audio, not just text.

### The system layer
- **Prompt vs. workflow vs. agent**:
  - *Prompt*: one call, one answer.
  - *Workflow*: a fixed sequence of steps, some of which call a model.
  - *Agent*: the model itself decides which step or tool comes next, in a loop, until the goal is met.
- **Deterministic vs. probabilistic** — conventional software gives the same
  output for the same input; a model may not. Design consequence: put
  deterministic rails (validation, schemas, approval gates) around probabilistic parts.
- **Tool calling and structured outputs** — the model emits a machine-readable
  request ("call `get_quote_status` with `quote_id=...`"); your code executes it
  and returns the result. Structured output (JSON schemas) is how model text
  becomes reliable input for downstream systems.
- **Retrieval-augmented generation (RAG)** — fetch relevant documents at question
  time and put them in context, so answers are grounded in your data instead of
  the model's training memory.
- **Memory and state** — conversation history, scratchpads, and databases that
  persist between calls. Agents need explicit state; models have none.
- **Single-agent vs. multi-agent** — one loop with many tools vs. several
  specialized loops coordinated by an orchestrator. Start single; multi-agent is
  an optimization, not a default.
- **The product spectrum** — assistant (answers when asked) → copilot (works
  alongside a human in their tool) → autonomous agent (pursues a goal with
  bounded independence) → orchestrator (coordinates other agents and systems).
- **Agency is a spectrum, not a binary.** The design question is never "is this
  an agent?" but "how much authority does this system have, over which actions,
  under whose supervision?"

## The essential conceptual model

Every serious agentic system contains these eleven parts. Memorize the list —
it becomes your review checklist for every design in this program:

1. A **goal**
2. **Instructions and policies**
3. **Context** (what it is told about the situation)
4. A **reasoning/planning loop**
5. **Tools**
6. **Data sources**
7. **State or memory**
8. **Permission boundaries**
9. **Evaluation mechanisms**
10. **Human oversight**
11. **Logging and observability**

If a proposal is missing any of 8–11, it is a demo, not a system.

## Practical assignment

Take five activities from your current work (e.g., preparing a quote, chasing a
PO, building an account brief, answering an availability question, writing a
weekly report). Classify each as:

- Information retrieval
- Content generation
- Decision support
- Process automation
- Agentic workflow

For each, note *why* — what property of the activity puts it in that class
(fixed inputs? judgment? multiple systems? consequences of error?).

## Deliverable — AI and Agentic Systems Concept Map

One page (drawn or written) that shows:

- The eleven components of an agentic system and how they connect
- The prompt → workflow → agent spectrum with one example of each *from your own job*
- Your five classified activities placed on that spectrum

Test: could you use this page to explain to a colleague, in ten minutes, what
an agent actually is and is not? If yes, Week 1 is done.
