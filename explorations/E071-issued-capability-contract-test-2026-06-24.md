---
artifact_type: exploration
exploration_id: E071
status: active
created: 2026-06-24
run_ref: RUN-0066
goal_ref: G06_issued_capability_contract_test
claim_refs:
  - TI-C019
  - TI-C020
depends_on:
  - E067-source-shadow-finality-interface-contract-2026-06-24.md
  - E069-fixed-source-bounded-access-negative-control-2026-06-24.md
  - E070-source-shadow-finality-positive-fixture-2026-06-24.md
---

# E071: IssuedCapability Contract Test

## Purpose

Run G06 from the ten-goal sequence. This fixture tests whether capability
language can distinguish:

```text
access-driven capability change
```

from:

```text
source-linked issued capability
```

without turning hidden access control into fake issuance.

## Definition

An `IssuedCapability` candidate is:

```text
IssuedCapability =
(
  source_extension_ref,
  task_family T,
  horizon h,
  budget B,
  Cap_before,
  Cap_after,
  native_comparison R_K,
  source_gate_verdict,
  projection_sufficiency_status,
  absorber_status
)
```

It is a genuine issued-capability candidate only when all five gates pass:

```text
IC-1 Task-natural capability:
  Cap is not "recover the hidden issuance label."

IC-2 Source gate:
  SourceExtension verdict is source_issuance_candidate.

IC-3 Non-ambient authority:
  Capability was not already present in a fixed richer source or hidden
  supervisor.

IC-4 Projection status declared:
  The run says whether projection is sufficient, insufficient, or lossy for the
  declared capability.

IC-5 AbsorberSet carried:
  Fixed-source, access, finality, instrumentation, and hidden-grammar absorbers
  are explicitly checked.
```

## Baseline A: G03 Fixed-Source Access Capability

Source:

```text
fixed Mu_infty + expanding P_n aperture
```

Capability:

```text
T = certify/use object a
Cap_before = cannot certify/use a through P_n
Cap_after  = can certify/use a through P_{n+1}
```

Gate result:

```yaml
IC-1_task_natural: passes
IC-2_source_gate: fails
IC-3_non_ambient_authority: fails
IC-4_projection_status_declared: passes
IC-5_absorber_set_carried: passes
```

Verdict:

```text
access_granted_capability
not IssuedCapability
```

Reason: capability changed because access changed. The source already contained
`a`.

## Baseline B: G02 Formal Source Capability

Source:

```text
Compat_G^MLTT finite trace
Gamma_n -> Gamma_{n+1}
sigma_star admitted at Gamma_{n+1}
```

Capability:

```text
T = future admissibility checking and successor construction using sigma_star
Cap_before = cannot use sigma_star
Cap_after  = can use sigma_star in downstream admissibility checks
```

Gate result:

```yaml
IC-1_task_natural: passes
IC-2_source_gate: passes
IC-3_non_ambient_authority: passes_for_local_MLTT_source_class
IC-4_projection_status_declared: passes
IC-5_absorber_set_carried: passes
```

Verdict:

```text
IssuedCapability_candidate_formal
```

Reason: the capability change is tied to the source extension in the local MLTT
class. The Platonist completed-oracle alternative remains an alternate ontology,
not an internal source object for this fixture.

## Projection Sufficiency Status

For G03:

```text
projection status: access projection changed
capability follows access
```

For G02:

```text
projection status: observer projection records the admitted construction but
does not preserve the full source construction space
```

Therefore G02 also carries:

```text
lossy_projection_residue
```

This does not weaken the issued-capability candidate because the task only
requires downstream availability of `sigma_star`, not full proof-search
reconstruction.

## Absorber Results

| Candidate | Fixed-source absorber | Access absorber | Hidden authority absorber | Verdict |
| --- | --- | --- | --- | --- |
| G03 access case | succeeds | succeeds | succeeds as fixed `Mu_infty` | not issued |
| G02 formal case | fails internally for local MLTT class | fails as total explanation | not used | formal issued-capability candidate |

## Contract Result

Capability language is usable if the repo keeps the word "issued" gated by the
source verdict.

Bad usage:

```text
observer can now do X, therefore source issued capability X
```

Good usage:

```text
source gate passed, Cap is task-natural, absorbers failed, and projection
status is declared; therefore this is an issued-capability candidate in the
stated class
```

## Verdict

G06 succeeds.

```yaml
access_capability_case: not_issued
formal_source_capability_case: IssuedCapability_candidate_formal
claim_status_change: none
```

## Claim-Ledger Implication

No claim movement. This run clarifies bridge vocabulary and protects future
capability claims from access-control inflation.
