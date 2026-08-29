---
name: academic-repro
description: Reproduce or assess computation- and data-derived results from research papers. Use for evidence-backed recomputation, independent reimplementation, mechanism checks, or bounded validation of figures, quantitative tables, and generated structures. Not for paper summaries, author-drawn explanatory diagrams, or styling-only edits.
---

# Academic Repro

Reproduce a defensible target-producing process and test its local claim—not hidden details or a reported number at any cost. Default to claim equivalence; pursue exact identity only when requested and supported. Treat mismatch as evidence, not a tuning objective.

## 1. Select the user intent

Separate user mode from evidence route:

- **Assess:** explain feasibility, evidence boundaries, likely routes, and blockers. Stay read-only unless the user asks for artifacts or execution.
- **Reproduce:** recover or implement a target-producing chain, run it, and evaluate the declared observables.
- **Validate:** audit an existing reproduction against a frozen target contract; do not silently rebuild or broaden it.
- **Package:** verify and assemble already useful results. Packaging cannot upgrade weak scientific evidence.

## 2. Classify the target by origin

- **Computed result:** produced by measurement, simulation, equations, statistics, training, search, optimization, or another algorithm. This includes generated architectures, topologies, and trees that may resemble schematics.
- **Input or condition:** a parameter, scenario, configuration, geometry, or dataset description used to generate results. Treat it as an input unless its derivation is the target.
- **Explanatory artifact:** an author-drawn theory, mechanism, process, or system diagram. This is outside Academic Repro; read [diagram-handoff.md](references/diagram-handoff.md) only when reconstruction is requested.
- **Image-only evidence:** pixels without sufficient paper, data, or method context. Recover only identifiable information; read [image-derived-reconstruction.md](references/image-derived-reconstruction.md).

Visual form never decides the route. Split mixed figures or tables into input, computed, explanatory, and image-derived targets. Resolve identity from the caption, nearby text, numbering, axes, units, and legends. Read [target-figure-acquisition.md](references/target-figure-acquisition.md) when extraction or multi-target binding is needed.

## 3. Freeze the scientific target

Before tuning or final execution, establish a compact target contract containing:

1. source identity and exact target locator;
2. the narrow local claim and target origin;
3. observables, units, and acceptance criteria;
4. each criterion's authority and whether it is scientific or only a project preference;
5. requested fidelity: exact output, metric equivalence, local-claim equivalence, or visible reconstruction;
6. evidence basis, material assumptions, consequential unknowns, and evidence boundary.

Keep the contract in reasoning or a short note; do not create a form merely to restate the paper. Separate observation from interpretation. Freeze scientific criteria and claim-defining choices before final outputs. Presentation may change only while values and scientific encoding stay fixed. User preference can define project acceptance, not scientific authority.

Reconstruct only the target-dependent chain. Do not expand into a full-paper reproduction unless another stage can change the conclusion. Resolve an unknown only when plausible choices could change the route, validity, acceptance, or claim.

Before implementation, gate an exact-output or author-workflow target on indispensable, non-regenerable author-specific input. Check user files, the paper and supplement or availability statement, official author source, and any directly cited data source. If no compatible input exists after this bounded pass, mark the exact route blocked and stop before substitute hunting or artifact creation. Do not digitize, synthesize, port, scaffold, smoke-test, or clean-rerun unless the user chooses a different objective. Paper-defined simulations, public benchmark inputs, and incidental presentation details bypass this gate.

## 4. Choose and disclose the evidence basis

Use the strongest minimal basis that answers the user's question:

- **Author-native recomputation:** target-relevant author data, code, model, or equations in the required environment.
- **Same-input independent implementation:** an independent implementation evaluated on the same material inputs.
- **Mechanism consistency:** a minimal reported physical, statistical, or algorithmic mechanism that can generate the behavior.
- **New-data replication:** the same empirical proposition tested on independent data.
- **Alternative-method robustness:** the proposition tested by a materially different defensible method.
- **Mathematical cross-check:** an independent derivation or numerical check of a mathematical claim.
- **Image-derived reconstruction:** only visible values, geometry, topology, or appearance; never the hidden experiment.
- **Blocked:** no honest basis can answer the objective because a material input, mapping, method, authority, or capability is unavailable.

Before translating, map the target to its author entry point, input, consequential parameters, output, and native runtime. For author-workflow reproduction, preserve usable target-relevant author source and runtime by default. Use a cross-language primary route only for an explicit independent or portable objective, a stronger cross-check, or a genuine native blocker, and disclose the boundary. Method provenance and input identity are separate: native author code on reconstructed input is not exact target recomputation. Read [source-environment-audit.md](references/source-environment-audit.md) only while a source or environment uncertainty remains consequential.

Separate image-informed choices. Palette, typography, spacing, and line style may be inferred when values stay unchanged. Scale, normalization, binning, or smoothing require justification and checks against underlying values. Never select claim-defining inputs, preprocessing, parameters, splits, seeds, thresholds, or runs to reach the reported number or appearance. A calibrated feature cannot validate itself; without an independent check, the match remains mechanism-consistent.

For related targets, share only controls that the paper's design truly shares. Preserve intended contrasts, validate each target separately, and propagate a shared upstream failure only to dependent targets. Validate panels jointly when the caption's claim depends on their comparison.

## 5. Validate and report without upgrading the evidence

Keep user intent, target origin, evidence basis, validation scope, and final status distinct. Report operational, validation, and scientific-claim status separately.

Apply the scientific gates in [execution-validation.md](references/execution-validation.md): traceable generation, method validity, and claim evaluation. Add visual-semantic fidelity only for a replacement or faithful reconstruction. When a number misses the paper, verify comparability, then run only a check that can distinguish a named cause or change status. Evaluate absolute value, relative improvement, trend, and mechanism separately; stop before threshold chasing. Mismatch alone does not establish misconduct, only what was not reproduced under tested conditions.

Scale evidence work to consequence. Read-only assessment creates no record. An ordinary single-target reproduction keeps only a compact summary of identity, basis, criterion, command, result, and status. A formal executable package adds a machine-bound record and clean-rerun receipt. Add seeds, repetitions, splits, controls, robustness checks, or a full audit bundle only when the study design, release risk, or user request makes them consequential. Follow [evidence-contract.md](references/evidence-contract.md) for this risk ladder.

Before a formal machine-verifiable delivery or a claim of `rerunnable` or `verified`, run the exact documented command from a clean copy and bind its receipt to the target and artifacts. Do not promote ordinary work merely because files exist. Follow [delivery-contract.md](references/delivery-contract.md) for executable delivery.

For a completed target, default delivery stays concise: primary result, actual generating source in the language and runtime used, indispensable inputs or configuration, minimum dependencies and notices, and a short README with one run command. Keep regenerable diagnostics, evidence records, and receipts internal unless requested or independently useful.

For an exact route blocked before execution, assessment-only work ends in chat. When reproduction files or a customer folder are expected, create only a one-screen README naming the target, status, indispensable missing material, bounded sources checked, and smallest item that would unblock it. Do not add source, dependencies, commands, synthetic substitutes, or rerun receipts. Alternative-data reconstruction or a future scaffold is a separate objective and requires an explicit request.
