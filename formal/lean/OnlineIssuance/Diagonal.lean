/-
OnlineIssuance^LC — G1: derived diagonal productivity (pass two).

Pass one (`OnlineIssuance.Core`) carried diagonal productivity as an ASSUMED
hypothesis bundle: `DiagonalFormed` states `notEnumerated : c.name ∉ e.values`
without deriving it. This module DERIVES it: it constructs, inside the object
language, an actual diagonal candidate against an arbitrary present enumerator
and PROVES non-enumeration by a character-level Cantor diagonal. After this
module, the only hypothesis left on the diagonal leg of `IssueLC` is
`EnumeratorPresent` (the enumerator exists in the present prefix).

Status labels (hostile-verifier vocabulary):
- `diagName` route: DERIVED — diagonal productivity at the finite tier.
  The construction uses only the enumerator's stage-n value list; the escape
  proof is the classic Cantor disagreement at each row's own index. No
  injective-naming hypothesis, no `Fresh` oracle/typeclass, no new constructor
  added to any inductive candidate grammar. The theorems hold for arbitrary
  value lists, not a hand-built instance.
- `freshName` route: DERIVED-FINITE-FRESHNESS — a cardinality/length argument
  (any name strictly longer than every enumerated name is new). It is honest
  but it is NOT the diagonal; it must never headline. It is kept because the
  comparator module (G3) reuses it as the per-stage escape seed.

Construction notes:
- Padded diagonal: `diagChars` ranges over `vss.length + 1` positions, one
  more than the row count. The escape argument is unchanged (disagreement at
  row i's own index i < vss.length, or a length mismatch), and the extra
  position makes `diagName vs` nonempty unconditionally
  (`diagName_ne_empty`), so downstream admissibility (G2) needs no
  `e.values ≠ []` side hypothesis.
- Alphabet non-triviality: `flip_ne` rests on `'a' ≠ 'b'`, a kernel-decided
  fact about the concrete `Char` type — a fact of the object language, not an
  assumption. If names are ever abstracted from `String`/`Char` to an opaque
  `Name` type, the two-element-alphabet fact becomes a hypothesis and the
  module must be relabeled hypothesis-parameterized.
- Disclosure notion: name identity. `PriorDisclosure e c` is `c.name ∈
  e.values` (Core), inheriting the fixture's PA-O3/PA-O4 obligations, where
  separation is checked name-by-name against the enumerated values. This is
  fidelity to the fixture, not relocation; the extensional-disclosure
  objection (an enumerator that "discloses" a candidate under a different
  name) is out of scope at this tier and stays with the comparator ladder.

Fidelity gap, recorded per hostile verification (non-blocking):
- Core's `EnumeratorPresent Γ e` is only `e.formedAt ≤ Γ.prefixStage`. The
  fixture's PA-O2 is strictly stronger: it also requires the enumerator to be
  a registered context symbol of kind `enumerator`, every enumerated value to
  be a registered context symbol of kind `candidate`, and the enumerator's
  totality claim for the present prefix. Core's docstring "mirrors PA-O2" is
  therefore an overstatement; the honest reading is "weaker than PA-O2".
- Why the weaker form CANNOT hide the diagonal assumption: the escape theorem
  `diagName_not_mem` is proved with ZERO hypotheses over an arbitrary value
  list — no presence, registration, or totality fact enters the escape at
  all. `EnumeratorPresent` occurs only on the HYPOTHESIS side of
  `diagonalFormed_derived` (it is carried into the bundle, never consumed by
  the non-enumeration proof), so replacing it with any stronger
  PA-O2-faithful predicate strengthens the antecedent and the derivation goes
  through verbatim. A weaker presence predicate can only make the bridge
  theorem EASIER to invoke, never smuggle the diagonal escape.
- Disposition: strengthening the predicate to full PA-O2 fidelity (symbol
  registration + kind + totality flag) is deferred to a later pass; Core.lean
  stays frozen as the pass-one interface. Recorded in the gate writeup
  (E120 addendum).

Stage-stamp divergence (fixture vs Core), covered by DUAL bundles:
- Python fixture (`tools/proof_assistant_online_issuance_witness.py`):
  PA-O3 stamps the diagonal `formed_at = n` (the context prefix) and PA-O6
  registers it in the successor context `Gamma_{n+1}`.
- Core's `DiagonalFormed` stamps `formedNext = Γ.prefixStage + 1`.
- Both readings are machine-covered here: `diagonalFormed_derived` inhabits
  Core's n+1 bundle; `DiagonalFormedAtPrefix` + `diagonalFormedAtPrefix_derived`
  cover the fixture's formed-at-n reading. The diagonal NAME is a function of
  stage-n data alone in both.

Scope discipline (E117/E118):
- Tier scope: finite present-enumerator only. This module does not touch the
  computable-grammar comparator (G3), external-Platonist completion, or
  physical source issuance.
- Core.lean is not edited; its assumed bundles remain as the documented
  pass-one interface, now inhabited from below.
- No claim movement: TI-C003 / TI-C019 / TI-C020 are untouched.
  claim_status_change: none.
-/

import OnlineIssuance.Core

namespace OnlineIssuance

/-! ## The diagonal step: flip one character -/

/-- Flip a character: the diagonal step at one position. -/
def flip (c : Char) : Char := if c = 'a' then 'b' else 'a'

/-- `flip` never fixes a character. Rests on `'a' ≠ 'b'`, a kernel-decided
fact about the concrete `Char` alphabet (see module docstring). -/
theorem flip_ne (c : Char) : flip c ≠ c := by
  simp only [flip]
  split
  · rename_i h; subst h; decide
  · rename_i h; exact fun hc => h hc.symm

/-! ## Character-level Cantor diagonal (padded) -/

/-- Padded Cantor diagonal over rows of characters: position `i` flips the
`i`-th character of the `i`-th row (rows out of range read as `[]`, positions
out of range as `'z'`; the default is irrelevant since `flip` fixes nothing).
One extra position beyond the row count keeps the result nonempty even for
zero rows. -/
def diagChars (vss : List (List Char)) : List Char :=
  (List.range (vss.length + 1)).map (fun i => (vss.getD i []).getD i 'z' |> flip)

theorem diagChars_length (vss : List (List Char)) :
    (diagChars vss).length = vss.length + 1 := by
  simp [diagChars]

theorem diagChars_getElem (vss : List (List Char)) (i : Nat)
    (h : i < vss.length + 1) :
    (diagChars vss)[i]'(by simpa [diagChars] using h)
      = flip ((vss.getD i []).getD i 'z') := by
  simp [diagChars]

/-- The diagonal row differs from every row: the classic Cantor argument,
escape at row `i`'s OWN index (character disagreement when the row is long
enough, length disagreement otherwise). -/
theorem diagChars_ne (vss : List (List Char)) (i : Nat) (h : i < vss.length) :
    diagChars vss ≠ vss[i] := by
  intro he
  by_cases hl : i < (vss[i]).length
  · -- flipped character at position i disagrees
    have hlen : (diagChars vss).length = vss.length + 1 := diagChars_length vss
    have hi' : i < (diagChars vss).length := by omega
    have h1 : (diagChars vss)[i]'hi' = flip ((vss.getD i []).getD i 'z') :=
      diagChars_getElem vss i (by omega)
    have h0 : vss.getD i [] = vss[i] := by
      simp [List.getD_eq_getElem?_getD, List.getElem?_eq_getElem h]
    have h2 : (vss[i]).getD i 'z' = (vss[i])[i]'hl := by
      simp [List.getD_eq_getElem?_getD, List.getElem?_eq_getElem hl]
    have h3 : (diagChars vss)[i]'hi' = (vss[i])[i]'(by rw [← he] at hl; exact he ▸ hl) := by
      simp only [he]
    rw [h1, h0, h2] at h3
    exact flip_ne _ h3
  · -- row i is too short to equal the diagonal
    have hlen : (diagChars vss).length = vss.length + 1 := diagChars_length vss
    have : (vss[i]).length = vss.length + 1 := by rw [← he, hlen]
    omega

