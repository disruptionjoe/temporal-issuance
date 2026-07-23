/-
OnlineIssuance^LC — Boundary-parent extension: the PARENT STATEMENT SHAPE
(leg 1) and the CROSS-REPO ASSEMBLY TARGET (leg 3).

Cross-repo swing (Joe direct chat, 2026-07-20). GU's diagonal-boundary parent
factors into leg (a) [self-encoding admissibility + diagonal = Lawvere
no-closure] and leg (b) [fixpoint-free label involution => no invariant
valuation]. `BoundaryInvolution.lean` formalized leg (b). This module:

  1. Formalizes the PARENT STATEMENT SHAPE: the hypothesis package
     (self-encoding admissibility as weak point-surjectivity of a closure
     candidate `T`, over an inhabited label object with a fixpoint-free
     involution) and BOTH conclusions ((a) no self-closure; (b) no
     alpha-invariant valuation), mirroring TI's leg-a style (Core.lean's
     hypothesis-structure discipline).

  2. PROVES conclusion (a) as Lawvere's fixed-point theorem, contrapositive,
     with the fixpoint-free involution `alpha` supplied as the map with no
     fixed point. The diagonal that witnesses non-closure is EXACTLY the
     parent's twisted diagonal `d = alpha . T . Delta` (`twistedDiagonal`
     below): no row of `T` represents it. This is the same Cantor/Lawvere
     engine that `Diagonal.lean`'s `diagName_not_mem` runs over the concrete
     String label object — here abstracted to any label object, so the two TI
     files now cover leg (a) both concretely (strings) and schematically
     (any B).

  3. States the cross-repo assembly TARGET as a proved conditional theorem.
     The missing leg-(a) bridge is now a typed premise
     `H_leg_a : ¬ WeaklyPointSurjective T`, rather than an admitted proof term.
     The target therefore machine-checks the composition while making no claim
     that TI has constructed the GU-side instance. GU's 2026-07-22 operator
     correction establishes that the earlier product-uniform surrogate is not
     sufficient for that physical instantiation: the live reopener is an actual
     source-owned operator/domain/end packet plus the map from that packet into
     the assembled `T`. Conjunct (b) remains a codomain-only fact and the TaF
     premise remains an inert placeholder until it is retraction-typed.

Mathlib-free (core Lean only; `Function.Injective` and the diagonal argument
are Init-level). Scope: INDEPENDENT-LEGS. The TaF composite is a separate gated
wave, appearing only as a named hypothesis in the target, never formalized.

No claim movement: TI-C003 / TI-C019 / TI-C020 untouched.
claim_status_change: none.
-/

import OnlineIssuance.BoundaryInvolution

namespace OnlineIssuance
namespace Boundary

/-! ## L1 encoding: self-encoding admissibility as weak point-surjectivity

The parent's L1: "a category with finite products and a diagonal
`Delta : A → A × A`; admissibility predicates are exactly the maps `A → B`; a
firewall-closure is a weakly point-surjective `T : A × A → B`." We curry
`A × A → B` to `A → A → B`; the diagonal `Delta` is `x ↦ (x, x)`, so the
diagonal composite reads `x ↦ T x x`. Admissibility predicates are the maps
`g : A → B`. Weak point-surjectivity: `T` internally represents every such
predicate (some row `a` reproduces `g`). -/

/-- The firewall-closure predicate: `T` weakly point-surjective — the observer
internally represents every admissibility predicate `g : A → B`. -/
def WeaklyPointSurjective {A B : Type _} (T : A → A → B) : Prop :=
  ∀ g : A → B, ∃ a : A, ∀ x : A, T a x = g x

/-- The parent's twisted diagonal `d = alpha . T . Delta`: flip the label read
off the diagonal of `T`. -/
def twistedDiagonal {A B : Type _} (alpha : B → B) (T : A → A → B) : A → B :=
  fun x => alpha (T x x)

/-! ## Leg (a): Lawvere no-closure, with the involution as the fixed-point-free map -/

