---
artifact_type: exploration
status: implemented_and_verified
governance_role: action_3_implemented_fixture
created: 2026-07-14
claim_movement: false
implementation_grade: executable_result_regenerated_and_focused_tests_passed_11_of_11
depends_on:
  - explorations/E176-w192-reciprocal-packet-intake-2026-07-14.md
  - explorations/E173-t2-bounded-completion-barrier-theorem-contract-2026-07-12.md
---

# E177: Three-World Issuance/Disclosure Discriminator

## Result first

The preregistered finite discriminator is implemented without changing the
frozen protocol:

```yaml
fixture_id: three_world_issuance_disclosure_discriminator
protocol_version: three_world_issuance_disclosure_discriminator_v1
protocol_digest: c098b51fcacd7c191319f573a0d0891eb28cdbbd6698c042a626aab131119042
world_a: FIXED_SOURCE_DISCLOSURE
world_b: DYNAMIC_SELECTION_WHOLE_FAMILY_COMPLETABLE
world_c: CANDIDATE_C_INCOMPLETE
world_c_positive_allowed: false
real_revision_trigger_found: false
physical_source_issuance_established: false
claim_status_change: none
TI_C020_reopened: false
taf_capability_evaluated: false
physically_forced_boundary_established: false
cross_repo_implication_allowed: false
```

The implementation imports the ordered 19-obligation list from the live T2
tool. Gate booleans are derived from evidence. World C includes desired positive
booleans as an adversarial input and ignores them; missing certificates keep the
verdict fail-closed.

## Frozen protocol

Protocol ID:

```text
three_world_issuance_disclosure_discriminator_v1
```

Hash canonical JSON containing ordered schema fields, perturbation IDs, T2
obligation IDs, verdict precedence, and the exact World A/B fixtures. Later
source adapters may populate the schema but may not change the protocol without
creating `v2`.

## Worlds

World A is fixed hidden/revealed source:

```text
U=Z/5Z, hidden table=(1,4,2), visible prefix=(1), e_n=4.
```

Expected class: `FIXED_SOURCE_DISCLOSURE`; every completion channel and
whole-family factorization fire; W1/W4/W5 fail.

World B is internal dynamics over a fixed completed family:

```text
U=Z/5Z, x_n=1, Gen_n(x)=(x^2+1) mod 5, e_n=2.
```

Expected class: `DYNAMIC_SELECTION_WHOLE_FAMILY_COMPLETABLE`. H7 may pass, but
the complete pre-action family absorbs the result and W1/W4/W5 fail.

World C is a source-extension candidate interface. It begins incomplete and
must report missing provenance, `Adapter_P`, noncompletion, W1, W4, W5, and
whole-family certificates. Desired booleans are never accepted as evidence.

## Immutable schema

Use frozen records for:

- all six `Adapter_P` fields;
- source action, `Cand_n`, `Gen_n`, `a_n`, `DeltaCap_n`, `Preserve_n`, family
  index, and candidate provenance;
- boundary/access/readout schedule;
- a closed completion-family index;
- perturbation evidence and record comparison;
- verified noncompletion certificates;
- H8 shortcut detection.

All gate values are derived from evidence.

## Frozen perturbations

Run exact deterministic enumeration:

1. identity;
2. every allowed initial state;
3. every declared generator parameter;
4. access delay, reorder, and suppression;
5. every declared output/coarse-graining channel;
6. name relabeling and every predeclared provenance path.

The last three are holdouts. W4 cannot pass unless every relevant fixed-source
absorber family is complete, no exact trace match exists, and a frozen
nonfactorization certificate verifies.

## Record preservation

Compare the exact ordered vector of pre/post-boundary records, provenance, and
all six perturbation traces. W5 passes only when pre-boundary records match,
the candidate predicts all records with zero error, a complete nonempty fixed
absorber family has strictly larger minimum error, holdouts were predicted
before readout, and `tau_n` plus `Preserve_n` verify.

Missing absorber completeness produces `W5_INCOMPLETE`, never true.

## Completion and whole-family tests

Each value, name, provenance/action, and capability channel returns
`ABSORBED`, `DEFEATED_VERIFIED`, or `UNRESOLVED`. Only a machine-verifiable
defeat counts.

Whole-family factorization compares the joint tuple

```text
(e_n, name, a_n, w_n, tau_n, DeltaCap_n, every perturbation trace)
```

