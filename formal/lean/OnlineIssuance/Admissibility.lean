/-
OnlineIssuance^LC — G2: derived self-encoding admissibility (pass two).

Pass one (`OnlineIssuance.Core`) carried self-encoding admissibility as an
ASSUMED hypothesis bundle: `AdmWitness` states only the SHAPE of a witness
(successor-stage stamp + aboutness). Core's `AdmWitness` is `⟨rfl, rfl⟩`-
inhabitable for a suitably built witness term — the pass-one bundle carried
NO semantic admissibility content. This module supplies a concrete
admissibility predicate (`AdmDef`), proves the diagonal candidate satisfies
it with a witness term constructible at the successor stage, and bridges back
into Core's interface. It also proves the honest obstruction half: the
discharge is predicate-RELATIVE and cannot be predicate-free.

Status labels (hostile-verifier vocabulary):
- `AdmDef` witness route: DERIVED-FOR-CONCRETE-PREDICATE. The admissibility
  predicate is `c.name ≠ "" ∧ c.formedAt ≤ Γ.prefixStage + 1` (the candidate
  names something, and its formation stamp respects the successor-stage
  discipline). For THIS predicate the diagonal's witness is derived with zero
  hypotheses (`adm_witness_diagonal_derived`); composed with G1, `IssueLC` is
  reachable from `{EnumeratorPresent}` alone (`issue_lc_all_derived`). This
  must NEVER be read as "self-encoding admissibility closed": the obstruction
  pair below shows the discharge cannot be predicate-free.
- `no_universal_self_encoding`: OBSTRUCTION-PROVED. The natural universal
  reading of the fixture's `self_encoding_admissibility` rule token — "every
  admissibility predicate accepts the stage's diagonal" — is REFUTED, and the
  refuting instance is the repo's own disclosure notion (`PriorDisclosure`),
  not a gerrymandered predicate (`diagonal_inadmissible_for_disclosure`).
  This is E117's demand made formal: the theorems name exactly which
  assumption carries the admissibility step (choice of the concrete
  predicate), instead of hiding it in a rule token.
- Core's `AdmWitness`: remains listed as the documented pass-one assumed
  bundle, now bridged-from-derived (`AdmDerived.toAdmWitness`). `AdmDerived`
  extends the shape with a `content : AdmDef Γ c` field — the guard against a
  hollow derivation that only re-inhabits the shape-only bundle.

Anti-gerrymander / non-triviality obligations (both machine-checked):
- Fairness: `adm_of_present` (any present-stage candidate with a nonempty
  name is admissible) and `enumerated_candidates_admissible` (the stage's own
  enumerated candidates satisfy the predicate) — `AdmDef` was not carved to
  accept only the diagonal.
- Non-triviality: `adm_not_trivial` (the name conjunct rejects the empty-named
  candidate) and `adm_rejects_future` (the stage conjunct rejects candidates
  stamped beyond the successor stage, for EVERY name — so the rejection is
  carried by the stage conjunct, not the name conjunct).

