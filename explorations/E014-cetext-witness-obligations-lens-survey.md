---
artifact_type: exploration
exploration_id: E014
status: active
governance_role: cetext_witness_obligations_lens_survey
source_run: RUN-0036
claim_refs:
  - TI-C007
  - TI-C008
  - TI-C013
  - TI-C016
---

# E014: CelExt as Boundary Witness Obligations Across Heterodox Lenses

## Introduction: The Witness Obligation Reframing

The previous runs established a conditional result: a physics bridge to BMS soft-charge structure
exists if and only if `ExtCat` is upgraded to `CelExt`, a celestial boundary category with three
independent legs — boundary objects, BMS-covariant morphisms, and a source-side Noether charge
`Q_f` that does not presuppose bulk radiative phase-space data. The question that remained open
was: what is `CelExt`?

This exploration reframes the question. Instead of asking "can Temporal Issuance derive BMS
physics?", we ask:

> What witness obligations survive projection to a boundary, and can those obligations generate
> a nontrivial celestial category?

**Formal setup.** For an admissible extension `e: S -> S'` in a typed source system `(C, <=_S, Ext_S)`,
define a **witness obligation** `W(e)` as a carried requirement — not merely a state of the system
after the extension, but a specification of what must remain demonstrably valid after transport,
projection, forgetting, reconciliation, or finalization. A witness obligation is a morphism-level
invariant that travels with the extension and that a downstream boundary observer could in principle
verify without access to the full bulk trajectory.

**Nontriviality gate.** For every lens, construct a parallel pair:

```
e1, e2 : S => S' with the same induced order (e1 ~_{<=_S} e2)
but different witness obligation W(e1) ≠ W(e2).
```

Ask: is there a boundary observable `O` such that `O(proj(e1)) ≠ O(proj(e2))`?

- If no such `O` exists: the boundary cannot detect the distinction — **bookkeeping**.
- If `O` distinguishes them only by importing known target-side physics: **absorbed**.
- If `O` distinguishes them via independently motivated source-side content: **nontrivial**.

A `live` verdict requires the nontriviality gate to pass without importing target physics. This
is a high bar. Most lenses are expected to be `conditional-live`, `absorbed`, or `bookkeeping`.

---

## Lens Survey

---

### B1 — Sheaf/Gluing

**1. Target category.**
The formal category is `Sh(S², Open)`, the category of sheaves on the sphere `S²` with the
standard open-cover topology. Objects are sheaves of source constraint data over patches of `S²`;
morphisms are restriction-compatible sheaf maps. This replaces the Lorentzian history target:
instead of histories in a manifold, we work with gluing-consistent local sections over the
two-sphere.

**2. Witness obligation definition.**
For an admissible extension `e: S -> S'`, `W(e)` is the local section consistency requirement:
every open cover `{U_i}` of `S²` must admit a consistent local section assignment `sigma_i` on
each patch that restricts compatibly on overlaps `U_i ∩ U_j`, and this assignment must survive the
extension. Formally, `W(e)` is the requirement that the Čech cocycle `{sigma_i|_{U_i ∩ U_j}} ∈ H¹({U_i}, F_e)`
is trivial (coboundary), where `F_e` is the sheaf of constraint data after extension `e`.

**3. Boundary projection map.**
Project: `proj(e) = (F_e, {sigma_i})`, the sheaf together with the local section assignment induced
by the extension. Two extensions with the same induced order `e1 ~_{<=_S} e2` may induce different
Čech cohomology classes `[c_e1] ≠ [c_e2] ∈ H¹({U_i}, F)` if they produce different gluing
obstructions over `S²`.

**4. Shadow observable.**
Boundary witness: the Čech cohomology class `[c_e] ∈ H¹(S², F)`. A boundary observer who can
assemble local section data from `S²` but not access the bulk can detect whether a consistent
global section exists. Non-vanishing Čech cohomology is a boundary-detectable obstruction.

**5. Nontriviality test.**
Parallel pair: Let `S = {p, q}` with `p <=_S q`. Define:
- `e1: S -> S' = {p, q, r}` extending by adding `r` with `p <=_S r` and requiring local sections
  on `U_1, U_2` to agree on `r` in the overlap — no gluing obstruction. `[c_{e1}] = 0`.
- `e2: S -> S'` same underlying order but assigning different local section data on `U_1 ∩ U_2`
  — a non-coboundary cocycle. `[c_{e2}] ≠ 0`.

The boundary observable `O = H¹(S², F)` detects this. Same order; different witness obligation;
different Čech cohomology class. The question is whether the different local section data is
independently motivated by source-side structure or imported from a target sheaf theory. If the
constraint structure `C` already determines which sections are admissible, this is source-side.
If the section assignment requires knowing what target the sheaf represents, it is absorbed.

**6. Failure mode.**
The most likely collapse is: the section assignment is absorbed by standard Čech/sheaf cohomology
theory, which applies to any presheaf and requires no Temporal Issuance content. The obstruction
class `[c_e]` is a topological invariant of the section data, not of the extension rule. If
`C`-typed constraints determine the section assignment independently, the result is nontrivial.
If they merely parameterize a standard sheaf, it is bookkeeping.

**7. Best toy model.**
Two-patch cover of `S¹` (simpler stand-in for `S²`). `U_1 = (0, 2π)`, `U_2 = (π, 3π) mod 2π`,
overlap is two arcs. `F_e(U_i)` = set of constraint-valid states on that patch. `e1` assigns
compatible states; `e2` assigns states that differ on overlaps by a non-trivial twist. The
transition function is the Čech cocycle. This is directly computable in two states and two patches.

**8. Verdict.**
`conditional-live`. The parallel pair exists and the boundary observable is the Čech cohomology
class, which is not manifestly `p^mu` or `Q_f` imported from Lorentzian physics. However,
whether the section assignment is genuinely source-side (typed constraint-driven) or merely sheaf
bookkeeping depends on whether `C` constrains the overlap data independently. A formal fixture
requires specifying what `C`-typed constraints say about local section compatibility on `S²`.

---

### B2 — Rigidity/Constraint

**1. Target category.**
The formal category is `RigMat`, with objects being constraint graphs `G = (V, E, d)` where `V`
is a set of constrained source states, `E` edges are admissibility relations, and `d: E -> {0,1,...,k}`
is a constraint multiplicity or degree assignment. Morphisms are graph homomorphisms preserving
the admissibility predicate. This replaces `LorHist` with a combinatorial constraint target.

