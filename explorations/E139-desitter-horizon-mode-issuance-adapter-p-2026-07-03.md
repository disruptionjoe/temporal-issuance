---
artifact_type: exploration
status: complete
governance_role: physical_frontier_big_swing
workflow: W000
goal_ref: desitter_horizon_mode_issuance_adapter_p
claim_refs:
  - TI-C019
  - TI-C020
  - TI-C021
depends_on:
  - explorations/E110-online-issuance-lc-physical-adapter-contract-2026-07-01.md
  - explorations/E112-oi-lc-candidate-scout-w1-w6-table-2026-07-01.md
  - explorations/E127-online-issuance-lc-ce-tier-comparator-2026-07-02.md
  - explorations/E138-online-issuance-lc-theorem-contract-integration-2026-07-03.md
  - explorations/E045-d-fork-synthesis-interior-optimum-verdict-2026-06-22.md
  - absorbers/cosmological-expansion.md
  - tools/desitter_horizon_mode_issuance_fixture.py
  - tests/test_desitter_horizon_mode_issuance_fixture.py
created: 2026-07-03
central_run: RUN-0124
constitutional: false
claim_status_change: none
---

# E139: de Sitter Comoving-Horizon Mode Issuance Through Adapter_P

## Purpose

Take the biggest available swing on the physical frontier (F2 / TI-C020) by supplying a
concrete, non-duplicative source-formation candidate drawn from the North Star's own triad
(cosmological expansion + structure formation) and running it through the full `Adapter_P`
gate with fixed-source null models and an executable fixture.

Non-duplication check: the E112 candidate scout scored seven families (quantum measurement,
causal-set growth, holographic/boundary, GU adapter language, assembly theory, Orch-OR,
dual-record graphs). Cosmological horizon-mode crossing was **not** among them. The
`absorbers/cosmological-expansion.md` file (RUN-0010) only ever tested `mu`/"growth" language;
it never ran expansion as an `Adapter_P` source-formation candidate. So this is a genuinely new
attack, and it targets the most North-Star-central physics available.

This is a swing, not a claim. The honest prior (from the whole absorber history) is that it will
be absorbed; the value is a sharp verdict and a precise resurrection trigger.

## The candidate

In de Sitter expansion `a(t) = e^{Ht}`, comoving modes exit the Hubble horizon; super-horizon
modes freeze and (via decoherence) seed the classical large-scale record (CMB / structure).
The TI question:

```text
Is "comoving mode k crossing the horizon and freezing into the cosmological record" genuine
source issuance (H_grow: the frozen-record observable algebra grows non-isomorphically, not
factorable through a fixed completion), or fixed-source disclosure (H_fixed: a fixed
Bunch-Davies algebra on a fixed comoving lattice, a changing horizon-access window, and a fixed
decoherence law)?
```

## Adapter_P mapping

```text
Gamma_n   frozen cosmological record at e-fold n
Adm_n     mode is issuable at n iff it crosses the horizon in [n, n+1): k / a(t_n) ~ H
e_n       the crossing/freezing event
w_n       witness: mode was sub-horizon (unrecorded, quantum) at n, super-horizon (frozen) at n+1
Gamma_n+1 record after admission
tau_n     the frozen amplitude / structure seed (a real, preserved record)
```

The mapping is total — every Adapter_P field has a natural cosmological referent. That is
exactly why the candidate is worth a real pass rather than a shortcut kill.

## Two regimes

The pass splits on a single background assumption, and that split is the whole result.

### Regime A — fixed background (the physically standard case)

Fixed comoving lattice `K_infty = {k}` with a fixed Bunch-Davies state; the horizon threshold
`k_cross(n)` sweeps over it as the universe expands. Frozen record modes `Gamma_n` are a growing
**subset** of `K_infty`.

Adapter_P W-gate:

| Gate | Verdict | Why |
| --- | --- | --- |
| W1 non-isomorphic algebra growth | FAIL | `Gamma_n ⊆ K_infty`; the frozen-record algebra embeds in a fixed global algebra `A_infty`. Growth is access, not new structure. |
| W2 prefix-formed admissibility | FAIL | `k ≤ k_cross(n)` is a fixed function of a pre-given lattice; admissibility is revealed, not formed. |
| W3 construction provenance | FAIL | modes are disclosed by the horizon sweep, not constructed. |
| W4 perturbation non-factorization | FAIL | perturb `H` and `k_cross(n)` reschedules; the record still factors through the same fixed `A_infty` under a different access schedule (checked in the fixture). |
| W5 record preservation | PASS | super-horizon freezing genuinely preserves `tau_n`. This is the one physically-real property — and it does not by itself supply issuance. |
| W6 gauge/access/language non-absorption | FAIL | the comoving-vs-physical coordinate choice and the gauge choice of the mode decomposition absorb "crossing." |

Fixed-source nulls: `fixed_H_infty`, `fixed_A_infty`, `bounded_access_to_Mu_infty`,
`fixed_stochastic_or_collapse_law` (the freeze/decohere step is a fixed law), and
`fixed_boundary_or_holographic_completion` all **absorb**.

