---
artifact_type: exploration
status: active
governance_role: lean_core_encoding
goal_ref: online_issuance_lc_lean_core_encoding
claim_refs:
  - TI-C003
  - TI-C019
  - TI-C020
depends_on:
  - explorations/E118-online-issuance-lc-theorem-prover-preflight-2026-07-01.md
  - explorations/E117-online-issuance-lc-hostile-review-packet-2026-07-01.md
  - explorations/E116-online-issuance-core-verdict-bundle-2026-07-01.md
  - formal/lean/OnlineIssuance/Core.lean
created: 2026-07-02
approved_by: joe
constitutional: false
---

# E120: OnlineIssuance LC Lean Core Encoding

## Purpose

Execute the immediate direct trigger from `agent-governance/NEXT-TRIGGER-PLAN.md`:

```text
W000 -> online_issuance_lc_lean_core_encoding
```

E118's blocker was `local_toolchain_available: lake: false, lean: false`. That blocker is
removed and the first encoding pass is complete and validated.

## What Was Done

1. **Toolchain provided.** `elan` installed (Windows, official installer); Lean 4.31.0 and
   Lake 5.0.0 verified working. Joe-directed session, 2026-07-02.
2. **Lean package created** at `formal/lean/` (`lakefile.toml`, `lean-toolchain` pinned to
   `leanprover/lean4:v4.31.0`, library root `OnlineIssuance.lean`).
3. **Core encoding written** at `formal/lean/OnlineIssuance/Core.lean` per the E118 encoding
   contract, core Lean only (no mathlib).
4. **Build validated:**

```text
$ lake build
Built OnlineIssuance.Core
Built OnlineIssuance
Build completed successfully (4 jobs).
```

## Theorem Inventory (all machine-checked)

| E118 target | Lean artifact | Status |
| --- | --- | --- |
| T1 finite prior-disclosure failure | `finite_non_disclosure`, `finite_non_disclosure_of_diagonal` | PROVED (from diagonal non-membership hypothesis) |
| T2 internal future-oracle invalidity | `no_internal_completed_future_oracle` | PROVED type-level: `InternalSource` is an inductive predicate with no constructor for `ProposedObject.completedFutureOracle`; the proof is by empty case analysis, not an English restriction |
| T3 Issue[S]^LC construction | `issue_lc_from_diagonal_witness` | PROVED with both formation assumptions (`DiagonalFormed`, `AdmWitness`) explicit in the statement |

Derived-vs-assumed split, exactly as E118 required:

| Obligation | Treatment in pass one |
| --- | --- |
| Prefix typing | DERIVED (`Ctx.wellFormed` field; `Ctx.symbol_in_prefix`; successor construction `Ctx.succWith` proves preservation) |
| Present enumerator | DERIVED (`EnumeratorPresent` predicate, mirrors PA-O2) |
| Diagonal successor formation | ASSUMED (`DiagonalFormed` hypothesis structure — productivity NOT closed, per E117) |
| Diagonal not in present enumeration | ASSUMED (carried in `DiagonalFormed.notEnumerated`) |
| Admissibility witness | ASSUMED (`AdmWitness` hypothesis structure — self-encoding admissibility NOT derived) |
| Source trace | DERIVED (`mkTrace`, `mkTrace_faithful`) |
| Internal future-oracle exclusion | DERIVED type-level (no oracle constructor in the internal object language) |
| Finite comparator failure | DERIVED (T1) |
| Computable comparator failure | DEFERRED (second pass; needs a precise computability model) |
| External Platonist completion | NOT a Lean target (absorber boundary, unchanged) |
| Physical source issuance | NOT modeled (TI-C020 parked) |

## What This Does and Does Not Establish

- Establishes: the E108/E115 Python-checked class boundary and the finite non-disclosure
  comparator now also hold in a typed, kernel-checked encoding; the open assumptions are
  visible in every theorem statement that uses them.
- Does NOT establish: diagonal productivity, self-encoding admissibility, any result against
  computable fixed grammars, external completion, or physical fixed-source absorbers.
- Grade: theorem of the executable Lean fixture, same class-relative scope as E116. This is
  hardening, not promotion.

## Claim Effects

No claim movement.

```yaml
TI-C003:
  movement: none
  note: verified theorem-prover code now exists for the pass-one contract; scope unchanged.
TI-C019:
  movement: none
  note: OnlineIssuance^LC residue remains class-relative.
TI-C020:
  movement: none
  note: physical source issuance remains unestablished and parked.
```

## Next Gate

Candidates, in preflight order:

1. `online_issuance_lc_computable_comparator_model` — choose a precise computability model
   (c.e. generation) and attempt the tier-3 non-disclosure boundary.
2. Attempt to DERIVE either open assumption (diagonal productivity or self-encoding
   admissibility) inside the Lean encoding; success would shrink the assumption surface E117
   flagged.
3. Optional mathlib adoption if either route needs computability or order-theory libraries.
