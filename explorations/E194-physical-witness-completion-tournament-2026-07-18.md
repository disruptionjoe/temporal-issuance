---
artifact_type: exploration
status: complete
governance_role: physical_witness_class_tournament
workflow: repository-work-cycle
claim_movement: false
created: 2026-07-18
central_run: RUN-0177
claim_refs:
  - TI-C019
  - TI-C020
depends_on:
  - COMPLETION-CLASS.md
  - explorations/E178-completion-class-v1-audit-2026-07-14.md
  - explorations/E182-emergent-gauge-sector-candidate-v0-2026-07-16.md
  - explorations/E193-crack-branching-fracture-candidate-v0-2026-07-17.md
  - tools/physical_witness_completion_tournament.py
  - tests/test_physical_witness_completion_tournament.py
---

# E194: Physical Witness Completion Tournament

## Result first

The whole-family completion tournament is complete for the twelve material
physical witness campaign classes from RUN-0161 through RUN-0175.

Computed verdict:

```yaml
fixture_id: physical_witness_completion_tournament
candidate_count: 12
scoped_class_verdict: SCOPED_CLASS_LEVEL_ABSORPTION
all_candidates_absorbed_by_composed_panel: true
all_v1_families_absorbed_somewhere: true
physical_source_issuance_established: false
TI_C020_reopened: false
claim_status_change: none
```

This is a scoped class-level absorption over tested classes, not a universal
physical no-go.

## Executable artifact

```text
tools/physical_witness_completion_tournament.py
tests/test_physical_witness_completion_tournament.py
tests/artifacts/physical_witness_completion_tournament_result.json
```

The fixture imports `CompletionClass v1`, declares the bounded composition
rules used for the tournament, and applies the composed panel to the physical
campaign classes:

| Candidate class | Completion verdict |
| --- | --- |
| emergent gauge sector | `PHYSICAL_PREDICTIVE_ABSORPTION` |
| measurement-induced phase transition | `PHYSICAL_PREDICTIVE_ABSORPTION` |
| crossed-product gravitational algebra | `PHYSICAL_PREDICTIVE_ABSORPTION` |
| CRISPR spacer acquisition | `PHYSICAL_PREDICTIVE_ABSORPTION` |
| dynamic/Floquet code | `PHYSICAL_PREDICTIVE_ABSORPTION` |
| prion conformation | `PHYSICAL_PREDICTIVE_ABSORPTION` |
| autocatalytic reaction network | `PHYSICAL_PREDICTIVE_ABSORPTION` |
| Schwinger pair production | `PHYSICAL_PREDICTIVE_ABSORPTION` |
| Bose-Einstein condensation | `PHYSICAL_PREDICTIVE_ABSORPTION` |
| r-process nucleosynthesis | `PHYSICAL_PREDICTIVE_ABSORPTION` |
| turbulent cascade | `PHYSICAL_PREDICTIVE_ABSORPTION` |
| crack branching fracture | `PHYSICAL_PREDICTIVE_ABSORPTION` |

Anti-collapse throughput is preserved as pre-campaign / incomplete-null-class
material and is not counted among the twelve physical-campaign classes.

## Declared composition closure

The tournament uses four bounded composition rules:

1. Product: independent completion witnesses may be combined when they
   preserve the same frozen records.
2. Sequential: a completion may combine pre-event source state, intervention
   schedule, and post-event access.
3. Quotient: representation and gauge quotients are applied after physical and
   operational witnesses.
4. Cap: whole-family and completed-history witnesses cap global novelty
   without upgrading to physical causation.

The cap rule is load-bearing. It preserves CompletionClass v1's distinction
between physical/predictive, operational/context, representational, and
global/ontological conclusions.

## Class-level finding

The tested family does not merely fail candidate-by-candidate. The failed
candidate classes share the same class boundary:

```text
Real physical novelty signal + fixed law/source/platform + fixed initial or
boundary data + stochastic seed or disorder + access/resource schedule +
representation/gauge/name/provenance quotient + whole-family/completed-history
cap = no physical source issuance relative to v1.
```

The result does not show that no physical source witness can exist. It shows
that the next candidate must be structurally different from the twelve tested
classes, not merely a new domain with emergent-looking behavior.

## Survivor criteria

Physical witness generation can resume only for a candidate that supplies all
of these before it asks for source-issuance credit:

```yaml
survivor_criteria:
  - source_owned_transition_law
  - internal_anti_after_naming_rule
  - w4_perturbation_nonfactorization
  - native_carrier_or_algebra_growth
  - matched_intervention_and_resource_budget
  - observable_difference_from_strongest_fixed_rival
```

The candidate must also preserve its physical records under the same comparison
contract used by CompletionClass v1.

## Nonclaims

- No claim status changes.
- No `TI-C020` reopen.
- No E177 mutation.
- No cross-repo verdict.
- No external action.
- No universal physical no-go beyond the tested campaign classes.

## Next route

```text
W000 -> TI-PHYSICAL-WITNESS-GENERATION
```

The route is now `READY_AFTER_TOURNAMENT`: generate or test a non-overlapping
physical candidate only if it is strong enough to meet the survivor criteria
above. A thirteenth domain example without new native source structure is no
longer material progress.
