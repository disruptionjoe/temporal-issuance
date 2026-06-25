---
artifact_type: exploration
exploration_id: E080
status: active
created: 2026-06-25
claim_refs:
  - TI-C019
  - TI-C020
  - TI-C022
depends_on:
  - E067-source-shadow-finality-interface-contract-2026-06-24.md
  - E071-issued-capability-contract-test-2026-06-24.md
  - E072-typed-effect-signature-source-shadow-finality-2026-06-24.md
context_repos:
  - ../../gu-formalization
  - ../../time-as-finality
verdict: no_claim_movement
---

# E080: GU Effect-Typed Witness Transport

## Purpose

Preserve the Temporal Issuance side of the GU / Time as Finality bridge.

The GU hourly run isolated five concrete blockers. The bridge question is
whether the Temporal Issuance source/shadow/finality contract can classify
those blockers without importing GU claims, merging ledgers, or treating
projection/finality/loss as source issuance.

## Contract Reuse

Reuse the E067 interface:

```text
SSF =
(
  SourceExtension,
  Projection,
  Capability,
  RecordFinality,
  LossKernel,
  AbsorberSet
)
```

Reuse the E072 effects:

```text
Issue[S]
Project[O]
Finalize[R]
Lose[K]
```

New GU-facing wrapper:

```text
EffectTypedWitnessTransport =
(
  GU_blocker,
  SSF_fields,
  effect_tags,
  GU_native_geometry_obligation,
  absorber_or_fault_class,
  closure_condition,
  demotion_condition
)
```

## How This Helps GU

Temporal Issuance can help GU by forcing exact category separation:

| GU blocker | TI effect classification | warning prevented |
|---|---|---|
| `K_IG_selector` | `Issue[S]` candidate only if source gate passes | Do not choose a selector just because it yields nonzero theta. |
| `d_RS,-1` | `Lose[K]` plus source-side quotient data | Do not cite raw rank as physical quotient rank. |
| `ActualDGU01OperatorCertificate` | `Finalize[R]` for an actual operator certificate | Do not use a typed surrogate as the real GU operator. |
| `SourceProjectorPFinBWithLocalModeRecords` | `Project[O] + Lose[K] + Finalize[R]` | Do not treat finite readout as source-mode derivation. |
| `LoopStateTransitionLedger_v1` | `Finalize[R]` for automation state transitions | Do not confuse repeated blocker rediscovery with convergence. |

## How GU Helps Temporal Issuance

GU gives Temporal Issuance a hard testbed for the E067/E072 contract:

| TI object | GU stress test | useful pressure |
|---|---|---|
| `SourceExtension` | source-forced IG selector and field-degree rule | Tests whether `Issue[S]` can be distinguished from target-saving choice. |
| `Projection` | `Phi_obs`, finite projector `P_fin^b`, and source-mode records | Tests projection sufficiency under real geometry and operator data. |
| `Capability` | RS physical quotient and CHSH admissible measurement tasks | Forces task-natural capability instead of hidden-label recovery. |
| `RecordFinality` | actual operator certificates and claim-DAG finality | Separates certificate status from truth or source reality. |
| `LossKernel` | H-linear quotienting, finite-mode truncation, gauge loss | Tests whether lost structure changes downstream admissibility. |
| `AbsorberSet` | no-go class maps, target smuggling, stale canon, control states | Gives stronger absorber classes for future TI physical-source claims. |

## Guardrails

No Temporal Issuance claim moves because of this artifact.

Forbidden inferences:

```text
GU geometry is hard, therefore TI-C020 is supported.
GU has observer shadows, therefore TI source issuance is real.
Projection/finality/loss in GU implies Issue[S].
TaF/TI bridge vocabulary solves GU physics blockers.
```

Allowed result:

```text
The E067/E072 contract is useful if it classifies GU blockers more cleanly or
GU exposes missing fields in the contract.
```

## Next Fixture

Construct a five-row `EffectTypedWitnessTransport` table for GU and require
each row to fill:

```text
GU_blocker
effect_tags
SourceExtension gate
Projection sufficiency status
task-natural Capability
RecordFinality state
LossKernel
AbsorberSet
GU-native closure condition
```

Expected first verdict:

```text
bridge_discipline_useful
claim_status_change: none
```

## Links To Preserve

- GU crosswalk note:
  `../../gu-formalization/explorations/time-as-finality-crosswalk/effect-typed-witness-transport-bidirectional-crosswalk-2026-06-25.md`
- GU five-goal synthesis:
  `../../gu-formalization/explorations/hourly-cycle1-effect-typed-witness-transport-five-goal-synthesis-2026-06-25.md`
- Time as Finality stress-test note:
  `../../time-as-finality/explorations/gu-effect-typed-witness-transport-stress-test-2026-06-25.md`
- E067 contract:
  `E067-source-shadow-finality-interface-contract-2026-06-24.md`
- E072 typed effects:
  `E072-typed-effect-signature-source-shadow-finality-2026-06-24.md`
