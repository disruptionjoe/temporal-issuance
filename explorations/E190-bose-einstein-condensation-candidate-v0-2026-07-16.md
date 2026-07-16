---
artifact_type: exploration
status: complete
governance_role: physical_witness_candidate
run_id: RUN-0172
created: 2026-07-16
claim_refs:
  - TI-C019
  - TI-C020
claim_status_change: none
depends_on:
  - COMPLETION-CLASS.md
  - steward/research-portfolio.json
  - agent-runs/RUN-0171-schwinger-pair-production-candidate-v0.md
  - tools/bose_einstein_condensation_candidate_v0.py
  - tests/test_bose_einstein_condensation_candidate_v0.py
---

# E190: Bose-Einstein Condensation Candidate v0

## Question

Can Bose-Einstein condensation supply a physical source-side issuance witness
for the `PHYSICAL-ISSUANCE-WITNESS` campaign?

## Verdict

No. The candidate has a real macroscopic-order formation signal, but it fails
closed as fixed many-body Hamiltonian completion: fixed bosonic field algebra,
Fock-space completion, particle species, trap geometry, interaction strength,
cooling path, reservoir, boundary conditions, seed fluctuations, measurement
access, and completed condensation history reproduce the candidate.

```yaml
candidate_status: CANDIDATE_KILLED_FIXED_MANY_BODY_HAMILTONIAN
completion_class_verdict: PHYSICAL_PREDICTIVE_ABSORPTION
packet_admitted: false
typed_action_2_packet: false
native_source_law_supplied: false
physical_source_issuance_established: false
TI_C020_reopened: false
claim_status_change: none
```

## Candidate Shape

The candidate covers bosonic many-body systems where cooling or density change
drives macroscopic ground-state occupation, phase coherence, interference, or
off-diagonal long-range order. It is a strong negative control because a new
macroscopic mode looks like new physical structure while the rival can freeze
the many-body theory and ensemble before evaluating the event.

The strongest fixed-source rival is frozen before evaluation:

```text
fixed many-body Hamiltonian
+ fixed bosonic field algebra
+ fixed particle species and Fock-space completion
+ fixed trap geometry
+ fixed interaction strength
+ fixed cooling trajectory and reservoir
+ fixed boundary conditions and symmetry-breaking seed
+ stochastic thermal fluctuation tape
+ measurement access and completed condensation history
```

## Adapter Result

| Field | Result |
| --- | --- |
| `Gamma_n` | supplied as fixed many-body Hamiltonian, bosonic field algebra, particle species, trap, interaction, cooling, reservoir, boundary, and seed |
| `Adm_n` | not source-supplied; supplied by fixed Hamiltonian, ensemble, particle-number sector, and cooling path |
| `e_n` | supplied as macroscopic occupation, phase coherence, or long-range-order transition |
| `w_n` | supplied as density profile, time-of-flight interference, condensate fraction, coherence, temperature, and cooling trace |
| `Gamma_{n+1}` | not source-supplied; same fixed bosonic field algebra after occupation or order-parameter selection |
| `tau_n` | supplied as time-ordered cooling, occupation, coherence, and measurement history |

## W1-W6 Result

| Gate | Result |
| --- | --- |
| W1 non-isomorphic source algebra | condensation signal present, source pass absent |
| W2 new admissibility predicate | condensation signal present, source pass absent |
| W3 construction-space growth | condensation signal present, source pass absent |
| W4 perturbation non-factorization | absent |
| W5 record preservation | present |
| W6 fixed-family / after-naming absorption | absent |

The result is not blocked by records. It is blocked because the apparent new
macroscopic mode is represented by a fixed field algebra, fixed Fock-space
completion, fixed Hamiltonian, fixed ensemble/cooling path, stochastic
fluctuations, measurement access, and completed history.

## CompletionClass v1 Result

The verified completion witness is:

```text
fixed_many_body_condensate_completion
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
missing_object_id: source_owned_condensate_mode_generation_law
required: >
  A native physical source law in which condensation creates a new mode
  algebra, admissibility predicate, transition grammar, or construction space
  not representable as fixed many-body Hamiltonian, fixed Fock-space
  completion, fixed trap geometry, fixed interaction strength, fixed
  reservoir/cooling path, stochastic fluctuation, observer access, or completed
  history.
also_required: >
  An internal anti-after-naming principle plus W4 perturbation
  non-factorization under the same preserved density, interference, coherence,
  condensate-fraction, temperature, and cooling records.
```

Do not repeat Bose-Einstein condensation, condensate-formation, macroscopic
occupation, or generic phase-coherence emergence claims unless a later packet
supplies that missing source object.

## Executable Artifact

```text
tools/bose_einstein_condensation_candidate_v0.py
tests/test_bose_einstein_condensation_candidate_v0.py
tests/artifacts/bose_einstein_condensation_candidate_v0_result.json
```

## Next-Work Handoff

Continue `TI-PHYSICAL-WITNESS-GENERATION`, excluding the nine killed campaign
classes: effective gauge/topological-sector candidates, monitored-dynamics
phase-transition candidates, crossed-product gravitational observer-algebra
bookkeeping candidates, CRISPR/adaptive immune sequence-acquisition
candidates, dynamic/Floquet scheduled-code logical-sector candidates,
prion-like conformational templating or strain-branching candidates,
autocatalytic reaction-network emergence candidates, Schwinger/vacuum
pair-production candidates, and Bose-Einstein-condensation/macroscopic
phase-coherence candidates under fixed many-body completion unless their
missing source objects appear.

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
