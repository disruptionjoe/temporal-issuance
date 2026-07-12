---
artifact_type: research_steering_card
status: active
governance_role: attention_priority
created: 2026-07-12
constitutional: false
ranking_engine: attention/priority_condorcet.py
---

# Research Steering Card

Primary function: Joe does not read this card. When Joe says "I have attention for this," run `python attention/priority_condorcet.py` and hand him the top few ranked items in order, each with a one-line why, and nothing else.

Seeded from the 2026-07-12 inline council assessment:

- Coherence gap: the repo has a strong formal source residue and a strong physical adapter gate, but no single interface object that connects source growth to a domain-native, preserved capability or task change while defeating whole-family completion.
- Local minimum: gate-aware no-worthy-work has become correct but inert. The repo repeatedly builds formal/local traces, pressures them through `Adapter_P`, watches whole-family completion or physical W1/W4/W5 fail, and then waits for a candidate to appear.
- Breakout moves: turn whole-family completion into a theorem target, build the missing operative source-action generator, and calibrate the physical gate with a CRISPR/Floquet near-miss batch.

## attention_priority

Current ranked list from `attention/priority_condorcet.py`:

1. **P1: Real H7-admitted packet intake** - Only a real packet through the E172/E173 obligations can revise the bounded contract or move claims.
2. **G2: Distinct T2 contract stressor gate** - Run only if it tests the T2 contract in a new way without repeating T3 or broadening the claim.
3. **W000: Gate-change wait after T3 validator** - Use this state when there is no real packet and no distinct contract-testing gate.

Re-rank by editing `ITEMS` and `BALLOTS` in `attention/priority_condorcet.py`, then re-run the script and paste the new ranked list here.

## council

Standing rule: the council proposes RESEARCH ADVANCEMENT of this repo only. It does NOT propose external review, submission prep, methodology papers, or "shipping" items. Joe is aware of those; they are not the advancement of the research.

Personas are ALWAYS run inline in a single worker, never one-agent-per-persona, at any count.

Standing roster:

| Persona | Lens |
| --- | --- |
| Orthodox professor | Does this reduce to known computability, physics, category theory, thermodynamics, or distributed-systems machinery? |
| Heterodox-rigorous professor | Which unforced choices are carrying the structure: no-hidden-oracle, source growth, anti-after-naming, or physical adapter fields? |
| Commercial scientist | What cheap decisive fixture or theorem target is being skipped in favor of more narrowing? |
| Philosopher of science | What would actually kill the central claim, and where is the repo protecting itself with scope language? |
| Wild mathematically-serious frontier scientist | What highest-upside object could make issuance more than formal residue? |
| Computability and proof-theory specialist | Are diagonalization, c.e. ceilings, internal admissibility, and completion boundaries stated without equivocation? |
| Category, sheaf, and topos theorist | Are `ExtCat`, `Adapter_P`, functorial transport, Cech residue, and prefix contexts real structure or presentation? |
| Quantum and operator-algebra foundations specialist | Is alleged state-space or algebra growth genuine, or fixed-H / fixed-A / measurement-context bookkeeping? |
| Thermodynamics and information theorist | Does any finality or cost claim survive Landauer, Bekenstein, maintenance thermodynamics, entropy, and resource-theory absorption? |
| Cosmology and boundary-physics specialist | Does horizon, boundary, celestial, or GU-adjacent language supply source crossing, or only imported exterior structure? |
| Distributed systems and finality theorist | Does record reality, canonical carrier membership, or multi-holder finality add operational surplus over fork choice and consensus finality? |
| Evolution and open-endedness theorist | Do CRISPR, autocatalysis, adjacent-possible graphs, or evolutionary search supply source formation, or fixed latent-space disclosure? |

## ranking_engine

Engine path:

```text
attention/priority_condorcet.py
```

Run:

```text
python attention/priority_condorcet.py
```

Ranking rule:

- `ITEMS` is the live hypothesis / next-move set.
- `BALLOTS` is each persona's strict preference order, best first.
- Item X outranks item Y when a majority of personas prefer X to Y.
- If the majority graph is acyclic, use that Condorcet order.
- On a cycle, fall back to Copeland score: pairwise wins minus pairwise losses.
- Tie-break by average ballot position, then item id.
- The script validates every ballot and exits 0 when the ranking is well formed.

## execution_strategy

Waves method:

- A wave is a dependency-bounded batch of hypotheses attacked together.
- Stop a wave and start a new one exactly when the next batch depends on the current wave's result.
- Independent probes fan out in parallel as separate background workers only when they do not write the same surfaces and do not depend on each other's result.
- Genuinely dependent probes serialize.
- Shared-surface merges are steward-owned and serial.

GU-style full wave protocol:

- Use a full blind-branch wave when one target has rival constructions or interpretations that could silently converge too early.
- Pre-register what each outcome means before deployment.
- Each branch is one worker, not one persona. The branch worker runs any personas inline and returns a graded verdict, construction used, confidence, load-bearing assumption, one killing obstruction, and a durable artifact.
- Branches stay mutually blind until they return.
- The orchestrator synthesizes the map, then cross-tests the no-go or adversarial branch against the constructive branches.
- Cross-share only after the first synthesis, then design the next wave.
- If the wave converges to one decisive target, the next pass should be a focused swing, not another broad blind wave.
- Use focused swings for high-cascade gates or shared-context checks where blind fan-out would reload the same assumptions and invite convention drift.

North Star and branch firewall:

- Classify work by directedness, not by certainty of payoff.
- Track 1 is the North Star pursuit: force or falsify the highest-value repo objective. It may be far, uncertain, and open-ended, but it is still exploit because it is controlled by the objective.
- Track 2 is one branch: formalize a byproduct only under explicitly declared postulates, in the form "X given S" without asserting S.
- Track 2 reports up into Track 1. It may supply forced numbers, fixtures, counterexamples, or conditional lemmas, but its finishability never reprioritizes it above Track 1.
- The only legitimate demotion of Track 1 is actual falsification or a computed/argued result that proves it has collapsed into another sharper Track 1 target. Difficulty is not a demotion condition.
- Every wave names its Track 1 objective before naming any Track 2 branch.

Generative re-ranking loop after each wave or parallel batch:

1. The council first reflects inline on what the wave taught: what is missing, what is newly important, and what should be demoted.
2. The council drafts new hypotheses opened by that reflection.
3. Drop resolved, killed, or absorbed items from the live set.
4. Condorcet-vote over the enlarged set of survivors plus new candidates.
5. Re-run `python attention/priority_condorcet.py`.
6. Update `attention_priority`, `open_threads / swing_status`, and `next_action`.

Discipline:

- Honesty above all. NARROWED and FALSIFIED are SUCCESSES, not failures - the whole value is that the loop catches its own wrong guesses. Never manufacture a result; never p-hack a computation toward a wanted answer; if you are choosing a value because it matches a target, stop and say so.
- Research advancement of THIS repo only (no shipping/external/methodology-paper items as council picks).
- One durable, reproducible artifact per swing, committed and pushed.
- Personas always inline, never per-agent.
- No em-dashes in prose.

## open_threads / swing_status

