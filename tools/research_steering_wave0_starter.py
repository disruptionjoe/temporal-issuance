"""Deterministic starter plan for Temporal Issuance research-steering Wave 0.

The script validates that the starter wave respects the attention card:
H1 is the blocking lane, H2 is started only as a dependent construction brief,
and H3/H4/H5/H7 can be prepared as disjoint sidecar lanes.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


LANES: dict[str, dict[str, Any]] = {
    "H1": {
        "title": "Whole-family completion barrier theorem",
        "wave_role": "blocking_lane",
        "mode": "solo_theorem_or_classifier_target",
        "depends_on": [],
        "starter_output": "bounded Adapter_P trace class plus completion-barrier proof target",
        "write_scope": ["explorations/E164", "tools/research_steering_wave0_starter.py"],
    },
    "H2": {
        "title": "Operative source-action generator",
        "wave_role": "dependent_starter",
        "mode": "brief_only_until_H1_names_target_class",
        "depends_on": ["H1"],
        "starter_output": "candidate internal anti-after-naming principles and H1 dependencies",
        "write_scope": ["explorations/E164"],
    },
    "H3_H4": {
        "title": "Physical near-miss calibration pair",
        "wave_role": "sidecar_starter",
        "mode": "parallel_fixture_contract_prep",
        "depends_on": [],
        "starter_output": "CRISPR and dynamic/Floquet minimal fixture contracts",
        "write_scope": ["explorations/E164"],
    },
    "H5": {
        "title": "Multi-holder reversal-cost source/readout separator",
        "wave_role": "sidecar_starter",
        "mode": "finite_fixture_contract_prep",
        "depends_on": [],
        "starter_output": "finite distinct-holder fixture with TaF and thermodynamic controls",
        "write_scope": ["explorations/E164"],
    },
    "H7": {
        "title": "Adapter_P preservation-map contract",
        "wave_role": "sidecar_starter",
        "mode": "checker_schema_prep",
        "depends_on": [],
        "starter_output": "minimal preservation-map checker schema",
        "write_scope": ["explorations/E164"],
    },
}


def validate_lanes() -> dict[str, Any]:
    lane_ids = set(LANES)
    errors: list[str] = []

    if LANES["H1"]["wave_role"] != "blocking_lane":
        errors.append("H1 must remain the blocking lane for Wave 0.")

    for lane_id, lane in LANES.items():
        for dep in lane["depends_on"]:
            if dep not in lane_ids:
                errors.append(f"{lane_id} depends on unknown lane {dep}.")

    full_execution_lanes = [
        lane_id
        for lane_id, lane in LANES.items()
        if lane["wave_role"] != "dependent_starter" and "prep" not in lane["mode"] and lane_id != "H1"
    ]
    if full_execution_lanes:
        errors.append(f"Only H1 may be framed as a full Wave 0 lane; got {full_execution_lanes}.")

    shared_writers = {
        lane_id: lane["write_scope"]
        for lane_id, lane in LANES.items()
        if lane_id != "H1" and lane["write_scope"] != ["explorations/E164"]
    }
    if shared_writers:
        errors.append(f"Sidecar lanes must merge only through E164 in Wave 0; got {shared_writers}.")

    result = {
        "wave_id": "research_steering_wave0_starter",
        "valid": not errors,
        "errors": errors,
        "blocking_lane": "H1",
        "sidecar_lanes": ["H3_H4", "H5", "H7"],
        "dependent_starter_lanes": ["H2"],
        "lanes": LANES,
        "next_dependency_boundary": "H2 construction and H3/H4 execution wait for H1 target-class result.",
    }
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    result = validate_lanes()
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["valid"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
