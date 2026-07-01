---
artifact_type: exploration
status: active
governance_role: machine_check_result
goal_ref: machine_check_online_issuance_witness
claim_refs:
  - TI-C003
  - TI-C019
  - TI-C020
depends_on:
  - explorations/E055-expressiveness-threshold-fixture-2026-06-24.md
  - explorations/E090-online-issuance-minimal-constructive-witness-2026-06-25.md
  - explorations/E091-online-issuance-verdict-and-formal-object-rewrite-2026-06-25.md
  - tools/online_issuance_witness_checker.py
  - tests/test_online_issuance_witness_checker.py
created: 2026-07-01
constitutional: false
---

# E108: OnlineIssuance Witness Machine Check

## Purpose

Execute the machine-check branch from RUN-0096:

```text
W000 -> machine_check_online_issuance_witness
```

Question:

```text
Can the E090 local-constructive witness schema be encoded in an executable formal calculus?
```

## Checker Scope

This is a small symbolic calculus, not a Lean/Coq proof.

It checks the E090 schema:

```text
Gamma_n forms Code_n, Cand_n, Adm_n, and Enum_n.
Enum_n is a present enumeration attempt.
Diag(Enum_n) is formed against Enum_n.
w_diag : Adm_n(Diag(Enum_n)) is formed.
Iss_n(Gamma_n, Diag(Enum_n), w_diag) = Gamma_{n+1}.
tau_diag records the source trace.
Omega_future is rejected as an internal source object.
```

## Execution

Executed locally:

```text
python tests/test_online_issuance_witness_checker.py
python tools/online_issuance_witness_checker.py --output tests/artifacts/online_issuance_witness_checker_result.json
```

Focused tests:

```text
5/5 passing
```

## Results

```yaml
checker_kind: small_symbolic_calculus
schema_machine_checked: true
proof_assistant_used: false
full_theorem_prover_verification: false
present_enumerator_valid: true
diagonal_candidate_formed: true
diagonal_candidate_not_in_present_enumeration: true
symbolic_for_all_k_separation_recorded: true
witness_formed: true
successor_issued: true
trace_recorded: true
internal_future_oracle_rejected: true
external_platonist_absorber_still_available: true
local_constructive_witness_passes: true
physical_source_issuance_established: false
```

Comparator results:

```yaml
finite_type_context:
  source_issuance_passes: false
  reason: finite candidate pools are pre-enumerable at the prefix

infinite_computable_context:
  source_issuance_passes: false
  reason: fixed grammar or c.e. generator absorbs the trace as search/disclosure

fixed_platonist_oracle_context:
  internal_source_valid: false
  external_absorber_valid: true
  reason: Omega_future represents the whole trace externally but violates the internal gate

local_constructive_context:
  internal_source_valid: true
  source_issuance_passes: true
  reason: present context forms a diagonal admissible successor without forming a completed future oracle
```

## Interpretation

This strengthens E090 in the limited but useful sense:

```text
The local-constructive OnlineIssuance witness schema is executable.
```

The checker validates the internal pattern:

```text
present enumeration -> diagonal candidate -> admissibility witness -> source trace
```

and keeps the main limitation explicit:

```text
External Platonist completion still absorbs the whole trace from outside the local constructive
source class.
```

So the result is not a physical claim and not a metaphysical defeat of block-style completion.
It is a class-relative formal strengthening of `OnlineIssuance^LC`.

## Effect Typing

```yaml
Issue[S]^LC: true
Issue[S]^physical: false
Project[O]: false
Finalize[R]: false
Lose[K]: false
claim_status_change: none
```

## Verdict

```yaml
formal_lc_witness_strengthened: true
claim_status_change: none
```

## Next Gate

The machine-check branch is complete at the small-calculus level. The next governance move is
frontier selection:

```text
W000 -> W010_frontier_selection_after_online_issuance_machine_check
```

That run should decide whether to:

1. upgrade this checker to Lean/Coq/Agda;
2. return to physical adapter preflight under the stricter `OnlineIssuance^LC` gate;
3. pursue another live frontier instead.

## Claim Effects

No claim movement.

```yaml
TI-C003:
  movement: none
  note: >
    The formal object is strengthened by executable small-calculus support, not promoted.

TI-C019:
  movement: none
  note: >
    The local-constructive source residue is strengthened class-relatively.

TI-C020:
  movement: none
  note: >
    No physical source issuance is established.
```
