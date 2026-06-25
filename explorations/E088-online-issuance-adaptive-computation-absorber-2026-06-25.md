---
artifact_type: exploration
status: active
governance_role: absorber_gauntlet
run_ref: RUN-0078
claim_refs:
  - TI-C019
  - TI-C003
depends_on:
  - explorations/E087-online-issuance-formal-object-v0-1-2026-06-25.md
---

# E088: OnlineIssuance Adaptive Computation Absorber

## Purpose

This executes Goal 2 from E086: try to absorb `OnlineIssuance v0.1` into ordinary computation,
dynamical systems, stochastic processes, and fixed latent search spaces.

## Target

The target is the E087 properness gate:

```text
formed present domain
witnessed extension
unavailability in prior context
no hidden completed oracle
recordability
```

An absorber wins if it represents every accepted source step as ordinary state evolution,
access, sampling, search, or projection without violating that gate.

## Absorber Results

| Absorber | Verdict | Reason |
| --- | --- | --- |
| Finite-state transition system | Absorbs finite traces only | A finite option pool precontains all possible accepted moves. Any "new" move is either state transition or access. |
| Countable-state transition system with fixed transition relation | Absorbs if the relation is fixed | The graph of possible moves is already given. Discovery is traversal. |
| Turing machine with expanding tape | Absorbs computably generated contexts | Tape growth is not source issuance when the update rule and grammar are fixed. |
| Interactive computation | Absorbs if all input channels and protocols are fixed | Unknown input can surprise the observer, but the machine class still treats the channel as an ambient source. |
| Oracle computation | Absorbs externally, violates internally | A sufficiently strong oracle can encode the whole trace, but E087 forbids the oracle as an internal formed source object. |
| Stochastic process with fixed law | Absorbs probabilistic novelty | Sampling from a fixed law produces uncertainty, not new admissibility. |
| Bayesian nonparametric fixed hyperprior | Absorbs open-ended-looking class growth | New clusters/classes are draws from a fixed prior or construction rule. |
| Adaptive control / reinforcement learning | Absorbs policy and model updates | Learning changes agent state, not source admissibility, unless the admissible action space itself changes without fixed latent precontainment. |
| Evolutionary search / genetic algorithms | Absorbs recombination and mutation search | Large or creative search remains fixed generator plus selection unless mutation operators or genotype space are source-issued. |
| Fixed latent graph plus access schedule | Absorbs adjacent-possible disclosure | Revealed edges or nodes are projection/access novelty, not source issuance. |

## Strongest Surviving Case

The computation gauntlet leaves only a narrow residue:

```text
An OnlineIssuance trace survives ordinary adaptive-computation absorption only when the accepted
extension cannot be generated from any fixed computable rule, fixed transition graph, fixed
stochastic law, fixed hyperprior, fixed input protocol, or fixed latent graph available at the
prior prefix, and when representing it requires adding an oracle over future contexts that is
not well-formed inside the source context.
```

This is exactly the E055-style class:

```text
self-encoding admissibility
diagonal/productive successor
no internally formed future-schema oracle
```

## What This Does Not Prove

This does not prove physical source issuance.

This does not defeat an external Platonist oracle. A meta-theory can always say:

```text
There is a completed object containing the entire future trace.
```

The result is class-relative:

```text
OnlineIssuance is not absorbed by fixed-law adaptive computation without changing the class to
external oracle / completed-source navigation.
```

## Path Kill

Killed:

```text
finite_computable_fixed_law_or_fixed_latent_growth_as_source_issuance
```

Reason:

```text
Finite, computable, stochastic fixed-law, fixed-hyperprior, adaptive-search, and fixed-latent
models can generate observer novelty and apparent opportunity growth without source issuance.
```

## Goal 2 Verdict

```yaml
goal_2: complete
adaptive_computation_absorber: partially_defeated_class_relatively
absorbed:
  - finite_option_growth
  - computable_context_growth
  - fixed_transition_graph_growth
  - fixed_law_stochastic_growth
  - fixed_hyperprior_class_growth
  - adaptive_search_growth
  - fixed_latent_graph_disclosure
survives_only_as: >
  constructive/productive source extension where the oracle needed to precontain future
  admissible witnesses is not well-formed inside the prior source context.
claim_status_change: none
next_goal: category_theory_bookkeeping_absorber
```

