---
artifact_type: exploration
status: active_starter_packet
governance_role: research_steering_wave_packet
workflow: user_directed_research_steering_wave
claim_movement: false
created: 2026-07-12
claim_refs:
  - TI-C012
  - TI-C018
  - TI-C019
  - TI-C020
depends_on:
  - attention/research-steering-card.md
  - attention/priority_condorcet.py
  - explorations/E163-full-adapter-p-diagonal-trace-pressure-2026-07-10.md
  - explorations/E152-adapter-p-no-go-preflight-2026-07-09.md
  - explorations/E110-online-issuance-lc-physical-adapter-contract-2026-07-01.md
---

# E164: Research Steering Wave 0 Starter

## Purpose

Joe asked to orchestrate a wave to get the current research-steering priorities started.

This is Wave 0: a dependency-bounded starter wave. It does not claim completion of any research lane. It starts each lane at the right dependency level without letting sidecars race ahead of H1.

## Computed Starter Plan

Executable artifact:

```text
tools/research_steering_wave0_starter.py
```

Focused test:

```text
tests/test_research_steering_wave0_starter.py
```

Result JSON:

```text
tests/artifacts/research_steering_wave0_starter_result.json
```

Computed verdict:

```yaml
wave_id: research_steering_wave0_starter
valid: true
blocking_lane: H1
dependent_starter_lanes:
  - H2
sidecar_lanes:
  - H3_H4
  - H5
  - H7
next_dependency_boundary: H2 construction and H3/H4 execution wait for H1 target-class result.
```

## H1 Blocking Lane

H1 is the whole-family completion barrier theorem.

Wave 0 starts H1 by naming the exact target class:

```text
record-preserving Adapter_P traces with:
  - all six Adapter_P fields mapped;
  - tau_n preserved;
  - finite-prefix non-precontainment stated;
  - completion/access/null models represented;
  - singleton after-naming represented;
  - whole-family completion represented.
```

The completion barrier must distinguish at least four completion notions:

1. Value completion: the future value is contained somewhere in a fixed space.
2. Name completion: the future value can be named after the fact.
3. Provenance/action completion: the action, witness, trace, and task delta are pre-formed before the action.
4. Capability completion: the task-menu delta is already determined by a fixed source plus access/readout/finality maps.

H1's first durable artifact should prove, refute, or executable-classify the following bounded claim:

```text
If a record-preserving Adapter_P trace is absorbed by value, name,
provenance/action, or capability completion under the same declared fields,
then it is not physical source issuance. A counterexample must supply an
internal rule that blocks the relevant completion before the action, not merely
after-fact singleton naming.
```

## H2 Dependent Starter

H2 is started as a dependent brief only. It should not build the source-action generator until H1 fixes the completion class.

Missing object:

```text
OperativeSourceActionGenerator =
(
  Gamma_n, Adm_n, Cand_n,
  Gen_n,
  a_n, w_n,
  Gamma_{n+1},
  Cap_n -> Cap_{n+1},
  DeltaCap_n,
  tau_n,
  Preserve_n,
  AAN_family
)
```

The object must internally produce an admissible source action, update the source context, change a native task/capability menu beyond TaF readout or fixed access, preserve `tau_n`, map into `Adapter_P`, and carry a family-level anti-after-naming rule.

Candidate `AAN_family` shapes:

- Productive admissible-family rule: for every H1-admissible precommitted disclosure family, the generator produces an admissible action or capability delta not family-disclosed by that family.
- Proof-carrying formation principle: completion must contain a pre-action certificate for the action, witness, task delta, and preserved trace, not merely a later value name.
- Endogenous admissibility update: the action changes the admissibility or construction grammar, with `Adm_{n+1}` not coded as a formed object of `Gamma_n`.

## H3/H4 Physical Calibration Sidecar

H3/H4 are started as fixture-contract preparation, not full physical execution.

CRISPR near-miss fixture:

