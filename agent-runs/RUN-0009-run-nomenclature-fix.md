---
artifact_type: run_record
status: complete
governance_role: terminology_fix
run_id: RUN-0009
trigger: manual_request
workflow: terminology_and_routing_fix
constitutional: false
governance_changes:
  - GCH-0006
---

# RUN-0009: Run Nomenclature Fix

## Decision

Clarify that prior `SIM-*` records were real repo runs and change future accelerated run naming.

## Why This Work Now

Joe correctly flagged that "sim" makes the runs sound fake. They were real runs with real commits and pushed repo state. The misleading part was the prefix, which meant only that the hourly wait was skipped.

## Fixes Applied

- Added `agent-governance/RUN-NOMENCLATURE.md`.
- Updated W000 to load the nomenclature surface.
- Updated closeout and W004 language to prefer real accelerated run terminology.
- Fixed stale steward metrics memory baseline text.
- Added `memory/future-run-queue.md` for deferred cleanup.
- Marked the old daily-review naming question as superseded.
- Routed the next five runs to ordinary `RUN-0010` through `RUN-0014` IDs.

## Deferred

Historical `SIM-*` files and commits were not renamed. They are already published and should remain stable unless confusion persists.

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
daily_review_updated_if_needed: true
governance_changes_logged_if_any: true
metrics_updated: true
vsm_map_checked: not_applicable
checks_run_or_skipped_with_reason: true
commit_pushed: true_after_this_commit
```

## Next Trigger Recommendation

Run RUN-0010 through W000 as the first of five real manual accelerated thin-trigger cycles.
