/-
OnlineIssuance^LC — core Lean encoding (pass one).

Executes the gate `online_issuance_lc_lean_core_encoding` from
`agent-governance/NEXT-TRIGGER-PLAN.md`, per the encoding contract in
`explorations/E118-online-issuance-lc-theorem-prover-preflight-2026-07-01.md`.

Scope discipline (E117 / E118):
- Diagonal successor formation and self-encoding admissibility are NOT derived.
  They are carried as explicit hypotheses (`DiagonalFormed`, `AdmWitness`) so
  every theorem that uses them shows them in its statement.
- The internal future-oracle exclusion is type-level: the internal source
  object language simply has no completed-future-oracle constructor, and the
  `InternalSource` predicate provably cannot hold of one.
- The finite prior-disclosure comparator is the first real theorem target.
- The infinite computable grammar comparator is deferred (second pass).
- The external-Platonist completion absorber is NOT a theorem target here.
- No claim movement: TI-C003 / TI-C019 / TI-C020 are untouched.
-/

namespace OnlineIssuance

/-- Kinds of symbols available inside the local-constructive (LC) source class.
Note there is deliberately no oracle kind. -/
inductive Kind where
  | codeSpace
  | candidateType
  | admissibilityPredicate
  | candidate
  | enumerator
  | witness
deriving Repr, DecidableEq

/-- A named object formed at a definite stage. -/
structure Symbol where
  name : String
  kind : Kind
  formedAt : Nat
deriving Repr, DecidableEq

/-- A prefix context: every symbol it carries was formed no later than the
prefix stage. Prefix typing is a derived discipline (the `wellFormed` field),
not an axiom. -/
structure Ctx where
  prefixStage : Nat
  symbols : List Symbol
  wellFormed : ∀ s ∈ symbols, s.formedAt ≤ prefixStage

/-! ## PA-O2-faithful enumerator presence -/

/-- Exact symbol registration in a context. -/
def Ctx.HasExactSymbol (Γ : Ctx) (name : String) (kind : Kind)
    (formedAt : Nat) : Prop :=
  ({ name := name, kind := kind, formedAt := formedAt } : Symbol) ∈ Γ.symbols

/-- Present-prefix symbol registration, allowing the registering symbol's
formation stage to be recovered from the context. -/
def Ctx.HasPresentSymbol (Γ : Ctx) (name : String) (kind : Kind) : Prop :=
  ∃ formedAt, Γ.HasExactSymbol name kind formedAt ∧ formedAt ≤ Γ.prefixStage

/-- An enumerator formed at some stage, enumerating finitely many names. -/
structure Enumerator where
  name : String
  formedAt : Nat
  values : List String
deriving Repr, DecidableEq

/-- The enumerator symbol itself is registered in the context with kind
`enumerator`. -/
def EnumeratorRegistered (Γ : Ctx) (e : Enumerator) : Prop :=
  Γ.HasExactSymbol e.name Kind.enumerator e.formedAt

/-- Every value emitted by the enumerator is registered as a present-prefix
candidate symbol. This is the PA-O2 "enumerated values are candidate
registrations" leg. -/
def EnumeratorValuesRegistered (Γ : Ctx) (e : Enumerator) : Prop :=
  ∀ v ∈ e.values, Γ.HasPresentSymbol v Kind.candidate

/-- The enumerator claims totality over the present candidate prefix: every
candidate symbol already present in the context appears in the enumerated
value list. This is intentionally finite and prefix-local; it does not claim
anything about future candidates, c.e. completion, or external Platonist
families. -/
def EnumeratorTotalForPrefix (Γ : Ctx) (e : Enumerator) : Prop :=
  ∀ s ∈ Γ.symbols, s.kind = Kind.candidate → s.formedAt ≤ Γ.prefixStage →
    s.name ∈ e.values