**2. Witness obligation definition.**
For an admissible extension `e: S -> S'`, `W(e)` is the constraint preservation requirement:
the extension must preserve the Maxwell rigidity count `f = 3|V| - |E|` (in 2D; adjusted for
dimension) or more precisely the rank condition `rank(R_e) = k` of the rigidity matrix `R_e`
constructed from the extended constraint system. The obligation is the rank invariant — what
the extension must carry to remain mechanically admissible.

**3. Boundary projection map.**
Project: `proj(e) = rank(R_e)`, the rank of the rigidity matrix after extension. Extensions
with the same induced order can differ in rigidity rank if they add constraints of different
strength or create different dependency structures.

**4. Shadow observable.**
Boundary observable: `rank(R_e)` or equivalently the Maxwell count `f = d|V| - |E| - d(d+1)/2`
in dimension `d`. A boundary observer who can enumerate the degrees of freedom and constraints
(without accessing internal bulk trajectories) can detect rigidity degree.

**5. Nontriviality test.**
Parallel pair: Three nodes `{a, b, c}` with `a <=_S b <=_S c` (same induced order for both
extensions).
- `e1` adds a single constraint edge `(a,b)` — rank of `R_{e1}` = 1, Maxwell count = `3·3 - 1 = 8`.
- `e2` adds two constraint edges `(a,b)` and `(b,c)` — rank of `R_{e2}` = 2 (if independent),
  Maxwell count = `3·3 - 2 = 7`.

Same induced source order `a <=_S b <=_S c`; different constraint structure; different rigidity
rank. The boundary observable `O = rank(R_e)` distinguishes `e1` from `e2`. This parallel pair
is executable.

**6. Failure mode.**
Rigidity rank is a property of the constraint graph, not of Temporal Issuance specifically.
The witness obligation `W(e) = rank(R_e)` is a well-studied invariant in combinatorial geometry
and structural engineering. The most likely collapse mode: rigidity matroids absorb this
completely — the boundary observable is a matroid rank, defined for any graph and requiring no
source-category content. `C`-typed constraints might just be edges in a constraint graph, making
this pure matroid theory.

**7. Best toy model.**
Three-node planar constraint graph with varying edge sets. The Maxwell count is directly
computable. Two extensions of the same base order that add different edge sets have measurably
different rigidity degrees. This is the standard minimal example from structural engineering.

**8. Verdict.**
`bookkeeping`. The rigidity rank is a combinatorial invariant of the constraint graph that is
fully absorbed by matroid theory and Maxwell counting. It does not require source-category
extension structure; it applies to any graph of constraints. The parallel pair is technically
valid but the boundary observable is entirely captured by standard matroid/rigidity theory.
There is no residue that requires or motivates Temporal Issuance specifically.

---

### B3 — Cellular Automata/Wolfram

**1. Target category.**
The formal category is `CoarseCA`, with objects being equivalence classes of update-system
configurations under a coarse-graining functor `Phi: CA_States -> CoarseStates`, and morphisms
being coarse-grained update maps. The Wolfram computational universe is the background: each
configuration has a computational equivalence class under a rule-space coarse-graining.

**2. Witness obligation definition.**
For an admissible extension `e: S -> S'`, `W(e)` is the computational equivalence class
`[R(e)] ∈ Rule_equiv` that the extension belongs to under coarse-graining — specifically the
property that the extension's update rule maps to the same or a compatible coarse-grained rule.
The obligation is: after coarse-graining, the extension must still be in a computable class
and the coarse-grained update must be distinguishable from the null update.

**3. Boundary projection map.**
`proj(e) = Phi(e)`, the coarse-grained update class. Two extensions with the same source order
can map to different coarse-grained rules if their local update behaviors differ.

**4. Shadow observable.**
Boundary observable: the coarse-grained rule class `Phi(e)`, or in the Wolfram classification,
the Wolfram class (I/II/III/IV) of the coarse-grained dynamics. A boundary observer who can run
the coarse-grained update but not the fine-grained extension sees the coarse rule class.

**5. Nontriviality test.**
Parallel pair: Two extensions of a base automaton state with the same induced ordering on source
cells but different local update rules — one producing periodic behavior (Wolfram Class II) and
one producing chaotic behavior (Wolfram Class III). Same induced order on the state lattice;
different coarse-grained rule class; different boundary observable.

The challenge: whether the Wolfram class is genuinely source-side or whether it requires knowing
what class the target system belongs to (target physics import). The Wolfram class of a rule is
a property of the rule itself — it can in principle be determined from the rule definition without
external reference. This suggests source-side independence.

**6. Failure mode.**
Two likely failure modes. First, Wolfram class assignment requires simulating the rule to
arbitrary time, which is computationally intractable and requires knowing what the rule computes
over time — this is effectively target-side (the class depends on the long-run dynamics, not just
the extension rule itself). Second, the parallel pair distinction (Class II vs Class III) is
absorbed by computational complexity theory and automata theory, both of which predate and do not
require Temporal Issuance.

**7. Best toy model.**
Two one-dimensional CA rules: Rule 4 (Wolfram Class I) and Rule 30 (Wolfram Class III), both
defined on the same state space `{0,1}^Z`. Same induced order on the cell lattice; different
coarse-grained dynamics; different Wolfram class. The boundary observer sees only the coarse-grained
pattern and can distinguish them.

**8. Verdict.**
`bookkeeping`. The Wolfram class is a well-characterized property of update rules, independent
of Temporal Issuance content. The parallel pair is formally valid (same order, different coarse
class, distinguishable boundary observable) but the boundary observable is absorbed by automata
theory. No residue is independently motivated by source-category extension structure.

---

### B4 — Database/Indexing

**1. Target category.**
The formal category is `RelSchema`, with objects being relational schemas `Sigma = (R, FD, IC)`
where `R` is a relation set, `FD` is a set of functional dependencies, and `IC` is a set of
integrity constraints. Morphisms are schema mappings preserving constraint satisfaction.
Extensions correspond to adding new tuples or schema elements while maintaining constraint integrity.

**2. Witness obligation definition.**
For an admissible extension `e: S -> S'`, `W(e)` is the stable retrieval constraint: for every
query `Q` expressible in the schema `Sigma_S`, the answer `Q(S')` after extension must be
consistent with `Q(S)` under the admissibility predicate — specifically, the extension must
not violate functional dependencies or integrity constraints in a way that makes an existing
consistent query inconsistent. The obligation is a stability certificate for the query interface.

