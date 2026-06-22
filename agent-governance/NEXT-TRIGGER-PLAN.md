---
artifact_type: trigger_plan
status: active
governance_role: next_trigger_state
constitutional: false
updated_by_run: RUN-0031 (W009 heterodox bridge incubator)
---

# Next Trigger Plan

## Current State

RUN-0030 (W007) and RUN-0031 (W009) complete. The repo has completed a full steelman and
heterodox bridge incubation pass against the post-BDO/ICO state.

Key findings from RUN-0030/RUN-0031:
- 62 personas identified 5 constructive routes not yet tried
- W009 incubation produced 9 bridge lemmas (BL-001 through BL-009)
- BL-003 SURVIVES (soft charges != p^mu: established physics)
- BL-007 is the critical open bridge lemma (requires BMS action on ExtCat)
- BL-004 (holonomy) is the mechanism that most cleanly evades BDO/ICO
- Two new speculative claims added: TI-C012 (holonomy), TI-C013 (BMS soft charge)
- No new path kills (no lemma killed with a precise obstruction in Phase 6)

## Formal Residue (Surviving)

The following formal results survive and are publishable without the physical mass-energy
interpretation:

1. **History-class nontriviality of F** (BDO, RUN-0028): a functor can map parallel
   extensions to distinct on-shell sectors. Absorbed by gauge/topological bookkeeping but
   a coherent formal structure.
2. **Preorder-from-extension** (RUN-0025): morphism-level `Ext_S` invariants exceed the
   induced preorder `<=_S`. Extension categories carry non-order structure.
3. **BDO lemma** (RUN-0028): proven result in Poincare-invariant Lorentzian field theory.
4. **ICO theorem** (RUN-0029): proven obstruction for any selection mechanism in any
   momentum-underdetermining Lorentzian target.
5. **E008 conditional theorem** (RUN-0026, E008): formally valid; antecedent permanently
   obstructed by BDO and ICO in the current control case; vacuously satisfied.

## Current Recommendation

**Primary: W000 -> W008 Category G (BMS Soft Charges / Asymptotic Symmetry)**

This is the highest expected-value next move because:
- BL-003 is already established (Q_f != p^mu is settled physics)
- BL-001 (BMS action on ExtCat) is the only blocking definition needed
- A definition attempt is a concrete, bounded task
- Resolution directly determines whether Category G survives or closes definitively

Specific task: Attempt to define a BMS group action on `ExtCat` morphisms. Check whether
the action is compatible with the admissibility rule (BMS transformations map admissible
extensions to admissible extensions). If yes, proceed to BL-007. If no, record as new BMS-
level obstruction and close Category G.

**Secondary: Formal residue documentation (Option A)**

Publish BDO lemma, ICO theorem, preorder-from-extension, and E008 conditional theorem as
a standalone mathematics paper. This is independent of bridge questions and is a publishable
result as it stands. Run in parallel with W008 Category G, not instead of it.

**Tertiary: Holonomy computation (TM-A from RUN-0031)**

Formalize TM-A (minimal holonomy model). Compute curvature of the `Ext_S` connection for
the minimal example. A nonzero curvature result would give a standalone formal result
supporting TI-C012.

## W009 Bridge Lemma Status

| Bridge Lemma | Status | Next Action |
| --- | --- | --- |
| BL-001 (BMS-covariant ExtCat) | UNKNOWN | Attempt definition |
| BL-002 (Q_f is morphism-level) | UNKNOWN | Depends on BL-001 |
| BL-003 (Q_f != p^mu) | SURVIVES | No action; established physics |
| BL-004 (holonomy nontrivial) | WEAK | Requires reversible extensions + non-flat curvature |
| BL-005 (pi_1(BExtCat) nontrivial) | WEAK | Requires endomorphisms in ExtCat |
| BL-006 (TQFT functor exists) | SURVIVES (existence) | Monoidal structure for interesting properties |
| BL-007 (soft charge is source-side) | UNKNOWN — CRITICAL | BL-001 required first |
| BL-008 (conformal target evades BDO) | WEAK | Operator-state correspondence check |
| BL-009 (quantum path-integral) | UNKNOWN | Action and measure on ExtCat needed |

## W008 Escape Route Status (Updated)

```yaml
BDO (RUN-0028):
  local_minimum_risk: medium
  assumption_used: full-boundary-data LorHist objects
  escape_route_inverted_construction: addressed_by_ICO

ICO (RUN-0029):
  local_minimum_risk: low-medium
  assumptions_used:
    - Poincare-invariant dynamics on fixed (M, eta)
    - standard Lagrangian field theory Hamiltonian
    - classical completion selection
  escape_routes:
    Category_A: non-Poincare / curved spacetime / LQG — NOT YET TRIED
    Category_B: quantum path-integral / superposition — NOT YET TRIED (BL-009 open)
    Category_D: holographic / AdS-CFT / BMS — PARTIALLY ADDRESSED (BL-003 established; BL-007 open)
    Category_E: source-generated metric — NOT YET TRIED
    Category_F: lax functors / oo-functors — NOT YET TRIED
    Category_G: BMS / soft charges — HIGHEST PRIORITY (BL-001 is the blocking step)
    Category_H: 2-category / enriched Ext_S — NOT YET TRIED
  phase_4_anti_local_minimum_gate: NOT_YET_RUN
```

## Prior Route Summary

RUN-0024 completed fixture-based ontology and survivor competition.
RUN-0025 killed direct derivation of `E = mc^2` from generic extension invariants.
RUN-0026 formalized the conditional Lorentzian realization theorem.
RUN-0027 tightened the goal to a minimal nontrivial `F`.
RUN-0028 (automated) constructed a weighted-category kinematic toy `F`.
RUN-0028 (BDO pass) proved the Boundary-Determination Obstruction.
RUN-0029 (ICO) proved the Inverted Construction Obstruction.
RUN-0030 (W007) ran the full 62-persona steelman and Hegelian pass post-BDO/ICO.
RUN-0031 (W009) ran the Heterodox Bridge Incubator against RUN-0030 synthesis.

## Automation Target

Codex hourly automation should point to:

- `workflows/W000-repo-steward-cycle.md`

W000 routes to W008 Category G (BMS soft charge) as the primary next target.
