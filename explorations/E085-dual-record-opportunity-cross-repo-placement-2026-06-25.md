---
artifact_type: exploration
status: active
governance_role: cross_repo_placement
run_ref: RUN-0075
claim_refs:
  - TI-C020
  - TI-C001
  - TI-C019
related:
  - explorations/E083-dual-record-opportunity-steelman-vote-2026-06-25.md
  - explorations/E067-source-shadow-finality-interface-contract-2026-06-24.md
  - explorations/E071-issued-capability-contract-test-2026-06-24.md
  - explorations/E082-sheafification-bridge-projection-absorber-2026-06-25.md
  - explorations/E084-legitimacy-monad-projection-finality-2026-06-25.md
  - ../time-as-finality/explorations/dual-record-opportunity-finality-crosswalk-2026-06-25.md
  - ../gu-formalization/explorations/time-as-finality-crosswalk/dual-record-opportunity-section-retrieval-v0.1.md
---

# E085: Dual-Record Opportunity Cross-Repo Placement

## Summary

The dual-record opportunity idea belongs primarily in Temporal Issuance as a
source/projection discriminator:

```text
stable record regime        = what has become reliable enough to build on
opportunity-edge regime     = what future moves are becoming admissible
```

The strong version is not "there are two layers." It is:

```text
a system's opportunity record may change the admissible move graph, not merely
reveal moves from a fixed latent graph.
```

That is exactly a Temporal Issuance question. If the opportunity regime only
changes observer access to a fixed `G_infty`, the result is `Project[O]` and
possibly `Finalize[R]` / `Lose[K]`, not `Issue[S]`. It pressures TI only if the
new move edge or operator cannot be represented as fixed-source bounded access.

## Placement

### Primary home: Temporal Issuance

TI owns the strongest discriminator:

```text
fixed latent move graph + access schedule
  versus
source-side growth of admissible move operators
```

This connects directly to:

- D4 type-novelty versus reachability novelty;
- E067 source-shadow-finality effect typing;
- E071 issued capability gates;
- E082 sheafification as projection/finality/loss;
- E084 legitimacy as observer-record finality, not source issuance.

### Fixture home: Time as Finality

Time as Finality is the natural executable home because it already has:

- finite record graphs;
- metastable finality and reversal-cost language;
- S3 event-DAG provenance;
- S4 probabilistic stabilization;
- S5 `Project[O] + Finalize[R] + Lose[K]`;
- S6/S7 sheafification and legitimacy thresholds;
- future-operation / opportunity-set audits.

The TaF fixture should measure whether opportunity records improve escape from
local minima while preserving the effect verdict.

### Crosswalk home: GU formalization

GU is a secondary stress surface only.

The idea can be useful for observer-finality and section-retrieval language:

```text
stable observer record       -> smooth observer-facing shadow
opportunity edge record      -> admissible future section/readout/capability
```

It must not be used as evidence that GU has two physical layers, that 4D/14D
splits are primary, or that a source geometry has been selected.

## Typed Object

Use the RUN-0075 fixture variables:

```text
S_n  stabilized public/action record
O_n  opportunity record over admissible move edges
G_n  current move graph
K_n  proposal kernel induced by O_n
T_n  transfer/finality rule from O_n to S_n
```

Effect reading:

```text
S_n stabilizes       -> Finalize[R]
O_n becomes visible  -> Project[O]
compressed/lost data -> Lose[K]
new source edge      -> Issue[S] only if the source gate passes
```

## Next Artifact

Recommended next executable artifact:

```text
dual_record_adjacent_possible_fixture_v0_1
```

Compare:

```text
A. single-record search
B. dual-record fixed-latent search
C. dual-record growing-adjacency search
```

Required outputs:

- local-minimum escape rate under equal budget;
- number and type of opportunity edges exposed or generated;
- whether every edge can be represented in a declared fixed `G_infty`;
- proposal-kernel change `K_n -> K_{n+1}`;
- finality transfer `T_n : O_n -> S_n`;
- effect verdict: `Issue[S]`, `Project[O]`, `Finalize[R]`, `Lose[K]`.

## Promotion And Demotion

Promote only to a stronger fixture line if C beats A and B under the declared
budget and the advantage cannot be re-described as fixed latent graph access,
annealing, random restart, evolutionary search, Bayesian nonparametrics,
ordinary novelty search, or enriched opportunity-set reachability.

Demote if the opportunity record is just:

```text
fixed G_infty + delayed access + stochastic exploration
```

In that case the idea remains useful record architecture, but not source-side
Temporal Issuance evidence.

## Verdict

```yaml
best_home: temporal-issuance
fixture_home: time-as-finality
gu_role: observer-finality stress surface only
status: fixture_candidate
claim_status_change: none
main_absorber: fixed_latent_graph_plus_access_schedule
next_artifact: dual_record_adjacent_possible_fixture_v0_1
```
