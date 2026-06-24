---
artifact_type: exploration
exploration_id: E066
status: active
created: 2026-06-24
run_ref: RUN-0062
claim_refs:
  - TI-C019
  - TI-C020
  - TI-C022
depends_on:
  - E065-cross-repo-os-agent-orchestration-persona-report-2026-06-24.md
---

# E066: Ten-Goal Source / Shadow / Finality Orchestration

## Purpose

Turn the RUN-0061 cross-repo persona result into ten concrete, well-ordered
goals. This artifact is an orchestration plan, not execution of all ten goals.
Each goal below should become its own run, artifact, commit, and push unless a
future instruction explicitly overrides that rule.

## Current Premise

Temporal Issuance should remain the source-side issuance program. Time as
Finality should remain the observer-shadow, projection, and finality audit
program. The useful bridge is an explicit interface contract, not a repo merger
or claim promotion.

## Orchestration Rule

The ten goals are not peers. Goal 1 is the serial dependency. Goals 2, 3, 6, 7,
8, and 9 can run as independent lanes after Goal 1. Goal 4 can also run after
Goal 1, but Goal 5 depends on Goal 4. Goal 10 is the final serial synthesis and
frontier re-rank.

Every actual goal run should:

1. start from clean git state;
2. write exactly one bounded primary artifact;
3. update steward surfaces only after the Repo Steward serial merge;
4. run `git diff --check`;
5. commit and push before the next run lands.

## Ten Goals

### G01: Source / Shadow / Finality Interface Contract

Type: serial foundation.

Question: what is the smallest contract connecting source issuance to observer
projection and record finality without merging Temporal Issuance and Time as
Finality?

Required objects:

```text
SourceExtension
Projection
Capability
RecordFinality
LossKernel
Absorber
```

Primary artifact:

```text
explorations/E067-source-shadow-finality-interface-contract-2026-06-24.md
```

Success condition: the contract is small enough to run finite examples through
it and strong enough to distinguish source issuance from bounded access to a
fixed richer source.

Failure condition: the contract collapses into shared vocabulary or a vague
cross-repo synthesis.

Parallelization: none. This must be serial.

### G02: Finite Positive Example Through The Contract

Type: parallel fixture lane after G01.

Question: can a finite formal example pass through all contract objects without
claim promotion?

Candidate example: `Compat_G^MLTT` source-extension residue, restricted to a
small finite trace where source novelty, projection, capability, record
finality, and loss are all explicitly typed.

Primary artifact:

```text
explorations/E068-source-shadow-finality-positive-fixture-2026-06-24.md
```

Success condition: one example traverses the interface without confusing source
novelty with observer finality.

Failure condition: the example cannot be typed without importing hidden future
schema or extra authority.

Parallelization: can run beside G03, G06, G07, G08, and G09 after G01.

### G03: Fixed-Source Bounded-Access Negative Control

Type: parallel absorber lane after G01.

Question: what does the contract do when apparent novelty is only expanding
access to a fixed richer source?

Candidate absorber:

```text
fixed Mu_infty + expanding aperture P_n + observer readout/finality
```

Primary artifact:

```text
explorations/E069-fixed-source-bounded-access-negative-control-2026-06-24.md
```

Success condition: the contract marks this as projection/access novelty, not
source issuance.

Failure condition: the contract incorrectly classifies fixed-source disclosure
as source-side issuance.

Parallelization: can run beside G02, G06, G07, G08, and G09 after G01.

### G04: AC-8 Actor Protocol Source Trace

Type: parallel source-witness lane after G01.

Question: can AC-8 be stated as an actor/message protocol with no hidden
supervisor, no completed future mailbox, and no preloaded global grammar?

Primary artifact:

```text
explorations/E070-ac8-actor-protocol-source-trace-2026-06-24.md
```

Success condition: a local actor trace produces a new admissible schema that
cannot be represented as a hidden future schema inside the current actors.

Failure condition: the trace requires a hidden supervisor, global grammar, or
completed future mailbox.

Parallelization: can run after G01, but G05 depends on it.

### G05: AC-8 Projection And Finality Audit

Type: dependent projection lane.

Depends on: G04.

Question: once AC-8 has a source trace, what does a Time as Finality observer
profile see, lose, and finalize?

Primary artifact:

```text
explorations/E071-ac8-projection-finality-audit-2026-06-24.md
```

Success condition: the audit separates source-side schema negotiation from
observer-visible records and finality.

