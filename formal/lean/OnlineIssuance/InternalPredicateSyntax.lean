/-
OnlineIssuance^LC - internal predicate syntax for admissibility.

This module executes the gate left by E127: admissibility predicates should be
modeled as internal objects, not only as meta-level Lean predicates
`Ctx -> Candidate -> Prop`.

Scope discipline:
- This is a small internal-code syntax, not a full arithmetic coding,
  recursive-function theory, or Godel numbering.
- Predicate acceptance is defined by structural interpretation of finite
  `PredCode` terms.
- A bounded self-quotation/witness result is proved for an internal code.
- A universal acceptance reading is refuted by an internal future-stage guard.
- External Platonist completion and physical source issuance are not modeled.
- No claim movement: TI-C003 / TI-C019 / TI-C020 are untouched.
-/

import OnlineIssuance.Admissibility

namespace OnlineIssuance

/-! ## Internal predicate codes -/

/-- A tiny object-language syntax for admissibility predicates. -/
inductive PredCode where
  | acceptAll
  | formedBySucc
  | selfQuote
  | and (left right : PredCode)
deriving Repr, DecidableEq

/-- A stable object-language rendering used as the quote name. -/
def PredCode.render : PredCode -> String
  | .acceptAll => "acceptAll"
  | .formedBySucc => "formedBySucc"
  | .selfQuote => "selfQuote"
  | .and left right =>
      "and(" ++ PredCode.render left ++ "," ++ PredCode.render right ++ ")"

/-- Structural interpretation of an internal predicate code. -/
def PredCode.Accepts (p : PredCode) (Γ : Ctx) (c : Candidate) : Prop :=
  match p with
  | .acceptAll => True
  | .formedBySucc => c.formedAt <= Γ.prefixStage + 1
  | .selfQuote => c.name = PredCode.render .selfQuote
  | .and left right => left.Accepts Γ c ∧ right.Accepts Γ c

/-- Quote a predicate code as a candidate object in the successor context. -/
def PredCode.quote (Γ : Ctx) (p : PredCode) : Candidate :=
  { name := p.render, formedAt := Γ.prefixStage + 1 }

/-! ## Predicate objects and witness bridge -/

/-- A formed internal predicate object. -/
structure InternalPredicate where
  code : PredCode
  formedAt : Nat
deriving Repr, DecidableEq

/-- The predicate object is available in the prefix context. -/
def InternalPredicate.Present (Γ : Ctx) (P : InternalPredicate) : Prop :=
  P.formedAt <= Γ.prefixStage

/-- Acceptance by a formed internal predicate object. -/
def InternalPredicate.Accepts (P : InternalPredicate) (Γ : Ctx)
    (c : Candidate) : Prop :=
  P.code.Accepts Γ c

/-- Derived admissibility from an internal predicate object: the predicate is
present, the code accepts the candidate, and the witness has Core's successor
shape. -/
structure InternalAdmDerived (Γ : Ctx) (c : Candidate) (w : Witness)
    (P : InternalPredicate) : Prop where
  predicatePresent : P.Present Γ
  accepted : P.Accepts Γ c
  formedNext : w.formedAt = Γ.prefixStage + 1
  aboutCandidate : w.proposition = c.name

/-- Bridge internal-code admissibility back into Core's shape-only witness
interface, with the content explicitly forgotten here. -/
theorem InternalAdmDerived.toAdmWitness {Γ : Ctx} {c : Candidate}
    {w : Witness} {P : InternalPredicate}
    (h : InternalAdmDerived Γ c w P) : AdmWitness Γ c w :=
  ⟨h.formedNext, h.aboutCandidate⟩

/-- If a present internal predicate code accepts a candidate, the successor
witness term is constructible. -/
theorem internal_witness_from_acceptance (Γ : Ctx) (c : Candidate)
    (P : InternalPredicate) (hp : P.Present Γ) (ha : P.Accepts Γ c) :
    InternalAdmDerived Γ c (mkAdmWitnessTerm Γ c) P :=
  ⟨hp, ha, rfl, rfl⟩

