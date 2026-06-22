---
artifact_type: run_record
run_id: RUN-0028
status: complete
governance_role: construct_or_refute_realization_functor
trigger: next_trigger_plan_RUN-0027
workflow: W000-repo-steward-cycle
constitutional: false
claims_touched:
  - TI-C007
  - TI-C008
  - TI-C009
  - TI-C010
---

# RUN-0028: Construct or Refute a Minimal Nontrivial Realization Functor F

## Timestamp

2026-06-21 (chat-executed steward pass; committed via Claude Code automation)

## Trigger

`agent-governance/NEXT-TRIGGER-PLAN.md` current recommendation (set by RUN-0027):
construct or refute a minimal nontrivial `F: ExtCat -> LorHist(M, eta, A)`, with the
RUN-0027 nontriviality gate `same <=_S / different Ext_S invariant`.

## Workflow

W000 Repo Steward Cycle -> direct construct/refute pass (no new dynamic workflow needed).

## Subagents (simulated in one record; parallelization unavailable in chat env)

Category Error Auditor, Mathematical Minimalist, Lorentzian geometer, Relativity
physicist, GU skeptic, NULL-SURVIVOR advocate, Time-as-Finality boundary keeper.

## Interpretation Fixed Before Work (auditable)

"Same `<=_S`, different `Ext_S` invariant" is read as a **parallel morphism pair**
`e1, e2 : S => S'` (same domain and codomain). The induced thin reflection sees only
`Hom(S,S') != empty`, so it cannot separate `e1` from `e2`; any separation must come
from morphism-level `Ext_S` structure (RUN-0025 result). The broader reading
(order-isomorphic subcategories mapping differently) only adds constraints, so it can
only strengthen the obstruction below, never weaken it.

## Strongest Version Generated (before attack)

Steelman F: `ExtCat` carries morphism-level invariants beyond `<=_S`; choose `LorHist`
objects rich enough to be non-unique boundary-value problems (curved/multiply-connected
`M`, multiple classical solutions, topological/internal-charge sectors). Then a parallel
pair `e1, e2` can map to two genuinely distinct on-shell histories `F(e1) != F(e2)`
sharing boundary data — a real Lorentzian-observable difference at the level of
**admissible history class**. Under this reading a nontrivial F is constructible.

## Central Result: Boundary-Determination Obstruction (BDO)

**Lemma (BDO, Minkowski/Poincare control case).**
In `LorHist(M, eta, A)` with `A` Poincare-invariant and Noether-regular, the total
conserved four-momentum `p^mu` of an on-shell morphism `h: B0 -> B1` is a function of
the boundary objects `(B0, B1)` and the fixed external `(M, eta, A)` alone — not of which
on-shell history realizes that boundary pair. Conservation makes `p^mu` constant along
the history, so it is read off either boundary slice; if objects encode full Cauchy /
asymptotic data, `p^mu` is an **object-level** invariant `p^mu[B]`.

Consequence: for any functor F and any parallel pair `e1, e2 : S => S'`,
`p^mu(F(e1)) = p^mu[F(S')] = p^mu(F(e2))`. Therefore `p^mu . F` factors through the thin
reflection `Preord(<=_S)`. The mass-energy observable is **blind** to every source
distinction the nontriviality gate is about. QED for the control case.

This is the precise, model-level form of E008's `only_imported_physics` failure
condition and the literal trigger of E008's `kill_test` ("...fails to change Lorentzian
energy-momentum data").

## Verdict Split (the epistemic payload)

- **"No F exists" is REFUTED.** A nontrivial F exists at the *admissible-history-class*
  rung (parallel extensions -> distinct on-shell sectors with the same boundary data).
- **"Nontrivial-at-mass-energy F" is OBSTRUCTED.** By BDO, the same-`<=_S` /
  different-`Ext_S` distinction cannot reach `p^mu` or the mass shell in the control
  case. To move `p^mu` you must change boundary objects — but that changes the induced
  order (`S -> S''` not `S -> S'`), breaking the "same `<=_S`" premise. Nontriviality and
  energy-momentum-relevance are **mutually exclusive** here.

Net: the thing that carries genuine `Ext_S` structure (history class / charge sector) is
exactly the thing that does **not** move energy-momentum; the thing TI wanted
(mass-energy) is exactly the thing that is boundary-fixed and hence **bookkeeping**.

## Required Output Verdicts (per NEXT-TRIGGER-PLAN expected outputs)

- functoriality verdict: **lax/bookkeeping on the energy-momentum observable**
  (`p^mu . F` factors through `Preord(<=_S)`); can be a genuine nontrivial functor only
  on the history-class observable.
- order/causality verdict: **order preservation only / lossy projection** for the
  mass-energy target (nontriviality lives in parallel morphisms, where order is blind).
- earned-structure ladder verdict: terminates at **causal_preorder** (induced) plus
  **admissible-history-class** in the toy. NOT earned: conformal structure, metric up to
  scale, full metric, action principle, Noether/Poincare machinery — all imported from
  the fixed external `(M, eta, A)`.
- metric-dependency verdict: **externally supplied metric**. Construction did not force
  reconstruction; bridge is metric-importing, not metric-generating.