Fixture fidelity (`tools/proof_assistant_online_issuance_witness.py`):
- Stage-stamp divergence, resolved deliberately by shipping BOTH stamps:
  the fixture (PA-O5) stamps `w_diag` at `formed_at = n`; Core's `AdmWitness`
  demands `formedNext = Γ.prefixStage + 1`. `mkAdmWitnessTerm` carries the
  n+1 stamp (feeds Core's bundle); `mkPresentWitness` carries the fixture's
  n stamp (`present_witness_prefix_typed` shows it is prefix-typed in Γ_n).
- Proposition fidelity: the fixture's witness proposition is the
  UNINTERPRETED string "Adm_n(Diag(Enum_n))". Here `w.proposition = c.name`
  supersedes it: the object language has no internal predicate syntax, so a
  quoted predicate application cannot be stated internally; the witness
  records interpreted aboutness instead, and the admissibility content lives
  in the meta-level `content : AdmDef Γ c` field of `AdmDerived`.
- PA-O6 double registration: `issuedCtx` registers BOTH the diagonal
  candidate and the witness in the successor context via `Ctx.succWith2`,
  with well-formedness constructed, not assumed.

Scope labels (quotational reading):
- No internal predicate syntax is modeled: `AdmDef` and the quantified `A` in
  the obstruction theorem are meta-level (Lean `Prop`-valued) predicates.
  Gödel-style self-application — a predicate applied to a quotation of
  itself — is NOT modeled here.
- The obstruction refutes the natural universal reading of the rule token
  (all predicates over contexts/enumerators/candidates), not every
  conceivable guard class one might restrict to.

Scope discipline (E117/E118): finite present-enumerator tier only; the
computable-grammar comparator (G3), external-Platonist completion, and
physical source issuance are not touched. Core.lean is not edited. No claim
movement: TI-C003 / TI-C019 / TI-C020 are untouched.
claim_status_change: none.
-/

import OnlineIssuance.Core
import OnlineIssuance.Diagonal

namespace OnlineIssuance

/-! ## The concrete admissibility predicate -/

/-- Concrete admissibility at stage `Γ.prefixStage`'s issuance step: the
candidate names something (nonempty name) and its formation stamp respects
the successor-stage discipline (formed no later than `Γ.prefixStage + 1`).
This is ONE concrete predicate; the obstruction theorems below show the
discharge cannot be predicate-free. -/
def AdmDef (Γ : Ctx) (c : Candidate) : Prop :=
  c.name ≠ "" ∧ c.formedAt ≤ Γ.prefixStage + 1

/-- Admissibility is decidable: the witness check is effective, not oracular. -/
instance AdmDef.instDecidable (Γ : Ctx) (c : Candidate) :
    Decidable (AdmDef Γ c) :=
  inferInstanceAs (Decidable (c.name ≠ "" ∧ c.formedAt ≤ Γ.prefixStage + 1))

/-! ## Fairness pair (anti-gerrymander): the predicate is not carved for the
diagonal -/

/-- Any present-stage candidate with a nonempty name is admissible: `AdmDef`
does not single out the diagonal. -/
theorem adm_of_present (Γ : Ctx) (c : Candidate) (hname : c.name ≠ "")
    (hstage : c.formedAt ≤ Γ.prefixStage) : AdmDef Γ c :=
  ⟨hname, Nat.le_trans hstage (Nat.le_succ _)⟩

/-- The stage's own enumerated candidates (read at the fixture's PA-O2 stamp,
formed at the prefix) satisfy the predicate, provided they name something. -/
theorem enumerated_candidates_admissible (Γ : Ctx) (e : Enumerator)
    (hne : ∀ v ∈ e.values, v ≠ "") :
    ∀ v ∈ e.values, AdmDef Γ ⟨v, Γ.prefixStage⟩ :=
  fun v hv => adm_of_present Γ ⟨v, Γ.prefixStage⟩ (hne v hv) (Nat.le_refl _)

/-! ## Non-triviality pair (anti-relocation-to-triviality): both conjuncts
reject something -/

/-- The name conjunct rejects the empty-named candidate, even at the present
stage. -/
theorem adm_not_trivial (Γ : Ctx) : ¬ AdmDef Γ ⟨"", Γ.prefixStage⟩ :=
  fun h => h.1 rfl

/-- The stage conjunct rejects candidates stamped beyond the successor stage —
for EVERY name, so the rejection is carried by the stage conjunct alone. -/
theorem adm_rejects_future (Γ : Ctx) (name : String) :
    ¬ AdmDef Γ ⟨name, Γ.prefixStage + 2⟩ := by
  intro h
  have h2 : Γ.prefixStage + 2 ≤ Γ.prefixStage + 1 := h.2
  omega

/-! ## The diagonal is admissible (for the concrete predicate) -/

/-- **G2 content step.** The derived diagonal candidate satisfies the concrete
admissibility predicate, with ZERO hypotheses: its name is nonempty by
G1's padding (`diagName_ne_empty`) and its stamp is exactly the successor
stage by construction. -/
theorem admDef_of_diagonal (Γ : Ctx) (e : Enumerator) :
    AdmDef Γ (diagCandidate Γ e) :=
  ⟨diagName_ne_empty e.values, Nat.le_refl _⟩

/-! ## Witness terms: both stage stamps shipped -/

/-- Witness term at the SUCCESSOR stamp (Core's `AdmWitness.formedNext`
reading). `proposition = c.name` is interpreted aboutness, superseding the
fixture's uninterpreted string "Adm_n(Diag(Enum_n))" (see module docstring). -/
def mkAdmWitnessTerm (Γ : Ctx) (c : Candidate) : Witness :=
  ⟨"w_diag", c.name, Γ.prefixStage + 1⟩

/-- Witness term at the fixture's PRESENT stamp (PA-O5: `formed_at = n`). -/
def mkPresentWitness (Γ : Ctx) (c : Candidate) : Witness :=
  ⟨"w_diag", c.name, Γ.prefixStage⟩

