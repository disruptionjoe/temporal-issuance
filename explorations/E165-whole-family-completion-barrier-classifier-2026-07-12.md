---
artifact_type: exploration
status: complete
governance_role: research_steering_wave_result
workflow: research_steering_wave1
claim_movement: false
created: 2026-07-12
central_run: RUN-0146
claim_refs:
  - TI-C019
  - TI-C020
depends_on:
  - explorations/E110-online-issuance-lc-physical-adapter-contract-2026-07-01.md
  - explorations/E145-generated-uv-d-fork-resurrection-fixture-2026-07-05.md
  - explorations/E152-adapter-p-no-go-preflight-2026-07-09.md
  - explorations/E163-full-adapter-p-diagonal-trace-pressure-2026-07-10.md
  - explorations/E164-research-steering-wave0-starter-2026-07-12.md
  - tools/whole_family_completion_barrier_classifier.py
  - tests/test_whole_family_completion_barrier_classifier.py
---

# E165: Whole-Family Completion Barrier Classifier

## Purpose

Wave 1 attacked H1 from the research-steering card:

```text
H1 whole-family completion barrier theorem or executable classifier
```

The North Star objective was to force or falsify the whole-family completion
absorber for bounded record-preserving `Adapter_P` traces. The wave did not
attempt a universal physics no-go theorem. It built the executable classifier
that H1 needed before H2, H3/H4, H5, or H7 could proceed cleanly.

## Executable Artifact

Executable:

```text
tools/whole_family_completion_barrier_classifier.py
```

Focused test:

```text
tests/test_whole_family_completion_barrier_classifier.py
```

Result JSON:

```text
tests/artifacts/whole_family_completion_barrier_classifier_result.json
```

## Computed Result

```yaml
fixture_id: whole_family_completion_barrier_classifier
kind: h1_executable_classifier_not_universal_theorem
bounded_candidate_class: record-preserving Adapter_P traces with value, name, provenance/action, and capability completion channels represented
all_completion_channels_exercised: true
preaction_family_noncompletion_required_for_escape: true
h1_result: narrowed_to_executable_classifier_and_preaction_family_noncompletion_target
next_track_1_recommendation: H2 operative source-action generator with pre-action family noncompletion rule
claim_status_change: none
physical_source_issuance_established: false
TI_C020_reopened: false
```

The classifier exercises four completion absorbers:

| Channel | Verdict |
| --- | --- |
| value completion | `VALUE_COMPLETION_ABSORPTION` |
| name completion | `NAME_COMPLETION_ABSORPTION` |
| provenance/action completion | `PROVENANCE_ACTION_COMPLETION_ABSORPTION` |
| capability completion | `CAPABILITY_COMPLETION_ABSORPTION` |

It also preserves the existing controls:

| Control | Verdict |
| --- | --- |
| missing Adapter_P field | `OUT_OF_SCOPE_NOT_ADAPTER_P_TRACE` |
| TaF finality/readout only | `TAF_EXPRESSIBLE_READOUT` |
| hidden global table or imported law | `IMPORTED_STRUCTURE_REJECTION` |

The only non-absorbed shape is:

```text
preaction_family_noncompletion_shape
```

It is schematic, not physical evidence. It has finite-prefix novelty and a
source-growth witness, but it is admitted only because it includes an internal
pre-action rule excluding all represented completion families. It therefore
routes to H2: the operative source-action generator must construct that rule.

## H1 Conclusion

H1 is resolved as an executable classifier, not as a universal theorem.

The honest conclusion:

```text
Within the bounded Adapter_P trace class, value, name, provenance/action, and
capability completion each absorb the candidate unless a pre-action family
noncompletion rule is part of the source action.
```

This is enough to break the current local minimum. The repo no longer waits for
an untyped sharper theorem target. It now has a precise target: construct or
kill the pre-action family noncompletion rule.

## Inline Council Reflection

Personas were run inline as a single council pass, not one-agent-per-persona.

