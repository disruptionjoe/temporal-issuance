---
artifact_type: exploration
status: active
governance_role: quantum_absorber_fixture
run_ref: RUN-0071
claim_refs:
  - TI-C020
  - TI-C001
related:
  - explorations/E075-rsps-record-fidelity-toy-baseline-2026-06-25.md
script:
  - tools/rsps_robustness_sweep.py
result_artifact:
  - tests/artifacts/rsps_robustness_sweep_result.json
---

# E076: RSPS Robustness Sweep

## Purpose

Execute Goal 2 of the five-goal disproof ladder:

> Test whether RSPS pointer-basis selection survives ordinary perturbations or is merely an
> ideal controlled-copy / GHZ artifact.

The sweep perturbs the record channel while staying inside standard fixed-H quantum/decoherence
language. This is an absorber-strengthening test, not evidence for source-side issuance.

## Sweep

Script:

```text
tools/rsps_robustness_sweep.py
```

Command:

```text
python tools/rsps_robustness_sweep.py --output tests/artifacts/rsps_robustness_sweep_result.json
```

Perturbations:

```text
copy reliability: 1.0, 0.95, 0.8, 0.65, 0.55, 0.5
accessible fragments: 0, 1, 2, 4, 8
record overlap: 0.0, 0.2, 0.5, 0.8, 0.95, 1.0
noise flip: 0.0, 0.05, 0.1, 0.2, 0.4, 0.5
varying N: 1, 2, 4, 8, 16
```

Non-orthogonal record overlap is converted into effective binary reliability by the Helstrom
distinguishability formula:

```text
q_overlap = (1 + sqrt(1 - overlap^2)) / 2
```

The full score remains:

```text
F = Stability + accessible Redundancy + Agreement
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

Interpretation:

1. The full RSPS score selects the pointer basis across every tested perturbation.
2. Redundancy-only selection becomes degenerate when accessible records carry no information.
3. No perturbation in this sweep favors a non-pointer basis.
4. This robustness remains inside standard fixed-H quantum/decoherence machinery.

## Important Qualification

This does not mean record fidelity derives the world.

The score contains stability and agreement terms that already encode pointer-basis preference.
The result therefore shows robust basis selection under the chosen RSPS functional, not a
source-side issuance witness.

The honest conclusion is:

```text
RSPS basis selection is not merely a perfect-GHZ artifact in this finite sweep.
But it remains a standard-QM absorber result unless a later fixture finds H-growing/A-growing
residue.
```

## Effect On The Five-Goal Ladder

Goal 1:

```text
baseline pointer selection: PASS
Born-weight derivation: FAIL
```

Goal 2:

```text
robust pointer selection under perturbation: PASS
redundancy-only degeneracy under no-record cases: EXPECTED
```

Goal 3 is now justified:

```text
Attempt a structural Born-weight no-go for record-stability/redundancy functionals.
```

Goal 3 should not claim that every conceivable functional fails. It should target the
specific class:

```text
functionals built from predictability / stability,
environmental redundancy,
decoherence or agreement,
without directly reading diag(rho_S) as a trace-rule input.
```

## Claim Effect

No claim status changes.

`TI-C020` is further pressured because the entire result is compatible with fixed-H quantum
mechanics. `TI-C001` gains only reconstruction-layer vocabulary: stable records select
accessible basis/objectivity structure.
