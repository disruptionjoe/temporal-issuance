---
artifact_type: exploration
status: complete
exploration_id: E154
governance_role: obligation_discharge
workflow: W000
goal_ref: q_obl_001_quorum_validity_grounding
date: 2026-07-09
claim_refs:
  - TI-C019
depends_on:
  - explorations/E031-nck-category-morphism-definitions-2026-06-22.md
  - explorations/E040-ostrom-witness-theorem-pp3-source-side-2026-06-22.md
  - explorations/E042-sbp-ind-verification-concrete-compat-family-2026-06-22.md
  - tools/q_obl_001_quorum_validity_grounding.py
  - tests/test_q_obl_001_quorum_validity_grounding.py
central_run: RUN-0134
constitutional: false
claim_status_change: none
verdict: Q_GROUNDED_BY_STRATIFICATION__RESIDUE_IS_NON_CONSTRUCTIVENESS_NOT_CIRCULARITY
---

# E154: Q-OBL-001 — Q Grounding Circularity Avoidance

## Purpose

Discharge Q-OBL-001, named in E031 Part V item 5 and III.3 and carried forward by E058
alongside FUNCTOR-OBL-001. The quorum-validity morphism weight

```text
Q(e) = -log(acceptance probability of e)
```

must be definable without circular reference to the shared admissibility predicate it is
meant to measure. E042 noted Q is "better positioned" over a productive option set but did
not discharge the circularity worry.

## The circularity worry (E031 III.3)

Q(e) uses "the fraction of observers that would accept `e` given the current shared
admissibility predicate `A_S`." The worry: acceptance depends on `A_S`, and if `A_S` were
itself Q-weighted, Q would be defined in terms of itself.

## Method and result

`tools/q_obl_001_quorum_validity_grounding.py` builds a five-observer, stage-stratified schema
trace. Each observer's acceptance rule reads only the constraint set `A_{S_n}` and the
candidate morphism — never Q. Findings:

```yaml
non_circularity:
  A_Sn_references_Q: false
  Q_reads_only_history_fixed_A: true
  dependency_is_dag_over_stages: true      # A_{S_n} -> Q(e) -> accept -> A_{S_{n+1}}
  holds: true
valuation:
  codomain: "[0, inf], additive"
  additive_under_independence: true         # -log(p1 p2) = -log p1 - log p2
  sub_additive_under_correlation: true      # bounded positive correction, exhibited
godelian_residue:
  per_realized_morphism_Q_finite: true
  global_option_map_computable: false
obligation_discharged: true
claim_status_change: none
```

**Grounding argument.** The admissibility predicate `A_{S_n}` is a plain set of
already-accepted constraints, produced by prior resolved quorum decisions; it does not
reference Q. `Q(e)` reads that history-fixed `A_{S_n}` and the observers' fixed acceptance
rule. The dependency graph `A_{S_n} -> Q(e) -> accept/reject -> A_{S_{n+1}}` is a DAG over
stages, so Q is defined by **well-founded recursion on the stage order**, not circularly. The
fixture proves this operationally by recomputing `Q(e)` against the frozen `A_{S_n}` and
getting the identical value at every stage.

**Valuation.** `-log` sends the acceptance ratio into `([0, inf], +)`, additive under
independent acceptance events. Under positively-correlated acceptance the composite Q is
strictly smaller than the sum (a bounded sub-additive correction), which the fixture exhibits
rather than hides.

**Godelian residue.** Over a productive (non-enumerable) option set (E042 Theorem 3), Q **per
realized morphism** remains a finite vote ratio — perfectly grounded. Only Q **as a function
over the whole option space** is non-computable. That is non-constructiveness, not
circularity, and it is exactly the property (acceptance over a non-enumerable option set
cannot be pre-committed) that E040/E042 wanted for the Ostrom witness.

## Verdict

Q-OBL-001 is **discharged**: Q is non-circular by stage stratification and is a valid
additive morphism invariant. The only residue is that the global option map is non-computable
in the Godelian regime — which strengthens, rather than threatens, the PP-3 source-side
witness.

## Failure risks / what would reopen this

- If a concrete AC-8 protocol defines the *next* admissibility predicate `A_{S_{n+1}}` as a
  Q-weighted aggregation in a way that folds Q(e) back into `A_{S_n}` at the *same* stage, the
  DAG stratification would break. The discharge holds for any protocol where `A_{S_n}` is
  fixed before `e` is weighed; protocols that violate this must be flagged.

## Claim-ledger effect

TI-C019: unchanged (`formalizing`). Q-OBL-001 marked discharged (grounded by stratification;
residue is non-constructiveness). No status movement.
