---
artifact_type: exploration
status: active
governance_role: lean_derivation_swing
goal_ref: online_issuance_lc_derivation_swing
claim_refs:
  - TI-C003
  - TI-C019
  - TI-C020
depends_on:
  - explorations/E120-online-issuance-lc-lean-core-encoding-2026-07-02.md
  - explorations/E118-online-issuance-lc-theorem-prover-preflight-2026-07-01.md
  - explorations/E117-online-issuance-lc-hostile-review-packet-2026-07-01.md
  - formal/lean/OnlineIssuance/Core.lean
  - formal/lean/OnlineIssuance/Diagonal.lean
  - formal/lean/OnlineIssuance/Admissibility.lean
  - formal/lean/OnlineIssuance/Comparator.lean
created: 2026-07-02
approved_by: joe
constitutional: false
---

# E121: OnlineIssuance LC Derivation Swing (G1/G2/G3)

## Purpose

Attack the three remaining substantive targets from E120's next-gate list, inside the
Lean 4.31.0 core encoding (no mathlib), with hostile verification of every result:

- **G1 — derive diagonal productivity.** Construct an actual diagonal candidate against a
  present enumerator and PROVE `notEnumerated`, instead of assuming `DiagonalFormed`.
- **G2 — derive self-encoding admissibility.** Give a concrete admissibility predicate and
  prove the witness for the diagonal candidate is constructible at the successor stage,
  instead of assuming `AdmWitness`.
- **G3 — tier-3 computable comparator.** Choose a precise computability model and prove (or
  honestly bound) the diagonal-escape statement against internally-definable stage-indexed
  grammars, not just one finite enumerator. Choosing the model was part of the swing.

