---
artifact_type: trigger_plan
status: active
governance_role: next_trigger_state
constitutional: false
updated_by_run: RUN-0028 (BDO pass)
---

# Next Trigger Plan

## Current Recommendation

Invoke W000: Repo Steward Cycle. Current W000 recommendation is the **inverted construction**:

```text
Target: construct or refute an Ext_S invariant that selects Lorentzian momentum data
the boundary leaves open.
```

Define `LorHist'` whose objects are momentum-underdetermining (partial or asymptotic
boundary data only). Ask whether an `Ext_S` morphism invariant can fix the `p^mu` data
left open by the boundary, across the `p^mu`-distinct on-shell completions.

## Why

RUN-0028 (BDO pass) proved the Boundary-Determination Obstruction: in the Poincare-invariant
Minkowski control case with objects encoding full boundary/Cauchy data, `p^mu` is an
object-level invariant and a parallel-pair `Ext_S` distinction cannot reach it. Nontriviality
and energy-momentum-relevance are mutually exclusive in that setting.

Exactly one door is left, and it is the genuinely informative one: invert the construction
by relaxing what LorHist objects fix.

## Nontriviality / Kill Test

Inherits the RUN-0027 gate, inverted past BDO:

```text
Take a parallel pair e1, e2 : S => S' with same <=_S, different Ext_S invariant.
Require F(e1), F(e2) to differ in p^mu data that the boundary objects do NOT fix.

PASS  -> source-side Ext_S content reaches energy-momentum; mass-energy bridge resurrects.
FAIL  -> record a precise obstruction; archive the physical interpretation to NULL-SURVIVOR,
         keep only the history-class formal residue.
```

## Hard Guardrails (do not skip)

These are where this path dies if it dies:

- **Covariance**: The momentum-underdetermining object definition must not introduce a
  preferred foliation. "Partial boundary data" must be covariant, not a disguised
  simultaneity surface.
- **No hidden-variable bookkeeping**: If the Ext_S invariant just labels which momentum
  completion is chosen by fiat, it is absorbed and the path is killed.
- **Keep (M, g) fixed**: Do not reconstruct the metric unless the construction forces it.
- **GU last**: BDO is GU-generic (conserved charges are boundary-determined regardless of
  observerse geometry). GU does not rescue. Evaluate GU compatibility only after the
  ordinary Lorentzian construction, if a positive result is found.

## Expected Outputs

- Definition of `LorHist'` and exactly which momentum data its objects leave open
- Candidate `Ext_S` selection invariant, or a precise no-go
- Covariance check (must pass for a live result)
- Hidden-variable check (must pass for a live result)
- Functoriality and order verdict for the inverted F
- Explicit answer: does the inverted F beat `NULL-SURVIVOR` at the energy-momentum rung?
- Claim-ledger updates for TI-C007, TI-C008, TI-C009, TI-C010
- Resurrection or second path-kill recorded in `memory/path-kills.md`
- Closeout checklist, metrics, memory, and next-trigger updates

## Disposition Rule

Treat a clean obstruction as success. If the inverted construction also collapses, the
physical interpretation of Temporal Issuance should be archived to `NULL-SURVIVOR` and the
program narrowed to its formal history-class residue — which is a legitimate, publishable
kill, not a failure of the repo.

## Proposed Subagents

- Repo Steward
- Lorentzian geometer
- Category Error Auditor
- Constructor / hidden-variable skeptic
- Relativity physicist
- NULL-SURVIVOR advocate
- Mathematical Minimalist

## Prior Route Summary

RUN-0024 completed the fixture-based ontology and survivor competition:

```yaml
C_status: weakened_carrier_only
<=_S_status: killed_as_independent_source_primitive
Ext_S_status: formalizing_next_test_target
best_survivor: constraint_extension_primitive
does_best_survivor_beat_NULL_SURVIVOR: not_yet
```

RUN-0025 killed direct derivation of `E = mc^2` from generic extension invariants and added
the category-level order/invariant theorems. RUN-0026 formalized the conditional Lorentzian
realization theorem `F: ExtCat -> LorHist(M, eta, A)` as the positive target. RUN-0027
tightened the goal to a minimal nontrivial `F` with the same-order/different-invariant gate.

RUN-0028 (automated) constructed a weighted-category kinematic toy `F` preserving a source
weight `Q` as proper time — but found `Q` is externally stipulated and absorber-threatened.

RUN-0028 (BDO pass) proved the Boundary-Determination Obstruction, closing the Q-source-audit
route and all boundary-fixing energy-momentum paths. The inverted construction is the one
remaining open door.

## Automation Target

Codex hourly automation should point to:

- `workflows/W000-repo-steward-cycle.md`

W000 may then route to W001, W002, W003, new dynamic workflows, dynamic personas, or
parallelized subagent runs.
