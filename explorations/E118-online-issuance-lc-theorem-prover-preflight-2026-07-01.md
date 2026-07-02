---
artifact_type: exploration
status: active
governance_role: theorem_prover_preflight
goal_ref: online_issuance_lc_theorem_prover_preflight
claim_refs:
  - TI-C003
  - TI-C019
  - TI-C020
depends_on:
  - explorations/E108-online-issuance-witness-machine-check-2026-07-01.md
  - explorations/E115-proof-assistant-online-issuance-witness-2026-07-01.md
  - explorations/E116-online-issuance-core-verdict-bundle-2026-07-01.md
  - explorations/E117-online-issuance-lc-hostile-review-packet-2026-07-01.md
  - tools/proof_assistant_online_issuance_witness.py
  - tests/test_proof_assistant_online_issuance_witness.py
created: 2026-07-01
fan_out_experiment: true
constitutional: false
---

# E118: OnlineIssuance LC Theorem-Prover Preflight

## Purpose

Execute the direct trigger:

```text
W000 -> online_issuance_lc_theorem_prover_preflight
```

Question:

```text
What is the smallest theorem-prover target that can harden the OnlineIssuance^LC local
constructive witness without converting the class-relative result into claim promotion?
```

## Preflight Result

```yaml
preflight_complete: true
selected_target: Lean 4
target_scope: core Lean encoding first, mathlib optional later
local_toolchain_available:
  lake: false
  lean: false
  coqc: false
  coqtop: false
  agda: false
verified_theorem_prover_code_added: false
reason_no_code_added: local theorem-prover executables are absent, so a .lean artifact would be unvalidated
first_encoding_goal: finite_non_disclosure_and_internal_oracle_exclusion
computable_comparator_status: second-pass target
external_platonist_absorber_defeated: false
physical_source_issuance_established: false
TI_C020_reopened: false
claim_status_change: none
next_gate: online_issuance_lc_lean_core_encoding
```

## Target Choice

Lean 4 is the smallest responsible first target for this repo because the current fixture needs:

- inductive datatypes for prefix contexts, symbols, candidates, witnesses, and traces;
- propositions-as-types for dependency and non-disclosure obligations;
- a simple list-membership theorem for the finite prior-disclosure comparator;
- a path toward later mathlib use if the formalization grows into category or computability
  obligations.

Coq and Agda remain viable alternatives, but they are not smaller for the first repo-local
step. The first Lean pass should avoid mathlib and category-theory libraries. The target is not
new category structure; it is the no-hidden-oracle / prior-disclosure boundary.

## Encoding Contract

The first Lean file should model the Python proof-obligation checker at the level where the
current hostile review found a real gap:

```text
Prefix context
  -> present enumerator
  -> diagonal successor
  -> admissibility witness
  -> source trace
  -> internal future-oracle exclusion
  -> finite prior-disclosure non-theorem
```

Suggested initial Lean surface:

```text
formal/lean/OnlineIssuance/Core.lean
```

Suggested definitions:

```lean
inductive Kind
  | codeSpace
  | candidateType
  | admissibilityPredicate
  | candidate
  | enumerator
  | witness

structure Symbol where
  name : String
  kind : Kind
  formedAt : Nat

structure Ctx where
  prefix : Nat
  symbols : List Symbol
  wellFormed : symbols.all (fun s => s.formedAt <= prefix) = true

structure Enumerator where
  name : String
  formedAt : Nat
  values : List String
  presentAt : formedAt <= 0

structure Candidate where
  name : String
  formedAt : Nat

structure Witness where
  name : String
  proposition : String
  formedAt : Nat

structure SourceTrace where
  source : String
  issued : String
  witness : String
  target : String
```

The exact Lean implementation may improve these names and remove the stringly fields, but the
first pass should keep the object small enough to prove something real.

## Axioms Versus Derived Obligations

The preflight split is:

