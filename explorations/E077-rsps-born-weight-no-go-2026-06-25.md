---
artifact_type: exploration
status: active
governance_role: quantum_absorber_theorem_candidate
run_ref: RUN-0072
claim_refs:
  - TI-C020
  - TI-C001
related:
  - explorations/E075-rsps-record-fidelity-toy-baseline-2026-06-25.md
  - explorations/E076-rsps-robustness-sweep-2026-06-25.md
---

# E077: RSPS Born-Weight No-Go

## Purpose

Execute Goal 3 of the five-goal disproof ladder:

> Attempt a scoped theorem that record-stability / redundancy / agreement functionals can
> select basis/objectivity but cannot derive Born weights unless they import trace-rule or
> diagonal-state information.

This is not a universal theorem against every possible probability derivation. It targets the
specific RSPS functional class used in E075/E076 and in the external handoff note.

## Target Functional Class

Let a candidate pointer structure be a projective decomposition:

```text
B = {Pi_i}
```

with branch weights:

```text
p_i = Tr(rho Pi_i)
```

The no-go targets scalar record-fidelity objectives of the form:

```text
F(B) = alpha Stability(B)
     + beta Redundancy(B)
     + gamma Agreement(B)
     - delta Cost(B)
```

where:

1. `Stability(B)` ranks predictability / robustness of a basis or history family.
2. `Redundancy(B)` is built from mutual information, redundancy plateaus, fragment agreement,
   or copied-record availability.
3. `Agreement(B)` penalizes off-diagonal interference, disagreement, or decoherence failure.
4. `Cost(B)` is basis/history/geometry cost, not a probability postulate.
5. `F` is a scalar objective used to select a basis, history family, branch structure, or
   accessible record structure.
6. `F` does not directly output or retain the full labelled diagonal vector
   `diag_B(rho) = (Tr(rho Pi_i))_i`.
7. `F` does not import the Born rule, trace rule, envariance, decision theory, relative
   frequency axiom, or collapse law as a separate probability module.

## No-Go Statement

Within this class:

```text
F can select a pointer basis or record-objectivity structure.
F cannot derive the Born weights.
```

More precisely:

```text
No scalar F of the above class determines the labelled Born vector
p = (Tr(rho Pi_i))_i
for the selected basis B*
unless F directly reads diag_B*(rho) or imports a separate weight rule.
```

## Proof Sketch

### Lemma 1: Basis Selection And Weight Assignment Are Different Types

The output type of `argmax_B F(B)` is:

```text
selected basis / selected history family / selected record structure
```

The output type of Born assignment is:

```text
probability measure over outcomes inside the selected structure
```

A selector can identify `B*` without assigning the measure `p_i = Tr(rho Pi_i)`.

### Lemma 2: Stability Does Not Carry Branch Weights

Predictability-sieve stability ranks bases or histories by robustness under dynamics. At the
selected pointer basis, ideal stability costs are typically zero or extremal for all branch
weights. E075 verified this in the controlled-copy fixture:

```text
raw stability cost at pointer basis = 0 for p0 = 0.3, 0.5, 0.7, 0.9
```

Therefore stability can select a basis but does not determine branch weights.

### Lemma 3: Agreement / Decoherence Does Not Carry Branch Weights

Agreement or decoherence terms test off-diagonal suppression, record compatibility, or
interference failure. At the selected pointer basis, these terms vanish or extremize when
off-diagonal components are suppressed. That condition is compatible with many different
diagonal vectors.

E075 verified:

```text
raw agreement cost at pointer basis = 0 for p0 = 0.3, 0.5, 0.7, 0.9
```

Therefore agreement can certify definiteness/compatibility but does not determine weights.

### Lemma 4: Redundancy Carries Objectivity Volume, Not The Labelled Born Vector

Redundancy terms built from mutual information or redundancy plateaus measure how much
information about the selected pointer variable is copied into accessible fragments.

In the perfect binary controlled-copy fixture:

```text
Redundancy at pointer basis = N * H2(p0)
```

This is not `p0`.

It is entropy-like:

```text
H2(0.3) = H2(0.7)
H2(0.5) > H2(0.9)
```

So redundancy can measure record objectivity capacity, but it does not recover the labelled
Born weights.

For higher-outcome systems, the obstruction is stronger: many non-permutation-equivalent
probability vectors have the same Shannon entropy or same coarse redundancy score. A scalar
redundancy objective cannot invert to the full probability vector.

### Lemma 5: If A Functional Reads The Full Diagonal Vector, It Has Imported A Weight Module

One can trivially recover Born weights by defining a "record-fidelity" functional that outputs:

```text
diag_B(rho)
```

or stores labelled record frequencies and then identifies them with probabilities.

But that is no longer the RSPS scalar selector class. It has imported the trace-rule object
or a frequency/probability module. That may be valid physics, but it is not a derivation from
record fidelity alone.

## Toy-Model Witnesses

E075 provides the binary witness:

| p0 | normalized F(pointer) | raw redundancy N*H2(p0) | Born weight |
|---:|---:|---:|---:|
| 0.3 | 3.0 | 7.0503271938 | 0.3 |
| 0.5 | 3.0 | 8.0 | 0.5 |
| 0.7 | 3.0 | 7.0503271938 | 0.7 |
| 0.9 | 3.0 | 3.7519647487 | 0.9 |

E076 adds that pointer-basis selection is robust under the tested perturbations:

```yaml
scenario_count: 28
pointer_wins_full_score_count: 28
full_score_failures: []
```

Together:

```text
basis selection survives
weight derivation fails
```

## Escape Routes

The no-go does not block these routes:

1. **Trace rule:** accept Born weights as `Tr(rho Pi_i)`.
2. **Envariance:** use Zurek-style entanglement symmetry arguments as a separate module.
3. **Decision theory:** use Everettian decision-theoretic derivations as a separate module.
4. **Collapse dynamics:** add a physical stochastic collapse law with its own probability rule.
5. **Frequency module:** use labelled long-run record frequencies, with the required typicality
   or probability assumption stated separately.
6. **Explicit diagonal readout:** make `diag_B(rho)` part of the formal input/output and stop
   calling the result a derivation from scalar record fidelity alone.

These may be legitimate. They are simply not the single-functional RSPS route.

## Effect On Temporal Issuance

This result sharpens the quantum absorber:

```text
record/finality language can explain basis accessibility
record/finality language does not explain quantum weights by itself
```

Therefore Temporal Issuance should not claim:

```text
issuance / finality / record fidelity derives the Born rule
```

unless a separate, explicit weight module is supplied and survives its own absorber tests.

## Verdict

```yaml
general_status: scoped_no_go_theorem_candidate
target_class: scalar_RSPS_stability_redundancy_agreement_functionals_without_diag_readout
basis_selection: survives
born_weight_derivation: fails
claim_status_change: none
next_goal: fixed_H_absorber_vs_H_growing_issuance_fixture
```

## Next Goal

Goal 4 should now test the fixed-H absorber directly:

```text
Can fixed-H quantum mechanics plus decoherence / Quantum Darwinism reproduce every
observer-accessible issuance trace produced by the RSPS record/finality layer?
```

If yes, the quantum record-fidelity line is absorbed as standard QM reconstruction vocabulary.
If no, name the exact residue.