| Item | State | Next admissible swing |
| --- | --- | --- |
| H1 Whole-family completion barrier theorem | Resolved as executable classifier in E165 | Preserve as dependency; do not rerun unless a concrete candidate breaks the classifier or a proof target becomes materially sharper. |
| H2 Pre-action family noncompletion source-action generator | Resolved as bounded formal/local OSAG in E166 | Preserve as dependency; do not promote to physical source action. |
| H7 Completion-aware Adapter_P admission contract | Resolved as admission gate in E167 | Require any boundary, neighbor, or physical packet to pass this gate before use. |
| H5 Multi-holder completion-channel separator | Resolved in E168 | Treat split-holder reversal/fork cost as TaF/readout unless additional H7-admitted source structure is supplied. |
| H9 H1 physical calibration batch | Resolved in E169 | Current CRISPR and Dynamic/Floquet near-misses are absorbed; no physical Adapter_P pass. |
| H6 Internal versus external completion boundary audit | Resolved in E170 | Formal/local OSAG support is bounded conditional form, not external completion language, full internal source structure, or physical Adapter_P passage. |
| H8 D-FORK regime signature bundle | Resolved in E171 | Use as a citation bundle, not a D-FORK decision procedure. |
| T1 Sharper completion-barrier theorem target | Resolved in E172 | The bounded Adapter_P completion-barrier theorem target is ready; universal no-go, physical-source, and D-FORK-decision overclaims are blocked. |
| T2 Mechanize bounded completion-barrier theorem contract | Resolved in E173 | Packaged the bounded contract `bounded_adapter_p_completion_barrier_v1`; no universal no-go, physical-source, or D-FORK-decision claim. |
| T3 T2 counterexample gate validator | Resolved in E174 | Validated the gate with adversarial rows; current near-misses fail, synthetic full control would force revision, and no real packet is found. |
| P1 Real H7-admitted packet intake | Conditional Track 1 | If a real concrete candidate appears, test it through E172/E173 obligations before any claim movement. |
| G2 Distinct T2 contract stressor gate | Conditional support | Select only if it tests the T2 contract in a new way without repeating T3 or broadening the claim. |

Current swing status:

```yaml
latest_material_result: E174 T3 T2 counterexample gate validator
current_gate_state: t2_counterexample_gate_validated_no_real_packet_found
steering_override: wait for a real H7-admitted packet or a distinct T2 contract-testing gate
wave0_started: true
wave0_packet: explorations/E164-research-steering-wave0-starter-2026-07-12.md
wave1_complete: true
wave1_packet: explorations/E165-whole-family-completion-barrier-classifier-2026-07-12.md
wave2_complete: true
wave2_packet: explorations/E166-osag-preaction-family-noncompletion-2026-07-12.md
wave3_complete: true
wave3_packet: explorations/E167-completion-aware-adapter-p-admission-contract-2026-07-12.md
wave4_complete: true
wave4_packet: explorations/E169-h9-physical-calibration-wave-2026-07-12.md
wave5_complete: true
wave5_packet: explorations/E170-h6-completion-boundary-audit-2026-07-12.md
wave6_complete: true
wave6_packet: explorations/E171-h8-d-fork-regime-signature-bundle-2026-07-12.md
wave7_complete: true
wave7_packet: explorations/E172-t1-completion-barrier-theorem-target-2026-07-12.md
wave8_complete: true
wave8_packet: explorations/E173-t2-bounded-completion-barrier-theorem-contract-2026-07-12.md
wave9_complete: true
wave9_packet: explorations/E174-t3-t2-counterexample-gate-validator-2026-07-12.md
active_dependency_boundary: real H7-admitted packet or distinct contract-testing gate
north_star_track: test the bounded contract only with real packet evidence or nonduplicative gate
branch_track: none
formal_local_support_boundary: bounded_conditional_form
d_fork_signature_bundle_reportable: true
bounded_theorem_target_ready: true
bounded_theorem_contract_packaged: true
t2_counterexample_gate_validated: true
real_counterexample_packet_found: false
claim_status_change: none
physical_source_issuance_established: false
```

## next_action

If Joe opens the lane, do not ask him to choose from the card. Run:

```text
python attention/priority_condorcet.py
```

Then hand him the top few items in order with one-line whys.

Default research route:

```text
Post-T3 gate-change wait.
```

Reason: E173 packages the bounded contract and E174 validates the counterexample gate without finding a real packet. Material progress now requires a real concrete H7-admitted packet or a distinct deliberate gate that tests the T2 contract without repeating T3 or broadening the claim.