/-- **Lawvere's fixed-point theorem (Set form).** If `T` is weakly
point-surjective, then EVERY `f : B → B` has a fixed point. The diagonal
`g x = f (T x x)` is represented by some row `a`, and its own value
`T a a = f (T a a)` is fixed. This is leg (a)'s engine, abstracted. -/
theorem lawvere_fixed_point {A B : Type _} {T : A → A → B}
    (hT : WeaklyPointSurjective T) (f : B → B) : ∃ b, f b = b := by
  obtain ⟨a, ha⟩ := hT (fun x => f (T x x))
  exact ⟨T a a, (ha a).symm⟩

/-- **Conclusion (a): no self-closure.** Contrapositive of Lawvere with the
fixpoint-free involution supplied as `f`: no closure candidate `T` is weakly
point-surjective. The observer cannot internally represent every admissibility
predicate — the twisted diagonal always escapes. -/
theorem no_self_closure {A B : Type _} (T : A → A → B) {alpha : B → B}
    (hff : FixpointFree alpha) : ¬ WeaklyPointSurjective T := by
  intro hT
  obtain ⟨b, hb⟩ := lawvere_fixed_point hT alpha
  exact hff b hb

/-- The escape made explicit: the twisted diagonal `d = alpha . T . Delta` is
represented by NO row of `T`. This is the parent's exact phrasing ("the
diagonal predicate `d = alpha . T . Delta` is unrepresented for every `T`") and
the abstract twin of `Diagonal.lean`'s `diagName_not_mem`. -/
theorem twistedDiagonal_unrepresented {A B : Type _} {alpha : B → B}
    (hff : FixpointFree alpha) (T : A → A → B) :
    ¬ ∃ a, ∀ x, T a x = twistedDiagonal alpha T x := by
  intro hex
  obtain ⟨a, ha⟩ := hex
  have h := ha a
  simp only [twistedDiagonal] at h
  exact hff (T a a) h.symm

/-! ## The parent statement shape: hypothesis package + both conclusions -/

/-- The parent's hypothesis package, as one structure (leg-a style, mirroring
Core.lean's `DiagonalFormed`/`AdmWitness` discipline of carrying hypotheses
visibly). `A` is the admissibility space; `B` the label object; `alpha` the
grading-flip induced across the firewall. `point : A` makes the space inhabited
(needed for the diagonal `Delta` to have an argument and for a valuation domain
to be nonempty — both genuine hypotheses, kept visible). -/
structure ParentHypotheses (A B : Type _) where
  /-- The grading-flip `alpha : B → B`. -/
  alpha : B → B
  /-- L2 first half: `alpha` is an involution (`J^2 = 1`). -/
  invol : Involution alpha
  /-- L2 second half: `alpha` is fixpoint-free (nontrivial firewall). -/
  fpf : FixpointFree alpha
  /-- The admissibility space is inhabited. -/
  point : A

/-- **Conclusion (a) in the package.** No firewall-closure exists. -/
theorem ParentHypotheses.no_self_closure {A B : Type _}
    (H : ParentHypotheses A B) (T : A → A → B) : ¬ WeaklyPointSurjective T :=
  OnlineIssuance.Boundary.no_self_closure T H.fpf

/-- **Conclusion (b) in the package.** No `alpha`-invariant valuation exists;
every definite valuation is an external, symmetry-breaking selection. -/
theorem ParentHypotheses.no_invariant_valuation {A B : Type _}
    (H : ParentHypotheses A B) :
    ¬ ∃ v : A → B, InvariantValuation H.alpha v :=
  OnlineIssuance.Boundary.no_invariant_valuation H.fpf H.point

/-- **THE BOUNDARY PARENT (statement shape, both conclusions).** From the
hypothesis package: (a) no firewall-closure `T` is point-surjective [needs the
diagonal leg — `alpha` supplies the fixpoint-free map], AND (b) no
`alpha`-invariant valuation exists [needs L2 alone]. The honest factorization
of the parent is visible in the proof term: (a) routes through `lawvere_fixed_point`
(diagonal), (b) through `no_invariant_valuation` (pure involution arithmetic). -/
theorem boundary_parent_law {A B : Type _} (H : ParentHypotheses A B) :
    (∀ T : A → A → B, ¬ WeaklyPointSurjective T)
    ∧ (¬ ∃ v : A → B, InvariantValuation H.alpha v) :=
  ⟨fun T => no_self_closure T H.fpf,
   no_invariant_valuation H.fpf H.point⟩

