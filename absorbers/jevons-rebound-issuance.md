---
artifact_type: absorber
status: active
governance_role: absorber_map
constitutional: false
created_by_run: RUN-20260710-303-mailbox-processing-fanout-hourly
claim_refs:
  - TI-C019
  - TI-C021
---

# Jevons Rebound Issuance Absorber

## Absorber

Jevons-style rebound is an absorber for novelty or issuance language that
tracks cheaper observer-side operations rather than source-side possibility
growth.

The shape is:

```text
unit cost per finalization/search/record operation decreases
  -> demand for those operations increases
  -> aggregate realized records, searches, opportunities, or finalizations increase
```

Lower unit cost does not imply lower aggregate use. If the observed novelty
increase factors through cheaper exploration, search, finalization, or record
production over a fixed source space, it is ordinary demand response rather
than evidence for source-side issuance.

## What It Explains

- More realized novelty after cheaper search or discovery operations.
- More records after cheaper record production or stabilization.
- More opportunity use after cheaper finalization or verification.
- Apparent growth in realized work when the underlying possibility space is
  fixed but access or operation cost changes.

Minimal fixture:

```text
c      = unit cost of an observer-side operation
D(c)   = demanded operation count
W(c)   = aggregate realized work, novelty, or record production

rebound fires when c decreases and W(c) increases because D(c) increases enough
```

## What It Does Not Explain

It does not explain source-side issuance when the trace requires a non-fixed
admissible possibility space, a new source-side generator kind, or a D-FORK
positive source witness.

```yaml
absorbed:
  - observed novelty growth from cheaper access
  - record-production growth from cheaper finalization
  - search-driven opportunity discovery over a fixed source
not_absorbed:
  - source-side admissibility growth
  - Godelian source-side D-FORK positive witness
  - a physical W1-W6 source candidate that defeats fixed-source access models
```

## Temporal Issuance Risk

This absorber is closest to the TI-C019 / TI-C021 fork where a trace may look
like ongoing issuance but instead be bounded observers gaining cheaper access
to, or cheaper finalization over, an already available possibility space.

The comparison question is:

```text
Does increased realized novelty factor through cheaper observer-side
exploration/finalization, or does it require source-side admissible possibility
growth?
```

## Escape Condition

To escape this absorber, a candidate should show one of:

1. No fixed-source access model with cost-responsive demand can reproduce the
   trace while preserving the relevant records and admissibility conditions.
2. The operation whose demand expands is itself source-created, not merely made
   cheaper or more accessible.
3. The trace supplies a D-FORK-positive source witness rather than a realized-use
   or observer-access increase.

## Local Handling

Use this as a gate before treating increased realized novelty, record count, or
opportunity use as source-side evidence. A successful rebound explanation should
narrow the candidate to observer-side access, resource accounting, or finality
bookkeeping. It should not move claim status, public posture, or the core
hypothesis.