/-- Non-membership: the diagonal is not any enumerated row. -/
theorem diagChars_not_mem (vss : List (List Char)) : diagChars vss ∉ vss := by
  intro hmem
  obtain ⟨i, hi, he⟩ := List.mem_iff_getElem.mp hmem
  exact diagChars_ne vss i hi he.symm

/-! ## Lift to strings: the diagonal name -/

/-- The diagonal name against a value list. A function of the enumerator's
stage-n values ONLY — no future data enters the construction. -/
def diagName (vs : List String) : String :=
  String.ofList (diagChars (vs.map String.toList))

theorem diagName_toList (vs : List String) :
    (diagName vs).toList = diagChars (vs.map String.toList) := by
  simp [diagName]

/-- **G1 (derived diagonal productivity, finite tier).** The diagonal name is
not among the enumerated values — proved, not assumed, for an arbitrary value
list. -/
theorem diagName_not_mem (vs : List String) : diagName vs ∉ vs := by
  intro hmem
  have hmap : (diagName vs).toList ∈ vs.map String.toList :=
    List.mem_map_of_mem hmem
  rw [diagName_toList] at hmap
  exact diagChars_not_mem _ hmap

theorem diagName_length (vs : List String) :
    (diagName vs).toList.length = vs.length + 1 := by
  rw [diagName_toList, diagChars_length, List.length_map]

/-- The diagonal name is nonempty (padding pays off here: no `vs ≠ []`
hypothesis). Downstream, G2's concrete admissibility predicate needs this. -/
theorem diagName_ne_empty (vs : List String) : diagName vs ≠ "" := by
  intro h
  have hlen := diagName_length vs
  rw [h] at hlen
  simp at hlen

/-! ## Inhabiting Core's assumed bundle (Core reading: formed at n+1) -/

/-- Derived diagonal candidate: name from stage-n data, formed-stamp at the
successor stage, matching Core's `DiagonalFormed.formedNext`. (The fixture
stamps `formed_at = n` and registers at n+1; see `DiagonalFormedAtPrefix`
below for that reading.) -/
def diagCandidate (Γ : Ctx) (e : Enumerator) : Candidate :=
  ⟨diagName e.values, Γ.prefixStage + 1⟩