/-- The canonical `Bool = {+,-}` instance of the whole package: the parent law
holds over any inhabited admissibility space with the `not`-swap firewall. -/
def boolParent {A : Type _} (a₀ : A) : ParentHypotheses A Bool :=
  ⟨Bool.not, not_involution, not_fixpointfree, a₀⟩

theorem bool_boundary_parent_law {A : Type _} (a₀ : A) :
    (∀ T : A → A → Bool, ¬ WeaklyPointSurjective T)
    ∧ (¬ ∃ v : A → Bool, InvariantValuation Bool.not v) :=
  boundary_parent_law (boolParent a₀)

/-! ## Leg 3: the cross-repo assembly TARGET (PROVED CONDITIONALLY)

The single theorem that conditionally composes the three repos' legs. GU's
l1-assembly swing (fixture grade) exhibits the proposed category `C_read` of
six reading classes over one Z/2; TI supplies the abstract diagonal theorem;
TaF supplies a distinct first/third-person mechanism. The pieces not yet at
theorem-prover grade are explicit hypotheses. In particular, `H_leg_a` has the
exact proposition needed for the first conjunct, so the proof checks without
hiding the missing cross-repo instantiation.

The companion `..._skeleton` below proves that the abstract self-closure
conclusion also follows from a genuine fixpoint-free `alpha`. It does not
construct the GU identification of `Read`, `B`, `alpha`, or `T`, and neither
the target nor the skeleton constructs the distinct typed TaF retraction. -/

/-- **CROSS-REPO ASSEMBLY TARGET (leg 3 - PROVED FROM TYPED PREMISES).**
Hypotheses (each a named missing piece):
  * `_H_assembly` - GU l1-assembly: the reading classes `Read` form one
                    category over the single label object `B` with finite
                    products, terminal object, and an equivariant diagonal;
                    admissibility predicates are the maps `Read → B`.
                    (Fixture grade in GU; NOT Lean-verified.)
  * `alpha`, `_H_involution`, `H_fpf` - GU/TI leg (b): the single fixpoint-free
                    involution on `B`. (Involution arithmetic PROVED in
                    `BoundaryInvolution.lean`; the identification that this is
                    the ONE assembled `alpha` is GU-side.)
  * `T`, `H_leg_a` - TI leg (a): the assembled firewall-closure candidate and
                    the typed point-surjectivity failure required by the
                    conclusion. The abstract law is proved locally; the claim
                    that these data arise from GU's physical construction is
                    NOT Lean-verified here.
  * `_H_taf`      - TaF composite: the first/third-person finality gap is the
                    joint conclusion-level analogue of (a) ∧ (b). The TaF
                    mechanism is now known to be a causal-past retraction
                    (`pi ∘ pi = pi`, oriented, non-invertible), not this
                    file's fixpoint-free involution. `_H_taf : True` remains
                    only an inert placeholder; a later typed assembly must
                    keep the retraction and involution legs distinct.
                    (Separate gated wave; NOT Lean.)
Conclusion: the unified boundary law, (a) ∧ (b), over the assembled data.

