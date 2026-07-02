/-
OnlineIssuance^LC — G3: tier-3 comparator (pass two).

Pass one (`OnlineIssuance.Core`) deferred the infinite-grammar comparator:
"Infinite computable grammar comparator: requires a precise computability
model (c.e. generation); NOT encoded here." Choosing the model IS part of
this gate. This module chooses core-Lean model (a): TWO explicitly separated
levels, both over stage-indexed / Nat-indexed TOTAL families.

THE MODEL (what it does and does not capture):
- Name level: `StageGrammar := Nat → List String` — a stage-indexed generator
  emitting finitely many names per stage. Whole-family disclosure is
  disclosure at SOME stage (`FamilyDisclosure`).
- Semantic level: `SemFamily := Nat → Nat → Bool` — a countable Nat-indexed
  family of TOTAL extensional candidates (sets of naturals as Boolean
  predicates). "Internally definable" means exactly "member of the family"
  (`InternallyIndexed`) — the class relativity is a DEFINITION here, and no
  theorem below quantifies over non-indexed grammars, so the
  external-Platonist absorber boundary is untouched BY CONSTRUCTION.
- Captured: every Nat-indexed total family — a SUPERCLASS of total computable
  grammars on the escape side, so the escape theorems (T4, T5) in particular
  cover all actual total computable enumerations.
- NOT captured: true c.e. (partial) generation. No programs, no partiality,
  no s-m-n / universal machine, no Kleene recursion theorem. The strict c.e.
  tier stays OPEN, with the classical ceiling noted: a positive c.e.-tier
  closure (one computable candidate escaping ALL c.e. sets) is classically
  impossible — the candidate's own singleton/name-set is c.e. — so the honest
  content of that tier is exactly the absorption picture proved here, not a
  stronger escape.
- Mathlib ruled out for this pass: the tier-2 verdict's interesting content
  (absorption) is provable in model (a); a positive c.e.-tier theorem is
  classically impossible anyway; mathlib on this toolchain would buy only
  obstruction statements at real install/pin cost. Revisit only if a later
  gate needs theorems over actual partial-recursive codes.

Design overrides of the G3 design (both deliberate, per plan):
- `mono` DROPPED: stage grammars are plain functions. Cumulativity is not
  load-bearing for any theorem in this module; carrying a provably-unused
  hypothesis invites the decorative-fidelity accusation.
- T8 RELABELED: not "whole-family name-level escape impossible" (a universal
  overclaim) but OBSTRUCTION-PROVED-FOR-THE-CONSTRUCTION — see below.

Status labels (hostile-verifier vocabulary):
- T4 `stage_fresh_escape`: DERIVED (name tier, per-grammar/per-stage).
  Quantifier order exposed: the escape name is chosen AFTER the pair (g, n).
  No claim that one name escapes all grammars or all stages — T7/T8 prove the
  reversed quantifier order FAILS for this construction.
  `stage_diag_escape` is a companion at the same tier covering the headline
  diagonal construction (stated deviation from the plan's theorem list:
  without it, G3 would silently demote the diagonal route to the secondary
  freshName route).
- T5 `diagSem_escapes`: DERIVED-MODEL-RELATIVE. Cantor diagonal over
  countable TOTAL Nat-indexed families; funext-free (congrFun only).
  "Internally definable" = "member of the family"; nothing about c.e.
  generation is claimed.
  CITATION CONTRACT (hostile-verification fix): any writeup citing T5 MUST
  carry THE MODEL paragraph above verbatim or equivalent — countable TOTAL
  Nat-indexed families; strict c.e. tier OPEN; classical ceiling on any
  positive c.e.-tier escape — wherever T5 is cited.
  "DERIVED-MODEL-RELATIVE" must never be shortened to "DERIVED" downstream.
