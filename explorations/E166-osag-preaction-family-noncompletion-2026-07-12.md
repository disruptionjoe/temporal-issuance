---
artifact_type: exploration
status: complete
governance_role: research_steering_wave_result
workflow: research_steering_wave2
claim_movement: false
created: 2026-07-12
central_run: RUN-0147
claim_refs:
  - TI-C019
  - TI-C020
depends_on:
  - explorations/E165-whole-family-completion-barrier-classifier-2026-07-12.md
  - tools/osag_preaction_family_noncompletion.py
  - tests/test_osag_preaction_family_noncompletion.py
---

# E166: OSAG Pre-Action Family Noncompletion

## Purpose

Wave 2 executed H2 from the research-steering plan:

```text
H2 pre-action family noncompletion source-action generator
```

H1 showed that bounded `Adapter_P` traces are absorbed by value, name,
provenance/action, or capability completion unless a pre-action family
noncompletion rule is part of the source action. H2 asks whether that rule can
be represented internally as an operative source-action generator (`OSAG`) or
whether it collapses to imported oracle language or after-fact singleton naming.

## Executable Artifact

Executable:

```text
tools/osag_preaction_family_noncompletion.py
```

Focused test:

```text
tests/test_osag_preaction_family_noncompletion.py
```

Result JSON:

```text
tests/artifacts/osag_preaction_family_noncompletion_result.json
```

## OSAG Tuple

This run uses the tuple named by the trigger plan:

```text
OSAG = (
  Gamma_n,
  Adm_n,
  Cand_n,
  Gen_n,
  a_n,
  w_n,
  Gamma_{n+1},
  DeltaCap_n,
  tau_n,
  Preserve_n,
  AAN_family
)
```

The bounded positive case is deliberately finite. It represents a stage-local
index of completion families and checks before action that no represented
family already covers the candidate. The generator is present-rule driven, not
an external table. This is a formal/local OSAG shape, not a physical candidate.

## Computed Result

```yaml
fixture_id: osag_preaction_family_noncompletion
kind: h2_bounded_formal_local_osag_constructor
h2_result: bounded_osag_shape_constructed_formal_local
bounded_osag_constructed: true
preaction_family_noncompletion_rule_generated_internal: true
fixed_completion_absorbed: true
after_fact_singleton_rejected: true
imported_oracle_rejected: true
adapter_preservation_checked: true
claim_status_change: none
physical_source_issuance_established: false
TI_C020_reopened: false
```

## Interpretation

H2 constructs a bounded formal/local OSAG shape.

That is useful because it keeps H1 from ending in a purely verbal target. The
noncompletion rule can be stated as a pre-action admission condition over a
represented family index, and it can reject three failure modes:

- fixed completion families that already cover the candidate;
- after-fact singleton naming;
- imported hidden completion oracles.

The result is still not a physical source action. It only shows how the escape
shape can be represented without immediately collapsing into the known H1
absorbers.

## Honest Boundary

Computed, high confidence:

- the OSAG tuple can be mapped in a finite formal/local fixture;
- fixed value, preformed action, and capability schedule completion remain
  terminal absorbers;
- after-fact singleton naming is rejected;
- imported oracle completion is rejected;
- no claim status changes and `TI-C020` remains parked.

Argued, medium confidence:

- H2 is complete enough to route the next Track 1 step to an admission contract;
- H7 should preserve the H1/H2 completion-family checks when accepting boundary
  or neighbor data;
- H9 and H5 are now calibration/support lanes, not the main objective.

## Next Route

```text
Wave 3: H7 completion-aware Adapter_P admission contract.
```

Minimum contract for H7:

1. Treat H1 completion channels and H2 OSAG family checks as preservation
   fields, not prose context.
2. Define admission for boundary, neighbor, or cross-repo candidate data without
   importing a hidden completion oracle.
3. Preserve `tau_n`, `Preserve_n`, represented family index, and candidate
   provenance.
4. Return a computed artifact that exits 0 and distinguishes admitted
   formal/local OSAG support from imported completion or readout language.
5. Preserve no claim movement unless a later durable artifact earns it.
