/-
OnlineIssuance^LC — Boundary-parent extension, LEG B: the involution leg.

Cross-repo swing (Joe direct chat, 2026-07-20). GU's diagonal-boundary parent
(gu-formalization explorations/diagonal-boundary-unification-2026-07-20.md,
l1-assembly-2026-07-20.md) FACTORS into:
  - leg (a): self-encoding admissibility + diagonal = Lawvere no-closure
             (TI's existing expressiveness-threshold package: Diagonal.lean /
             Admissibility.lean already carry this at theorem-prover grade);
  - leg (b): a FIXPOINT-FREE label involution => NO invariant valuation.

This module formalizes leg (b) — the elementary group-action arithmetic GU's
family proves per-sector at fixture grade (W75 PART B: an exhaustive
fixed-point count under the swap), now at theorem-prover grade over an
arbitrary label object. It is deliberately Mathlib-free (the whole OnlineIssuance
package is: lean-toolchain v4.31.0, no `require mathlib`), using only Lean core
`List`/`Bool`/`Function`.

Scope discipline: INDEPENDENT-LEGS only. This is leg (b) in isolation; the
Lawvere no-closure composite (which needs leg (a)'s diagonal) is stated and
proved in `BoundaryParent.lean`. The TaF first/third-person composite is a
SEPARATE gated wave and is not formalized.

No claim movement: TI-C003 / TI-C019 / TI-C020 untouched. This file adds new
definitions and theorems only; it edits nothing.
claim_status_change: none.
-/

namespace OnlineIssuance
namespace Boundary

/-! ## The label object and its structure map -/

/-- `alpha` is an involution on the label object `B`: applying it twice is the
identity. This is the parent's `J^2 = 1` / `alpha . alpha = id`. -/
def Involution {B : Type _} (alpha : B → B) : Prop := ∀ b, alpha (alpha b) = b

/-- `alpha` is fixpoint-free: it fixes no label. This is the parent's L2 (the
firewall is nontrivial; the swap has no fixed boundary grade). -/
def FixpointFree {B : Type _} (alpha : B → B) : Prop := ∀ b, alpha b ≠ b

/-- An `alpha`-invariant valuation on a domain `A`: a map `v : A → B` every one
of whose values is fixed by `alpha`. The parent's `alpha`-invariant valuation
`p : A → B` (an internal, orientation-free commitment to a definite label). -/
def InvariantValuation {A B : Type _} (alpha : B → B) (v : A → B) : Prop :=
  ∀ a, alpha (v a) = v a

/-! ## Leg (b), the pointwise core: no fixed label -/

/-- Restatement: a fixpoint-free involution has no fixed point. Trivial, but it
is the exact content the parent's conclusion (b) rides on, and every result
below reduces to it. -/
theorem no_fixed_point {B : Type _} {alpha : B → B}
    (hff : FixpointFree alpha) : ¬ ∃ b, alpha b = b := by
  intro h
  obtain ⟨b, hb⟩ := h
  exact hff b hb

/-! ## Leg (b), the valuation form (the parent's conclusion (b))

The domain `A` must be inhabited: over the empty domain the (unique) empty
valuation is vacuously invariant, so nonemptiness is a genuine hypothesis, made
visible as the explicit witness `a₀ : A`. -/

/-- **LEG (b).** Given a fixpoint-free involution `alpha` on the label object
and an inhabited domain, NO `alpha`-invariant valuation exists. Every definite
valuation is therefore a symmetry-breaking selection: the orientation datum is
external to any internal map. Proof is one line of group-action arithmetic —
an invariant value would be a fixed point of `alpha`. -/
theorem no_invariant_valuation {A B : Type _} {alpha : B → B}
    (hff : FixpointFree alpha) (a₀ : A) :
    ¬ ∃ v : A → B, InvariantValuation alpha v := by
  intro h
  obtain ⟨v, hv⟩ := h
  exact hff (v a₀) (hv a₀)

/-- Contrapositive convenience: if some `alpha`-invariant valuation exists over
an inhabited domain, `alpha` has a fixed point (the dissolution direction — the
parent's `alpha = id` control reopens exactly here). -/
theorem fixed_point_of_invariant_valuation {A B : Type _} {alpha : B → B}
    (v : A → B) (hv : InvariantValuation alpha v) (a₀ : A) :
    ∃ b, alpha b = b :=
  ⟨v a₀, hv a₀⟩

/-! ## Leg (b), the exhaustive-count form (mirrors the probe's action arithmetic)

W75 PART B counts fixed points under the swap over a finite enumeration and
finds ZERO. Here: over ANY enumeration `l : List B`, no element is a fixed
point. No fragile filter lemmas — the statement is the count made total. -/

/-- Over any enumeration of labels, a fixpoint-free involution fixes none of
them: the exhaustive fixed-point count is empty, for every list. -/
theorem no_fixed_in_enumeration {B : Type _} {alpha : B → B}
    (hff : FixpointFree alpha) (l : List B) : ∀ b ∈ l, alpha b ≠ b :=
  fun b _ => hff b

/-! ## Involutions are injective (orbit structure)

The pairing that makes the action free: an involution is its own inverse, hence
a bijection, so labels come in `alpha`-orbits. Used by the referee lens as the
"orbits partition" backbone; `Function.Injective` is Lean-core. -/

/-- An involution is injective. -/
theorem involution_injective {B : Type _} {alpha : B → B}
    (hinv : Involution alpha) : Function.Injective alpha := by
  intro x y hxy
  have : alpha (alpha x) = alpha (alpha y) := congrArg alpha hxy
  rwa [hinv x, hinv y] at this

/-- A fixpoint-free involution has no 2-cycle collapse: `alpha b` and `b` are
always distinct partners (the orbit through `b` has two elements). -/
theorem partner_ne {B : Type _} {alpha : B → B}
    (hff : FixpointFree alpha) (b : B) : alpha b ≠ b := hff b

/-! ## The canonical Z/2 label: `Bool` with `not`

The parent's label object is `B = {+,-}`. Its concrete realization is `Bool`
with `alpha = not`. Everything above then computes; these are the theorem-prover
analogue of the Python probe's `swap` battery, decided by the kernel. -/

/-- `not` is an involution on `Bool` (each label case kernel-decided). -/
theorem not_involution : Involution Bool.not := by
  intro b; cases b <;> decide

/-- `not` is fixpoint-free on `Bool`: the swap fixes neither `+` nor `-`. -/
theorem not_fixpointfree : FixpointFree Bool.not := by
  intro b; cases b <;> decide

/-- The exhaustive fixed-point count over the full label object `{false, true}`
is ZERO — W75 PART B's count, here as non-existence of a `not`-fixed label,
reusing the fixpoint-free lemma through `no_fixed_point`. -/
theorem bool_no_fixed_point : ¬ ∃ b : Bool, Bool.not b = b :=
  no_fixed_point not_fixpointfree

/-- Concrete leg (b): over any inhabited domain there is no `not`-invariant
`Bool`-valuation. The canonical instance of `no_invariant_valuation`. -/
theorem bool_no_invariant_valuation {A : Type _} (a₀ : A) :
    ¬ ∃ v : A → Bool, InvariantValuation Bool.not v :=
  no_invariant_valuation not_fixpointfree a₀

end Boundary
end OnlineIssuance