**3. Boundary projection map.**
`proj(e) = (FD_e, IC_e)`, the functional dependency set and integrity constraint set after
extension. A boundary observer with only the schema (not the data) can read off the constraint
profile. Two extensions with the same induced order can have different `FD_e` sets (different
functional dependencies emerge from the added tuples).

**4. Shadow observable.**
Boundary observable: the set of functional dependencies `FD_e` or equivalently the Armstrong
axiom closure of the schema after extension. This is a schema-level invariant detectable without
access to the full tuple content.

**5. Nontriviality test.**
Parallel pair: Base schema with attributes `{A, B, C}` and dependency `A -> B`.
- `e1`: add tuple `(a1, b1, c1)` — after extension `FD_e1 = {A -> B}` still (no new FD implied).
- `e2`: add tuple `(a1, b1, c2)` and `(a1, b2, c1)` — creates violation then repair, ultimately
  adding `A -> BC` as an emergent dependency. `FD_e2 = {A -> B, A -> C}`.

Same base order (same tuple sequence); different witness obligation (different functional dependency
set survives); different boundary observable (Armstrong closure differs).

**6. Failure mode.**
The functional dependency set is a property of the relational schema that is absorbed by database
normalization theory (Armstrong axioms, BCNF, etc.). The boundary observable `FD_e` is well
defined and entirely captured by relational algebra. No Temporal Issuance content is required.
The most likely collapse: the extension rule is just tuple insertion, and the FD tracking is
pure relational database theory.

**7. Best toy model.**
Three-attribute schema `{A, B, C}` with one initial FD. Two tuple insertions of the same base
relation that induce different FD closures. The Armstrong axiom closure of each is directly
computable and the two schemas are distinguishable by a boundary observer who can only see the
schema, not the data.

**8. Verdict.**
`bookkeeping`. The boundary observable (FD set / Armstrong closure) is absorbed by standard
relational database theory. The parallel pair is valid but the distinction requires no
Temporal Issuance content. A boundary observer who knows relational database theory can detect
the distinction without any reference to source-side admissibility structure.

---

### B5 — ZK/Proof-Carrying

**1. Target category.**
The formal category is `ProofSys`, with objects being type-theoretic contexts `Gamma` (a list of
typed assumptions) and morphisms being proof terms `pi: Gamma |- phi` (proofs of propositions
`phi` in context `Gamma`). Extensions correspond to adding new axioms or proof obligations to
the context. This is the Curry-Howard correspondence formulation: extensions are admissible
derivations that preserve proof-theoretic consistency.

**2. Witness obligation definition.**
For an admissible extension `e: S -> S'`, `W(e)` is the admissibility proof certificate: a
proof term `pi_e` that witnessing the admissibility of `e` is itself a valid derivation in the
proof system, and that the extended context `Gamma_{S'}` does not introduce a proof of `⊥`
(contradiction). The obligation is the certificate that the extension is consistent and
admissible — a carried proof of non-contradiction.

**3. Boundary projection map.**
`proj(e) = size(pi_e)`, the proof complexity of the admissibility certificate. Alternatively,
`proj(e) = class(pi_e)` where class is the proof complexity class (polynomial vs. exponential
vs. unprovable). A boundary verifier who can check proofs but not generate them sees the
complexity class.

**4. Shadow observable.**
Boundary observable: proof complexity class or verification residue — specifically, the size
of the shortest proof of admissibility for extension `e`. Two extensions with the same induced
order can have admissibility certificates of different complexity.

**5. Nontriviality test.**
Parallel pair: Two extensions of a base context `Gamma` with the same logical consequence order
on propositions (same induced `<=_S`) but different admissibility proofs:
- `e1`: adds axiom `A -> B` to context; admissibility proof is trivial (axioms are always
  admissible). `|pi_{e1}|` = O(1).
- `e2`: adds derived theorem `T` that follows from a long chain; admissibility proof requires
  the full derivation. `|pi_{e2}|` = O(n) for some large `n`.

Same implication order on propositions; different certificate complexity; the boundary verifier
detects the size of the proof needed. This is technically valid.

**6. Failure mode.**
Proof complexity is absorbed by proof complexity theory (circuit complexity, proof length bounds,
IP = PSPACE results, etc.). The proof complexity class of an admissibility certificate is a
well-studied object in computational logic. More critically: whether a derivation is admissible
in a proof system is a metalogical question that requires knowing the proof system's rules —
i.e., the target logic. If the target logic is not independently derived from `C`-typed
constraints, this imports target-side content (the proof system itself is the target physics
analogue).

**7. Best toy model.**
Propositional logic context with two extensions: one adds an axiom (trivial certificate), one
adds a derived theorem requiring a long proof. The proof sizes are measurably different and
the boundary verifier can distinguish them by checking proof length.

**8. Verdict.**
`conditional-live`. The parallel pair is valid and the boundary observable (proof complexity
class) is not manifestly `p^mu` or `Q_f` imported from Lorentzian physics. The failure risk
is that proof systems and complexity classes are entirely absorbed by proof theory and
computational complexity — but the admissibility certificate for an extension of a typed
constraint system `C` is potentially a novel object if `C`-typed admissibility differs from
standard logical admissibility. This requires a formal specification of what makes an
admissibility proof for `Ext_S` distinct from ordinary proof-theoretic admissibility. Without
that specification, the result is bookkeeping.

---

### B6 — Consensus/Finality

**1. Target category.**
The formal category is `ConsFin`, with objects being protocol states `(chain, votes, finalized_prefix)`
and morphisms being valid state transitions under a finality protocol (e.g., Avalanche-style:
a transition is admissible if it achieves the required confidence threshold on a branch). The
extension `e: S -> S'` adds a new block or decision to the protocol state.

**2. Witness obligation definition.**
For an admissible extension `e: S -> S'`, `W(e)` is the branch finalization obligation: a
record of which branches have been finalized (irreversibly committed) by the protocol after
extension `e`, and what value was finalized on each branch. This is carried because downstream
participants need to know which commitment is permanent. `W(e) = (branch_id, finalized_value,
round_number)`.

**3. Boundary projection map.**
`proj(e) = {(branch_id, finalized_value)}` — the set of finalized branches and their committed
values, readable from the protocol's finality certificate without replaying the full history.
Two extensions with the same induced order (same causal precedence structure on blocks) can
differ in which value was finalized on a contested branch.

