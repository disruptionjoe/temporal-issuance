#!/usr/bin/env python3
"""H7 completion-aware Adapter_P admission contract.

This Wave 3 artifact consumes H1 and H2 as preservation requirements. It
classifies boundary, neighbor, or cross-repo candidate packets without importing
hidden completion or readout language. It is formal/local only and does not move
claim status.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ADMITTED_FORMAL_LOCAL_OSAG_SUPPORT = "ADMITTED_FORMAL_LOCAL_OSAG_SUPPORT"
IMPORTED_COMPLETION_REJECTION = "IMPORTED_COMPLETION_REJECTION"
READOUT_ONLY_REJECTION = "READOUT_ONLY_REJECTION"
MISSING_PRESERVATION_REJECTION = "MISSING_PRESERVATION_REJECTION"
UNSUPPORTED_PROVENANCE_REJECTION = "UNSUPPORTED_PROVENANCE_REJECTION"

REQUIRED_H1_FLAGS = (
    "all_completion_channels_exercised",
    "preaction_family_noncompletion_required_for_escape",
)

REQUIRED_H2_FLAGS = (
    "bounded_osag_constructed",
    "preaction_family_noncompletion_rule_generated_internal",
    "fixed_completion_absorbed",
    "after_fact_singleton_rejected",
    "imported_oracle_rejected",
)


@dataclass(frozen=True)
class AdmissionPacket:
    packet_id: str
    source_kind: str
    preserves_tau_n: bool
    preserves_preserve_n: bool
    preserves_represented_family_index: bool
    preserves_candidate_provenance: bool
    maps_adapter_fields: bool
    uses_h1_completion_channels: bool
    uses_h2_family_checks: bool
    hidden_completion_oracle: bool
    imported_law_or_schema: bool
    readout_only_language: bool
    declares_formal_local_only: bool
    claims_physical_source: bool
    moves_claim_status: bool


@dataclass(frozen=True)
class AdmissionDecision:
    packet_id: str
    source_kind: str
    verdict: str
    admitted: bool
    terminal: bool
    missing_requirements: tuple[str, ...]
    reason: str


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def h1_h2_floor(
    *,
    h1_path: Path = Path("tests/artifacts/whole_family_completion_barrier_classifier_result.json"),
    h2_path: Path = Path("tests/artifacts/osag_preaction_family_noncompletion_result.json"),
) -> dict[str, Any]:
    h1 = load_json(h1_path)
    h2 = load_json(h2_path)
    return {
        "h1_result": h1["h1_result"],
        "h2_result": h2["h2_result"],
        "h1_required_flags": {flag: bool(h1[flag]) for flag in REQUIRED_H1_FLAGS},
        "h2_required_flags": {flag: bool(h2[flag]) for flag in REQUIRED_H2_FLAGS},
        "h1_completion_absorption_classes_seen": h1[
            "completion_absorption_classes_seen"
        ],
        "h2_osag_tuple": h2["osag_tuple"],
        "h1_physical_source_issuance_established": h1[
            "physical_source_issuance_established"
        ],
        "h2_physical_source_issuance_established": h2[
            "physical_source_issuance_established"
        ],
        "h1_claim_status_change": h1["claim_status_change"],
        "h2_claim_status_change": h2["claim_status_change"],
    }


def h1_h2_floor_satisfied(floor: dict[str, Any]) -> bool:
    return (
        all(floor["h1_required_flags"].values())
        and all(floor["h2_required_flags"].values())
        and not floor["h1_physical_source_issuance_established"]
        and not floor["h2_physical_source_issuance_established"]
        and floor["h1_claim_status_change"] == "none"
        and floor["h2_claim_status_change"] == "none"
    )


def admission_packets() -> tuple[AdmissionPacket, ...]:
    return (
        AdmissionPacket(
            packet_id="boundary_osag_support",
            source_kind="boundary",
            preserves_tau_n=True,
            preserves_preserve_n=True,
            preserves_represented_family_index=True,
            preserves_candidate_provenance=True,
            maps_adapter_fields=True,
            uses_h1_completion_channels=True,
            uses_h2_family_checks=True,
            hidden_completion_oracle=False,
            imported_law_or_schema=False,
            readout_only_language=False,
            declares_formal_local_only=True,
            claims_physical_source=False,
            moves_claim_status=False,
        ),
        AdmissionPacket(
            packet_id="neighbor_completion_table",
            source_kind="neighbor",
            preserves_tau_n=True,
            preserves_preserve_n=True,
            preserves_represented_family_index=False,
            preserves_candidate_provenance=True,
            maps_adapter_fields=True,
            uses_h1_completion_channels=True,
            uses_h2_family_checks=False,
            hidden_completion_oracle=True,
            imported_law_or_schema=False,
            readout_only_language=False,
            declares_formal_local_only=True,
            claims_physical_source=False,
            moves_claim_status=False,
        ),
        AdmissionPacket(
            packet_id="cross_repo_readout_language",
            source_kind="cross_repo",
            preserves_tau_n=True,
            preserves_preserve_n=True,
            preserves_represented_family_index=True,
            preserves_candidate_provenance=True,
            maps_adapter_fields=True,
            uses_h1_completion_channels=True,
            uses_h2_family_checks=True,
            hidden_completion_oracle=False,
            imported_law_or_schema=False,
            readout_only_language=True,
            declares_formal_local_only=True,
            claims_physical_source=False,
            moves_claim_status=False,
        ),
        AdmissionPacket(
            packet_id="boundary_missing_preserve_n",
            source_kind="boundary",
            preserves_tau_n=True,
            preserves_preserve_n=False,
            preserves_represented_family_index=True,
            preserves_candidate_provenance=True,
            maps_adapter_fields=True,
            uses_h1_completion_channels=True,
            uses_h2_family_checks=True,
            hidden_completion_oracle=False,
            imported_law_or_schema=False,
            readout_only_language=False,
            declares_formal_local_only=True,
            claims_physical_source=False,
            moves_claim_status=False,
        ),
        AdmissionPacket(
            packet_id="physical_source_claim_shortcut",
            source_kind="cross_repo",
            preserves_tau_n=True,
            preserves_preserve_n=True,
            preserves_represented_family_index=True,
            preserves_candidate_provenance=False,
            maps_adapter_fields=True,
            uses_h1_completion_channels=True,
            uses_h2_family_checks=True,
            hidden_completion_oracle=False,
            imported_law_or_schema=True,
            readout_only_language=False,
            declares_formal_local_only=False,
            claims_physical_source=True,
            moves_claim_status=True,
        ),
    )


def missing_requirements(packet: AdmissionPacket) -> tuple[str, ...]:
    missing: list[str] = []
    if not packet.preserves_tau_n:
        missing.append("tau_n")
    if not packet.preserves_preserve_n:
        missing.append("Preserve_n")
    if not packet.preserves_represented_family_index:
        missing.append("represented_family_index")
    if not packet.preserves_candidate_provenance:
        missing.append("candidate_provenance")
    if not packet.maps_adapter_fields:
        missing.append("adapter_fields")
    if not packet.uses_h1_completion_channels:
        missing.append("h1_completion_channels")
    if not packet.uses_h2_family_checks:
        missing.append("h2_family_checks")
    if packet.hidden_completion_oracle:
        missing.append("no_hidden_completion_oracle")
    if packet.imported_law_or_schema:
        missing.append("no_imported_law_or_schema")
    if packet.readout_only_language:
        missing.append("no_readout_only_language")
    if not packet.declares_formal_local_only:
        missing.append("formal_local_only")
    if packet.claims_physical_source:
        missing.append("no_physical_source_claim")
    if packet.moves_claim_status:
        missing.append("no_claim_status_movement")
    return tuple(missing)


def classify_packet(packet: AdmissionPacket) -> AdmissionDecision:
    missing = missing_requirements(packet)
    if packet.hidden_completion_oracle or packet.imported_law_or_schema:
        verdict = IMPORTED_COMPLETION_REJECTION
        admitted = False
        terminal = True
        reason = "The packet imports a completion table, law, schema, or physical-source shortcut."
    elif packet.readout_only_language:
        verdict = READOUT_ONLY_REJECTION
        admitted = False
        terminal = True
        reason = "The packet is finality/readout language rather than OSAG support."
    elif any(item in missing for item in ("tau_n", "Preserve_n", "represented_family_index", "adapter_fields")):
        verdict = MISSING_PRESERVATION_REJECTION
        admitted = False
        terminal = False
        reason = "The packet does not preserve the required H1/H2 Adapter_P fields."
    elif any(item in missing for item in ("candidate_provenance", "h1_completion_channels", "h2_family_checks")):
        verdict = UNSUPPORTED_PROVENANCE_REJECTION
        admitted = False
        terminal = False
        reason = "The packet lacks provenance or does not explicitly carry H1/H2 checks."
    elif packet.claims_physical_source or packet.moves_claim_status:
        verdict = IMPORTED_COMPLETION_REJECTION
        admitted = False
        terminal = True
        reason = "Admission cannot move claims or assert physical source issuance."
    else:
        verdict = ADMITTED_FORMAL_LOCAL_OSAG_SUPPORT
        admitted = True
        terminal = False
        reason = "The packet admits only formal/local OSAG support while preserving H1/H2 fields."
    return AdmissionDecision(
        packet_id=packet.packet_id,
        source_kind=packet.source_kind,
        verdict=verdict,
        admitted=admitted,
        terminal=terminal,
        missing_requirements=missing,
        reason=reason,
    )


def run_admission_contract() -> dict[str, Any]:
    floor = h1_h2_floor()
    decisions = [classify_packet(packet) for packet in admission_packets()]
    admitted = [decision.packet_id for decision in decisions if decision.admitted]
    return {
        "fixture_id": "completion_aware_adapter_p_admission_contract",
        "kind": "h7_completion_aware_adapter_p_admission_contract",
        "h1_h2_floor": floor,
        "h1_h2_floor_satisfied": h1_h2_floor_satisfied(floor),
        "decisions": [
            {
                "packet_id": decision.packet_id,
                "source_kind": decision.source_kind,
                "verdict": decision.verdict,
                "admitted": decision.admitted,
                "terminal": decision.terminal,
                "missing_requirements": list(decision.missing_requirements),
                "reason": decision.reason,
            }
            for decision in decisions
        ],
        "admitted_packet_ids": admitted,
        "h7_result": "completion_aware_formal_local_admission_contract_built",
        "next_track_1_recommendation": (
            "H9 physical calibration batch or H5/H6 separator only after a concrete "
            "candidate packet satisfies this H7 admission contract."
        ),
        "claim_status_change": "none",
        "physical_source_issuance_established": False,
        "TI_C020_reopened": False,
        "honest_current_result": (
            "H7 admits only formal/local OSAG support that preserves tau_n, Preserve_n, "
            "the represented family index, candidate provenance, H1 completion channels, "
            "and H2 family checks. Imported completion, readout-only, and posture-moving "
            "packets are rejected."
        ),
    }


def write_json(result: dict[str, Any], output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    write_json(run_admission_contract(), args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