/-- The enumerator is present in the context's prefix in the PA-O2-faithful
sense: it is a registered context symbol of kind `enumerator`, all enumerated
values are registered candidate symbols, and the enumerator is total for the
present candidate prefix. -/
structure EnumeratorPresent (Γ : Ctx) (e : Enumerator) : Prop where
  formedInPrefix : e.formedAt ≤ Γ.prefixStage
  registered : EnumeratorRegistered Γ e
  valuesRegistered : EnumeratorValuesRegistered Γ e
  prefixTotal : EnumeratorTotalForPrefix Γ e

theorem EnumeratorPresent.enumerator_symbol {Γ : Ctx} {e : Enumerator}
    (h : EnumeratorPresent Γ e) :
    Γ.HasExactSymbol e.name Kind.enumerator e.formedAt :=
  h.registered

theorem EnumeratorPresent.value_symbol {Γ : Ctx} {e : Enumerator}
    (h : EnumeratorPresent Γ e) {v : String} (hv : v ∈ e.values) :
    Γ.HasPresentSymbol v Kind.candidate :=
  h.valuesRegistered v hv

theorem EnumeratorPresent.total_for_candidate {Γ : Ctx} {e : Enumerator}
    (h : EnumeratorPresent Γ e) {s : Symbol} (hs : s ∈ Γ.symbols)
    (hk : s.kind = Kind.candidate) :
    s.name ∈ e.values :=
  h.prefixTotal s hs hk (Γ.wellFormed s hs)

/-- A candidate object formed at a definite stage. -/
structure Candidate where
  name : String
  formedAt : Nat
deriving Repr, DecidableEq

/-- An admissibility witness formed at a definite stage. -/
structure Witness where
  name : String
  proposition : String
  formedAt : Nat
deriving Repr, DecidableEq

/-- A source trace: the structural record of an issuance. -/
structure SourceTrace where
  source : String
  issued : String
  witness : String
  target : String
deriving Repr, DecidableEq

/-- Prior disclosure of a candidate by a (finite, present-prefix) enumerator:
the candidate's name is already among the enumerated values. This is the
finite comparator only; the computable-grammar comparator is deferred. -/
def PriorDisclosure (e : Enumerator) (c : Candidate) : Prop :=
  c.name ∈ e.values

/-! ## Prefix bookkeeping (derived, not axiomatized) -/

/-- Every symbol in a well-formed context is prefix-typed. -/
theorem Ctx.symbol_in_prefix (Γ : Ctx) (s : Symbol) (hs : s ∈ Γ.symbols) :
    s.formedAt ≤ Γ.prefixStage :=
  Γ.wellFormed s hs

/-- Successor-context construction: extending a context to the next stage with
a symbol formed exactly at that stage preserves well-formedness. -/
def Ctx.succWith (Γ : Ctx) (s : Symbol) (hs : s.formedAt = Γ.prefixStage + 1) :
    Ctx where
  prefixStage := Γ.prefixStage + 1
  symbols := s :: Γ.symbols
  wellFormed := by
    intro t ht
    cases ht with
    | head => omega
    | tail _ hmem =>
        have := Γ.wellFormed t hmem
        omega

/-! ## Explicit hypothesis bundles (NOT derived — E117 boundary)

Diagonal productivity and self-encoding admissibility are open per the hostile
review. They are stated as hypothesis structures so no theorem below can use
them invisibly. -/

/-- Hypothesis bundle: a diagonal successor candidate has been formed against a
present enumerator. `notEnumerated` is the diagonal property, carried as an
assumption, not derived. -/
structure DiagonalFormed (Γ : Ctx) (e : Enumerator) (c : Candidate) : Prop where
  enumPresent : EnumeratorPresent Γ e
  formedNext : c.formedAt = Γ.prefixStage + 1
  notEnumerated : c.name ∉ e.values

/-- Hypothesis bundle: an admissibility witness for the candidate, formed at
the successor stage. Self-encoding admissibility is assumed, not derived. -/
structure AdmWitness (Γ : Ctx) (c : Candidate) (w : Witness) : Prop where
  formedNext : w.formedAt = Γ.prefixStage + 1
  aboutCandidate : w.proposition = c.name

/-! ## T1: finite prior-disclosure failure -/

