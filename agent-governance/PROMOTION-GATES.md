---
artifact_type: promotion_gates
status: active
governance_role: promotion_control
constitutional: false
---

# Promotion Gates

## Claim Promotion

A claim may not move directly from `speculative` to `promoted`.

Minimum path:

1. speculative
2. formalizing
3. testable or weakened
4. hostile review
5. promoted or killed

**Who promotes (2026-07-03).** Agents own the promotion decision and may execute status moves in `CLAIM-LEDGER.md` directly once the path above is satisfied — promotion no longer pauses for Joe. This is deliberate: agents hold the closest read on whether a claim has earned its status, and pausing on Joe was blocking the flow of work.

**Step 4 (hostile review) is not a work-stop.** Hostile review is adversarial scrutiny of the claim; the steward performs it directly or requests an outside reviewer. Needing or requesting outside review is a judgment input, not a halt — it may change which claim or path the steward advances next, but it never stops the program and never justifies a global "no worthy work until reviewed" wait. Route any review request via `CapacityOS/mailboxes/joeops/` and keep working.

**Mandatory JoeOps notice on hard promotion.** Moving a claim to `promoted` — the tier an external reader would take as "this repo asserts this is true" — MUST be accompanied by an awareness note dropped in `CapacityOS/mailboxes/joeops/`, using `agent-governance/templates/hard-promotion-joeops-notice.md`. The note is for awareness, not approval. It records what was promoted, the case FOR (how each gate was met), the steelmanned case AGAINST, how the call was made, the risks / blast radius, the supporting artifacts and certificates (tests, Lean proofs — `sorry`/`axiom`-free?), and how to reverse. Filing the note is part of the promotion, not optional. Status moves below `promoted` need no note. A `promoted -> killed/weakened` demotion needs no note but is logged in the ledger as usual.

## Workflow Promotion

A dynamic workflow becomes durable only if it:

- produces reusable learning
- improves verdict probability
- has clear inputs and outputs
- has a learning return
- does not create unmergeable noise

## Persona Promotion

A persona becomes durable only if repeated runs show that it improves at least one of:

- falsification quality
- absorber mapping
- formal precision
- category-error detection
- governance legitimacy

