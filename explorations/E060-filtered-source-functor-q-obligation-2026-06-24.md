---
artifact_type: exploration
status: active
exploration_id: E060
run_ref: RUN-0055
created: 2026-06-24
claim_refs:
  - TI-C012
  - TI-C017
  - TI-C019
  - TI-C020
---

# E060 - Filtered-Source Functor and Q Obligation

## Purpose

Execute the RUN-0054 next trigger:

```text
W000 -> FUNCTOR_OBL_001_Q_OBL_001_filtered_source_functor
```

Required tests:

1. Define or refute a functorial bridge `Phi: Compat_G^MLTT -> FiltSh(C)`.
2. Test whether SBP parity data is preserved as a flat `Z/2` local system.
3. Check `N` naturality.
4. Ground `Q` over the productive option set without circularly using future accepted schemas.
5. Reconcile `GAUGE-COV-OBL-001` and distortion-residue status with E049/E050/E052.

## Verdict

```yaml
Phi_parity_constructed: true
Phi_domain: finite_SBP_parity_subcategory_of_Compat_G_MLTT
Phi_target: filtered_finite_Cech_presheaves_with_flat_Z2_local_system
strict_total_Phi: not_proved_without_cover_parity_and_localization_data
SBP_parity_preserved: true_on_finite_parity_subcategory
N_strict_naturality: failed
N_replacement: filtered_lax_residual_equation
Q_global_productive_measure: killed
Q_prefix_local_conditional_weight: survives
GAUGE_COV_OBL_001: already_closed_for_structural_Compat_and_Compat_G_MLTT
distortion_residue: nonzero_for_SBP_incompatibility_guard
claim_status_change: none
path_kill_added: global_normalized_Q_over_productive_SBP_option_set_as_source_invariant
```

## 1. Domain and Target

Define the finite parity subcategory:

```text
SBPPar^MLTT(S0) subset Compat_G^MLTT
```

Objects are finite MLTT schema contexts reachable from `S0` by accepted SBP morphisms whose
local overlap data carries an E054-style parity value.

Morphisms are finite accepted SBP paths with proof terms:

```text
e: S -> S'
e carries:
  c_e                   -- new constraint
  pi_e                  -- constructed Compat_G^MLTT proof term
  chi(e) in Z/2          -- SBP polarity-flip parity
```

The target category is:

```text
FiltSh_Z2(C_fin)
```

Objects are finite filtered Cech presheaf/sheaf objects over a chosen finite cover `C_fin`,
equipped with a flat `Z/2` local system. The filtration is by schema stage. The `Z/2` local
system records the parity transition values:

```text
tau_e = (-1) ^ chi(e)
```

This target is deliberately finite and fixture-local. It is not the full GU/H3 target.

## 2. The Functor `Phi_par`

Define:

```text
Phi_par(S_n) =
  filtered Cech object whose local sections are constructed Compat_G^MLTT proof terms
  visible in the finite cover C_fin at stage n, with flat Z/2 transition values induced
  by accumulated SBP parity.
```

For an SBP morphism:

```text
e: S_n -> S_{n+1}
```

define:

```text
Phi_par(e): Phi_par(S_n) -> Phi_par(S_{n+1})
```

as the filtration extension that:

1. adjoins the new local proof term `pi_e`;
2. updates the overlap transition by `tau_e = (-1)^chi(e)`;
3. preserves prior restriction maps on the old cover data;
4. extends the flat `Z/2` local system by multiplication of transition signs.

### Identity

For `id_S`, no proof term is adjoined and `chi(id_S)=0`, so `tau_id=+1`.

```text
Phi_par(id_S) = id_{Phi_par(S)}
```

### Composition

For composable SBP morphisms:

```text
S --e1--> S' --e2--> S''
```

the accumulated parity is:

```text
chi(e2 o e1) = chi(e1) + chi(e2) mod 2
tau(e2 o e1) = tau(e1) * tau(e2)
```

The filtration extension also composes by adjoining proof terms in path order. Therefore:

```text
Phi_par(e2 o e1) = Phi_par(e2) o Phi_par(e1)
```

on the finite SBP-parity subcategory.

## 3. What This Proves

This discharges the finite bridge demanded by E059:

```text
odd SBP parity in Compat_G^MLTT
=> flat Z/2 transition in a finite filtered Cech object
```

The E054 cocycle is preserved by `Phi_par`: its two overlap signs map to a flat `Z/2`
local system whose loop product is `-1`.

This also explains why E054 was not merely AB contextuality. The transition signs are induced
by source-side compatibility/parity data, not chosen as an external transition table.

## 4. What This Does Not Prove

There is not yet a total canonical functor:

```text
Compat_G^MLTT -> FiltSh(C)
```

without additional data:

