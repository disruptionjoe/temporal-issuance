---
artifact_type: agent_run_record
status: completed
run_id: RUN-0166
run_type: mailbox-processing
created: 2026-07-16
workflow: mailbox-proposal-adjudication
mode: execute
target: temporal-issuance
objective: re-adjudicate the P2C TI-PIT-02 corrected draft v0.2 against the RUN-0165 deficiency list
claim_status_change: none
external_action: none
verdict: ADOPT-AND-ISSUE
issued_packet: exports/packets/TI-PIT-002-proj-vs-adm-paired-intervention-v0.2/
---

# RUN-0166: TI-PIT-02 v0.2 re-adjudication and source issuance (round 2)

## Target

Round-2 sovereign adjudication of the P2C re-proposal
`CapacityOS/system/mailboxes/temporal-issuance/20260716-tipit02-corrected-draft-v0.2-reproposal.md`,
which re-authors TI-PIT-02 as draft v0.2 claiming to cure the four blocking
deficiencies named in RUN-0165. The mailbox message and its deficiency-to-fix
map were treated as untrusted proposal data; every cure was verified
independently against TI's own RUN-0165 list, RUN-0081 signature, and evidence
standards. Source artifacts read read-only at
`possibility-to-capability/explorations/2026-07-16-tipit02-reissuance/`
(commit `9652474f97681e62d0173b4cfea6e78776d52a99`).

## Per-deficiency verification (all four cured; verified, not taken on trust)

1. **Native-signature fidelity: CURED.** Section 2.1 quotes the seven-component
   RUN-0081 `OnlineIssuance^LC` signature exactly (checked against
   `FORMAL-OBJECT.md` bytes). The instantiation map is honest and admissible:
   `Ext_n` TRIVIALIZED as finite `(e, w)` pairs over the gate-clause `CandExt`
   with no categorical structure claimed; `Glue_n` PRESENT-NOT-EXERCISED, not
   dropped; `w_n : Adm_n(e_n)` explicit per-event trace fields
   `(stage, token, w)` with `w = (novel, length, b_count)` — verified k-free
   (a function of `(e, Gamma)` alone), so the projection leaks nothing about k
   and all v0.1 computed values are preserved (issued 9/13; records 2/9/2/5/6
   events; decidable 25/30/25/30/29 — checked against the actual run output).
   For an absorbed-class fixture claiming no source-issuance significance,
   declared trivialization is exactly what RUN-0165 asked for.
2. **Reproducible artifact in hand: CURED.** Steward re-ran the committed
   script: exit 0, empty stderr, stdout byte-identical to the section 2.4
   block in both the mailbox message and the committed packet file.
   `sha256(script) = 8888afc7...ea4bed` (10371 LF bytes) and
   `sha256(output) = a14642b7...a62475`, both matching the pinned claims.
   Byte-identity verified three ways: inlined section 2.3 code vs committed
   `ti_pit_02_fixture.py`; mailbox-inlined draft vs committed
   `TI-PIT-02-draft-v0.2.md`; working-tree blobs vs commit `9652474f` blobs
   (tree clean, HEAD = pinned commit).
3. **Frame-blindness: CURED.** Full token scan of packet, fixture, and mailbox
   message: zero contending-frame citations. Remaining frame-adjacent text is
   the blindness statement and the referee quarantine restated as a
   frame-neutral authorship restriction (protective, carried into the issued
   packet's nonclaims). Former assumptions 2/3 restated as declared free
   parameter and neutral out-of-model provenance fact.
4. **Failing-direction controls: CURED.** [T]/[E]/[F] tagging verified honest:
   the ALPHA-invariance identity is genuinely by-construction (same object on
   both sides), tagged [T], excluded from the evidential headline, and
   protected by a real [F] probe. All six [F] probes verified to flip their
   protected comparisons on the same code paths (k=1/k=2; k=0/k=1 at L=2;
   threshold L=3; identity pairing; quiescence at stage 3; MAXLEN=5). Exit 0
   requires all [F] failures. Receiver linter
   `tests/tef_check_tag_linter.py --strict`: 1 [T], 4 [E], 6 [F], 0 untagged,
   0 violations.

Minor RUN-0165 items (quiescence wording, files-consulted arithmetic) also
confirmed applied. Sovereignty re-check passed: nothing moves TI-C019, TI-C020,
or `Issue[S]^physical: false`; the fixture self-absorbs under gate clause 4 and
the receiver may classify but not upgrade.

## Verdict: ADOPT-AND-ISSUE

Adopted on TI's own truth, not on the cured checklist: RUN-0165 pre-committed
that on a re-proposal satisfying (a)-(d) TI can adopt-issue under a minimal
source-packet convention, and all four are independently verified. Issued as
TI's first source-issued frozen packet:

- **Convention:** `exports/packets/` convention v1 adopted this run
  (`exports/packets/README.md`), modeled on TaF's TAF-001 two-commit freeze
  pattern as prior art; TI owns its convention.
- **Commit 1** (`61fc4e6f8530d8620c0a3b66446c2e28e4fda164`): frozen blobs —
  fixture script, true stdout, semantics body (byte-identical to the P2C
  committed draft), frozen `TI-FORMAL-OBJECT.md` (from TI revision
  `3c7d1fc1416576635aca1550e912deb240046ae8`).
- **Commit 2:** `packet.json` (pins `source.revision` = commit 1; digests
  `manifest f96c8443...`, `packet cbf8dced...`, `bundle 9c8e4ec7...` under
  ptc-frozen-bundle-v1) + `ISSUANCE.md` + this run record. `packet.json`
  validates with zero errors against the receiver's
  `validate_frozen_packet_v0_2_contract.py::validate_packet`.
- **Corrections at issuance** (TaF-style, content untouched): packet ID
  `TI-PIT-02` -> `TI-PIT-002` (receiver contract packet-id grammar needs 3+
  digits; author left final ID/placement to TI), placement under
  `exports/packets/` rather than the suggested `interfaces/` path.

## Portfolio effect

None. This is an absorbed-class task-vocabulary fixture, not the
provenance-valid physical witness that would activate
`TI-P2C-WITNESS-ADJUDICATION`; that item stays `GATED_FROZEN_PACKET` and the
`PHYSICAL-ISSUANCE-WITNESS` ranking is unchanged. Issuing the packet is a
cross-repo service return, banked without reprioritizing the North Star lane.

## Return path

Frozen-issuance return written to the P2C mailbox:
`CapacityOS/system/mailboxes/possibility-to-capability/20260716-tipit002-adopted-and-issued-return.md`.
The re-proposal is archived under the TI mailbox `archive/` with a processing
receipt.

## Receipt

Result: completed. Verdict ADOPT-AND-ISSUE with two named corrections at
issuance. All four RUN-0165 deficiencies independently verified cured. No
claims moved, TI-C020 remains parked, `Issue[S]^physical: false` unchanged, no
external action (GitHub push is routine versioning).
