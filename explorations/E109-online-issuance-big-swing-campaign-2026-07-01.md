---
artifact_type: exploration
status: active
governance_role: frontier_selection_campaign
workflow: W010_frontier_selection_after_online_issuance_machine_check
claim_refs:
  - TI-C001
  - TI-C003
  - TI-C019
  - TI-C020
depends_on:
  - explorations/E057-ti-c020-fixed-h-vs-h-growing-six-axis-fixture-2026-06-24.md
  - explorations/E091-online-issuance-verdict-and-formal-object-rewrite-2026-06-25.md
  - explorations/E108-online-issuance-witness-machine-check-2026-07-01.md
created: 2026-07-01
constitutional: false
---

# E109: OnlineIssuance Big-Swing Campaign

## Purpose

Run the W010 frontier-selection pass after RUN-0097 and turn the result into a large but
bounded campaign.

Current state:

```yaml
record_table_route: archived_as_interface_vocabulary
online_issuance_lc: strengthened_by_small_calculus
physical_source_issuance: not_established
external_platonist_absorber: still_available_outside_local_constructive_class
```

The big swing should not add more metaphor. It should attack the remaining gap:

```text
Can a physical or cross-repo candidate instantiate OnlineIssuance^LC under the strict W1-W6
source-witness gate, or must the repo keep the formal residue separate from physics?
```

## State Sync

```yaml
latest_run_seen: RUN-0097
memory_current: false
next_trigger_current: true
roadmap_current: true
surface_tensions:
  - tension_id: memory_summary_stale_after_RUN_0081
    surfaces:
      - memory/steward-memory-summary.md
      - agent-governance/NEXT-TRIGGER-PLAN.md
    description: >
      Memory summary still stops at RUN-0081, while trigger and roadmap include RUN-0097.
      Use RUN-0097/E108 as current truth for this campaign.
  - tension_id: official_next_trigger_vs_user_big_swing
    surfaces:
      - agent-governance/NEXT-TRIGGER-PLAN.md
      - Joe request
    description: >
      NEXT-TRIGGER-PLAN recommends W010 frontier selection. Joe asked to orchestrate a big
      swing, so this artifact executes the W010 routing pass and creates a campaign.
```

## Frontier Candidates

### F1 - OnlineIssuance LC To Physical Witness Gate

```yaml
frontier_id: F1
title: OnlineIssuance^LC to physical W1-W6 adapter gate
claim_refs:
  - TI-C019
  - TI-C020
layer: physical_bridge
candidate_workflow: W000 -> online_issuance_lc_physical_adapter_contract
why_live: >
  RUN-0097 strengthened the formal residue. The central unresolved question is whether any
  physical candidate instantiates it rather than merely projecting from fixed-H/fixed-source
  structure.
success_condition: >
  Define an adapter contract where a candidate supplies non-isomorphic algebra/admissibility or
  construction-space growth, no hidden oracle, record preservation, perturbation
  non-factorization, and absorber defeat.
failure_condition: >
  No candidate can even state the W1-W6 witness without importing fixed-H/fixed-A/fixed-boundary
  structure or experimenter-added schema.
main_absorbers_or_kill_risks:
  - fixed H_infty / fixed A_infty
  - fixed instrument or channel family
  - fixed stochastic/collapse law
  - fixed boundary or holographic completion
  - bounded access to richer source
expected_artifact: E110-online-issuance-lc-physical-adapter-contract
```

### F2 - Proof-Assistant Hardening

```yaml
frontier_id: F2
title: Upgrade the small-calculus witness to Lean/Coq/Agda or demote scope
claim_refs:
  - TI-C003
  - TI-C019
layer: source
candidate_workflow: W000 -> proof_assistant_online_issuance_witness
why_live: >
  RUN-0097 is executable but not a proof assistant result. A formal proof would harden the
  class-relative residue.
success_condition: >
  Encode contexts, present formation, diagonal candidate construction, witness formation, and
  internal future-oracle rejection in a proof assistant or a stricter typed calculus.
failure_condition: >
  The witness depends on informal rules that cannot be typed without smuggling in a future
  oracle or weakening diagonal productivity.
main_absorbers_or_kill_risks:
  - informal self-reference
  - hidden global universe
  - proof-engine plumbing without verdict movement
expected_artifact: E110-proof-assistant-online-issuance-witness
```

### F3 - Candidate Scout And Exclusion Table