/-- The fixture-stamped witness is prefix-typed in Γ_n (it could be carried as
a well-formed symbol of the PRESENT context). -/
theorem present_witness_prefix_typed (Γ : Ctx) (c : Candidate) :
    (mkPresentWitness Γ c).formedAt ≤ Γ.prefixStage :=
  Nat.le_refl _

/-! ## Derived admissibility bundle: shape PLUS content -/

/-- Derived admissibility: Core's `AdmWitness` shape (successor stamp +
aboutness) PLUS the semantic content `AdmDef Γ c`. The `content` field is the
guard against a hollow derivation — Core's shape-only bundle is
`⟨rfl, rfl⟩`-inhabitable and carried no admissibility semantics. -/
structure AdmDerived (Γ : Ctx) (c : Candidate) (w : Witness) : Prop where
  formedNext : w.formedAt = Γ.prefixStage + 1
  aboutCandidate : w.proposition = c.name
  content : AdmDef Γ c

/-- Bridge into the pass-one interface: derived admissibility yields Core's
assumed bundle (by forgetting the content — visibly, here, not silently). -/
theorem AdmDerived.toAdmWitness {Γ : Ctx} {c : Candidate} {w : Witness}
    (h : AdmDerived Γ c w) : AdmWitness Γ c w :=
  ⟨h.formedNext, h.aboutCandidate⟩

/-- **G2 witness constructibility.** For any candidate satisfying the concrete
predicate, the successor-stage witness term is constructible and the derived
bundle holds. -/
theorem adm_witness_derived (Γ : Ctx) (c : Candidate) (hc : AdmDef Γ c) :
    AdmDerived Γ c (mkAdmWitnessTerm Γ c) :=
  ⟨rfl, rfl, hc⟩

/-- **G2 for the diagonal.** The derived diagonal's admissibility witness is
constructible at the successor stage with ZERO hypotheses. Returns
`AdmDerived` (content field present), not the bare shape. -/
theorem adm_witness_diagonal_derived (Γ : Ctx) (e : Enumerator) :
    AdmDerived Γ (diagCandidate Γ e) (mkAdmWitnessTerm Γ (diagCandidate Γ e)) :=
  adm_witness_derived Γ _ (admDef_of_diagonal Γ e)

/-- T3 with the admissibility leg DERIVED: any candidate carrying a derived
diagonal bundle and the concrete admissibility content issues, with the
witness term constructed, not assumed. -/
theorem issue_lc_derived_witness (Γ : Ctx) (e : Enumerator) (c : Candidate)
    (hDiag : DiagonalFormed Γ e c) (hAdm : AdmDef Γ c) :
    IssueLC Γ e c (mkAdmWitnessTerm Γ c) :=
  ⟨hDiag, (adm_witness_derived Γ c hAdm).toAdmWitness, hDiag.notEnumerated⟩

/-! ## Obstruction pair (the honest half): the discharge is predicate-relative -/

/-- If admissibility is read as the repo's own prior-disclosure notion
("admissible = already enumerated"), the diagonal is provably INADMISSIBLE.
So there is a natural, non-gerrymandered predicate under which self-encoding
admissibility FAILS for the diagonal. -/
theorem diagonal_inadmissible_for_disclosure (Γ : Ctx) (e : Enumerator) :
    ¬ PriorDisclosure e (diagCandidate Γ e) :=
  diagName_not_mem e.values

/-- **OBSTRUCTION-PROVED.** The natural universal reading of the fixture's
`self_encoding_admissibility` rule token — every admissibility predicate
accepts the stage's diagonal — is refutable, and the refuting instance is
`PriorDisclosure` itself, not a gerrymandered predicate. The admissibility
discharge is therefore predicate-RELATIVE: `AdmDef` above is one concrete
choice, visibly named, never predicate-free. (Scope: refutes the universal
reading over all meta-level predicates; restricted guard classes are not
individually refuted, and no internal predicate syntax is modeled.) -/
theorem no_universal_self_encoding :
    ¬ ∀ (A : Ctx → Enumerator → Candidate → Prop) (Γ : Ctx) (e : Enumerator),
        EnumeratorPresent Γ e → A Γ e (diagCandidate Γ e) := by
  intro h
  let enumSym : Symbol := ⟨"Enum_0", Kind.enumerator, 0⟩
  let Γ0 : Ctx :=
    { prefixStage := 0
      symbols := [enumSym]
      wellFormed := by
        intro s hs
        simp [enumSym] at hs
        subst s
        exact Nat.le_refl 0 }
  let e0 : Enumerator := ⟨"Enum_0", 0, []⟩
  have hpresent : EnumeratorPresent Γ0 e0 := by
    refine ⟨Nat.le_refl 0, ?_, ?_, ?_⟩
    · simp [EnumeratorRegistered, Ctx.HasExactSymbol, Γ0, e0, enumSym]
    · intro v hv
      cases hv
    · intro s hs hk _hstage
      simp [Γ0, enumSym] at hs
      subst s
      cases hk
  have h0 := h (fun _ e c => PriorDisclosure e c)
    Γ0 e0 hpresent
  exact diagonal_inadmissible_for_disclosure _ _ h0

