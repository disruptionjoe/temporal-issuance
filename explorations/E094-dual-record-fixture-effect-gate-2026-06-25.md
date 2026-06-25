---
artifact_type: exploration
status: active
governance_role: effect_gate_verdict
run_ref: RUN-0086
claim_refs:
  - TI-C019
  - TI-C020
  - TI-C001
depends_on:
  - explorations/E093-dual-record-comparator-freeze-2026-06-25.md
  - ../time-as-finality/results/dual-record-opportunity-fixture-v0.1-results.md
---

# E094: Dual-Record Fixture Effect Gate

## Purpose

Apply the Temporal Issuance source/shadow/finality effect gate to the Time as
Finality dual-record opportunity fixture.

## Input Result

Time as Finality implemented:

```text
models/dual_record_opportunity_fixture.py
tests/test_dual_record_opportunity_fixture.py
results/dual-record-opportunity-fixture-v0.1-results.md
```

Focused tests:

```text
5/5 passing
```

Fixture summary:

```text
A  single-record search traps at state 2
B0 limited fixed-latent search traps at state 2
C  growing-adjacency search generates 2 -> 7 and reaches target 10
B1 exact fixed-latent absorber exposes 2 -> 7 and also reaches target 10
```

## Strong Hypothesis Preserved

The strong hypothesis remains:

```text
Some systems may maintain opportunity-edge records that change admissible move
graphs and help escape local minima.
```

The fixture supports a bounded version:

```text
C beats A and B0 under equal budget.
```

This should not be flattened into "nothing happened." Something did happen:
the opportunity record changed the local move graph in the finite model.

## Conservative Effect Verdict

The source-side reading is absorbed:

```text
B1 reproduces C once the critical edge 2 -> 7 is supplied as a fixed latent
edge with a matching access trigger.
```

Therefore:

```text
Project[O]   yes
Finalize[R]  yes
Lose[K]      yes
Issue[S]     no
```

## Source Issuance Gate

Candidate source object:

```text
issued_object = edge 2 -> 7
```

Gate result:

```text
SI-1 online availability relative to B0: passes locally
SI-2 no hidden future schema: fails under B1
SI-3 admissibility growth: fails under exact fixed-latent absorber
SI-4 recordability: passes
```

Verdict:

```text
not source_issuance_candidate
```

The correct classification is:

```text
projection_access_novelty
record_finality_only
lossy_projection_residue
absorber_controlled_bookkeeping
```

## Why The Strong Form Was Not Lost

The conservative verdict does not erase the information in the strong form.

Retained information:

```text
stable records and opportunity-edge records are distinct regimes;
opportunity records can change finite proposal kernels;
local-minimum escape is a meaningful observable;
the bounded residue is real relative to a declared limited comparator.
```

Demoted information:

```text
the finite C result is not evidence of source-side issuance unless the exact
fixed-latent absorber is defeated.
```

## Claim Effects

```yaml
TI-C020:
  status: speculative
  movement: none
  note: >
    The fixture supplies no physical-source evidence. It strengthens the
    fixed-latent/access-schedule absorber for opportunity-regime claims.

TI-C019:
  status: formalizing
  movement: none
  note: >
    The dual-record line remains useful as a discriminator vocabulary, but this
    finite fixture does not affect the OnlineIssuance^LC formal residue.

TI-C001:
  status: weakened
  movement: none
  note: >
    Stable/opportunity record separation remains reconstruction vocabulary.
```

## Path Kill

Kill this shortcut:

```text
dual-record growing-adjacency success in the finite fixture
=> source-side Temporal Issuance evidence
```

Reason:

```text
exact fixed latent edge plus matching access trigger reproduces the result.
```

## Next Artifact

Proceed to the GU observer-finality stress witness only as a bounded capability
and section-retrieval crosswalk:

```text
DualRecordSectionRetrievalWitness_v0_1
```

Guardrail:

```text
Use the result as observer-finality/capability vocabulary, not as GU source
geometry and not as source-side issuance evidence.
```

## Verdict

```yaml
effect_gate_complete: true
fixture_result: bounded_growing_adjacency_residue_relative_to_B0
absorber_result: exact_fixed_latent_edge_absorbs_source_side_reading
effect_verdict:
  Issue[S]: false
  Project[O]: true
  Finalize[R]: true
  Lose[K]: true
claim_status_change: none
next_trigger: GU_dual_record_section_retrieval_witness
```
