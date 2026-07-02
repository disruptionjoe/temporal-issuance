/-
OnlineIssuance^LC - T8 name-level absorption for the diagonal name.

This module closes the narrow citation boundary left by `Comparator.lean`.
`Comparator` machine-checked whole-family name absorption for `freshName`, but
`diagName` name-level absorption was still a prose countability remark plus
the semantic `extendFamily` absorber. Here the absorber is explicit:

- `binaryNameAbsorberFamily n` emits every {'a','b'} string of length at most n.
- every `diagName vs` is an {'a','b'} string of length `vs.length + 1`.
- therefore every `diagName vs` is disclosed by the fixed absorber family at
  stage `vs.length + 1`.

Scope discipline:
- This is a bounded name-level absorber for the concrete `diagName`
  construction, not a fully general theorem over arbitrary name-producing
  functions.
- No external-Platonist completion, c.e. positive escape, or physical source
  issuance claim is touched.
- claim_status_change: none.
-/

import OnlineIssuance.Comparator

namespace OnlineIssuance

/-! ## Binary strings -/

/-- All character lists of exactly length `n` over the concrete alphabet
{'a','b'}. -/
def binaryCharLists : Nat -> List (List Char)
  | 0 => [[]]
  | n + 1 =>
      let tails := binaryCharLists n
      tails.map (fun cs => 'a' :: cs) ++ tails.map (fun cs => 'b' :: cs)

/-- A list is binary when every character is either 'a' or 'b'. -/
def BinaryChars (cs : List Char) : Prop :=
  ∀ c, c ∈ cs -> c = 'a' ∨ c = 'b'

theorem mem_binaryCharLists_of_binary (cs : List Char)
    (hbin : BinaryChars cs) : cs ∈ binaryCharLists cs.length := by
  induction cs with
  | nil =>
      simp [binaryCharLists]
  | cons c cs ih =>
      have hc : c = 'a' ∨ c = 'b' := hbin c (List.Mem.head cs)
      have htail : BinaryChars cs := by
        intro x hx
        exact hbin x (List.Mem.tail c hx)
      have hcs : cs ∈ binaryCharLists cs.length := ih htail
      cases hc with
      | inl ha =>
          subst c
          simp [binaryCharLists, hcs]
      | inr hb =>
          subst c
          simp [binaryCharLists, hcs]

theorem flip_binary (c : Char) : flip c = 'a' ∨ flip c = 'b' := by
  unfold flip
  split
  · exact Or.inr rfl
  · exact Or.inl rfl

theorem diagChars_binary (vss : List (List Char)) : BinaryChars (diagChars vss) := by
  intro c hc
  unfold diagChars at hc
  obtain ⟨i, _hi, hc_eq⟩ := List.mem_map.mp hc
  rw [← hc_eq]
  exact flip_binary ((vss.getD i []).getD i 'z')

theorem diagChars_mem_binaryCharLists (vss : List (List Char)) :
    diagChars vss ∈ binaryCharLists (vss.length + 1) := by
  rw [← diagChars_length vss]
  exact mem_binaryCharLists_of_binary (diagChars vss) (diagChars_binary vss)

/-! ## Fixed absorber grammar -/

/-- All binary names of exactly length `n`. -/
def binaryNamesOfLength (n : Nat) : List String :=
  (binaryCharLists n).map String.ofList

/-- All binary names of length at most `n`. -/
def binaryNamesUpTo (n : Nat) : List String :=
  (List.range (n + 1)).flatMap binaryNamesOfLength

/-- The fixed name-level absorber for `diagName`: stage `n` emits all
binary strings of length at most `n`. -/
def binaryNameAbsorberFamily : StageGrammar := binaryNamesUpTo

theorem mem_binaryNamesUpTo_of_exact {name : String} {k : Nat}
    (h : name ∈ binaryNamesOfLength k) : name ∈ binaryNamesUpTo k := by
  unfold binaryNamesUpTo
  exact List.mem_flatMap.mpr
    ⟨k, List.mem_range.mpr (Nat.lt_succ_self k), h⟩

theorem diagName_mem_binaryNamesOfLength (vs : List String) :
    diagName vs ∈ binaryNamesOfLength (vs.length + 1) := by
  have hchars := diagChars_mem_binaryCharLists (vs.map String.toList)
  have hnames :
      String.ofList (diagChars (vs.map String.toList)) ∈
        (binaryCharLists ((vs.map String.toList).length + 1)).map String.ofList :=
    List.mem_map_of_mem hchars
  simpa [binaryNamesOfLength, diagName] using hnames

/-- **T8-diag bounded positive form.** The fixed binary-name absorber
discloses the concrete diagonal name at the stage matching its length. -/
theorem diagName_absorbed (vs : List String) :
    GrammarDisclosure binaryNameAbsorberFamily (vs.length + 1) (diagName vs) := by
  unfold GrammarDisclosure binaryNameAbsorberFamily
  exact mem_binaryNamesUpTo_of_exact (diagName_mem_binaryNamesOfLength vs)

/-- Whole-family form: every `diagName` output is disclosed somewhere by the
same fixed absorber family. -/
theorem diagName_family_disclosure (vs : List String) :
    FamilyDisclosure binaryNameAbsorberFamily (diagName vs) :=
  ⟨vs.length + 1, diagName_absorbed vs⟩

/-- **T8-diag obstruction form.** There is no input on which the concrete
`diagName` construction escapes the fixed binary-name absorber family. This is
the bounded theorem needed for the E121 citation boundary; the broader
Nat-to-String surjection theorem is unnecessary for this construction. -/
theorem no_diagName_whole_family_escape :
    ¬ ∃ vs : List String,
      ¬ FamilyDisclosure binaryNameAbsorberFamily (diagName vs) := by
  intro h
  obtain ⟨vs, hesc⟩ := h
  exact hesc (diagName_family_disclosure vs)

end OnlineIssuance
