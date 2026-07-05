---
artifact_type: exploration
status: complete
governance_role: cech_h3_functor_negative_half
workflow: W000
goal_ref: cech_h3_functor_obl_001_negative_half
claim_refs:
  - TI-C012
  - TI-C017
  - TI-C019
depends_on:
  - explorations/E059-cech-h3-ehresmannian-bridge-obligation-discharge-2026-06-24.md
  - explorations/E060-filtered-source-functor-q-obligation-2026-06-24.md
  - explorations/E061-h3-c1-c3-bridge-from-finite-filtered-functor-2026-06-24.md
created: 2026-07-04
central_run: RUN-0128
constitutional: false
claim_status_change: none
---

# E143: Cech H3 Functor Negative Half

## Purpose

Fire the unfired posture-panel route:

```text
W000 -> cech_h3_functor_obl_001_negative_half
```

The target is not to repeat the finite Cech fixture. The target is to make the
larger negative bridge burden executable:

- preserve the finite SBP parity Cech witness as formal residue;
- test whether `Phi_par` can become a total `Compat_G^MLTT -> FiltSh(C)` functor;
- test whether the finite `Z/2` local-system class discharges the intended GU/H3 bridge;
- test whether C3 spacelike/correspondence geometry is derived rather than imported.

## Executable Fixture

Fixture: `tools/cech_h3_functor_negative_half.py`.

Artifact: `tests/artifacts/cech_h3_functor_negative_half_result.json`.

Focused tests: `tests/test_cech_h3_functor_negative_half.py`.

The fixture evaluates five attempts:

1. finite SBP parity subcategory;
2. all-`Compat_G^MLTT` extension without a non-parity rule;
3. preselected H3 comparison theorem;
4. imported C3 geometry;
5. hidden global transition table.

## Result

```yaml
fixture_id: cech_h3_functor_obl_001_negative_half
finite_cech_parity_residue_preserved: true
total_compat_g_mltt_functor_constructed: false
gu_h3_bridge_discharged: false
c3_geometry_derived: false
negative_half_passed: true
path_kill_reaffirmed: finite_filtered_Z2_local_system_as_sufficient_full_GU_H3_or_C3_geometry_bridge
claim_status_change: none
focused_tests: 6 passed
full_suite: pending in RUN-0128 receipt
```

## What Survived

The finite result still matters:

```text
finite SBP parity + C/Compat provenance -> flat Z/2 local-system residue
```

This remains a clean formal residue. The run does not weaken E054/E060.

## What Failed

The larger bridge still fails.

`Phi_par` has cover/localization and parity data, but it has no canonical rule
for non-parity morphisms. A total functor over all of `Compat_G^MLTT` therefore
does not follow from the finite fixture.

The GU/H3 bridge also does not follow. A comparison theorem from the finite
flat `Z/2` class to the intended GU/H3 object is an extra theorem, not an
output of the finite witness.

C3 spacelike/correspondence geometry is likewise not derived. When supplied in
the fixture, it is marked as imported geometry, not source-derived bridge data.

The hidden-global-table case is rejected because it imports completed future
transition data, exactly the absorber the source-side discipline is supposed to
avoid.

## Verdict

```text
The finite Cech parity witness remains formal residue, but the full GU/H3 and
C3 bridge overclaim remains killed.
```

No claim status moves. No public posture changes. No physical source witness is
established.

## Next Pressure

The posture-panel Cech negative-half item is now fired. The next run should not
repeat Landauer, CelExt steps 1-6, or this Cech negative-half fixture.

Next useful move:

```text
W000 -> W010_frontier_selection_after_posture_panel_candidates
```

Minimum contract: rerank after the posture-panel candidates that have now been
executed. If D-FORK pressure remains the highest-value branch, select a
nonduplicative D-FORK variant rather than replaying the old RUN-0050 formal
source fixture.