| Obligation | First Lean treatment | Reason |
| --- | --- | --- |
| Prefix typing | Derived from `Ctx.wellFormed` and successor prefix construction. | This is bookkeeping and should not be axiomatized. |
| Present enumerator | Derived from an `EnumeratorPresent Gamma Enum` predicate. | Mirrors PA-O2. |
| Diagonal successor formation | Axiom or parameter in pass one. | The hostile review says productivity is not closed. Do not pretend it is derived. |
| Diagonal not in present enumeration | Axiom carried by the diagonal-formation parameter. | Needed for the first finite non-disclosure theorem. |
| Admissibility witness | Axiom or parameter in pass one. | Self-encoding admissibility is not yet proved. |
| Source trace | Derived once candidate and witness are supplied. | Trace shape is structural. |
| Internal future-oracle exclusion | Derived by omitting any completed-future-oracle constructor from internal source objects, or by proving forbidden kinds cannot satisfy `InternalSource`. | This should be type-level discipline, not a handwave. |
| Finite comparator failure | Derived from diagonal non-membership in the present enumerator. | First real theorem target. |
| Computable comparator failure | Deferred. | Requires a careful model of computable grammars / c.e. generation. |
| External Platonist completion | Not a Lean theorem target. | It remains an external absorber boundary, not an internal contradiction. |
| Physical source issuance | Not modeled. | TI-C020 stays parked. |

## First Theorem Targets

### T1: Finite Prior-Disclosure Failure

Attempt:

```lean
theorem finite_non_disclosure
  (hDiag : diag.name ∉ enum.values) :
  ¬ PriorDisclosure enum diag
```

Interpretation:

```text
If prior disclosure is defined as membership in the present prefix enumerator, then the
diagonal candidate is not prior-prefix disclosure.
```

This is meaningful but narrow. It does not defeat computable fixed grammars, external
completion, or physical fixed-source absorbers.

### T2: Internal Future-Oracle Invalidity

Attempt:

```lean
theorem no_internal_completed_future_oracle :
  ¬ InternalSourceObject CompletedFutureOracle
```

Interpretation:

```text
The local constructive source class has no internal completed-future-oracle object. This
preserves the class boundary E108/E115 already checked in Python.
```

This theorem must be a result of the internal object type or predicate, not merely an English
restriction.

### T3: IssueLC Construction

Attempt:

```lean
theorem issue_lc_from_diagonal_witness
  (hDiag : DiagonalFormed Gamma enum diag)
  (hAdm : AdmWitness Gamma diag witness) :
  IssueLC Gamma diag witness
```

Interpretation:

```text
Given the deliberately stated formation assumptions, the source trace can be typed as
Issue[S]^LC.
```

This theorem is useful only if the assumptions remain visible in the theorem statement.

## Non-Disclosure Attempt Boundary

The non-disclosure theorem should be attempted in three tiers:

1. Finite prior disclosure: prove in the first Lean pass.
2. Internal fixed oracle: prove exclusion in the first Lean pass if the object language is
   clean enough.
3. Infinite computable grammar: defer until the repo chooses a precise computability model.

Do not compress these into a single theorem. That would hide the exact objection E117 surfaced:
the diagonal/productivity and self-encoding assumptions are not yet derived.

## Claim Effects

No claim movement.

```yaml
TI-C003:
  movement: none
  note: >
    The formal object now has a theorem-prover target contract, not verified theorem-prover
    code.

TI-C019:
  movement: none
  note: >
    The OnlineIssuance^LC residue remains class-relative. The first Lean target can harden the
    finite non-disclosure and internal-oracle boundaries only.

TI-C020:
  movement: none
  note: >
    Physical source issuance remains unestablished and parked.
```

## Next Gate

Immediate next route:

```text
W000 -> online_issuance_lc_lean_core_encoding
```

Required:

1. Provide a Lean 4 toolchain (`lean` / `lake`) in the execution environment.
2. Add a minimal, validated Lean file for the core encoding.
3. Prove `finite_non_disclosure` and internal future-oracle exclusion.
4. Keep diagonal productivity and self-encoding admissibility explicit as assumptions if they
   are not derived.
5. Do not model physical source issuance or reopen TI-C020.
6. Return with no claim movement unless the repo-local promotion process is explicitly invoked.