**4. Shadow observable.**
Boundary observable: `finalized_value(branch_id)` — the committed value on a given branch
after extension `e`. In a fork-choice-rule finality system, this is the invariant that boundary
participants read from the finality certificate.

**5. Nontriviality test.**
Parallel pair: Base protocol state with two contested branches `B_1` and `B_2`, each with the
same causal depth (same induced order in the DAG).
- `e1`: votes accumulate to finalize `B_1` with value `v_1`. `W(e1) = (B_1, v_1)`.
- `e2`: votes accumulate to finalize `B_2` with value `v_2 ≠ v_1`. `W(e2) = (B_2, v_2)`.

Same DAG order structure; different finalization obligation; different boundary observable.
The boundary participant reads the finalized value and sees `v_1 ≠ v_2`.

**6. Failure mode.**
Finalized values are properties of the consensus protocol and the vote distribution, not of
source-category extension structure. The boundary observable `finalized_value(branch_id)` is
determined by the vote distribution — which is target-side input (the votes are the dynamics).
The extension rule `Ext_S` has no independent role unless typed constraints determine which
branch accumulates votes. If they do, the vote distribution is parametrized by source-side
content — but this is equivalent to importing voting dynamics as the target physics.

**7. Best toy model.**
Two-branch Avalanche-style protocol with 5 validators and two competing values `{0, 1}`. Both
branches have the same DAG depth (same induced order). In `e1`, validators favor branch 1;
in `e2`, branch 2. Final committed values differ. The boundary finality certificate is directly
inspectable and distinguishes the two extensions.

**8. Verdict.**
`absorbed`. The fork-choice outcome depends on vote distribution, which is target-side protocol
dynamics. The `Ext_S` rule has no independent mechanism to determine which branch is finalized
without importing the voting dynamics. The parallel pair is valid structurally but the boundary
observable difference is determined by target-side data (votes), not source-side constraint
extension structure. This is the consensus analogue of ICO: the selection among competing
branches falls to target-side dynamics, not source-side admissibility rules.

---

### B7 — Agent Orchestration/Memory

**1. Target category.**
The formal category is `AgentMem`, with objects being agent memory states `M = (task_graph, commitments, context_window, deformation_log)` and morphisms being admissible task dispatches `d: M -> M'` that extend the task graph while preserving outstanding commitments and future-admissibility conditions. An extension `e: S -> S'` is a task dispatch that adds new obligations to the agent's memory state.

**2. Witness obligation definition.**
For an admissible extension `e: S -> S'`, `W(e)` is the persistent future-admissibility deformation:
a record of how the extension deforms the space of future admissible dispatches — specifically,
which future tasks are now obligated, which are excluded, and which are deformed in priority by
the memory state created by `e`. Formally, `W(e) = delta_{Adm}(e)` where `delta_{Adm}(e)` is the
change in the admissibility predicate for future extensions induced by committing to `e`.

**3. Boundary projection map.**
`proj(e) = (commitments_e, excluded_future_tasks_e)` — the set of inherited commitments and
exclusions visible to a downstream agent that reads only the handoff state, not the full
task history. Two extensions with the same task order can produce different commitment/exclusion
profiles if they involve tasks with different side effects on future admissibility.

**4. Shadow observable.**
Boundary observable: the inherited commitment residue `commitments_e` — the set of active
obligations carried forward after extension `e`, visible to any downstream agent reading the
context handoff. This is observable without replaying the full task history.

**5. Nontriviality test.**
Parallel pair: Base agent state with two pending tasks `{T_a, T_b}` in the same priority order
(`T_a <=_S T_b`).
- `e1`: dispatch `T_a` first; `T_a` creates a commitment `C_1` that excludes `T_c` in the
  future. `commitments_{e1} = {C_1}`.
- `e2`: dispatch `T_b` first; `T_b` creates a different commitment `C_2` that excludes `T_d`.
  `commitments_{e2} = {C_2}`.

Same priority order; different dispatch sequence; different commitment residue; downstream agent
sees different inherited obligations.

**6. Failure mode.**
The commitment residue is a property of the task graph dynamics — which tasks exclude which
future tasks. This is determined by the task definitions (target-side content: what each task
does when executed). The `Ext_S` rule has no independent mechanism to determine commitment
exclusion patterns without knowing what the tasks do. Absorbed by task-graph theory and
multi-agent planning systems.

**7. Best toy model.**
Two-task agent with explicit exclusion rules: `dispatch(T_a) -> excludes(T_c)`,
`dispatch(T_b) -> excludes(T_d)`. Same priority ordering `T_a <= T_b`. Two extensions differ
by dispatch sequence; commitment residues differ; downstream agent distinguishes them via the
handoff state. This is directly executable in a minimal planning system.

**8. Verdict.**
`bookkeeping`. The commitment residue is determined by task semantics (target-side), not
source-side extension rules. The parallel pair is structurally valid but the distinction is
absorbed by multi-agent planning theory. The witness obligation `W(e) = delta_{Adm}(e)` is
interesting as a formalism but does not require Temporal Issuance content — it applies to any
system where tasks modify future admissibility.

---

### B8 — Celestial/BMS Physics

**1. Target category.**
The formal category is `CelExt`, the candidate celestial boundary category defined in E013:
objects are boundary source states `B = (Sigma, H, sector, constraints)` on `S²`; morphisms are
admissible boundary insertions or kernel maps `phi: B -> B'` changing the soft-charge sector;
composition is given by operator product or OPE gluing on `S²`. BMS acts on this category as a
boundary symmetry group.

**2. Witness obligation definition.**
For an admissible extension `e: B -> B'`, `W(e)` is the boundary soft-memory obligation: a
record of the soft-charge shift `delta Q_f(e) = Q_f(B') - Q_f(B)` induced by the extension,
where `Q_f` is computed from the boundary current algebra or symplectic structure of `CelExt`
— without importing the bulk Hamiltonian or the bulk radiative phase-space definition of `Q_f`.
The obligation is: the charge shift must be computable from boundary data alone.

**3. Boundary projection map.**
`proj(e) = delta Q_f(e)` — the boundary soft-charge shift induced by the extension, computed
from boundary current algebra without bulk input. Two extensions with the same boundary ordering
(same induced `<=_{CelExt}`) can have different charge shifts if they correspond to different
soft-charge sectors on `S²`.

