---
artifact_type: exploration
status: advisory_record
governance_role: wall_triage_followup
claim_movement: false
created: 2026-07-10
source: class_no_go_audit_plus_science_advisory_council
claim_refs:
  - TI-C006
  - TI-C009
  - TI-C010
  - TI-C017
  - TI-C018
  - TI-C019
  - TI-C020
---

# E159: Class No-Go Audit And Science Council Update

This note records the repo-local outcome of the cross-repo "class no-go mistaken
for a wall" audit and the follow-on five-lens Science Advisory Council. It is an
advisory record only. It does not reopen a lane, promote a claim, or change a
claim status.

## Method

The audit applied two failure forms:

- Form A: Layer-0 semantic misalignment, where a no-go theorem and the local
  lane use the same term for different objects.
- Form B: diagnostic artifact, where a screen rejects genuine examples of the
  target class rather than falsifying the target.

The council then asked what the audit might still be missing through five
lightweight lenses: falsificationist, paradigm historian, cross-disciplinary
translator, adversarial methodologist, and constructive steelman.

## TI Findings

| Wall | Recorded verdict or grade | Council disposition | Action discipline |
| --- | --- | --- | --- |
| Bare `<=_S`, `CLAIM-LEDGER.md` TI-C006 and `memory/path-kills.md` RUN-0024 | TI-C006 `killed` | Confirmed genuine wall for bare source-side order. Derived order remains allowed only as a successful `Ext_S` invariant. | Do not resurrect bare order; derive it from a successful typed extension rule if needed. |
| Energy-momentum route, TI-C009/TI-C010 and `memory/path-kills.md` BDO/ICO | `archived`; BDO/ICO path-killed the Lorentzian `p^mu` route | Prior council flagged possible overbreadth if "energy" meant cost-of-finality. Spot-checking `explorations/E140-cost-of-finality-landauer-energy-bridge-2026-07-03.md` shows that route has now also been tested and absorbed. | Downgrade the prior second-look to a genuine wall over both tested energy routes, with E140's honest limits. |
| Holonomy from bare `Ext_S`, `explorations/E015-holonomy-fixture.md`, TI-C018 | TI-C018 `weakened`; bare loop does not determine holonomy | Confirmed Form-A candidate. A loop word is not a `G`-valued holonomy until a transport functor `A: ExtCat -> B G` is derived or stipulated. | Re-examine only by deriving `A` from C-typed admissibility; otherwise keep as formal residue. |
| Cech/sheaf witness, TI-C017 in `CLAIM-LEDGER.md` | Generic obstruction absorbed by AB sheaf contextuality; survivor narrowed | Confirmed genuine wall for generic no-global-section novelty. | Specify admissibility-determined sheaf data before using the route as novelty. |
| D4 categorical no-go, `explorations/E017-d4-categorical-formalization.md` | Unqualified functor no-go killed; online/prefix-faithful obstruction survives conditionally | Confirmed Form-A/scope lesson. Broad `CloSys` with completed history and online prefix-faithful closed systems are different targets. | State the narrow `CloSys_online` theorem only; do not cite the unqualified no-go. |
| D4 projection-level evidence, `memory/path-kills.md` RUN-0046 | Path killed by fixed-source aperture construction | Confirmed genuine wall against reading projection-layer D4 as source-side issuance evidence. | Need a witness not representable as fixed source plus apertures. |
| Mere expressiveness, `memory/path-kills.md` RUN-0050 | Path killed | Confirmed genuine wall against complexity/infinity alone as issuance evidence. | Require self-encoding admissibility, productive escape, and no hidden completed oracle. |

## Council Top TI Advice

1. Holonomy remains the cleanest Form-A caution: "loop" and "holonomy" must not
   be conflated. The missing object is a source-derived transport functor.
2. The prior audit's energy-route overbreadth warning is now mostly superseded
   by E140. BDO/ICO closed the ordering-to-`p^mu` route, and E140 closed the
   cost-of-finality route as absorbed at the control-case level.
3. The D4 categorical lesson is methodological: the useful theorem is the
   online/prefix-faithful obstruction, not the killed unqualified no-go.

## No Claim Movement

No claim status changes are made by this note. The ledger-facing state is
annotation-only: TI-C009/TI-C010 already carry the E140 cost-of-finality result
as tested and absorbed, so future audits should not treat that route as still
untested.
