---
artifact_type: exploration
status: complete
governance_role: physical_witness_candidate
run_id: RUN-0168
created: 2026-07-16
claim_refs:
  - TI-C019
  - TI-C020
claim_status_change: none
depends_on:
  - COMPLETION-CLASS.md
  - steward/research-portfolio.json
  - explorations/E149-physical-candidates-state-space-growth-intake-2026-07-07.md
  - explorations/E186-dynamic-floquet-code-candidate-v0-2026-07-16.md
  - tools/prion_conformation_candidate_v0.py
  - tests/test_prion_conformation_candidate_v0.py
---

# E187: Prion Conformation Candidate v0

## Question

Can prion-like conformational templating or strain branching supply a physical
source-side issuance witness for the `PHYSICAL-ISSUANCE-WITNESS` campaign?

## Verdict

No. The candidate has a real conformational propagation signal, but it fails
closed as a fixed conformational-landscape completion: fixed protein sequence,
fixed environment/chaperone context, seed conformer, stochastic folding or
collision tape, assay labels, strain relabeling, and completed folding lineage.

```yaml
candidate_status: CANDIDATE_KILLED_FIXED_CONFORMATIONAL_LANDSCAPE
completion_class_verdict: PHYSICAL_PREDICTIVE_ABSORPTION
packet_admitted: false
typed_action_2_packet: false
native_source_law_supplied: false
physical_source_issuance_established: false
TI_C020_reopened: false
claim_status_change: none
```

## Candidate Shape

The candidate covers prion-like cases where a seed conformer templates a stable
folding strain, amyloid morphology, or phenotype-level branch without changing
the underlying protein sequence. It is a strong negative control because it
looks like new phenotype formation while the rival can freeze the molecular
state space and energy landscape before evaluating the event.

The strongest fixed-source rival is frozen before evaluation:

```text
fixed amino-acid sequence
+ fixed conformational energy landscape
+ fixed solvent, temperature, and chaperone/proteostasis context
+ seed conformer as initial condition
+ stochastic folding/collision tape
+ assay and strain-labeling rule
+ completed folding lineage history
```

## Adapter Result

| Field | Result |
| --- | --- |
| `Gamma_n` | supplied as fixed sequence, environment, chaperone context, and conformational landscape |
| `Adm_n` | not source-supplied; supplied by the fixed folding landscape, seed, boundary, and assay labels |
| `e_n` | supplied as seeded propagation of a stable conformational strain |
| `w_n` | supplied as folding trajectory, strain assay, morphology, and lineage record |
| `Gamma_{n+1}` | not source-supplied; same fixed landscape after seeded templating or observer-visible strain selection |
| `tau_n` | supplied as time-ordered propagation and phenotype trace |

## W1-W6 Result

| Gate | Result |
| --- | --- |
| W1 non-isomorphic source algebra | conformational signal present, source pass absent |
| W2 new admissibility predicate | conformational signal present, source pass absent |
| W3 construction-space growth | conformational signal present, source pass absent |
| W4 perturbation non-factorization | absent |
| W5 record preservation | present |
| W6 fixed-family / after-naming absorption | absent |

The result is not blocked by records. It is blocked because the apparent new
strain branch is represented by the fixed molecular state space plus fixed
energy landscape, seed, environment, stochastic folding path, assay readout,
and completed lineage history.

## CompletionClass v1 Result

The verified completion witness is:

```text
fixed_conformational_landscape_completion
```

It absorbs the candidate through:

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

All other primitive families are represented and nonfactorized for this bounded
candidate, so the decisive verdict is `PHYSICAL_PREDICTIVE_ABSORPTION`.

## Exact Missing Source Object

```yaml
missing_object_id: source_owned_conformational_grammar_expansion_law
required: >
  A native physical source law in which seeded propagation creates a new
  admissibility predicate, conformational grammar, or molecular state algebra
  not representable as fixed sequence, fixed conformational landscape, fixed
  environment/chaperone context, seed initial condition, stochastic folding
  tape, assay label, or completed folding history.
also_required: >
  An internal anti-after-naming principle plus W4 perturbation
  non-factorization under the same preserved strain, morphology, lineage, and
  phenotype records.
```

Do not repeat prion-like conformational templating, amyloid strain branching,
or phenotype-from-folding claims unless a later packet supplies that missing
source object.

## Executable Artifact

```text
tools/prion_conformation_candidate_v0.py
tests/test_prion_conformation_candidate_v0.py
tests/artifacts/prion_conformation_candidate_v0_result.json
```

## Next-Work Handoff

Continue `TI-PHYSICAL-WITNESS-GENERATION`, excluding the six killed campaign
classes: effective gauge/topological-sector candidates, monitored-dynamics
phase-transition candidates, crossed-product gravitational observer-algebra
bookkeeping candidates, CRISPR/adaptive immune sequence-acquisition
candidates, dynamic/Floquet scheduled-code logical-sector candidates, and
prion-like conformational templating or strain-branching candidates under
fixed conformational-landscape completion unless their missing source objects
appear.

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
