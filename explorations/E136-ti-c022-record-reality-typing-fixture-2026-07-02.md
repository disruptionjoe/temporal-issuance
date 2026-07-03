---
artifact_type: exploration
status: complete
governance_role: fixture_result
exploration_id: E136
workflow: W000 -> ti_c022_record_reality_typing_fixture
claim_refs:
  - TI-C022
  - TI-C019
depends_on:
  - explorations/E058-ti-c022-shared-process-continuity-predicate-2026-06-24.md
  - explorations/E062-ti-c022-fork-choice-canonical-chain-ontology-absorber-2026-06-24.md
  - memory/path-kills.md#run-0057
created: 2026-07-02
central_run: RUN-20260702-082-progress-fanout-hourly
constitutional: false
claim_status_change: none
---

# E136: TI-C022 Record-Reality Typing Fixture

## Purpose

Execute the automation-safe route left by RUN-0120:

```text
W000 -> ti_c022_record_reality_typing_fixture
```

The fixture tests the RUN-0057 resurrection trigger:

```text
Find a protocol trace in which fork-choice / canonical-chain finality succeeds
but TI-C022 fails, or TI-C022 succeeds while canonical-chain finality fails,
without changing quorum, finality, or carrier-selection assumptions.
```

## Fixture

Executable fixture:

```text
tools/ti_c022_record_reality_typing_fixture.py
tests/test_ti_c022_record_reality_typing_fixture.py
tests/artifacts/ti_c022_record_reality_typing_fixture_result.json
```

The fixture compares two predicates on the same finite traces:

```text
TI-C022 record reality:
  quorum-certified target state
  + unique cofinal quorum-legitimate carrier
  + target belongs to that carrier

Canonical-chain finality:
  quorum validity
  + canonical-carrier selection
  + finality rule
  + finalized record membership
```

## Cases

```yaml
cases_checked:
  - unforked_progress
  - temporary_fork_canonicalized
  - permanent_fork_no_canonical_carrier
  - quorum_without_finality
```

Results:

```yaml
same_assumption_divergence_found: false
operational_absorption_reaffirmed: true
apparent_divergences_require_assumption_change: true
branch_local_integrity_distinguished_from_record_reality: true
canonical_membership_matches_ti_c022_when_matched_assumptions_hold: true
```

## Result

No matched-assumption divergence was found.

- In ordinary unforked progress, TI-C022 record reality and canonical-chain
  finality both accept the same records.
- In a temporary fork with canonicalization, both accept canonical-branch
  records and both reject orphaned branch-local records.
- In a permanent fork with two cofinal branches, both reject branch-local
  records because no unique shared carrier / canonical carrier exists.
- In a quorum-without-finality trace, both reject the record as shared-process
  real because quorum integrity alone is not carrier membership.

The only apparent divergences come from changing the assumption set:

```yaml
invalid_moves:
  - treat_branch_local_integrity_as_canonical_finality
  - declare_orphaned_branch_record_ontologically_real_by_override
```

Both moves are invalid for this discriminator. The first substitutes
branch-local BFT/TCB integrity for canonical-carrier finality. The second drops
the TI-C022 membership requirement in the unique cofinal quorum-legitimate
carrier.

## Verdict

```yaml
TI_C022_independent_operational_surplus: false
remaining_surplus: ontological_record_reality_typing
resurrection_trigger_met: false
claim_status_change: none
path_kill_added: false
path_kill_reaffirmed: TI_C022_as_independent_operational_surplus_over_fork_choice_canonical_chain_finality
next_gate: W010_frontier_selection_after_ti_c022_record_reality_fixture
```

RUN-0057's path kill remains correct in this bounded executable class:
canonical-chain/finality machinery operationally realizes the TI-C022
predicate once quorum validity, carrier selection, finality, and finalized
record membership are supplied. TI-C022 still names an ontological
interpretation: canonical-carrier membership is what makes a record shared-
process real. The fixture does not produce an independent operational theorem
or claim-status movement.

## Claim Effects

```yaml
TI-C022:
  status: unchanged_speculative
  effect: operational_absorption_reaffirmed_by_executable_fixture
  strongest_objection: >
    Fork-choice / canonical-chain finality operationally implements the
    predicate when matched assumptions are supplied.
  remaining_surplus: ontological_record_reality_typing

TI-C019:
  status: unchanged_formalizing
  effect: >
    The shared-participation record-reality interpretation remains available,
    but this fixture adds no new source-side issuance result.
```

## Next Trigger Recommendation

Absent Joe authorization for the higher-value formal integration gate, route
back to frontier selection with this TI-C022 branch closed at the current
operational tier:

```text
W000 -> W010_frontier_selection_after_ti_c022_record_reality_fixture
```

The W010 pass should preserve the standing Joe gate:

```text
bounded FORMAL-OBJECT / CLAIM-LEDGER integration without status promotion
```

It should also avoid reopening TI-C022 unless a new trace supplies the exact
RUN-0057 resurrection trigger.
