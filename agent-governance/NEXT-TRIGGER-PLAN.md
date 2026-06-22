---
artifact_type: trigger_plan
status: active
governance_role: next_trigger_state
constitutional: false
updated_by_run: RUN-0034
---

# Next Trigger Plan

## Current State

RUN-0034 completed the celestial-boundary bridge test after the BMS and physics-bridge tree passes.

Current verdict:

```yaml
physics_bridge_possible: yes_conditionally
physics_derived_from_current_TI: no
strongest_bridge: celestial_boundary_ExtCat_to_BMS_soft_charge
bridge_type: conditional_new_hypothesis
```

This does not derive physics from the current Temporal Issuance primitives. It says a bridge is
possible only if `ExtCat` is upgraded or identified with an independently specified celestial
boundary category (`CelExt`) carrying BMS symmetry and boundary Noether charges.

## What Survives

1. Formal extension-category residue.
2. Absorbed BMS control model: `ExtCat_BMS` as asymptotic radiative phase space.
3. Conditional new-hypothesis bridge: `CelExt` as independently specified celestial boundary category.

## Current Recommendation

Primary, if the physics bridge continues:

```text
W000 -> CelExt fixture suite
```

Run:

1. object fixture: one boundary sector on `S^2` with a soft-charge label;
2. morphism fixture: one admissible boundary insertion changing the charge sector;
3. composition fixture: two insertions whose composed charge shift is additive;
4. BMS functoriality fixture: supertranslation acts functorially on morphisms and composition;
5. source-side `Q_f` fixture: decide whether `Q_f` is computed without invoking a bulk Hamiltonian;
6. absorber fixture: decide whether the construction is merely celestial S-matrix relabeling.

Secondary, if Joe wants the formal residue first:

```text
W000 -> formal residue documentation
```

## Claim State

| Claim | Current status | Route |
| --- | --- | --- |
| TI-C012 | formalizing | Holonomy is formal residue, not independent physics bridge. |
| TI-C013 | formalizing | BMS route conditionally live only through CelExt-style boundary category. |
| TI-C014 | formalizing | Absorbed `ExtCat_BMS` control model. |
| TI-C015 | archived | Current TI primitives do not derive physics under explored tree. |
| TI-C016 | formalizing | Conditional new-hypothesis bridge via independently specified CelExt. |

## Automation Target

Codex hourly automation should point to:

- `workflows/W000-repo-steward-cycle.md`

W000 should route to the `CelExt` fixture suite unless Joe explicitly chooses formal residue
documentation instead.
