---
artifact_type: workflow
workflow_id: W008
status: active
governance_role: research_driver_with_local_minimum_escape
constitutional: false
created_by_run: RUN-0029
---

# W008: Bridge Or Definitive Kill

## Purpose

Run until one of two outcomes is reached:

1. **Bridge found**: A bridge from `Ext_S` to some target observable (energy-momentum or
   otherwise) is constructed, survives adversarial review, passes nontriviality and mechanism
   checks, and is not absorbed by named frameworks.

2. **Definitive kill**: Every identified escape route — across both physics tracks and
   nonstandard realization tracks — has been attempted, every resulting obstruction has been
   confirmed as a genuine global kill (not a local minimum), and N adversarial skeptics have
   failed to find an overlooked route.

**Anti-pattern this workflow exists to prevent**: Killing the bridge because a particular
technical approach hit a wall, without checking whether that wall is a local minimum
specific to the assumptions used, rather than a global obstruction.

**Critical structural point**: BDO and ICO are proofs about a specific target category —
Lorentzian field theory with Noether charges and Poincare symmetry. They do not apply if the
target category changes. Before accepting them as global kills, the workflow must ask whether
the same intuition finds a natural formal home in a different kind of target category — one
where "state becomes real through admissible extension, witness, consensus, or computation"
is already native language. This is the Nonstandard Realization Track (Track B below), and
it must be run before Phase 5 can be reached.

---

## Entry Condition

W008 should be invoked when:

- One or more formal obstructions have been recorded in `memory/path-kills.md`, AND
- The next-trigger plan is pointing toward program closure or archiving, AND
- A systematic escape-route check has not yet been run against those obstructions.

Current entry state (as of RUN-0029): BDO and ICO seal the Poincare-invariant Lorentzian
energy-momentum route from both directions under fixed `(M, eta)` with standard Noether/
Poincare dynamics. Physical interpretation archived to NULL-SURVIVOR. Formal residue kept.

---

## Phase 1: Obstruction Inventory

Load and audit all recorded path kills from `memory/path-kills.md`:

For each kill record, extract:

```yaml
kill_id:
path:
reason_killed:
evidence:
local_minimum_risk: [low / medium / high]
possible_future_resurrection_trigger:
assumptions_used:
  - assumption_1
  - assumption_2
```

Flag any kill with `local_minimum_risk: medium` or higher for the escape-route phase.

**Do not accept kills at face value.** A kill is only as strong as the narrowest assumption
it depends on. The goal of Phase 1 is to make those assumptions explicit.

---

## Phase 2: Escape-Route Enumeration

W008 runs two independent tracks. Both must be exhausted before Phase 5.

**Track A — Physics escape routes**: relax the assumptions within the Lorentzian target
category. These address cases where BDO/ICO apply but may be local minima due to
specific symmetry, dynamics, boundary data, or functoriality choices.

**Track B — Nonstandard realization lenses**: change the target category entirely.
BDO and ICO assume the target is Lorentzian field theory with Noether charges. If the
target changes to a category where "admissible extension" has a native formal home —
sheaf consistency, rigidity, computational irreversibility, consensus finality, proof cost —
then BDO and ICO simply do not apply. These lenses require different nontriviality tests
and different kill conditions.

The two tracks are independent. A kill in Track A does not kill Track B, and vice versa.

---

### Track A: Physics escape-route categories

**Category A — Relax the symmetry assumption**
- Kill uses Poincare invariance → try non-Poincare settings:
  - Curved spacetime (GR, diffeomorphism invariance)
  - Background-independent frameworks (LQG, spin foams, CDT)
  - Topological field theories (TQFT, Chern-Simons) where energy-momentum is not the
    primary conserved quantity

**Category B — Relax the dynamics assumption**
- Kill uses classical on-shell histories → try:
  - Path-integral / quantum amplitude formulation
  - Non-commutative or deformed phase spaces
  - Histories as quantum superpositions (amplituhedron, twistor, positive geometry)

**Category C — Relax the object specification**
- Kill depends on a specific LorHist object structure → try:
  - Categorical dual (morphisms as objects via representable functor)
  - Sheaf-theoretic object specification (objects as sheaves of local data)
  - Derived or ∞-categorical formulation

