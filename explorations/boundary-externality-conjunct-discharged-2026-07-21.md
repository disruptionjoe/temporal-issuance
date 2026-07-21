---
artifact_type: exploration
status: complete
governance_role: cross_repo_lean_externality_conjunct_discharge
workflow: repository-work-cycle
claim_movement: false
created: 2026-07-21
directed_by: "Joe direct chat, 2026-07-21 (scoped Lean discharge; GU oracle-relative Prong III handoff)"
claim: none
canon: none
posture: none
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
external_action: none
depends_on:
  - formal/lean/OnlineIssuance/BoundaryInvolution.lean
  - formal/lean/OnlineIssuance/BoundaryParent.lean
  - "mailbox: temporal-issuance/archive/20260721-discharge-externality-conjunct-no-invariant-valuation.md"
  - "READ-ONLY gu-formalization: explorations/oracle-relative-prongIII-exhaustiveness-theorem-2026-07-21.md"
produces:
  - formal/lean/OnlineIssuance/BoundaryParent.lean
  - tools/boundary_externality_conjunct_split_probe.py
runnable:
  - tools/boundary_externality_conjunct_split_probe.py
---

# Boundary externality conjunct discharged: the TARGET's `sorry` split

## Result first

**Outcome: L-DONE.** The `sorry` in
`cross_repo_boundary_law_TARGET` (`BoundaryParent.lean`) is now **split**. The
EXTERNALITY conjunct — `¬ ∃ v : Read → B, InvariantValuation alpha v`
(conclusion b) — is **PROVED with no `sorry`**, discharged directly from the
already-proved `no_invariant_valuation H_fpf point` (a fixpoint-free involution on
an inhabited domain admits no invariant valuation). **Only** the self-closure
conjunct — `¬ WeaklyPointSurjective T` (conclusion a, the diagonal /
Lawvere-fixed-point leg) — keeps the `sorry`. That remaining `sorry` carries the
GU-side product-uniform norm-resolvent boundary-value theorem (open theorem O-b),
an analysis deliverable, plus the cross-repo instantiation of `T` — it was NOT
weakened or deleted.

The two conjuncts genuinely factor: the TARGET conclusion is an `And`, its second
component depends only on `H_fpf` and `point` (never on `T`, the product carrier,
or L1), so the split is honest, not forced.

## What changed

Edited `formal/lean/OnlineIssuance/BoundaryParent.lean` only (plus this receipt
and one probe). `BoundaryInvolution.lean` untouched — no helper was needed; every
ingredient (`no_invariant_valuation`, `not_involution`, `not_fixpointfree`) was
already present. Mathlib-free; no new imports.

1. **`cross_repo_boundary_law_TARGET` body split.**
   `sorry` → `⟨sorry, no_invariant_valuation H_fpf point⟩`. The externality
   conjunct is now the same proof term as in the already-proved
   `cross_repo_boundary_law_skeleton`; only the self-closure conjunct is `sorry`.
   Doc comment updated with the SPLIT STATUS (what is proved vs. what stays open,
   and why).

2. **Concrete GU-instance witness `k_s_flip_externality`** (new theorem, no
   `sorry`). The K_S-sign flip `alpha = Ad(U_h)` on the two-element
   Krein-orientation label `{+K_S, -K_S}` is realized in core Lean by `Bool` with
   `alpha = Bool.not` (`not_involution`, `not_fixpointfree`, kernel-decided). Over
   any inhabited reading space there is no `not`-invariant valuation — the
   externality theorem thus has a concrete, non-vacuous model. Doc comment traces
   it to GU's `U_h K_S U_h⁻¹ = -K_S` (deck-oddness, defect ~1e-12, machine-exact
   GU-side — explicitly NOT a Lean obligation).

3. **`k_s_flip_hypotheses_inhabited`** (new theorem, no `sorry`). Witnesses that
   the TARGET's involution hypotheses (`H_involution`, `H_fpf`) have a genuine
   model: `Bool.not` satisfies both `Involution` and `FixpointFree`, paired with
   the externality conclusion it forces. Makes the non-vacuity explicit.

4. Module header docstring (point 3) updated to describe the split.

## What is now proved (no `sorry`) vs. what `sorry` remains

