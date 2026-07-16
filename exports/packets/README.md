# TI Source-Issued Packets

Status: convention v1, adopted 2026-07-16 by the Temporal Issuance steward (first instance: TI-PIT-002). Modeled on the Time as Finality `exports/packets/` convention (TAF-001) as prior art; TI owns this convention independently.

`exports/packets/` holds **source-issued frozen packets**: outbound evidence artifacts that Temporal Issuance issues to other repositories. They are neither internal explorations nor agent-run records; their bytes must stay frozen independently of internal iteration.

## Rules

- One directory per packet: `TI-<FAMILY>-<nnn>-<slug>-v<major.minor>/`.
- Contents: `packet.json` (metadata conforming to the receiving repository's frozen-packet contract), `blobs/` (the raw frozen artifacts: computations, captured outputs, the packet semantics body, and frozen copies of the TI source documents the packet's premises cite), a `.gitattributes` marking everything `-text`, and an `ISSUANCE.md` recording the steward decision.
- **Frozen means frozen.** After issuance, nothing inside a packet directory is edited, ever. Corrections issue a new packet version directory; the old one stays.
- Two-commit issuance: commit 1 freezes the blob contents; `packet.json` then pins `source.revision` to commit 1's SHA and carries digests over the frozen bytes; commit 2 adds `packet.json` and `ISSUANCE.md`.
- Issuing a packet never changes a TI claim status, and a receiver's conclusions built on a packet never flow back into TI claims (`authority_transfer = false`).
- Issuance is a steward act on a mailbox proposal or internal decision; the adopting steward validates content against TI's own formal object (RUN-0081 `OnlineIssuance^LC`) and evidence standards before issuing, and may reject or return NOT-YET-ISSUABLE.
