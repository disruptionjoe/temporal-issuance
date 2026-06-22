---
artifact_type: trigger_plan
status: active
governance_role: next_trigger_state
constitutional: false
updated_by_run: RUN-0037
---

# Next Trigger Plan

## Current State

RUN-0037 completed the holonomy fixture recommended by RUN-0036.

Current verdict:

```yaml
physics_bridge_possible: yes_conditionally
physics_derived_from_current_TI: no
holonomy_fixture_result: formal_positive_bare_derivation_failed
bare_Ext_S_derives_connection: false
transport_enriched_holonomy: true
next_fixture: cech_sheaf_fixture
```

The strongest near-nontrivial witness from RUN-0036, B9 (Holonomy/Gauge), now has a sharper
status. A nontrivial holonomy witness is available for a transport-enriched extension category:

```text
A: ExtCat -> B G
```

But a bare closed loop in `Ext_S` does not determine a `G`-element. The fixture found no minimal
fourth option between:

1. no transition data, so no holonomy is determined;
2. stipulated transport data, so formal holonomy exists but the connection is added;
3. a consistency rule forcing identity product, so holonomy is trivial.

## What Survives

1. Formal extension-category residue (TI-C008).
2. Conditional holonomy residue: transport-enriched `ExtCat` can carry order-invisible holonomy
   (TI-C012, TI-C018 weakened).
3. Conditional new-hypothesis bridge: `CelExt` as independently specified boundary category
   (TI-C016).
4. Cech/sheaf witness route (TI-C017), now the simplest remaining test of whether typed source
   admissibility can determine transition/cocycle data.
5. Absorbed BMS control model: `ExtCat_BMS` as asymptotic radiative phase space (TI-C014).

## Current Recommendation

Primary: Cech/sheaf fixture

```text
W000 -> cech_sheaf_fixture
```

Specify the section-compatibility predicate for `C`-typed extensions on a two-patch cover of
`S^1`. Ask whether the admissibility rule independently determines which Cech cocycles are
allowed, rather than merely accepting a preselected sheaf or transition function.

Success condition: `C`-typed admissibility forces a nontrivial allowed cocycle class or a
nontrivial obstruction class not chosen independently as sheaf data.

Failure condition: every nontrivial cocycle requires stipulating overlap/transition data not
forced by source admissibility. This would weaken TI-C017 and push the program toward formal
residue documentation.

Secondary: formal residue documentation

```text
W000 -> formal_residue_documentation
```

If Joe wants to stop boundary-witness probing, document the formal residue now: preorder-from-
extension, BDO, ICO, conditional realization theorem, history-class nontriviality, and transport-
enriched holonomy.

Tertiary: direct CelExt fixture suite

```text
W000 -> CelExt_fixture_suite
```

Still relevant only if the physics bridge via B8 is pursued directly. It must test boundary
objects, admissible boundary morphisms, composition, BMS functoriality, source-side `Q_f`, and
absorber status.

## Claim State

| Claim | Current status | Route |
| --- | --- | --- |
| TI-C008 | formalizing | Formal residue: extension categories carry non-order invariants. |
| TI-C012 | formalizing | Holonomy is formal residue when a transport functor `A: ExtCat -> B G` is supplied or derived. |
| TI-C013 | formalizing | BMS route conditionally live only through CelExt-style boundary category. |
| TI-C014 | formalizing | Absorbed `ExtCat_BMS` control model. |
| TI-C015 | archived | Current TI primitives do not derive physics under explored tree. |
| TI-C016 | formalizing | Conditional new-hypothesis bridge via independently specified CelExt. |
| TI-C017 | speculative | Cech/sheaf witness; depends on `C`-typed section compatibility specification. |
| TI-C018 | weakened | Bare `Ext_S` does not derive holonomy; transport-enriched `ExtCat` gives formal residue. |

## Automation Target

Codex hourly automation should point to:

- `workflows/W000-repo-steward-cycle.md`

W000 should route to the Cech/sheaf fixture unless Joe explicitly chooses:

- formal residue documentation,
- direct CelExt fixture suite, or
- a pause in physics-bridge/boundary-witness pursuit.