Hard rules in force throughout: no `sorry`, no `axiom` declarations; assumptions that cannot
be discharged stay as visible hypothesis parameters; every theorem audited to depend on at
most `propext` / `Classical.choice` / `Quot.sound`; "derived" means derived — a design that
merely relocates the assumption gets labeled ASSUMED-RELOCATED by the verifier, not DERIVED.
Core.lean stayed frozen as the pass-one interface (verified byte-identical to the E120
commit: git blob `e56432c3d4aa6b4dce6223b40af7723e248548a5` = `HEAD:formal/lean/OnlineIssuance/Core.lean`
at commit `c68c840`; SHA-256
`3b1fde43d11e058c3268a3f008fabf8fe0da77b356e3f8a31067b32f4735b2e0`; both hashes recorded in
`formal/lean/Scratch.lean`'s header and re-verified after all edits and rebuilds).

## Per-Target Outcomes (hostile-verifier labels)

Two independent hostile lenses were applied to each module: KERNEL+AXIOMS (build + axiom
audit) and RELOCATION+FAITHFULNESS (E117-successor: does the design smuggle the assumption
back in under another name?). Label vocabulary: DERIVED / PARTIALLY-DERIVED /
ASSUMED-RELOCATED / HONEST-OBSTRUCTION.

| Target | Lean module | KERNEL+AXIOMS | RELOCATION+FAITHFULNESS | Headline |
| --- | --- | --- | --- | --- |
| G1 diagonal productivity | `OnlineIssuance.Diagonal` | DERIVED | DERIVED | `diagName_not_mem` — diagonal name not among enumerated values, arbitrary value lists, **zero hypotheses**; `diagonalFormed_derived` inhabits Core's assumed `DiagonalFormed` bundle from the sole hypothesis `EnumeratorPresent` |
| G2 self-encoding admissibility | `OnlineIssuance.Admissibility` | DERIVED | DERIVED | `issue_lc_all_derived` — `IssueLC` for the constructed diagonal and constructed witness from the **single hypothesis** `EnumeratorPresent`; plus `no_universal_self_encoding`, an OBSTRUCTION-PROVED bound on the universal reading |
| G3 computable comparator | `OnlineIssuance.Comparator` | DERIVED | DERIVED | `diagSem_escapes` (T5) — no countable total Nat-indexed family internally indexes its own diagonal — **DERIVED-MODEL-RELATIVE, axiom-free**; per-stage escapes (T4); absorption/no-fixed-point pair (T6, `no_fixed_point_of_absorption`) |

Module-level DERIVED does not mean everything inside is unconditionally derived; the
per-theorem labels below and the "NOT established" section carry the real scope.

Build state after the swing: `lake build` completes clean, 7 jobs (`OnlineIssuance.Core`,
`.Diagonal`, `.Admissibility`, `.Comparator`, root, plus deps). Axiom audit
(`lake env lean Scratch.lean`, cumulative across all 45 G1/G2/G3 declarations): every
declaration within {`propext`, `Classical.choice`, `Quot.sound`}; the G3 semantic tier and
several G2 theorems are fully axiom-free; no `sorryAx`, no `ofReduceBool`, no user axioms.
Grep across all `.lean` sources for `sorry`/`axiom`/`admit`/`native_decide`/`unsafe`/`implemented_by`:
zero declaration-level hits.

## Theorem Inventory

### G1 — `formal/lean/OnlineIssuance/Diagonal.lean`

| Artifact | Content | Label |
| --- | --- | --- |
| `flip_ne` | flip never fixes a character (kernel fact `'a' ≠ 'b'` on concrete `Char`) | DERIVED (axiom-free) |
| `diagChars_length`, `diagChars_getElem` | padded diagonal shape lemmas (length = rows+1; i-th char is flip of row i's i-th char) | DERIVED |
| `diagChars_ne`, `diagChars_not_mem` | Cantor escape at row i's own index (length-mismatch fallback); diagonal row not in the row list | DERIVED |
| `diagName_toList`, `diagName_length`, `diagName_ne_empty` | string-lift shape lemmas; nonempty **unconditionally** via padding | DERIVED |
| `diagName_not_mem` | **G1 headline**: diagonal name not among enumerated values, arbitrary value lists, zero hypotheses | DERIVED |
| `diagonalFormed_derived` | Core's assumed `DiagonalFormed` bundle inhabited for `diagCandidate`, sole hypothesis `EnumeratorPresent` | DERIVED |
| `issue_lc_from_derived_diagonal` | `IssueLC` from {`EnumeratorPresent`, `AdmWitness`} — diagonal leg derived, admissibility leg still ASSUMED-visible (G2's target) | DERIVED (diagonal leg) |
| `registerDiagonal_stage`, `registerDiagonal_registers` | successor-context registration via `Ctx.succWith` (fixture PA-O6 shape) | DERIVED |
| `diagonalFormedAtPrefix_derived` | fixture-reading bundle (`formed_at = n`), sole hypothesis `EnumeratorPresent` (dual stage-stamp coverage) | DERIVED |
| `len_le_maxLen`, `freshName_length`, `freshName_not_mem` | length-escape fresh name (cardinality route — explicitly NOT the diagonal; kept for G3 reuse) | DERIVED-FINITE-FRESHNESS |

Fidelity note (recorded in the module docstring and as an addendum in E120): Core's
`EnumeratorPresent` (`e.formedAt ≤ Γ.prefixStage`) is **strictly weaker** than fixture PA-O2,
which additionally requires enumerator/candidate symbol registration and the totality claim.
The weakening cannot hide the diagonal assumption: `diagName_not_mem` is hypothesis-free, and
`EnumeratorPresent` occurs only on the antecedent side of `diagonalFormed_derived` — any
PA-O2-faithful strengthening strengthens the antecedent and the derivation goes through
verbatim. Strengthening is deferred to a later pass; Core.lean stays frozen.

### G2 — `formal/lean/OnlineIssuance/Admissibility.lean`

| Artifact | Content | Label |
| --- | --- | --- |
| `AdmDef` (+ decidability instance) | concrete decidable admissibility predicate: nonempty name AND `formedAt ≤ prefixStage+1` | DERIVED-FOR-CONCRETE-PREDICATE |
| `adm_of_present`, `enumerated_candidates_admissible` | fairness / anti-gerrymander: present-stage candidates and the stage's own enumerated candidates satisfy `AdmDef` | DERIVED (axiom-free) |
| `adm_not_trivial`, `adm_rejects_future` | non-triviality: empty-named present candidate rejected; beyond-successor stamps rejected for every name | DERIVED |
| `admDef_of_diagonal` | the derived diagonal satisfies `AdmDef` with zero hypotheses (G1's padding pays off) | DERIVED |
| `mkAdmWitnessTerm` / `mkPresentWitness` + `present_witness_prefix_typed` | BOTH witness stage stamps shipped (Core `n+1` / fixture `n`) — divergence resolved by shipping both, not silently picking one | DERIVED |
| `AdmDerived` + `AdmDerived.toAdmWitness` | shape-PLUS-content bundle and the visible bridge into Core's assumed shape-only `AdmWitness`; the `content` field guards against hollow re-inhabitation (the pass-one bundle is rfl,rfl-inhabitable) | DERIVED (axiom-free) |
| `adm_witness_derived`, `adm_witness_diagonal_derived` | witness constructibility at the successor stage; the diagonal's witness with zero hypotheses | DERIVED |
| `issue_lc_derived_witness` | T3 with the admissibility leg derived (diagonal bundle hypothesis-parameterized in this variant) | DERIVED (axiom-free) |
| `diagonal_inadmissible_for_disclosure` | under the disclosure reading of admissibility, the diagonal is provably inadmissible | DERIVED |
| `no_universal_self_encoding` | predicate-free discharge of the `self_encoding_admissibility` rule token is **refutable**; refuter = the repo's own `PriorDisclosure`, not a gerrymandered predicate | OBSTRUCTION-PROVED |
| `Ctx.succWith2`, `issuedCtx`, `issuedCtx_stage`, `issuedCtx_registers` | PA-O6 double registration of candidate and witness in the constructed successor context | DERIVED |
| `issue_lc_all_derived`, `issue_lc_all_derived_full` | **G1+G2 composed headline**: `IssueLC` (and, in the `_full` variant, `AdmDerived` kept visible) from the single hypothesis `EnumeratorPresent` | DERIVED |

### G3 — `formal/lean/OnlineIssuance/Comparator.lean`

Computability model chosen (this choice was part of the gate): **countable total
Nat-indexed families** — stage-indexed grammars `Nat → List String` at the name tier, and
total families `F : Nat → Nat → Bool` at the semantic tier. Cantor diagonalization is carried
out inside core Lean against these. See the model-boundary paragraph below — it is a
citation obligation, not a footnote.

| Artifact | Content | Label |
| --- | --- | --- |
| `stage_fresh_escape` (T4), `stage_diag_escape` | against every stage grammar `g` and stage `n`, `freshName (g n)` / the headline `diagName` construction is not disclosed at stage `n` | DERIVED |
| `freshName_eq_allAName` | `freshName vs` is the all-'a' name of length `maxLen vs + 1` | DERIVED |
| `fresh_diagonal_absorbed` (T7), `fresh_diagonal_grammar_disclosed` | a fixed `absorberFamily` pre-discloses every `freshName` output at the matching stage, against any opponent grammar/stage | DERIVED — **machine-checked for `freshName` ONLY, not the diagonal route** (citation contract in docstring) |
| `fresh_family_disclosure` | positive universal form of T7: every `freshName` output is family-disclosed by the fixed absorber | DERIVED |
| `no_whole_family_name_escape` (T8) | no input escapes the whole fixed `absorberFamily` via `freshName` — a **double-negation restatement of T7 with no independent mathematical content**; cite `fresh_family_disclosure` or T7 instead | OBSTRUCTION-PROVED-FOR-THE-CONSTRUCTION |
| `diagSem_ne_at_own_index` | extensional diagonal disagrees with family member i at input i | DERIVED (axiom-free) |
| `diagSem_escapes` (T5) | no countable total Nat-indexed family internally indexes its own diagonal | **DERIVED-MODEL-RELATIVE** (axiom-free) — label must never be shortened to DERIVED |
| `diag_absorbed_by_extension` (T6), `extension_preserves` | a fixed extension of F internally indexes F's diagonal and still indexes every member of F (absorption existential) | DERIVED (axiom-free) |
| `no_fixed_point_of_absorption` | the extended family has its own escaping diagonal; absorption never closes | DERIVED (axiom-free) |

**T5 model-boundary paragraph (citation contract — must travel with every citation of
`diagSem_escapes`):** T5 is proved for **total Nat-indexed families of total Boolean
functions**. This is NOT recursive-function theory. It does not model partial computable
functions, does not have an s-m-n theorem or a universal machine, and does not capture true
c.e. (computably enumerable) generation, where enumeration order and non-termination are
essential. The strict c.e. tier is **OPEN**. In particular, a positive escape theorem at the
c.e. tier would face a classical ceiling (core Lean's classical logic proves the existence
of escapes without providing internally-computable ones); nothing in this module addresses
that. DERIVED-MODEL-RELATIVE means exactly: derived, relative to this stated model, and the
statement makes no claim beyond it.

## What Is Established

- **G1.** Diagonal productivity at the finite tier is DERIVED, not assumed: a concrete
  padded-Cantor construction whose non-enumeration theorem (`diagName_not_mem`) has zero
  hypotheses, bridged into Core's `DiagonalFormed` bundle from `EnumeratorPresent` alone.
  E117's "productivity obligation not closed" objection is closed at this tier.
- **G2.** Self-encoding admissibility is DERIVED for the concrete predicate `AdmDef`,
  including the successor-stage witness for the diagonal, with fairness and non-triviality
  theorems guarding against gerrymandering, and with the universal reading honestly
  refuted (`no_universal_self_encoding`).
- **Composed assumption surface after G1+G2:** `IssueLC` is reachable from the single
  hypothesis `EnumeratorPresent` (`issue_lc_all_derived`, verified by signature). The E120
  pass-one theorem needed both `DiagonalFormed` and `AdmWitness` assumed; both are now
  constructed.
- **G3.** A precise computability model was chosen and the diagonal-escape / absorption
  dialectic is machine-checked inside it: per-stage escape against every stage grammar (T4),
  the semantic diagonal escape (T5, axiom-free), absorption of any fixed construction by a
  fixed larger family (T6/T7), and the no-fixed-point theorem that absorption never closes.
- All of the above passes the kernel axiom audit ({`propext`, `Classical.choice`,
  `Quot.sound`} ceiling; semantic tier axiom-free) and both hostile lenses, with
  Core.lean and the Python fixture (`tools/proof_assistant_online_issuance_witness.py`)
  byte-untouched.

## What Is NOT Established (merciless)

- **True c.e. generation is not captured.** G3's model is total Nat-indexed families. No
  partial computability, no enumeration-in-time, no halting phenomena, no s-m-n/universal
  machine. The strict c.e. tier of E118's tier-3 target remains **OPEN**, and the classical
  ceiling on any positive c.e.-tier escape is unaddressed. T5's DERIVED-MODEL-RELATIVE label
  is load-bearing.
- **T8 has no independent content.** `no_whole_family_name_escape` is a double-negation
  rewrap of T7 for the `freshName` construction only. Its general form (against a
  `Nat → String` surjection) was not built.
- **The diagonal's name-level absorption is prose-only.** T7/T8/`fresh_family_disclosure`
  are machine-checked for `freshName` ONLY; `diagName`'s name-level absorption rests on the
  prose remark about stage-enumerability of {'a','b'}-strings plus the F-dependent semantic
  T6. Any writeup describing "stipulated constant upgraded to theorem" as covering the
  diagonal route is overclaiming.
- **The external-Platonist completion absorber is untouched.** Deliberately out of scope
  per E117/E118; nothing here defeats or even models it. Same for **physical source
  issuance** (TI-C020's surface): not modeled, not established, still parked.
- **G2 is predicate-relative.** Universal self-encoding admissibility is refuted, not
  proved; the derivation holds for `AdmDef` only. No internal predicate syntax and no
  Gödel-style self-application is modeled — `AdmDef` and the quantified predicate in the
  obstruction theorem are meta-level Lean predicates; the fixture's uninterpreted witness
  proposition string is superseded by interpreted aboutness (`w.proposition = c.name`).
- **Disclosure is name-identity membership.** The extensional objection (same extension,
  different name) is handled only at G3's semantic tier, not in G1/G2's disclosure notion.
- **`flip_ne` rests on concrete `Char`.** The kernel fact `'a' ≠ 'b'`. Abstracting the name
  alphabet forces relabeling; the docstring carries the caveat.
- **`EnumeratorPresent` is weaker than fixture PA-O2** (registration, kind discipline,
  totality claim all missing). Documented with the cannot-hide argument in the Diagonal
  docstring and E120's addendum; strengthening deferred.
- **`freshName` is not the diagonal.** The cardinality-route freshness lemmas are
  quarantined as DERIVED-FINITE-FRESHNESS and must not be cited as diagonal productivity.
- **Grade unchanged in kind:** these are theorems of the executable Lean fixture, class-
  relative in exactly E116/E120's sense. This is assumption-surface shrinkage and honest
  bounding, not promotion.

## Claim Effects

No claim movement.

```yaml
TI-C003:
  movement: none
  note: both E117 open assumptions (diagonal productivity, self-encoding admissibility)
    now DERIVED at the finite tier inside the Lean encoding; IssueLC reachable from
    EnumeratorPresent alone. Scope of the claim unchanged.
TI-C019:
  movement: none
  note: OnlineIssuance^LC residue remains class-relative; the tier-3 comparator result is
    model-relative (total Nat-indexed families), strict c.e. tier open.
TI-C020:
  movement: none
  note: physical source issuance remains unestablished and parked; not modeled here.
```

## Next Gates

Candidates, in preflight order:

1. `online_issuance_lc_ce_tier_comparator` — the strict c.e. tier: adopt a real partial-
   computability model (mathlib `Nat.Partrec` / computability library, accepting the
   `lake exe cache get` cost on Windows) and either prove the escape/absorption pair there
   or write the precise obstruction (including the classical ceiling on positive escapes).
2. `enumerator_present_pa_o2_fidelity` — strengthen `EnumeratorPresent` to full PA-O2
   fidelity (symbol registration, kind discipline, totality claim) in a successor interface
   module, re-deriving `diagonalFormed_derived` against it (expected verbatim, per the
   cannot-hide argument).
3. T8 general form — the `Nat → String` surjection statement, and a machine-checked
   name-level absorption for `diagName` itself (currently prose-only).
4. Internal predicate syntax — model admissibility predicates as internal objects (toward
   Gödel-style self-application) to upgrade `no_universal_self_encoding` from a meta-level
   quantification to an internal one.
5. External-Platonist boundary and physical issuance: unchanged, out of scope, no gate
   proposed here.