CURRENT STATUS (2026-07-22, after GU's operator/domain correction).
The two conjuncts factor and their interpretation must stay independent:
  * Conjunct (b), CODOMAIN FIXED-OUTPUT
    (`¬ ∃ v, InvariantValuation alpha v`), follows directly from
    `no_invariant_valuation H_fpf point`. It says that a map cannot return an
    alpha-fixed label when alpha has no fixed point. Because alpha acts only on
    the codomain in `InvariantValuation`, this theorem is silent about a genuine
    alpha-equivariant reader and carries no GU-internal unreadability result by
    itself. The physical claim still needs the open domain-side bridge that
    every internal sigma-supplier lies in the alpha-even observable class.
  * Conjunct (a), SELF-CLOSURE (`¬ WeaklyPointSurjective T`), is supplied to this
    cross-repo target by the typed `H_leg_a` premise. TI proves the abstract
    Lawvere implication separately, but the physical identification of GU's
    assembled reader data with these abstract types remains source-gapped. The
    earlier product-uniform numerical/surrogate result is not sufficient after
    GU's correction. Reopen physical instantiation only from a source-owned
    first-order operator, end geometry and density, closed-domain/Green-trace
    packet, symmetry actions, and an explicit map into the assembled `T`.
The honest position: the TARGET is now proof-admission-free and conditionally proved;
the substantive GU reader interpretation, the physical self-closure instance,
and the distinct typed TaF retraction remain open. -/
theorem cross_repo_boundary_law_TARGET
    {Read B : Type _}
    (_H_assembly : True)
    (alpha : B → B) (_H_involution : Involution alpha) (H_fpf : FixpointFree alpha)
    (T : Read → Read → B) (H_leg_a : ¬ WeaklyPointSurjective T)
    (_H_taf : True)
    (point : Read) :
    (¬ WeaklyPointSurjective T)
    ∧ (¬ ∃ v : Read → B, InvariantValuation alpha v) :=
  -- (a) self-closure: supplied as a typed cross-repo premise; physical instantiation stays open.
  -- (b) codomain fixed-output fact: PROVED; no physical-reader bridge implied.
  ⟨H_leg_a, no_invariant_valuation H_fpf point⟩

/-- Companion: the ABSTRACT SKELETON of the target, PROVED. Given
the involution/fixpoint-free hypotheses and an inhabited `Read`, the boundary
law for the specific `T` follows from the leg-(a) and leg-(b) lemmas. This
isolates the remaining cross-repo work as instantiation: showing that these
`alpha` and `T` arise from GU's `C_read` and relate to TI's and TaF's distinct
faces, rather than a gap in the abstract logic. -/
theorem cross_repo_boundary_law_skeleton
    {Read B : Type _}
    {alpha : B → B} (H_fpf : FixpointFree alpha)
    (T : Read → Read → B) (point : Read) :
    (¬ WeaklyPointSurjective T)
    ∧ (¬ ∃ v : Read → B, InvariantValuation alpha v) :=
  ⟨no_self_closure T H_fpf,
   no_invariant_valuation H_fpf point⟩

/-! ## Illustrative two-label model of the codomain conjunct

`Bool.not` supplies a concrete fixpoint-free two-label swap, so the codomain
statement is not an implication over an uninhabited hypothesis package. This
finite model is generic: it contains no domain action and no GU observable
algebra. GU commit `a0a1401` therefore defeats the earlier interpretation of
this witness as a theorem that an internal observer cannot read or supply
sigma. That substantive conclusion requires the separate open bridge that
internal observables are alpha-even. -/

/-- **Historical API name; codomain-only Bool witness.** This theorem proves
exactly that no map into `Bool` has pointwise `Bool.not`-fixed outputs. It does
not model an alpha action on `Read`, exclude alpha-equivariant readers, or prove
GU-internal sigma unreadability. The name is retained to avoid needless API
churn; see GU correction `a0a1401` and RUN-0193. -/
theorem k_s_flip_externality {Read : Type _} (point : Read) :
    ¬ ∃ v : Read → Bool, InvariantValuation Bool.not v :=
  no_invariant_valuation not_fixpointfree point

/-- Historical API name; witnesses only that the abstract codomain hypothesis
package is inhabited by `Bool.not`. It supplies no GU domain-side bridge. -/
theorem k_s_flip_hypotheses_inhabited {Read : Type _} (point : Read) :
    Involution Bool.not ∧ FixpointFree Bool.not
    ∧ ¬ ∃ v : Read → Bool, InvariantValuation Bool.not v :=
  ⟨not_involution, not_fixpointfree,
   no_invariant_valuation not_fixpointfree point⟩

end Boundary
end OnlineIssuance