/-- IssueLC can be built from a diagonal bundle plus internal-code
admissibility. This is the internal-syntax analogue of the old meta-level
`AdmDef` bridge. -/
theorem issue_lc_from_internal_admissibility (Γ : Ctx) (e : Enumerator)
    (c : Candidate) (P : InternalPredicate) (hDiag : DiagonalFormed Γ e c)
    (hp : P.Present Γ) (ha : P.Accepts Γ c) :
    IssueLC Γ e c (mkAdmWitnessTerm Γ c) :=
  issue_lc_from_diagonal_witness Γ e c (mkAdmWitnessTerm Γ c) hDiag
    ((internal_witness_from_acceptance Γ c P hp ha).toAdmWitness)

/-! ## Bounded self-application / witness result -/

/-- The self-quote predicate formed in the current prefix. -/
def selfQuotePredicate (Γ : Ctx) : InternalPredicate :=
  { code := .selfQuote, formedAt := Γ.prefixStage }

/-- The self-quote code accepts its own quoted candidate. -/
theorem selfQuote_accepts_own_quote (Γ : Ctx) :
    PredCode.Accepts .selfQuote Γ (PredCode.quote Γ .selfQuote) := by
  simp [PredCode.Accepts, PredCode.quote, PredCode.render]

/-- Bounded self-application: the formed internal predicate object accepts the
candidate that quotes its own code. -/
theorem selfQuotePredicate_accepts_own_quote (Γ : Ctx) :
    (selfQuotePredicate Γ).Accepts Γ (PredCode.quote Γ .selfQuote) :=
  selfQuote_accepts_own_quote Γ

/-- The self-quote predicate is present in its own prefix context. -/
theorem selfQuotePredicate_present (Γ : Ctx) :
    (selfQuotePredicate Γ).Present Γ :=
  Nat.le_refl _

/-- The self-quote acceptance produces an internal admissibility witness with
Core's successor-stage witness shape. -/
theorem selfQuote_internal_witness (Γ : Ctx) :
    InternalAdmDerived Γ (PredCode.quote Γ .selfQuote)
      (mkAdmWitnessTerm Γ (PredCode.quote Γ .selfQuote))
      (selfQuotePredicate Γ) :=
  internal_witness_from_acceptance Γ (PredCode.quote Γ .selfQuote)
    (selfQuotePredicate Γ) (selfQuotePredicate_present Γ)
    (selfQuotePredicate_accepts_own_quote Γ)

/-! ## Internal obstruction: not every code accepts every candidate -/

/-- The formed-by-successor guard rejects a candidate stamped beyond the
successor stage. -/
theorem formedBySucc_rejects_future (Γ : Ctx) (name : String) :
    ¬ PredCode.Accepts .formedBySucc Γ
      ({ name := name, formedAt := Γ.prefixStage + 2 } : Candidate) := by
  intro h
  simp [PredCode.Accepts] at h

/-- There is no universal internal-code acceptance theorem. The refuting code
is not a meta-level adversarial predicate; it is an object-language guard. -/
theorem no_universal_internal_acceptance :
    ¬ ∀ (p : PredCode) (Γ : Ctx) (c : Candidate), p.Accepts Γ c := by
  intro h
  let Γ0 : Ctx :=
    { prefixStage := 0
      symbols := []
      wellFormed := by
        intro s hs
        cases hs }
  have hf := h .formedBySucc Γ0
    ({ name := "future", formedAt := Γ0.prefixStage + 2 } : Candidate)
  exact formedBySucc_rejects_future Γ0 "future" hf

/-! ## A compact internal analogue of the prior concrete predicate -/

/-- Internal code corresponding to "presently admissible enough": accept the
candidate and require the successor-stage formation bound. -/
def boundedAdmCode : PredCode :=
  .and .acceptAll .formedBySucc

/-- The bounded admissibility code accepts its own quote. -/
theorem boundedAdmCode_accepts_own_quote (Γ : Ctx) :
    boundedAdmCode.Accepts Γ (PredCode.quote Γ boundedAdmCode) := by
  simp [boundedAdmCode, PredCode.Accepts, PredCode.quote]

end OnlineIssuance
