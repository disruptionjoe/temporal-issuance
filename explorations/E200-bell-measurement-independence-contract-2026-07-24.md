---
artifact_type: exploration
status: complete
exploration_id: E200
date: 2026-07-24
lane: 1
work_group: PHYSICAL-ISSUANCE-WITNESS
topic: bell_measurement_independence_contract
result: BELL_CAUSAL_SEPARATION_WITH_MEASUREMENT_INDEPENDENCE_RESIDUE
claim_status_change: none
claim_refs:
  - TI-C019
relates_to:
  - E025
  - E196
  - E199
run_ref: agent-runs/RUN-0212-bell-measurement-independence-contract.md
---

# E200: Bell Measurement-Independence Contract

## Question

E199 replaced stage-0 fixedness with three independent physical obligations:
bound discloser degree/access below the joined history object `J_H`, separate
static disclosure from adaptive source reads, and justify future-independence
from a completed history or branch oracle. Does a spacelike-separated CHSH
Bell experiment establish that contract?

## Construction fork

This run compares two explicit constructions:

| object | construction used | why |
| --- | --- | --- |
| Bell experiment | spacelike-separated CHSH settings and outcomes | strongest standard physical setting for closing post-choice causal communication |
| fixed rival | local, stage-0-fixed, measurement-dependent hidden schedule | strongest E199 rival; hidden state may correlate with settings and outcomes |

The rival is mathematical. Its inclusion does not assert superdeterminism or
physical realizability. Excluding it by assuming independent settings would
simply assume the future-independence obligation under test.

## Physical evidence boundary

Bell-CHSH violations pressure **local hidden-variable families only together
with measurement independence**. Barrett and Gisin show that relaxing setting
independence allows singlet correlations with very little setting/hidden-state
mutual information. Friedman et al. construct tight relaxed Bell inequalities
with arbitrary measurement dependence. Cosmic Bell tests move any shared
cause for settings and outcomes farther into the past, but Handsteiner et al.
state their conclusion conditionally on the stellar setting information and
other experimental assumptions.

Primary sources:

- J. Barrett and N. Gisin, “How Much Measurement Independence Is Needed to
  Demonstrate Nonlocality?”, *Physical Review Letters* 106, 100406 (2011),
  https://doi.org/10.1103/PhysRevLett.106.100406
- A. S. Friedman et al., “Relaxed Bell Inequalities with Arbitrary Measurement
  Dependence for Each Observer” (2018), https://arxiv.org/abs/1809.01307
- J. Handsteiner et al., “Cosmic Bell Test: Measurement Settings from Milky
  Way Stars”, *Physical Review Letters* 118, 060401 (2017),
  https://doi.org/10.1103/PhysRevLett.118.060401

These results support a clean split:

1. spacelike setting and outcome events strongly support the classification of
   post-setting communication as adaptive copying rather than a static local
   rival;
2. Bell data do not independently derive measurement independence between the
   initial hidden state and later settings;
3. a finite transcript is finite data and can itself be encoded in a fixed
   schedule, so it cannot prove the Turing non-reducibility `J_H not <=_T O`
   required by E199.

## Executable pressure

`tools/e200_bell_measurement_independence_contract.py` freezes a four-row
all-winning CHSH-game transcript. One hidden schedule fixed before the first
trial stores each trial's settings and outputs. Local response functions read
the stored row; there is no post-setting communication and the finite
transcript is reproduced exactly. The model violates measurement independence.

This is not a quantum model and does not reproduce an infinite Born
distribution. It is the minimal finite-data control showing why causal
separation and stage-0 fixedness do not prove future-independence. The
measurement-independent local family remains the proper target of the Bell
inequality; the measurement-dependent family is outside that theorem's
antecedent, not experimentally refuted by it.

## Contract verdict

| E199 obligation | Bell construction result | verdict |
| --- | --- | --- |
| degree/access bound `J_H not <=_T O` | finite data cannot establish it; fixed schedule encodes the transcript | not established |
| causal-source separation | spacelike separation excludes ordinary post-setting communication under the physical causal model | supported |
| future-independence | equivalent here to a measurement-independence/free-settings premise not derived from Bell statistics | not established |
| construction disclosure | CHSH geometry and measurement-dependent local rival are explicit | established |

```yaml
result: BELL_CAUSAL_SEPARATION_WITH_MEASUREMENT_INDEPENDENCE_RESIDUE
named_construction: spacelike_separated_CHSH_Bell_experiment
strongest_fixed_rival: stage_zero_measurement_dependent_local_schedule
degree_access_bound_established: false
causal_source_separation_supported: true
future_independence_established: false
finite_data_proves_turing_nonreducibility: false
physical_source_issuance_established: false
claim_status_change: none
```

## Consequence

Bell is useful negative Progress: it closes one part of E199's burden while
showing that the remaining part is not hidden in “loophole-free” language.
Bell nonlocality or device-independent randomness must not be promoted into
source issuance unless the protocol independently bounds adversarial
setting/history correlation strongly enough to imply the required source
non-reducibility. `TI-C019` remains formalizing and `TI-C020` remains parked.

The next construction should have a preregistered causal model that supplies a
quantitative initial-state/setting independence or entropy bound, then ask
whether that finite operational bound has any legitimate route to E199's
stronger degree separation. Repeating Bell rhetoric without such a bound would
not advance the question.
