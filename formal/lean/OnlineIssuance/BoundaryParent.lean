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

  3. STATES (does NOT prove) the cross-repo assembly TARGET: the single
     theorem that would fuse GU's involution leg, TI's diagonal leg, and TaF's
     first/third-person composite, with the not-yet-Lean pieces named as
     explicit hypotheses and the body left `sorry`. A companion
     `..._skeleton` theorem proves the abstract conclusion from the abstract
     hypotheses, isolating exactly what is discharged (the logic) from what is
     open (the cross-repo instantiation of the assembled category).

Mathlib-free (core Lean only; `Function.Injective` and the diagonal argument
are Init-level). Scope: INDEPENDENT-LEGS. The TaF composite is a separate gated
wave, appearing only as a named hypothesis in the target, never formalized.

No claim movement: TI-C003 / TI-C019 / TI-C020 untouched. New file; edits
nothing. claim_status_change: none.
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
  no_self_closure T H.fpf

/-- **Conclusion (b) in the package.** No `alpha`-invariant valuation exists;
every definite valuation is an external, symmetry-breaking selection. -/
theorem ParentHypotheses.no_invariant_valuation {A B : Type _}
    (H : ParentHypotheses A B) :
    ¬ ∃ v : A → B, InvariantValuation H.alpha v :=
  no_invariant_valuation H.fpf H.point

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

/-! ## Leg 3: the cross-repo assembly TARGET (STATED, NOT PROVED)

The single theorem that would fuse the three repos' legs. GU's l1-assembly
swing (fixture grade) exhibits the assembled category `C_read` of six reading
classes over ONE Z/2; TI holds leg (a) (this file + Diagonal.lean); TaF holds
the first/third-person composite. The pieces that are NOT yet at theorem-prover
grade are named as explicit hypotheses; the body is `sorry`.

The companion `..._skeleton` below PROVES the abstract conclusion from the
abstract hypotheses with NO `sorry`, so the reader can see precisely what is
discharged (the categorical/arithmetic logic) versus what the `sorry` in the
TARGET stands for (that `alpha`, `T`, and the label map genuinely ARISE from
GU's assembled `C_read` and coincide with TI's diagonal witness and TaF's gap —
a cross-repo instantiation Lean cannot witness from inside TI). -/

/-- **CROSS-REPO ASSEMBLY TARGET (leg 3 — STATED, NOT PROVED).**
Hypotheses (each a named missing piece):
  * `H_assembly`  — GU l1-assembly: the reading classes `Read` form one
                    category over the single label object `B` with finite
                    products, terminal object, and an equivariant diagonal;
                    admissibility predicates are the maps `Read → B`.
                    (Fixture grade in GU; NOT Lean-verified.)
  * `alpha`, `H_involution`, `H_fpf` — GU/TI leg (b): the single fixpoint-free
                    involution on `B`. (Involution arithmetic PROVED in
                    `BoundaryInvolution.lean`; the identification that this is
                    the ONE assembled `alpha` is GU-side.)
  * `T`, `H_leg_a` — TI leg (a): the assembled firewall-closure candidate, and
                    the identification of TI's diagonal productivity
                    (`diagName_not_mem`) with the point-surjectivity failure of
                    `T`. (Cross-repo identification; NOT Lean-verified here.)
  * `H_taf`       — TaF composite: the first/third-person finality gap is the
                    joint conclusion-level analogue of (a) ∧ (b). The TaF
                    mechanism is now known to be a causal-past retraction
                    (`pi ∘ pi = pi`, oriented, non-invertible), not this
                    file's fixpoint-free involution. `H_taf : True` remains
                    only an inert placeholder; a later typed assembly must
                    keep the retraction and involution legs distinct.
                    (Separate gated wave; NOT Lean.)
Conclusion: the unified boundary law, (a) ∧ (b), over the assembled data. -/
theorem cross_repo_boundary_law_TARGET
    {Read B : Type _}
    (H_assembly : True)
    (alpha : B → B) (H_involution : Involution alpha) (H_fpf : FixpointFree alpha)
    (T : Read → Read → B) (H_leg_a : True)
    (H_taf : True)
    (point : Read) :
    (¬ WeaklyPointSurjective T)
    ∧ (¬ ∃ v : Read → B, InvariantValuation alpha v) :=
  sorry

/-- Companion: the ABSTRACT SKELETON of the target, PROVED (no `sorry`). Given
the involution/fixpoint-free hypotheses and an inhabited `Read`, the boundary
law for the specific `T` follows from the leg-(a) and leg-(b) lemmas. This
isolates the `sorry` in the TARGET as standing ONLY for the cross-repo
instantiation (that these `alpha`, `T` arise from GU's `C_read` and TI's/TaF's
faces), not for any gap in the logic. -/
theorem cross_repo_boundary_law_skeleton
    {Read B : Type _}
    {alpha : B → B} (H_fpf : FixpointFree alpha)
    (T : Read → Read → B) (point : Read) :
    (¬ WeaklyPointSurjective T)
    ∧ (¬ ∃ v : Read → B, InvariantValuation alpha v) :=
  ⟨no_self_closure T H_fpf,
   no_invariant_valuation H_fpf point⟩

end Boundary
end OnlineIssuance
