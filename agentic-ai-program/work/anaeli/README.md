# Project 03 — Anaeli — AI Legal Agent (Gestión Jurídica)

Artifacts folder for Anaeli, the Colombian AI legal agent being built inside
Gestión Jurídica. The command center carries it as **P03**, seeded with 9
drafted workflows: client intake & triage, derechos de petición, acciones de
tutela, legal research & jurisprudence, expediente monitoring (Rama Judicial),
términos procesales calendar, contract review, client status communication,
and case-file/evidence organization.

## Domain-specific standing orders (beyond the global ones)

- **A licensed abogado reviews and signs everything.** Anaeli drafts,
  researches, monitors, and organizes — it does not give legal advice to
  clients or file anything autonomously. Autonomy Level ≤ 2 on all
  client-facing and court-facing actions until evaluation evidence and
  professional-responsibility review say otherwise.
- **Citations are existence-checked.** Every sentencia, ley, or decreto cited
  must be verified against its source before it reaches a document.
  Hallucinated case law is the defining failure mode of legal AI — the Week 9
  evaluation set must include adversarial citation cases, and the correct
  behavior when unsure is abstention.
- **Deadline computations are human-confirmed.** Anaeli computes términos
  (hábiles vs. calendario, festivos); a human confirms every date that enters
  the calendar. A blown término is the existential risk of a practice.
- **Ley 1581 (habeas data) and secreto profesional govern all data.** Client
  identity, health, employment, and case facts are the most sensitive data in
  any project in this program: least-privilege access, no client data in
  unapproved tools, identity verification before any status disclosure.

## Reflecting the head start

This is the most advanced project of the three — record that honestly:
mark existing artifacts (prototype, prompts, datasets, templates) as
*In progress* / *Complete* in the VAULT, and note where each lives. The gaps
the vault exposes (typically the evaluation set, the governance charter, and
the operating procedure) are the highest-value next work, not more features.

**Data hygiene:** no unredacted client names, case facts, or personal data
committed here — ever. This folder holds method artifacts, not case files.
