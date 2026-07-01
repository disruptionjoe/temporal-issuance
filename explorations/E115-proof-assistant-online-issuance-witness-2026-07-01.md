---
artifact_type: exploration
status: active
governance_role: proof_hardening_result
goal_ref: proof_assistant_online_issuance_witness
claim_refs:
  - TI-C003
  - TI-C019
  - TI-C020
depends_on:
  - explorations/E108-online-issuance-witness-machine-check-2026-07-01.md
  - explorations/E114-oi-lc-assembly-w4-w6-physical-protocol-fixture-2026-07-01.md
  - tools/online_issuance_witness_checker.py
  - tools/proof_assistant_online_issuance_witness.py
  - tests/test_online_issuance_witness_checker.py
  - tests/test_proof_assistant_online_issuance_witness.py
created: 2026-07-01
constitutional: false
---

# E115: Proof-Assistant-Style OnlineIssuance Witness Hardening

## Purpose

Execute the direct trigger from E114:

```text
W000 -> proof_assistant_online_issuance_witness
```

Question:

```text
Can the OnlineIssuance^LC local constructive witness be hardened beyond the small symbolic
calculus while preserving the no-hidden-future-oracle boundary?
```

## Checker Scope

This is a proof-obligation checker, not Lean/Coq/Agda.

It consumes the E108 symbolic witness result and verifies nine explicit typed obligations:

1. prefix typing,
2. present enumerator formation,
3. diagonal dependency,
4. diagonal separation,
5. admissibility-witness dependency,
6. source-trace shape,
7. no hidden future oracle,
8. comparator scope,
9. effect typing.

## Execution

Executed locally:

```text
python -m unittest tests/test_online_issuance_witness_checker.py tests/test_proof_assistant_online_issuance_witness.py
python tools/proof_assistant_online_issuance_witness.py --output tests/artifacts/proof_assistant_online_issuance_witness_result.json
```

Focused tests:

```text
10/10 passing
```

## Results

```yaml
checker_kind: typed_proof_obligation_checker
proof_assistant_used: false
full_theorem_prover_verification: false
strictly_harder_than_small_symbolic_calculus: true
obligation_count: 9
obligations_passed: 9
all_obligations_passed: true
no_hidden_future_oracle_preserved: true
external_platonist_absorber_still_available: true
Issue[S]^LC: true
Issue[S]^physical: false
TI_C020_reopened: false
claim_status_change: none
next_gate: online_issuance_core_verdict_bundle
```

## Interpretation

The E090/E108 local constructive witness is now supported by a stricter proof-object layer.
The checker does not merely look for positive fixture flags; it validates dependency closure,
prefix discipline, diagonal separation, source-trace typing, and the oracle boundary.

This strengthens the formal/local result:

```text
OnlineIssuance^LC has a checked local constructive witness in a typed proof-obligation
calculus.
```

It does not establish:

- physical source issuance,
- a full theorem-prover proof,
- defeat of external Platonist completion,
- claim promotion,
- reopening TI-C020.

## Claim Effects

No claim movement.

```yaml
TI-C003:
  movement: none
  note: >
    The formal object has stricter proof-obligation support, not promotion.

TI-C019:
  movement: none
  note: >
    The class-relative local-constructive source residue is strengthened.

TI-C020:
  movement: none
  note: >
    Physical source issuance remains unestablished and the Assembly physical branch remains absorbed.
```

## Next Gate

The immediate next route is:

```text
W000 -> online_issuance_core_verdict_bundle
```

That bundle should synthesize the OnlineIssuance^LC result, the physical Assembly absorption
result, the external Platonist absorber, and the claim-status boundary into a compact verdict
surface.

