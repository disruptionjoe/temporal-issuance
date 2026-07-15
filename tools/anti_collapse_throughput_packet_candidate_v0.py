#!/usr/bin/env python3
"""Fail-closed packet evaluator for the anti-collapse throughput candidate.

The candidate is worth preserving because it points directly at source-side
openness, but this executable has no path that admits it without a native
source law, Adapter_P fields, W1/W4/W5, and verified CompletionClass v1
nonfactorization.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

import completion_class_v1 as cc


PACKET_STATUS = "PACKETIZED_FAIL_CLOSED_NOT_ADMITTED"
COMPLETION_STATUS = "unresolved_no_verified_nonfactorization"


@dataclass(frozen=True)
class RequiredField:
    field_id: str
    supplied: bool
    finding: str
    blocks_admission: bool = True


REQUIRED_SOURCE_FIELDS = (
    RequiredField(
        "typed_source_state",
        False,
        "No typed source state is supplied beyond the open-system metaphor.",
    ),
    RequiredField(
        "typed_transition_object",
        False,
        "No Action-2 transition object is supplied.",
    ),
    RequiredField(
        "native_source_law",
        False,
        "No native source law distinguishes issuance from dissipative or access dynamics.",
    ),
    RequiredField(
        "adapter_p",
        False,
        "No Adapter_P fields state what crosses the interface.",
    ),
    RequiredField(
        "provenance",
        False,
        "No machine-verifiable candidate provenance or preservation trace is supplied.",
    ),
    RequiredField(
        "w1_w4_w5",
        False,
        "W1, W4, and W5 witness fields remain absent.",
    ),
    RequiredField(
        "whole_family_noncompletion_certificates",
        False,
        "No whole-family noncompletion certificates are verified.",
    ),
    RequiredField(
        "verifier_backed_nonfactorization",
        False,
        "CompletionClass v1 nonfactorization is asserted by none of the eleven families.",
    ),
    RequiredField(
        "composition_closure",
        False,
        "Declared product and sequential composition closure is missing.",
    ),
)


FAMILY_NOTES = {
    "hidden_state": "A latent fixed state could still determine the throughput trace.",
    "initial_condition": "Admitted initial data could still determine the candidate.",
    "boundary_condition": "Boundary data could still explain anti-collapse maintenance.",
    "fixed_source": "A fixed law, algebra, source family, or instrument family remains open.",
    "stochastic_seed": "A fixed stochastic law plus seed remains open.",
    "name_provenance": "The throughput label may still be representational packaging.",
    "resource_capability": "Maintenance throughput may be ordinary resource or capability activation.",
    "whole_family": "A closed family could still contain the joint signature.",
    "completed_history": "A completed-history description could still extensionally contain it.",
    "observer_information_access": "The residual can be observer-counting or aperture disclosure.",
    "relabel_gauge": "The sign and residual may vanish under the declared quotient.",
}


def completion_case() -> cc.CompletionCase:
    return cc.CompletionCase(
        case_id="anti_collapse_throughput_packet_candidate_v0",
        represented_family_ids=cc.PRIMITIVE_FAMILY_IDS,
        verified_nonfactorization_family_ids=(),
        witnesses=(),
        composition_closure_declared=False,
    )


def required_field_summary() -> list[dict[str, Any]]:
    return [asdict(field) for field in REQUIRED_SOURCE_FIELDS]


def completion_family_assessments() -> list[dict[str, Any]]:
    return [
        {
            "family_id": family_id,
            "represented": True,
            "status": COMPLETION_STATUS,
            "finding": FAMILY_NOTES[family_id],
        }
        for family_id in cc.PRIMITIVE_FAMILY_IDS
    ]


def residual_assessment() -> dict[str, Any]:
    return {
        "candidate_shape": "1/sqrt(N)",
        "residual_location": "observer_counting_artifact",
        "source_residual_established": False,
        "projection_residual_established": False,
        "observer_counting_artifact_established": True,
        "reason": (
            "N is introduced only as a counting or aggregation index. Without "
            "a native source law and Adapter_P trace, the residual is not a "
            "source-side nonfactorization result."
        ),
    }


def sign_correction() -> dict[str, Any]:
    return {
        "gu_krein_sign_reading": "forced_internal",
        "out_of_band_sign_reading_allowed": False,
        "used_as_undecidability_evidence": False,
        "used_as_external_observer_evidence": False,
        "finding": (
            "The killed out-of-band sign reading is preserved as unavailable; "
            "the sign clause supplies no packet admission evidence."
        ),
    }


def run_packet() -> dict[str, Any]:
    case = completion_case()
    completion_decision = cc.classify_case(case)
    missing_fields = [
        field.field_id for field in REQUIRED_SOURCE_FIELDS if not field.supplied
    ]

    return {
        "fixture_id": "anti_collapse_throughput_packet_candidate_v0",
        "source_artifact": (
            "explorations/E179-anti-collapse-throughput-packet-preflight-2026-07-15.md"
        ),
        "packet_status": PACKET_STATUS,
        "packet_admitted": False,
        "typed_action_2_packet": False,
        "native_source_law_supplied": False,
        "required_source_fields": required_field_summary(),
        "blocking_missing_fields": missing_fields,
        "completion_class_version": "completion_class_v1",
        "completion_family_count": len(cc.PRIMITIVE_FAMILY_IDS),
        "all_completion_families_represented": True,
        "completion_family_assessments": completion_family_assessments(),
        "completion_class_verdict": completion_decision["verdict"],
        "unresolved_family_ids": completion_decision["unresolved_family_ids"],
        "missing_family_ids": completion_decision["missing_family_ids"],
        "composition_closure_declared": completion_decision[
            "composition_closure_declared"
        ],
        "residual_assessment": residual_assessment(),
        "sign_correction": sign_correction(),
        "physical_source_issuance_established": False,
        "claim_status_change": "none",
        "TI_C020_reopened": False,
        "E177_modified": False,
        "cross_repo_implication": False,
        "next_required_test": (
            "typed_action_2_packet_or_native_source_law_with_verifier_backed_nonfactorization"
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
        default=Path(
            "tests/artifacts/anti_collapse_throughput_packet_candidate_v0_result.json"
        ),
    )
    args = parser.parse_args()
    result = run_packet()
    write_json(result, args.output)
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