**4. Shadow observable.**
Boundary observable: `delta Q_f(e)` — detectable by a boundary CFT observer who measures the
Noether charge of the BMS current on `S²`. This is directly analogous to the soft charge in
celestial holography but defined from the boundary side.

**5. Nontriviality test.**
Parallel pair: Two boundary insertions `phi_1, phi_2: B -> B'` with the same boundary ordering
(same induced order on boundary operator insertions) but different soft-charge sectors:
- `phi_1` inserts a soft graviton in sector `s_1`; `delta Q_f(phi_1) = q_1`.
- `phi_2` inserts a soft graviton in sector `s_2 ≠ s_1`; `delta Q_f(phi_2) = q_2 ≠ q_1`.

The boundary CFT observer detects `q_1 ≠ q_2`. This is the most physically grounded parallel
pair in the survey. The nontriviality test passes — provided `Q_f` is computed from the boundary
current algebra without importing bulk radiative phase-space data.

The precise conditional: if the boundary current algebra is independently specified (not derived
by reduction from the bulk), then `delta Q_f(e)` is source-side relative to `CelExt`. The
absorption risk: if defining `Q_f` on the boundary requires knowing the bulk stress-energy
tensor or the Bondi news tensor, then it imports bulk physics and is absorbed.

**6. Failure mode.**
Two failure modes. First: absorbed — if every definition of `Q_f` on `CelExt` ultimately requires
bulk data (the boundary stress tensor Noether charge requires knowing the bulk action, or the
symplectic structure requires the Bondi news). Second: blocked — if `CelExt` does not yet have
a sufficiently independent specification to define `Q_f` without bulk input; celestial holography
is not yet a completed boundary CFT for all flat-space gravity.

**7. Best toy model.**
Scalar celestial amplitude with two different soft insertions in the same collinear limit (same
conformally mapped ordering on `S²`). The Weinberg soft theorem gives different soft-charge
shifts for different soft particles. A boundary `S²` observer who measures the soft factor can
distinguish the two insertions without accessing the bulk scattering amplitude. This is a
partial toy model for the parallel pair — but the soft factor in the Weinberg theorem is derived
from bulk scattering, so it is absorbed unless a genuinely boundary-intrinsic definition is used.

**8. Verdict.**
`conditional-live`. This is the highest-quality lens for the physics bridge. The parallel pair
is most concretely motivated, the boundary observable is physically meaningful, and the charge
shift `delta Q_f(e)` is the closest thing in this survey to an independently motivated CelExt
boundary observable. The result is conditional on: (a) `CelExt` having an independent boundary
specification, and (b) `Q_f` being computable from that boundary specification without bulk
input. If both conditions are met, this lens gives a genuine nontrivial boundary witness. If
either fails, the result is absorbed.

---

### B9 — Holonomy/Gauge

**1. Target category.**
The formal category is `BunConn`, with objects being principal `G`-bundles `P -> S²` with
connection `A` over the base `S²`, and morphisms being bundle maps preserving the connection
(i.e., gauge-equivalent maps). Extensions `e: S -> S'` correspond to adding or modifying
connection data around loops on `S²`. The holonomy group of the connection is the structural
invariant.

**2. Witness obligation definition.**
For an admissible extension `e: S -> S'`, `W(e)` is the parallel transport residue around the
extension loop: `Hol_A(gamma_e) ∈ G` where `gamma_e` is the loop in `S²` induced by the
extension `e` (the path traced by adding the new constraint and returning to the base point).
The obligation is: the holonomy around the loop induced by the extension must be computable
from the connection data inherited by the extension, without importing a separate curvature
or field strength from target physics.

**3. Boundary projection map.**
`proj(e) = Hol_A(gamma_e) mod gauge` — the holonomy class in the gauge group `G`, modulo gauge
equivalence (a conjugacy class in `G`). This is the Wilson loop analogue: a boundary observer
who can measure holonomies but not local gauge fields sees the conjugacy class.

**4. Shadow observable.**
Boundary observable: the holonomy conjugacy class `[Hol_A(gamma_e)] ∈ G/conj`. This is
detectable by an observer who can run test particles around loops on the boundary without
accessing local gauge field values. The holonomy is invariant under gauge transformations and
is thus a genuine observable.

**5. Nontriviality test.**
Parallel pair: Two extensions of a base connection state on `S²`, with the same loop-induced
source ordering (same `<=_S` among visited nodes) but different connection data:
- `e1`: trivial connection `A_1 = 0`; `Hol_{A_1}(gamma) = e ∈ G` (identity).
- `e2`: non-trivial connection `A_2 ≠ 0`; `Hol_{A_2}(gamma) = g ≠ e`.

Same induced order; different connection witness; different holonomy observable. The boundary
observer detects `g ≠ e` via the Wilson loop.

This parallel pair is the most structurally clean in the survey: the holonomy is a genuinely
morphism-level invariant that does not factor through the induced preorder, cleanly evades BDO
(holonomy is a loop invariant, not a boundary momentum), and cleanly evades ICO (holonomy is
not a momentum selection mechanism). BL-004 in RUN-0031 established precisely this.

**6. Failure mode.**
If the connection `A` is a Berry connection, gauge connection, or Levi-Civita connection imported
from a known physical theory, the holonomy is absorbed by that theory (Berry phase, gauge theory,
GR holonomy, etc.). The holonomy is a clean formal invariant of the bundle+connection, but the
bundle and connection themselves must be independently source-defined. Without a source-side
derivation of `A` from `Ext_S`, the connection is stipulated from target physics and the holonomy
is absorbed.

**7. Best toy model.**
`G = U(1)`, `S² = base`, `A = Dirac monopole connection` for `e2` and flat connection for `e1`.
Loops on `S²` around the Dirac string give holonomy `e^{i theta}` for `e2` and identity for `e1`.
Same loop order; different connection; different holonomy. The Wilson loop is directly computable.
This is TM-A from RUN-0031.

**8. Verdict.**
`conditional-live`. The holonomy is the strongest formal invariant in the survey for cleanly
evading BDO and ICO. The parallel pair is well-defined and the boundary observable is not
`p^mu` or `Q_f` imported from Lorentzian physics. The result is conditional on independently
deriving the connection `A` from `Ext_S` structure. Without that derivation, the holonomy is
a formal residue (TI-C012) rather than a physics bridge. This is the best formal result in the
survey.

---

