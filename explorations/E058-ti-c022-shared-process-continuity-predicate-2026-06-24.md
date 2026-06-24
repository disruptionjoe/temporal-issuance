---
artifact_type: exploration
status: active
exploration_id: E058
date: 2026-06-24
workflow: W000 -> shared_process_continuity_predicate_formalization
claim_refs:
  - TI-C022
  - TI-C019
depends_on:
  - E044 (TI-C022 BFT/TCB discriminator)
  - RUN-0048 (monotone-obstruction, SBP-IND, TI-C021/TI-C022 discriminators)
  - RUN-0052 (next-trigger route)
verdict: CONTINUITY_PREDICATE_FORMALIZED_NOT_EVENTUAL_SYNCHRONY
claim_status_change: none
path_kill: shared_process_continuity_as_mere_eventual_synchrony_liveness
---

# E058: TI-C022 Shared-Process Continuity Predicate

## Purpose

Run the primary trigger after RUN-0052:

```text
W000 -> shared_process_continuity_predicate_formalization
```

E044 defeated the BFT/TCB absorber with the Permanent-Fork Discriminator, but left one honest
residual pressure:

```text
Is "continuing shared process" just eventual-synchrony liveness restated?
```

This note states the predicate in order-theoretic, clock-free terms and tests that reduction.

## Object

Let a shared OnlineSchemaSys trace be represented by:

```text
T = (L, <=, #, QC, rec)
```

where:

- `L` is the set of quorum-legitimate schema states actually reached in the trace;
- `s <= t` means `t` extends `s` by admissible schema extension;
- `s # t` means `s` and `t` are incompatible states with no common admissible successor;
- `QC(s)` records the quorum certificate or legitimacy witness for `s`;
- `rec(e)` is the record produced by an event or extension `e: s -> t`.

This is a poset/compatibility object. It does not require a global clock.

## Continuity Carriers

A subset `F subset L` is a continuity carrier iff:

```text
1. prefix_closed:
   if t in F and s <= t, then s in F.

2. directed:
   for all s,t in F, there exists u in F such that s <= u and t <= u.

3. quorum_legitimate:
   every s in F has QC(s).

4. cofinal_as_a_branch:
   F is a maximal unbounded directed branch of L.
```

In ordinary words, a continuity carrier is a branch of quorum-legitimate schema states that
keeps extending without being absorbed into a larger incompatible branch.

Let:

```text
Cof(T) = the set of cofinal continuity carriers in T.
```

## The TI-C022 Predicate

For an event `e: s -> t`, define:

```text
SharedContinuous_T(e) iff
  (a) rec(e) has a quorum certificate QC(t), and
  (b) Cof(T) = {F*} is a singleton, and
  (c) t in F*.
```

Equivalently:

```text
An event is genuine shared-process issuance iff its record is quorum-legitimate
and its target state belongs to the unique cofinal quorum-legitimate branch of
the shared schema-state poset.
```

This is the formal version of E044's condition (b). It says the record must be carried by the
one continuing shared process, not merely finalized on a local branch.

## Canonical Cases

### Case 1: Normal Unforked Progress

```text
L = s0 <= s1 <= s2 <= ...
Cof(T) = {L}
```

Every quorum-certified event on the chain satisfies `SharedContinuous_T`.

Verdict:

```yaml
record_integrity: true
shared_process_continuity: true
```

### Case 2: Temporary Fork With Later Canonicalization

```text
         a1 <= a2 <= a3 <= ...
        /
s0 <= f
        \
         b1 <= b2   (bounded/orphaned)
```

If the `a` branch is the only cofinal branch:

```text
Cof(T) = {A}
```

then events on `A` can be genuine, while records on the orphaned `B` branch are local records,
even if they were locally well-formed.

Verdict:

```yaml
canonical_branch_records: genuine
orphan_branch_records: local_not_genuine_shared_issuance
```

### Case 3: Permanent Fork

```text
         a1 <= a2 <= a3 <= ...
        /
s0 <= f
        \
         b1 <= b2 <= b3 <= ...
```

If both `A` and `B` are cofinal and incompatible:

```text
Cof(T) = {A, B}
```

then singleton uniqueness fails. Neither branch record satisfies the global predicate.

Verdict:

```yaml
branch_A_record_integrity: may_hold
branch_B_record_integrity: may_hold
shared_process_continuity: false
TI_C022_verdict: neither_branch_record_is_genuine_shared_process_issuance
```

This recovers E044 exactly.

## Eventual-Synchrony Reduction Test

Eventual synchrony is an environment/protocol assumption:

```text
ES: after some stabilization point, message delays are bounded enough for a protocol
to make progress under its fault assumptions.
```

