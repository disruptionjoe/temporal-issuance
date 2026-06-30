---
artifact_type: exploration
status: active
governance_role: fixture_comparator_freeze
goal_ref: multi_observer_clock_free_record_cadence_fixture
claim_refs:
  - TI-C001
  - TI-C003
  - TI-C019
  - TI-C020
depends_on:
  - explorations/E095-coherent-issuance-not-clock-2026-06-30.md
  - explorations/E058-ti-c022-shared-process-continuity-predicate-2026-06-24.md
  - explorations/E072-typed-effect-signature-source-shadow-finality-2026-06-24.md
constitutional: false
created: 2026-06-30
---

# E096: Clock-Free Record-Cadence Fixture

## Purpose

Freeze the first finite fixture for E095 before implementation.

The target intuition is:

```text
Observer-local record streams may cohere because they are projections of one
shared issuance constraint, not because all observers share one universal clock.
```

The fixture must make that claim vulnerable. It compares three explanations:

```text
A. independent local records plus later reconciliation
B. hidden global tick / preferred foliation
C. clock-free shared issuance constraint with local projections
```

The fixture only advances E095 if C shows something A does not while avoiding
collapse into B.

## Non-Goals

This fixture does not prove source-side issuance, quantum mechanics, relativity,
or physical time.

It is a discriminator scaffold for the exact ambiguity in E095:

```text
Does "all observers do it in sync" mean a hidden clock,
or can it mean coherent admissibility without coordinate simultaneity?
```

## Fixture Objects

Use three observers:

```text
O_A, O_B, O_C
```

Each observer has only a local record stream:

```text
Rec_A = A-local append-only records, ordered by <_A
Rec_B = B-local append-only records, ordered by <_B
Rec_C = C-local append-only records, ordered by <_C
```

There is no shared numeric time coordinate in C. Local cadence is:

```text
kappa_i = the observer-local append relation <_i plus gaps between local records
```

The shared object is not a clock. It is a finite admissibility constraint:

```text
C_shared = parity-consistent triangle records
```

For a record handle `h`, the three pairwise edge bits are:

```text
x_AB(h)
x_BC(h)
x_CA(h)
```

Admissibility condition:

```text
x_AB(h) xor x_BC(h) xor x_CA(h) = 0
```

Observers see only local projections:

```text
O_A sees x_AB(h), x_CA(h)
O_B sees x_AB(h), x_BC(h)
O_C sees x_BC(h), x_CA(h)
```

The handle `h` is a record-family identifier, not a clock tick. The fixture
should allow records for different handles to interleave differently across
observers.

## Frozen Stress Trace

Use one hostile handle first:

```text
h0
```

Local proposals arrive in this observer-local order:

```text
p1: O_A proposes x_AB(h0) = 1
p2: O_C proposes x_CA(h0) = 0
p3: O_B proposes x_BC(h0) = 0
p4: O_B proposes x_BC(h0) = 1
```

Given p1 and p2, the admissible value is:

```text
x_BC(h0) = 1
```

Therefore p3 is the hostile proposal. It is locally recordable but globally
incompatible with the already admitted projections if the parity constraint is
load-bearing.

Add a second handle to test non-simultaneous interleaving:

```text
h1
```

Interleave h1 before h0 is fully settled:

```text
p5: O_C proposes x_CA(h1) = 1
p6: O_A proposes x_AB(h1) = 0
p7: O_B proposes x_BC(h1) = 1
```

For h1, p5, p6, and p7 are already parity-consistent:

```text
0 xor 1 xor 1 = 0
```

This prevents the hidden move where the fixture quietly treats each handle as a
global round that must complete before the next handle begins.

## Compared Systems

### A. Independent Local Records Plus Later Reconciliation

```text
record rule: each observer appends any locally well-formed proposal
shared constraint check: only after local finalization
repair rule: incompatible records are edited, orphaned, or marked as local-only
clock: none required
```

Expected role:

```text
negative control for after-the-fact gluing.
```

A can discover the parity obstruction only after it has admitted the hostile
record. If records are already final, A must either revise final records or
demote a branch to local-only.

Expected effect typing:

```text
Project[O] + Finalize[R] + Lose[K]
not Issue[S]
```

### B. Hidden Global Tick / Preferred Foliation

```text
record rule: a hidden total order T groups all observers by global round
shared constraint check: performed per round before local projection
repair rule: not needed if T chooses compatible triples
clock: yes, explicit hidden tick
```

Expected role:

```text
absorber for "sync" language.
```

B should reproduce coherent records easily. It is not an acceptable reading of
E095 because it buys coherence by adding a preferred foliation / global round
structure.

Expected effect typing:

```text
Project[O] + Finalize[R]
not Issue[S]
hidden_clock_absorber: true
```

### C. Clock-Free Shared Issuance Constraint

```text
record rule: a local proposal is admitted iff the current partial family still
             has at least one global completion satisfying C_shared
shared constraint check: prefix-admissibility over partial records
repair rule: incompatible proposals are rejected, deferred, or marked unissued
clock: none; only local append order plus compatibility
```

For h0:

```text
p1 admitted
p2 admitted
p3 rejected or deferred because no global completion remains
p4 admitted
```

For h1:

