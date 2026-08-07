# Week 7 — U: Unite

**Goal:** connect the *minimum necessary* systems — read-only first, safe data
first. Integration is where prototypes die; keep this week ruthlessly small.

## The minimum system set

For a sales-intelligence workflow, the typical connections in priority order:

1. **CRM** — accounts, opportunities, activities, open quotes
2. **Email or an approved communications source** — recent customer threads
3. **Product information** — catalog, availability signals
4. **Pricing sources** — internally visible pricing/margin context
5. **Internal documents** — account plans, call notes, org charts
6. **External research sources** — news, project announcements, public tenders
7. **Output destination** — where recommendations land (a document, a dashboard, a draft email folder)

Connect only what the Week 8 vertical slice needs. Everything else waits.

## Rules for this week

- **Read-only integrations first.** No write access to any business system in
  the prototype phase. The "output destination" is a document or draft — not a
  sent email, not a CRM update.
- **Synthetic or redacted data first.** Build and debug against invented
  accounts or redacted exports. Move to live read-only data only once the
  plumbing works and only within company-approved boundaries.
- **Manual export is a valid integration.** If API access to the CRM requires a
  three-month IT ticket, a weekly CSV export is an honest Level-0 integration —
  note it as a dependency for the roadmap, and keep building. Do not let
  perfect integration block a working prototype.
- **Never paste confidential data into unapproved tools.** The integration
  story you tell in Week 12 must survive a security review of what you actually did.
- **One credential, least privilege.** Whatever identity the prototype uses
  should see only the data in the blueprint's data-flow diagram.

## What to produce

1. **Connection register** — for each source: method (API / export / manual),
   refresh cadence, data classification, and approval status (who said it was OK)
2. **Working retrieval** — demonstrate that for one real (or realistic) account
   you can programmatically assemble: open opportunities, recent activity,
   quote status, and one external signal
3. **Dependency list** — integrations you deferred, what unlocks them, and who
   owns that unlock (this feeds the 90-day roadmap)

## Quality test

Pick an account. Can the system assemble its context bundle in under a minute
without you hand-copying anything? If yes — even via a CSV export — Unite is done.