`SharedContinuous_T` is a trace/legitimacy predicate:

```text
SC: the realized quorum-legitimate schema-state poset has a unique cofinal carrier,
and the record belongs to it.
```

They are different types of condition. More importantly, they are not equivalent.

### ES Is Not Necessary For SC

There can be a trace with unbounded or irregular delays, no stable global delay bound, and no
eventual-synchrony guarantee, while the realized legitimate states still form one cofinal
directed branch:

```text
not ES, but Cof(T) = {F*}
```

The shared process is continuous in the realized poset even if the network model never supplies
the eventual-synchrony assumption.

### ES Is Not Sufficient For SC

There can be eventual synchrony in the network schedule while the relevant fault or legitimacy
assumptions fail, or while two quorum-certified incompatible branches survive as cofinal
branches:

```text
ES, but Cof(T) = {F_A, F_B}
```

Then `SharedContinuous_T` is false for branch-local records. Eventual message delivery does not
by itself choose a unique legitimate carrier.

### Conditional Implication Under Extra Assumptions

Under a particular protocol, fault bound, and fork-choice/finality rule, eventual synchrony may
help prove:

```text
ES + <=f faults + valid fork-choice + common-prefix/finality => Cof(T) is singleton
```

That is a conditional implementation theorem. It is not an equivalence and it does not absorb
the predicate. It says distributed-systems machinery can realize or check the predicate under
extra assumptions.

## Absorber Results

```yaml
BFT_liveness:
  verdict: not_absorbed
  reason: BFT liveness is protocol progress under assumptions; SC is branch uniqueness and
    record membership in the realized trace.

eventual_synchrony:
  verdict: not_absorbed
  reason: neither necessary nor sufficient for SC without extra protocol and fault assumptions.

TCB_integrity:
  verdict: not_absorbed
  reason: authentication/tamper-evidence does not determine unique cofinal carrier membership.

fork_choice_finality:
  verdict: partial_operational_absorption
  reason: a fork-choice/canonical-chain rule is the natural operational implementation of SC.
    TI-C022's remaining surplus is the ontological typing of canonical-branch membership as
    genuine shared-process issuance rather than merely ledger finality.
```

## The Exact Surplus

The exact formal surplus is:

```text
record_integrity + unique_cofinal_quorum_legitimate_carrier_membership
```

not:

```text
record_integrity + eventual_synchrony
```

This matters because E044's permanent fork can have branch-local integrity without a unique
cofinal shared carrier. BFT may be silent off-assumption. TI-C022 still renders a verdict:
branch-local records are not genuine shared-process issuance.

The honest narrowing:

```text
Operationally, TI-C022 is very close to canonical-chain / fork-choice finality.
Formally, it is a trace predicate over quorum-legitimate schema states.
Ontologically, it asserts that canonical-carrier membership is load-bearing for
record reality.
```

The first two are formal. The third remains the speculative TI interpretation.

## Verdict

```yaml
predicate_formalized: true
clock_free: true
eventual_synchrony_reduction: failed
BFT_liveness_absorption: failed
TCB_integrity_absorption: failed
fork_choice_operational_absorption: partial
TI_C022_status_change: none
path_kill_added: shared_process_continuity_as_mere_eventual_synchrony_liveness
```

`TI-C022` survives the residual eventual-synchrony objection, but it does not earn promotion.
The operational content is mostly canonical-carrier membership. The speculative remainder is the
claim that this membership is ontologically load-bearing for record reality.

## Claim-Ledger Effect

```yaml
TI-C022:
  status: unchanged_speculative
  effect: predicate_formalized_and_eventual_synchrony_absorber_defeated
  strongest_version: >
    A record is genuine shared-process issuance iff it is quorum-certified and belongs to the
    unique cofinal quorum-legitimate continuity carrier of the schema-state poset.
  strongest_objection: >
    Fork-choice / canonical-chain finality operationally implements most of the predicate.
    The remaining surplus is ontological, not yet an independent theorem or physical prediction.

TI-C019:
  status: unchanged_formalizing
  effect: shared-participation component receives a cleaner record-legitimacy predicate.
```

## Next Trigger Recommendation

RUN-0051's next ranked frontier after TI-C020 and TI-C022 is:

```text
W000 -> E054_E056_Cech_H3_Ehresmannian_holonomy_bridge_obligations
```

Carry forward:

```text
W000 -> FUNCTOR_OBL_001_Q_OBL_001_filtered_source_functor
```

Do not re-run TI-C022 unless Joe specifically wants to pressure the remaining fork-choice /
canonical-chain ontology absorber.
