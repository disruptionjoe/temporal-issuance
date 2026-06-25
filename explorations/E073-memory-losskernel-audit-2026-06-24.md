---
artifact_type: exploration
exploration_id: E073
status: active
created: 2026-06-24
run_ref: RUN-0068
goal_ref: G07_memory_losskernel_audit
claim_refs:
  - TI-C019
depends_on:
  - E067-source-shadow-finality-interface-contract-2026-06-24.md
  - E072-typed-effect-signature-source-shadow-finality-2026-06-24.md
context_repos:
  - temporal-issuance
  - ../time-as-finality
---

# E073: Memory LossKernel Audit

## Purpose

Run G07 from the ten-goal sequence. This audit treats memory summaries and
memory packs as projections with typed loss, not as neutral mirrors of history
or authority surfaces.

## Effect Classification

Memory summarization has effects:

```text
Project[O]   yes, raw history is projected to a compact load surface
Finalize[R]  yes, committed memory surfaces become durable records
Lose[K]      yes, details are compressed or omitted
Issue[S]     no
```

Memory does not issue new research truth. It preserves, compresses, and routes.

## Temporal Issuance Steward Memory

Source history:

```text
H_TI = run records + memory log + claim ledger + path kills + roadmap +
       next-trigger plans + governance ledgers + explorations
```

Projection:

```text
pi_memory(H_TI) = memory/steward-memory-summary.md
```

Capability:

```text
Cap_memory = choose the next run, avoid stale killed paths, preserve current
strongest version and objection, and reload enough state for W000.
```

### Preserved Fields

The current summary preserves:

- current North Star and constitutional framing;
- current verdict that TI does not derive physics;
- current next required test;
- recent run outcomes from RUN-0050 through RUN-0067;
- major killed or parked paths;
- the strongest surviving formal-source witness;
- the rule that physical TI-C020 is unresolved.

### Lost Fields

The current summary loses or compresses:

- full proof details from individual explorations;
- exact line-by-line changes;
- complete persona arguments;
- all raw alternatives considered and rejected inside each run;
- exact local order quirks in the append-only memory log;
- detailed resurrection triggers unless separately preserved in path-kills;
- fine-grained evidence from adjacent repos unless cited by a recent run.

### Quotient Relation

Two raw histories are equivalent under the memory summary when they produce the
same compact current state:

```text
H1 ~_summary H2 iff pi_memory(H1) and pi_memory(H2) give the steward the same
current verdict, strongest objection, killed paths, and next trigger.
```

This quotient is useful but lossy.

### Capability Spread Risk

The dangerous spread is:

```text
same memory summary
different true blocker or resurrection condition
```

Mitigations already present:

- summary cites run IDs;
- memory log remains append-only history;
- path kills preserve resurrection triggers;
- memory summarizer protocol says the log wins if summary and log disagree;
- next-trigger plan is a separate authority/routing surface.

Verdict for TI memory:

```text
Project[O] + Finalize[R] + Lose[K]
not Issue[S]
```

## Time As Finality Memory Packs

Source history:

```text
H_TaF = workflow runs + family memory logs + research operating model +
        registries + synthesis logs
```

Projection:

```text
pi_pack(H_TaF) = workflows/context-packs/*/MEMORY.md
```

Capability:

```text
Cap_pack = let a workflow load compact family guidance without reading raw
history.
```

### Preserved Fields

The TaF memory packs preserve:

- purpose and scope of the workflow family;
- authority disclaimer;
- summarizer contract;
- learning-return schema;
- current rolled-up guidance, when any exists;
- rule that ordinary agents read the compact surface, not raw logs.

### Lost Fields

The packs lose:

- raw workflow history;
- full rejected ideas;
- one-off details not promoted by summarizer;
- exact conflicts unless promoted or logged;
- all lessons not yet summarized.

### Authority Guard

TaF explicitly marks memory packs as guidance only and below higher authority
surfaces. This is the correct LossKernel posture.

Verdict for TaF memory packs:

```text
Project[O] + Lose[K]
not Issue[S]
not policy authority
```

## Cross-Repo Memory Contract

Memory surfaces should declare:

```text
preserved_fields
lost_fields
quotient_relation
capability_spread_risk
authority_rank
escalation_path
```

Temporal Issuance already has most of this across its summary and summarizer
protocol. Time as Finality has it explicitly in memory-pack form.

## Finding

G07 succeeds. Memory summaries are useful precisely because they are lossy
projections. They should be treated as:

```text
Project[O] + Finalize[R] + Lose[K]
```

and explicitly not:

```text
Issue[S]
```

## Actionable Next Improvement

Future Temporal Issuance memory summarizer work should add a compact
LossKernel section when the summary format is next revised:

```text
preserved_fields:
lost_fields:
capability_spread_risk:
authority_limit:
```

This is queued as a future improvement, not implemented here, because G07's
purpose is audit and classification rather than governance-format expansion.

## Claim-Ledger Implication

No claim movement. This is governance/formalism hygiene for memory surfaces.

## Next Goal Recommendation

The next ten-goal sequence item should be:

```text
G08_TI_C022_record_reality_typing_fixture
```

Reason: G07 has finished the LossKernel lane; G08 is the remaining record
finality/type surplus lane before AC-8 actor work.
