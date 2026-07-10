---
artifact_type: exploration
status: complete
exploration_id: E156
governance_role: conditional_discharge
workflow: W000
goal_ref: n_concavity_regime_discriminator
date: 2026-07-09
claim_refs:
  - TI-C019
  - TI-C021
depends_on:
  - explorations/E031-nck-category-morphism-definitions-2026-06-22.md
  - explorations/E041-monotone-obstruction-sbp-finite-type-space-2026-06-22.md
  - explorations/E042-sbp-ind-verification-concrete-compat-family-2026-06-22.md
  - tools/n_concavity_regime_discriminator.py
  - tests/test_n_concavity_regime_discriminator.py
central_run: RUN-0136
constitutional: false
claim_status_change: none
verdict: N_CURVATURE_IS_A_REGIME_SIGNATURE_NOT_A_DECISION_PROCEDURE
---

# E156: N Concavity as an FTS / Godelian Regime Signature

## Purpose

Resolve the conditional left open in E031 II.1: N is concave in the issuance rate under a
finite depleting pool of novel types (diminishing returns), but concavity can fail when new
types beget new types (E028/E042 Godelian mechanism). E031 tied this to "a concrete Compat
family." This note turns the condition into an executable diagnostic and connects the
abandoned N-functor work to the live D-FORK discriminator (E042).

## Method

`tools/n_concavity_regime_discriminator.py` runs a toy novelty process in two declared
regimes and reads the discrete second difference (curvature) of the realized novelty rate
`N_n = novel-pool / (novel-pool + non-novel-background)`:

- **FTS regime:** fixed finite novel pool; each resolution depletes it (`births = 0`).
- **Godelian regime:** each resolution injects one fresh independent proposition
  (`births = 1`), operationalizing E042 Family G.

## Result

```yaml
fts_regime:
  all_concave: true            # every second difference < 0
  declines: true               # N falls to < half its start
godelian_regime:
  sustained: true              # N holds >= 3/4 of its start
  declines: false
curvature_separates_regimes: true
interior_optimum:
  fts: "exists (concave N, recovers E041 Theorem 2)"
  godelian: "not forced (sustained N, recovers E041 Prop 2)"
claim_status_change: none
```

In the FTS regime N is concave and declines as the novel pool depletes — the diminishing
returns that guarantee an interior optimum `lambda*(S)` (E041 Theorem 2). In the Godelian
regime the pool does not deplete, N is sustained, and its curvature is not uniformly
negative — no forced interior optimum (E041 Prop 2). N's curvature therefore **cleanly
separates the two D-FORK regimes**.

## Honest scope (kill-criteria discipline)

This is a **finite-window curvature diagnostic, not a decision procedure.** E042 proved the
true FTS/Godelian structural bit is non-computable in general (the independent set of a
consistent r.e. extension of Q is productive, hence non-c.e.). The fixture only demonstrates
that *within each declared regime* N's curvature behaves as E041/E042 predict. So curvature is
a legitimate regime **signature** usable as corroborating evidence when the regime is
otherwise pinned — it is explicitly **not** an oracle that decides the parked operative-source
question. Treating it as such would violate the D-FORK non-computability result and the
anti-premature-closure rule.

## Claim-ledger effect

- TI-C019: unchanged (`formalizing`). The N-functor curvature is now tied to the D-FORK regime
  bit with an executable diagnostic, without deciding the non-computable bit.
- TI-C021: unchanged (`speculative`). This corroborates the regime-pinned reading of TI-C021
  (SAX/subadditivity is the FTS signature; sustained marginal issuance is the Godelian
  signature) from the N side, consistent with E043. No promotion.

## Failure risks / what would reopen this

- If a Compat family shows sustained N *with* a genuine interior optimum, or depleting N
  *without* one, the curvature signature would decouple from the interior-optimum property and
  this diagnostic would lose its status. The two toy regimes here do not show that.