### B10 — Resource/Thermodynamic

**1. Target category.**
The formal category is `ResTh`, a resource theory category with objects being resource states
`rho ∈ R` and morphisms being free operations `F: rho -> sigma` that do not increase resource
content under the allowed operations. Extensions correspond to resource transformations that
produce new states while paying a resource cost. The thermodynamic analogue: objects are
thermodynamic states; morphisms are adiabatic or isothermal processes; the resource is free
energy or entropy.

**2. Witness obligation definition.**
For an admissible extension `e: S -> S'`, `W(e)` is the cost of the extension under the resource
monotone: `W(e) = Delta_F(e) = F(rho_{S'}) - F(rho_S)` where `F` is the relevant resource
monotone (free energy, entropy, etc.). The obligation is: the extension must carry a record of
how much resource was consumed or generated, detectable at the boundary.

**3. Boundary projection map.**
`proj(e) = Delta_F(e)` — the resource cost/gain detectable from the final resource state without
replaying the full extension path. Two extensions with the same induced order (same state-space
ordering on `rho`) can have different resource costs if they reach the same final state via
different paths with different work expenditures.

**4. Shadow observable.**
Boundary observable: `Delta_F(e)` — the free energy difference or entropy change detectable by
a boundary thermometer that can measure the endpoint state but not the full trajectory.

**5. Nontriviality test.**
Parallel pair: Two thermodynamic processes reaching the same macrostate `sigma` from the same
initial macrostate `rho` (same `<=_S` ordering) via different paths:
- `e1`: reversible isothermal process; `Delta_F(e1) = 0` (reversible, no extra work).
- `e2`: irreversible process with entropy generation; `Delta_F(e2) > 0`.

Same macrostate order; different path irreversibility; different resource cost. A boundary
thermometer at the final state cannot always distinguish these (the endpoint is the same). This
is the key failure: if `rho_{S'1} = rho_{S'2}` (same final state), no boundary measurement of
the endpoint state distinguishes `e1` from `e2`. The boundary must access path information,
not just endpoint data.

**6. Failure mode.**
The primary failure: if the final state is the same for both extensions (same induced order,
same endpoint state), then the endpoint boundary observable cannot distinguish them. The resource
cost is a property of the path, not the endpoint. To observe the path cost, the boundary must
measure entropy production along the trajectory — which requires bulk access, not just boundary
access. This makes resource cost a non-boundary-accessible observable in the strict sense.

Alternative failure: if the boundary can access a more refined state (e.g., joint system state
including auxiliary register recording entropy), then the distinction is recoverable, but this
auxiliary register imports thermodynamic bookkeeping machinery.

**7. Best toy model.**
Two-state system with states `{0, 1}`. Both extensions `e1, e2` go from `0` to `1`. `e1` is
reversible (Landauer-erasure-avoiding); `e2` is irreversible (Landauer minimum cost). Same
initial and final state; different work cost. The boundary observer who sees only the endpoint
cannot distinguish them. An observer who sees the heat bath can — but the heat bath is bulk.

**8. Verdict.**
`bookkeeping`. The resource cost is a path property that is either not boundary-accessible (if
the boundary only sees the endpoint) or absorbed by thermodynamics and resource theory (if the
boundary can access path information via an auxiliary register). The parallel pair is structurally
valid but the boundary observable is either inaccessible or absorbed by known resource theory.
No residue independently motivates Temporal Issuance.

---

### B11 — ANN/Representation Learning

**1. Target category.**
The formal category is `RepLearn`, with objects being trained representation spaces `(Phi, W)` —
a feature map `Phi: Input -> LatentSpace` and trained weights `W` — and morphisms being
continual learning updates `f: (Phi, W) -> (Phi', W')` that extend the representation while
preserving or improving the learned structure. Extensions correspond to adding new training
examples or tasks to the learning system.

**2. Witness obligation definition.**
For an admissible extension `e: (Phi, W) -> (Phi', W')`, `W(e)` is the stable latent attractor
obligation: a specification of which regions of latent space remain stable (do not catastrophically
forget) and which new stable attractors are created by the extension. Formally, `W(e)` is the
subset of latent space `A_e ⊆ LatentSpace` that forms a stable attractor under the updated
dynamics — the set of representations that are preserved and retrievable after training on the
extension data.

**3. Boundary projection map.**
`proj(e) = A_e` — the stable attractor set in latent space, identifiable by a boundary observer
who can probe the learned representation with test inputs but not inspect the weight matrix
directly. Two extensions with the same input order (same training data ordering) can produce
different attractor structures if they differ in task composition or regularization.

**4. Shadow observable.**
Boundary observable: `collapse_measure(A_e)` — the representation collapse measure, e.g., the
effective dimensionality of the learned representation (cosine similarity of learned embeddings
or the eigenspectrum of the embedding matrix). This is a standard metric in representation
learning that a boundary evaluator can compute by probing the model with test inputs.

**5. Nontriviality test.**
Parallel pair: Two training sequences over the same base dataset (same induced order on training
examples) but different task compositions:
- `e1`: single-task training; representation collapse is moderate; `collapse_measure(A_{e1}) = c_1`.
- `e2`: multi-task training with conflicting objectives; representation collapse is higher or the
  attractor splits; `collapse_measure(A_{e2}) = c_2 ≠ c_1`.

Same data order; different witness obligation (attractor structure); different boundary observable
(collapse measure).

**6. Failure mode.**
Attractor structure and representation collapse are properties of the learning dynamics —
the optimization landscape, loss function, and architecture — all of which are target-side
(they define what the model is learning). The `Ext_S` rule has no independent mechanism to
determine representation collapse without knowing the loss function and architecture. Absorbed
by deep learning theory, continual learning theory, and the neural tangent kernel framework.

**7. Best toy model.**
Two-layer linear network trained on two tasks sequentially. Single-task vs. multi-task training
on the same data order. The effective dimensionality of the learned embedding layer is measurably
different. A boundary evaluator who probes with test inputs can detect the dimensionality
difference without inspecting the weight matrix. This is a standard continual learning experiment.

**8. Verdict.**
`bookkeeping`. The representation collapse measure is absorbed by deep learning and continual
learning theory. The parallel pair is valid but the boundary observable difference is determined
by the learning dynamics (target-side), not source-side extension rules. No Temporal Issuance
content is required or motivated.

---

### B12 — Holographic/Boundary Encoding

