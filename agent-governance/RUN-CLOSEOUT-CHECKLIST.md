---
artifact_type: run_closeout_checklist
status: active
governance_role: system_3_control
constitutional: false
---

# Run Closeout Checklist

## Purpose

Make each W000 cycle finish cleanly enough that sequential triggers are observable, auditable, and recoverable.

This checklist is a control surface, not a scoring system. It should catch omissions without replacing steward judgment.

## Required Closeout Items

Each W000 cycle should record whether these items were completed, not applicable, or skipped with reason:

```yaml
run_record_written:
memory_log_updated:
memory_summary_checked:
claim_ledger_checked:
roadmap_checked:
next_trigger_plan_updated:
path_kills_recorded_if_any:
export_queue_updated_if_any:
daily_review_updated_if_needed:
governance_changes_logged_if_any:
metrics_updated:
vsm_map_checked:
checks_run_or_skipped_with_reason:
commit_pushed:
```

## Use Rules

- Use this checklist at closeout for W000 cycles and simulated W000 cycles.
- Do not treat every unchecked item as failure. Some items may be not applicable.
- If an item is skipped, record the reason in the run record.
- If the checklist itself creates noise, revise it through the governance-change ledger.
