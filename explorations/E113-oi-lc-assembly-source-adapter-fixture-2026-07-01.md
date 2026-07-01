---
artifact_type: exploration
status: active
governance_role: assembly_source_adapter_result
goal_ref: oi_lc_assembly_source_adapter_fixture
claim_refs:
  - TI-C001
  - TI-C003
  - TI-C019
  - TI-C020
depends_on:
  - explorations/E064-assembly-theory-d4-source-projection-operationalization-2026-06-24.md
  - explorations/E069-fixed-source-bounded-access-negative-control-2026-06-24.md
  - explorations/E070-source-shadow-finality-positive-fixture-2026-06-24.md
  - explorations/E112-oi-lc-candidate-scout-w1-w6-table-2026-07-01.md
  - tools/oi_lc_assembly_source_adapter_fixture.py
  - tests/test_oi_lc_assembly_source_adapter_fixture.py
created: 2026-07-01
constitutional: false
---

# E113: OI LC Assembly Source Adapter Fixture

## Purpose

Execute the next routed big swing:

```text
W000 -> oi_lc_assembly_source_adapter_fixture
```

Question:

```text
Can the Assembly Theory source assembly-index witness
AI_src,n undefined -> AI_src,n+1 defined
survive the immediate fixed-source, access, modeler-schema, and fixed-search absorbers?
```

This is still not a physical claim. It tests whether the E112 fixture candidate has a real
formal/local source trace.

## Executable Fixture

Executable artifact:

```text
tests/artifacts/oi_lc_assembly_source_adapter_fixture_result.json
```

The toy assembly calculus computes:

```text
AI(state, x) = minimal finite constructor cost for x from seeds and constructors.
undefined    = no finite construction path in that prefix.
```

The target object is:

```text
ABC
```

The local surviving trace is:

```text
Gamma_n:
  seeds: A, B, C
  constructor: join_ab(A, B) -> AB
  AI_src,n(ABC): undefined

Gamma_{n+1}:
  source-generated constructor: bind_c(AB, C) -> ABC
  AI_src,n+1(ABC): 2
```

Adapter_P mapping:

```text
Gamma_n          source assembly context before bind_c
Adm_n            target ABC not constructible at prefix n
e_n              source-generated constructor bind_c
w_n              computed witness AI_src,n(ABC)=undefined and AI_src,n+1(ABC)=2
Gamma_{n+1}      successor context containing bind_c
tau_n            constructor provenance record and assembly-index computation
```

## Controls

| Control | Expected absorber | Result |
| --- | --- | --- |
| Projection access negative | bounded access to `Mu_infty` | rejected as source evidence |
| Fixed complete assembly space negative | fixed richer source / completion | rejected as source evidence |
| Experimenter-added schema negative | modeler-added constructor | rejected as source evidence |
| Fixed search process negative | fixed stochastic/search process | rejected as source evidence |
| Local source-generated constructor | targeted absorbers fail | formal/local source candidate |

## Result

```yaml
trace_count: 5
all_negative_controls_rejected: true
local_source_candidate_source_d4: true
local_source_candidate_targeted_absorbers_defeated: true
local_source_candidate_passes_assembly_source_gate: true
local_source_candidate_adapter_contract_passed: false
Issue[S]^assembly_local: true
Issue[S]^physical: false
TI_C020_reopened: false
claim_status_change: none
next_gate: oi_lc_assembly_w4_w6_physical_protocol_fixture
```

## What Was Learned

The Assembly source-index witness is now more than a scout candidate. It survives as a
formal/local source trace when the no-hidden-oracle discipline is granted.

The useful residue is:

```text
source-generated constructor provenance can make a source assembly index move from
undefined to defined while projection disclosure, fixed completion, modeler schema, and
fixed search controls all fail as explanations.
```

## What Still Fails

The surviving trace does not pass full `Adapter_P`.

It supplies:

```yaml
W2_new_admissibility_predicate: true
W3_construction_space_growth: true
W5_record_preservation: true
W6_gauge_access_language_absorption: true_for_targeted_local_absorbers
```

It does not supply:

```yaml
W1_non_isomorphic_algebra: false
W4_perturbation_non_factorization: false
real_physical_candidate: false
```

So the right reading is:

```text
formal/local Assembly source witness: yes
physical source issuance evidence: no
```

## Claim Movement

None.

```yaml
Issue[S]^assembly_local: true
Issue[S]^physical: false
TI_C020_reopened: false
claim_status_change: none
```

## Next Run

```text
W000 -> oi_lc_assembly_w4_w6_physical_protocol_fixture
```

Required next:

1. propose a real physical or empirical assembly-domain trace;
2. define a W4 perturbation that cannot factor through fixed chemistry/search/modeler schema;
3. preserve records under the same trace;
4. check W1 or explain why Assembly can only ever be W2/W3 evidence;
5. keep TI-C020 parked unless a real candidate passes full `Adapter_P`.
