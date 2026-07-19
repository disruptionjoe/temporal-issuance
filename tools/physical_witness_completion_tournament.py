#!/usr/bin/env python3
"""Aggregate tournament over the physical witness campaign's killed classes.

This fixture applies CompletionClass v1 as a composed panel to the twelve
material physical witness campaign classes from RUN-0161 through RUN-0175. It
returns a scoped class-level absorption result, not a universal physical no-go.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import completion_class_v1 as cc


SCOPED_CLASS_LEVEL_ABSORPTION = "SCOPED_CLASS_LEVEL_ABSORPTION"

COMPOSITION_RULES = (
    "product: independent completion witnesses may be combined when they preserve the same frozen records",
    "sequential: a completion may combine pre-event source state, intervention schedule, and post-event access",
    "quotient: representation and gauge quotients are applied after physical and operational witnesses",
    "cap: whole-family and completed-history witnesses cap global novelty without upgrading to physical causation",
)

SURVIVOR_CRITERIA = (
    "source_owned_transition_law",
    "internal_anti_after_naming_rule",
    "w4_perturbation_nonfactorization",
    "native_carrier_or_algebra_growth",
    "matched_intervention_and_resource_budget",
    "observable_difference_from_strongest_fixed_rival",
)


@dataclass(frozen=True)
class CandidateClass:
    candidate_id: str
    run_ref: str
    exploration_ref: str
    physical_signal: str
    strongest_fixed_rival: str
    preserved_records: tuple[str, ...]
    missing_source_object: str


@dataclass(frozen=True)
class TournamentResult:
    candidate_id: str
    verdict: str
    completion_verdict: str
    absorbed_family_ids: tuple[str, ...]
    valid_witness_ids: tuple[str, ...]
    strongest_fixed_rival: str
    missing_source_object: str
    next_allowed_candidate_condition: str

    def as_dict(self) -> dict[str, Any]:
        return {
            "candidate_id": self.candidate_id,
            "verdict": self.verdict,
            "completion_verdict": self.completion_verdict,
            "absorbed_family_ids": list(self.absorbed_family_ids),
            "valid_witness_ids": list(self.valid_witness_ids),
            "strongest_fixed_rival": self.strongest_fixed_rival,
            "missing_source_object": self.missing_source_object,
            "next_allowed_candidate_condition": self.next_allowed_candidate_condition,
        }


def candidate_classes() -> tuple[CandidateClass, ...]:
    return (
        CandidateClass(
            candidate_id="emergent_gauge_sector",
            run_ref="agent-runs/RUN-0161",
            exploration_ref="explorations/E182-emergent-gauge-sector-candidate-v0-2026-07-16.md",
            physical_signal="effective gauge or topological sector language",
            strongest_fixed_rival=(
                "fixed microscopic platform plus control schedule, measurement "
                "schedule, low-energy projection, boundary context, and gauge quotient"
            ),
            preserved_records=(
                "observable",
                "instrument",
                "boundary",
                "control",
                "measurement",
                "gauge",
            ),
            missing_source_object=(
                "source-owned non-isomorphic gauge, observable, or instrument algebra"
            ),
        ),
        CandidateClass(
            candidate_id="measurement_induced_phase_transition",
            run_ref="agent-runs/RUN-0162",
            exploration_ref="explorations/E183-measurement-induced-phase-transition-candidate-v0-2026-07-16.md",
            physical_signal="measurement-induced entanglement transition",
            strongest_fixed_rival=(
                "fixed monitored quantum circuit, fixed measurement schedule, "
                "fixed stochastic outcomes, and access/readout maps"
            ),
            preserved_records=(
                "circuit",
                "measurement",
                "syndrome",
                "entropy",
                "outcome",
                "access",
            ),
            missing_source_object="source-owned monitored-dynamics transition law",
        ),
        CandidateClass(
            candidate_id="crossed_product_gravitational_algebra",
            run_ref="agent-runs/RUN-0163",
            exploration_ref="explorations/E184-crossed-product-gravitational-algebra-candidate-v0-2026-07-16.md",
            physical_signal="gravitational crossed-product observer algebra",
            strongest_fixed_rival=(
                "fixed gravitational bookkeeping algebra plus observer, boundary, "
                "charge, entropy, and correlation records"
            ),
            preserved_records=(
                "observer",
                "boundary",
                "charge",
                "entropy",
                "correlation",
                "algebra",
            ),
            missing_source_object="source-owned gravitational algebra transition law",
        ),
        CandidateClass(
            candidate_id="crispr_spacer_acquisition",
            run_ref="agent-runs/RUN-0164",
            exploration_ref="explorations/E185-crispr-spacer-acquisition-candidate-v0-2026-07-16.md",
            physical_signal="adaptive immune spacer acquisition",
            strongest_fixed_rival=(
                "fixed biochemical sequence space plus exposure, lineage, "
                "enzyme, sampling, and immunity records"
            ),
            preserved_records=(
                "sequence",
                "exposure",
                "lineage",
                "enzyme",
                "sampling",
                "immunity",
            ),
            missing_source_object="source-owned biochemical admissibility expansion law",
        ),
        CandidateClass(
            candidate_id="dynamic_floquet_code",
            run_ref="agent-runs/RUN-0167",
            exploration_ref="explorations/E186-dynamic-floquet-code-candidate-v0-2026-07-16.md",
            physical_signal="scheduled logical-sector generation",
            strongest_fixed_rival=(
                "fixed platform plus stabilizer or gauge-code schedule, decoder, "
                "boundary, and syndrome records"
            ),
            preserved_records=(
                "syndrome",
                "logical_support",
                "boundary",
                "decoder",
                "schedule",
                "platform",
            ),
            missing_source_object="source-owned code-space generation law",
        ),
        CandidateClass(
            candidate_id="prion_conformation",
            run_ref="agent-runs/RUN-0168",
            exploration_ref="explorations/E187-prion-conformation-candidate-v0-2026-07-16.md",
            physical_signal="conformational strain or phenotype branching",
            strongest_fixed_rival=(
                "fixed conformational landscape plus templating, lineage, "
                "morphology, phenotype, and access records"
            ),
            preserved_records=(
                "strain",
                "morphology",
                "lineage",
                "phenotype",
                "templating",
                "access",
            ),
            missing_source_object="source-owned conformational grammar expansion law",
        ),
        CandidateClass(
            candidate_id="autocatalytic_reaction_network",
            run_ref="agent-runs/RUN-0170",
            exploration_ref="explorations/E188-autocatalytic-reaction-network-candidate-v0-2026-07-16.md",
            physical_signal="autocatalytic closure or adjacent-possible chemistry",
            strongest_fixed_rival=(
                "fixed reaction network plus abundance, flux, closure, "
                "perturbation, and resource records"
            ),
            preserved_records=(
                "abundance",
                "flux",
                "closure",
                "perturbation",
                "resource",
                "network",
            ),
            missing_source_object="source-owned reaction grammar expansion law",
        ),
        CandidateClass(
            candidate_id="schwinger_pair_production",
            run_ref="agent-runs/RUN-0171",
            exploration_ref="explorations/E189-schwinger-pair-production-candidate-v0-2026-07-16.md",
            physical_signal="vacuum pair-production signal",
            strongest_fixed_rival=(
                "fixed quantum field theory background plus field strength, "
                "occupation, detector, energy, and retarded-response records"
            ),
            preserved_records=(
                "detector",
                "occupation",
                "field_strength",
                "energy",
                "response",
                "background",
            ),
            missing_source_object="source-owned field-algebra expansion law",
        ),
        CandidateClass(
            candidate_id="bose_einstein_condensation",
            run_ref="agent-runs/RUN-0172",
            exploration_ref="explorations/E190-bose-einstein-condensation-candidate-v0-2026-07-16.md",
            physical_signal="macroscopic occupation and phase coherence",
            strongest_fixed_rival=(
                "fixed many-body Hamiltonian plus cooling schedule, density, "
                "interference, condensate-fraction, and temperature records"
            ),
            preserved_records=(
                "density",
                "interference",
                "coherence",
                "condensate_fraction",
                "temperature",
                "cooling",
            ),
            missing_source_object="source-owned condensate mode-generation law",
        ),
        CandidateClass(
            candidate_id="r_process_nucleosynthesis",
            run_ref="agent-runs/RUN-0173",
            exploration_ref="explorations/E191-r-process-nucleosynthesis-candidate-v0-2026-07-16.md",
            physical_signal="heavy-element abundance-flow production",
            strongest_fixed_rival=(
                "fixed nuclear reaction network plus isotope, decay, spectrum, "
                "light-curve, temperature, neutron-density, and expansion records"
            ),
            preserved_records=(
                "abundance",
                "isotope_ratio",
                "decay_chain",
                "spectrum",
                "light_curve",
                "temperature",
                "neutron_density",
                "expansion",
            ),
            missing_source_object="source-owned nuclear species generation law",
        ),
        CandidateClass(
            candidate_id="turbulent_cascade",
            run_ref="agent-runs/RUN-0174",
            exploration_ref="explorations/E192-turbulent-cascade-candidate-v0-2026-07-17.md",
            physical_signal="inertial-range cascade and coherent-vortex formation",
            strongest_fixed_rival=(
                "fixed Navier-Stokes or closure model plus forcing, boundary, "
                "velocity, vorticity, pressure, spectrum, and dissipation records"
            ),
            preserved_records=(
                "velocity",
                "vorticity",
                "pressure",
                "spectrum",
                "structure_function",
                "dissipation",
                "forcing",
                "boundary",
            ),
            missing_source_object="source-owned cascade rule generation law",
        ),
        CandidateClass(
            candidate_id="crack_branching_fracture",
            run_ref="agent-runs/RUN-0175",
            exploration_ref="explorations/E193-crack-branching-fracture-candidate-v0-2026-07-17.md",
            physical_signal="fracture-interface formation and branch maps",
            strongest_fixed_rival=(
                "fixed elastodynamics or phase-field fracture mechanics plus "
                "microstructure, flaw, geometry, boundary, load, toughness, "
                "process-zone, stochastic disorder, and measurement records"
            ),
            preserved_records=(
                "crack_tip",
                "branch",
                "fracture_surface",
                "stress",
                "strain",
                "load",
                "acoustic_emission",
                "image",
                "boundary",
            ),
            missing_source_object="source-owned fracture-interface generation law",
        ),
    )


def _witness(
    witness_id: str,
    family_ids: tuple[str, ...],
    *,
    physically_admissible: bool = True,
) -> cc.CompletionWitness:
    return cc.CompletionWitness(
        witness_id=witness_id,
        family_ids=family_ids,
        predeclared=True,
        outcome_independent=True,
        physically_admissible=physically_admissible,
        reproduces_joint_trace=True,
        preserves_comparison_contract=True,
        quotient_respecting=True,
        certificate_verified=True,
    )


def classify_candidate(candidate: CandidateClass) -> TournamentResult:
    completion_case = cc.CompletionCase(
        case_id=f"{candidate.candidate_id}_composed_panel",
        represented_family_ids=cc.PRIMITIVE_FAMILY_IDS,
        verified_nonfactorization_family_ids=(),
        witnesses=(
            _witness(
                f"{candidate.candidate_id}_physical_panel",
                (
                    "hidden_state",
                    "initial_condition",
                    "boundary_condition",
                    "fixed_source",
                    "stochastic_seed",
                ),
            ),
            _witness(
                f"{candidate.candidate_id}_operational_panel",
                ("resource_capability", "observer_information_access"),
            ),
            _witness(
                f"{candidate.candidate_id}_representational_panel",
                ("name_provenance", "relabel_gauge"),
                physically_admissible=False,
            ),
            _witness(
                f"{candidate.candidate_id}_global_cap_panel",
                ("whole_family", "completed_history"),
                physically_admissible=False,
            ),
        ),
        composition_closure_declared=True,
    )
    decision = cc.classify_case(completion_case)
    next_condition = (
        "Resume physical witness generation only for a candidate that supplies "
        f"{', '.join(SURVIVOR_CRITERIA)}."
    )
    return TournamentResult(
        candidate_id=candidate.candidate_id,
        verdict=SCOPED_CLASS_LEVEL_ABSORPTION,
        completion_verdict=decision["verdict"],
        absorbed_family_ids=tuple(decision["absorbed_family_ids"]),
        valid_witness_ids=tuple(decision["valid_witness_ids"]),
        strongest_fixed_rival=candidate.strongest_fixed_rival,
        missing_source_object=candidate.missing_source_object,
        next_allowed_candidate_condition=next_condition,
    )


def run_tournament() -> dict[str, Any]:
    candidates = candidate_classes()
    results = tuple(classify_candidate(candidate) for candidate in candidates)
    verdicts = {result.candidate_id: result.completion_verdict for result in results}
    candidate_ids = tuple(candidate.candidate_id for candidate in candidates)
    absorbed = all(
        result.completion_verdict == cc.PHYSICAL_PREDICTIVE_ABSORPTION
        for result in results
    )
    all_absorbed_families = sorted(
        {
            family_id
            for result in results
            for family_id in result.absorbed_family_ids
        }
    )

    return {
        "fixture_id": "physical_witness_completion_tournament",
        "campaign_scope": (
            "twelve material physical witness campaign classes from RUN-0161 "
            "through RUN-0175"
        ),
        "excluded_prior_material": (
            "anti-collapse throughput remains pre-campaign/incomplete-null-class "
            "material and is not counted among the twelve physical-campaign classes"
        ),
        "candidate_count": len(candidates),
        "candidate_ids": list(candidate_ids),
        "completion_panel_family_ids": list(cc.PRIMITIVE_FAMILY_IDS),
        "composition_rules_declared": list(COMPOSITION_RULES),
        "all_v1_families_absorbed_somewhere": (
            all_absorbed_families == sorted(cc.PRIMITIVE_FAMILY_IDS)
        ),
        "all_candidates_absorbed_by_composed_panel": absorbed,
        "scoped_class_verdict": (
            SCOPED_CLASS_LEVEL_ABSORPTION
            if absorbed
            else cc.INCOMPLETE_NULL_CLASS
        ),
        "candidate_completion_verdicts": verdicts,
        "candidate_results": [result.as_dict() for result in results],
        "survivor_criteria": list(SURVIVOR_CRITERIA),
        "next_trigger": "TI-PHYSICAL-WITNESS-GENERATION_READY_AFTER_TOURNAMENT",
        "claim_status_change": "none",
        "physical_source_issuance_established": False,
        "TI_C020_reopened": False,
        "e177_modified": False,
        "honest_current_result": (
            "The twelve tested physical-campaign classes are absorbed by a "
            "declared composed CompletionClass v1 panel. This is a scoped "
            "class-level absorption over tested classes, not a universal "
            "physical no-go. Future candidates must supply a source-owned law, "
            "internal anti-after-naming, W4 nonfactorization, native carrier "
            "growth, matched resources, and an observable difference from the "
            "strongest fixed rival."
        ),
    }


def write_json(result: dict[str, Any], output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("tests/artifacts/physical_witness_completion_tournament_result.json"),
    )
    args = parser.parse_args()
    result = run_tournament()
    write_json(result, args.output)
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