/-- **G1 bridge.** Core's `DiagonalFormed` bundle — assumed in pass one — is
now DERIVED for the constructed candidate. The only remaining hypothesis is
enumerator presence. -/
theorem diagonalFormed_derived (Γ : Ctx) (e : Enumerator)
    (h : EnumeratorPresent Γ e) : DiagonalFormed Γ e (diagCandidate Γ e) :=
  ⟨h, rfl, diagName_not_mem e.values⟩

/-- G1 corollary: T3's diagonal input no longer needs to be assumed. The
admissibility witness bundle `AdmWitness` remains an explicit hypothesis here
(it is G2's target, not G1's). -/
theorem issue_lc_from_derived_diagonal (Γ : Ctx) (e : Enumerator) (w : Witness)
    (h : EnumeratorPresent Γ e) (hAdm : AdmWitness Γ (diagCandidate Γ e) w) :
    IssueLC Γ e (diagCandidate Γ e) w :=
  issue_lc_from_diagonal_witness Γ e _ w (diagonalFormed_derived Γ e h) hAdm

/-! ## Registration at the successor stage (fixture's PA-O6 step) -/

/-- Register the derived diagonal in the successor context via `Ctx.succWith`:
the well-formedness of `Γ_{n+1}` is constructed, not assumed. -/
def registerDiagonal (Γ : Ctx) (e : Enumerator) : Ctx :=
  Γ.succWith ⟨(diagCandidate Γ e).name, Kind.candidate, Γ.prefixStage + 1⟩ rfl

theorem registerDiagonal_stage (Γ : Ctx) (e : Enumerator) :
    (registerDiagonal Γ e).prefixStage = Γ.prefixStage + 1 := rfl

theorem registerDiagonal_registers (Γ : Ctx) (e : Enumerator) :
    (⟨(diagCandidate Γ e).name, Kind.candidate, Γ.prefixStage + 1⟩ : Symbol)
      ∈ (registerDiagonal Γ e).symbols :=
  List.Mem.head _

/-! ## Fixture reading: formed at the prefix stage n

The Python fixture (PA-O3) stamps the diagonal `formed_at = n` and registers
it at n+1 (PA-O6). Core's bundle stamps n+1. Both readings are machine-covered
so the divergence cannot hide an assumption. -/

/-- `DiagonalFormed` with the fixture's stage stamp: formed AT the prefix
stage, not at the successor. Same derived `notEnumerated` content. -/
structure DiagonalFormedAtPrefix (Γ : Ctx) (e : Enumerator) (c : Candidate) :
    Prop where
  enumPresent : EnumeratorPresent Γ e
  formedAtPrefix : c.formedAt = Γ.prefixStage
  notEnumerated : c.name ∉ e.values

/-- The diagonal candidate under the fixture's stamp (formed at n). -/
def diagCandidateAtPrefix (Γ : Ctx) (e : Enumerator) : Candidate :=
  ⟨diagName e.values, Γ.prefixStage⟩

/-- The fixture-reading bundle is likewise DERIVED, with the same single
remaining hypothesis. -/
theorem diagonalFormedAtPrefix_derived (Γ : Ctx) (e : Enumerator)
    (h : EnumeratorPresent Γ e) :
    DiagonalFormedAtPrefix Γ e (diagCandidateAtPrefix Γ e) :=
  ⟨h, rfl, diagName_not_mem e.values⟩

/-! ## Secondary route: DERIVED-FINITE-FRESHNESS (not the diagonal)

A length/cardinality escape: any name strictly longer than every enumerated
name is new. Honest but weaker in kind — it must never headline as "diagonal
productivity". Kept because the comparator module (G3) reuses it. -/

/-- Maximum character-length over a value list. -/
def maxLen (vs : List String) : Nat :=
  vs.foldr (fun s n => max s.toList.length n) 0

theorem len_le_maxLen {s : String} {vs : List String} (h : s ∈ vs) :
    s.toList.length ≤ maxLen vs := by
  induction vs with
  | nil => cases h
  | cons a t ih =>
    cases h with
    | head => simp only [maxLen, List.foldr_cons]; exact Nat.le_max_left _ _
    | tail _ h' =>
      have := ih h'
      simp only [maxLen, List.foldr_cons] at *
      omega

/-- A fresh name by length: strictly longer than everything enumerated. -/
def freshName (vs : List String) : String :=
  String.ofList (List.replicate (maxLen vs + 1) 'a')

theorem freshName_length (vs : List String) :
    (freshName vs).toList.length = maxLen vs + 1 := by
  simp [freshName]

/-- DERIVED-FINITE-FRESHNESS: the length-escape name is not enumerated.
(Cardinality route — NOT the diagonal.) -/
theorem freshName_not_mem (vs : List String) : freshName vs ∉ vs := by
  intro hmem
  have hle := len_le_maxLen hmem
  rw [freshName_length] at hle
  omega

end OnlineIssuance