**Proved, no `sorry`:**
- `cross_repo_boundary_law_TARGET`, conjunct (b) — externality — via
  `no_invariant_valuation H_fpf point`.
- `k_s_flip_externality` — concrete GU instance of the externality conjunct.
- `k_s_flip_hypotheses_inhabited` — non-vacuity of the involution hypotheses.
- (unchanged, still no `sorry`) `no_invariant_valuation`,
  `cross_repo_boundary_law_skeleton`, `lawvere_fixed_point`, `no_self_closure`,
  `twistedDiagonal_unrepresented`, `boundary_parent_law`, `bool_boundary_parent_law`.

**`sorry` remains (intentionally, unchanged in load):**
- `cross_repo_boundary_law_TARGET`, conjunct (a) — `¬ WeaklyPointSurjective T`.
  This is the diagonal / self-closure leg. Its load: the GU-side **product-uniform
  norm-resolvent boundary-value theorem** (O-b, ~N^1.35 sup-mode divergence) plus
  the cross-repo instantiation of `T` from GU's assembled `C_read`. The LOGIC of
  leg (a) given a genuine fixpoint-free `alpha` is already proved (`no_self_closure`
  / `cross_repo_boundary_law_skeleton`, no `sorry`); the `sorry` stands ONLY for
  the operator-grade analysis obstruction and the assembly identification — not a
  gap in the categorical/arithmetic logic. It is an analysis deliverable, not a
  Lean task yet, and was deliberately left open.

## Compile-confidence (hand-checked; `lake` NOT run)

`lake build` was NOT run (host-locked, serialized to the steward). Types
hand-checked against the repo's proven tactic surface:

- **`cross_repo_boundary_law_TARGET`** — HIGH. Second component
  `no_invariant_valuation H_fpf point : ¬ ∃ v : Read → B, InvariantValuation alpha v`
  is byte-for-byte the same application already elaborated in
  `cross_repo_boundary_law_skeleton` (which compiles). First component `sorry`
  elaborates to any Prop. `⟨_, _⟩` is the `And` constructor. Expect the standard
  `declaration uses 'sorry'` warning (intended). The unused hypotheses
  (`H_assembly`, `H_involution`, `H_leg_a`, `H_taf`) were already unused in the
  prior all-`sorry` body — no new linter surface.
- **`k_s_flip_externality`** — VERY HIGH. Identical in form to the compiling
  `bool_no_invariant_valuation` in `BoundaryInvolution.lean`
  (`no_invariant_valuation not_fixpointfree a₀`); only the binder name differs.
- **`k_s_flip_hypotheses_inhabited`** — HIGH. `⟨not_involution, not_fixpointfree,
  no_invariant_valuation not_fixpointfree point⟩` against
  `Involution Bool.not ∧ FixpointFree Bool.not ∧ ¬ ∃ …`; right-associative `And`
  flattens under the anonymous constructor. All three components are existing
  compiling terms.

**Steward follow-up (serialized):** run `lake build formal/lean` (or the package
target) to confirm; expect success with exactly one `sorry` warning
(`cross_repo_boundary_law_TARGET`, conjunct a). No other `sorry` is introduced.

## Cross-check probe

`tools/boundary_externality_conjunct_split_probe.py` — foreground, **exit 0**,
deterministic (double-run byte-identical), pure-Python, seeded 20260721, no
network. Models B = {+K_S, -K_S} as {+1, -1} with `alpha` = the K_S-sign flip
(negation). Confirms by exhaustive finite enumeration: (b) discharges
non-vacuously (0 invariant valuations at |Read| = 1,2,3; the flip is a
fixpoint-free involution); teeth hold (alpha = id reopens: invariant valuations
reappear); (a) is recorded as declared-open, not attempted.
HEADLINE: `4 [E] + 1 [F] = 5 (declared-open/setup [T] = 3) ALL PASS`.

## Boundary

Exploration tier. Edited exactly the Lean file `BoundaryParent.lean`, this
receipt, and one new probe. `BoundaryInvolution.lean` and every claim / canon /
verdict / ledger / gate file untouched; GU repo untouched (READ-ONLY input only).
No claim movement (TI-C003 / TI-C019 / TI-C020 untouched). No commit/push (steward
reviews + commits). No external actions. `lake build` remains the steward's
serialized gate.
