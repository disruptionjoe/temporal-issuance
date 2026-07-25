---
artifact_type: exploration
status: active_evidence
run_id: RUN-20260725-080909-temporal-issuance-progress
---

# E202: Device-Independent Randomness Amplification Is Not Degree Escape

## Question

Does a composable device-independent randomness-amplification theorem close
E199's source-degree guard `J_H not <=_T O`?

## Named construction and fork

Kessler and Arnon-Friedman, *Device-independent Randomness Amplification and
Privatization* ([arXiv:1705.04148](https://arxiv.org/abs/1705.04148)), prove a
protocol using a public Santha-Vazirani source and two-component device against
the theorem's stated quantum-adversary model. Its conclusion is operational:
the extracted string is close to uniform/secret in that model.

| object | construction used | strongest rival |
| --- | --- | --- |
| entropy object | composable smooth/min-entropy style secrecy against the stated quantum side information | a stage-0 oracle containing a completed realized history or branch family |
| target conclusion | bounded guessing/secrecy in the theorem model | `J_H not <=_T O` for every admissible fixed oracle |

The rival is not a quantum adversary instance merely because it is fixed at
stage 0. E199 already shows fixedness alone does not exclude an oracle carrying
the relevant history. The theorem does not claim to type every such oracle, nor
does it conclude individual-sequence algorithmic randomness or Turing
non-reducibility.

## Result

`tools/e202_randomness_amplification_degree_boundary.py` freezes the type
separation. The named theorem earns the operational entropy conclusion, but
the E199 guard requires two additional propositions: coverage of all admitted
stage-0 information and a non-reducibility conclusion. Neither is supplied.

```yaml
result: COMPOSABLE_ENTROPY_BOUND_WITH_DEGREE_RESIDUE
operational_entropy_conclusion: true
all_stage_zero_side_information_typed: false
turing_nonreducibility_proved: false
e199_degree_guard_established: false
physical_source_issuance_established: false
claim_status_change: none
```

This is material negative progress: finite device-independent secrecy is
stronger than Cosmic Bell's corrupt-trial frequency budget, but still has the
wrong conclusion type for source-degree separation. Do not promote statistical
or composable randomness into issuance.
