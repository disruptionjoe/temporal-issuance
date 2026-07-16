---
artifact_type: exploration
status: complete
governance_role: physical_witness_candidate
run_id: RUN-0167
created: 2026-07-16
claim_refs:
  - TI-C019
  - TI-C020
claim_status_change: none
depends_on:
  - COMPLETION-CLASS.md
  - steward/research-portfolio.json
  - explorations/E149-physical-candidates-state-space-growth-intake-2026-07-07.md
  - explorations/E185-crispr-spacer-acquisition-candidate-v0-2026-07-16.md
  - tools/dynamic_floquet_code_candidate_v0.py
  - tests/test_dynamic_floquet_code_candidate_v0.py
---

# E186: Dynamic/Floquet Quantum-Code Candidate v0

## Question

Can dynamic/Floquet quantum-code logical-qubit generation supply a physical
source-side issuance witness for the `PHYSICAL-ISSUANCE-WITNESS` campaign?

## Verdict

No. The candidate has a real logical-sector formation signal, but it fails
closed as fixed Hilbert-space and stabilizer/gauge-family dynamics under a
predeclared time-periodic measurement schedule, boundary data, decoder/readout
rule, noise or syndrome random tape, access schedule, gauge relabeling, and
completed syndrome history.

```yaml
candidate_status: CANDIDATE_KILLED_FIXED_CODE_SCHEDULE
completion_class_verdict: PHYSICAL_PREDICTIVE_ABSORPTION
packet_admitted: false
typed_action_2_packet: false
native_source_law_supplied: false
physical_source_issuance_established: false
TI_C020_reopened: false
claim_status_change: none
```

## Candidate Shape

The candidate covers dynamic or Floquet quantum-code settings where logical
structure appears across a period even though an instantaneous static code
description may not expose the same protected subsystem. It is a strong
negative control because it looks like code-space growth while the rival can
freeze the physical substrate and schedule before evaluating the event.

The strongest fixed-source rival is frozen before evaluation:

```text
fixed physical qubit Hilbert space
+ fixed stabilizer/gauge family
+ fixed time-periodic measurement and control schedule
+ fixed boundary and initialization data
+ fixed decoder and logical readout rule
+ noise or syndrome random tape
+ completed syndrome history
```

## Adapter Result

| Field | Result |
| --- | --- |
| `Gamma_n` | supplied as fixed physical qubit Hilbert space, stabilizer/gauge checks, noise model, boundary conditions, and time-periodic measurement schedule |
| `Adm_n` | not source-supplied; supplied by fixed schedule, gauge/stabilizer constraints, boundary, syndrome rules, and decoder |
| `e_n` | supplied as time-scheduled appearance of a logical qubit or protected subsystem |
| `w_n` | supplied as syndrome history, logical operator support, decoder transcript, and record trace |
| `Gamma_{n+1}` | not source-supplied; same fixed code family after one period or decoder-visible access change |
| `tau_n` | supplied as period-by-period syndrome and logical-support record |

## W1-W6 Result

| Gate | Result |
| --- | --- |
| W1 non-isomorphic source algebra | logical signal present, source pass absent |
| W2 new admissibility predicate | logical signal present, source pass absent |
| W3 construction-space growth | logical signal present, source pass absent |
| W4 perturbation non-factorization | absent |
| W5 record preservation | present |
| W6 fixed-family / after-naming absorption | absent |

The result is not blocked by records. It is blocked because the apparent new
logical sector is represented by the fixed physical algebra plus the
predeclared stabilizer/gauge schedule, decoder, boundary data, and completed
syndrome history.

## CompletionClass v1 Result

The verified completion witness is:

```text
fixed_floquet_code_schedule_completion
```

It absorbs the candidate through:

- `boundary_condition`
- `fixed_source`
- `stochastic_seed`
- `resource_capability`
- `whole_family`
- `completed_history`
- `observer_information_access`
- `relabel_gauge`

All other primitive families are represented and nonfactorized for this
bounded candidate, so the decisive verdict is
`PHYSICAL_PREDICTIVE_ABSORPTION`.

## Exact Missing Source Object

```yaml
missing_object_id: source_owned_code_space_generation_law
required: >
  A native physical source law in which the code source creates a new
  admissibility predicate, logical algebra, or construction grammar not
  representable as fixed Hilbert space, fixed stabilizer/gauge family, fixed
  time-periodic schedule, boundary data, decoder/readout access, noise or
  syndrome random tape, or completed syndrome history.
also_required: >
  An internal anti-after-naming principle plus W4 perturbation
  non-factorization under the same preserved syndrome, logical-support,
  boundary, and decoder records.
```

Do not repeat dynamic/Floquet quantum-code, scheduled stabilizer/gauge-code, or
logical-qubit-generation candidates unless a later packet supplies that
missing source object.

## Executable Artifact

```text
tools/dynamic_floquet_code_candidate_v0.py
tests/test_dynamic_floquet_code_candidate_v0.py
tests/artifacts/dynamic_floquet_code_candidate_v0_result.json
```

## Next-Work Handoff

Continue `TI-PHYSICAL-WITNESS-GENERATION`, excluding the five killed campaign
classes: effective gauge/topological-sector candidates, monitored-dynamics
phase-transition candidates, crossed-product gravitational observer-algebra
bookkeeping candidates, CRISPR / biological sequence-acquisition candidates,
and dynamic/Floquet scheduled-code logical-sector candidates under fixed
Hilbert-space completion unless their missing source objects appear.

The next worthwhile swing should choose another non-overlapping physically
serious candidate with a source-owned transition law before the fixed rival is
evaluated, or state a bounded no-go target only if it can be expressed without
universalizing beyond tested candidate classes.

## Nonclaims

- No physical source issuance is established.
- No claim status changed.
- `TI-C020` remains speculative.
- E177 is unchanged.
- No cross-repo implication or external action occurred.
