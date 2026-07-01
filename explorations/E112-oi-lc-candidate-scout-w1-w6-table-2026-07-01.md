---
artifact_type: exploration
status: active
governance_role: candidate_scout_result
goal_ref: oi_lc_candidate_scout_w1_w6_table
claim_refs:
  - TI-C001
  - TI-C003
  - TI-C019
  - TI-C020
depends_on:
  - explorations/E057-ti-c020-fixed-h-vs-h-growing-six-axis-fixture-2026-06-24.md
  - explorations/E064-assembly-theory-d4-source-projection-operationalization-2026-06-24.md
  - explorations/E094-dual-record-fixture-effect-gate-2026-06-25.md
  - explorations/E108-online-issuance-witness-machine-check-2026-07-01.md
  - explorations/E110-online-issuance-lc-physical-adapter-contract-2026-07-01.md
  - explorations/E111-adapter-p-missing-piece-63-persona-pass-2026-07-01.md
  - tools/oi_lc_candidate_scout_w1_w6_table.py
  - tests/test_oi_lc_candidate_scout_w1_w6_table.py
created: 2026-07-01
constitutional: false
---

# E112: OI LC Candidate Scout W1-W6 Table

## Purpose

Execute the next big-swing route:

```text
W000 -> oi_lc_candidate_scout_w1_w6_table
```

Question:

```text
Which candidate family, if any, can state a concrete Adapter_P W1-W6 witness obligation
worth an executable absorber fixture?
```

This is a scout, not evidence. A `fixture_candidate` verdict means "test this next," not
"TI-C020 is reopened."

## Adapter_P Scoring Fields

Each candidate was scored against:

```text
Gamma_n
Adm_n
e_n
w_n
Gamma_{n+1}
tau_n
```

and the W1-W6 gate:

```text
W1 invariant / non-isomorphic algebra
W2 admissibility predicate
W3 construction provenance
W4 perturbation non-factorization
W5 record preservation
W6 gauge/access/language absorption
```

plus fixed-source nulls:

```text
fixed_H_infty
fixed_A_infty
fixed_instrument_family
fixed_stochastic_or_collapse_law
fixed_boundary_or_holographic_completion
bounded_access_to_Mu_infty
experimenter_added_schema
```

## Result

Executable artifact:

```text
tests/artifacts/oi_lc_candidate_scout_w1_w6_table_result.json
```

Summary:

```yaml
candidate_count: 7
fixture_candidate_count: 1
parked_count: 2
killed_shortcut_count: 4
selected_fixture_candidate: assembly_theory_source_assembly_index
selected_fixture_candidate_is_evidence: false
Issue[S]^physical: false
TI_C020_reopened: false
next_gate: oi_lc_assembly_source_adapter_fixture
```

## Scout Table

| Candidate family | Adapter_P outcome | Main absorber pressure | Stop-rule verdict |
| --- | --- | --- | --- |
| Quantum measurement / contextuality | Names records and contexts, but no source-generated `e_n` or `w_n` | fixed `H_infty`, fixed `A_infty`, fixed instrument family, AB/contextuality fixed-cover language | `killed_shortcut` |
| Causal-set / sequential growth | Has real growth vocabulary, but witness is usually a fixed birth law | fixed stochastic law, label/gauge absorption, missing record-preservation protocol | `parked` |
| Holographic / boundary encodings | Maps too naturally to fixed richer boundary/source | fixed boundary or holographic completion | `killed_shortcut` |
| GU missing-piece adapter language | Promising geometry/interface language, but no exact typed `Adm_n`, `e_n`, or `w_n` | bounded-access and language/gauge relabeling remain open | `parked` |
| Assembly Theory source assembly index | Can state an executable W2/W3 obligation: `AI_src,n` undefined -> `AI_src,n+1` defined | bounded-access and experimenter-added-schema nulls undefeated | `fixture_candidate` |
| Quantum-biological / Orch-OR substrate | Supplies a substrate story, not an Adapter_P source-growth witness | fixed-H, fixed collapse/stochastic law, substrate-parameter absorption | `killed_shortcut` |
| Dual-record adjacent-possible graphs, current form | States changing opportunity edges, but current form is absorbed by fixed latent graph plus changing access | bounded access to `Mu_infty`, experimenter-added schema | `killed_shortcut` |

## What Was Learned

The strongest next candidate is Assembly Theory source assembly index, but only in a narrow sense:
it can state a testable source-growth obligation. It has not passed W1-W6.

The obligation is:

```text
Show a source assembly index where AI_src,n is undefined and AI_src,n+1 is defined,
while defeating fixed-source precontainment, bounded access to Mu_infty, and
experimenter-added schema.
```

That is more executable than the other surveyed routes because it can name the witness shape:

```text
Gamma_n          source construction universe at prefix n
Adm_n            predicate for source assembly class formation
e_n              candidate new construction class/object
w_n              trace that AI_src,n was undefined and AI_src,n+1 became defined
Gamma_{n+1}      source context after admission
tau_n            assembly/provenance trace
```

## What Collapsed

Four shortcuts should not be used as TI-C020 evidence:

```text
quantum contextuality alone
fixed holographic/boundary completion
quantum-biological / Orch-OR substrate claims alone
current-form dual-record adjacent-possible opportunity graphs
```

They may remain useful vocabulary or substrate hypotheses, but they do not supply an
Adapter_P source-growth witness.

## What Stayed Parked

Two routes remain interesting but under-typed:

```text
causal-set / sequential-growth models
GU missing-piece adapter language
```

They need exact typed adapter inventories or non-precontained admissibility witnesses before
they deserve the next executable fixture.

## Claim Movement

None.

```yaml
Issue[S]^LC: true
Issue[S]^physical: false
TI_C020_reopened: false
claim_status_change: none
```

## Next Run

```text
W000 -> oi_lc_assembly_source_adapter_fixture
```

The fixture should try to kill the selected candidate by comparing:

```text
assembly source-index undefined-to-defined
```

against:

```text
fixed complete assembly space
bounded access to pre-existing Mu_infty
experimenter/modeler-added schema
fixed stochastic or search process
```

Success for the next fixture would not automatically prove TI-C020. It would only create a
stronger candidate trace for the full `Adapter_P` absorber gate.
