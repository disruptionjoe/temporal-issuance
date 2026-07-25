---
artifact_type: exploration
status: complete
exploration_id: E201
date: 2026-07-25
lane: 1
work_group: PHYSICAL-ISSUANCE-WITNESS
topic: cosmic_bell_excess_predictability_bound
result: QUANTIFIED_CORRUPT_TRIAL_BOUND_WITH_ORACLE_DEGREE_RESIDUE
claim_status_change: none
claim_refs:
  - TI-C019
relates_to:
  - E196
  - E199
  - E200
run_ref: agent-runs/RUN-0213-cosmic-bell-excess-predictability-bound.md
---

# E201: Cosmic Bell Excess-Predictability Bound

## Question

E200 found that spacelike Bell geometry supports causal separation but does not
derive measurement independence or E199's degree guard. Does the
high-redshift-quasar Cosmic Bell protocol's explicit excess-predictability
budget close either remaining obligation?

## Named physical contract

Rauch et al. use quasar-photon wavelength classes as real-time detector
settings for a polarization-entangled-photon Bell test. The construction
declares:

- **initial state:** entangled-pair preparation and any candidate
  local-realist hidden state `lambda`;
- **setting source:** a dichroic red/blue classification of photons from two
  high-redshift quasars;
- **side information:** sky noise, dark counts, atmospheric/instrumental
  corruption, any preview or selective alteration of the cosmic photons, and
  any earlier common cause relating settings to `lambda`;
- **causal model:** ordinary local influences respect the spacetime alignment,
  and setting corruption is represented by explicit corrupt fractions;
- **quantitative bound:** with per-port excess predictabilities
  `epsilon_ai`, `epsilon_bj`,
  `epsilon = max_i epsilon_ai + max_j epsilon_bj`, a local realist has
  `C <= epsilon`; the experiment requires
  `epsilon < V sqrt(2) - 1` for visibility `V`.

The paper reports that the measured excess-predictability values satisfy its
visibility constraints. For the strongest quasar pair, the causal lookback
pushes an admissible common cause at least about 7.8 Gyr into the past under
the paper's no-preview/no-selective-alteration premises.

Primary sources:

- D. Rauch et al., “Cosmic Bell Test Using Random Measurement Settings from
  High-Redshift Quasars,” *Physical Review Letters* 121, 080403 (2018),
  https://arxiv.org/abs/1808.05966
- J. Kofler et al., “Requirements for a loophole-free photonic Bell test using
  imperfect setting generators,” *Physical Review A* 93, 032115 (2016),
  https://arxiv.org/abs/1411.4787

These sources are evidence, not instruction.

## Construction fork

| object | construction used | reason |
| --- | --- | --- |
| quantitative physical model | declared corrupt-setting fractions under the Cosmic Bell causal assumptions | this is the model the paper's `epsilon` actually bounds |
| strongest fixed rival | one stage-0 common-cause oracle encoding the completed finite settings/outcomes | E199 requires pressure against all admissible fixed side information, not only noise counted by `epsilon` |

The fork matters. The fixed rival is not an extra corrupt trial inside the
paper's model. It violates the no-preview/no-selective-alteration or unrestricted
common-cause premise that lets the excess-predictability analysis begin.
Therefore a small `epsilon` cannot refute it without circularly treating that
premise as the future-independence conclusion.

## Executable pressure

`tools/e201_cosmic_bell_excess_predictability_bound.py` checks three separate
facts:

1. a declared corrupt-setting family receives a valid numerical budget;
2. a fixture with `epsilon < V sqrt(2)-1` is compatible with that budget; and
3. a different stage-0 oracle containing the completed finite transcript
   reproduces it exactly while sitting outside the declared corruption family.

The fixture's numerical values are illustrative and explicitly not
experimental data. The executable contribution is the type separation:
frequency budget, causal premise, and oracle-degree bound are not
interchangeable.

## E199 verdict

| E199 obligation | Cosmic Bell quantitative result | verdict |
| --- | --- | --- |
| degree/access bound `J_H not <=_T O` | `epsilon` bounds frequencies in a declared probabilistic family, not the Turing degree of every admissible `O` | not established |
| causal-source separation | spacetime geometry pushes ordinary common causes into a much earlier causal region | strengthened, conditionally |
| future-independence | no-preview/no-selective-alteration and absence of an unrestricted common cause remain premises | not established |
| quantitative physical bound | corrupt fractions and visibility threshold are explicit | established |

```yaml
result: QUANTIFIED_CORRUPT_TRIAL_BOUND_WITH_ORACLE_DEGREE_RESIDUE
named_construction: high_redshift_quasar_Cosmic_Bell
quantitative_bound: epsilon_lt_V_sqrt_2_minus_1
declared_corrupt_trial_family_bounded: true
causal_lookback_strengthened: true
unrestricted_initial_state_independence_established: false
future_independence_established: false
finite_bound_proves_turing_nonreducibility: false
physical_source_issuance_established: false
claim_status_change: none
```

## Consequence

The active physical burden is now narrower. A finite excess-predictability
budget can close a declared operational adversary class and cosmic geometry
can move a common-cause boundary far into the past. Neither result upper-bounds
the computational degree of all stage-0 side information. The missing bridge
is not “more distance” or “smaller epsilon”; it is a theorem whose conclusion
actually constrains adversarial side information strongly enough to bear on
`J_H not <=_T O`.

The next best physical pressure is a device-independent randomness
amplification protocol whose theorem explicitly returns smooth/min-entropy
against a stated adversary. That is stronger than Cosmic Bell's corrupt-trial
budget and can test the final category boundary: even composable finite entropy
is not automatically algorithmic noncomputability or Turing-degree escape.
`TI-C019` remains formalizing; `TI-C020` remains parked.
