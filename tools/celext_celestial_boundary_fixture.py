"""CelExt celestial-boundary fixture, steps 1-3 (RUN-0126).

Toy category fragment only. This does not derive BMS physics, define Q_f, or
prove that Temporal Issuance supplies a completed celestial boundary theory.

It executes the first three obligations from E013:

1. typed boundary source object on S^2,
2. admissible boundary insertion changing a soft-charge sector,
3. additive composition of admissible insertions.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any


FORBIDDEN_INPUTS = {
    "bulk_hamiltonian",
    "bulk_s_matrix",
    "radiative_phase_space",
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
    forbidden_refs: tuple[str, ...] = ()


def forbidden_refs_used(*items: BoundaryObject | BoundaryInsertion) -> list[str]:
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


def build_positive_fragment() -> dict[str, Any]:
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


def run_fixture() -> dict[str, Any]:
    positive = build_positive_fragment()
    controls = build_controls()
    steps_1_3_complete = (
        all(obj["typed_boundary_object"] for obj in positive["objects"])
        and positive["morphism"]["admissible_boundary_morphism"]
        and positive["composition"]["additive_composition"]
        and all(controls.values())
    )

    return {
        "fixture": "celext_celestial_boundary_fixture_steps_1_3",
        "kind": "toy_category_fragment_not_physics_derivation",
        "contract_source": "explorations/E013-celestial-boundary-physics-bridge.md",
        "positive_fragment": positive,
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
            "bulk_import_control_rejected": controls["bulk_import_rejected"],
            "BMS_functoriality_tested": False,
            "source_side_Q_f_tested": False,
            "ICO_prime_tested": False,
            "absorber_tested": False,
            "physics_derived_from_TI": False,
            "claim_status_change": "none",
            "verdict": "celext_steps_1_3_pass_as_internal_toy_category_fragment"
            if steps_1_3_complete
            else "celext_steps_1_3_incomplete",
            "next_required": (
                "steps_4_6: BMS functoriality, source-side Q_f / ICO prime, "
                "and absorber check against celestial S-matrix relabeling"
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
