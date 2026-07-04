"""CelExt celestial-boundary fixture, steps 1-6 (RUN-0126/RUN-0127).

Toy category fragment only. This does not derive BMS physics, define Q_f, or
prove that Temporal Issuance supplies a completed celestial boundary theory.

It executes the six obligations from E013:

1. typed boundary source object on S^2,
2. admissible boundary insertion changing a soft-charge sector,
3. additive composition of admissible insertions.
4. supertranslation-like action preserving objects, morphisms, and composition,
5. Q_f-like charge determined from boundary data rather than bulk data,
6. absorber check against celestial S-matrix relabeling.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any


FORBIDDEN_INPUTS = {
    "bulk_hamiltonian",
    "bulk_s_matrix",
    "celestial_s_matrix",
    "celestial_amplitude_table",
    "radiative_phase_space",
    "bulk_stress_tensor",
    "precomputed_bms_charge",
    "target_side_q_f",
}

REQUIRED_OBJECT_CONSTRAINTS = {
    "celestial_sphere_S2",
    "soft_charge_sector:int",
    "ward_identity_label",
}


@dataclass(frozen=True)
class BoundaryObject:
    object_id: str
    sphere: str
    soft_charge: int
    hard_sector: str
    constraints: tuple[str, ...]
    primitive_sources: tuple[str, ...] = (
        "boundary_sector_label",
        "ward_identity_label",
    )
    forbidden_refs: tuple[str, ...] = ()


@dataclass(frozen=True)
class BoundaryInsertion:
    morphism_id: str
    source: BoundaryObject
    target: BoundaryObject
    soft_shift: int
    operator_family: str
    ward_identity_preserved: bool = True
    admissibility_witness: str = "charge_sector_shift_matches_target"
    composition_trace: tuple[str, ...] = ()
    primitive_sources: tuple[str, ...] = (
        "boundary_operator_family",
        "ward_identity_label",
    )
    forbidden_refs: tuple[str, ...] = ()


@dataclass(frozen=True)
class SupertranslationAction:
    action_id: str
    mode_label: str
    charge_offset: int
    q_weight: int
    primitive_sources: tuple[str, ...] = (
        "boundary_supertranslation_label",
        "ward_identity_label",
    )
    forbidden_refs: tuple[str, ...] = ()


def forbidden_refs_used(
    *items: BoundaryObject | BoundaryInsertion | SupertranslationAction,
) -> list[str]:
    used: set[str] = set()
    for item in items:
        used.update(set(item.forbidden_refs).intersection(FORBIDDEN_INPUTS))
    return sorted(used)


def object_report(obj: BoundaryObject) -> dict[str, Any]:
    required_present = REQUIRED_OBJECT_CONSTRAINTS <= set(obj.constraints)
    no_forbidden = not forbidden_refs_used(obj)
    typed = obj.sphere == "S2" and isinstance(obj.soft_charge, int) and required_present
    return {
        "object_id": obj.object_id,
        "sphere": obj.sphere,
        "soft_charge": obj.soft_charge,
        "hard_sector": obj.hard_sector,
        "constraints": list(obj.constraints),
        "required_constraints_present": required_present,
        "forbidden_inputs_used": forbidden_refs_used(obj),
        "typed_boundary_object": typed and no_forbidden,
        "reason": (
            "Object is an S2 boundary sector with an integer soft-charge label and "
            "explicit Ward/admissibility labels."
            if typed and no_forbidden
            else "Object is missing required source-side boundary typing or imports forbidden data."
        ),
    }


def admissibility_report(morphism: BoundaryInsertion) -> dict[str, Any]:
    expected_target_charge = morphism.source.soft_charge + morphism.soft_shift
    target_charge_matches = morphism.target.soft_charge == expected_target_charge
    source_ok = object_report(morphism.source)["typed_boundary_object"]
    target_ok = object_report(morphism.target)["typed_boundary_object"]
    no_forbidden = not forbidden_refs_used(morphism)
    admissible = (
        source_ok
        and target_ok
        and target_charge_matches
        and morphism.ward_identity_preserved
        and no_forbidden
    )
    return {
        "morphism_id": morphism.morphism_id,
        "source": morphism.source.object_id,
        "target": morphism.target.object_id,
        "soft_shift": morphism.soft_shift,
        "expected_target_charge": expected_target_charge,
        "actual_target_charge": morphism.target.soft_charge,
        "target_charge_matches": target_charge_matches,
        "ward_identity_preserved": morphism.ward_identity_preserved,
        "forbidden_inputs_used": forbidden_refs_used(morphism),
        "admissible_boundary_morphism": admissible,
        "reason": (
            "Morphism is source-side admissible: it maps between typed boundary sectors, "
            "changes the soft-charge label by its declared shift, and preserves the "
            "Ward/admissibility label without importing bulk data."
            if admissible
            else "Morphism is not source-side admissible under the step-2 fixture."
        ),
    }


def compose(first: BoundaryInsertion, second: BoundaryInsertion) -> BoundaryInsertion:
    if first.target.object_id != second.source.object_id:
        raise ValueError("cannot compose insertions with non-matching boundary sectors")
    return BoundaryInsertion(
        morphism_id=f"{second.morphism_id}_after_{first.morphism_id}",
        source=first.source,
        target=second.target,
        soft_shift=first.soft_shift + second.soft_shift,
        operator_family=f"{second.operator_family}_after_{first.operator_family}",
        ward_identity_preserved=(
            first.ward_identity_preserved and second.ward_identity_preserved
        ),
        admissibility_witness="additive_charge_shift_composition",
        composition_trace=(first.morphism_id, second.morphism_id),
        primitive_sources=tuple(
            dict.fromkeys(first.primitive_sources + second.primitive_sources)
        ),
        forbidden_refs=first.forbidden_refs + second.forbidden_refs,
    )


def composition_report(first: BoundaryInsertion, second: BoundaryInsertion) -> dict[str, Any]:
    try:
        composite = compose(first, second)
    except ValueError as exc:
        return {
            "composable": False,
            "error": str(exc),
            "additive_composition": False,
        }

    first_report = admissibility_report(first)
    second_report = admissibility_report(second)
    composite_report = admissibility_report(composite)
    additive = (
        composite.soft_shift == first.soft_shift + second.soft_shift
        and composite.target.soft_charge
        == composite.source.soft_charge + first.soft_shift + second.soft_shift
    )
    return {
        "composable": True,
        "first": first_report,
        "second": second_report,
        "composite": composite_report,
        "composition_trace": list(composite.composition_trace),
        "additive_composition": additive
        and first_report["admissible_boundary_morphism"]
        and second_report["admissible_boundary_morphism"]
        and composite_report["admissible_boundary_morphism"],
    }


def boundary_object(object_id: str, soft_charge: int) -> BoundaryObject:
    return BoundaryObject(
        object_id=object_id,
        sphere="S2",
        soft_charge=soft_charge,
        hard_sector="finite_hard_sector_label",
        constraints=tuple(sorted(REQUIRED_OBJECT_CONSTRAINTS)),
    )


def identity_insertion(obj: BoundaryObject) -> BoundaryInsertion:
    return BoundaryInsertion(
        morphism_id=f"id_{obj.object_id}",
        source=obj,
        target=obj,
        soft_shift=0,
        operator_family="identity_boundary_insertion",
        admissibility_witness="identity_boundary_insertion",
    )


def apply_supertranslation_to_object(
    obj: BoundaryObject,
    action: SupertranslationAction,
) -> BoundaryObject:
    return BoundaryObject(
        object_id=f"{action.action_id}({obj.object_id})",
        sphere=obj.sphere,
        soft_charge=obj.soft_charge + action.charge_offset,
        hard_sector=obj.hard_sector,
        constraints=obj.constraints,
        primitive_sources=tuple(
            dict.fromkeys(obj.primitive_sources + action.primitive_sources)
        ),
        forbidden_refs=obj.forbidden_refs + action.forbidden_refs,
    )


def apply_supertranslation_to_morphism(
    morphism: BoundaryInsertion,
    action: SupertranslationAction,
) -> BoundaryInsertion:
    transformed_trace = (
        tuple(f"{action.action_id}({step})" for step in morphism.composition_trace)
        if morphism.composition_trace
        else ()
    )
    return BoundaryInsertion(
        morphism_id=f"{action.action_id}({morphism.morphism_id})",
        source=apply_supertranslation_to_object(morphism.source, action),
        target=apply_supertranslation_to_object(morphism.target, action),
        soft_shift=morphism.soft_shift,
        operator_family=morphism.operator_family,
        ward_identity_preserved=morphism.ward_identity_preserved,
        admissibility_witness=(
            f"{morphism.admissibility_witness}_after_supertranslation"
        ),
        composition_trace=transformed_trace,
        primitive_sources=tuple(
            dict.fromkeys(morphism.primitive_sources + action.primitive_sources)
        ),
        forbidden_refs=morphism.forbidden_refs + action.forbidden_refs,
    )


def same_boundary_arrow(left: BoundaryInsertion, right: BoundaryInsertion) -> bool:
    return (
        left.source.soft_charge == right.source.soft_charge
        and left.target.soft_charge == right.target.soft_charge
        and left.soft_shift == right.soft_shift
        and left.operator_family == right.operator_family
        and left.ward_identity_preserved == right.ward_identity_preserved
    )


def supertranslation_functoriality_report(
    first: BoundaryInsertion,
    second: BoundaryInsertion,
    action: SupertranslationAction,
) -> dict[str, Any]:
    original_composite = compose(first, second)
    transformed_first = apply_supertranslation_to_morphism(first, action)
    transformed_second = apply_supertranslation_to_morphism(second, action)
    transformed_composite_direct = apply_supertranslation_to_morphism(
        original_composite,
        action,
    )
    transformed_composite_via_parts = compose(transformed_first, transformed_second)
    original_identity = identity_insertion(first.source)
    transformed_identity_direct = apply_supertranslation_to_morphism(
        original_identity,
        action,
    )
    transformed_identity_expected = identity_insertion(
        apply_supertranslation_to_object(first.source, action)
    )

    transformed_reports = [
        admissibility_report(transformed_first),
        admissibility_report(transformed_second),
        admissibility_report(transformed_composite_direct),
        admissibility_report(transformed_composite_via_parts),
        admissibility_report(transformed_identity_direct),
    ]
    identity_preserved = same_boundary_arrow(
        transformed_identity_direct,
        transformed_identity_expected,
    )
    composition_preserved = same_boundary_arrow(
        transformed_composite_direct,
        transformed_composite_via_parts,
    )
    admissibility_preserved = all(
        report["admissible_boundary_morphism"] for report in transformed_reports
    )
    action_has_no_forbidden_refs = not forbidden_refs_used(action)
    functorial = (
        action_has_no_forbidden_refs
        and identity_preserved
        and composition_preserved
        and admissibility_preserved
    )
    return {
        "action_id": action.action_id,
        "mode_label": action.mode_label,
        "charge_offset": action.charge_offset,
        "q_weight": action.q_weight,
        "forbidden_inputs_used": forbidden_refs_used(action),
        "identity_preserved": identity_preserved,
        "composition_preserved": composition_preserved,
        "admissibility_preserved": admissibility_preserved,
        "transformed_first": transformed_reports[0],
        "transformed_second": transformed_reports[1],
        "transformed_composite_direct": transformed_reports[2],
        "transformed_composite_via_parts": transformed_reports[3],
        "BMS_functoriality": functorial,
        "reason": (
            "The supertranslation-like action shifts every boundary sector by a constant offset, "
            "leaves morphism soft shifts invariant, preserves identity arrows, and commutes with additive composition."
            if functorial
            else "The action does not satisfy the toy functoriality checks."
        ),
    }


def soft_charge_functional_report(
    morphism: BoundaryInsertion,
    action: SupertranslationAction,
) -> dict[str, Any]:
    forbidden_inputs = forbidden_refs_used(morphism, action)
    delta_from_boundary_sectors = morphism.target.soft_charge - morphism.source.soft_charge
    q_from_boundary = action.q_weight * delta_from_boundary_sectors
    q_from_declared_shift = action.q_weight * morphism.soft_shift
    admissible = admissibility_report(morphism)["admissible_boundary_morphism"]
    determined = (
        admissible
        and not forbidden_inputs
        and q_from_boundary == q_from_declared_shift
    )
    return {
        "morphism_id": morphism.morphism_id,
        "action_id": action.action_id,
        "formula": "Q_f(e) = f_weight * (q_target - q_source)",
        "q_value": q_from_boundary,
        "q_from_declared_shift": q_from_declared_shift,
        "boundary_sector_delta": delta_from_boundary_sectors,
        "forbidden_inputs_used": forbidden_inputs,
        "uses_bulk_hamiltonian": "bulk_hamiltonian" in forbidden_inputs,
        "uses_bulk_s_matrix": "bulk_s_matrix" in forbidden_inputs,
        "uses_precomputed_bms_charge": "precomputed_bms_charge" in forbidden_inputs,
        "source_side_Q_f": determined,
        "source_side_relative_to_celext": determined,
        "source_side_relative_to_current_TI_primitives": False,
        "reason": (
            "The toy Q_f value is determined from boundary sector labels and the supertranslation generator weight, "
            "without importing a bulk Hamiltonian, bulk S-matrix, or precomputed BMS charge."
            if determined
            else "Q_f is not source-side under this fixture because it depends on forbidden or mismatched data."
        ),
    }


def absorber_report(
    morphism: BoundaryInsertion,
    action: SupertranslationAction,
) -> dict[str, Any]:
    b0 = boundary_object("B_q0", 0)
    b1 = boundary_object("B_q1", 1)
    s_matrix_relabel = BoundaryInsertion(
        morphism_id="celestial_s_matrix_relabeling_control",
        source=b0,
        target=b1,
        soft_shift=1,
        operator_family="celestial_s_matrix_relabel",
        forbidden_refs=("celestial_s_matrix", "bulk_s_matrix"),
    )
    imported_q = BoundaryInsertion(
        morphism_id="precomputed_bms_charge_control",
        source=b0,
        target=b1,
        soft_shift=1,
        operator_family="boundary_soft_insertion",
        forbidden_refs=("precomputed_bms_charge",),
    )
    positive_q = soft_charge_functional_report(morphism, action)
    relabel_q = soft_charge_functional_report(s_matrix_relabel, action)
    imported_q_report = soft_charge_functional_report(imported_q, action)
    positive_independent = (
        positive_q["source_side_Q_f"]
        and "celestial_s_matrix" not in positive_q["forbidden_inputs_used"]
        and "bulk_s_matrix" not in positive_q["forbidden_inputs_used"]
    )
    relabeling_rejected = not relabel_q["source_side_Q_f"]
    imported_q_rejected = not imported_q_report["source_side_Q_f"]
    absorbed = not (positive_independent and relabeling_rejected and imported_q_rejected)
    return {
        "positive_fragment_not_s_matrix_relabeling": positive_independent,
        "celestial_s_matrix_relabeling_rejected": relabeling_rejected,
        "precomputed_bms_charge_rejected": imported_q_rejected,
        "absorbed_by_celestial_s_matrix_relabeling": absorbed,
        "positive_Q_f": positive_q,
        "s_matrix_relabeling_control_Q_f": relabel_q,
        "precomputed_charge_control_Q_f": imported_q_report,
        "reason": (
            "The positive toy fragment computes Q_f from boundary sector data, while S-matrix relabeling "
            "and precomputed-charge controls fail the source-side test."
            if not absorbed
            else "The construction remains absorbed because the positive case cannot be separated from imported S-matrix or charge data."
        ),
    }


def ico_prime_report(q_report: dict[str, Any], absorber: dict[str, Any]) -> dict[str, Any]:
    target_import_avoided_conditionally = q_report["source_side_relative_to_celext"]
    insufficient_source_data_for_current_ti = not q_report[
        "source_side_relative_to_current_TI_primitives"
    ]
    bookkeeping_rejected_in_positive_fragment = not absorber[
        "absorbed_by_celestial_s_matrix_relabeling"
    ]
    return {
        "ICO_prime_tested": True,
        "target_import_avoided_conditionally": target_import_avoided_conditionally,
        "insufficient_source_data_unresolved_for_current_TI": (
            insufficient_source_data_for_current_ti
        ),
        "bookkeeping_rejected_in_positive_fragment": (
            bookkeeping_rejected_in_positive_fragment
        ),
        "verdict": (
            "conditional_celext_internal_boundary_charge_not_ti_derivation"
            if target_import_avoided_conditionally
            and bookkeeping_rejected_in_positive_fragment
            else "absorbed_or_insufficient_under_ico_prime"
        ),
        "reason": (
            "ICO' is avoided only relative to the explicitly added toy CelExt boundary category. "
            "Current Temporal Issuance primitives still do not derive the boundary current/action structure."
        ),
    }


def build_positive_entities() -> tuple[
    BoundaryObject,
    BoundaryObject,
    BoundaryObject,
    BoundaryInsertion,
    BoundaryInsertion,
]:
    b0 = boundary_object("B_q0", 0)
    b1 = boundary_object("B_q1", 1)
    b3 = boundary_object("B_q3", 3)
    e01 = BoundaryInsertion(
        morphism_id="I_soft_plus_1",
        source=b0,
        target=b1,
        soft_shift=1,
        operator_family="boundary_soft_insertion",
    )
    e13 = BoundaryInsertion(
        morphism_id="I_soft_plus_2",
        source=b1,
        target=b3,
        soft_shift=2,
        operator_family="boundary_soft_insertion",
    )
    return b0, b1, b3, e01, e13


def build_positive_fragment() -> dict[str, Any]:
    b0, b1, b3, e01, e13 = build_positive_entities()
    return {
        "objects": [object_report(obj) for obj in (b0, b1, b3)],
        "morphism": admissibility_report(e01),
        "composition": composition_report(e01, e13),
    }


def build_controls() -> dict[str, Any]:
    b0 = boundary_object("B_q0", 0)
    b1 = boundary_object("B_q1", 1)
    b2 = boundary_object("B_q2", 2)

    mismatched_target = BoundaryInsertion(
        morphism_id="bad_target_charge",
        source=b0,
        target=b2,
        soft_shift=1,
        operator_family="boundary_soft_insertion",
    )
    bulk_import = BoundaryInsertion(
        morphism_id="bulk_imported_boundary_insertion",
        source=b0,
        target=b1,
        soft_shift=1,
        operator_family="bulk_s_matrix_relabel",
        forbidden_refs=("bulk_s_matrix",),
    )
    broken_composition_second = BoundaryInsertion(
        morphism_id="bad_second_step",
        source=b1,
        target=b2,
        soft_shift=2,
        operator_family="boundary_soft_insertion",
    )

    good_first = BoundaryInsertion(
        morphism_id="good_first_step",
        source=b0,
        target=b1,
        soft_shift=1,
        operator_family="boundary_soft_insertion",
    )

    return {
        "target_charge_mismatch_rejected": not admissibility_report(
            mismatched_target
        )["admissible_boundary_morphism"],
        "bulk_import_rejected": not admissibility_report(
            bulk_import
        )["admissible_boundary_morphism"],
        "nonadditive_composition_rejected": not composition_report(
            good_first, broken_composition_second
        )["additive_composition"],
    }


def build_steps_4_6_fragment() -> dict[str, Any]:
    _, _, _, e01, e13 = build_positive_entities()
    composite = compose(e01, e13)
    action = SupertranslationAction(
        action_id="T_f",
        mode_label="supertranslation_f_l1m0",
        charge_offset=5,
        q_weight=7,
    )
    functoriality = supertranslation_functoriality_report(e01, e13, action)
    source_charge = soft_charge_functional_report(composite, action)
    absorber = absorber_report(composite, action)
    ico_prime = ico_prime_report(source_charge, absorber)
    return {
        "supertranslation_action": functoriality,
        "source_side_soft_charge": source_charge,
        "absorber": absorber,
        "ico_prime": ico_prime,
    }


def run_fixture() -> dict[str, Any]:
    positive = build_positive_fragment()
    controls = build_controls()
    steps_4_6 = build_steps_4_6_fragment()
    steps_1_3_complete = (
        all(obj["typed_boundary_object"] for obj in positive["objects"])
        and positive["morphism"]["admissible_boundary_morphism"]
        and positive["composition"]["additive_composition"]
        and all(controls.values())
    )
    steps_4_6_complete = (
        steps_4_6["supertranslation_action"]["BMS_functoriality"]
        and steps_4_6["source_side_soft_charge"]["source_side_Q_f"]
        and steps_4_6["ico_prime"]["ICO_prime_tested"]
        and not steps_4_6["absorber"]["absorbed_by_celestial_s_matrix_relabeling"]
    )

    return {
        "fixture": "celext_celestial_boundary_fixture_steps_1_6",
        "kind": "toy_category_fragment_not_physics_derivation",
        "contract_source": "explorations/E013-celestial-boundary-physics-bridge.md",
        "positive_fragment": positive,
        "steps_4_6_fragment": steps_4_6,
        "controls": controls,
        "summary": {
            "step_1_typed_boundary_object": all(
                obj["typed_boundary_object"] for obj in positive["objects"]
            ),
            "step_2_admissible_boundary_morphism": positive["morphism"][
                "admissible_boundary_morphism"
            ],
            "step_3_additive_composition": positive["composition"][
                "additive_composition"
            ],
            "steps_1_3_complete": steps_1_3_complete,
            "step_4_supertranslation_functoriality": steps_4_6[
                "supertranslation_action"
            ]["BMS_functoriality"],
            "step_5_source_side_Q_f_relative_to_CelExt": steps_4_6[
                "source_side_soft_charge"
            ]["source_side_relative_to_celext"],
            "step_5_source_side_Q_f_relative_to_current_TI": steps_4_6[
                "source_side_soft_charge"
            ]["source_side_relative_to_current_TI_primitives"],
            "step_6_s_matrix_relabeling_absorber_rejected": not steps_4_6[
                "absorber"
            ]["absorbed_by_celestial_s_matrix_relabeling"],
            "steps_4_6_complete": steps_4_6_complete,
            "steps_1_6_complete": steps_1_3_complete and steps_4_6_complete,
            "bulk_import_control_rejected": controls["bulk_import_rejected"],
            "BMS_functoriality_tested": True,
            "source_side_Q_f_tested": True,
            "ICO_prime_tested": steps_4_6["ico_prime"]["ICO_prime_tested"],
            "ICO_prime_verdict": steps_4_6["ico_prime"]["verdict"],
            "absorber_tested": True,
            "absorber_status": (
                "positive_toy_fragment_not_s_matrix_relabeling__current_TI_still_not_derivation"
                if not steps_4_6["absorber"][
                    "absorbed_by_celestial_s_matrix_relabeling"
                ]
                else "absorbed_by_celestial_s_matrix_relabeling"
            ),
            "physics_derived_from_TI": False,
            "claim_status_change": "none",
            "verdict": (
                "celext_steps_1_6_pass_as_conditional_internal_boundary_fixture"
                if steps_1_3_complete and steps_4_6_complete
                else "celext_steps_1_6_incomplete"
            ),
            "next_required": (
                "cech_h3_functor_obl_001_negative_half or D-fork pressure; "
                "do not treat CelExt as TI-derived physics"
            ),
        },
    }


def main() -> None:
    result = run_fixture()
    out = (
        Path(__file__).resolve().parents[1]
        / "tests"
        / "artifacts"
        / "celext_celestial_boundary_result.json"
    )
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True))
    print(json.dumps(result["summary"], indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
