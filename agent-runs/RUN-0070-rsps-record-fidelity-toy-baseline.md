---
artifact_type: agent_run
status: complete
run_id: RUN-0070
date: 2026-06-25
workflow_used: W000 -> RSPS_record_fidelity_toy_baseline
trigger: manual_request
claim_refs:
  - TI-C020
  - TI-C001
  - TI-C019
artifacts:
  - explorations/E075-rsps-record-fidelity-toy-baseline-2026-06-25.md
  - tools/rsps_record_fidelity_toy.py
  - tests/artifacts/rsps_record_fidelity_toy_result.json
---

# RUN-0070: RSPS Record-Fidelity Toy Baseline

## Trigger

Joe asked to execute the five-goal disproof ladder. This run executes Goal 1:

```text
Reproduce the RSPS toy baseline before running robustness, no-go, fixed-H absorber, or residue
adjudication goals.
```

## Current Strongest Version

Record-fidelity language is strongest when narrowed:

```text
record stabilization selects pointer basis / accessible objectivity
Born weights remain supplied by the trace rule or a separate module
```

This is useful for Temporal Issuance only as downstream reconstruction/finality vocabulary,
unless a later fixture supplies H-growing/A-growing physical source structure.

## Current Strongest Objection

The whole RSPS layer may be absorbed by standard fixed-H quantum mechanics, decoherence,
einselection, and Quantum Darwinism. Even if basis selection is robust, it may not create any
source-side issuance residue.

## Work Performed

Created executable fixture:

```text
tools/rsps_record_fidelity_toy.py
```

Ran:

```text
python tools/rsps_record_fidelity_toy.py --output tests/artifacts/rsps_record_fidelity_toy_result.json
```

Created result artifact:

```text
tests/artifacts/rsps_record_fidelity_toy_result.json
```

Created exploration write-up:

```text
explorations/E075-rsps-record-fidelity-toy-baseline-2026-06-25.md
```

## Result

Basis selection:

```yaml
p0: 0.7
N: 8
argmax_theta_rad: 0.0
argmax_theta_deg: 0.0
F_pointer: 3.0
F_x_basis: 0.0
basis_selection_check: PASS
```

Born-weight no-go:

```yaml
normalized_F_pointer:
  p0_0_3: 3.0
  p0_0_5: 3.0
  p0_0_7: 3.0
  p0_0_9: 3.0
raw_redundancy:
  p0_0_3: 7.0503271938
  p0_0_5: 8.0
  p0_0_7: 7.0503271938
  p0_0_9: 3.7519647487
verdict: >
  The fidelity functional selects the pointer basis but does not contain the Born weights.
```

## What Collapsed

The overstrong route collapsed:

```text
one record-fidelity functional selects realized structure and derives Born probabilities
```

In the toy model, the weight information is not in `F`.

## What Survived

The modest RSPS route survived:

```text
record fidelity selects pointer basis / objectivity
weights come from diag(rho_S) via the trace rule
```

## What Was Absorbed

The result is fully compatible with standard fixed-H quantum mechanics. It strengthens the
fixed-H absorber for TI-C020 rather than supporting a physical issuance claim.

## What Was Promoted

None.

## Claim Effects

No claim status changed.

`TI-C020` is pressured: quantum record-fidelity language must not be used as source-side
issuance evidence unless a later fixture supplies a growing observable algebra, admissibility
predicate, or construction-space witness.

`TI-C001` is supported only as downstream reconstruction vocabulary.

`TI-C019` is unchanged.

## Path Kill

Recorded:

```text
single_record_fidelity_functional_derives_born_weights_in_controlled_copy_fixture
```

This kill is scoped to the controlled-copy fixture. A general theorem is Goal 3, not claimed
here.

## Next Run

Goal 2:

```text
W000 -> RSPS_robustness_sweep
```

Required:

1. Imperfect copying.
2. Partial environment access.
3. Non-orthogonal environment records.
4. Noise.
5. Varying `N`.

Success condition:

```text
pointer-basis extremum remains stable under ordinary decoherence perturbations
```

Failure condition:

```text
record-fidelity pointer selection is only an ideal GHZ artifact
```

## Closeout Checklist

```yaml
run_record_written: complete
memory_log_updated: complete
memory_summary_checked: complete
claim_ledger_checked: complete
roadmap_checked: complete
next_trigger_plan_updated: complete
path_kills_recorded_if_any: complete
export_queue_updated_if_any: not_applicable
daily_review_updated_if_needed: not_applicable
governance_changes_logged_if_any: not_applicable
metrics_updated: complete
vsm_map_checked: skipped_no_governance_topology_change
checks_run_or_skipped_with_reason: complete_python_fixture_ran
commit_pushed: pending_at_run_record_creation
```
