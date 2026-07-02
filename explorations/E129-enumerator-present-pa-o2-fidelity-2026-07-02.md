---
artifact_type: exploration
status: complete
created: 2026-07-02
run_ref: RUN-0114
claim_refs:
  - TI-C019
  - TI-C003
constitutional: false
---

# E129: Enumerator Present PA-O2 Fidelity

## Purpose

Close the fidelity gap left by RUN-0113: Core's `EnumeratorPresent` interface
was still weaker than the original PA-O2 fixture because it only required the
enumerator's formation stage to be within the context prefix.

RUN-0114 strengthens the Lean interface so `EnumeratorPresent` carries:

1. registered context symbol for the enumerator,
2. kind `enumerator`,
3. candidate registration for enumerated values, and
4. present-prefix totality over candidate symbols.

## Formal Changes

Primary formal artifact:

```text
formal/lean/OnlineIssuance/Core.lean
```

New definitions:

```lean
Ctx.HasExactSymbol
Ctx.HasPresentSymbol
EnumeratorRegistered
EnumeratorValuesRegistered
EnumeratorTotalForPrefix
```

`EnumeratorPresent` is now a proof-bearing structure:

```lean
structure EnumeratorPresent (Γ : Ctx) (e : Enumerator) : Prop where
  formedInPrefix : e.formedAt ≤ Γ.prefixStage
  registered : EnumeratorRegistered Γ e
  valuesRegistered : EnumeratorValuesRegistered Γ e
  prefixTotal : EnumeratorTotalForPrefix Γ e
```

Access theorems added:

```lean
EnumeratorPresent.enumerator_symbol
EnumeratorPresent.value_symbol
EnumeratorPresent.total_for_candidate
```

Downstream adaptation:

```text
formal/lean/OnlineIssuance/Admissibility.lean
```

The `no_universal_self_encoding` obstruction now constructs a PA-O2-faithful
empty enumerator context instead of passing a bare stage inequality.

Provenance cleanup:

```text
formal/lean/OnlineIssuance/Diagonal.lean
```

The old PA-O2 gap note is marked as superseded by RUN-0114.

## Verdict

```yaml
pa_o2_fidelity_closed: true
enumerator_symbol_registration_required: true
enumerator_kind_required: true
enumerated_value_candidate_registration_required: true
present_prefix_totality_required: true
diagonal_escape_uses_pa_o2_assumptions: false
existing_issue_lc_stack_preserved: true
external_platonist_completion_defeated: false
strict_ce_positive_escape_reopened: false
physical_source_issuance_established: false
TI_C020_reopened: false
claim_status_change: none
```

## Interpretation

The Lean interface now matches the PA-O2 burden at the finite present-prefix
level. An enumerator is not merely a timestamped object; it must be registered
as an enumerator symbol in the context, its values must be registered
candidate symbols, and it must certify totality over the context's present
candidate symbols.

The positive diagonal route is not made stronger by hiding assumptions. The
non-enumeration proof still uses only the enumerator's value list:

```text
diagName_not_mem : diagName vs ∉ vs
```

`EnumeratorPresent` remains the explicit antecedent to the derived diagonal
bundle. The stronger PA-O2 interface narrows when the theorem can be invoked;
it does not participate in the diagonal escape proof.

## Scope Limits

- Prefix totality is finite and context-local.
- Candidate registration is by candidate symbol name in the present prefix.
- Extensional disclosure under alternate names remains outside this finite
  name-tier interface.
- The strict c.e. ceiling from E127 is unchanged.
- External Platonist completion remains an absorber boundary, not an internal
  contradiction.
- No physical source issuance is modeled.

## Validation

Passed:

```text
~/.elan/bin/lake.exe build
```

The build rechecked:

- `OnlineIssuance.Core`
- `OnlineIssuance.Diagonal`
- `OnlineIssuance.Admissibility`
- `OnlineIssuance.Comparator`
- `OnlineIssuance.CEComparator`
- `OnlineIssuance.InternalPredicateSyntax`
- aggregate `OnlineIssuance`

## Next Route

```text
W000 -> W010_frontier_selection_after_pa_o2_fidelity
```

Reason: the explicit hardening queue left by E121/E127/E128 is now closed at
the current finite-prefix Lean tier. The next run should re-rank the live
frontier instead of inventing another narrow interface patch.
