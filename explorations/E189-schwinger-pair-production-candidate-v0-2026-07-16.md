---
artifact_type: exploration
status: complete
governance_role: physical_witness_candidate
run_id: RUN-0171
created: 2026-07-16
claim_refs:
  - TI-C019
  - TI-C020
claim_status_change: none
depends_on:
  - COMPLETION-CLASS.md
  - steward/research-portfolio.json
  - agent-runs/RUN-0170-autocatalytic-reaction-network-candidate-v0.md
  - tools/schwinger_pair_production_candidate_v0.py
  - tests/test_schwinger_pair_production_candidate_v0.py
---

# E189: Schwinger Pair-Production Candidate v0

## Question

Can Schwinger vacuum pair production supply a physical source-side issuance
witness for the `PHYSICAL-ISSUANCE-WITNESS` campaign?

## Verdict

No. The candidate has a real particle-formation signal, but it fails closed as
fixed QFT background-field completion: fixed Lagrangian, charged field content,
external field profile, boundary conditions, vacuum preparation, couplings and
renormalization, detector access, stochastic vacuum amplitude, and completed
field history reproduce the candidate.

```yaml
candidate_status: CANDIDATE_KILLED_FIXED_QFT_BACKGROUND
completion_class_verdict: PHYSICAL_PREDICTIVE_ABSORPTION
packet_admitted: false
typed_action_2_packet: false
native_source_law_supplied: false
physical_source_issuance_established: false
TI_C020_reopened: false
claim_status_change: none
```

## Candidate Shape

The candidate covers strong-field QFT cases where the vacuum state yields
charged pairs under an external electric field. It is a strong negative control
because "particles from vacuum" looks like new physical content while the rival
can freeze the theory, background field, and measurement context before
evaluating the event.

The strongest fixed-source rival is frozen before evaluation:

```text
fixed QFT Lagrangian
+ fixed charged field content
+ fixed external field profile
+ fixed boundary conditions
+ fixed vacuum state
+ fixed couplings and renormalization
+ stochastic vacuum amplitude or mode tape
+ detector access and completed field history
```

## Adapter Result

| Field | Result |
| --- | --- |
| `Gamma_n` | supplied as fixed QFT, charged sector, background field, boundary, vacuum, and renormalization |
| `Adm_n` | not source-supplied; supplied by fixed equations, spectrum, boundary, and field profile |
| `e_n` | supplied as nonzero pair-production amplitude or occupation transition |
| `w_n` | supplied as detector counts, occupation record, field-strength trace, energy budget, and retarded response |
| `Gamma_{n+1}` | not source-supplied; same fixed QFT sector after occupation or detector access |
| `tau_n` | supplied as time-ordered background-field, occupation, and detector history |

## W1-W6 Result

| Gate | Result |
| --- | --- |
| W1 non-isomorphic source algebra | pair signal present, source pass absent |
| W2 new admissibility predicate | pair signal present, source pass absent |
| W3 construction-space growth | pair signal present, source pass absent |
| W4 perturbation non-factorization | absent |
| W5 record preservation | present |
| W6 fixed-family / after-naming absorption | absent |

The result is not blocked by records. It is blocked because the apparent
particle production is represented by a fixed field algebra, fixed charged
sector, fixed external field, fixed boundary and vacuum preparation, detector
access, stochastic amplitude, and completed history.

## CompletionClass v1 Result

The verified completion witness is:

```text
fixed_qft_background_completion
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
missing_object_id: source_owned_field_algebra_expansion_law
required: >
  A native physical source law in which the pair-production event creates a new
  field algebra, charged sector, admissibility predicate, or transition grammar
  not representable as fixed QFT Lagrangian, fixed background field profile,
  fixed boundary condition, fixed vacuum state, stochastic amplitude, observer
  access, or completed field history.
also_required: >
  An internal anti-after-naming principle plus W4 perturbation non-factorization
  under the same preserved detector, occupation, field-strength, energy, and
  retarded-response records.
```

Do not repeat Schwinger, vacuum-pair-production, generic "particles from
vacuum", or background-field particle-formation claims unless a later packet
supplies that missing source object.

## Executable Artifact

```text
tools/schwinger_pair_production_candidate_v0.py
tests/test_schwinger_pair_production_candidate_v0.py
tests/artifacts/schwinger_pair_production_candidate_v0_result.json
```

## Next-Work Handoff

Continue `TI-PHYSICAL-WITNESS-GENERATION`, excluding the eight killed campaign
classes: effective gauge/topological-sector candidates, monitored-dynamics
phase-transition candidates, crossed-product gravitational observer-algebra
bookkeeping candidates, CRISPR/adaptive immune sequence-acquisition
candidates, dynamic/Floquet scheduled-code logical-sector candidates,
prion-like conformational templating or strain-branching candidates,
autocatalytic reaction-network emergence candidates, and Schwinger/vacuum
pair-production candidates under fixed QFT background-field completion unless
their missing source objects appear.

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
