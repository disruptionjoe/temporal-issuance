---
artifact_type: exploration
status: active
governance_role: lean_internal_predicate_syntax
goal_ref: internal_predicate_syntax_for_admissibility
claim_refs:
  - TI-C003
  - TI-C019
  - TI-C020
depends_on:
  - explorations/E127-online-issuance-lc-ce-tier-comparator-2026-07-02.md
  - formal/lean/OnlineIssuance/Admissibility.lean
  - formal/lean/OnlineIssuance/InternalPredicateSyntax.lean
created: 2026-07-02
central_run: RUN-20260702-072-progress-fanout-hourly
constitutional: false
claim_status_change: none
---

# E128: Internal Predicate Syntax For Admissibility

## Purpose

Execute the direct trigger left by E127:

```text
W000 -> internal_predicate_syntax_for_admissibility
```

E121 / `Admissibility.lean` proved a useful concrete predicate result, but the
predicate `AdmDef` was still a meta-level Lean predicate:

```lean
Ctx -> Candidate -> Prop
```

This run adds an object-language layer:

```text
formal/lean/OnlineIssuance/InternalPredicateSyntax.lean
```

The goal is not a full Godel numbering or computability theory. The goal is a
bounded internal syntax that can carry admissibility as formed predicate code,
prove a self-application/witness result, and record the exact obstruction to a
universal acceptance reading.

## Model Boundary

Internal syntax:

```lean
inductive PredCode where
  | acceptAll
  | formedBySucc
  | selfQuote
  | and (left right : PredCode)
```

Interpretation:

```lean
def PredCode.Accepts (p : PredCode) (Gamma : Ctx) (c : Candidate) : Prop
```

Predicate objects:

```lean
structure InternalPredicate where
  code : PredCode
  formedAt : Nat
```

What this captures:

- predicate code as an internal finite object;
- prefix presence of a predicate object;
- quotation of predicate code as a candidate;
- acceptance by structural interpretation of the code;
- witness construction from internal-code acceptance;
- an internal guard that rejects overbroad universal acceptance.

What it does not capture:

- arithmetic coding of arbitrary Lean syntax;
- recursive-function theory;
- a universal machine or s-m-n;
- a full Godel fixed-point theorem;
- defeat of external Platonist completion;
- physical source issuance.

## Theorem Inventory

| Artifact | Content | Label |
| --- | --- | --- |
| `PredCode` | finite object-language predicate syntax | MODEL |
| `PredCode.render` | stable quote name for predicate code | MODEL |
| `PredCode.Accepts` | structural interpretation of predicate code | MODEL |
| `PredCode.quote` | quote a predicate code as a successor candidate | MODEL |
| `InternalPredicate` | formed predicate object with code and stage | MODEL |
| `InternalAdmDerived` | present predicate + acceptance + Core witness shape | MODEL |
| `InternalAdmDerived.toAdmWitness` | explicit bridge back to Core's `AdmWitness` | DERIVED |
| `internal_witness_from_acceptance` | present accepting predicate yields witness term | DERIVED |
| `issue_lc_from_internal_admissibility` | diagonal bundle plus internal acceptance yields `IssueLC` | DERIVED |
| `selfQuote_accepts_own_quote` | self-quote code accepts its own quote | DERIVED |
| `selfQuote_internal_witness` | self-quote acceptance yields internal admissibility witness | DERIVED |
| `formedBySucc_rejects_future` | internal guard rejects future-stamped candidate | DERIVED |
| `no_universal_internal_acceptance` | not every internal code accepts every candidate | OBSTRUCTION-PROVED |
| `boundedAdmCode_accepts_own_quote` | compact bounded admissibility code accepts its own quote | DERIVED |

## Result

```yaml
internal_predicate_syntax_complete: true
lean_module_added: formal/lean/OnlineIssuance/InternalPredicateSyntax.lean
predicate_codes_modeled: true
predicate_objects_formed: true
self_application_witness: bounded
universal_acceptance_refuted: true
full_godel_coding_modeled: false
external_platonist_completion_defeated: false
physical_source_issuance_established: false
TI_C020_reopened: false
claim_status_change: none
```

## Interpretation

This closes the specific E127 caveat that admissibility had only been modeled
as a meta-level predicate. The new object-language syntax can state and verify
bounded internal predicate acceptance.

The positive result is intentionally narrow:

```text
selfQuote accepts quote(selfQuote)
```

and the acceptance produces a witness through `InternalAdmDerived`. This is
internal-code witness formation, not a full theorem about arbitrary arithmetic
self-reference.

The obstruction is equally important:

```text
formedBySucc rejects a future-stamped candidate
```

Therefore no universal internal-code theorem can say every predicate accepts
every candidate. The admissibility step remains code-relative and guard-
relative, but it is no longer only meta-level English.

## Claim Effects

No claim movement.

```yaml
TI-C003:
  movement: none
  note: formal object hardening now includes internal predicate-code syntax.
TI-C019:
  movement: none
  note: OnlineIssuance^LC is strengthened as class-relative formal machinery,
    but no promotion is earned.
TI-C020:
  movement: none
  note: physical source issuance remains unestablished and parked; not modeled
    here.
```

## Next Gate

```text
W000 -> enumerator_present_pa_o2_fidelity
```

Reason: the remaining near-formal interface caveat is PA-O2 fidelity. Existing
Lean docs record that `EnumeratorPresent` is weaker than the original proof-
assistant fixture: it checks only `formedAt <= prefixStage`, not registered
context symbol, kind, candidate registration, or totality for the present
prefix.

Secondary:

```text
W000 -> W010_frontier_selection_after_internal_predicate_syntax
```

Use this if the steward should re-rank rather than continue interface
hardening.