```yaml
frontier_id: F3
title: Rank physical/cross-repo candidate families against W1-W6 before spending fixture work
claim_refs:
  - TI-C020
layer: physical_bridge
candidate_workflow: W000 -> oi_lc_candidate_scout_w1_w6_table
why_live: >
  The repo has many evocative candidates: quantum measurement/contextuality, causal-set growth,
  GU adapter language, assembly theory, holographic boundaries, and quantum-biological fixtures.
  Most are likely absorbed, but a ranked exclusion table prevents recency or aesthetics from
  picking the next fixture.
success_condition: >
  Identify one candidate with a concrete W1-W6 witness obligation, or explicitly keep TI-C020
  parked.
failure_condition: >
  All named candidates fail before fixture construction.
main_absorbers_or_kill_risks:
  - attractive vocabulary without witness
  - repeating already killed physical bridge routes
  - fixed-source aperture absorption
expected_artifact: E111-oi-lc-w1-w6-candidate-scout
```

### F4 - Source Trace To TaF Projection Contract

```yaml
frontier_id: F4
title: Contract from OnlineIssuance tau_n to Time-as-Finality reconstruction
claim_refs:
  - TI-C001
  - TI-C019
layer: projection
candidate_workflow: W000 -> source_trace_to_taf_projection_contract
why_live: >
  TaF owns temporal reconstruction and OnlineIssuance owns the source residue. A clean contract
  would prevent future duplication errors.
success_condition: >
  Define how tau_n projects into TaF traces while preserving Issue[S] vs Project[O]/Finalize[R]
  separation.
failure_condition: >
  The contract adds only explanatory vocabulary beyond E103/E107.
main_absorbers_or_kill_risks:
  - duplicated TaF
  - interface work without claim movement
expected_artifact: E112-source-trace-to-taf-contract
```

### F5 - Publishable Core Bundle

```yaml
frontier_id: F5
title: Package the formal result as theorem/no-go/checker bundle
claim_refs:
  - TI-C003
  - TI-C019
layer: export
candidate_workflow: W000 -> online_issuance_publishable_core_bundle
why_live: >
  The repo now has a coherent result: fixed-law and category absorbers succeed; local
  constructive productive witness survives; a small checker validates the witness schema.
success_condition: >
  Produce a publishable paper skeleton with definitions, no-go results, witness schema, limits,
  and absorber table.
failure_condition: >
  The bundle reveals a missing formal dependency that should be fixed before export.
main_absorbers_or_kill_risks:
  - overclaiming physical relevance
  - hiding class-relative scope
expected_artifact: E113-online-issuance-core-paper-skeleton
```

## Ranked Next Work

```yaml
ranked_next_work:
  - rank: 1
    frontier_id: F1
    score_label: highest
    reason: >
      It attacks the central unresolved fork: whether the strengthened formal source residue
      can ever touch physical reality under the strict witness gate.
    why_not_higher: n/a
    recommended_workflow: online_issuance_lc_physical_adapter_contract

  - rank: 2
    frontier_id: F2
    score_label: high
    reason: >
      It hardens the formal source residue and has high failure value, but it does not by itself
      address TI-C020.
    why_not_higher: >
      Proof hardening can become proof-engine plumbing if no physical or publishable route
      depends on the extra rigor.
    recommended_workflow: proof_assistant_online_issuance_witness

  - rank: 3
    frontier_id: F3
    score_label: high
    reason: >
      It prevents another attractive physical candidate from bypassing W1-W6 and can select the
      first actual fixture after the adapter contract.
    why_not_higher: >
      Candidate scouting should follow the adapter contract so every candidate is scored against
      the same gate.
    recommended_workflow: oi_lc_candidate_scout_w1_w6_table

  - rank: 4
    frontier_id: F5
    score_label: medium
    reason: >
      Export pressure would clarify the result, but the campaign should first decide whether a
      physical adapter contract is possible.
    why_not_higher: >
      Publishing too early risks freezing a class-relative result before its physical boundary is
      cleanly stated.
    recommended_workflow: online_issuance_publishable_core_bundle

  - rank: 5
    frontier_id: F4
    score_label: medium
    reason: >
      It is useful architecture, especially after the record-table duplication correction.
    why_not_higher: >
      It likely improves hygiene more than verdict movement.
    recommended_workflow: source_trace_to_taf_projection_contract
```

## Big-Swing Campaign

The campaign should run serially, with stop rules.

### Goal A - OnlineIssuance LC Physical Adapter Contract

Trigger:

```text
W000 -> online_issuance_lc_physical_adapter_contract
```

Purpose:

```text
Define exactly what it would mean for a physical process to instantiate OnlineIssuance^LC.
```

Required:

1. Define `Adapter_P` from a physical candidate trace into:
   `Gamma_n`, `Adm_n`, `e_n`, `w_n`, `Gamma_{n+1}`, and `tau_n`.
2. Import E057's W1-W6 gate:
   non-isomorphic algebra, new admissibility predicate, construction-space growth,
   perturbation non-factorization, record preservation, and gauge/name absorption.