1. a finite or structured cover `C`;
2. a localization rule that sends proof terms to patches/overlaps;
3. a parity functional `chi` on the relevant SBP morphisms;
4. a rule for non-parity morphisms;
5. a comparison from the finite flat `Z/2` local-system data to the full GU/H3 target.

So the honest result is:

```text
Phi_par exists on the finite SBP-parity subcategory.
The full GU/H3 bridge remains open.
```

## 5. `N` Naturality

E031 defined:

```text
N(lambda, S) = |D4-Hom_lambda(S)| / |Hom_lambda(S)|
```

Strict naturality would require a canonical way to compare the D4 density at `S` with the
D4 density at `S'` for every morphism `e: S -> S'`.

That fails in the Godelian regime. An SBP morphism changes the future option space:

- it consumes or resolves some current options;
- it creates new admissibility proof terms;
- in the Godelian regime it can open productive successors not enumerable from the prefix.

There is no canonical commutative square making `N(lambda, -)` a strict natural
transformation over all of `Ext_S`.

The viable replacement is a filtered/lax residual equation:

```text
N(lambda, S') = transport_e(N(lambda, S)) + Delta_N(e)
```

where `Delta_N(e)` is the novelty-residue term created by the SBP update. In the finite
type-space regime, `Delta_N` is depletion-like. In the Godelian regime, `Delta_N` may be
productive and non-precommittable.

This is not a failure of TI. It is a useful result: strict naturality would erase the very
novelty `N` is supposed to measure.

## 6. `Q` Grounding

The old global form of `Q` wanted:

```text
Q(e) = -log Pr(e accepted)
```

over the whole productive SBP option set.

That cannot be made global without reintroducing a hidden completed option space. In the
Godelian regime the SBP space is productive and not c.e.; a normalized probability measure
over "all future SBP options" would require exactly the kind of completed oracle the MLTT
source model forbids.

So the global version is killed.

The surviving version is prefix-local:

```text
q_n(e) = P_n(e is accepted | e is proposed to quorum, S_n, I_n)
Q_n(e) = -log q_n(e)
```

where:

- `I_n` is the information available at stage `n`;
- the denominator is the finite/submitted proposal frontier, not the whole productive SBP
  space;
- acceptance is evaluated against the current shared admissibility predicate, not a future
  accepted schema;
- for composed paths:

```text
Q(e2 o e1) = Q_n(e1) + Q_{n+1}(e2 | e1)
```

This avoids circularity by making `Q` a conditional record/proposal weight, not a global
source invariant.

## 7. Gauge Covariance and Distortion Residue

RUN-0054 treated `GAUGE-COV-OBL-001` and distortion residue as pending. This run reconciles
that with E049/E050/E052:

- E049 closes `GAUGE-COV-OBL-001` for structural Compat, the SBP incompatibility guard, and
  RecCost. Family A remains conditional only in the sense that arbitrary name-dependent
  Compat instantiations are forbidden.
- E050 proves quorum equivariance under GAUGE-COV and verifies it for Family G.
- E052 shows these results survive under `Compat_G^MLTT`.

Therefore:

```text
GAUGE-COV-OBL-001 is closed for the operative structural / Compat_G^MLTT setting.
Distortion residue is nonzero for SBP morphisms with the incompatibility guard active.
```

Under `Phi_par`, the distortion residue appears as a filtration jump plus, when parity is
odd, a nontrivial `Z/2` transition. This is still not a full Ehresmannian transport functor
`A: ExtCat -> B G`, but it is now a source-conditioned filtered-sheaf witness.

## Path Killed

```yaml
path: global_normalized_Q_over_productive_SBP_option_set_as_source_invariant
reason_killed: >
  A global normalized Q over the whole productive SBP option set would require a completed
  probability space of all future SBP options. That imports the hidden completed oracle / fixed
  A_infty structure that Compat_G^MLTT explicitly forbids. Q can be made non-circular only as
  a prefix-local conditional weight on the currently proposed finite frontier.
local_minimum_risk: >
  Medium. This should not kill Q itself. It kills only the global source-invariant reading.
  Prefix-local Q remains useful for record/proposal cost, quorum surprise, and path weights.
possible_future_resurrection_trigger: >
  A constructive measure object over productive SBP options that is formed at stage n without
  enumerating or pre-containing future options, and that composes under accepted morphism paths
  without using future accepted schemas.
```

## Next Work

The next run should test whether the finite/lax result can carry the larger bridge:

```text
W000 -> H3_C1_C3_bridge_from_finite_filtered_functor
```

Required:

1. Try to extend `Phi_par` from `SBPPar^MLTT(S0)` to a broader filtered-sheaf target.
2. Decide whether the flat `Z/2` local-system class is enough for the GU/H3 bridge or remains
   a finite formal residue.
3. Pressure the C3 spacelike/correspondence geometry obligation directly.
4. Keep `Q` prefix-local unless a constructive non-oracular measure is supplied.
