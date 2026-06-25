---
artifact_type: exploration
status: active
governance_role: quantum_absorber_fixture
run_ref: RUN-0070
claim_refs:
  - TI-C020
  - TI-C001
  - TI-C019
related:
  - explorations/E053-predictive-accessible-orch-or-gu-62-persona-pass-2026-06-23.md
  - explorations/E057-ti-c020-fixed-h-vs-h-growing-six-axis-fixture-2026-06-24.md
  - explorations/E074-stochastic-quantum-willow-entanglement-learning-2026-06-24.md
script:
  - tools/rsps_record_fidelity_toy.py
result_artifact:
  - tests/artifacts/rsps_record_fidelity_toy_result.json
---

# E075: RSPS Record-Fidelity Toy Baseline

## Purpose

Execute Goal 1 of the five-goal disproof ladder:

> Reproduce the Record-Stabilization Pointer Selection (RSPS) toy result before doing more
> synthesis, GU section retrieval, Orch-OR contact, or physical-source speculation.

The test asks two questions:

1. Can a record-fidelity functional select the einselected pointer basis in a standard quantum
   measurement toy model?
2. Does that same functional contain the Born weights?

This is a standard-QM absorber fixture. It does not try to prove Temporal Issuance. It tries to
bound what record-stabilization language can legitimately claim.

## Model

Controlled-copy / GHZ einselection fixture:

```text
|Psi> = a |0>|0..0> + b |1>|1..1>
p0 = |a|^2
p1 = |b|^2
N = 8 environment fragments
```

Candidate system basis is parameterized by `theta`:

```text
theta = 0       pointer / z basis
theta = +/-pi/2 x-like basis
```

The executable fixture computes:

```text
Stability(theta)  = 1 - H2(cos^2(theta / 2))
Redundancy(theta) = I(S_theta : E_1) / H2(p0)
Agreement(theta)  = 1 - |sin(theta)|
F(theta)          = Stability + Redundancy + Agreement
```

The raw Born-weight no-go table separately records:

```text
raw redundancy at pointer basis = N * H2(p0)
raw stability cost at pointer basis = 0
raw agreement cost at pointer basis = 0
diag(rho_S) = (p0, 1-p0)
```

## Result

Command:

```text
python tools/rsps_record_fidelity_toy.py --output tests/artifacts/rsps_record_fidelity_toy_result.json
```

Baseline parameters:

```yaml
p0: 0.7
N: 8
theta_steps: 1801
```

Pointer-basis selection:

```yaml
argmax_theta_rad: 0.0
argmax_theta_deg: 0.0
F_pointer: 3.0
F_x_basis: 0.0
basis_selection_check: PASS
```

Born-weight check at the winning basis:

| p0 | Born weight for branch 0 | H2(p0) | raw redundancy N*H2(p0) | normalized F(pointer) |
|---:|---:|---:|---:|---:|
| 0.3 | 0.3 | 0.8812908992 | 7.0503271938 | 3.0 |
| 0.5 | 0.5 | 1.0 | 8.0 | 3.0 |
| 0.7 | 0.7 | 0.8812908992 | 7.0503271938 | 3.0 |
| 0.9 | 0.9 | 0.4689955936 | 3.7519647487 | 3.0 |

The fidelity functional selects the basis. It does not select the probabilities.

## Boundary Theorem Of The Toy Model

In this controlled-copy fixture:

```text
record fidelity selects pointer structure
record fidelity does not derive Born weights
```

Reason:

1. The normalized fidelity score is constant at the winning pointer basis across branch weights.
2. The only raw amplitude-dependent term is redundancy, proportional to `H2(p0)`.
3. `H2(p0)` is symmetric under `p0 <-> 1-p0`; it cannot distinguish `p0 = 0.3` from `p0 = 0.7`.
4. `H2(p0)` is maximal at `p0 = 0.5`, so its sensitivity is entropy-like, not branch-weight-like.
5. The actual Born weights live in `diag(rho_S) = (p0, 1-p0)`, not in `F`.

Therefore no monotone function of this record-fidelity score can recover the Born weights.

## Surviving RSPS Claim

Keep:

```text
Record stabilization / redundancy can select the accessible pointer basis.
Observer-accessible objectivity is record-structured.
Measurement finality can be described as stable redundant record formation.
```

Drop or kill for this fixture:

```text
A single record-fidelity functional derives both basis and Born probabilities.
```

The honest survivor is:

```text
RSPS = record-stabilization pointer selection.

Basis/objectivity comes from record fidelity.
Weights come from the trace rule or a separate weight module.
```

## Effect On Temporal Issuance

This supports the downstream reconstruction layer (`TI-C001`) and pressures the physical bridge
claim (`TI-C020`):

```text
predictive -> accessible
unsettled compatibility -> stable record basis
observer record finality -> pointer/objectivity selection
```

But it does not establish source-side issuance (`TI-C019`) or physical H-growing/A-growing
structure. Standard fixed-H quantum mechanics already accounts for the toy fixture.

## Disproof Value

This is useful because it blocks an overstrong route:

```text
record fidelity alone -> realized world including probabilities
```

The toy model says:

```text
record fidelity -> basis/objectivity only
Born weights -> external trace-rule ingredient
```

That is a narrowing result. It reduces the chance that Temporal Issuance survives by borrowing
ordinary quantum objectivity language while quietly overclaiming probability derivation.

## Next Goal

Goal 2 should run a robustness sweep:

```text
imperfect copying
partial environment fragments
non-orthogonal records
noise
varying N
```

Success condition:

```text
pointer-basis extremum remains stable across ordinary decoherence perturbations
```

Failure condition:

```text
record-fidelity pointer selection is only an ideal GHZ artifact
```

Either result is useful. A robust result strengthens the fixed-H absorber. A fragile result
narrows RSPS before it contaminates TI claims.
