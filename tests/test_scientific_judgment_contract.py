from __future__ import annotations

import json
import unittest
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
EVALS = REPO / "evals" / "scientific_judgment.json"


class ScientificJudgmentEvalTests(unittest.TestCase):
    def test_forward_eval_set_is_well_formed_and_covers_boundaries(self) -> None:
        payload = json.loads(EVALS.read_text(encoding="utf-8"))
        self.assertEqual(payload["schema_version"], 1)
        cases = payload["cases"]
        self.assertGreaterEqual(len(cases), 8)

        ids = [case["id"] for case in cases]
        self.assertEqual(len(ids), len(set(ids)))
        for case in cases:
            self.assertTrue(case["prompt"].strip())
            self.assertTrue(case["expected_decision"].strip())
            self.assertTrue(case["failure_mode"].strip())
            self.assertGreaterEqual(len(case["tags"]), 1)

        tags = {tag for case in cases for tag in case["tags"]}
        self.assertTrue({
            "provenance-routing",
            "threshold-authority",
            "missing-native-tool",
            "mixed-table",
            "visual-semantics",
            "image-only",
            "multi-target",
        }.issubset(tags))


if __name__ == "__main__":
    unittest.main()