/-! ## PA-O6: double registration in the successor context -/

/-- Successor-context construction registering TWO symbols formed exactly at
the successor stage (candidate and witness); well-formedness is constructed,
not assumed. -/
def Ctx.succWith2 (Γ : Ctx) (s₁ s₂ : Symbol)
    (h₁ : s₁.formedAt = Γ.prefixStage + 1)
    (h₂ : s₂.formedAt = Γ.prefixStage + 1) : Ctx where
  prefixStage := Γ.prefixStage + 1
  symbols := s₁ :: s₂ :: Γ.symbols
  wellFormed := by
    intro t ht
    cases ht with
    | head => omega
    | tail _ ht' =>
      cases ht' with
      | head => omega
      | tail _ hmem =>
        have := Γ.wellFormed t hmem
        omega

/-- The issued successor context: the fixture's PA-O6 step. Both the derived
diagonal candidate and its derived witness are registered in Γ_{n+1}. -/
def issuedCtx (Γ : Ctx) (e : Enumerator) : Ctx :=
  Γ.succWith2
    ⟨(diagCandidate Γ e).name, Kind.candidate, Γ.prefixStage + 1⟩
    ⟨(mkAdmWitnessTerm Γ (diagCandidate Γ e)).name, Kind.witness,
      Γ.prefixStage + 1⟩
    rfl rfl

theorem issuedCtx_stage (Γ : Ctx) (e : Enumerator) :
    (issuedCtx Γ e).prefixStage = Γ.prefixStage + 1 := rfl

/-- PA-O6 double registration: the successor context carries BOTH the diagonal
candidate symbol and the witness symbol. -/
theorem issuedCtx_registers (Γ : Ctx) (e : Enumerator) :
    (⟨(diagCandidate Γ e).name, Kind.candidate, Γ.prefixStage + 1⟩ : Symbol)
        ∈ (issuedCtx Γ e).symbols
    ∧ (⟨(mkAdmWitnessTerm Γ (diagCandidate Γ e)).name, Kind.witness,
        Γ.prefixStage + 1⟩ : Symbol)
        ∈ (issuedCtx Γ e).symbols :=
  ⟨List.Mem.head _, List.Mem.tail _ (List.Mem.head _)⟩

/-! ## The composed headline: IssueLC from {EnumeratorPresent} alone -/

/-- **G1+G2 composed headline.** `IssueLC` — the pass-one target that needed
BOTH assumed bundles — is reachable from the single hypothesis
`EnumeratorPresent`. The diagonal candidate is constructed and its
non-enumeration proved (G1); the admissibility witness is constructed and its
content proved for the concrete predicate (G2). Tier scope: finite
present-enumerator; predicate scope: `AdmDef` (see obstruction pair). -/
theorem issue_lc_all_derived (Γ : Ctx) (e : Enumerator)
    (h : EnumeratorPresent Γ e) :
    IssueLC Γ e (diagCandidate Γ e) (mkAdmWitnessTerm Γ (diagCandidate Γ e)) :=
  ⟨diagonalFormed_derived Γ e h,
   (adm_witness_diagonal_derived Γ e).toAdmWitness,
   diagName_not_mem e.values⟩

/-- The composed headline WITH the semantic admissibility content kept
visible: `IssueLC` (Core's interface, whose admissibility field is the
shape-only bundle) together with `AdmDerived` (shape plus content), from the
same single hypothesis. Added so the composed result cannot be mistaken for a
re-inhabitation of the hollow shape. -/
theorem issue_lc_all_derived_full (Γ : Ctx) (e : Enumerator)
    (h : EnumeratorPresent Γ e) :
    IssueLC Γ e (diagCandidate Γ e) (mkAdmWitnessTerm Γ (diagCandidate Γ e))
      ∧ AdmDerived Γ (diagCandidate Γ e)
          (mkAdmWitnessTerm Γ (diagCandidate Γ e)) :=
  ⟨issue_lc_all_derived Γ e h, adm_witness_diagonal_derived Γ e⟩

end OnlineIssuance
