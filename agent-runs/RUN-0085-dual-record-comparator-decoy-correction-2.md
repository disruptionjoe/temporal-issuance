---
artifact_type: agent_run
status: complete
run_id: RUN-0085
date: 2026-06-25
workflow_used: implementation_correction
trigger: dual_record_fixture_test_found_equal_score_decoy_leak
claim_refs:
  - TI-C019
  - TI-C020
  - TI-C001
artifacts:
  - explorations/E093-dual-record-comparator-freeze-2026-06-25.md
---

# RUN-0085: Dual-Record Comparator Decoy Correction 2

## Trigger

The Time as Finality fixture still found a B0 escape after RUN-0084.

Cause:

```text
0 -> 5
```

has equal score under the frozen acceptance rule, so B0 accepted it and entered
the rising basin without needing the critical `2 -> 7` bridge.

## Correction

E093 now freezes B0 as:

```text
1 -> 5
3 -> 6
4 -> 6
```

The first decoy can be exposed from state 1 and fail by score, while the other
decoys remain unavailable in the ordinary trapped path.

## Claim Effects

No claim status changed.

## Next Run

Continue:

```text
W000 -> implement_dual_record_adjacent_possible_fixture
```

## Closeout Checklist

```yaml
run_record_written: complete
exploration_corrected: complete
roadmap_update: not_needed_comparator_detail_only
next_trigger_plan_update: complete_same_route
claim_ledger_checked: complete_no_change
checks_run_or_skipped_with_reason: git_diff_check_only_docs_change
commit_pushed: pending_at_run_record_creation
```