3. Add the RUN-0097 limits:
   small-calculus LC support does not imply physical source issuance.
4. State rejection conditions for fixed-H, fixed-A, fixed-instrument, fixed-boundary,
   fixed-Mu, holographic, and bounded-access absorbers.

Success:

```text
A physical adapter contract exists with crisp pass/fail conditions and no implicit claim
promotion.
```

Failure:

```text
No non-circular adapter contract can be stated; TI-C020 stays parked and the next move is the
publishable formal-core bundle.
```

### Goal B - W1-W6 Candidate Scout

Trigger:

```text
W000 -> oi_lc_candidate_scout_w1_w6_table
```

Run only after Goal A.

Purpose:

```text
Rank candidate families against the adapter contract before building another physical fixture.
```

Candidate families:

```text
quantum measurement / contextuality
causal-set or sequential-growth models
holographic/boundary encodings
GU missing-piece adapter language
assembly-theory source assembly index
quantum-biological / Orch-OR substrate
dual-record adjacent-possible opportunity graphs
```

Success:

```text
One candidate supplies at least a plausible W1-W6 witness obligation worth an executable fixture.
```

Failure:

```text
All named candidates fail the preflight; TI-C020 remains parked and the formal result becomes
the export target.
```

### Goal C - Best-Candidate Absorber Fixture

Trigger:

```text
W000 -> oi_lc_best_candidate_absorber_fixture
```

Run only if Goal B selects a candidate.

Purpose:

```text
Build an executable fixture comparing the best candidate against fixed-source absorbers.
```

Success:

```text
The candidate defeats every fixed-source absorber while preserving records and W1-W6.
```

Failure:

```text
The candidate is absorbed; record a path kill and return to formal-core publication or proof
assistant hardening.
```

### Goal D - Proof-Assistant Hardening

Trigger:

```text
W000 -> proof_assistant_online_issuance_witness
```

Run in either of two cases:

```text
1. Goal A succeeds and a stricter formal backbone is needed for adapter work.
2. Goal B fails and the formal residue becomes the main publishable result.
```

Success:

```text
The RUN-0097 checker is upgraded to Lean/Coq/Agda or a stricter typed calculus.
```

Failure:

```text
The small-calculus result is demoted to executable pseudocode; the publishable claim must be
stated as a conjectural schema or informal theorem.
```

### Goal E - Publishable Core / Verdict Bundle

Trigger:

```text
W000 -> online_issuance_core_verdict_bundle
```

Purpose:

```text
Package the current formal result and the physical-bridge limits into a paper-grade artifact.
```

Required:

1. Definitions: `OnlineIssuance^LC`, effect typing, no-hidden-oracle discipline.
2. No-go table: finite, computable, category, fixed latent, external completion, record-table.
3. Positive schema: local constructive diagonal witness.
4. Machine-check appendix: RUN-0097 small calculus.
5. Physical boundary: W1-W6 or explicit TI-C020 parking.

## Primary Next Trigger

```yaml
primary_next_trigger:
  workflow_or_run: W000 -> online_issuance_lc_physical_adapter_contract
  reason: >
    This is the largest bounded move after RUN-0097 because it tests whether the formal residue
    can be connected to a physical witness without violating the repo's absorber discipline.
  claim_refs:
    - TI-C019
    - TI-C020
  success_condition: >
    A non-circular `Adapter_P` contract exists with W1-W6 pass/fail conditions and explicit
    fixed-source absorber nulls.
  failure_condition: >
    No adapter can be stated without importing fixed physical structure or experimenter-added
    schema; TI-C020 stays parked and the formal-core bundle becomes primary.
  expected_artifact: explorations/E110-online-issuance-lc-physical-adapter-contract-2026-07-01.md
```

Secondary triggers:

```yaml
secondary_triggers:
  - workflow_or_run: W000 -> proof_assistant_online_issuance_witness
    reason: Harden the formal residue if the physical adapter route needs stronger proof.
  - workflow_or_run: W000 -> oi_lc_candidate_scout_w1_w6_table
    reason: Rank candidate families after the adapter contract exists.
  - workflow_or_run: W000 -> online_issuance_core_verdict_bundle
    reason: Package the formal result if the physical adapter route fails at preflight.
```

## Claim Effects

No claim movement.

```yaml
TI-C001:
  movement: none
  note: >
    TaF remains the temporal reconstruction owner.

TI-C003:
  movement: none
  note: >
    The formal object remains OnlineIssuance^LC with small-calculus support.

TI-C019:
  movement: none
  note: >
    The class-relative formal residue remains live; no metaphysical promotion.

TI-C020:
  movement: none
  note: >
    The campaign is designed to test whether TI-C020 can be reopened under W1-W6, not to reopen
    it prematurely.
```
