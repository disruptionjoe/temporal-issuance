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

1. **Bridge found**: A physics bridge from `Ext_S` to Lorentzian energy-momentum is
   constructed, survives adversarial review, passes covariance and mechanism checks, and is
   not absorbed by named frameworks.

2. **Definitive kill**: Every identified escape route has been attempted, every resulting
   obstruction has been confirmed as a genuine global kill (not a local minimum), and N
   adversarial skeptics have failed to find an overlooked route.

**Anti-pattern this workflow exists to prevent**: Killing the bridge because a particular
technical approach hit a wall, without checking whether that wall is a local minimum
specific to the assumptions used, rather than a global obstruction.

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

For each kill flagged in Phase 1, generate a systematic list of escape routes:

### Standard escape-route categories

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

For each escape route, record:

```yaml
escape_route_id:
kill_evaded:
approach:
category: [A / B / C / D / E / F / G / H]
rationale: why this approach might evade the kill
local_minimum_risk_if_killed: [low / medium / high]
verdict: [live / killed / stuck]
```

---

## Phase 3: Construction Attempt (Per Escape Route)

For each `live` escape route from Phase 2, run a bounded construction attempt:

### Subagents for each attempt

1. **Mathematical builder** — attempt the construction in the target framework
2. **Category Error Auditor** — check whether the constructed object is genuinely
   new or is absorbed by a known framework
3. **Lorentzian geometer / physicist** — check physical coherence
4. **Covariance checker** — apply the covariance guardrail
5. **Hidden-variable skeptic** — apply the mechanism guardrail

### Nontriviality gate (inherited from RUN-0027, applied per attempt)

```text
Take a parallel pair e1, e2 : S => S' with same <=_S, different Ext_S invariant.
The construction must make F(e1) and F(e2) differ on the target observable.
If not, classify as bookkeeping.
```

### Outcome per attempt

```yaml
attempt_id:
escape_route_id:
construction_found: [yes / no / partial]
covariance_check: [pass / fail / inapplicable]
mechanism_check: [pass / fail / inapplicable]
absorber_comparison: [novel / absorbed_by: ...]
nontriviality_gate: [pass / fail / inapplicable]
verdict: [bridge_candidate / killed / stuck]
```

---

## Phase 4: Kill Verification (Anti-Local-Minimum Gate)

For each kill from Phase 3, before accepting it:

### Gate questions

1. **Assumption specificity**: Is this kill specific to one or more assumptions that can be
   independently varied? Name each assumption explicitly.

2. **Neighboring-framework check**: Has the analogous construction been attempted in:
   - Time-as-finality (adjacent repo — is the bridge problem solved there in a different form?)
   - Geometric Unity (is GU a live context for any of these?)
   - Causal set theory, spin foam models, or other discrete-spacetime frameworks?

3. **Prior resurrection check**: Does any prior path-kill record in this repo have a
   `possible_future_resurrection_trigger` that matches the approach just tried?

4. **Adversarial resurrection pass** (N = 3 skeptics minimum):
   Run N independent agents prompted: *"Try to find an escape route this kill missed.
   You are not permitted to accept the kill. Your job is to break it."*
   Record: does any skeptic find a live route?

5. **Local-minimum verdict**: Assign `local_minimum_confirmed: yes / no / uncertain`

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

6. **Scope of each W008 invocation**: One W008 run = one escape-route category (A-H) or
   a small cluster of closely related routes. Do not try all categories in one run; fan out.

---

## Current Escape-Route Status (as of RUN-0029)

```yaml
BDO (RUN-0028):
  local_minimum_risk: medium
  assumption_used: full-boundary-data LorHist objects
  escape_route_inverted_construction: addressed_by_ICO

ICO (RUN-0029):
  local_minimum_risk: unknown
  assumptions_used:
    - Poincare-invariant dynamics on fixed (M, eta)
    - standard Lagrangian field theory Hamiltonian
    - classical completion selection
  escape_routes_not_yet_tried:
    - Category A: non-Poincare / curved spacetime / LQG
    - Category B: quantum path-integral / superposition of completions
    - Category D: holographic / AdS-CFT / asymptotic BMS symmetries
    - Category E: source-generated metric
    - Category F: lax functors / oo-functors
    - Category G: non-energy-momentum observables (soft charges, entanglement entropy)
    - Category H: Ext_S as a 2-category or enriched category
  phase_4_anti_local_minimum_gate: NOT_YET_RUN
```

The next W008 invocation should pick the highest-leverage escape route and attempt it.
Recommended starting point: Category G (soft theorem / asymptotic symmetry charges) because
BMS and related asymptotic symmetry groups are a known setting where boundary data *does not*
fix all conserved charges — which is exactly the gap both BDO and ICO exploited.

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
