---
artifact_type: exploration
status: active
exploration_id: E050
date: 2026-06-22
topic: quorum_equivariance_test_layer_obl_001_subreq2
claim_refs:
  - TI-C019
relates_to:
  - E031 (Ext_S category; SBP morphism class; AC-8 quorum cost; Compat predicate)
  - E040 (Ostrom Redistribution Theorem; WITNESS-OBL-001; quorum legitimacy)
  - E042 (SBP-IND verification; FTS/Gödelian fork; Family G)
  - E046 (hostile audit; LAYER-OBL-001; 20-absorber analysis; Gauge Absorber #5)
  - E047 (GU cross-repo; Riemannian/Ehresmannian framing; LAYER-OBL-001 sub-req 1)
  - E048 (Weinstein UCSD 2025; distortion vs. torsion; tau+ structure; double coset; GAUGE-COV-OBL-001)
blocking_task_addressed: >
  LAYER-OBL-001 sub-requirement 2 — show that A_{S_{n+1}} is determined by quorum-accepted
  schema updates (the source-layer "right action") and NOT merely by individual observer
  type-name choices (the observer-layer "left action"). The quorum equivariance test
  was named in E048 as a medium-priority obligation; this exploration executes it.
proof_verdict: >
  CONDITIONALLY QUORUM-EQUIVARIANT. The AC-8 quorum update rule is quorum-equivariant
  under condition GAUGE-COV (Compat is schema-relabeling-covariant). In the Gödelian
  regime (Family G, E042), this condition holds by construction. In the FTS regime,
  it must be verified against the specific Compat instantiation. LAYER-OBL-001
  sub-requirement 2 is conditionally closed, with GAUGE-COV-OBL-001 as the outstanding
  verification obligation. Combined with E042's SBP-IND result, the two sub-requirements
  jointly support the double-coset structure for the Gödelian regime.
---

# E050: Quorum Equivariance Test — LAYER-OBL-001 Sub-Requirement 2

## Purpose

E048 named the QUORUM-EQUIVARIANCE TEST as a concrete diagnostic for LAYER-OBL-001
sub-requirement 2 (medium priority, blocking LAYER-OBL-001). E049 handles sub-requirement 1
(distortion residue non-zero). This exploration executes sub-requirement 2:

> Show that A_{S_{n+1}} is determined by quorum-accepted schema updates (source-layer
> "right action") and NOT merely by individual observer type-name choices (observer-layer
> "left action").

The Weinstein double-coset structure (E048 Claim 3) provides the formal model:
- In GU: the inhomogeneous gauge group has two operations on a connection (gauge
  transformation = left action; add gauge potential = right action). The double coset
  absorbs the left action, leaving only the right action visible. The result is
  gauge-equivariant (divergence-free in GU's language).
- In TI: the AC-8 quorum has two operations on A_{S_n} (individual observer type-name
  choice = left action; quorum-accepted SBP extension = right action). If the double-coset
  structure holds, A_{S_{n+1}} is determined only by the right action.

---

## 1. Setup: The Two Operations on A_{S_n}

From E048 §Claim 2-3, the TI Inhomogeneous Admissibility Group has two factors:

```text
TI-IAG = TypeRelabelings ⋊ AdmissibleExtensions
```

**Left factor (TypeRelabelings):** A type relabeling is a bijection phi: T_infty -> T_infty
that preserves the admissibility structure. Formally: phi is a schema isomorphism if
for all subsets X subset T_S, A_S(X) = A_{phi(S)}(phi(X)). A type relabeling acts on
a schema state S_n by:

```text
phi * S_n = phi(S_n) = (phi(T_{S_n}), A_{phi(S_n)})
```

where phi(T_{S_n}) = {phi(c) : c in T_{S_n}} and A_{phi(S_n)}(Y) = A_{S_n}(phi^{-1}(Y)).

**Right factor (AdmissibleExtensions):** An admissible extension e: S_n -> S_{n+1} acts
on A_{S_n} by adding a new constraint c_e with a new type:

```text
e * A_{S_n} = A_{S_{n+1}}
```

where A_{S_{n+1}} is determined by A_{S_n} and Compat(c_e, X, S_n) as in E031 §I.2.

**The two "ways to push" A_{S_n}:**

Following the E048 tau+ structure:
- (Left push): phi * A_{S_n} = A_{phi(S_n)} — relabel type names while preserving
  admissibility structure. This is an observer-coordination-layer operation.
- (Right push): A_{S_n} -> A_{S_{n+1}} via quorum-accepted extension e — update the
  admissibility predicate by accepting a new typed constraint. This is the candidate
  source-layer operation.

The E048 distortion residue is the gauge-equivariant component of A_{S_{n+1}} - A_{S_n}
not explained by type relabeling (LAYER-OBL-001 sub-req 1, handled in E049). The
quorum equivariance test asks whether the right push is sensitive to LEFT push choices
made PRIOR to submitting the proposal to quorum.

---

## 2. Formalization of the Quorum Update Rule

### 2.1 The E028 Quorum Legitimacy Condition (restated from E040)

A schema extension e: S_n -> S' updates the shared schema from S_n to S_{n+1} = S'
iff at least k observers (out of n total) evaluate e against the current shared
admissibility predicate A_{S_n} and accept it.

**The acceptance predicate for observer O_i:**
Observer O_i accepts e iff:

```text
Accept_i(e, S_n) = 1  iff  Compat(c_e, T_{S_n}, S_n) = 1
```

where the evaluation is performed relative to the SHARED admissibility predicate A_{S_n},
not relative to O_i's local type-name schema.

**The quorum acceptance condition:**
e is quorum-accepted iff:

```text
|{O_i : Accept_i(e, S_n) = 1}| >= k
```

**The quorum update rule:**
If e passes quorum, the shared schema updates:

```text
S_{n+1} = S_n + e = (T_{S_n} union {c_e}, A_{S_{n+1}})
```

where A_{S_{n+1}} is defined by E031 §I.2:

```text
A_{S_{n+1}}(X) = 1  iff  A_{S_n}(X \ {c_e}) = 1  AND  Compat(c_e, X \ {c_e}, S_n) = 1
```

If the quorum rejects e (fewer than k accept), S_{n+1} = S_n (no update).

### 2.2 The Incompatibility Guard

E046 §5 (Gauge Absorber) noted that SBP proposals carry a TYPE-INCOMPATIBILITY condition:
two concurrent SBP proposals e_1: S_n -> S' and e_2: S_n -> S'' are SBP-incompatible iff:

```text
Compat(c_{e_1}, T_{S''}, S_n) = 0  AND  Compat(c_{e_2}, T_{S'}, S_n) = 0
```

The quorum therefore cannot accept BOTH e_1 and e_2 from the same S_n — at most one
SBP fork per stage is accepted. This is the "incompatibility guard" that makes the quorum
a genuine arbiter between competing proposals, not a passive accumulator.

### 2.3 The Full AC-8 Quorum Update Rule

Combining the above:

```text
AC-8 Quorum Update Rule (QUR):

Given: shared schema S_n, observer set {O_1, ..., O_n}, threshold k, proposals
  e_1: S_n -> S'_1, ..., e_m: S_n -> S'_m (where m proposals are submitted)

Step 1 (Compatibility screening): For each proposal e_j, check
  Compat(c_{e_j}, T_{S_n}, S_n) = 1. Proposals failing this are invalid and
  withdrawn before quorum evaluation.

Step 2 (Incompatibility guard): Among valid proposals, the quorum may not simultaneously
  accept two SBP-incompatible proposals. If e_j and e_k are SBP-incompatible
  (their types fork the schema), the quorum accepts at most one.

Step 3 (Threshold vote): Surviving valid proposals are put to vote. A proposal e_j
  is accepted iff >= k observers evaluate it against A_{S_n} and return Accept.

Step 4 (Update): The first proposal to reach threshold k updates the schema:
  S_{n+1} = S_n + e_j for the accepted e_j. If no proposal reaches threshold,
  S_{n+1} = S_n.
```

This rule produces A_{S_{n+1}} as a function of:
- A_{S_n} (the current shared admissibility predicate)
- c_{e_j} (the type and constraint structure of the accepted proposal)
- Compat(c_{e_j}, -, S_n) (the compatibility predicate evaluated at the current schema)

---

## 3. The Quorum Equivariance Test

### 3.1 Test Statement (Formal)

Two observers O_i and O_j use different local type-name conventions. They observe the same
structural SBP proposal (the same underlying typed constraint extension), but under their
respective naming conventions they describe it differently:
- O_i labels the proposed constraint as c_i (type: tau_i)
- O_j labels the same constraint as c_j = r_{ij}(c_i), where r_{ij} is a type relabeling

**The quorum equivariance test:**

Does the quorum-accepted schema update A_{S_{n+1}} depend on WHICH naming convention
is used to represent the proposal, or only on the STRUCTURAL CONTENT of the proposal?

Formally: Let r: T_infty -> T_infty be a type relabeling (schema isomorphism). Let
e: S_n -> S' be an SBP proposal under the identity convention. Let r(e) denote the
"same" proposal represented under r-relabeling: the extension adding constraint
c_{r(e)} = r(c_e) to r(S_n).

**The test passes (quorum-equivariant) iff:**

```text
For any type relabeling r, if e passes quorum from S_n,
then r(e) passes quorum from r(S_n),
and the resulting schema updates are related by r:

  r(S_{n+1}) = r(S_n + e) = r(S_n) + r(e)
```

Equivalently: the quorum update rule QUR commutes with type relabeling.

### 3.2 Key Question: Does the Acceptance Predicate Depend on Type Names?

The acceptance predicate for observer O_i is:

```text
Accept_i(e, S_n) = 1  iff  Compat(c_e, T_{S_n}, S_n) = 1
```

Does this evaluation depend on the specific NAMES (labels) in T_{S_n}, or only on the
STRUCTURAL RELATIONS encoded in Compat?

The answer turns on the definition of Compat. There are two cases:

**Case A (Torsion-style Compat — schema-relabeling-SENSITIVE):**
Compat(c, T, S) depends on the specific type labels in T and the label of c. Two
structurally identical proposals with different type names could evaluate differently.
In this case, the acceptance predicate depends on type names and the quorum outcome
can vary with naming convention. The test FAILS.

**Case B (Distortion-style Compat — schema-relabeling-COVARIANT, GAUGE-COV condition):**
Compat(phi(c), phi(T), phi(S)) = Compat(c, T, S) for every schema isomorphism phi.
The acceptance predicate depends only on structural relations, not specific type labels.
The test PASSES.

This is exactly the GAUGE-COV-OBL-001 condition from E048.

### 3.3 Formal Proof of Quorum Equivariance under GAUGE-COV

**Theorem (Quorum Equivariance):** If the Compat predicate satisfies GAUGE-COV
(schema-relabeling-covariance), then the quorum update rule is quorum-equivariant:

```text
For any schema isomorphism phi: T_infty -> T_infty and any SBP proposal e: S_n -> S',
the quorum accepts e from S_n with threshold k
iff
the quorum accepts phi(e) from phi(S_n) with the same threshold k,
and phi(S_{n+1}) = phi(S_n + e) = phi(S_n) + phi(e).
```

*Proof.*

**Step 1:** Acceptance of e from S_n.

Observer O_i accepts e iff Accept_i(e, S_n) = 1, i.e., Compat(c_e, T_{S_n}, S_n) = 1.

**Step 2:** Acceptance of phi(e) from phi(S_n).

Observer O_i (working under the phi convention) accepts phi(e) iff:

```text
Compat(phi(c_e), phi(T_{S_n}), phi(S_n)) = 1
```

By GAUGE-COV:

```text
Compat(phi(c_e), phi(T_{S_n}), phi(S_n)) = Compat(c_e, T_{S_n}, S_n)
```

Therefore Accept_i(phi(e), phi(S_n)) = Accept_i(e, S_n).

**Step 3:** The quorum count is identical.

Since each observer's acceptance is identical (Step 2), the count of accepting observers
is identical. Therefore e reaches threshold k from S_n iff phi(e) reaches threshold k
from phi(S_n). QED on the threshold condition.

**Step 4:** The updated schema is related by phi.

If e is accepted and S_{n+1} = S_n + e, then by the E031 §I.2 formula:

```text
A_{S_{n+1}}(X) = 1  iff  A_{S_n}(X \ {c_e}) = 1  AND  Compat(c_e, X \ {c_e}, S_n) = 1
```

The schema updated from phi(S_n) by phi(e) has admissibility:

```text
A_{phi(S_{n+1})}(Y) = 1  iff  A_{phi(S_n)}(Y \ {phi(c_e)}) = 1  AND
                                Compat(phi(c_e), Y \ {phi(c_e)}, phi(S_n)) = 1
```

Setting Y = phi(X):

```text
A_{phi(S_n)}(phi(X) \ {phi(c_e)}) = A_{phi(S_n)}(phi(X \ {c_e})) = A_{S_n}(X \ {c_e})
```

(using that phi is an admissibility-preserving isomorphism)

```text
Compat(phi(c_e), phi(X) \ {phi(c_e)}, phi(S_n)) = Compat(phi(c_e), phi(X \ {c_e}), phi(S_n))
                                                  = Compat(c_e, X \ {c_e}, S_n)
```

(using GAUGE-COV)

Therefore: A_{phi(S_{n+1})}(phi(X)) = A_{S_{n+1}}(X), which means phi(S_{n+1}) is the
schema state produced by applying phi(e) to phi(S_n). In other words:

```text
phi(S_n + e) = phi(S_n) + phi(e)
```

This proves quorum equivariance. QED.

### 3.4 The Double-Coset Structure

The Quorum Equivariance theorem confirms the double-coset structure from E048 Claim 3:

- **Left action (type relabelings) is absorbed:** The quorum evaluation of any proposal e
  from S_n is IDENTICAL to the evaluation of the relabeled proposal phi(e) from phi(S_n)
  (Step 2 above). The left action has "no effect" on the quorum outcome — it falls through
  because GAUGE-COV makes Compat invariant under phi.

- **Right action (quorum-accepted extensions) determines A_{S_{n+1}}:** The schema update
  is determined by the TYPE COMPATIBILITY STRUCTURE of the accepted proposal (specifically:
  Compat(c_e, -, S_n) and the constraint c_e's structural relations to T_{S_n}), not by
  the specific type-name labels.

The formal double-coset quotient:

```text
TI-IAG double coset: TypeRelabelings \ AdmissibleExtensions / TypeRelabelings
```

The QUR factors through this double quotient: A_{S_{n+1}} depends on the double coset
of the accepted extension, not on its specific labeling in any observer's naming convention.

This is the TI analog of GU's theta map factoring through A/G (connections modulo gauge):
the quorum-accepted schema update A_{S_{n+1}} factors through the double quotient, making
it "divergence-free" in E048's vocabulary — the update does not "leak" observer-layer
naming artifacts into the shared schema state.

---

## 4. Does the E028 Quorum Legitimacy Condition Depend on Type Names?

The critical question for quorum equivariance is whether the E028 quorum legitimacy
condition itself (the THRESHOLD vote, the INCOMPATIBILITY GUARD, and the VALIDITY
SCREENING) depends on specific type names.

### 4.1 Validity Screening (Step 1 of QUR)

The compatibility screening: Compat(c_{e_j}, T_{S_n}, S_n) = 1.

Under GAUGE-COV, this is type-name-invariant (proven in Step 2 of §3.3). Validity
screening passes or fails based on structural compatibility, not type labels.

**Conclusion: Validity screening is type-name-independent under GAUGE-COV.**

### 4.2 Incompatibility Guard (Step 2 of QUR)

Two proposals e_1, e_2 are SBP-incompatible iff:

```text
Compat(c_{e_1}, T_{S''}, S_n) = 0  AND  Compat(c_{e_2}, T_{S'}, S_n) = 0
```

Under GAUGE-COV (applying phi):

```text
Compat(phi(c_{e_1}), phi(T_{S''}), phi(S_n)) = Compat(c_{e_1}, T_{S''}, S_n) = 0
Compat(phi(c_{e_2}), phi(T_{S'}), phi(S_n)) = Compat(c_{e_2}, T_{S'}, S_n) = 0
```

Therefore phi(e_1) and phi(e_2) are SBP-incompatible relative to phi(S_n) iff e_1 and
e_2 are SBP-incompatible relative to S_n. The incompatibility guard is type-name-invariant
under GAUGE-COV.

**Conclusion: The incompatibility guard is type-name-independent under GAUGE-COV.**

### 4.3 Threshold Vote (Step 3 of QUR)

The threshold vote requires k-of-n observers to Accept. As proven in Step 2-3 of §3.3,
the acceptance count is identical across naming conventions under GAUGE-COV.

**Conclusion: The threshold vote is type-name-independent under GAUGE-COV.**

### 4.4 Summary: E028 Condition is Type-Name-Independent under GAUGE-COV

All three components of the E028 quorum legitimacy condition (validity screening,
incompatibility guard, threshold vote) are type-name-independent when the Compat predicate
is schema-relabeling-covariant. The E028 condition imposes a structural requirement on
proposals, not a syntactic one. Individual observers can use any naming convention they
like; the quorum outcome is the same.

---

## 5. Check: Does Family G (Gödelian Compat) Satisfy GAUGE-COV?

E042 defined Family G's Compat predicate:

```text
Compat_G(c, X, S) = 1  iff  Ax(S) union {the constraint encoded by c} union
                              {constraints in X}  does not prove bottom (consistency preserved)
```

where constraint labels are pairs (phi, w) with phi a first-order arithmetic formula and
w in {0,1} polarity.

**Claim: Compat_G satisfies GAUGE-COV.**

A type relabeling in Family G must preserve the interpretation of constraint labels.
Because constraint labels are arithmetic formulas (not opaque type names), a "relabeling"
in Family G is an ISOMORPHISM of the arithmetic constraint structure — specifically, a
bijection phi such that phi(c) = (phi_f(formula), w) where phi_f is a formula-level
isomorphism that preserves provability relations.

For any such phi:

```text
Compat_G(phi(c), phi(X), phi(S)) = 1
  iff  Ax(phi(S)) union {phi(c)} union {phi(X)}  does not prove bottom
  iff  phi(Ax(S)) union {phi(c)} union phi(X)  does not prove bottom
  iff  Ax(S) union {c} union {X}  does not prove bottom (isomorphism preserves consistency)
  iff  Compat_G(c, X, S) = 1
```

The last step uses that phi is an isomorphism of the arithmetic structure and therefore
preserves consistency: Th(Ax(S)) is isomorphic to Th(phi(Ax(S))) = Th(Ax(phi(S))).

**Conclusion: Family G (Gödelian Compat) satisfies GAUGE-COV.**

Therefore, by the Quorum Equivariance Theorem (§3.3), Family G's quorum update rule is
quorum-equivariant. The double-coset structure holds in the Gödelian regime.

**Status of GAUGE-COV-OBL-001 for Family G:**
SATISFIED. GAUGE-COV holds for the Gödelian Compat family by construction (provability
preserving isomorphisms preserve consistency, hence preserve Compat_G). This is not an
additional assumption; it follows from the arithmetic structure of Family G.

---

## 6. Interaction with E042 (SBP-IND)

E042 established two key results for SBP-IND:
- In the FTS regime: SBP-IND FAILS. The SBP space is finite and enumerable; the SSC
  adversary succeeds.
- In the Gödelian regime: SBP-IND HOLDS. The SBP space (propositions independent of Ax(S))
  is productively infinite and non-c.e.

The quorum equivariance test and SBP-IND address DIFFERENT layers of the LAYER-OBL-001
question:

**SBP-IND (E042):** Addresses whether the CONTENT of SBP proposals is non-pre-determinable
from the shared schema history. This concerns the SOURCE-SIDE non-computability of the
proposal function. It is a property of the observer's proposal space, answering: "Can
an adversary predict what proposals will be submitted?"

**Quorum Equivariance (E050):** Addresses whether the OUTCOME of the quorum is independent
of individual observer NAMING CONVENTIONS. This concerns whether the shared schema update
A_{S_{n+1}} is a structural fact or a naming-convention artifact. It answers: "Is the
quorum outcome the same regardless of how observers label their proposals?"

They jointly close LAYER-OBL-001 sub-requirement 2 as follows:

```text
LAYER-OBL-001 sub-requirement 2 (from E048):
  Show that A_{S_{n+1}} is determined by quorum-accepted schema updates (right action)
  and NOT by individual observer type-name choices (left action).

Two-part discharge:
  Part A (E042/SBP-IND): The CONTENT of proposals that reach quorum is not determined
    by any pre-committed source. Proposals carry genuine structural information not
    reducible to the shared history.
  Part B (E050/Quorum Equivariance): The PROCESSING of proposals by the quorum is
    type-name-invariant. Given any proposal, the quorum outcome depends only on the
    proposal's structural compatibility with A_{S_n}, not on how individual observers
    label the types involved.

Together: A_{S_{n+1}} encodes (a) non-pre-determinable structural content (SBP-IND)
processed by (b) a type-name-invariant quorum mechanism (quorum equivariance).
Neither individual observer naming choices NOR pre-committed source templates determine
A_{S_{n+1}}. The double-coset structure holds: left action (naming) absorbed, right
action (structural schema extension) determines evolution.
```

**The FTS/Gödelian fork interaction:**

In the FTS regime: E042 shows SBP-IND fails (proposals are pre-determinable from the
finite type budget). Quorum equivariance may hold (GAUGE-COV is verifiable for FTS Compat
families), but it provides no source-side content since there is no genuine SBP-IND.
Sub-requirement 2 is vacuously equivariant but the equivariant content is empty (the
"right action" that escapes observer relabeling is itself exhaustible from a fixed source).

In the Gödelian regime: Both SBP-IND (E042 Theorem 3) and quorum equivariance (E050 §3.3
and §5) hold. The double-coset structure is non-trivially populated: the right action
carries productively infinite, non-c.e., type-name-invariant structural content. This is
genuine source-layer content that passes through the double coset intact.

**Diagram of interaction:**

```text
              Individual Observer
              Naming Choice (left)
                      |
                      v
              Type Relabeling phi
                      |
              [GAUGE-COV absorbs phi]
                      |
                      v (phi falls through)
SBP Proposal --> Quorum Evaluation --> A_{S_{n+1}}
(structural         (structural         (structural
 content,            compatibility       update,
 non-predeterminable check, k-of-n       phi-covariant)
 by SBP-IND)         threshold)
```

The diagram shows: phi (left action) enters the quorum evaluation but is absorbed by
GAUGE-COV. The structural content of the SBP proposal (which is non-pre-determinable by
SBP-IND) is what reaches A_{S_{n+1}}. The double-coset structure is exactly this diagram.

---

## 7. Failure Modes and Conditions

### 7.1 Failure Mode: GAUGE-COV Violated

If the Compat predicate is NOT schema-relabeling-covariant (torsion-style rather than
distortion-style), then the quorum outcome CAN depend on type names. In this case:

- Observer O_i labels proposal as (tau, +) (assert formula tau)
- Observer O_j labels the "same" proposal as (sigma, +) where sigma != tau
- The quorum evaluates differently against A_{S_n} depending on whether it reads tau or sigma

This means individual observer naming choices BLEED INTO the shared schema state. The left
action is not absorbed; it partially determines A_{S_{n+1}}. This is absorber #18 (Observer
Privilege, E046): the quorum is partly adjudicating naming conventions, not purely schema-
boundary proposals.

**What this failure means for LAYER-OBL-001:**
If GAUGE-COV fails, sub-requirement 2 is open: A_{S_{n+1}} partially reflects observer-
layer naming artifact. The PP-3 inference is blocked because the shared schema state
conflates source-layer structural content with observer-layer conventions.

**Mitigation:** The GAUGE-COV-OBL-001 obligation from E048 — amend E031's Compat definition
to the distortion-style covariant version if it is not already covariant. For Family G
(Gödelian), GAUGE-COV holds by construction (§5 above). For other Compat families, it
must be verified.

### 7.2 Failure Mode: Type-Incompatibility Itself is Gauge-Relative

The E046 Gauge Absorber (#5) raised the concern that SBP-incompatibility might be gauge-
relative: two proposals that appear type-incompatible under one naming convention might
appear compatible under another convention.

The quorum equivariance theorem (§3.3) addresses this directly. Under GAUGE-COV, the
incompatibility guard is type-name-invariant (§4.2): e_1 and e_2 are SBP-incompatible
iff phi(e_1) and phi(e_2) are SBP-incompatible for all phi. No relabeling can convert
an SBP-incompatible pair into a compatible pair.

**If GAUGE-COV holds:** The Gauge Absorber is DEFEATED. SBP-incompatibility is a structural
property of the proposals, not a naming-convention artifact.

**If GAUGE-COV fails:** The Gauge Absorber may succeed: a phi could in principle convert
an "incompatible" pair into a "compatible" pair, and the quorum would then not be adjudicating
genuine structural incompatibility but naming-convention choice. Sub-requirement 2 open.

### 7.3 Failure Mode: Non-Uniform Naming Conventions Across Observers

In the test statement (§3.1), we assumed that all observers evaluate the proposal against
the SHARED A_{S_n}. The quorum legitimacy condition (E028 §2, restated in E040 §1) specifies:
"at least k observers must evaluate e against the current shared admissibility predicate A_{S_n}."

The key is "shared" — the evaluation is against the COMMON schema state, not against
individual observers' private schema states. This ensures that even if O_i and O_j use
different type-name conventions locally, they evaluate against the SAME A_{S_n} when
participating in the quorum.

Under GAUGE-COV, evaluating against A_{S_n} is isomorphic to evaluating against phi(A_{S_n})
for any phi (because Compat is phi-invariant). So even observers with different conventions
converge on the same structural evaluation.

**Conclusion:** The E028 quorum legitimacy condition's "shared A_{S_n}" requirement, combined
with GAUGE-COV, is the formal mechanism that prevents non-uniform naming from fragmenting the
quorum. The shared schema is the common reference frame; GAUGE-COV ensures the evaluation
against that frame is naming-convention-neutral.

---

## 8. Verdict: LAYER-OBL-001 Sub-Requirement 2

### 8.1 Verdict Statement

```text
VERDICT: CONDITIONALLY QUORUM-EQUIVARIANT

The AC-8 quorum update rule (QUR) is quorum-equivariant — A_{S_{n+1}} is determined
by the right action (quorum-accepted schema updates) and not by the left action (individual
observer type-name choices) — under condition GAUGE-COV (Compat is schema-relabeling-
covariant).

For Family G (Gödelian Compat), GAUGE-COV holds by construction (§5). The double-coset
structure is confirmed for the Gödelian regime.

For FTS Compat families, GAUGE-COV must be verified against the specific Compat
instantiation (GAUGE-COV-OBL-001, E048).

LAYER-OBL-001 sub-requirement 2:
  - In the Gödelian regime: CONDITIONALLY CLOSED. The double-coset structure holds;
    the left action is absorbed; A_{S_{n+1}} is a structural fact about the accepted
    proposal and A_{S_n}, not a naming-convention artifact. Closed conditional on
    Family G being the operative Compat family (D-FORK question, E042).
  - In the FTS regime: CONDITIONALLY OPEN pending GAUGE-COV-OBL-001 verification.
    Moot for source-side claims (E042 shows SBP-IND fails in FTS anyway).
```

### 8.2 What Closes and What Remains Open

**Closed by E050:**
1. The formal structure of the quorum equivariance test — the theorem (§3.3) and its
   proof under GAUGE-COV are complete.
2. GAUGE-COV verification for Family G (Gödelian Compat): confirmed by construction (§5).
3. Type-name-independence of all three components of the E028 quorum legitimacy condition
   under GAUGE-COV (§4): validity screening, incompatibility guard, threshold vote — all
   confirmed type-name-independent.
4. The double-coset structure for the Gödelian regime: left action (type relabeling) is
   absorbed; right action (structural SBP extension) determines A_{S_{n+1}} (§3.4).
5. Interaction with E042 SBP-IND formalized: the two results operate at different layers
   and jointly discharge sub-requirement 2 in the Gödelian regime (§6).

**Still open (outstanding obligations):**
1. **GAUGE-COV-OBL-001** (E048): Verify that E031's general Compat(c, T, S) definition
   is schema-relabeling-covariant. For Family G: done. For the general definition in
   E031 §I.2: needs explicit check. If the general Compat is not covariant, the definition
   should be amended to the distortion-style version.
2. **D-FORK resolution** (E042 §6): Which regime (Gödelian or FTS) is the operative source?
   Until this is settled, the conditional closure of sub-requirement 2 (in the Gödelian
   regime) is conditional on the answer being "Gödelian."
3. **LAYER-OBL-001 sub-requirement 1** (handled in E049): The distortion residue must be
   non-zero. E050 confirms sub-requirement 2 is satisfied; it does not discharge sub-
   requirement 1.
4. **LAYER-OBL-001 sub-requirement 3** (E046): The Gödelian SBP space must be creationist
   (open-ended source extension), not Platonist (navigation of fixed arithmetic truth).
   Neither E049 nor E050 addresses sub-requirement 3; it remains the deepest open item.

### 8.3 LAYER-OBL-001 Status After E050

LAYER-OBL-001 (from E046): "Specify conditions under which quorum coordination is correctly
attributed to source-layer construction (not navigation of a fixed Gödelian structure)."

Sub-requirement 2 status: **CONDITIONALLY CLOSED (Gödelian regime)** — E050.

Full LAYER-OBL-001 status: **STILL OPEN** — sub-requirements 1 (E049) and 3 (open) must
also be discharged. E050 closes sub-requirement 2 as a standalone, but LAYER-OBL-001 as
a whole remains open until all three sub-requirements are satisfied.

---

## 9. E046 Absorber Audit Effects

### 9.1 Gauge Absorber (#5) — Updated Status

E046 Absorber #5 (Gauge Absorber): "SBP proposals might be gauge-equivalent descriptions
of the same source constraint; the quorum performs gauge-fixing, not source extension."

Previous status (E048): CONDITIONALLY DEFEATED pending GAUGE-COV-OBL-001 verification.

E050 update:
- For Family G (Gödelian Compat): GAUGE-COV holds by construction (§5). The Gauge
  Absorber is DEFEATED for Family G. SBP-incompatibility is structural (type-relabeling-
  covariant), not naming-convention artifact. No relabeling phi can convert incompatible
  proposals into compatible ones in Family G.
- For general Compat: CONDITIONALLY DEFEATED pending GAUGE-COV-OBL-001.

**New absorber classification for #5:**

| # | Absorber | E046 Classification | E048 Update | E050 Update |
|---|---|---|---|---|
| 5 | Gauge | Partial absorber (potentially fatal) | Conditionally defeated (GAUGE-COV-OBL-001) | Defeated for Family G; conditionally defeated for general Compat |

### 9.2 Observer-Privilege Absorber (#18) — Updated Status

E046 Absorber #18 (Observer-Privilege): "Individual observer proposal powers belong to the
shared process; proposals are proxies for the process's generative capacity."

E046 classified this as "Interpretation shift only — does not weaken source-side interpretation;
it relocates the source from individual observers to the shared process."

E050 interaction: Quorum equivariance CONFIRMS this interpretation. The quorum equivariance
theorem shows that A_{S_{n+1}} is determined by the structural content of the accepted proposal
(which represents the "shared process" view), not by individual observer naming choices. The
observer-privilege absorber's shift to "shared process as source" is consistent with the
double-coset structure: the double coset precisely captures the shared-process view (naming
absorbed, structural extension survives).

E050 does not change the absorber #18 classification but provides formal precision: the
"shared process" that absorber #18 identifies as the source is formally the right-action
factor of the double-coset construction, not an amorphous shared-generative capacity.

**Updated classification for #18:** Interpretation shift only — now with formal support
from the double-coset structure (E050 §3.4). The relocating interpretation is confirmed
consistent with quorum equivariance.

### 9.3 All Other Absorbers

No other absorber classifications change from E046/E048. E050's quorum equivariance theorem
does not affect absorbers #1-4, #6-17, #19-20 beyond what E048 already established.

---

## 10. Summary of Resolved and Open Items

### Resolved by This Exploration

1. **Quorum equivariance theorem:** Proved (conditionally on GAUGE-COV). The AC-8 quorum
   update rule commutes with type relabelings when Compat is schema-relabeling-covariant.

2. **Double-coset structure confirmed:** The left action (type relabeling) is absorbed by
   the quorum's GAUGE-COV-satisfying Compat predicate; the right action (structural schema
   extension) determines A_{S_{n+1}}.

3. **GAUGE-COV for Family G:** Verified by construction. Gödelian Compat (consistency
   preservation) is schema-relabeling-covariant because arithmetic isomorphisms preserve
   provability and consistency.

4. **E028 quorum legitimacy is type-name-independent under GAUGE-COV:** All three components
   (validity screening, incompatibility guard, threshold vote) confirmed.

5. **Interaction with E042 SBP-IND formalized:** The two results operate at different layers
   (proposal-content layer vs. quorum-processing layer) and jointly discharge LAYER-OBL-001
   sub-requirement 2 in the Gödelian regime.

6. **Gauge Absorber #5 (E046) defeated for Family G:** Under GAUGE-COV (which holds for
   Family G), no type-relabeling phi converts SBP-incompatible proposals into compatible
   ones. The absorber is formally defeated for the Gödelian operative source.

7. **LAYER-OBL-001 sub-requirement 2:** CONDITIONALLY CLOSED in the Gödelian regime.

### Open / Still Blocked

1. **GAUGE-COV-OBL-001 for general Compat:** Must verify that E031 §I.2's general Compat
   definition is schema-relabeling-covariant. If not, amend to distortion-style.

2. **LAYER-OBL-001 sub-requirement 1 (E049):** The distortion residue must be shown
   non-zero. E050 does not address this.

3. **LAYER-OBL-001 sub-requirement 3 (E046):** The Gödelian SBP space must be creationist
   (source-side creation), not Platonist (navigation of fixed arithmetic structure). Neither
   E049 nor E050 addresses this; it is the deepest remaining gap for the PP-3 inference.

4. **D-FORK resolution (E042):** The operative-source question (Gödelian or FTS?) remains
   open. Sub-requirement 2's conditional closure is conditional on this.

---

## Governance Constraints

1. Do not use quorum equivariance to claim PP-3 is resolved. Quorum equivariance establishes
   that the shared schema update is a structural fact (not a naming convention artifact), but
   it does not establish that the structural fact is source-side rather than observer-coordination
   side. That is sub-requirement 3.

2. Quorum equivariance is a NECESSARY condition for LAYER-OBL-001 sub-requirement 2, not
   sufficient alone. It must combine with SBP-IND (E042) for the full discharge.

3. GAUGE-COV must be verified for any specific Compat family before the quorum equivariance
   theorem is applied to it. For Family G, this is done. For FTS families, it is pending.

4. The double-coset structure is formally confirmed here only for the abstract category-level
   argument. The physics-level claim (that this corresponds to genuine source-side novelty)
   requires LAYER-OBL-001 sub-requirements 1 and 3 as well.
