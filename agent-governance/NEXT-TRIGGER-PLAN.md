---
artifact_type: trigger_plan
status: active
governance_role: next_trigger_state
constitutional: false
updated_by_run: RUN-0036
---

# Next Trigger Plan

## Current State

RUN-0036 completed a 12-lens witness-obligation survey of candidate `CelExt` structures.

Current verdict:

```yaml
physics_bridge_possible: yes_conditionally
physics_derived_from_current_TI: no
strongest_bridge: holonomy_witness_B9_conditional_live
bridge_type: conditional_new_hypothesis
cetext_independence_required: true
```

No lens achieved a `live` verdict. Five lenses are `conditional-live` (B1/B5/B8/B9/B12);
six are `bookkeeping` (B2/B3/B4/B7/B10/B11); one is `absorbed` (B6).

The witness-obligation reframing confirms and sharpens the CelExt question: the obstacle
is not conceptual but formal — no lens can independently specify the key structure
(connection, section-compatibility predicate, boundary CFT) from `Ext_S` alone. The
strongest near-nontrivial result is B9 (Holonomy/Gauge), where the holonomy parallel pair
is concretely executable and cleanly evades BDO and ICO.

## What Survives

1. Formal extension-category residue (TI-C008).
2. Absorbed BMS control model: `ExtCat_BMS` as asymptotic radiative phase space (TI-C014).
3. Conditional new-hypothesis bridge: `CelExt` as independently specified celestial boundary
   category (TI-C016).
4. Two new speculative claims: TI-C017 (Čech/sheaf witness), TI-C018 (holonomy witness).
5. Holonomy parallel pair as the strongest near-nontrivial result in the survey (B9).

## Current Recommendation

Primary: holonomy fixture

```text
W000 -> holonomy_fixture
```

Specify the smallest typed constraint system `(C_min, <=_S^min, Ext_S^min)` with:
- at least one closed extension loop `s_0 -> s_1 -> ... -> s_n -> s_0`;
- a composition rule for `Ext_S` that assigns a group element `g ∈ G` to each
  elementary extension;
- check whether the holonomy around any loop is non-trivial (g ≠ e);
- verify that the connection is determined by `Ext_S^min` and not by an imported gauge theory.

Success condition: non-trivial holonomy for at least one loop, with the connection
independently derived from `Ext_S^min`. This would be the first nontrivial CelExt witness
result in the program.

Failure condition: every constraint system that admits a non-trivial holonomy also requires
importing a connection from a target gauge theory. This would absorb TI-C018 and weaken B9
to bookkeeping.

Secondary: CelExt fixture suite (still live from RUN-0034)

```text
W000 -> CelExt_fixture_suite
```

This remains relevant if the physics bridge via B8 is pursued directly. The six-fixture
structure from NEXT-TRIGGER-PLAN (RUN-0034 version) still applies.

Tertiary: Čech/sheaf fixture (new from RUN-0036)

```text
W000 -> cech_sheaf_fixture
```

Specify the section-compatibility predicate for `C`-typed extensions on a two-patch cover
of `S¹`. Ask whether the admissibility rule independently determines which Čech cocycles
are allowed (i.e., which extensions are globally section-consistent). This is a simpler
entry point than the holonomy fixture.

## Claim State

| Claim | Current status | Route |
| --- | --- | --- |
| TI-C008 | formalizing | Formal residue: extension categories carry non-order invariants. |
| TI-C012 | formalizing | Holonomy is formal residue; now extended by TI-C018 with connection-independence condition. |
| TI-C013 | formalizing | BMS route conditionally live only through CelExt-style boundary category. |
| TI-C014 | formalizing | Absorbed `ExtCat_BMS` control model. |
| TI-C015 | archived | Current TI primitives do not derive physics under explored tree. |
| TI-C016 | formalizing | Conditional new-hypothesis bridge via independently specified CelExt. |
| TI-C017 | speculative | Čech/sheaf witness; depends on `C`-typed section compatibility specification. |
| TI-C018 | speculative | Holonomy witness; depends on `Ext_S`-derived connection. |

## Automation Target

Codex hourly automation should point to:

- `workflows/W000-repo-steward-cycle.md`

W000 should route to the holonomy fixture unless Joe explicitly chooses:
- CelExt fixture suite (physics bridge direct route), or
- Čech/sheaf fixture (simpler entry), or
- formal residue documentation.
