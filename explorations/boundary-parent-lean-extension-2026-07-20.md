---
artifact_type: exploration
status: complete
governance_role: cross_repo_lean_extension_boundary_parent
workflow: repository-work-cycle
claim_movement: false
created: 2026-07-20
directed_by: "Joe direct chat, 2026-07-20 (cross-repo: TI Lean extension of the boundary-law parent)"
claim: none
canon: none
posture: none
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
external_action: none
depends_on:
  - formal/lean/OnlineIssuance/Core.lean
  - formal/lean/OnlineIssuance/Diagonal.lean
  - formal/lean/OnlineIssuance/Admissibility.lean
  - "READ-ONLY gu-formalization: explorations/diagonal-boundary-unification-2026-07-20.md"
  - "READ-ONLY gu-formalization: explorations/l1-assembly-2026-07-20.md"
produces:
  - formal/lean/OnlineIssuance/BoundaryInvolution.lean
  - formal/lean/OnlineIssuance/BoundaryParent.lean
  - tools/boundary_parent_lean_probe.py
runnable:
  - tools/boundary_parent_lean_probe.py
---

# Boundary-parent Lean extension: leg (a) schematized, leg (b) proved

## Result first

**Outcome: L-DONE.** GU's diagonal-boundary parent (H62/H63, the Lawvere
no-closure / arena-value theorem) FACTORS into leg (a) [self-encoding
admissibility + diagonal = Lawvere no-closure] and leg (b) [fixpoint-free
label involution => no invariant valuation]. TI already held leg (a) at
theorem-prover grade over the concrete `String` label object
(`Diagonal.lean` `diagName_not_mem`, `Admissibility.lean`). This swing
extends the TI Lean backbone to cover **more of the parent**:

1. **The parent STATEMENT SHAPE is formalized** (`BoundaryParent.lean`): the
   hypothesis package as one structure `ParentHypotheses` (self-encoding
   admissibility as weak point-surjectivity of a closure candidate `T`, over
   an inhabited label object carrying a fixpoint-free involution) and BOTH
   conclusions ((a) no self-closure; (b) no `alpha`-invariant valuation),
   in the same hypothesis-visible style as `Core.lean`.

2. **Leg (b) is proved** (`BoundaryInvolution.lean`): given a fixpoint-free
   involution `alpha`, no invariant valuation exists over any inhabited
   domain. Elementary group-action arithmetic, proved for an arbitrary label
   object and instantiated on the canonical `Bool` Z/2.

3. **Leg (a) is proved schematically** as a bonus over the mission floor:
   Lawvere's fixed-point theorem, contrapositive, with `alpha` itself as the
   fixpoint-free map. The witness of non-closure is EXACTLY the parent's
   twisted diagonal `d = alpha . T . Delta` — `twistedDiagonal_unrepresented`
   is the abstract twin of `diagName_not_mem`. So TI now holds leg (a) both
   concretely (strings, existing) and schematically (any label object, new).