- nontriviality test: **PASS** at history-class level; **FAIL** at energy-momentum level
  (BDO). Per E008 kill_test, the mass-energy discriminator is bookkeeping.
- GU compatibility (evaluated only after ordinary attempt, per discipline):
  **GU-unneeded / GU-irrelevant.** BDO is generic to Lorentzian Noether charges; an
  observerse target shares boundary-determination of conserved charges, so importing GU
  does not evade BDO. Not GU-blocked; just orthogonal.
- absorber comparison: the surviving history-class nontriviality is absorbed by ordinary
  gauge/topological-sector and fiber-bundle bookkeeping (information-theory / causal-set
  absorbers). No residual mass-energy work.
- does `Ext_S` beat NULL-SURVIVOR? **For the physical/mass-energy interpretation: NO** —
  NULL-SURVIVOR (O10) still wins at the energy-momentum rung. For pure formal
  structure: a sliver survives (history-class discrimination) but does no physical work
  and is independently absorbable.
- decision on source-side residue: **partial kill.** Kill the mass-energy bridge path;
  keep `Ext_S` formalizing under a strictly narrower target (see resurrection trigger).

## Claim-Ledger Updates (proposed)

- **TI-C009** (TI connects to GU/mass-energy via extension/energy-momentum):
  `speculative -> weakened (energy-momentum route path-killed by BDO)`. Evidence: BDO.
- **TI-C010** (conditional Lorentzian realization theorem recovers mass-energy *if* a
  composition-preserving nontrivial F exists): the **conditional stays true** (E008 proof
  skeleton is sound), but its **antecedent is shown unsatisfiable at the energy-momentum
  level in the control case**. Status: `formalizing`, antecedent-obstructed noted. Bridge
  downgraded.
- **TI-C007** (`Ext_S` load-bearing): stays `formalizing`, narrowed to "load-bearing at
  history-class level only, not energy-momentum."
- **TI-C008** (extension induces order while carrying invariant not recoverable from
  order): **supported at the formal level** — a parallel-pair invariant exists and can map
  to a distinct admissible-history class — but explicitly does not reach energy-momentum.

## Path Kill (for memory/path-kills.md)

```yaml
path: nontrivial realization functor carrying Ext_S structure into Lorentzian energy-momentum (mass-energy bridge)
reason_killed: Boundary-Determination Obstruction. Total conserved p^mu is boundary-object-determined; parallel extensions (same <=_S) cannot move it; nontriviality and energy-momentum-relevance are mutually exclusive in the Poincare-invariant control case. Realizes E008 only_imported_physics failure and kill_test.
evidence: BDO lemma (RUN-0028 BDO pass); E008 kill_test; RUN-0025 parallel-invariant result.
local_minimum_risk: medium. Used the clean Minkowski control case with objects = full boundary/Cauchy data. If objects under-determine total momentum, BDO weakens.
possible_future_resurrection_trigger: a LorHist formulation whose objects under-determine total p^mu (e.g. partial/asymptotic boundary data only) PLUS an Ext_S invariant that fixes the momentum data the boundary leaves open. If such a model is consistent, covariant, and not hidden-variable bookkeeping, reopen the bridge.
run_ref: RUN-0028 (BDO pass)
claim_refs: [TI-C007, TI-C008, TI-C009, TI-C010]
```

## Recommended Next Run

W000 -> **invert the construction**: do not let boundary objects fix momentum. Define a
`LorHist'` whose objects are momentum-underdetermining (partial/asymptotic boundary data),
then ask whether an `Ext_S` morphism invariant can *select* among the p^mu-distinct on-shell
completions. Sharp target:

```text
Does there exist Ext_S structure that fixes Lorentzian momentum data left open by the boundary,
without reducing to hidden-variable bookkeeping or a preferred foliation?
```

If yes -> the mass-energy bridge resurrects with real source-side content. If no (precise
obstruction) -> archive the physical interpretation to NULL-SURVIVOR and keep only the
history-class formal residue.

## Blockers

Chat environment: cannot push to GitHub (no repo auth). Run record + proposed file patches
produced for review; applied via Claude Code automation against the local repo.

## Closeout Checklist

```yaml
run_record_written: true
strongest_version_generated_before_kill: true
memory_log_update_proposed: true
memory_summary_update_proposed: true
claim_ledger_update_proposed: true
roadmap_update_proposed: true
next_trigger_plan_update_proposed: true
path_kill_recorded: true
metrics_update_proposed: true
checks_run_or_skipped_with_reason: ascii_scan_pass; git_push_skipped_no_auth_in_chat_applied_via_claude_code
commit_pushed: false_in_chat_true_after_automation
```

## Files Changed

- `agent-runs/RUN-0028-construct-or-refute-minimal-nontrivial-realization-functor.md` (this file)
- `agent-governance/NEXT-TRIGGER-PLAN.md` (replace target with the inverted-construction next run)
- `explorations/E008-conditional-lorentzian-realization-theorem.md` (record BDO + split verdict)
- `CLAIM-LEDGER.md` (TI-C007/008/009/010 status edits above)
- `memory/path-kills.md` (append the BDO path kill block above)
- `ROADMAP.md`, `memory/steward-memory-log.md`, `memory/steward-memory-summary.md`, `agent-governance/STEWARD-METRICS.md`