**Category D — Relax the boundary-data assumption**
- Kill uses Cauchy / full-boundary data objects → try:
  - Holographic / AdS-CFT duality (boundary data is CFT data, not Cauchy data)
  - Asymptotic symmetry groups (BMS, extended BMS, w_{1+inf} algebras)
  - Covariant phase space with degenerate symplectic structure

**Category E — Relax the fixed-background assumption**
- Kill uses fixed external `(M, g)` → try:
  - Source-generated metric (Ext_S determines the metric via some variational principle)
  - Background-independent amplitude where the "metric" emerges from the extension structure

**Category F — Relax the composition-preservation requirement**
- Kill assumes strict functoriality → try:
  - Lax or oplax functors
  - Profunctors / spans / correspondences
  - ∞-functors where composition is only homotopy-coherent

**Category G — Change the target observable**
- Kill shows p^mu is inaccessible → try:
  - Different conserved charges (charge sectors, topological charges, anomaly coefficients)
  - Entanglement entropy as a bridge quantity
  - Asymptotic symmetry charges (soft theorems)

**Category H — Change the source structure**
- Kill assumes Ext_S is a standard category → try:
  - Ext_S as a 2-category or ∞-category
  - Ext_S with additional structure (monoidal, enriched, fibered)
  - Ext_S as an operad or multicategory

For each Track A escape route, record:

```yaml
escape_route_id:
track: A
kill_evaded:
approach:
category: [A / B / C / D / E / F / G / H]
rationale: why this approach might evade the kill
local_minimum_risk_if_killed: [low / medium / high]
verdict: [live / killed / stuck]
```

---

### Track B: Nonstandard Realization Lenses

These lenses ask a different question from Track A. Instead of "can we relax the physics
assumptions to evade BDO/ICO?", they ask: "Does this intuition have a natural formal home
in a completely different kind of target category where energy-momentum is not even the
primary observable?"

For each lens below, run the six standard Track B questions before any kill assessment.

#### Track B Questions (apply to all lenses)

1. **What replaces LorHist?** What is the target category for this lens?
2. **What replaces energy-momentum or mass?** What is the shadow-world observable that Ext_S might control?
3. **What does Ext_S actually control?** What is the natural invariant of admissible extension in this formal home?
4. **What is the shadow-world observable?** What would a witness detect that a non-extended system could not produce?
5. **Does BDO or ICO still apply?** These proofs assume a Lorentzian Noether structure. Is that structure present here? If not, what is the actual obstruction (if any)?
6. **What toy model would distinguish genuine source-side work from relabeling?** Construct the minimal test.

#### Lens B1 — Sheaf / Gluing Consistency

The intuition: `Ext_S` is not selecting a momentum value; it is a gluing/consistency condition
across local observer patches. Matter or structure is what remains coherent under restriction
maps.

- Target category: sheaves on a site (Grothendieck topos); objects are local sections; morphisms are restriction-compatible assignments
- Shadow observable: sheaf cohomology class or gluing obstruction (the thing that fails when extension is not admissible)
- Natural Ext_S role: defines what local data is "admissibly extendable" across patches — determines which sections glue globally
- BDO/ICO applicability: neither applies. BDO assumes Lorentzian Noether charges. ICO assumes Lagrangian dynamics. Neither appears here.
- Key question: does the gluing obstruction carry source-side content that changes across extension rules?

#### Lens B2 — Rigidity / Constraint Satisfaction

The intuition: "matter" is not energy injection but rigidity — a configuration that cannot
deform without violating the extension constraints. Temporal Issuance supplies the constraint
structure; rigidity under those constraints is the physical invariant.

- Target category: constraint graphs or rigidity matroids; objects are configurations; morphisms are constraint-preserving deformations
- Shadow observable: rigidity degree / infinitesimal motion count (Maxwell criterion; count = 0 is rigid)
- Natural Ext_S role: admissible extension adds constraints; the constraint sequence determines whether the resulting configuration is rigid or floppy
- BDO/ICO applicability: neither applies. Rigidity is a graph/algebraic property, not a Lorentzian Noether property.
- Key question: does the admissibility rule generate distinct rigidity classes for same-order / different-Ext_S cases?

#### Lens B3 — Cellular Automata / Coarse-Grained Update Invariant

The intuition: the source side is a rule-based update system; physics is a coarse-grained
shadow invariant that is preserved across different update rules if and only if the admissible
extension structure is equivalent.