**1. Target category.**
The formal category is `HolEnc`, with objects being boundary code states `psi_∂ ∈ H_∂` (boundary
Hilbert space sectors) and morphisms being admissible boundary operations `U_∂: psi_∂ -> psi'_∂`
that correspond to bulk operations within the entanglement wedge. Extensions `e: psi_∂ -> psi'_∂`
add new boundary degrees of freedom sufficient for partial bulk reconstruction. This directly
parallels `CelExt` but in the AdS/holographic rather than flat-space/BMS setting.

**2. Witness obligation definition.**
For an admissible extension `e: psi_∂ -> psi'_∂`, `W(e)` is the boundary code sufficiency
obligation: after extension `e`, the boundary state `psi'_∂` must contain sufficient degrees of
freedom to reconstruct a strictly larger bulk region — the entanglement wedge must grow. Formally,
`W(e)` is the entanglement wedge `EW(psi'_∂)` — the bulk region reconstructible from `psi'_∂`.

**3. Boundary projection map.**
`proj(e) = EW(psi'_∂)` — the entanglement wedge of the extended boundary state, detectable by
a boundary observer who can compute the Ryu-Takayanagi surface from the boundary entanglement
structure without accessing the bulk directly. Two extensions with the same boundary ordering
(same induced `<=_S` on boundary degrees of freedom) can have different entanglement wedges if
they differ in entanglement structure.

**4. Shadow observable.**
Boundary observable: `S_EE(psi'_∂)` — the entanglement entropy (or equivalently, the RT surface
area) of the extended boundary state. Different extensions produce different entanglement entropies,
which correspond to different bulk reconstruction reach.

**5. Nontriviality test.**
Parallel pair: Two boundary extensions with the same induced boundary ordering (same reduced
density matrix ordering) but different entanglement structures:
- `e1`: product state extension `psi'_∂ = psi_∂ ⊗ |0>_∂`; `S_EE` does not increase; entanglement
  wedge does not grow.
- `e2`: maximally entangled extension `psi'_∂ = (psi_∂ ⊗ |phi^+>_∂) / sqrt(2)` (adding an EPR
  pair); `S_EE` increases by `log 2`; entanglement wedge grows.

Same boundary ordering; different entanglement witness; different RT surface; different bulk
reconstruction capability.

**6. Failure mode.**
Entanglement entropy and RT surfaces are properties of the quantum state and the holographic
dictionary (the bulk geometry). The entanglement wedge calculation requires knowing the bulk
geometry to compute the RT surface — this imports bulk physics. More fundamentally, the holographic
dictionary (which bulk region corresponds to which boundary state) is the target-side content
in the AdS/CFT setting. Without a source-side derivation of the holographic dictionary from
`Ext_S`, this is absorbed by standard AdS/CFT holography.

**7. Best toy model.**
Perfect tensor network (HaPPY model): a simple 6-qubit tensor network with 5 boundary qubits
and 1 bulk qubit. Two extensions add boundary qubits in different entanglement configurations;
the boundary entanglement entropy differs; the bulk reconstruction capability differs. The RT
surface in this toy model is directly computable. This is TM-C from RUN-0031.

**8. Verdict.**
`conditional-live`. The parallel pair is valid and the boundary observable (RT surface /
entanglement entropy) is not manifestly `p^mu` imported from Lorentzian physics. The conditional:
if the holographic dictionary can be independently specified from `Ext_S` structure (without
importing bulk AdS geometry), then the entanglement wedge growth is a genuine witness. This is
the AdS analogue of the CelExt question. It is conditional on the same independence requirement
as B8, but in a different physical setting (AdS vs. flat space). The lens is `conditional-live`
because the independence requirement is conceptually feasible but not yet formalized for the
Temporal Issuance setting.

---

## Synthesis

### Q1: Which lens gives the strongest independently motivated CelExt structure?

**B9 (Holonomy/Gauge)** gives the strongest independently motivated non-Lorentzian boundary
structure. The holonomy group of a connection over `S²` is defined purely in terms of the bundle
and connection data, without presupposing Lorentzian null infinity. The connection `A` lives on
the boundary sphere, and the holonomy is a boundary-computable invariant. If `A` can be derived
from `Ext_S` structure (the fiber bundle connection emerges from the geometry of extension paths),
then `CelExt = BunConn(S²)` is independently specified without presupposing flat-space scattering
or Bondi coordinates.

**B1 (Sheaf/Gluing)** is the runner-up: Čech cohomology on `S²` is independently defined and
does not presuppose Lorentzian null infinity. The Čech cohomology class of a section assignment
is a topological invariant of the sphere.

**B8 (CelExt/BMS)** is the most physically motivated but requires the most prior structure
(boundary CFT, BMS action, current algebra) that is currently not independently derived from
`Ext_S`.

### Q2: Which lens gives the strongest nontrivial boundary observable?

**B9 (Holonomy/Gauge)** again. The holonomy parallel pair (trivial vs. non-trivial connection,
same loop order, different Wilson loop) is the most concretely executable test in the survey.
The Wilson loop value is directly computable given the connection; no target-side bulk input is
needed to compute the parallel transport. The test is: given a typed constraint system `(C, <=_S,
Ext_S)`, does it determine a connection `A` on `S²` such that two extensions with the same
`<=_S`-order produce different holonomies?

**B5 (ZK/Proof-Carrying)** and **B1 (Sheaf/Gluing)** both have concretely executable parallel
pairs, but neither is as physically well-grounded as the holonomy.

### Q3: Which lens best avoids BDO/ICO absorption?

**B9 (Holonomy/Gauge)** cleanly avoids both obstructions:
- BDO killed the route where `p^mu` is object-level. Holonomy is a morphism-level loop invariant —
  it depends on the path taken, not just the endpoint objects. BDO does not reach it.
- ICO killed the route where any mechanism for selecting `p^mu` among competing completions
  imports target dynamics. Holonomy is not a momentum selection mechanism; it is a transport
  invariant. ICO does not reach it.

This was already established in BL-004 (RUN-0031). The present survey confirms it from the
witness-obligation direction: the holonomy witness obligation `W(e) = Hol_A(gamma_e)` is neither
`p^mu` nor a selection among `p^mu`-distinct completions.

**B1 (Sheaf/Gluing)** also avoids BDO/ICO: the Čech cohomology class is not a momentum and not
a completion-selection mechanism. But B1 is more likely than B9 to be bookkeeping.