```text
p5, p6, p7 may interleave with h0 and still be admitted if each prefix remains
globally completable.
```

Expected role:

```text
candidate formalization of "coherent under a shared issuance constraint" without
coordinate simultaneity.
```

Expected effect typing before hostile review:

```text
Project[O] + Finalize[R]
Issue[S]: candidate only if fixed-source, causal-order, and sheaf/gluing
          absorbers fail
Lose[K]: only for rejected/deferred incompatible local proposals
```

## Measurements

The executable fixture should report:

```text
observer_count
record_handles
local_append_count_by_observer
global_ticks_used
hidden_total_order_used
admitted_records
rejected_records
deferred_records
revised_final_records
orphaned_local_records
parity_obstructions
global_completion_checks
max_unsettled_handle_width
coherence_without_revision
effect_verdict
absorber_verdict
```

## Verdict Rules

### C Beats A

C beats A only if:

```text
C preserves parity coherence without revising already-final records,
while A either revises, orphans, or demotes at least one finalized local record.
```

This is a reconstruction-layer win only. It does not imply source issuance.

### C Avoids B

C avoids B only if:

```text
global_ticks_used = 0
hidden_total_order_used = false
records for h0 and h1 can interleave without requiring round completion
the admission decision depends on compatibility/completability, not global slot number
```

If the implementation assigns hidden rounds, B absorbs C.

### C Survives As Source Candidate

C becomes a bounded `Issue[S]` candidate only if all are true:

```text
1. C beats A.
2. C avoids B.
3. The source-side gate from E072 passes.
4. The same behavior cannot be represented as ordinary sheaf gluing over a fixed site
   plus after-the-fact section selection.
5. The same behavior cannot be represented as fixed-H / fixed-A quantum record update
   or ordinary causal consistency.
```

Expected first verdict is more conservative:

```text
Project[O] + Finalize[R], with possible Lose[K],
not Issue[S] unless the absorbers are explicitly defeated.
```

## Absorber List

The result must be demoted if reproduced by:

```text
hidden global round / preferred foliation
ordinary causal partial order
ordinary sheaf compatibility on a fixed site
after-the-fact gluing / reconciliation
fork-choice or canonical-chain finality alone
fixed-H / fixed-observable-algebra quantum record maps
fixed latent source plus changing access aperture
database constraint checking over already-known schema
```

## Implementation Sketch

The executable version is intentionally small:

```text
tools/clock_free_record_cadence_fixture.py
tests/test_clock_free_record_cadence_fixture.py
tests/artifacts/clock_free_record_cadence_fixture_result.json
```

The implementation does not optimize or search. It replays the frozen stress trace
under A, B, and C, then emits the measurement table.

## Execution Result v0.1

Executed locally:

```text
python tests/test_clock_free_record_cadence_fixture.py
python tools/clock_free_record_cadence_fixture.py --output tests/artifacts/clock_free_record_cadence_fixture_result.json
```

Focused tests:

```text
5/5 passing
```

Result summary:

```yaml
A_independent_reconciliation:
  coherence_without_revision: false
  revised_final_records:
    - p3
  parity_obstructions: 1

B_hidden_global_tick:
  coherence_without_revision: true
  global_ticks_used: 2
  hidden_total_order_used: true
  absorber_verdict: hidden_clock_absorber

C_clock_free_constraint:
  coherence_without_revision: true
  global_ticks_used: 0
  hidden_total_order_used: false
  rejected_records:
    - p3
```

Comparison verdict:

```yaml
C_beats_A: true
C_avoids_B: true
B_reproduces_coherence_with_hidden_tick: true
```

Conservative effect verdict:

```yaml
Issue[S]: false
Project[O]: true
Finalize[R]: true
Lose[K]: true
claim_status_change: none
```

Interpretation:

```text
The fixture gives E095 a concrete positive scope: clock-free admissibility can
preserve cross-observer record coherence without revising finalized local records
and without using a hidden global tick.

It does not establish source-side issuance. The next gate is executed in
`E097-clock-free-cadence-absorber-gauntlet-2026-06-30.md`: C defeats causal-order-alone
but is absorbed by fixed-site sheaf compatibility, database constraint checking,
fixed-H record update, and fixed latent source plus changing access.
```

## Claim Effects

```yaml
TI-C001:
  movement: none
  note: >
    The fixture sharpens observer-side record cadence and reconstruction language.

TI-C003:
  movement: none
  note: >
    kappa_i remains observer-side unless C defeats the source gate and absorbers.

TI-C019:
  movement: none
  note: >
    The shared-process hypothesis gains a concrete discriminator surface, not a
    promoted claim.

TI-C020:
  movement: none
  note: >
    No physical bridge is established.
```

## Verdict

```yaml
comparator_frozen: true
fixture_executable: true
fixture_executed: true
fixture_home: temporal-issuance
expected_positive_scope: clock_free_coherence_vs_after_the_fact_reconciliation
expected_absorbers:
  - hidden_global_tick
  - fixed_site_sheaf_gluing
  - ordinary_causal_consistency
  - fixed_H_record_update
claim_status_change: none
next_trigger: source_side_resurrection_requires_nonfixed_admissibility_or_nonfixed_site
```
