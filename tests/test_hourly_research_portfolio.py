from __future__ import annotations

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PORTFOLIO = ROOT / "steward" / "research-portfolio.json"


class HourlyResearchPortfolioTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.data = json.loads(PORTFOLIO.read_text(encoding="utf-8"))

    def test_active_lane_and_ready_work_exist(self) -> None:
        active = [
            group
            for group in self.data["work_groups"]
            if group["state"] == "ACTIVE" and group["hourly_eligible"]
        ]
        self.assertEqual([group["id"] for group in active], [self.data["lane_1_work_group"]])
        ready = [
            item
            for item in active[0]["internal_work_items"]
            if item["state"] == "READY" and item["hourly_eligible"]
        ]
        self.assertGreaterEqual(len(ready), 2)
        selected = max(ready, key=lambda item: item["priority_score"])
        self.assertEqual(selected["id"], "TI-PHYSICAL-WITNESS-GENERATION")

    def test_no_wait_only_state_and_gated_activation(self) -> None:
        contract = self.data["selection_contract"]
        self.assertIn("actively generate or kill", contract["no_wait_only_state"])
        self.assertTrue(contract["select_highest_ranked_unblocked_item"])
        self.assertTrue(contract["rerank_after_every_material_run"])
        for group in self.data["work_groups"]:
            for item in group.get("internal_work_items", []):
                if not item["hourly_eligible"]:
                    self.assertTrue(item.get("activation"))

    def test_trigger_plan_activates_physical_campaign(self) -> None:
        trigger = (ROOT / "agent-governance" / "NEXT-TRIGGER-PLAN.md").read_text(
            encoding="utf-8"
        )
        context = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
        self.assertIn("TI-PHYSICAL-WITNESS-GENERATION", trigger)
        self.assertIn(self.data["lane_1_work_group"], trigger)
        self.assertIn("actively generate or kill", trigger)
        self.assertIn("LANES.yaml", context)


if __name__ == "__main__":
    unittest.main()
