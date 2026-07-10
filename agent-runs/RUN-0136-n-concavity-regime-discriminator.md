---
artifact_type: agent_run
status: complete
run_id: RUN-0136
run_family: repo_progress
created: 2026-07-09
trigger: source_formal_obligation_closure
constitutional: false
---

# RUN-0136: N Concavity Regime Signature

## Objective

Resolve the E031 II.1 conditional (N concavity vs Godelian sustained novelty) as an executable
diagnostic tying the N-functor work to the D-FORK discriminator (E042).

## Method

Ran a toy novelty process in FTS (depleting pool) and Godelian (self-injecting pool) regimes;
read the discrete second difference of the realized novelty rate.

Primary artifact: `explorations/E156-n-concavity-regime-discriminator-2026-07-09.md`.

Executable artifacts:

- `tools/n_concavity_regime_discriminator.py`
- `tests/test_n_concavity_regime_discriminator.py`
- `tests/artifacts/n_concavity_regime_discriminator_result.json`

## Result

```yaml
fts_regime: concave_and_declining_interior_optimum_exists
godelian_regime: sustained_no_forced_optimum
curvature_separates_regimes: true
scope: finite_window_signature_not_a_decision_procedure
claim_status_change: none
```

The true FTS/Godelian bit is non-computable (E042); curvature is a corroborating signature, not
an oracle.

## Files Changed

- `explorations/E156-n-concavity-regime-discriminator-2026-07-09.md`
- `tools/n_concavity_regime_discriminator.py`
- `tests/test_n_concavity_regime_discriminator.py`
- `tests/artifacts/n_concavity_regime_discriminator_result.json`

## Boundaries

No claim status moved. No constitutional, public-posture, mailbox, or external change. Physical
branch untouched.
