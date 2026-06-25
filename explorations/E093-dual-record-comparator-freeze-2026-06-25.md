---
artifact_type: exploration
status: active
governance_role: fixture_comparator_freeze
run_ref: RUN-0083
claim_refs:
  - TI-C019
  - TI-C020
  - TI-C001
depends_on:
  - explorations/E083-dual-record-opportunity-steelman-vote-2026-06-25.md
  - explorations/E085-dual-record-opportunity-cross-repo-placement-2026-06-25.md
  - explorations/E092-w010-frontier-route-lock-dual-record-2026-06-25.md
---

# E093: Dual-Record Comparator Freeze

## Purpose

Freeze the comparator for the first executable dual-record adjacent-possible
fixture before code is written.

This protects the strong hypothesis from being flattened while also protecting
the repo from overclaiming.

Strong hypothesis:

```text
An opportunity-edge record may change the admissible move graph in a way that
helps escape local traps.
```

Conservative first formalization:

```text
A finite search fixture compares stable-only records, fixed-latent opportunity
records, and growing-adjacency opportunity records under equal budget. It can
show a bounded residue relative to a declared comparator, but it cannot by
itself prove source-side issuance.
```

## Fixture Objects

```text
S_n  stabilized public/action record:
     accepted state, score, provenance, and accepted-edge history

O_n  opportunity-edge record:
     available non-final candidate moves, failed local probes, latent edges
     exposed, generated edges, and stuckness markers

G_n  current move graph:
     the edges admissible for proposals at step n

K_n  proposal kernel:
     deterministic ranked proposal rule over outgoing edges in G_n

T_n  transfer/finality rule:
     accepted opportunity edge becomes part of S_{n+1}; rejected or unused
     opportunity data stays in O_n or enters Lose[K]
```

## Frozen Finite Landscape

The executable fixture should use this small hostile landscape:

```text
states: 0..10
start: 0
target: 10
budget: 8 proposal attempts
base graph: i -> i+1 and i -> i-1 when in range
acceptance rule: accept only moves with score >= current score
```

Score table:

```text
0: 0
1: 1
2: 3   local trap under base moves
3: 2
4: 1
5: 0
6: 2
7: 4
8: 7
9: 9
10: 12
```

The base graph traps greedy monotone search at state 2. Any escape must either
accept a downhill move, reveal a latent shortcut, restart/noise into another
basin, or generate a new adjacency edge.

## Compared Systems

### A. Single-Record Search

```text
record regime: S_n only
graph: base graph only
proposal rule: highest-scoring admissible outgoing edge not yet exhausted
edge growth: none
```

Expected role:

```text
negative control; should get trapped at state 2.
```

### B0. Dual-Record Fixed-Latent Search, Limited Comparator

```text
record regime: S_n + O_n
graph: base graph plus declared latent edge reservoir
latent reservoir:
  0 -> 4
  1 -> 5
  3 -> 7
access schedule: expose one latent edge per proposal attempt if its source is
                 the current stable state
edge growth: none
critical bridge 2 -> 7: absent by declaration
```

Expected role:

```text
tests whether ordinary opportunity access, without the critical bridge, beats
the single-record trap.
```

### B1. Dual-Record Fixed-Latent Search, Exact Absorber Panel

```text
record regime: S_n + O_n
graph: base graph plus declared latent edge reservoir
latent reservoir:
  2 -> 7
access schedule: expose critical latent edge when stuckness threshold is met
edge growth: none
```

Expected role:

```text
absorber control. If B1 reproduces C, the result is not source-side issuance.
```

### C. Dual-Record Growing-Adjacency Search

```text
record regime: S_n + O_n
graph: base graph initially
stuckness threshold: 2 consecutive failed/non-improving proposal attempts at
                     the same stable state
growth rule: when stuckness threshold is met, add the smallest forward edge
             current -> j such that score(j) > score(current), if no existing
             admissible outgoing edge improves the current score
max generated jump: 5 states
critical generated edge from state 2: 2 -> 7
```

Expected role:

```text
tests the bounded growing-adjacency version of the hypothesis.
```

## Equal-Budget Rule

Every proposal, latent-edge exposure attempt, and generated-edge attempt counts
against the same budget of 8 attempts.

Stable transfer rule:

```text
If a proposed edge is accepted, append it to S_n provenance and update the
stable state. If it is not accepted, record it in O_n and increment stuckness.
```

Loss rule:

```text
When O_n is summarized into S_n, failed probes and unused opportunity edges are
not part of the stable action record. They remain audit data or enter Lose[K].
```

## Measurements

The fixture must report:

```text
final_state
final_score
target_reached
proposal_attempts
accepted_edges
failed_probes
latent_edges_exposed
generated_edges
best_score
stuckness_events
effect_verdict
absorber_verdict
```

## Verdict Rules

Primary bounded residue:

```text
C beats A and B0 under equal budget, and the useful edge is absent from B0's
declared fixed latent reservoir.
```

Absorber result:

```text
B1 reproduces C when the critical edge is placed in a fixed latent reservoir
with a matching access trigger.
```

Effect typing:

```text
If C beats A/B0 but B1 reproduces C:
  Project[O] + Finalize[R] + Lose[K]
  not Issue[S]

If C beats A/B0 and a declared broad fixed-latent comparator cannot reproduce
it:
  bounded Issue[S] candidate only, requiring later hostile review

If C does not beat A/B0:
  absorbed_by_standard_search_or_record_architecture
```

## Absorber List

The result must be demoted if reproduced by:

```text
fixed latent graph plus access schedule
simulated annealing or downhill acceptance
random restart
evolutionary search
ordinary novelty search
Bayesian nonparametric generation from a fixed hyperprior
enriched reachability / opportunity-set accounting
```

## Next Artifact

The executable fixture should be created in Time as Finality:

```text
models/dual_record_opportunity_fixture.py
models/run_dual_record_opportunity_fixture.py
tests/test_dual_record_opportunity_fixture.py
results/dual-record-opportunity-fixture-v0.1-results.md
results/dual-record-opportunity-fixture-v0.1.json
```

## Verdict

```yaml
comparator_frozen: true
primary_fixture_home: time-as-finality
expected_positive_scope: bounded_residue_relative_to_declared_limited_comparator
expected_absorber: exact_fixed_latent_edge_reproduces_C
claim_status_change: none
next_trigger: implement_dual_record_adjacent_possible_fixture
```
