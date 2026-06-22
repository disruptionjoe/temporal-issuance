---
artifact_type: run_record
status: complete
governance_role: urgent_fix
run_id: RUN-0015
trigger: manual_request
workflow: cross_repo_context_protocol
constitutional: false
---

# RUN-0015: Cross-Repo Context Protocol

## Decision

Add a bounded protocol for using time-as-finality and GU formalization as prior-thinking context.

## Why This Work Now

Joe clarified that Temporal Issuance should be aware of both repos as context for how the thinking developed. They should change the work, but not merge ledgers or become authority. If the steward gets stuck, it should inspect those threads for local-minimum escape routes.

## Context Checked

```yaml
context_repo: time-as-finality
source_file: ../time-as-finality/explorations/temporal-issuance-bridge-v0.1.md
why_consulted: The current strongest survivor in Temporal Issuance is partial reconciliation and obstruction, which overlaps with TaF record finality and gluing work.
what_helped: The bridge note frames Temporal Issuance as source-side realization order and TaF as observer-facing readout and falsification language.
what_did_not_transfer: TaF claims and evidence do not promote Temporal Issuance claims.
effect_on_temporal_issuance: Use TaF as escape context when `G_ij`, `Omega_ij`, access, cadence, or gluing stall.
```

```yaml
context_repo: gu-formalization
source_file: ../gu-formalization/README.md and ../gu-formalization/OVERVIEW.md
why_consulted: Temporal Issuance is under no-go and absorber pressure from relativity, causal set theory, and information theory.
what_helped: GU formalization's public posture treats no-go theorems as class-relative and requires candidate substrate programs to specify obligations before defense.
what_did_not_transfer: GU claims, physics content, and publication strategy do not become Temporal Issuance claims.
effect_on_temporal_issuance: Use GU as method context for class-relative no-go handling and specification discipline.
```

## Hard Output

Created `agent-governance/CROSS-REPO-CONTEXT-PROTOCOL.md`.

## Closeout Checklist

```yaml
run_record_written: true
memory_log_updated: true
memory_summary_checked: true
claim_ledger_checked: true
roadmap_checked: true
next_trigger_plan_updated: true
path_kills_recorded_if_any: not_applicable
export_queue_updated_if_any: not_applicable
daily_review_updated_if_needed: not_applicable
governance_changes_logged_if_any: true
metrics_updated: true
vsm_map_checked: not_applicable
checks_run_or_skipped_with_reason: true
commit_pushed: true_after_this_commit
```

## Next Trigger Recommendation

Run W004 assessment over RUN-0010 through RUN-0015, then draft the overall repo-working assessment.
