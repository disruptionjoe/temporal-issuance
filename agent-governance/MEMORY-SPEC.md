---
artifact_type: memory_spec
status: active
governance_role: memory_contract
constitutional: false
pattern_sources:
  - CapacityOS FLW-135 Memory Pack Pattern
  - CapacityOS FLW-103 Anchored Agent Pattern
---

# Memory Spec

Temporal Issuance uses the Memory Pack shape.

## Required Pieces

1. Compact load surface
2. Append-only memory log
3. Memory summary
4. Summarizer contract
5. Learning return schema
6. Authority boundaries

## Steward Memory Paths

- Compact load surface: `agent-governance/REPO-STEWARD.md`
- Memory summary: `memory/steward-memory-summary.md`
- Memory log: `memory/steward-memory-log.md`
- Learning return schema: `memory/learning-return-schema.md`

## Append-Only Rule

Memory log entries are append-only. Corrections are new entries. Do not rewrite history.

## Summary Rule

The memory summary compresses current state for future steward wakeups. It should not become policy unless an authority surface records the policy change.

## Dynamic Packs

Durable workflows and personas may receive their own memory pack when repeated use shows that memory would improve falsification, absorption, formalization, or governance quality.