against a closed family or verified symbolic decision procedure. Search failure
is not a nonfactorization certificate.

## Verdict lattice

Use this precedence:

```text
schema invalid / out of scope
terminal safety rejection
fixed-source disclosure
dynamic selection, whole-family completable
completion-absorbed near miss
candidate C incomplete
candidate survives bounded discriminator
```

Survival triggers review of the bounded contract only. It does not establish
physical issuance or move claims.

## Cross-repo capability firewall

The TI capability field and the Time as Finality object are not identical:

```yaml
delta_cap_ti: opaque_adapter_field
capability_C_R_taf: NOT_EVALUATED
identity_between_them: false
cross_repo_implication_allowed: false
```

Every world has explicit `source_minus`, `source_plus`, `region_minus`, and
`region_plus` interface slots. The optional TaF interface carries region and
observer IDs, access-complete shadow fields, causal domain, horizon, detector
cadence, fixed `M_R` and `M_ext`, task records, resource budgets, external
record holdings, boundary mode, and separate structural, access-complete, and
all-intervention equality certificates. Missing fields serialize as `ABSENT`
or `NOT_EVALUATED`.

World A must fail access-complete equality when hidden/revealed access is
recorded honestly. Worlds B and C do not receive a TaF capability verdict from
TI source structure.

Any task interface declares inputs, allowed operations, target transformation,
success predicate, before/after result, cost, and provenance. Work, memory,
control, transport, storage, external-resource, causal-path, and
boundary-forcing ledgers remain separate from TI completion fields.

Split the record outputs:

```yaml
W5_TI_record_preservation: derived
W5_TAF_same_shadow_capability: NOT_EVALUATED
ti_verdict: derived
taf_interface_verdict: NOT_EVALUATED
```

TaF readout/state, description, joint-record, finality-state, causal-domain,
transition-menu, resource, law-sector, and fixed-source absorbers are optional
interface statuses only. They never replace TI's four completion channels and
never inherit a TI pass.

## Required deterministic checks

The verifier must pin the protocol digest; classify A and B exactly; keep C
incomplete with a sorted missing-field list; reject desired booleans without
certificates; exercise all four completion channels and six perturbations;
prove A/B have zero-error fixed-source matches; import the ordered 19-obligation
contract rather than duplicate it; keep H8/imported/readout shortcuts terminal;
and produce byte-stable JSON.

Expected root result:

```yaml
world_a: FIXED_SOURCE_DISCLOSURE
world_b: DYNAMIC_SELECTION_WHOLE_FAMILY_COMPLETABLE
world_c: CANDIDATE_C_INCOMPLETE
real_revision_trigger_found: false
physical_source_issuance_established: false
claim_status_change: none
TI_C020_reopened: false
taf_capability_evaluated: false
physically_forced_boundary_established: false
cross_repo_implication_allowed: false
```

Implemented executable surfaces:

- `tools/three_world_issuance_disclosure_discriminator.py`
- `tests/test_three_world_issuance_disclosure_discriminator.py`
- `tests/artifacts/three_world_issuance_disclosure_discriminator_result.json`

## Implementation grade and boundary

Implemented, high confidence from construction:

- deterministic World A and B controls are encoded exactly as preregistered;
- World C has no positive path without verified evidence for the live T2
  obligations;
- value, name, provenance/action, capability, and whole-family completion are
  separate derived results;
- all six frozen perturbation IDs and the W5 record comparison are represented;
- TI `DeltaCap_n` and TaF `C(R)` remain nonidentical, with cross-repo implication
  disabled;
- the generated result artifact records no claim, physical-source, D-FORK, TaF,
  or physically forced boundary movement.

Independent verification completed:

- root regenerated the checked result artifact from the executable with
  `PYTHONDONTWRITEBYTECODE=1`;
- `python tests/test_three_world_issuance_disclosure_discriminator.py` passed
  all 11 focused tests on 2026-07-14;
- World A remained fixed disclosure, World B remained whole-family-completable
  dynamics, World C remained fail-closed incomplete, and no revision trigger,
  claim movement, physical-source result, or TaF capability verdict appeared.

This implementation is a bounded classifier over the frozen controls and
interfaces. It is not a universal no-go, a physical source theorem, a TaF
capability verdict, or evidence that a real World C packet exists.
