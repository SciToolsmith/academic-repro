from __future__ import annotations

import unittest
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
SKILL = REPO / "academic-repro"


class BehaviorContractTests(unittest.TestCase):
    def read(self, relative: str) -> str:
        return (SKILL / relative).read_text(encoding="utf-8")

    def test_author_workflow_prefers_usable_native_source_without_overclaiming_input(self) -> None:
        entrypoint = self.read("SKILL.md")
        source_audit = self.read("references/source-environment-audit.md")

        self.assertIn("preserve usable target-relevant author source and runtime by default", entrypoint)
        self.assertIn("Use a cross-language primary route only", entrypoint)
        self.assertIn("Track method provenance and input identity independently", source_audit)
        self.assertIn("not exact regeneration of the published target", source_audit)

    def test_visual_inference_is_tiered_and_calibration_cannot_validate_itself(self) -> None:
        validation = self.read("references/execution-validation.md")

        for category in ("Presentation-only", "Encoding", "Claim-defining scientific"):
            self.assertIn(f"**{category}:**", validation)
        self.assertIn("A feature used to calibrate", validation)
        self.assertIn("cannot also validate it", validation)

    def test_reported_value_is_not_a_tuning_objective_and_mismatch_is_bounded(self) -> None:
        validation = self.read("references/execution-validation.md")

        self.assertIn("reported number is a validation reference, never an optimization objective", validation)
        for component in ("absolute level", "relative improvement or ordering", "qualitative trend", "proposed mechanism"):
            self.assertIn(component, validation)
        self.assertIn("A mismatch alone cannot establish fabrication", validation)
        self.assertIn("Continue only when the next check can distinguish a cause", validation)

    def test_default_delivery_is_result_first_and_route_consistent(self) -> None:
        delivery = self.read("references/delivery-contract.md")

        self.assertIn("in the language and runtime used", delivery)
        self.assertIn("compact reproduction statement", delivery)
        self.assertIn("paper target or reported value", delivery)
        self.assertIn("regenerable intermediate CSV/JSON outputs", delivery)
        self.assertIn("Do not replace the executed native source with an unrelated port", delivery)
        self.assertIn("evidence records and clean-rerun receipts internal", delivery)

    def test_existing_activated_proprietary_runtime_does_not_trigger_an_automatic_pause(self) -> None:
        permissions = self.read("references/permission-gates.md")

        self.assertIn("already-installed and activated proprietary software", permissions)
        self.assertIn("needs no new agreement, login, payment, activation, shared license", permissions)


if __name__ == "__main__":
    unittest.main()
