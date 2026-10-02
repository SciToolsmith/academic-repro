from __future__ import annotations

import copy
import hashlib
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
SCRIPTS = REPO / "paper-reproduce" / "scripts"
VALIDATOR = SCRIPTS / "evidence_record.py"
sys.path.insert(0, str(SCRIPTS))

from evidence_record import EvidenceError, artifact_set_digest, validate_record  # noqa: E402


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def artifact_entries() -> list[dict]:
    return [
        {"role": "source", "path": "reproduce.py", "sha256": digest(b"source")},
        {"role": "configuration", "path": "parameters.json", "sha256": digest(b"config")},
        {"role": "environment", "path": "requirements.txt", "sha256": digest(b"environment")},
        {"role": "output", "path": "result.png", "sha256": digest(b"output")},
    ]


def valid_record(entries: list[dict] | None = None) -> dict:
    entries = entries or artifact_entries()
    output_digest = next(item["sha256"] for item in entries if item["role"] == "output")
    environment_digest = digest(b"python-test-environment")
    return {
        "schemaVersion": "academic-repro.evidence/v1",
        "targetId": "fig-01",
        "evidenceBasis": "same-input-independent",
        "claim": "The reproduced response preserves the declared ordering.",
        "sourceIdentity": {
            "role": "paper",
            "locator": "Figure 1 and its caption",
            "sha256": digest(b"paper"),
        },
        "artifactSetDigest": artifact_set_digest(entries),
        "criteria": [{
            "id": "ordering-pass",
            "statement": "Method A remains below method B over the declared interval.",
            "authority": "paper",
            "purpose": "scientific-validity",
            "frozenBeforeRun": True,
            "evidenceRole": "acceptance",
            "status": "passed",
            "expected": "A is below B over the interval.",
            "observed": "A is below B at every evaluated point.",
            "evidenceOutputs": ["result.png"],
            "independentFromCalibration": True,
        }],
        "status": {
            "operational": "complete",
            "validation": "passed",
            "claim": "supported",
        },
        "cleanRerun": {
            "status": "passed",
            "argv": ["python3", "reproduce.py", "--config", "parameters.json"],
            "environmentDigest": environment_digest,
            "freshWorkspace": True,
            "outputsRemovedBeforeRun": True,
            "outputs": [{"path": "result.png", "sha256": output_digest}],
            "matchPolicy": "exact-sha256",
            "validatedCriteria": [],
        },
    }


class EvidenceRecordTests(unittest.TestCase):
    def test_valid_record_and_cli_verify_compact_artifact_set(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            entries = artifact_entries()
            record_path = root / "evidence.json"
            record_path.write_text(json.dumps(valid_record(entries)), encoding="utf-8")
            artifact_set_path = root / "artifact-set.json"
            artifact_set_path.write_text(json.dumps(entries), encoding="utf-8")
            expected = digest(record_path.read_bytes())

            completed = subprocess.run(
                [
                    sys.executable,
                    str(VALIDATOR),
                    "--record",
                    str(record_path),
                    "--expect-sha256",
                    expected,
                    "--artifact-set",
                    str(artifact_set_path),
                    "--json",
                ],
                cwd=REPO,
                text=True,
                capture_output=True,
            )
            self.assertEqual(completed.returncode, 0, completed.stderr)
            summary = json.loads(completed.stdout)
            self.assertEqual(summary["targetId"], "fig-01")
            self.assertEqual(summary["cleanRerunStatus"], "passed")
            self.assertEqual(summary["sha256"], expected)

            entries[0]["sha256"] = digest(b"changed")
            artifact_set_path.write_text(json.dumps(entries), encoding="utf-8")
            rejected = subprocess.run(
                [
                    sys.executable,
                    str(VALIDATOR),
                    "--record",
                    str(record_path),
                    "--artifact-set",
                    str(artifact_set_path),
                ],
                cwd=REPO,
                text=True,
                capture_output=True,
            )
            self.assertEqual(rejected.returncode, 2)
            self.assertIn("artifact set digest does not match", rejected.stderr)

    def test_positive_claim_requires_frozen_non_user_scientific_evidence(self) -> None:
        record = valid_record()
        user_only = copy.deepcopy(record)
        criterion = user_only["criteria"][0]
        criterion["authority"] = "user"
        criterion["purpose"] = "project-acceptance"
        with self.assertRaisesRegex(EvidenceError, "non-user scientific-validity evidence"):
            validate_record(user_only)

        unfrozen = copy.deepcopy(record)
        unfrozen["criteria"][0]["frozenBeforeRun"] = False
        with self.assertRaisesRegex(EvidenceError, "frozen before the final run"):
            validate_record(unfrozen)

    def test_mechanism_support_requires_independent_discriminating_evidence(self) -> None:
        record = valid_record()
        record["evidenceBasis"] = "mechanism-consistency"
        with self.assertRaisesRegex(EvidenceError, "independent discriminating evidence"):
            validate_record(record)

        consistent = copy.deepcopy(record)
        consistent["status"]["claim"] = "mechanism-consistent"
        validate_record(consistent)

        discriminating = copy.deepcopy(record)
        discriminating["criteria"][0]["evidenceRole"] = "held-out"
        discriminating["criteria"][0]["independentFromCalibration"] = True
        validate_record(discriminating)

    def test_clean_rerun_and_study_profile_scale_with_risk(self) -> None:
        record = valid_record()
        inconsistent = copy.deepcopy(record)
        inconsistent["status"]["operational"] = "partial"
        with self.assertRaisesRegex(EvidenceError, "requires complete execution"):
            validate_record(inconsistent)

        equivalent = copy.deepcopy(record)
        equivalent["cleanRerun"]["matchPolicy"] = "criteria-equivalent"
        with self.assertRaisesRegex(EvidenceError, "re-evaluate every criterion"):
            validate_record(equivalent)
        equivalent["cleanRerun"]["validatedCriteria"] = ["ordering-pass"]
        validate_record(equivalent)

        profiled = copy.deepcopy(record)
        profiled["studyProfile"] = {
            "kind": "stochastic",
            "checks": [{
                "name": "seed-stability",
                "status": "passed",
                "detail": "The conclusion held across the declared seed set.",
            }],
        }
        self.assertEqual(validate_record(profiled)["studyProfile"]["kind"], "stochastic")

    def test_record_rejects_mismatched_digest_without_traceback(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            record_path = root / "evidence.json"
            record_path.write_text(json.dumps(valid_record()), encoding="utf-8")
            completed = subprocess.run(
                [sys.executable, str(VALIDATOR), "--record", str(record_path), "--expect-sha256", "0" * 64],
                cwd=REPO,
                text=True,
                capture_output=True,
            )
            self.assertEqual(completed.returncode, 2)
            self.assertIn("evidence record SHA-256 mismatch", completed.stderr)
            self.assertNotIn("Traceback", completed.stderr)


if __name__ == "__main__":
    unittest.main()
