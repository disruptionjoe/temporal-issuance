---
artifact_type: exploration
status: complete
governance_role: physical_witness_candidate
run_id: RUN-0170
created: 2026-07-16
claim_refs:
  - TI-C019
  - TI-C020
claim_status_change: none
depends_on:
  - COMPLETION-CLASS.md
  - steward/research-portfolio.json
  - explorations/E149-physical-candidates-state-space-growth-intake-2026-07-07.md
  - agent-runs/RUN-0169-p2cw1-whole-family-adjudication.md
  - tools/autocatalytic_reaction_network_candidate_v0.py
  - tests/test_autocatalytic_reaction_network_candidate_v0.py
---

# E188: Autocatalytic Reaction-Network Candidate v0

## Question

Can autocatalytic chemical reaction-network emergence supply a physical
source-side issuance witness for the `PHYSICAL-ISSUANCE-WITNESS` campaign?

## Verdict

No. The candidate has a real autocatalytic closure signal, but it fails closed
as fixed reaction-network completion: fixed species alphabet, fixed reaction
graph, fixed catalyst inventory, fixed rate laws, feedstock and boundary flux,
initial concentrations, stochastic collision or reaction tape, observer naming,
and completed reaction history reproduce the candidate.

```yaml
candidate_status: CANDIDATE_KILLED_FIXED_REACTION_NETWORK
completion_class_verdict: PHYSICAL_PREDICTIVE_ABSORPTION
packet_admitted: false
typed_action_2_packet: false
native_source_law_supplied: false
physical_source_issuance_established: false
TI_C020_reopened: false
claim_status_change: none
```

## Candidate Shape

The candidate covers chemical cases where a set of reactions becomes
self-sustaining or autocatalytically closed after a concentration threshold,
feedstock condition, or catalyst-supported pathway appears. It is a strong
negative control because it resembles adjacent-possible growth while the rival
can freeze the entire reaction grammar before evaluating the event.

The strongest fixed-source rival is frozen before evaluation:

```text
fixed molecular species alphabet
+ fixed reaction graph
+ fixed catalyst inventory
+ fixed rate-law table
+ fixed feedstock and reactor boundary flux
+ seed concentrations as initial condition
+ stochastic collision or reaction tape
+ completed reaction history
```

## Adapter Result

| Field | Result |
| --- | --- |
| `Gamma_n` | supplied as fixed species, reactions, catalysts, rates, feedstock, and boundary |
| `Adm_n` | not source-supplied; supplied by the fixed graph and rate-law table |
| `e_n` | supplied as catalytic closure under fixed feedstock and rates |
| `w_n` | supplied as abundance trace, reaction events, closure certificate, flux record, and perturbation response |
| `Gamma_{n+1}` | not source-supplied; same fixed reaction network after threshold crossing or path selection |
| `tau_n` | supplied as time-ordered reaction and abundance history |

## W1-W6 Result

| Gate | Result |
| --- | --- |
| W1 non-isomorphic source algebra | autocatalytic signal present, source pass absent |
| W2 new admissibility predicate | autocatalytic signal present, source pass absent |
| W3 construction-space growth | autocatalytic signal present, source pass absent |
| W4 perturbation non-factorization | absent |
| W5 record preservation | present |
| W6 fixed-family / after-naming absorption | absent |

The result is not blocked by records. It is blocked because the apparent new
self-sustaining chemical organization is represented by a fixed molecular
species alphabet, reaction graph, catalyst inventory, rate-law table,
feedstock/boundary context, seed concentrations, stochastic reaction path, and
completed history.

## CompletionClass v1 Result

The verified completion witness is:

```text
fixed_reaction_network_completion
```

It absorbs the candidate through all eleven CompletionClass v1 primitive
families:

- `hidden_state`
- `initial_condition`
- `boundary_condition`
- `fixed_source`
- `stochastic_seed`
- `name_provenance`
- `resource_capability`
- `whole_family`
- `completed_history`
- `observer_information_access`
- `relabel_gauge`

The decisive verdict is `PHYSICAL_PREDICTIVE_ABSORPTION`.

## Exact Missing Source Object

```yaml
missing_object_id: source_owned_reaction_grammar_expansion_law
required: >
  A native physical source law in which the chemistry creates a new
  admissibility predicate, species algebra, reaction rule, or catalysis grammar
  not representable as fixed species alphabet, fixed reaction graph, fixed rate
  law, feedstock or boundary input, seed concentration, stochastic collision
  tape, observer naming, or completed reaction history.
also_required: >
  An internal anti-after-naming principle plus W4 perturbation non-factorization
  under the same preserved abundance, flux, closure, and perturbation records.
```

Do not repeat autocatalytic-set, chemical adjacent-possible, origin-of-life
reaction-closure, or generic reaction-network emergence claims unless a later
packet supplies that missing source object.

## Executable Artifact

```text
tools/autocatalytic_reaction_network_candidate_v0.py
tests/test_autocatalytic_reaction_network_candidate_v0.py
tests/artifacts/autocatalytic_reaction_network_candidate_v0_result.json
```

## Next-Work Handoff

Continue `TI-PHYSICAL-WITNESS-GENERATION`, excluding the seven killed campaign
classes: effective gauge/topological-sector candidates, monitored-dynamics
phase-transition candidates, crossed-product gravitational observer-algebra
bookkeeping candidates, CRISPR/adaptive immune sequence-acquisition
candidates, dynamic/Floquet scheduled-code logical-sector candidates,
prion-like conformational templating or strain-branching candidates, and
autocatalytic reaction-network emergence candidates under fixed reaction-network
completion unless their missing source objects appear.

The next worthwhile swing should choose another non-overlapping physically
serious candidate with a source-owned transition law before the fixed rival is
evaluated, or state a bounded no-go target only when the tested family is
specific enough to avoid universalizing beyond the candidate evidence.

## Nonclaims

- No physical source issuance is established.
- No claim status changed.
- `TI-C020` remains speculative.
- E177 is unchanged.
- No cross-repo implication or external action occurred.