- Target category: coarse-graining functors from update rules to macroscopic observables; objects are equivalence classes of rules; morphisms are coarse-graining maps
- Shadow observable: the conserved macroscopic quantity (Wolfram-style computational equivalence class, or Langton's lambda-type invariant)
- Natural Ext_S role: different extension rules → different computational equivalence classes → different coarse-grained invariants
- BDO/ICO applicability: neither applies. These are combinatorial/computational categories, not Lorentzian.
- Key question: can the same-order / different-Ext_S test produce distinguishable coarse-grained invariants?

#### Lens B4 — Database / Indexing / Retrieval Stabilization

The intuition: realization is indexing + retrieval + stabilization under repeated queries. An
entity is "real" in the sense that it is stably retrievable — independent queries return
consistent answers. Admissible extension determines the indexing key structure.

- Target category: query-answer systems or relational schemas; objects are schema types; morphisms are query-preserving schema transformations
- Shadow observable: query consistency / retrieval stability (the thing that breaks when an inadmissible index is queried)
- Natural Ext_S role: defines which key extensions are admissible (maintain retrieval consistency); different rules → different stable-retrieval classes
- BDO/ICO applicability: neither applies. No Lorentzian structure present.
- Key question: does admissibility generate source-side key-extension invariants that cannot be recovered from the schema type (order) alone?

#### Lens B5 — ZK / Proof-Carrying Computation

The intuition: the source side proves admissibility without revealing construction. A valid
proof of admissible extension is the "physical" object; the observable is proof existence and
verifiability, not energy-momentum.

- Target category: proof systems or type theories; objects are propositions/types; morphisms are proof terms / proofs of P → Q
- Shadow observable: proof complexity / verifiability certificate (what a witness checks without seeing the full derivation)
- Natural Ext_S role: defines the admissibility predicate; different rules → different proof complexity classes for the same state transition
- BDO/ICO applicability: neither applies directly, but the notion of "same order" maps to proof derivability and "different invariant" maps to proof complexity class.
- Key question: can two proof terms witnessing the same propositional transition (same <=_S) carry distinct verifiable complexity certificates (different Ext_S invariant)?

#### Lens B6 — Consensus / Avalanche Finality

The intuition: many observers don't create reality; they finalize one branch through
metastable agreement. The source extension rule is the agreement protocol; "mass-energy" is
whatever the finalized branch preserves as an invariant across the quorum.

- Target category: consensus protocols or social choice functions; objects are observer states or ballot profiles; morphisms are vote-aggregation maps
- Shadow observable: the finalized value (the thing all nodes converge to and lock); a branch that failed to finalize has no shadow
- Natural Ext_S role: the extension rule determines which branches achieve quorum; different rules → different finality conditions → different invariants of the finalized branch
- BDO/ICO applicability: neither applies. Consensus finality is a distributed-systems property, not a Lorentzian field-theory property.
- Key question: does the extension admissibility rule determine a conserved quantity of the finalized branch that differs from the null case?

---

For each Track B lens, record:

```yaml
escape_route_id:
track: B
lens: [B1 / B2 / B3 / B4 / B5 / B6]
answers:
  target_category:
  shadow_observable:
  ext_s_role:
  bdo_ico_applicability:
  nontriviality_test:
  toy_model:
verdict: [live / killed / stuck / needs_formalization]
```

---

## Phase 3: Construction Attempt (Per Escape Route)

For each `live` escape route from Phase 2 (either track), run a bounded construction attempt.

### Subagents for Track A attempts

1. **Mathematical builder** — attempt the construction in the target framework
2. **Category Error Auditor** — check whether the constructed object is genuinely new or absorbed
3. **Lorentzian geometer / physicist** — check physical coherence
4. **Covariance checker** — apply the covariance guardrail
5. **Hidden-variable skeptic** — apply the mechanism guardrail

### Subagents for Track B attempts

1. **Domain specialist** (for the relevant lens domain: sheaf theory, rigidity theory, CA theory, database theory, proof complexity, consensus theory)
2. **Category Error Auditor** — is the Ext_S role genuinely new in this category, or is it absorbed?
3. **Nontriviality specialist** — does the source-side distinction survive under the relevant quotient / coarse-graining / consensus operation?
4. **Hidden-variable skeptic** — is the shadow observable secretly bookkeeping?
5. **Cross-lens comparator** — does this construction collapse into one of the existing absorbers (thermodynamics, information theory, causal set theory, time-as-finality)?

### Nontriviality gate (generalized for both tracks)

```text
Take a parallel pair e1, e2 : S => S' with same <=_S, different Ext_S invariant.
The construction must make F(e1) and F(e2) differ on the TARGET OBSERVABLE for this route.
For Track A: the observable is energy-momentum or a related Lorentzian quantity.
For Track B: the observable is defined per-lens (gluing obstruction, rigidity class,
             coarse-grained invariant, retrieval stability, proof complexity, finalized value).
If not distinguishable, classify as bookkeeping.
```

### Outcome per attempt

```yaml
attempt_id:
track: [A / B]
escape_route_id:
construction_found: [yes / no / partial]
target_observable:
nontriviality_gate: [pass / fail / inapplicable]
absorber_comparison: [novel / absorbed_by: ...]
mechanism_check: [pass / fail / inapplicable]
bdo_ico_applicability: [applies / does_not_apply / partially_applies]
verdict: [bridge_candidate / killed / stuck / needs_formalization]
```

---

## Phase 4: Kill Verification (Anti-Local-Minimum Gate)

For each kill from Phase 3, before accepting it:

### Gate questions

1. **Assumption specificity**: Is this kill specific to one or more assumptions that can be
   independently varied? Name each assumption explicitly.
   - For Track A kills: which physics assumptions (Poincare, classical, fixed background, etc.)?
   - For Track B kills: which formal-structure assumptions (site topology, graph connectivity, CA rule class, query type, proof system, consensus protocol type)?

2. **Track coverage check**: Has the kill been tested across BOTH tracks?
   - A kill in Track A (Lorentzian physics) does not kill Track B (nonstandard lenses), and vice versa.
   - A kill in one lens (e.g., B1 sheaf) does not kill other lenses (B2-B6).
   - A "global kill" requires killing all Track A categories AND all Track B lenses independently.

3. **Neighboring-framework check**: Has the analogous construction been attempted in:
   - Time-as-finality (adjacent repo — is the bridge problem solved there in a different form?)
   - Geometric Unity (is GU a live context for any of these?)
   - The specific domain of the Track B lens (sheaf theory community, distributed systems, proof complexity, etc.)?

4. **Prior resurrection check**: Does any prior path-kill record in this repo have a
   `possible_future_resurrection_trigger` that matches the approach just tried?

5. **Adversarial resurrection pass** (N = 3 skeptics minimum):
   Run N independent agents prompted: *"Try to find an escape route this kill missed.
   You are not permitted to accept the kill. Your job is to break it."*
   For Track B kills: at least one skeptic must come from the lens domain, not from physics.
   Record: does any skeptic find a live route?

6. **Local-minimum verdict**: Assign `local_minimum_confirmed: yes / no / uncertain`

If `local_minimum_confirmed: yes` → return to Phase 2 with the new route found.
If `local_minimum_confirmed: uncertain` → flag for human (Joe) review before archiving.
If `local_minimum_confirmed: no` → proceed to Phase 5.

---

## Phase 5: Disposition Gate

Only reached when all escape routes are killed AND all kills pass the anti-local-minimum gate.

### Disposition options

**A — Definitive kill**: The physics bridge from `Ext_S` to Lorentzian energy-momentum is
definitively obstructed. Archive the physical interpretation. Record:
- All obstructions (with their assumption envelopes)
- All escape routes tried (with verdicts)
- Adversarial resurrection pass results
- Surviving formal residue

**B — Program scope revision**: The bridge is not derivable from current `Ext_S` structure
to standard Lorentzian energy-momentum, but a modified or narrower claim survives. Reframe
the program around that claim.

**C — Bridge found**: A construction survived all checks. Promote the relevant claims.
Document the construction fully. Proceed to testability phase (Phase 3, ROADMAP).

**D — Human judgment required**: One or more kills have `local_minimum_confirmed: uncertain`.
Stop and present to Joe before proceeding.

---

## Governance Rules

1. **Do not bypass the anti-local-minimum gate**: Phase 4 is not optional. A kill that
   hasn't passed Phase 4 is tentative, not final.

2. **Record all escape routes attempted**: Even dead ends are informative. Every Category
   A-H route tried, even if killed, should be logged in `memory/path-kills.md` with a
   clear `local_minimum_risk` assessment.

3. **N ≥ 3 adversarial skeptics in Phase 4**: Fewer skeptics create false certainty.
   Skeptics must be genuinely hostile; they may not accept the kill as correct.

4. **Human gate at `local_minimum_confirmed: uncertain`**: The steward cannot independently
   resolve genuine uncertainty about whether a kill is a local minimum. Stop and ask.

5. **Bridge candidate requires promoted claim status**: A construction that passes Phase 3
   but hasn't been through Phase 4 adversarial review is a candidate only — do not promote
   claims until Phase 4 clears it.

6. **Scope of each W008 invocation**: One W008 run = one escape-route category (Track A: A-H)
   or one Track B lens (B1-B6). Do not try all categories in one run; fan out in parallel.

7. **Track B runs before Track A concludes**: Do not declare a global kill based on Track A
   alone. Track B lenses must be attempted (and each killed with its own local-minimum check)
   before Phase 5 is reachable.

---

## Current Escape-Route Status (as of RUN-0029)

### Track A — Physics escape routes

```yaml
BDO (RUN-0028):
  local_minimum_risk: medium
  assumption_used: full-boundary-data LorHist objects
  escape_route_inverted_construction: addressed_by_ICO

ICO (RUN-0029):
  local_minimum_risk: medium
  assumptions_used:
    - Poincare-invariant dynamics on fixed (M, eta)
    - standard Lagrangian field theory Hamiltonian
    - classical completion selection (not quantum superposition)
  escape_routes_not_yet_tried:
    - Category A: non-Poincare / curved spacetime / LQG / spin foams
    - Category B: quantum path-integral / superposition of completions
    - Category D: holographic / AdS-CFT / asymptotic BMS symmetries
    - Category E: source-generated metric
    - Category F: lax functors / oo-functors
    - Category G: non-energy-momentum observables (soft charges, entanglement entropy)
    - Category H: Ext_S as a 2-category or enriched category
  phase_4_anti_local_minimum_gate: NOT_YET_RUN
```

### Track B — Nonstandard realization lenses

```yaml
B1_sheaf_gluing:
  status: not_yet_attempted
  bdo_ico_applicability: does_not_apply
  priority: high

B2_rigidity_constraint:
  status: not_yet_attempted
  bdo_ico_applicability: does_not_apply
  priority: high

B3_cellular_automata_coarse_graining:
  status: not_yet_attempted
  bdo_ico_applicability: does_not_apply
  priority: medium

B4_database_indexing_retrieval:
  status: not_yet_attempted
  bdo_ico_applicability: does_not_apply
  priority: medium

B5_zk_proof_carrying_computation:
  status: not_yet_attempted
  bdo_ico_applicability: partially_applies_at_complexity_level
  priority: high

B6_consensus_avalanche_finality:
  status: not_yet_attempted
  bdo_ico_applicability: does_not_apply
  priority: high

phase_4_anti_local_minimum_gate_for_any_track_b_lens: NOT_YET_RUN
```

### Priority recommendation for next W008 invocations

**Track A starting point**: Category G (soft theorem / asymptotic symmetry charges) — BMS
symmetry groups are a known setting where boundary data does not fix all conserved charges,
which is exactly the gap BDO and ICO exploit.

**Track B starting point**: B1 (sheaf/gluing) and B6 (consensus/finality) in parallel —
both are settings where "state becomes real through admissible extension" is already native
language, and neither BDO nor ICO applies. These are most likely to reframe the obstruction
rather than merely evade it.

**Key insight for Track B**: BDO and ICO may kill the bridge only when the target is ordinary
Lorentzian energy-momentum. They do not kill bridges where the shadow invariant is rigidity
(B2), consensus finality (B6), proof cost (B5), gluing obstruction (B1), computational
irreversibility (B3), or coarse-grained update energy (B3). These are heterodox openings,
not physics escapes.

---

## Invocation

W008 is invoked from W000 when `NEXT-TRIGGER-PLAN.md` recommends bridge-or-definitive-kill
work. The steward reads the "Current Escape-Route Status" section above (updated by each run)
and picks the next route.

After each run:
- Update the escape-route status table above with the new verdict
- Append to `memory/path-kills.md` if a new kill is recorded
- Update `CLAIM-LEDGER.md` if claim status changes
- Update `agent-governance/NEXT-TRIGGER-PLAN.md` with the next escape route to attempt

W008 terminates when the disposition gate (Phase 5) is reached and one of A-D is recorded.
