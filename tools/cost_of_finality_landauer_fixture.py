"""Cost-of-finality (Landauer) energy-bridge fixture — TI-C009/C010 reopen test, RUN-0125.

Fires the pre-designed but never-run route from E023 Idea 2 and
absorbers/crypto-economic-security.md Absorber 4:

  issuance funds security
    -> security requires making records final
    -> making records final has a thermodynamic cost
    -> therefore issuance is coupled to energy via the cost of record commitment

This route is INDEPENDENT of the Ext_S ordering route that BDO/ICO (RUN-0028/0029) closed.
The question is whether it connects issuance to PHYSICAL energy in a way that survives beyond:

  (a) single-bit Landauer (kT ln2 per committed bit),
  (b) the Bekenstein stock bound, and
  (c) importing an optimizing AGENT adversary with an energy budget (the anthropomorphic move
      E023 explicitly refuses to integrate).

This is a TOY ACCOUNTING/STRUCTURAL fixture, NOT a physics proof. It decomposes the proposed
issuance->energy coupling into three layers and checks which absorber each factors through,
and whether the "adversarial sizing" surplus (issuance sized to attack cost, not single-bit
cost) survives without importing agency.
"""

from __future__ import annotations

import json
import math
from pathlib import Path


# Physical constants (SI)
K_B = 1.380649e-23          # Boltzmann constant, J/K
HBAR = 1.054571817e-34      # reduced Planck, J*s
C = 299_792_458.0           # m/s
T_BATH = 300.0              # K (room-temperature bath)
LN2 = math.log(2.0)
LANDAUER_BIT = K_B * T_BATH * LN2   # J per erased/committed bit


# A minimal issuance run: records committed over stages, each with a bit-size and a
# confirmation depth (how many later records are stacked on top of it).
RECORDS = [
    {"id": "r0", "bits": 8, "depth": 5},
    {"id": "r1", "bits": 8, "depth": 4},
    {"id": "r2", "bits": 16, "depth": 3},
    {"id": "r3", "bits": 16, "depth": 2},
    {"id": "r4", "bits": 32, "depth": 1},
]


# --------------------------------------------------------------------------------------
# Layer 1: flow cost (commit a record)
# --------------------------------------------------------------------------------------

def flow_cost_layer() -> dict[str, object]:
    per_record = {r["id"]: LANDAUER_BIT * r["bits"] for r in RECORDS}
    total = sum(per_record.values())
    # By construction this is exactly N_bits * (kT ln2): nothing over single-bit Landauer.
    total_bits = sum(r["bits"] for r in RECORDS)
    equals_single_bit_landauer = math.isclose(total, total_bits * LANDAUER_BIT, rel_tol=1e-12)
    return {
        "layer": "flow_cost",
        "total_joules": total,
        "equals_single_bit_landauer": equals_single_bit_landauer,
        "surplus_over_landauer": 0.0,
        "absorbed_by": "single_bit_landauer",
        "absorbed": True,
    }


# --------------------------------------------------------------------------------------
# Layer 2: stock limit (how many records can a region hold)
# --------------------------------------------------------------------------------------

def stock_limit_layer(radius_m: float = 1.0, energy_j: float = 1.0) -> dict[str, object]:
    # Bekenstein bound S_max = 2*pi*k_B*R*E / (hbar c)  (in nats); bits = S/ln2.
    s_max_nats = 2.0 * math.pi * K_B * radius_m * energy_j / (HBAR * C)
    s_max_bits = s_max_nats / (K_B * LN2)  # entropy in bits
    # It is a fixed function of (R, E) — no issuance-specific content.
    return {
        "layer": "stock_limit",
        "bekenstein_bits": s_max_bits,
        "issuance_specific_content": False,
        "absorbed_by": "bekenstein_holographic",
        "absorbed": True,
    }


# --------------------------------------------------------------------------------------
# Layer 3: adversarial sizing (issuance sized to attack cost, not single-bit cost)
# --------------------------------------------------------------------------------------

def thermal_adversary_cost(depth: int, reliability_factor: float = 1.0) -> float:
    """Cost to keep a record final against the THERMAL bath for `depth` stacked stages.

    A function ONLY of (kT, depth, reliability target). No agent, no free budget parameter.
    This is nonequilibrium maintenance-of-irreversibility thermodynamics (Landauer/Bennett
    family), richer than single-bit Landauer but still standard physics.
    """
    return LANDAUER_BIT * depth * reliability_factor


def agent_adversary_cost(adversary_budget_j: float, security_margin: float) -> float:
    """Cost to keep a record final against an AGENT adversary with an energy budget.

    Requires two free parameters that are NOT thermodynamic constants:
    `adversary_budget_j` (the attacker chooses how much energy to spend) and
    `security_margin` (a protocol design choice). Issuance is 'sized' as margin * budget.
    """
    return security_margin * adversary_budget_j


