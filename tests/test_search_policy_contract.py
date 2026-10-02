from __future__ import annotations

import unittest
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
REFERENCES = REPO / "paper-reproduce" / "references"


class ConditionalPolicySurfaceTests(unittest.TestCase):
    def test_source_audit_is_a_conditional_reference_not_a_second_workflow(self) -> None:
        text = (REFERENCES / "source-environment-audit.md").read_text(encoding="utf-8")
        self.assertLessEqual(len(text.split()), 1100)
        self.assertNotIn("--matlab-live-probe", text)
        self.assertNotIn("--author-native-runtime", text)
        self.assertNotIn("decision queue", text.casefold())

    def test_permission_reference_avoids_universal_resource_budgets(self) -> None:
        text = (REFERENCES / "permission-gates.md").read_text(encoding="utf-8")
        self.assertLessEqual(len(text.split()), 650)
        for fixed_budget in ("250 MiB", "2 GiB", "20 minutes"):
            self.assertNotIn(fixed_budget, text)


if __name__ == "__main__":
    unittest.main()