Failure condition: the projection audit cannot distinguish actor-local source
novelty from observer-side record stabilization.

Parallelization: cannot start until G04 is complete.

### G06: IssuedCapability Contract Test

Type: parallel capability lane after G01.

Question: can capability language be used as the shared bridge vocabulary
without turning access control into fake issuance?

Primary artifact:

```text
explorations/E072-issued-capability-contract-test-2026-06-24.md
```

Success condition: `IssuedCapability` is non-derivable in the source layer and
projection-sufficient in the observer layer.

Failure condition: the capability is merely hidden ambient authority disclosed
later.

Parallelization: can run beside G02, G03, G07, G08, and G09 after G01.

### G07: Memory LossKernel Audit

Type: parallel governance/formalism lane after G01.

Question: what exactly do steward memory summaries and Time as Finality memory
packs preserve, compress, and lose?

Primary artifact:

```text
explorations/E073-memory-losskernel-audit-2026-06-24.md
```

Success condition: memory summaries can be typed as lossy projections below
authority surfaces.

Failure condition: summaries silently become authority or cannot state what was
lost.

Parallelization: can run beside G02, G03, G06, G08, and G09 after G01.

### G08: TI-C022 Record-Reality Typing Fixture

Type: parallel absorber lane after G01.

Question: after RUN-0057, is there any type-level surplus beyond ordinary
fork-choice/canonical-chain finality?

Primary artifact:

```text
explorations/E074-ti-c022-record-reality-typing-fixture-2026-06-24.md
```

Success condition: a precise type distinction remains after the protocol
already supplies quorum validity, canonical carrier selection, finality, and
finalized record membership.

Failure condition: all operational and type-level content is absorbed by
standard finality machinery.

Parallelization: can run beside G02, G03, G06, G07, and G09 after G01.

### G09: Typed Effect Signature

Type: parallel formal discipline lane after G01.

Question: can a minimal effect signature prevent the actual category mistakes
seen in recent runs?

Candidate effects:

```text
Issue[S]
Project[O]
Finalize[R]
Lose[K]
```

Primary artifact:

```text
explorations/E075-typed-effect-signature-for-source-shadow-finality-2026-06-24.md
```

Success condition: the effect labels block at least one real mistake, such as
treating projection novelty as source issuance.

Failure condition: the labels only rename existing distinctions and do not
improve any fixture.

Parallelization: can run beside G02, G03, G06, G07, and G08 after G01.

### G10: Frontier Re-Rank And Integration

Type: final serial synthesis.

Depends on: all completed prior goals.

Question: after the ten-goal sequence, what is the next highest-verdict
frontier?

Primary artifact:

```text
agent-runs/RUN-00XX-ten-goal-frontier-integration.md
```

Success condition: W010 can rank the results, preserve parked conditions, and
choose one next trigger without stale memory, duplicate path kills, or unclear
claim movement.

Failure condition: results are too broad, too disconnected, or too
governance-heavy to change the frontier.

Parallelization: none. This is serial.

## Batch Plan

### Batch 0: Serial Foundation

```text
G01
```

Output: interface contract.

Why serial: every other goal needs the same typed vocabulary and absorber
boundary.

### Batch 1: Independent Contract Fixtures

```text
G02, G03, G06, G07, G08, G09
```

Output: six bounded artifacts, each committed and pushed after its own run.

Parallel shape: these can be run as read-only explorer lanes or separate serial
runs. Shared steward surfaces must be merged only by the Repo Steward.

### Batch 2: AC-8 Source Then Projection

```text
G04 -> G05
```

Output: actor-protocol trace, then projection/finality audit.

Why separate: source trace must exist before observer-finality audit can be
honest.

### Batch 3: Serial Integration

```text
G10
```

Output: W010-style frontier re-rank and next-trigger decision.

## Recommended Immediate Next Run

```text
W000 -> G01_source_shadow_finality_interface_contract
```

Do not start the other nine goals before G01 exists. Without G01, the other
goals will likely drift into vocabulary bridges.

## Claim-Ledger Implication

No claim movement is warranted from this orchestration plan. Claim movement can
only occur after a concrete fixture changes the status of a specific claim.

## Kill Condition For The Ten-Goal Sequence

Stop or re-route the sequence if G01 cannot define a small contract that
distinguishes:

```text
source issuance
projection/access novelty
record finality
lossy memory/projection
absorber-controlled bookkeeping
```

If that distinction fails, the ten-goal plan is not mature enough to execute.
