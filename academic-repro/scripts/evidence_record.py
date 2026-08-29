#!/usr/bin/env python3
"""Validate a compact Academic Repro evidence record.

The record stores only judgment that cannot be derived from the delivery plan.
Artifact paths and hashes are collapsed into one canonical set digest so the
assembler can bind files automatically without duplicating a large manifest.
Optional study-profile checks are used only when the research design needs them.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import stat
import sys
from pathlib import Path
from typing import List, Optional, Sequence, Tuple


SCHEMA_VERSION = "academic-repro.evidence/v1"
MAX_RECORD_BYTES = 512 * 1024
MAX_ITEMS = 32

EVIDENCE_BASES = {
    "author-native-recompute",
    "same-input-independent",
    "mechanism-consistency",
    "new-data-replication",
    "alternative-method-robustness",
    "mathematical-cross-check",
}
SOURCE_ROLES = {"paper", "target-manifest", "supplied-artifact", "data", "code", "other"}
AUTHORITIES = {"paper", "method", "domain", "user"}
CRITERION_PURPOSES = {"scientific-validity", "project-acceptance"}
EVIDENCE_ROLES = {"acceptance", "held-out", "negative-control", "mechanism-discrimination"}
OPERATIONAL_STATUSES = {"complete", "partial", "failed"}
VALIDATION_STATUSES = {"passed", "partially-passed", "failed", "inconclusive"}
CLAIM_STATUSES = {
    "supported", "mechanism-consistent", "partially-supported", "unsupported", "inconclusive",
}
RESULT_STATUSES = {"passed", "partially-passed", "failed", "inconclusive"}
CLEAN_RERUN_STATUSES = {"passed", "failed", "not-run"}
MATCH_POLICIES = {"exact-sha256", "criteria-equivalent"}
STUDY_PROFILES = {"stochastic", "empirical", "custom"}
PROFILE_CHECK_STATUSES = {"passed", "failed", "inconclusive", "not-applicable"}
ARTIFACT_ROLES = {"source", "configuration", "input", "model", "environment", "output"}

IDENTIFIER = re.compile(r"^[A-Za-z0-9](?:[A-Za-z0-9._-]{0,126}[A-Za-z0-9])?$")
DIGEST = re.compile(r"^[0-9a-f]{64}$")
PORTABLE_COMMAND = re.compile(r"^[A-Za-z0-9._+-]+$")


class EvidenceError(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise EvidenceError(message)


def _keys(value: object, *, allowed: set[str], required: set[str], label: str) -> dict:
    require(isinstance(value, dict), f"{label} must be an object")
    unknown = sorted(set(value) - allowed)
    missing = sorted(required - set(value))
    require(not unknown, f"{label} has unknown fields: {', '.join(unknown)}")
    require(not missing, f"{label} is missing fields: {', '.join(missing)}")
    return value


def _line(value: object, label: str, limit: int = 1000) -> str:
    require(isinstance(value, str), f"{label} must be a string")
    require(0 < len(value) <= limit, f"{label} must contain 1-{limit} characters")
    require(value == value.strip(), f"{label} may not have leading or trailing whitespace")
    require("\n" not in value and "\r" not in value, f"{label} must be one line")
    require(
        not any(ord(character) < 32 or ord(character) == 127 for character in value),
        f"{label} contains a control character",
    )
    return value


def _identifier(value: object, label: str) -> str:
    item = _line(value, label, 128)
    require(IDENTIFIER.fullmatch(item) is not None, f"{label} must be a portable identifier")
    return item


def _digest(value: object, label: str) -> str:
    item = _line(value, label, 64)
    require(DIGEST.fullmatch(item) is not None, f"{label} must be a lowercase SHA-256 digest")
    return item


def _relative_path(value: object, label: str) -> str:
    item = _line(value, label, 512).replace("\\", "/")
    require(not item.startswith("/"), f"{label} must be relative")
    require("//" not in item and re.match(r"(?i)^[A-Z]:", item) is None, f"unsafe {label}: {item}")
    parts = Path(item).parts
    require(parts and all(part not in {"", ".", ".."} for part in parts), f"unsafe {label}: {item}")
    return Path(*parts).as_posix()


def _string_list(value: object, label: str, *, allow_empty: bool = True, limit: int = MAX_ITEMS) -> List[str]:
    require(isinstance(value, list), f"{label} must be a list")
    minimum = 0 if allow_empty else 1
    require(minimum <= len(value) <= limit, f"{label} must contain {minimum}-{limit} entries")
    return [_line(item, f"{label}[{index}]", 500) for index, item in enumerate(value)]


def _argv(value: object, label: str, *, allow_empty: bool = False) -> List[str]:
    result = _string_list(value, label, allow_empty=allow_empty, limit=64)
    if result:
        require(PORTABLE_COMMAND.fullmatch(result[0]) is not None, f"{label}[0] must be a portable command")
        require(sum(len(item) for item in result) <= 8192, f"{label} is too long")
    return result


def _artifact_entry(value: object, label: str) -> dict:
    item = _keys(value, allowed={"role", "path", "sha256"}, required={"role", "path", "sha256"}, label=label)
    role = _line(item["role"], f"{label}.role", 32)
    require(role in ARTIFACT_ROLES, f"unsupported artifact role: {role}")
    return {
        "role": role,
        "path": _relative_path(item["path"], f"{label}.path"),
        "sha256": _digest(item["sha256"], f"{label}.sha256"),
    }


def artifact_set_digest(entries: object) -> str:
    require(isinstance(entries, list), "artifact set must be a list")
    require(1 <= len(entries) <= 512, "artifact set must contain 1-512 entries")
    normalized = [_artifact_entry(item, f"artifactSet[{index}]") for index, item in enumerate(entries)]
    keys = [(item["role"], item["path"].casefold()) for item in normalized]
    require(len(keys) == len(set(keys)), "artifact set contains duplicate role/path entries")
    normalized.sort(key=lambda item: (item["role"], item["path"].casefold(), item["sha256"]))
    payload = json.dumps(normalized, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def _criterion(value: object, index: int) -> dict:
    label = f"criteria[{index}]"
    item = _keys(
        value,
        allowed={
            "id", "statement", "authority", "purpose", "frozenBeforeRun", "evidenceRole",
            "status", "expected", "observed", "evidenceOutputs", "independentFromCalibration",
        },
        required={
            "id", "statement", "authority", "purpose", "frozenBeforeRun", "evidenceRole",
            "status", "expected", "observed", "evidenceOutputs", "independentFromCalibration",
        },
        label=label,
    )
    authority = _line(item["authority"], f"{label}.authority", 32)
    purpose = _line(item["purpose"], f"{label}.purpose", 32)
    evidence_role = _line(item["evidenceRole"], f"{label}.evidenceRole", 32)
    status_value = _line(item["status"], f"{label}.status", 32)
    require(authority in AUTHORITIES, f"unsupported criterion authority: {authority}")
    require(purpose in CRITERION_PURPOSES, f"unsupported criterion purpose: {purpose}")
    require(evidence_role in EVIDENCE_ROLES, f"unsupported criterion evidence role: {evidence_role}")
    require(status_value in RESULT_STATUSES, f"unsupported criterion status: {status_value}")
    frozen = item["frozenBeforeRun"]
    independent = item["independentFromCalibration"]
    require(isinstance(frozen, bool), f"{label}.frozenBeforeRun must be a boolean")
    require(isinstance(independent, bool), f"{label}.independentFromCalibration must be a boolean")
    outputs = [
        _relative_path(path, f"{label}.evidenceOutputs[{path_index}]")
        for path_index, path in enumerate(
            _string_list(item["evidenceOutputs"], f"{label}.evidenceOutputs", allow_empty=False)
        )
    ]
    require(len(outputs) == len(set(outputs)), f"{label}.evidenceOutputs contains duplicates")
    return {
        "id": _identifier(item["id"], f"{label}.id"),
        "statement": _line(item["statement"], f"{label}.statement"),
        "authority": authority,
        "purpose": purpose,
        "frozenBeforeRun": frozen,
        "evidenceRole": evidence_role,
        "status": status_value,
        "expected": _line(item["expected"], f"{label}.expected"),
        "observed": _line(item["observed"], f"{label}.observed"),
        "evidenceOutputs": outputs,
        "independentFromCalibration": independent,
    }


def _status(value: object, criteria: List[dict], evidence_basis: str) -> dict:
    item = _keys(
        value,
        allowed={"operational", "validation", "claim"},
        required={"operational", "validation", "claim"},
        label="status",
    )
    operational = _line(item["operational"], "status.operational", 32)
    validation = _line(item["validation"], "status.validation", 32)
    claim = _line(item["claim"], "status.claim", 32)
    require(operational in OPERATIONAL_STATUSES, f"unsupported operational status: {operational}")
    require(validation in VALIDATION_STATUSES, f"unsupported validation status: {validation}")
    require(claim in CLAIM_STATUSES, f"unsupported claim status: {claim}")
    if claim in {"supported", "mechanism-consistent"}:
        require(
            operational == "complete" and validation == "passed",
            f"{claim} requires complete execution and passed validation",
        )
    elif claim == "partially-supported":
        require(
            operational in {"complete", "partial"} and validation == "partially-passed",
            "partially-supported requires complete/partial execution and partially-passed validation",
        )
    elif claim == "unsupported":
        require(
            operational == "complete" and validation == "failed",
            "unsupported requires complete execution and failed validation",
        )
    else:
        require(
            operational in {"complete", "partial", "failed"} and validation == "inconclusive",
            "inconclusive claim requires attempted execution and inconclusive validation",
        )
    result_statuses = {criterion["status"] for criterion in criteria}
    if validation == "passed":
        require(result_statuses == {"passed"}, "passed validation requires every criterion to pass")
        require(claim in {"supported", "mechanism-consistent"}, "passed validation requires a positive claim")
    elif validation == "partially-passed":
        require(result_statuses != {"passed"} and result_statuses & {"passed", "partially-passed"}, "partially-passed validation requires mixed or partial positive evidence")
        require(claim == "partially-supported", "partially-passed validation requires partially-supported claim")
    elif validation == "failed":
        require("failed" in result_statuses and claim == "unsupported", "failed validation requires a failed criterion and unsupported claim")
    else:
        require("inconclusive" in result_statuses and claim == "inconclusive", "inconclusive validation requires an inconclusive criterion and claim")

    if claim in {"supported", "mechanism-consistent", "partially-supported", "unsupported"}:
        require(all(item["frozenBeforeRun"] for item in criteria), "evaluated criteria must be frozen before the final run")
    positive_scientific = [
        item for item in criteria
        if item["status"] in {"passed", "partially-passed"}
        and item["purpose"] == "scientific-validity"
        and item["authority"] in {"paper", "method", "domain"}
    ]
    if claim in {"supported", "mechanism-consistent", "partially-supported"}:
        require(positive_scientific, "positive claim requires non-user scientific-validity evidence")
    if evidence_basis == "mechanism-consistency":
        if claim == "supported":
            require(
                any(
                    item["status"] == "passed"
                    and item["independentFromCalibration"]
                    and item["evidenceRole"] in {"held-out", "negative-control", "mechanism-discrimination"}
                    for item in positive_scientific
                ),
                "supported mechanism claim requires independent discriminating evidence",
            )
        elif validation == "passed":
            require(claim == "mechanism-consistent", "mechanism-only pass must be mechanism-consistent")
    else:
        require(claim != "mechanism-consistent", "mechanism-consistent claim requires mechanism evidence")
    return {"operational": operational, "validation": validation, "claim": claim}


def _clean_rerun(value: object, criteria: List[dict]) -> dict:
    item = _keys(
        value,
        allowed={
            "status", "argv", "environmentDigest", "freshWorkspace", "outputsRemovedBeforeRun",
            "outputs", "matchPolicy", "validatedCriteria",
        },
        required={
            "status", "argv", "environmentDigest", "freshWorkspace", "outputsRemovedBeforeRun",
            "outputs", "matchPolicy", "validatedCriteria",
        },
        label="cleanRerun",
    )
    status_value = _line(item["status"], "cleanRerun.status", 32)
    require(status_value in CLEAN_RERUN_STATUSES, f"unsupported clean-rerun status: {status_value}")
    argv = _argv(item["argv"], "cleanRerun.argv", allow_empty=status_value == "not-run")
    fresh = item["freshWorkspace"]
    removed = item["outputsRemovedBeforeRun"]
    require(isinstance(fresh, bool), "cleanRerun.freshWorkspace must be a boolean")
    require(isinstance(removed, bool), "cleanRerun.outputsRemovedBeforeRun must be a boolean")
    outputs_raw = item["outputs"]
    require(isinstance(outputs_raw, list), "cleanRerun.outputs must be a list")
    minimum = 1 if status_value == "passed" else 0
    require(minimum <= len(outputs_raw) <= MAX_ITEMS, f"cleanRerun.outputs must contain {minimum}-{MAX_ITEMS} entries")
    outputs: List[dict] = []
    for index, raw in enumerate(outputs_raw):
        label = f"cleanRerun.outputs[{index}]"
        entry = _keys(raw, allowed={"path", "sha256"}, required={"path", "sha256"}, label=label)
        outputs.append({
            "path": _relative_path(entry["path"], f"{label}.path"),
            "sha256": _digest(entry["sha256"], f"{label}.sha256"),
        })
    require(len({item["path"] for item in outputs}) == len(outputs), "cleanRerun.outputs contains duplicates")
    policy = _line(item["matchPolicy"], "cleanRerun.matchPolicy", 32)
    require(policy in MATCH_POLICIES, f"unsupported clean-rerun match policy: {policy}")
    validated = _string_list(item["validatedCriteria"], "cleanRerun.validatedCriteria")
    criterion_ids = {item["id"] for item in criteria}
    require(set(validated).issubset(criterion_ids), "cleanRerun references unknown criteria")
    if status_value == "passed":
        require(fresh and removed, "passed clean rerun requires a fresh workspace and removed outputs")
        if policy == "exact-sha256":
            require(not validated, "exact-sha256 clean rerun does not need criterion declarations")
        else:
            require(set(validated) == criterion_ids, "criteria-equivalent clean rerun must re-evaluate every criterion")
    elif status_value == "not-run":
        require(not argv and not fresh and not removed and not outputs and not validated, "not-run clean rerun may not claim execution evidence")
    return {
        "status": status_value,
        "argv": argv,
        "environmentDigest": _digest(item["environmentDigest"], "cleanRerun.environmentDigest"),
        "freshWorkspace": fresh,
        "outputsRemovedBeforeRun": removed,
        "outputs": outputs,
        "matchPolicy": policy,
        "validatedCriteria": validated,
    }


def _study_profile(value: object) -> Optional[dict]:
    if value is None:
        return None
    item = _keys(value, allowed={"kind", "checks"}, required={"kind", "checks"}, label="studyProfile")
    kind = _line(item["kind"], "studyProfile.kind", 32)
    require(kind in STUDY_PROFILES, f"unsupported study profile: {kind}")
    require(isinstance(item["checks"], list), "studyProfile.checks must be a list")
    require(1 <= len(item["checks"]) <= MAX_ITEMS, f"studyProfile.checks must contain 1-{MAX_ITEMS} entries")
    checks: List[dict] = []
    names: set[str] = set()
    for index, raw in enumerate(item["checks"]):
        label = f"studyProfile.checks[{index}]"
        check = _keys(raw, allowed={"name", "status", "detail"}, required={"name", "status", "detail"}, label=label)
        name = _identifier(check["name"], f"{label}.name")
        require(name.casefold() not in names, f"duplicate study-profile check: {name}")
        names.add(name.casefold())
        status_value = _line(check["status"], f"{label}.status", 32)
        require(status_value in PROFILE_CHECK_STATUSES, f"unsupported study-profile check status: {status_value}")
        checks.append({"name": name, "status": status_value, "detail": _line(check["detail"], f"{label}.detail")})
    return {"kind": kind, "checks": checks}


def validate_record(value: object) -> dict:
    record = _keys(
        value,
        allowed={
            "schemaVersion", "targetId", "evidenceBasis", "claim", "sourceIdentity",
            "artifactSetDigest", "criteria", "status", "cleanRerun", "studyProfile",
        },
        required={
            "schemaVersion", "targetId", "evidenceBasis", "claim", "sourceIdentity",
            "artifactSetDigest", "criteria", "status", "cleanRerun",
        },
        label="evidence record",
    )
    require(record["schemaVersion"] == SCHEMA_VERSION, f"unsupported evidence schema: {record['schemaVersion']}")
    basis = _line(record["evidenceBasis"], "evidenceBasis", 64)
    require(basis in EVIDENCE_BASES, f"unsupported evidence basis: {basis}")
    source = _keys(
        record["sourceIdentity"],
        allowed={"role", "locator", "sha256"},
        required={"role", "locator", "sha256"},
        label="sourceIdentity",
    )
    source_role = _line(source["role"], "sourceIdentity.role", 32)
    require(source_role in SOURCE_ROLES, f"unsupported source identity role: {source_role}")
    require(isinstance(record["criteria"], list), "criteria must be a list")
    require(1 <= len(record["criteria"]) <= MAX_ITEMS, f"criteria must contain 1-{MAX_ITEMS} entries")
    criteria = [_criterion(item, index) for index, item in enumerate(record["criteria"])]
    ids = [item["id"].casefold() for item in criteria]
    require(len(ids) == len(set(ids)), "criteria contains duplicate ids")
    status_value = _status(record["status"], criteria, basis)
    clean = _clean_rerun(record["cleanRerun"], criteria)
    return {
        "schemaVersion": SCHEMA_VERSION,
        "targetId": _identifier(record["targetId"], "targetId"),
        "evidenceBasis": basis,
        "claim": _line(record["claim"], "claim"),
        "sourceIdentity": {
            "role": source_role,
            "locator": _line(source["locator"], "sourceIdentity.locator", 500),
            "sha256": _digest(source["sha256"], "sourceIdentity.sha256"),
        },
        "artifactSetDigest": _digest(record["artifactSetDigest"], "artifactSetDigest"),
        "criteria": criteria,
        "status": status_value,
        "cleanRerun": clean,
        "studyProfile": _study_profile(record.get("studyProfile")),
    }


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def _load_json_file(path: Path, label: str, limit: int) -> object:
    try:
        mode = path.lstat().st_mode
    except FileNotFoundError as exc:
        raise EvidenceError(f"missing {label}: {path}") from exc
    require(not stat.S_ISLNK(mode), f"{label} may not be a symlink: {path}")
    require(stat.S_ISREG(mode), f"{label} must be a regular file: {path}")
    require(path.stat().st_size <= limit, f"{label} exceeds the size limit")
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise EvidenceError(f"{label} is not valid UTF-8 JSON: {path}") from exc


def load_record(path: Path, expected_sha256: Optional[str] = None) -> Tuple[dict, str]:
    value = _load_json_file(path, "evidence record", MAX_RECORD_BYTES)
    digest = sha256_file(path)
    if expected_sha256 is not None:
        require(_digest(expected_sha256, "expected evidence digest") == digest, "evidence record SHA-256 mismatch")
    return validate_record(value), digest


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--record", type=Path, required=True)
    parser.add_argument("--expect-sha256")
    parser.add_argument("--artifact-set", type=Path, help="optional JSON list used to verify artifactSetDigest")
    parser.add_argument("--json", action="store_true")
    arguments = parser.parse_args(argv)
    try:
        record, digest = load_record(arguments.record, arguments.expect_sha256)
        if arguments.artifact_set is not None:
            artifact_entries = _load_json_file(arguments.artifact_set, "artifact set", MAX_RECORD_BYTES)
            require(
                artifact_set_digest(artifact_entries) == record["artifactSetDigest"],
                "artifact set digest does not match the evidence record",
            )
    except (EvidenceError, OSError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    summary = {
        "schemaVersion": record["schemaVersion"],
        "targetId": record["targetId"],
        "evidenceBasis": record["evidenceBasis"],
        "validationStatus": record["status"]["validation"],
        "claimStatus": record["status"]["claim"],
        "cleanRerunStatus": record["cleanRerun"]["status"],
        "sha256": digest,
    }
    if arguments.json:
        print(json.dumps(summary, ensure_ascii=False, sort_keys=True))
    else:
        print(f"valid evidence record: {summary['targetId']} ({digest})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