/-- **T1.** If prior disclosure is membership in the present prefix
enumerator, the diagonal candidate is not prior-prefix disclosure. Meaningful
but narrow: it does not defeat computable fixed grammars, external completion,
or physical fixed-source absorbers. -/
theorem finite_non_disclosure (e : Enumerator) (c : Candidate)
    (hDiag : c.name ∉ e.values) : ¬ PriorDisclosure e c :=
  hDiag

/-- T1 in context: the diagonal hypothesis bundle already carries finite
non-disclosure. -/
theorem finite_non_disclosure_of_diagonal (Γ : Ctx) (e : Enumerator)
    (c : Candidate) (hDiag : DiagonalFormed Γ e c) : ¬ PriorDisclosure e c :=
  hDiag.notEnumerated

/-! ## T2: internal future-oracle invalidity (type-level) -/

/-- Objects internal to the LC source class. This inductive is the class
boundary: there is no completed-future-oracle constructor. -/
inductive InternalSourceObject where
  | ofSymbol (s : Symbol)
  | ofEnumerator (e : Enumerator)
  | ofCandidate (c : Candidate)
  | ofWitness (w : Witness)
deriving Repr, DecidableEq

/-- Objects that could be *proposed* as source machinery, including the
forbidden one: a completed-future oracle revealing content beyond some stage. -/
inductive ProposedObject where
  | internalObj (o : InternalSourceObject)
  | completedFutureOracle (revealsBeyond : Nat)
deriving Repr, DecidableEq

/-- The internal-source predicate: holds exactly of internal LC objects. -/
inductive InternalSource : ProposedObject → Prop where
  | mk (o : InternalSourceObject) : InternalSource (.internalObj o)

/-- **T2.** The LC source class has no internal completed-future-oracle
object. This is a consequence of the object language (no constructor exists),
not an English-level restriction. Preserves the class boundary E108/E115
checked in Python. -/
theorem no_internal_completed_future_oracle (n : Nat) :
    ¬ InternalSource (.completedFutureOracle n) := by
  intro h
  cases h

/-! ## T3: Issue[S]^LC construction from explicit assumptions -/

/-- Issue[S]^LC: a diagonal candidate, an admissibility witness, and finite
non-disclosure, at the successor stage of the prefix context. -/
structure IssueLC (Γ : Ctx) (e : Enumerator) (c : Candidate) (w : Witness) :
    Prop where
  diagonal : DiagonalFormed Γ e c
  admissible : AdmWitness Γ c w
  notPriorDisclosed : ¬ PriorDisclosure e c

/-- **T3.** Given the deliberately stated formation assumptions — the diagonal
bundle and the admissibility witness bundle, both visible in the statement —
the issuance can be typed as Issue[S]^LC. -/
theorem issue_lc_from_diagonal_witness (Γ : Ctx) (e : Enumerator)
    (c : Candidate) (w : Witness)
    (hDiag : DiagonalFormed Γ e c) (hAdm : AdmWitness Γ c w) :
    IssueLC Γ e c w :=
  ⟨hDiag, hAdm, hDiag.notEnumerated⟩

/-- The source trace is structural once candidate and witness are supplied. -/
def mkTrace (c : Candidate) (w : Witness) : SourceTrace :=
  { source := "S_LC"
    issued := c.name
    witness := w.name
    target := "shared-process" }

/-- Trace shape sanity: the trace records exactly the issued candidate and the
witness used. -/
theorem mkTrace_faithful (c : Candidate) (w : Witness) :
    (mkTrace c w).issued = c.name ∧ (mkTrace c w).witness = w.name :=
  ⟨rfl, rfl⟩

/-! ## Deferred (second pass; recorded so they cannot be silently claimed)

- Infinite computable grammar comparator: requires a precise computability
  model (c.e. generation); NOT encoded here.
- External-Platonist completion: an absorber boundary, not an internal
  contradiction; NOT a theorem target.
- Physical source issuance (TI-C020): not modeled; stays parked.
-/

end OnlineIssuance