- T6 `diag_absorbed_by_extension` / T7 `fresh_diagonal_absorbed` (+
  `fresh_diagonal_grammar_disclosed`): DERIVED — the fixture's stipulated
  `infinite_computable_context` NEGATIVE verdict
  (`source_issuance_passes = False`, reason: "a fixed grammar or c.e.
  generator absorbs the trace as search/disclosure",
  `tools/online_issuance_witness_checker.py`) upgraded from a stipulated
  constant to a theorem. The `extendFamily` claim is EXISTENTIAL — a fixed
  meta-family absorbs the given diagonal — never universal ("every
  conceivable construction is absorbed" is NOT claimed).
  T7 honesty: name-level absorption is machine-checked for `freshName`
  specifically (its outputs are all-'a' strings, enumerable in closed form
  per length by `allXNames` — no surjectivity hypothesis). `diagName`'s
  name-level absorption is a prose countability remark (the {'a','b'}-strings
  are likewise stage-enumerable in closed form, but that grammar is not built
  here); `diagName`'s machine-checked absorption is the semantic T6.
  CITATION CONTRACT (hostile-verification fix): writeups MUST NOT describe
  this "stipulated constant upgraded to theorem" as covering the diagonal
  route. The fixed-absorber-first absorption (T7 / T8 /
  `fresh_family_disclosure`) is machine-checked for `freshName` ONLY;
  `diagName`'s name-level absorption rests on the prose {'a','b'}-string
  stage-enumerability remark plus the F-dependent semantic T6.
- T8 `no_whole_family_name_escape`: OBSTRUCTION-PROVED-FOR-THE-CONSTRUCTION.
  The concrete `absorberFamily` pre-discloses EVERY `freshName` output at
  some stage, so the freshName construction never escapes the whole family.
  The fully general name-level impossibility (every escape construction
  absorbed by some fixed family) would need a Nat → String surjection and
  stays a prose countability note in the E-writeup; it is not claimed here.
  CITATION CONTRACT (hostile-verification fix): T8 is a double-negation
  restatement of T7 for the freshName construction — it adds NO independent
  mathematical content beyond T7 and must be presented as a restatement in
  any writeup, never as an additional result. Its positive universal form
  (the stronger-looking, direct statement) is `fresh_family_disclosure`.
- `no_fixed_point_of_absorption`: DERIVED — absorption never closes: the
  extended family has its own escaping diagonal. Per-family escape (T5) and
  fixed-family absorption (T6) coexist at different quantifier orders; that
  coexistence IS the class-relative structure of the comparator table.

Comparator-table consistency (tiers NOT compressed):
- T1/T2/T3 (Core) are untouched; T4–T8 are separate declarations.
- This module SUPPORTS the stipulated tier-2 negative verdict and never
  contradicts it: the LC-positive (`issue_lc_all_derived`, G1+G2) is a
  per-stage escape with the diagonal chosen AFTER the present enumerator; the
  tier-2 negative is fixed-family absorption with the family chosen AFTER the
  construction. Both are theorems here, each at its own quantifier order.
- The semantic tier's extensional candidate identity (functions Nat → Bool)
  sits BESIDE the name level, not replacing it: name-identity disclosure
  (Core's `PriorDisclosure`) remains the object language's notion at the
  finite tier.

Scope discipline (E117/E118): external-Platonist completion and physical
source issuance are not modeled and are not targets. Core.lean is not edited.
No claim movement: TI-C003 / TI-C019 / TI-C020 are untouched.
claim_status_change: none.
-/

import OnlineIssuance.Core
import OnlineIssuance.Diagonal

namespace OnlineIssuance

/-! ## Name level: stage-indexed grammars -/

/-- A stage-indexed grammar: at each stage, finitely many generated names.
Plain function — cumulativity (monotone stages) is deliberately NOT required;
it is not load-bearing for any theorem in this module. -/
abbrev StageGrammar := Nat → List String

/-- Name-level disclosure at a stage: the grammar generates the name there. -/
def GrammarDisclosure (g : StageGrammar) (n : Nat) (name : String) : Prop :=
  name ∈ g n

/-- Whole-family disclosure: the grammar generates the name at SOME stage. -/
def FamilyDisclosure (g : StageGrammar) (name : String) : Prop :=
  ∃ n, GrammarDisclosure g n name

/-- **T4 (per-grammar, per-stage escape — name tier).** Against EVERY stage
grammar and EVERY stage, the length-escape name built from that stage's
output is not disclosed at that stage. Quantifier order: the escape name is
chosen AFTER (g, n). DERIVED from G1's `freshName_not_mem`. -/
theorem stage_fresh_escape (g : StageGrammar) (n : Nat) :
    ¬ GrammarDisclosure g n (freshName (g n)) :=
  freshName_not_mem (g n)

/-- T4 companion: the same per-stage escape for the headline DIAGONAL
construction (`diagName`), so the diagonal route is not silently demoted to
the freshName route at this tier. DERIVED from G1's `diagName_not_mem`. -/
theorem stage_diag_escape (g : StageGrammar) (n : Nat) :
    ¬ GrammarDisclosure g n (diagName (g n)) :=
  diagName_not_mem (g n)

/-! ## Name level: the fixed absorber grammar -/

/-- The all-'a' name of a given length (the shape of every `freshName`
output). -/
def allAName (k : Nat) : String :=
  String.ofList (List.replicate k 'a')

/-- Closed-form stage vocabulary: at stage `n`, all all-'a' names of length
at most `n`. Constructed outright — NO surjectivity hypothesis, no assumed
covering. -/
def allXNames (n : Nat) : List String :=
  (List.range (n + 1)).map allAName

/-- The fixed absorber grammar: stage `n` emits `allXNames n`. A single,
concrete, computable-by-inspection stage grammar fixed BEFORE any escape
construction is consulted. -/
def absorberFamily : StageGrammar := allXNames

/-- `freshName vs` IS the all-'a' name of length `maxLen vs + 1`. -/
theorem freshName_eq_allAName (vs : List String) :
    freshName vs = allAName (maxLen vs + 1) := rfl

/-- **T7 (fixed-grammar absorption of the fresh escape — name tier).** The
fixed `absorberFamily` pre-discloses the `freshName` escape for EVERY input
value list, at the stage matching its length. This upgrades the fixture's
stipulated tier-2 reason — "a fixed grammar or c.e. generator absorbs the
trace as search/disclosure" — from a constant to a theorem, for the freshName
construction. -/
theorem fresh_diagonal_absorbed (vs : List String) :
    GrammarDisclosure absorberFamily (maxLen vs + 1) (freshName vs) := by
  show freshName vs ∈ (List.range (maxLen vs + 1 + 1)).map allAName
  rw [freshName_eq_allAName]
  exact List.mem_map_of_mem (List.mem_range.mpr (Nat.lt_succ_self _))

/-- T7 corollary, phrased against an arbitrary opponent grammar: whatever
stage grammar `g` the escape is built against, the escape name is
family-disclosed by the SAME fixed absorber. The absorber is chosen once;
the opponent and stage are universally quantified after it. -/
theorem fresh_diagonal_grammar_disclosed (g : StageGrammar) (n : Nat) :
    FamilyDisclosure absorberFamily (freshName (g n)) :=
  ⟨maxLen (g n) + 1, fresh_diagonal_absorbed (g n)⟩

/-- **T8 (OBSTRUCTION-PROVED-FOR-THE-CONSTRUCTION).** There is NO input on
which the freshName construction escapes the whole fixed absorber family:
whole-family name-level escape FAILS for this construction. Scope: this
refutes escape for the concrete `freshName` construction against the concrete
`absorberFamily`; the fully general impossibility (every construction
absorbed) is NOT claimed — it would need a Nat → String surjection and stays
a prose countability note. -/
theorem no_whole_family_name_escape :
    ¬ ∃ vs : List String, ¬ FamilyDisclosure absorberFamily (freshName vs) := by
  intro h
  obtain ⟨vs, hesc⟩ := h
  exact hesc ⟨maxLen vs + 1, fresh_diagonal_absorbed vs⟩

/-- **T8 positive universal form (hostile-verification fix).** EVERY
`freshName` output is family-disclosed by the fixed absorber. This is the
direct statement of what T7 already proves; `no_whole_family_name_escape`
is its double-negation rewrap and adds no independent content. Writeups
should cite this form (or T7) and present T8 as a restatement. -/
theorem fresh_family_disclosure (vs : List String) :
    FamilyDisclosure absorberFamily (freshName vs) :=
  ⟨maxLen vs + 1, fresh_diagonal_absorbed vs⟩

/-! ## Semantic level: countable total families and the extensional diagonal -/

/-- A countable Nat-indexed family of TOTAL extensional candidates (each a
Boolean predicate on Nat). Model boundary: a superclass of total computable
grammars on the escape side; NOT c.e. generation — no programs, no
partiality, no s-m-n. -/
abbrev SemFamily := Nat → Nat → Bool

/-- Class relativity as a DEFINITION: a semantic candidate is internally
definable relative to `F` iff it IS one of `F`'s members. No theorem in this
module quantifies over non-indexed grammars, so the external-Platonist
absorber boundary is untouched by construction. -/
def InternallyIndexed (F : SemFamily) (f : Nat → Bool) : Prop :=
  ∃ i, F i = f

/-- The extensional Cantor diagonal against a family: disagree with member
`i` at input `i`. -/
def diagSem (F : SemFamily) : Nat → Bool :=
  fun i => !(F i i)

/-- The diagonal disagrees with each member at that member's own index. -/
theorem diagSem_ne_at_own_index (F : SemFamily) (i : Nat) :
    diagSem F i ≠ F i i := by
  show (!(F i i)) ≠ F i i
  cases F i i
  · exact fun h => Bool.noConfusion h
  · exact fun h => Bool.noConfusion h

/-- **T5 (semantic escape — DERIVED-MODEL-RELATIVE).** No countable total
Nat-indexed family internally indexes its own diagonal. Funext-free: the
proof uses `congrFun` only (pointwise disagreement refutes equality of
functions; no function-extensionality axiom enters). -/
theorem diagSem_escapes (F : SemFamily) :
    ¬ InternallyIndexed F (diagSem F) := by
  intro h
  obtain ⟨i, hi⟩ := h
  exact diagSem_ne_at_own_index F i (congrFun hi i).symm

/-! ## Semantic level: fixed-family absorption of the diagonal -/

/-- A fixed meta-family absorbing `F`'s diagonal: index 0 carries the
diagonal, index i+1 carries `F i`. The absorption claim downstream is
EXISTENTIAL — this one fixed family absorbs — never universal. -/
def extendFamily (F : SemFamily) : SemFamily :=
  fun i =>
    match i with
    | 0 => diagSem F
    | Nat.succ j => F j

/-- **T6 (fixed-family absorption — semantic tier).** The diagonal that
escapes `F` is internally indexed by the fixed extension of `F`. Together
with T7 this is the machine-checked content of the fixture's tier-2 negative
verdict: the escape is absorbed as disclosure by a fixed larger grammar. -/
theorem diag_absorbed_by_extension (F : SemFamily) :
    InternallyIndexed (extendFamily F) (diagSem F) :=
  ⟨0, rfl⟩

/-- The extension loses nothing: every member of `F` is still internally
indexed by the extension. -/
theorem extension_preserves (F : SemFamily) (f : Nat → Bool)
    (h : InternallyIndexed F f) : InternallyIndexed (extendFamily F) f := by
  obtain ⟨i, hi⟩ := h
  exact ⟨i + 1, hi⟩

/-- **Absorption never closes.** The extended family has its own escaping
diagonal: no family reaches a fixed point of the absorb-then-diagonalize
step. Per-family escape (T5) and fixed-family absorption (T6) coexist at
different quantifier orders — that coexistence is the class-relative
structure of the comparator table, and it is exactly why this module supports
the tier-2 NEGATIVE verdict without contradicting the LC-positive of G1+G2. -/
theorem no_fixed_point_of_absorption (F : SemFamily) :
    ¬ InternallyIndexed (extendFamily F) (diagSem (extendFamily F)) :=
  diagSem_escapes (extendFamily F)

end OnlineIssuance
