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

```yaml
change_id: GCH-0007
timestamp: 2026-06-22
run_id: RUN-0015
changed_surface:
  - agent-governance/CROSS-REPO-CONTEXT-PROTOCOL.md
  - absorbers/time-as-finality.md
  - absorbers/gu-formalization.md
  - absorbers/README.md
  - workflows/W000-repo-steward-cycle.md
change_type: cross_repo_context_protocol
reason: Joe clarified that Temporal Issuance should be aware of time-as-finality and GU formalization as prior-thinking context and local-minimum escape surfaces.
expected_learning_value: Help the steward escape local minima without merging ledgers or importing adjacent claims as authority.
risk: Cross-repo context could blur project boundaries if treated as evidence rather than context.
review_needed: false
rollback_or_revisit_trigger: If cross-repo context starts promoting claims or importing assumptions, narrow this protocol to explicit stuck-state use only.
```

```yaml
change_id: GCH-0008
timestamp: 2026-06-21T22:36:05-05:00
run_id: RUN-0023
changed_surface:
  - workflows/W006-divergent-persona-convergence-check.md
  - workflows/W007-steelman-and-hegelian-persona-pass.md
  - workflows/README.md
change_type: durable_workflow_creation
reason: Joe asked to save both full persona-analysis versions as workflows after RUN-0020 and RUN-0022 proved useful.
expected_learning_value: Let W000 reuse full divergent persona generation and full steelman/Hegelian persona passes when future convergence or weak-target risks appear.
risk: The workflows could become heavyweight ceremony if invoked too often or could protect the hypothesis if steelman output is mistaken for evidence.
review_needed: false
rollback_or_revisit_trigger: If W006 or W007 repeatedly fails to change research decisions, produces no new alternatives, or slows fixture-based testing, narrow, split, or retire the workflow.
```

```yaml
change_id: GCH-0009
timestamp: 2026-06-22T08:19:35-05:00
run_id: RUN-0038
changed_surface:
  - HYPOTHESIS.md
  - NORTH-STAR.md
  - CLAIM-LEDGER.md
  - README.md
  - ROADMAP.md
  - agent-governance/NEXT-TRIGGER-PLAN.md
change_type: constitutional_object_change
reason: >
  Joe explicitly approved, in the trusted control channel, a vNext of the constitutional core
  hypothesis. The deepest claim moves from temporal issuance as monotone realization of
  constraint to a shared, observer-participatory process kept open-ended by ongoing issuance.
  Temporal order/finality become the downstream observer-side reconstruction layer. The
  issuance-energy-cosmology bridge is named as the central research target, not an earned result.
expected_learning_value: >
  Redirects the program away from arrow-of-time derivation (too easily absorbed) toward making
  issuance precise and testing whether it is more than a relabeling of known physics.
risk: >
  A constitutional change can lock in a framing prematurely. Mitigated by keeping TI-C019
  speculative, preserving the prior framing as TI-C001, and requiring a discriminator before any
  physics-bridge claim.
review_needed: false
rollback_or_revisit_trigger: >
  If the issuance-precision pass finds no discriminator separating issuance from stochastic
  update, information flow, causal/event growth, or thermodynamic entropy, weaken TI-C019 and
  reopen the constitutional framing with Joe.
```

```yaml
change_id: GCH-0010
timestamp: 2026-06-24
run_id: manual_request
changed_surface:
  - workflows/W010-frontier-selection-and-next-work-ranking.md
  - workflows/README.md
change_type: durable_workflow_creation
reason: >
  Joe asked to preserve the reusable meta-workflow used to inspect the repo, identify the
  live frontier, and rank the next most important work. W000 already serves as the steward
  container, but the repo lacked a specific frontier-selection subroutine for cases where
  multiple next actions compete or routing surfaces may be stale.
expected_learning_value: >
  Improve next-trigger quality by extracting frontier candidates from memory, roadmap,
  claim ledger, path kills, latest runs, and explorations; rank them by verdict movement;
  and recommend one primary next trigger with success/failure conditions.
risk: >
  W010 could become process ceremony if invoked when the next trigger is already fresh and
  obvious, or could bias the repo toward ranking exercises instead of doing research.
review_needed: false
rollback_or_revisit_trigger: >
  If W010 repeatedly selects the same route W000 would have selected without catching stale
  state, hidden blockers, or higher-leverage work, narrow it to on-demand use or retire it.
```
