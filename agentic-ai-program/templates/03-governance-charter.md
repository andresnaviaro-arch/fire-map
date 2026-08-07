# Template — Governance Charter

Copy to `work/governance-charter.md`. This is the document that lets a
risk-minded reviewer say yes. Every field must have a named person or an
explicit rule — "TBD" means not ready for pilot.

## System identity
- **System name:**
- **Workflow covered:**
- **Version / date:**

## Ownership

| Role | Name | Responsibility |
|---|---|---|
| Business owner | | Outcomes, adoption, pilot decisions |
| Technical owner | | Build, operation, incident response |
| Data owner | | What data may be used and how |
| Risk owner | | Controls, reviews, escalation authority |

## Users
- **Authorized users:** *(named individuals during pilot; a role definition later)*
- **Access method:**

## Data rules
- **Permitted data:**
- **Prohibited data:** *(e.g., anything outside assigned accounts; HR data; supplier cost beyond the user's own visibility)*
- **Data residence:** *(where context, logs, and outputs are stored)*
- **Vendor terms check:** *(does the model provider train on our data? who verified?)*

## Action rules

| Action | Allowed? | Autonomy level | Approval required from |
|---|---|---|---|
| Read CRM records | | | |
| Draft customer email | | | |
| Send customer email | | | |
| Update CRM records | | | |
| State or commit pricing | | | |
| | | | |

## Escalation rules
*The agent must stop and route to a human when:* …

## Audit and logging
- **What is logged:** inputs, retrieved evidence, outputs, tool calls, approvals/overrides, timestamps
- **Where logs live / retention:**
- **Who reviews them / cadence:**

## Incident handling
- **What counts as an incident:** *(harmful action, policy violation, data disclosure, sustained wrong output)*
- **Report to / within:**
- **Kill switch:** *who turns it off, how, in how many minutes*
- **Rollback:** *what happens to in-flight and recent outputs*

## Periodic review
- **Cadence:** *(monthly during pilot)*
- **Review inputs:** eval scores, override rate, incidents, cost
- **Standing agenda:** should any autonomy level move up or down?

## Signatures
| Role | Name | Date |
|---|---|---|
| Business owner | | |
| Risk owner | | |
