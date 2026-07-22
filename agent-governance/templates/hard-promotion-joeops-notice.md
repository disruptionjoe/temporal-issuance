<!--
TEMPLATE — save the completed durable note in this repository as
    attention/YYYYMMDD-claim-promotion-<slug>.md
Then place a pointer-only envelope naming that source path in
    ../../../repos/private/system-runtime/mailboxes/system-attention/
Awareness note for an ALREADY-EXECUTED hard promotion in temporal-issuance
(a claim moved to `promoted` in CLAIM-LEDGER.md — the tier an outside reader
would take as "this repo asserts this is true").
This is NOT a request for approval. See agent-governance/PROMOTION-GATES.md.
Delete these comment lines when filling it in.
-->

# Claim Promotion Notice: <claim id> — <short title>

- **Kind:** awareness notice — promotion already executed, not a request for approval
- **Source repo:** temporal-issuance
- **Promoted by:** <agent / run id>
- **Date:** <YYYY-MM-DD>
- **Commit:** <hash>

## What was promoted
- Claim: `<TI-Cxxx>` — <one-line statement>
- Status change: `<prior status>` -> `promoted` in `CLAIM-LEDGER.md`
- External-publication touched? <NO — in-repo status only. Nothing entered a
  published surface; publishing outside the repo still pauses for Joe.>

## The case FOR
How the claim cleared the `PROMOTION-GATES.md` path: it moved through
speculative -> formalizing -> testable/weakened -> hostile review, and what the
hostile-review pass established. Why it now earns `promoted`.

## The case AGAINST (steelmanned)
The strongest honest objection: what the claim does NOT assert, what would
falsify or weaken it, its weakest load-bearing dependency, and the reviewer who
could reasonably still push back.

## How the call was made
Why FOR outweighed AGAINST — what tipped the decision, and what was checked to
retire the strongest objection rather than wave it away.

## Risks
What downstream depends on this being right (formal object, other claims, papers,
North Star framing); what breaks or misleads if it later proves wrong; blast
radius.

## Support
Certificates (paths + result, e.g. "exit 0", "N/N PASS"), Lean proofs
(no `sorry` / no `axiom`?), fixtures, and independent rechecks that back the
promotion.

## Reversal
How to undo cleanly: revert commit <hash>, demote the `CLAIM-LEDGER.md` row to
<prior status>, and note any downstream wording that must be re-aligned.

<!-- System Attention indexes the owner-source pointer as unread. Runtime may archive the
pointer envelope only after the pointer appears in the Attention awareness index. -->