### Q4: Which lens most naturally connects to BMS soft memory without being absorbed by it?

**B8 (CelExt/BMS)** is the most natural connection. The soft-charge shift `delta Q_f(e)` is
the direct analogue of BMS soft memory in the boundary category. The connection is most natural
precisely because `Q_f` is the BMS charge.

But the absorption risk is also highest here. The closest non-absorbed connection is:

**B9 (Holonomy/Gauge)** → if the connection `A` on `S²` is the Bondi-van der Burg-Metzner-Sachs
(BvdBMS) connection or the Cartan geometry connection for asymptotic flatness, then the holonomy
`Hol_A(gamma)` is a gauge-invariant memory observable. The connection between holonomy and BMS
memory is the following: BMS supertranslation memory is a transition in the holonomy of the
gravitational connection at null infinity. The holonomy lens provides the formal structure that
connects to BMS without importing the full BMS action as a primitive — but deriving the
gravitational connection from `Ext_S` is still required.

### Q5: Which lens best matches Temporal Issuance primitives?

**B5 (ZK/Proof-Carrying)** matches most naturally. The typed constraints `C` in Temporal Issuance
are the closest analogue to typed proof contexts `Gamma`. The admissibility rule `Ext_S` is the
closest analogue to an admissibility condition on proof terms. The admissibility certificate
`pi_e` is a direct formal model of the witness obligation. The source state `S` is the proof
context before extension; `S'` is the extended context.

The limitation: proof complexity classes are absorbed by proof theory, and the admissibility
certificate for `C`-typed extensions would need to differ from standard logical admissibility
to produce a nontrivial result.

**B6 (Consensus/Finality)** also matches TI primitives: finality is the closest operational
analogue to what Temporal Issuance claims about constraints becoming irreversibly extended. But
B6 is absorbed by consensus dynamics.

### Q6: Which lens deserves the next executable fixture?

**B9 (Holonomy/Gauge)** deserves the next executable fixture. The reasons:

1. The parallel pair is most concretely executable: specify a `G`-bundle over `S²`, a base
   connection `A_1 = 0` and a non-trivial connection `A_2`, and two loops with the same source
   ordering. Compute `Hol_{A_1}(gamma)` and `Hol_{A_2}(gamma)` directly. This requires no
   external physics.
2. The witness obligation `W(e) = Hol_A(gamma_e)` is formally precise and not manifestly
   absorbed by known physics (unless the connection is imported from gauge theory, which is the
   failure condition — but testing whether `Ext_S` can independently specify the connection is
   precisely what the fixture would probe).
3. BDO and ICO do not reach this observable. The holonomy formally evades the two strongest
   known obstructions.
4. The connection to BMS memory (BMS memory as holonomy of gravitational connection at null
   infinity) provides a physically meaningful endpoint for the fixture: if the fixture succeeds,
   the holonomy bridge to BMS memory becomes conditionally live, not just speculatively live.

The specific fixture: define the smallest typed constraint system `(C_min, <=_S^min, Ext_S^min)`
that induces a nontrivial `U(1)` connection on a two-patch cover of `S²` (the minimal sheaf
approximation to a bundle over `S²`). Verify that two extensions with the same `<=_S` order
produce holonomies that differ by a non-trivial element of `U(1)`. Verify that the connection
is determined by `Ext_S^min` and not imported from target physics.

---

## Highest-Value Next Result

The one lens/parallel-pair test most worth formalizing:

**B9 — Holonomy/Gauge, minimal `U(1)` connection from `Ext_S`.**

Concretely: given a typed constraint system `(C, <=_S, Ext_S)` with a set of source states `S`
admitting a loop of extensions (a closed chain `s_0 -> s_1 -> ... -> s_n -> s_0`), ask whether
the composition rule for `Ext_S` determines a `U(1)` phase (or more generally a group element
`g ∈ G`) that is non-trivial for some loops and trivial for others, with the distinction
detectable by a boundary Wilson loop observable. If yes: the first nontrivial CelExt witness
finding in the Temporal Issuance program. If no: the connection must be stipulated from target
physics, and the holonomy route joins the list of absorbed bridge candidates.

This test is strictly scoped: it does not claim to derive BMS, physics, or mass-energy. It
claims only that source-side extension loops can carry a non-trivial holonomy observable — the
weakest possible claim that would give the CelExt witness program a genuine foothold.

---

## New Claims

### TI-C017 (speculative)

**Claim.** A witness obligation `W(e)` for an admissible extension `e: S -> S'` in a typed
constraint system `(C, <=_S, Ext_S)` can survive projection to a boundary `S²` as a Čech
cohomology class in `H¹(S², F_e)`, where `F_e` is the sheaf of constraint-valid sections
induced by `e`. This class is not necessarily trivial for all admissible extensions, and
non-trivial classes correspond to gluing obstructions detectable at the boundary.

**Status:** speculative. Depends on specifying what `C`-typed constraints say about local section
compatibility on `S²`.

**Strongest objection.** The Čech cohomology class is absorbed by standard sheaf cohomology
theory. Without a specification that `C`-typed admissibility constrains the section overlap data
in a way distinct from any presheaf, this is bookkeeping.

**Next action.** Specify the section-compatibility predicate for `C`-typed extensions on a two-patch
cover of `S¹` (simplest case). Ask whether the admissibility rule independently determines which
Čech cocycles are allowed.

---

### TI-C018 (speculative)

**Claim.** A typed constraint extension system `(C, <=_S, Ext_S)` with closed extension loops
can determine a `G`-valued holonomy observable `Hol_{A_{Ext_S}}(gamma) ∈ G` that (a) is a
morphism-level invariant not recoverable from the induced preorder `<=_S`, (b) cleanly evades
both BDO and ICO, and (c) can serve as the witness observable for a boundary category
`CelExt = BunConn(S²)` if the connection `A_{Ext_S}` is determined by the extension rule
without importing target-side physics.

**Status:** speculative. Extends TI-C012 by making the connection-independence condition precise
and connecting the holonomy to the witness-obligation formalism introduced in RUN-0036.

**Strongest objection.** The connection `A_{Ext_S}` cannot be determined by `Ext_S` without
importing a gauge theory or Berry-phase framework. If the connection is imported, the holonomy
is absorbed by that framework.

**Next action.** Run the holonomy fixture: specify `(C_min, <=_S^min, Ext_S^min)` and derive
the induced connection; test whether it is non-trivial for any loop.
