---
artifact_type: run_record
status: complete
governance_role: accelerated_thin_trigger
run_id: RUN-0013
trigger: manual_accelerated_thin_trigger
workflow: W000 -> definition_repair
constitutional: false
claims_touched:
  - TI-C003
---

# RUN-0013: Definition Repair

## Thin Trigger Route

`AGENTS.md` -> `workflows/W000-repo-steward-cycle.md` -> Repo Steward decision.

## Decision

The steward ran a definition repair pass for `mu`, `kappa_i`, and `G_ij`.

## Why This Work Now

RUN-0012 weakened `IssuanceSystem` and identified measure, cadence, and reconciliation as the main formal blockers. The next highest-learning move was to attempt repair before running another broad assessment.

## Hard Output

Created `FORMAL-DEFINITION-REPAIR.md`.

## Main Findings

- Generic `mu` remains killed. A stricter `lambda_i` candidate may be tested.
- `kappa_i` should be ordinal record-update structure, not clock-rate language.
- `G_ij` should expose reconciliation failures or lag through `Omega_ij`; otherwise it is likely absorbed by existing gluing machinery.
- The next useful test is a toy two-observer patch, not more prose.

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
governance_changes_logged_if_any: not_applicable
metrics_updated: true
vsm_map_checked: true
checks_run_or_skipped_with_reason: true
commit_pushed: true_after_this_commit
```

## Next Trigger Recommendation

RUN-0014 should create the minimal toy-patch test candidates needed to pressure the repaired definitions before W004 assessment.
