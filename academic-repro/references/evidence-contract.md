# Proportional evidence contract

Evidence should reduce ambiguity, not become a second research project. Use the least expensive tier that can support the requested conclusion, and promote a target only when a real risk or deliverable requires it.

## Choose the evidence tier

- **Assessment:** stay read-only. Report feasibility, likely evidence basis, unknowns, and blockers. Create no evidence file.
- **Ordinary reproduction or validation:** keep one compact summary of target identity, evidence basis, paper target, observed result, criterion, command, and status. A paragraph or small object is enough; do not create a ledger for routine steps.
- **Formal executable package:** use one `academic-repro.evidence/v1` record per validated scientific target, bind it to the delivery, and obtain a clean-rerun receipt.
- **Study-specific or audit work:** add only the checks made consequential by stochastic behavior, empirical design, safety, external release, or an explicit audit request. A full audit bundle is an output choice, not the default workflow.

Do not promote work merely because a field exists in a schema. Promote it when an omitted check could change the route, criterion, status, reproducibility claim, or user's decision.

## Keep the formal record compact

The v1 record stores judgment that cannot be safely derived:

- stable target and source identity;
- evidence basis and narrow local claim;
- frozen criteria with authority, purpose, expected and observed result, and supporting output;
- operational, validation, and scientific-claim status; and
- the clean-rerun receipt.

It does not repeat the delivery plan's file lists, assumptions, entrypoint, or command in several sections. Instead, `artifactSetDigest` is computed canonically from the actual delivered source, configuration, inputs, models, environment declarations, and declared outputs. The assembler recomputes that digest from real files. Models should not hand-copy a long hash manifest when the helper can derive it.

Each criterion states whether it came from the paper, method, domain knowledge, or user, and whether it serves scientific validity or project acceptance. A user preference can accept a deliverable but cannot by itself support a scientific claim. Freeze claim-relevant criteria before the final run.

## Keep claims inside their evidence boundary

Criterion results determine validation and claim status. A successful command is only operational evidence. A failed command does not refute the paper, and a target-local result does not establish paper-wide truth.

A calibrated mechanism match is `mechanism-consistent`. Upgrade it to `supported` only after an independent held-out prediction, negative control, or mechanism-discriminating check passes. This distinction is mandatory because it changes the scientific meaning, not because the schema asks for another field.

## Use clean reruns only for reproducibility claims

A clean rerun is required for a formal machine-verifiable package or before calling work `rerunnable` or `verified`; ordinary reproduction, read-only assessment, and exploration do not automatically enter this tier. Copy proposed customer files into a fresh workspace, remove outputs, run the documented argument vector, and confirm recreation.

Use `exact-sha256` when outputs should be byte-identical. Use `criteria-equivalent` for stochastic or platform-sensitive outputs and re-evaluate every frozen criterion on the clean-run outputs. Merely finding a pre-existing result is not a clean rerun.

## Add study-specific checks conditionally

The optional `studyProfile` records only checks relevant to the design. Examples include seed stability for stochastic work, split integrity or leakage checks for empirical work, and a named domain check for a custom design. Do not require seeds for deterministic equations, train/test checks for simulations without learned data, or repeated trials when they cannot affect the claim.

## Packaging interface

The formal delivery interface is `academic-repro.delivery-plan/v5`. Each validated scientific target in a v5 plan references one internal `academic-repro.evidence/v1` file through an `evidenceRecord` source path and SHA-256. The assembler verifies target identity, route-compatible evidence basis, statuses, the canonical artifact-set digest, criterion output paths, exact rerun command, clean-run outputs, and byte equality when requested.

Legacy `academic-repro.delivery-plan/v4` and `scirepro.delivery-plan/v4` plans remain readable for lightweight or existing workflows, but they do not gain the v5 machine-bound guarantee. Evidence records stay outside the concise customer folder unless the user explicitly requests an audit bundle.
