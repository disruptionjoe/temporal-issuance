---
artifact_type: agent_run
status: complete
run_id: RUN-0071
date: 2026-06-25
workflow_used: W000 -> RSPS_robustness_sweep
trigger: manual_request
claim_refs:
  - TI-C020
  - TI-C001
artifacts:
  - explorations/E076-rsps-robustness-sweep-2026-06-25.md
  - tools/rsps_robustness_sweep.py
  - tests/artifacts/rsps_robustness_sweep_result.json
---

# RUN-0071: RSPS Robustness Sweep

## Trigger

Joe asked to execute the five-goal disproof ladder. This run executes Goal 2:

```text
Robustness sweep after the RSPS controlled-copy baseline.
```

## Current Strongest Version

The modest RSPS result survives if pointer-basis selection is stable under ordinary record
perturbations, while Born weights remain external.

## Current Strongest Objection

The robustness may be partly built into the chosen functional because stability and agreement
terms already prefer the pointer basis. Therefore the result strengthens a standard-QM
basis-selection absorber, not a Temporal Issuance source claim.

## Work Performed

Created:

```text
tools/rsps_robustness_sweep.py
```

Ran:

```text
python tools/rsps_robustness_sweep.py --output tests/artifacts/rsps_robustness_sweep_result.json
```

Created:

```text
tests/artifacts/rsps_robustness_sweep_result.json
explorations/E076-rsps-robustness-sweep-2026-06-25.md
```

## Result

```yaml
scenario_count: 28
pointer_wins_full_score_count: 28
full_score_failures: []
redundancy_degenerate_count: 4
redundancy_degenerate_cases:
  - copy_reliability_0.5
  - accessible_fragments_0
  - record_overlap_1.0
  - noise_flip_0.5
```

## What Collapsed

The simple objection that RSPS pointer-basis selection is only an ideal perfect-copy artifact
is weakened for this finite perturbation sweep.

## What Survived

Modest RSPS:

```text
record-fidelity basis selection is robust across ordinary noisy/partial/nonorthogonal record
channels in this toy class
```

## What Was Absorbed

All of this remains standard fixed-H quantum/decoherence structure. It does not supply a
source-side issuance witness.

## What Was Promoted

None.

## Claim Effects

No claim status changed.

## Next Run

Goal 3:

```text
W000 -> general_RSPS_Born_weight_no_go
```

Required:

1. State the functional class precisely.
2. Prove or refute that stability/redundancy/agreement functionals do not determine Born
   weights unless they import `diag(rho_S)` / trace-rule information.
3. Preserve scope: if only a class theorem is available, do not overstate it.

## Closeout Checklist

```yaml
run_record_written: complete
memory_log_updated: complete
memory_summary_checked: complete
claim_ledger_checked: complete
roadmap_checked: complete
next_trigger_plan_updated: complete
path_kills_recorded_if_any: not_applicable
export_queue_updated_if_any: not_applicable
daily_review_updated_if_needed: not_applicable
governance_changes_logged_if_any: not_applicable
metrics_updated: complete
vsm_map_checked: skipped_no_governance_topology_change
checks_run_or_skipped_with_reason: complete_python_fixture_ran
commit_pushed: pending_at_run_record_creation
```