- Orthodox professor: the result should not be sold as a theorem about all physical novelty. It is a bounded operational classifier over `Adapter_P` traces. That is the right level.
- Heterodox-rigorous professor: the load-bearing unforced choice is now explicit: `preaction_family_noncompletion_rule`. If it is imported, global, or after-fact, the structure collapses.
- Commercial scientist: the cheap calibration fixtures are now well specified, but their finishability does not outrank H2. They are tests for the classifier, not the objective.
- Philosopher of science: the kill condition is sharper. If no internal source action can produce the pre-action family noncompletion rule without a hidden oracle, the claimed escape dies cleanly.
- Wild frontier scientist: the highest-upside object is no longer another finite trace. It is the rule generator that changes the admissible family before completion can name the result.
- Computability and proof-theory specialist: H1 separates local diagonal freshness from family-level noncompletion. The next proof burden is to show whether the family rule is internally productive or just a renamed oracle.
- Category, sheaf, and topos theorist: the admission map now needs to preserve completion-channel status, not only Adapter_P fields. H7 should be rewritten through the H1 channels.
- Quantum and operator-algebra foundations specialist: H3/H4 become calibration, not evidence. Floquet and effective-algebra examples should mainly test capability and provenance/action completion.
- Thermodynamics and information theorist: H5 should test whether holder costs are capability/readout completion, not source crossing. Cost alone is not a noncompletion rule.
- Cosmology and boundary-physics specialist: boundary supply counts only if it carries a TI-side pre-action noncompletion map. Otherwise it is imported structure or fixed boundary completion.
- Distributed systems and finality theorist: multi-holder finality is likely a capability-completion or TaF-readout case unless the holder transition changes the source family before the record.
- Evolution and open-endedness theorist: CRISPR and adjacent-possible examples become useful stress tests only after H2 states what it means to generate the family rule internally.

## Generated Candidate Set

The council drafted a new live set after H1:

| Item | Status |
| --- | --- |
| H2 Pre-action family noncompletion source-action generator | New Track 1. Builds the OSAG rule H1 identified as the only non-absorbed escape shape. |
| H7 Completion-aware Adapter_P admission contract | Live support. Turns H1 channels into preservation/admission maps for boundary and neighbor data. |
| H9 H1 physical calibration batch | New merged branch. Runs CRISPR near-miss and Dynamic/Floquet negative control through H1 plus Adapter_P. |
| H5 Multi-holder completion-channel separator | Live support. Tests reversal cost against H1 capability-completion and TaF-readout absorbers. |
| H6 Internal versus external completion boundary theorem | Live clarifier. Keeps pre-action noncompletion from turning into external completion language. |
| H8 D-FORK regime signature bundle | Parked live synthesis. Waits for H2/H7 before packaging. |

Dropped or resolved:

- H1 is resolved as a dependency by this classifier.
- H3 and H4 are merged into H9, a calibration batch.
- No claim is promoted and no physical-source assertion is made.

## Condorcet Re-Rank

After updating `attention/priority_condorcet.py`, the ranking is:

```text
1. H2 Pre-action family noncompletion source-action generator
2. H7 Completion-aware Adapter_P admission contract
3. H9 H1 physical calibration batch
4. H5 Multi-holder completion-channel separator
5. H6 Internal versus external completion boundary theorem
6. H8 D-FORK regime signature bundle
```

The important priority correction is that H9 is useful but subordinate. Its
finishability does not outrank H2.

## Computed vs Argued Claims

COMPUTED, high confidence:

- The H1 classifier runs and exits 0.
- All four completion absorption classes are exercised.
- The pre-action family noncompletion shape is the only non-absorbed H1 escape.
- No physical source issuance is established.
- `TI-C020` remains parked.

ARGUED, medium confidence:

- H1 is sufficiently resolved as an executable classifier for routing purposes.
- H2 is now the correct Track 1 because it constructs or kills the rule H1 requires.
- H9 should not outrank H2 despite being a cleaner near-term payoff.
- H7 should be updated soon because every future admission map now needs H1 completion-channel preservation.

## Next Route

```text
Wave 2: H2 pre-action family noncompletion source-action generator.
```

Minimum contract for Wave 2:

1. Define `OSAG = (Gamma_n, Adm_n, Cand_n, Gen_n, a_n, w_n, Gamma_{n+1}, DeltaCap_n, tau_n, Preserve_n, AAN_family)`.
2. Make `AAN_family` a pre-action rule, not after-fact singleton naming.
3. Show whether the rule is internally generated or imported.
4. Preserve `tau_n` and map all six `Adapter_P` fields.
5. Return a computed artifact that exits 0 and either constructs a bounded OSAG shape or kills it.
