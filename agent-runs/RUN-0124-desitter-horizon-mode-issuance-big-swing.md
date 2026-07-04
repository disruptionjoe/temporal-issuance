---
artifact_type: agent_run
status: complete
run_id: RUN-0124
run_family: repo_progress
created: 2026-07-03
trigger: joe_directed_session
constitutional: false
---

# RUN-0124: de Sitter Horizon-Mode Issuance — Physical-Frontier Big Swing

## Objective

Joe asked for the biggest swing possible on the most promising path. The formal leg is
Lean-hardened and now recorded (RUN-0123); the live frontier is the physical leg (F2 / TI-C020).
Supply a concrete, non-duplicative physical source-formation candidate from the North Star's own
triad and run it through the full `Adapter_P` gate with an executable fixture.

## Candidate selection

Cosmological expansion / de Sitter comoving-horizon mode crossing. Non-duplicative: not among
E112's seven scored families; the cosmological-expansion absorber never ran it as an Adapter_P
source-formation candidate. Most North-Star-central physics available (expansion + structure
formation).

## Method

- Mapped the candidate onto Adapter_P (`Gamma_n, Adm_n, e_n, w_n, Gamma_{n+1}, tau_n`).
- Built a toy discriminator fixture comparing a fixed-background regime against a
  self-generating (Goedelian) lattice regime, scoring W1-W6 and the fixed-source nulls.
- Executable artifacts:
  - `tools/desitter_horizon_mode_issuance_fixture.py`
  - `tests/test_desitter_horizon_mode_issuance_fixture.py`
  - `tests/artifacts/desitter_horizon_mode_issuance_result.json`

## Result

```yaml
fixed_background_regime: absorbed_as_fixed_source_disclosure
generated_lattice_regime: reduces_to_OnlineIssuance_LC_class_relative_residue
new_physical_surplus_over_formal_residue: false
physical_question_separable_from_D_FORK: false
Issue[S]^physical: false
TI_C020_reopened: false
claim_status_change: none
fixture_tests: 4 passed
full_suite: 70 passed
```

Primary artifact: `explorations/E139-desitter-horizon-mode-issuance-adapter-p-2026-07-03.md`.

## What collapsed

The standard fixed-background regime is fully absorbed: the frozen-record algebra is a growing
accessible subalgebra of a fixed Bunch-Davies algebra on a fixed comoving lattice, with a fixed
decoherence law. W1, W2, W3, W4, W6 fail; only W5 (record preservation) holds and does not
supply issuance. All relevant fixed-source nulls absorb.

## What survived / clarified

The candidate does not give an independent physical handle on issuance. It **reduces the
physical question to D-FORK** (E042/E045): the only regime where horizon-mode crossing could be
issuance is one where the comoving index set is self-generating — the same open bit TI-C019
turns on — and there it merely re-instantiates the `OnlineIssuance^LC` class-relative residue
with the same c.e. ceiling. This is a genuine unification/narrowing result: "connect issuance to
cosmological expansion" is not a separate program from "decide whether the operative source is
self-generating."

## What was absorbed

Cosmological horizon-mode crossing (standard regime) is added to the fixed-source-disclosure
pile, joining Everett branching (E123) and relativistic block universe (E124). A cosmological
resurrection trigger for TI-C020 is now recorded in E139.

## Honest limits

Toy Adapter_P discriminator, not a QFT-in-curved-spacetime simulation. The "physical question =
D-FORK" reduction is argued at adapter-structure + fixed-source-null level, not proven as a
theorem over all de Sitter models. Known de Sitter subtleties (no global vacuum across static
patches, IR/secular growth, entanglement growth) are treated as absorbed by fixed-lattice +
access and are the explicit resurrection route.

## Blockers

None. No claim movement; no gated surface touched (this is an exploration + fixture, not a
FORMAL-OBJECT / CLAIM-LEDGER status edit; the TI-C020 note is `movement: none`).

## Recommended next run

Either (a) attack the cosmological resurrection trigger directly with a dynamical-background /
generated-UV model, or (b) route back to the D-FORK expressiveness-threshold fixture (E042 §6.2)
now that the physical frontier is shown to reduce to it.

## Files changed

- tools/desitter_horizon_mode_issuance_fixture.py
- tests/test_desitter_horizon_mode_issuance_fixture.py
- tests/artifacts/desitter_horizon_mode_issuance_result.json
- explorations/E139-desitter-horizon-mode-issuance-adapter-p-2026-07-03.md
- explorations/README.md
- CLAIM-LEDGER.md
- agent-governance/NEXT-TRIGGER-PLAN.md
- agent-runs/RUN-0124-desitter-horizon-mode-issuance-big-swing.md