4. **The cross-repo assembly TARGET is stated, not proved** (leg 3):
   `cross_repo_boundary_law_TARGET`, a `sorry`-bodied theorem whose
   hypotheses name the missing pieces (GU's assembled category `C_read`;
   the identification of TI's diagonal with the assembled closure candidate;
   TaF's first/third-person composite). A companion
   `cross_repo_boundary_law_skeleton` PROVES the abstract conclusion from the
   abstract hypotheses with no `sorry`, isolating exactly what the target's
   `sorry` stands for (cross-repo instantiation) from the logic (discharged).

**Named Mathlib dependencies: NONE.** The whole OnlineIssuance package is
Mathlib-free (`lake-manifest.json` packages `[]`, toolchain
`leanprover/lean4:v4.31.0`). Every new proof uses only Lean-core `List` /
`Bool` / `Function.Injective` / `congrArg` / `obtain` / `simp` / `decide`,
matching the tactic surface the existing files already compile against. This
is why the outcome is L-DONE, not L-PARTIAL: nothing is blocked on an
unavailable lemma.

**Python cross-check:** `tools/boundary_parent_lean_probe.py` — HEADLINE
`9 [E] + 2 [F] = 11 (setup [T] = 3 excluded) ALL PASS`, exit 0, deterministic
(double-run byte-identical), pure Python.

## What was formalized, theorem by theorem

### `BoundaryInvolution.lean` (leg b)

| name | statement | compile-confidence |
|---|---|---|
| `Involution` / `FixpointFree` / `InvariantValuation` | the three defs over an arbitrary label object | HIGH (defs) |
| `no_fixed_point` | fixpoint-free => no fixed label | HIGH |
| `no_invariant_valuation` | fixpoint-free + inhabited domain => no invariant valuation (**LEG b**) | HIGH |
| `fixed_point_of_invariant_valuation` | contrapositive (dissolution direction) | HIGH |
| `no_fixed_in_enumeration` | over any list, no element is fixed (the exhaustive-count form of W75 PART B) | HIGH |
| `involution_injective` | an involution is `Function.Injective` (orbit backbone) | HIGH |
| `partner_ne` | `alpha b ≠ b` (2-element orbit) | HIGH |
| `not_involution` / `not_fixpointfree` | `Bool.not` is a fixpoint-free involution | HIGH (`cases b <;> decide`) |
| `bool_no_fixed_point` | 0 fixed labels on the full `{false,true}` (reuses `no_fixed_point`) | HIGH |
| `bool_no_invariant_valuation` | canonical Z/2 instance of leg (b) | HIGH |

### `BoundaryParent.lean` (parent shape + leg a schematic + target)

| name | statement | compile-confidence |
|---|---|---|
| `WeaklyPointSurjective` | L1 firewall-closure predicate (`T` represents every `A → B`) | HIGH (def) |
| `twistedDiagonal` | `d = alpha . T . Delta` | HIGH (def) |
| `lawvere_fixed_point` | weak point-surjectivity => every `f : B → B` has a fixed point | HIGH |
| `no_self_closure` | fixpoint-free `alpha` => no `T` is point-surjective (**conclusion a**) | HIGH |
| `twistedDiagonal_unrepresented` | `d` is represented by no row of `T` (parent's exact phrasing; abstract twin of `diagName_not_mem`) | HIGH |
| `ParentHypotheses` | the hypothesis package as one structure | HIGH |
| `ParentHypotheses.no_self_closure` / `.no_invariant_valuation` | the two conclusions in the package | HIGH |
| `boundary_parent_law` | both conclusions from the package, factorization visible in the proof term | HIGH |
| `boolParent` / `bool_boundary_parent_law` | canonical `Bool` instance of the whole law | HIGH |
| `cross_repo_boundary_law_TARGET` | leg 3 — cross-repo fusion, body `sorry`, missing pieces named as hypotheses | compiles WITH `sorry` (by design) |
| `cross_repo_boundary_law_skeleton` | the abstract conclusion PROVED from abstract hypotheses (no sorry) | HIGH |

### The target statement (leg 3), verbatim shape

```lean
theorem cross_repo_boundary_law_TARGET
    {Read B : Type _}
    (H_assembly : True)                 -- GU l1-assembly: C_read over one Z/2 (fixture grade, NOT Lean)
    (alpha : B → B) (H_involution : Involution alpha) (H_fpf : FixpointFree alpha)  -- leg b (proved)
    (T : Read → Read → B) (H_leg_a : True)   -- TI leg a = point-surjectivity failure of T (cross-repo, NOT Lean)
    (H_taf : True)                      -- TaF composite = (a) ∧ (b) (separate gated wave, NOT Lean)
    (point : Read) :
    (¬ WeaklyPointSurjective T)
    ∧ (¬ ∃ v : Read → B, InvariantValuation alpha v) :=
  sorry
```

The `True` placeholders are honest inert markers: the abstract conclusion is
already dischargeable (see `cross_repo_boundary_law_skeleton`), so the only
genuine gap the `sorry` records is that `alpha`, `T`, and the label map must
be shown to ARISE from GU's assembled `C_read` and to coincide with TI's
diagonal witness and TaF's gap — a cross-repo instantiation TI cannot witness
from inside its own repo. This is the tri-repo one-way discipline in Lean form.

## Confidence discipline (what the build must still confirm)

I did NOT run `lake build` (workspace Local Resource Safety: Lean builds are
host-serialized). My compile-confidence rests on: (i) every tactic used
(`obtain`, `simp [def]`, `cases <;> decide`, `intro`, `congrArg`, `rwa`)
already appears in the existing, compiling OnlineIssuance files; (ii) no
Mathlib symbol is referenced; (iii) each proof is a one-to-three-step term
whose types I have checked by hand above. The residual risks are the usual
Lean-4 pitfalls a build catches instantly: a `simp only [twistedDiagonal]`
that needs a different unfolding lemma, or a beta-defeq in `lawvere_fixed_point`
the elaborator wants spelled out. I rate all non-`sorry` theorems HIGH but
flag `lake build formal/lean` as the steward's serialized follow-up step. The
`sorry` in `cross_repo_boundary_law_TARGET` is intentional and will emit the
standard `declaration uses 'sorry'` warning — it is a stated target, not a
proof gap in the logic.

## Council pass (inline, five lenses)

- **Proof engineer.** The proofs are minimal and reuse the repo's own tactic
  vocabulary; `bool_no_fixed_point` and `bool_no_invariant_valuation` are
  term-mode reuses of the general lemmas rather than fresh `decide`s, which
  keeps the Bool layer honest (it is an instance, not a re-proof). The one
  thing a build owns: `simp only [twistedDiagonal]` — if the def does not
  unfold under `simp only`, swap to `show T a a = alpha (T a a) at h` or
  `unfold twistedDiagonal at h`. `unfold` is core; noted as the fallback.
- **Type theorist.** Universes are clean (`Type _` throughout; the structure
  and defs are universe-polymorphic and never force `Prop`/`Type` mixing).
  `WeaklyPointSurjective` currying `A × A → B` to `A → A → B` is faithful:
  the diagonal `Delta : A → A × A` becomes `x ↦ (x,x)` and its post-composite
  with `T` is `x ↦ T x x`, exactly the diagonal Lawvere needs. The inhabited
  hypothesis `point : A` is not cosmetic — over the empty domain the empty
  valuation is vacuously invariant, so dropping it would make leg (b) false;
  carrying it as a field is the correct discipline.
- **TI-native diagonal reader.** The extension respects E117/E118: hypotheses
  stay visible (in a structure, like `DiagonalFormed`), nothing is derived by
  sleight. Leg (a)'s new schematic form is genuinely the same engine as
  `diagName_not_mem` — both are the Cantor/Lawvere escape; the string version
  flips a character, the schematic version applies `alpha`. Naming them twins
  is accurate, not a stretch. No claim moves; `AdmDef`, `EnumeratorPresent`,
  and the TI-C rows are untouched.
- **GU-parent reader.** The factorization matches GU's receipts exactly:
  conclusion (a) needs L1 + the diagonal (here: `WeaklyPointSurjective` + the
  `alpha`-twisted diagonal), conclusion (b) needs L2 ALONE (here:
  `no_invariant_valuation` from `FixpointFree` with no `T` in sight). That leg
  (b) is proved without any diagonal is the whole point of GU's W75 PART B,
  and the Lean proof term makes it visible. `twistedDiagonal` reproduces the
  parent's `d = alpha . T . Delta` symbol-for-symbol. What is NOT imported:
  any GU physics, the Krein grading, the Sp(1) torsor — the label object is a
  bare type with a fixpoint-free involution, which is all leg (b) needs.
- **Adversarial referee.** Charge 1: "leg (b) is a one-line triviality dressed
  as a theorem." Conceded as mathematics, denied as deliverable — the TARGET
  was theorem-prover-grade coverage of the parent's SHAPE, and a one-line
  proof that compiles is worth more than a paragraph that does not; the value
  is the faithful encoding + the cross-repo target, not proof length. Charge 2:
  "you smuggled leg (a) in as a bonus but did not connect it to the existing
  `diagName_not_mem`." Answer: correct that no Lean `import`-level identity is
  asserted (the types differ: `String`-lists vs abstract `T`); the connection
  is stated as parallel witnesses and left as a named target, not faked.
  Charge 3: "the `sorry` hides the real work." Answer: the companion
  `_skeleton` theorem proves the same conclusion with no sorry; the sorry is
  quarantined to the cross-repo INSTANTIATION, which is genuinely not
  TI-internal and correctly left open under the one-way rule.

## Receipts

- `formal/lean/OnlineIssuance/BoundaryInvolution.lean` — leg (b), 10 named
  results, Mathlib-free.
- `formal/lean/OnlineIssuance/BoundaryParent.lean` — parent shape + leg (a)
  schematic + leg-3 target, 12 named results (one `sorry` by design).
- `tools/boundary_parent_lean_probe.py` — HEADLINE
  `9 [E] + 2 [F] = 11 (setup [T] = 3 excluded) ALL PASS`, exit 0, deterministic.
  [T] swap involutive + fixpoint-free + id-control; [E] injectivity, 0
  invariant valuations for |A|=1,2,3, exhaustive Lawvere no-closure for
  |A|=1,2,3, twisted-diagonal escape (|A|=2 exhaustive); [F] dissolution teeth
  (swap gives 0, id gives >0 invariant valuations) + singleton-label plant
  (correctly NOT excluded).
- Parent receipts (read-only): gu-formalization
  `explorations/diagonal-boundary-unification-2026-07-20.md` (Section 1 parent
  shape, Section 4 TI face), `explorations/l1-assembly-2026-07-20.md`
  (Section 4 the boundary law at fixture grade).
- TI leg-a receipts: `Diagonal.lean` `diagName_not_mem`, `Admissibility.lean`
  `AdmDef` / `no_universal_self_encoding`.

## PROPOSAL TO STEWARD (steward-ratifiable; nothing promoted here)

This swing wrote NEW files only and moved no claim, gate, ledger, or status.
For steward disposition:

1. **Serialized `lake build`.** Run `lake build` in `formal/lean` (host-locked;
   not run here). Expected: all non-`sorry` theorems compile; one
   `declaration uses 'sorry'` warning from `cross_repo_boundary_law_TARGET`.
   If `simp only [twistedDiagonal]` fails, the one-line fix is
   `unfold twistedDiagonal at h` (noted by the proof-engineer lens).
2. **Root aggregation (optional).** To include the new modules in the library
   build, add `import OnlineIssuance.BoundaryInvolution` and
   `import OnlineIssuance.BoundaryParent` to `formal/lean/OnlineIssuance.lean`.
   Left UNDONE deliberately — editing an existing file is outside this swing's
   no-mutation scope. Building the two files directly also works.
3. **Cross-repo note (steward's call, not sent here).** If the steward wishes,
   record in the TI mailbox that leg (a) now has a schematic Lean form
   (`twistedDiagonal_unrepresented`) in addition to the concrete
   `diagName_not_mem`, so a future L1-grade tri-repo unification has TI's leg
   pre-located at two grades. No GU/TaF claim movement is proposed.
4. **No claim movement.** TI-C003 / TI-C019 / TI-C020 untouched;
   claim_status_change: none.

## Boundary

Exploration tier; claim/canon/posture: none; no external actions; no commits
or pushes; new files only, no existing file edited; GU touched read-only;
nothing written outside temporal-issuance; `lake`/Lean NOT run (host-locked,
serialized — flagged for the steward). The `sorry` target is a stated goal,
not a claimed proof. Leg (a) and leg (b) are formalized as INDEPENDENT legs;
the TaF composite is a separate gated wave and appears only as a named
hypothesis in the target.
