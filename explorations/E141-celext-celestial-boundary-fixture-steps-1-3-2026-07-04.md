---
artifact_type: exploration
status: complete
governance_role: celestial_boundary_fixture
workflow: W000
goal_ref: celext_celestial_boundary_fixture_steps_1_3
claim_refs:
  - TI-C013
  - TI-C014
  - TI-C015
  - TI-C016
depends_on:
  - explorations/E013-celestial-boundary-physics-bridge.md
  - agent-runs/RUN-0034-celestial-boundary-physics-bridge.md
  - agent-runs/RUN-0036-cetext-witness-obligations.md
  - tools/celext_celestial_boundary_fixture.py
  - tests/test_celext_celestial_boundary_fixture.py
created: 2026-07-04
central_run: RUN-0126
constitutional: false
claim_status_change: none
---

# E141: CelExt Celestial Boundary Fixture, Steps 1-3

## Purpose

Fire the second unfired posture-panel candidate preserved after RUN-0125:

```text
W000 -> celext_celestial_boundary_fixture_steps_1_3
```

This is the bounded first half of the CelExt fixture suite proposed in E013. It tests whether the
repo can instantiate a minimal internal CelExt category fragment before attempting BMS
functoriality, source-side `Q_f`, ICO' pressure, or absorber checks.

## Claim Discipline

This run does not claim:

- Temporal Issuance derives BMS.
- Temporal Issuance derives celestial holography.
- Temporal Issuance derives physics.
- `Q_f` has been defined source-side.
- CelExt is independent of celestial S-matrix or radiative phase-space data.

The strongest possible positive result is limited:

```text
CelExt steps 1-3 pass as a toy internal category fragment:
typed boundary object, admissible boundary morphism, and additive composition.
```

## Executable Fixture

Fixture: `tools/celext_celestial_boundary_fixture.py`.

Artifact: `tests/artifacts/celext_celestial_boundary_result.json`.

Focused tests: `tests/test_celext_celestial_boundary_fixture.py`.

The fixture instantiates:

1. boundary source objects `B_q` on `S2` with integer soft-charge labels;
2. boundary insertions whose declared soft-charge shift matches the target sector;
3. composition of two admissible insertions, where the composite shift is additive.

It rejects three controls:

- target charge mismatch;
- importing bulk S-matrix data;
- nonadditive composition.

## Result

```yaml
step_1_typed_boundary_object: true
step_2_admissible_boundary_morphism: true
step_3_additive_composition: true
bulk_import_control_rejected: true
BMS_functoriality_tested: false
source_side_Q_f_tested: false
ICO_prime_tested: false
absorber_tested: false
physics_derived_from_TI: false
claim_status_change: none
verdict: celext_steps_1_3_pass_as_internal_toy_category_fragment
```

## What Collapsed

Nothing major collapsed. This was a construction test, not a kill run. The controls block the
most obvious overclaim: a target-side charge mismatch, bulk S-matrix import, or nonadditive
composition cannot pass as a source-side CelExt step-1-to-3 fixture.

## What Survived

The first half of the E013 fixture suite survives as executable scaffolding. CelExt can be
represented internally enough to carry typed boundary sectors, admissible insertions, and
additive composition without immediately importing bulk data.

## What Was Not Tested

The live hard parts remain untouched:

- whether BMS acts functorially on this fragment;
- whether `Q_f` can be determined source-side rather than imported;
- whether ICO' still classifies the route as target import, insufficient source data, or
  bookkeeping;
- whether the whole construction is merely celestial S-matrix relabeling.

## Verdict

The honest verdict is narrow positive:

```text
CelExt steps 1-3 are executable as an internal toy category fragment.
```

This earns the right to run steps 4-6. It does not move TI-C013/TI-C016, does not reopen
TI-C020, and does not change public posture.

## Next Exact Test

Run the second half of the CelExt fixture suite:

```text
W000 -> celext_celestial_boundary_fixture_steps_4_6
```

Minimum contract:

1. test a supertranslation-like action for functoriality over objects, morphisms, and composition;
2. test whether a `Q_f`-like charge is determined from boundary-source data without a bulk
   Hamiltonian or S-matrix;
3. run the absorber check: if the construction is only celestial S-matrix relabeling, mark the
   route absorbed.

## Validation

```powershell
python tests\test_celext_celestial_boundary_fixture.py
python tools\celext_celestial_boundary_fixture.py
```

Both passed during RUN-0126.

Full suite:

```powershell
python -m unittest discover -s tests -p test_*.py
```

Result: 81 passed.