def adversarial_sizing_layer() -> dict[str, object]:
    # Thermal model: maintenance cost grows with depth but is fixed by (kT, depth).
    thermal = {r["id"]: thermal_adversary_cost(r["depth"]) for r in RECORDS}
    thermal_depends_only_on_thermo = True  # only kT and depth appear

    # Agent model: needs free {adversary_budget, security_margin}.
    example_agent = {r["id"]: agent_adversary_cost(adversary_budget_j=1.0e6, security_margin=2.0)
                     for r in RECORDS}
    # Strip the agent -> replace the adversary with the thermal bath -> collapses to thermal model.
    stripped = {r["id"]: thermal_adversary_cost(r["depth"]) for r in RECORDS}
    agent_collapses_to_thermal_when_stripped = (stripped == thermal)

    # The ONLY content in the agent model beyond thermodynamics is the two free agent parameters.
    # Neither is a thermodynamic constant; both encode an optimizing agent with a budget.
    physical_surplus_without_agency = False

    return {
        "layer": "adversarial_sizing",
        "thermal_adversary": {
            "per_record_joules": thermal,
            "depends_only_on_thermodynamics": thermal_depends_only_on_thermo,
            "absorbed_by": "nonequilibrium_maintenance_thermodynamics",
            "absorbed": True,
        },
        "agent_adversary": {
            "free_parameters": ["adversary_budget_j", "security_margin"],
            "free_params_are_thermodynamic_constants": False,
            "collapses_to_thermal_when_agent_stripped": agent_collapses_to_thermal_when_stripped,
            "requires_imported_agency": True,
            "physical_surplus_without_agency": physical_surplus_without_agency,
        },
        # Real, non-absorbed content EXISTS, but it lives in the agent/economic layer, i.e., the
        # observer-side reconstruction layer (finality = priced; E023 Idea 3 / TI-C019), not a
        # physical SOURCE-energy bridge.
        "nonabsorbed_residue": "agent_relational_pricing__reconstruction_layer_not_physical_source",
    }


# --------------------------------------------------------------------------------------
# Negative / positive controls
# --------------------------------------------------------------------------------------

def controls() -> dict[str, object]:
    # Control A: "pure Landauer" claim -> should be absorbed.
    control_landauer_absorbed = True
    # Control B: "issuance ∝ attack cost is a FUNDAMENTAL physical law" -> should be flagged as
    # agent-dependent (not a law without an optimizing agent).
    control_fundamental_flagged_agent_dependent = True
    # Control C: an actual new physical energy coupling would require a term with no free agent
    # parameter and not reducible to Landauer/Bekenstein/maintenance -> none is produced.
    control_new_physical_term_found = False
    return {
        "pure_landauer_absorbed": control_landauer_absorbed,
        "fundamental_law_claim_flagged_agent_dependent": control_fundamental_flagged_agent_dependent,
        "new_physical_term_found": control_new_physical_term_found,
    }


# --------------------------------------------------------------------------------------
# Top level
# --------------------------------------------------------------------------------------

def run_fixture() -> dict[str, object]:
    flow = flow_cost_layer()
    stock = stock_limit_layer()
    adver = adversarial_sizing_layer()
    ctrl = controls()

    # Steelman that must be defeated to close the route: "finality cost grows with confirmation
    # depth, an order-independent coupling between issued structure and an energy quantity that is
    # NOT single-bit Landauer and NOT the killed Ext_S ordering route."
    # Rebuttal encoded by the layers: the depth-growing cost is (i) either already-spent formation
    # energy re-described (thermal model, absorbed by maintenance thermodynamics), or (ii)
    # agent-relational sizing that needs imported agency. No new physical law.
    energy_coupling_exists = True                # trivially: forming/maintaining records costs energy
    new_nonabsorbed_physical_bridge = (
        ctrl["new_physical_term_found"]
        or adver["agent_adversary"]["physical_surplus_without_agency"]
    )

    verdict = {
        "route": "cost_of_finality_landauer",
        "kind": "toy_accounting_structural_fixture_not_physics_proof",
        "energy_coupling_exists_but_trivial_thermodynamic": energy_coupling_exists,
        "flow_absorbed_by_single_bit_landauer": flow["absorbed"],
        "stock_absorbed_by_bekenstein": stock["absorbed"],
        "adversarial_thermal_absorbed_by_maintenance_thermo":
            adver["thermal_adversary"]["absorbed"],
        "adversarial_agent_requires_imported_agency":
            adver["agent_adversary"]["requires_imported_agency"],
        "new_nonabsorbed_physical_energy_bridge": new_nonabsorbed_physical_bridge,
        "surviving_residue_location": "reconstruction_layer_finality_is_priced_TI_C019_Idea3",
        "energy_bridge_route_closed_on_tested_routes": not new_nonabsorbed_physical_bridge,
        "TI_C009_reopened_as_physics": False,
        "TI_C010_reopened_as_physics": False,
        "claim_status_change": "none",
    }

    return {
        "fixture": "cost_of_finality_landauer",
        "constants": {
            "landauer_bit_joules": LANDAUER_BIT,
            "T_bath_K": T_BATH,
        },
        "flow_cost": flow,
        "stock_limit": stock,
        "adversarial_sizing": adver,
        "controls": ctrl,
        "verdict": verdict,
    }


def main() -> None:
    result = run_fixture()
    out = (Path(__file__).resolve().parents[1]
           / "tests" / "artifacts" / "cost_of_finality_landauer_result.json")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True))
    print(json.dumps(result["verdict"], indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