Verdict A: **absorbed as fixed-source disclosure.** This is the physically standard regime, and
it does not reopen TI-C020.

### Regime B — generated lattice (self-generating / Goedelian background)

Suppose instead the comoving mode label formed at stage `n+1` is not drawn from a pre-given
lattice but **diagonalizes** the stage-`n` present enumerator (the admissible index set is
itself generated). Then:

- **Finite-prefix freshness survives:** a fixed completion equal to the entire stage-`P`
  enumerated menu still misses the stage-`P` diagonal label (verified in the fixture for every
  stage). No fixed finite lattice chosen at stage 0 pre-contains the issued labels.
- **Whole-family escape is absorbed** by a singleton enumerator that lists the realized
  sequence after the fact — exactly the E127 c.e. ceiling.

Verdict B: this is **not new**. It is the already-established `OnlineIssuance^LC` class-relative
residue wearing cosmological clothing. Finite-prefix issuance survives class-relatively; an
absolute physical W1 does not.

## What the swing establishes

```yaml
fixed_background_regime: absorbed_as_fixed_source_disclosure
generated_lattice_regime: reduces_to_OnlineIssuance_LC_class_relative_residue
new_physical_surplus_over_formal_residue: false
physical_question_separable_from_D_FORK: false
Issue[S]^physical: false
TI_C020_reopened: false
claim_status_change: none
```

The important content is the collapse of the two regimes onto the program's existing structure:

1. In the standard fixed-background regime, cosmological horizon-mode crossing is **fixed-source
   disclosure** — a growing accessible subalgebra of a fixed Bunch-Davies algebra, plus a fixed
   decoherence law. Every relevant fixed-source null absorbs it.
2. The only regime in which it could be issuance is one where the comoving mode index set is
   itself self-generating — and there it is **the same open bit** that TI-C019 already turns on
   (PP-3 / D-FORK, E042/E045: is the operative source effective type space Goedelian or
   fixed-finite?). It adds no physical surplus over `OnlineIssuance^LC` and inherits the same
   c.e. ceiling.

So the cosmological route does not give an independent physical handle on issuance. It **reduces
the physical question to D-FORK.** That is a genuine unification result and a real narrowing of
the North Star search: "connect issuance to cosmological expansion" is not a separate program
from "decide whether the operative source is self-generating."

## Honest limits of this swing

- The fixture is a **toy Adapter_P discriminator, not a physics simulation.** It formalizes the
  factorization/freshness structure, not QFT-in-curved-spacetime dynamics.
- The reduction "physical question = D-FORK" is argued at the level of the adapter structure and
  the fixed-source nulls, not proven as a theorem about all de Sitter models.
- Eternal de Sitter has known subtleties (no global vacuum across static patches, IR/secular
  growth, entanglement-entropy growth) that this pass treats as absorbed by fixed-lattice +
  access. A model where one of those provably fails to factor is exactly the resurrection route.

## Resurrection trigger for TI-C020 via this candidate

Reopen only if someone exhibits a physically-motivated **dynamical-background** model in which:

```text
1. the comoving mode index set at stage n+1 provably CONTAINS a mode not FORMABLE (not merely
   not-yet-accessed) at stage n — i.e., generated UV/degrees-of-freedom, not a fixed lattice;
2. horizon-crossing records cannot be factored through ANY fixed completed mode algebra plus a
   fixed access schedule plus a fixed decoherence law, while preserving tau_n; and
3. the escape is not the singleton after-the-fact absorption (i.e., a whole-family escape, which
   would also break the OnlineIssuance^LC / E127 ceiling).
```

Condition 3 makes clear this trigger is at least as hard as the open strict-c.e. escape; a win
here would be a win there too.

## Claim effects

```yaml
TI-C020:
  movement: none
  note: >
    Cosmological horizon-mode crossing is absorbed as fixed-source disclosure in the standard
    fixed-background regime, and reduces to the OnlineIssuance^LC class-relative residue (open
    D-FORK bit) in the self-generating regime. No physical source issuance; TI-C020 stays
    parked, now with a cosmological resurrection trigger attached.
TI-C019:
  movement: none
  note: >
    Strengthens the case that TI-C019's deepest fork (self-generating vs fixed-finite source) is
    the load-bearing question even for the physics bridge: the cosmological route does not bypass
    it.
TI-C021:
  movement: none
  note: >
    Consistent with the E043 regime-pinning: sustained issuance requires the Goedelian regime;
    the fixed-background cosmological case is the fixed-source (disclosure) side.
```

## Verdict

```yaml
status: complete
big_swing_executed: true
candidate: desitter_comoving_horizon_mode_issuance
adapter_p_mapping_total: true
fixed_background_absorbed: true
generated_regime_is_new_physical_surplus: false
physical_frontier_reduced_to_D_FORK: true
Issue[S]^physical: false
TI_C020_reopened: false
claim_status_change: none
fixture: tools/desitter_horizon_mode_issuance_fixture.py
fixture_tests: 4 passed
full_suite: 70 passed
```