```text
tools/crispr_adapter_p_near_miss_fixture.py
tests/test_crispr_adapter_p_near_miss_fixture.py
tests/artifacts/crispr_adapter_p_near_miss_fixture_result.json
```

It should map prior array, Cas machinery, exposure context, native acquisition rule, new spacer insertion, sequencing/integration witness, updated array, and genomic/readout trace into `Adapter_P`.

Expected honest verdict unless the fixture beats the hostile controls:

```text
NEAR_MISS_FIXED_SEQUENCE_SPACE_ABSORBED
```

Dynamic/Floquet negative-control fixture:

```text
tools/dynamic_floquet_code_negative_control_fixture.py
tests/test_dynamic_floquet_code_negative_control_fixture.py
tests/artifacts/dynamic_floquet_code_negative_control_fixture_result.json
```

It should map fixed hardware Hilbert space, instrument family, schedule prefix, measurement/gate rule, generated logical/effective code structure, syndrome/logical witness, successor platform state, and measurement trace into `Adapter_P`.

Expected honest verdict unless a real anomaly appears:

```text
NEGATIVE_CONTROL_FIXED_PLATFORM_SCHEDULE_ABSORBED
```

## H5 Multi-Holder Separator Sidecar

H5 is started as a finite fixture contract.

Exact confusion:

```text
Does multi-holder hardening indicate TI-side Ext_S source crossing,
or only TaF finality/readout over a fixed source with changed access,
redundancy, and holder permissions?
```

Minimal finite fixture:

```text
holders: {A, B, C}
values: {0, 1}
quorum: 2
cases:
  single_holder_bundle: three physical copies controlled by A
  multi_holder_split: three physical copies controlled separately by A, B, C
measures:
  CanReverse(O)
  CanFork(O)
  CanPostdict(O)
  mu_INFO
  mu_COMP
  mu_HOLDER
```

Controls:

- Match physical copy count and overwrite count for Landauer/thermodynamic controls.
- Classify pure holder-boundary reversal loss as `TAF_EXPRESSIBLE_READOUT`.
- Predeclare all states, quorums, holder maps, and operations in `S_inf` for fixed-source access absorption.

## H7 Preservation-Map Contract Sidecar

H7 is started as a checker-schema brief.

A boundary or neighbor-repo datum counts for TI only if it carries:

- `adapter_field_map`;
- `record_preservation_map`;
- `source_crossing_map`;
- `absorber_control_map`;
- `anti_import_map`;
- `anti_after_naming_map`;
- `neighbor_comparison_map`.

Minimum classifier outcomes:

```text
OUT_OF_SCOPE_NOT_ADAPTER_P_TRACE
FIXED_SOURCE_DISCLOSURE
TAF_EXPRESSIBLE_READOUT
IMPORTED_STRUCTURE_REJECTION
CLASS_RELATIVE_FORMAL_RESIDUE
WHOLE_FAMILY_COMPLETION_ABSORPTION
POTENTIAL_COUNTEREXAMPLE_REQUIRES_FULL_FIXTURE
```

## Computed vs Argued Claims

COMPUTED, high confidence:

- The Wave 0 starter dependency graph validates with H1 as the blocking lane.
- H2 is correctly marked dependent on H1.
- H3/H4, H5, and H7 are starter sidecars only and merge through this packet.

ARGUED, medium confidence:

- H1 is the right first full swing because it converts the repeated whole-family completion absorber into a theorem or classifier target.
- H3/H4 should not execute before H1 because otherwise they risk becoming another candidate-scout loop.
- H5 and H7 are worth starting now because their contracts sharpen the interface without requiring H1's final answer.

## Next Route

```text
Wave 1: H1 whole-family completion barrier theorem or executable classifier.
```

Do not run H2 construction or H3/H4 execution until H1 names the target class they must escape. H5 and H7 can proceed as bounded checker fixtures if they do not write shared routing surfaces and keep claim movement at none.
