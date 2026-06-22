---
artifact_type: trigger_plan
status: active
governance_role: next_trigger_state
constitutional: false
updated_by_run: RUN-0029 (ICO — inverted construction obstruction)
---

# Next Trigger Plan

## Current State

The physical mass-energy bridge interpretation of Temporal Issuance has been archived to
NULL-SURVIVOR following RUN-0029. Two independent obstructions seal the Poincare-invariant
Lorentzian energy-momentum route:

- **BDO (RUN-0028):** With full-boundary-data LorHist objects, `p^mu` is object-level;
  parallel-pair `Ext_S` distinctions cannot reach it. Nontriviality and energy-momentum-
  relevance are mutually exclusive in the Poincare-invariant Minkowski control case.
- **ICO (RUN-0029):** With momentum-underdetermining LorHist' objects, `p^mu` is
  morphism-level, but morphism-level variation is indexed by target-side dynamical physics
  (coupling constants, interaction Hamiltonian, scattering amplitudes, angular distributions),
  not source-side `Ext_S` invariants. Any selection mechanism either imports target physics
  (ICO-1, absorbed), is insufficient to determine `p^mu` (ICO-2, bridge fails), or trivially
  re-encodes the completion choice (ICO-3, bookkeeping). Covariance: PASS. Mechanism: FAIL.

BDO and ICO together cover the full logical space of LorHist object specifications under
the fixed `(M, eta)` guardrail. The inverted construction collapses; no third door exists.

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

The Poincare-invariant Lorentzian energy-momentum route is closed (BDO + ICO). This does
NOT yet mean the bridge is definitively killed — BDO and ICO both carry local-minimum risk
under assumptions that can be relaxed (Poincare symmetry, fixed background, classical
completion, full or partial Cauchy data).

**Option W008 — Bridge-or-definitive-kill with local-minimum escape checking (recommended):**
Invoke `W008-bridge-or-definitive-kill.md`. This workflow enumerates all escape routes from
the current obstructions, attempts each construction, verifies each kill against the
anti-local-minimum gate (N ≥ 3 adversarial skeptics), and only archives the physical
interpretation after all escape routes are exhausted and all kills are confirmed global.

Current escape routes not yet tried (starting point for next W008 invocation):
- Category G: soft theorem / asymptotic symmetry charges (BMS, w_{1+inf}) — highest leverage
  because boundary data does not fix soft charges; this is exactly the gap BDO + ICO exploited
- Category B: quantum path-integral / superposition of completions
- Category A: non-Poincare / curved spacetime / LQG / spin foams
- Category D: holographic / AdS-CFT / asymptotic data
- Others: see W008 escape-route taxonomy

**Option A — Formal residue documentation:**
Document surviving formal results (BDO, ICO, preorder-from-extension, E008) as a publishable
research note. Run this in parallel with W008, not instead of it.

**Option B — Program scope revision:**
Revise the program scope to a non-mass-energy version of Temporal Issuance if W008
exhausts all energy-momentum routes.

**Default: invoke W008 next.** The program should not archive the physical interpretation
solely on the basis of BDO + ICO until the W008 anti-local-minimum gate has been run.

## Disposition Rule (Applied)

A clean obstruction was achieved (ICO, RUN-0029). The physical interpretation is archived
to NULL-SURVIVOR. The formal history-class residue is kept. This is a legitimate,
publishable result — not a failure of the repo.

## Prior Route Summary

RUN-0024 completed fixture-based ontology and survivor competition:

```yaml
C_status: weakened_carrier_only
<=_S_status: killed_as_independent_source_primitive
Ext_S_status: formalizing_next_test_target
best_survivor: constraint_extension_primitive
does_best_survivor_beat_NULL_SURVIVOR: not_yet
```

RUN-0025 killed direct derivation of `E = mc^2` from generic extension invariants and
proved preorder-from-extension and extension-invariant theorems.

RUN-0026 formalized the conditional Lorentzian realization theorem `F: ExtCat -> LorHist(M, eta, A)`.

RUN-0027 tightened the goal to a minimal nontrivial `F` with the same-order/different-invariant gate.

RUN-0028 (automated) constructed a weighted-category kinematic toy `F` preserving `Q` as
proper time — externally stipulated, absorber-threatened.

RUN-0028 (BDO pass) proved the Boundary-Determination Obstruction. Closed the full-boundary-
data energy-momentum route. TI-C009 weakened.

RUN-0029 (ICO) proved the Inverted Construction Obstruction. Closed the
momentum-underdetermining energy-momentum route. Physical interpretation archived to
NULL-SURVIVOR. TI-C007 weakened, TI-C009 archived, TI-C010 archived.

## Automation Target

Codex hourly automation should point to:

- `workflows/W000-repo-steward-cycle.md`

W000 routes to formal residue documentation (Option A) or program scope revision (Option B)
as directed by Joe.
