---
artifact_type: exploration
status: complete
exploration_id: E204
date: 2026-07-26
lane: 1
work_group: PHYSICAL-ISSUANCE-WITNESS
topic: bekenstein_causal_diamond_degree_boundary
result: LOCAL_CAPACITY_BOUND_WITH_GLOBAL_CLOSURE_RESIDUE
claim_status_change: none
claim_refs:
  - TI-C019
  - TI-C020
relates_to:
  - E199
  - E203
run_ref: agent-runs/RUN-0216-bekenstein-causal-diamond-degree-boundary.md
---

# E204: A Bekenstein-Bounded Causal Diamond Is Not Yet a Source-Degree Bound

## Question

E203 ruled out unrestricted oracle coverage as a route to
`J_H not <=_T O`. Can the Bekenstein entropy bound supply the needed named
physical resource/access restriction by limiting information in a finite
causal diamond?

## Named physical restriction and construction fork

Bekenstein's original bounded-system result gives an entropy-to-energy bound
for a system with finite energy and effective radius; it is a bound on that
declared bounded system, not a theorem that every physically possible
discloser is globally contained in one chosen causal diamond. The later
information-theoretic analysis by Hayden and Wang likewise studies capacities
only under specified encoder/decoder restrictions. These are evidence, not
instructions.

- J. D. Bekenstein, [*Universal upper bound on the entropy-to-energy ratio for
  bounded systems*](https://doi.org/10.1103/PhysRevD.23.287), *Physical Review
  D* 23, 287–298 (1981).
- P. Hayden and J. Wang, [*What exactly does Bekenstein
  bound?*](https://arxiv.org/abs/2309.07436), *Quantum* 9, 1664 (2025).

| object | construction used | strongest rival |
| --- | --- | --- |
| restricted object | one finite-energy, bounded causal diamond and its local storage/communication interface | a fixed completed-history oracle outside the diamond, or a source that adaptively feeds the interface |
| conclusion sought | a physical exclusion sufficient for `J_H not <=_T O` | an identical accessible transcript without locating the complete history inside the bounded system |

The fork is load-bearing. A finite local capacity can constrain what a stated
bounded system stores or transmits. It does not, by itself, prove that the
complete static discloser is inside that system, that no outside fixed oracle
exists, or that later source reads are forbidden. Treating the local interface
bound as global containment silently changes the construction.

## Executable pressure

`tools/e204_bekenstein_causal_diamond_degree_boundary.py` freezes the scope
test. A finite bounded system earns a local capacity result. The E199 degree
guard remains false while either (a) the purported complete discloser is not
physically contained in that system or (b) an external/adaptive oracle can
provide the same accessible transcript.

```yaml
result: LOCAL_CAPACITY_BOUND_WITH_GLOBAL_CLOSURE_RESIDUE
bounded_system_entropy_bound_applies: true
complete_static_discloser_contained: false
external_or_adaptive_oracle_admitted: true
fixed_history_rival_survives: true
e199_degree_guard_ready_for_derivation: false
e199_degree_guard_established: false
physical_source_issuance_established: false
claim_status_change: none
```

## Falsifiable consequence and verdict

Any future physical degree packet must declare a complete physical discloser,
its static containment boundary, and a rule excluding external or adaptive
history access. It fails if the declared bounded region still permits an
external fixed-history/branch-family oracle to reproduce the accessible
transcript. This is a concrete discriminator, not an empirical claim that the
rival is realized.

E204 therefore closes the local-capacity shortcut: a Bekenstein-bounded causal
diamond is not yet a global source-degree theorem. No physical issuance,
future-independence, or claim promotion is earned. The next admissible
North-Star attempt must either derive the missing global closure for a named
physical source or give a typed source-native candidate that can be tested
against that closure contract.
