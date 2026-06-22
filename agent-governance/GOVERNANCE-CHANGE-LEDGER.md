---
artifact_type: governance_change_ledger
status: active
governance_role: governance_change_memory
constitutional: false
---

# Governance Change Ledger

This ledger records material governance design changes with rationale.

Use this for changes to:

- authority boundaries
- constitutional objects
- workflow assessment design
- persona mix
- question sets
- lookback windows
- synthesis formats
- metric definitions
- contributor-management rules
- memory summarizer rules
- automation behavior

Routine run records and normal claim-ledger updates do not need entries here unless they change governance design.

## Entry Schema

New entries should use this schema. Older launch entries are preserved below as legacy table entries.

```yaml
change_id:
timestamp:
run_id:
changed_surface:
change_type:
reason:
expected_learning_value:
risk:
review_needed:
rollback_or_revisit_trigger:
```

Append entries. Do not rewrite or delete prior entries unless a future recorded governance change explicitly changes this convention.

## Entries

| Change ID | Run | Change | Rationale | Risk | Follow-up |
| --- | --- | --- | --- | --- | --- |
| GCH-0004 | SIM-RUN-004 | Created memory summarizer protocol. | RUN-0004 identified memory drift as a core risk; the repo needed clear rules for compact summaries before more automation. | Summary rules could become too heavy for small runs. | Keep small-run summary updates concise unless strategic state changes. |
| GCH-0003 | SIM-RUN-003 | Created contributor intake and evaluation workflow. | RUN-0004 identified contributor legitimacy and manipulation risks; W005 gives public inputs a safe route into evidence without becoming operative instructions. | A workflow stub may be too weak once real contributors arrive. | Reassess after first substantive external contribution. |
| GCH-0002 | SIM-RUN-002 | Created observation-only steward metrics. | RUN-0004 identified that the steward needed signals for drift, churn, stale memory, automation health, and research/governance balance before more autonomous runs. | Metrics can become targets and create local minima. | Keep metrics observation-only until a later recorded change proves a control use is needed. |
| GCH-0001 | SIM-RUN-001 | Created governance-change ledger. | RUN-0004 and RUN-0005 showed the repo needs a place to record changes to workflow/persona/assessment design before automation evolves further. | The ledger could become ceremony if every minor edit is logged. | Use for material governance design changes only. |

## Structured Entries

```yaml
change_id: GCH-0005
timestamp: 2026-06-22
run_id: RUN-0007
changed_surface:
  - agent-governance/GOVERNANCE-CHANGE-LEDGER.md
  - agent-governance/STEWARD-METRICS.md
  - agent-governance/RUN-CLOSEOUT-CHECKLIST.md
  - agent-governance/MEMORY-SUMMARIZER-PROTOCOL.md
  - workflows/W004-stewardship-assessment-and-drift-audit.md
  - agent-governance/VSM-MAP.md
  - workflows/W005-contributor-intake-and-evaluation.md
  - workflows/W000-repo-steward-cycle.md
change_type: minimal_readiness_instrumentation
reason: Combine RUN-0004 stewardship recommendations with a minimal VSM viability check before a VSM-aware five-run stress simulation.
expected_learning_value: Make the simulation observable, auditable, and useful without building a complete governance system.
risk: Readiness instrumentation could become ceremony or retroactively obscure that the first five-run simulation already occurred.
review_needed: false
rollback_or_revisit_trigger: If the next VSM-aware simulation produces no additional observability or slows research without catching drift, weaken or retire the added readiness surfaces.
```

```yaml
change_id: GCH-0006
timestamp: 2026-06-22
run_id: RUN-0009
changed_surface:
  - agent-governance/RUN-NOMENCLATURE.md
  - workflows/W000-repo-steward-cycle.md
  - agent-governance/RUN-CLOSEOUT-CHECKLIST.md
  - workflows/W004-stewardship-assessment-and-drift-audit.md
  - agent-governance/STEWARD-METRICS.md
  - memory/future-run-queue.md
change_type: terminology_clarification
reason: Joe clarified that the prior "sim" wording was misleading because the runs were real repo runs.
expected_learning_value: Preserve historical provenance while preventing future confusion about run reality.
risk: Future readers may still misread historical `SIM-RUN-*` filenames without opening the nomenclature surface.
review_needed: false
rollback_or_revisit_trigger: If historical run names continue to confuse readers, add frontmatter clarification to old run records without renaming files.
```
