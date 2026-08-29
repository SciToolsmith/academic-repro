---
name: academic-repro
description: Reproduce or assess computation- and data-derived results from research papers. Use for evidence-backed recomputation, independent reimplementation, mechanism checks, or bounded validation of figures, quantitative tables, and generated structures. Not for paper summaries, author-drawn explanatory diagrams, or styling-only edits.
---

# Academic Repro

Reproduce the evidence behind a target, not its pixels. Build the smallest transparent process that can test the target's narrow local paper claim. Exact appearance matters only when it carries scientific meaning or the user requests a replacement compatible with the original presentation.

## 1. Select the user intent

Keep the requested mode separate from the scientific evidence route:

- **Assess:** explain feasibility, evidence boundaries, likely routes, and blockers. Stay read-only unless the user asks for artifacts or execution.
- **Reproduce:** recover or implement a target-producing chain, run it, and evaluate the declared observables.
- **Validate:** audit an existing reproduction against a frozen target contract; do not silently rebuild or broaden it.
- **Package:** verify and assemble already useful results. Packaging cannot upgrade weak scientific evidence.

## 2. Classify the target by origin

- **Computed result:** produced by measurement, simulation, equations, statistics, training, search, optimization, or another algorithm. This includes generated architectures, topologies, and trees that may resemble schematics.
- **Input or condition:** a parameter, scenario, configuration, geometry, or dataset description used to generate results. Treat it as an input unless its derivation is the target.
- **Explanatory artifact:** an author-drawn theory, mechanism, process, or system diagram. This is outside Academic Repro; read [diagram-handoff.md](references/diagram-handoff.md) only when reconstruction is requested.
- **Image-only evidence:** pixels without sufficient paper, data, or method context. Recover only identifiable information; read [image-derived-reconstruction.md](references/image-derived-reconstruction.md).

Visual form never decides the route. A mixed table or figure may contain separate input, computed, explanatory, and image-derived targets. Resolve uncertain identity from the caption, nearby text, numbering, panels, axes, units, and legends before execution. Read [target-figure-acquisition.md](references/target-figure-acquisition.md) when extraction, identity binding, or multi-target tracking is needed.

## 3. Freeze the scientific target

Before tuning or final execution, establish a compact target contract containing:

1. source identity and exact target locator;
2. the narrow local claim and target origin;
3. observables, units, and acceptance criteria;
4. each criterion's authority and whether it is scientific or only a project preference;
5. requested fidelity: exact output, metric equivalence, local-claim equivalence, or visible reconstruction;
6. evidence basis, material assumptions, consequential unknowns, and evidence boundary.

Keep this contract in reasoning or a short working note when that is sufficient; do not create a form merely to restate the paper. Separate visible observations from author interpretation. Freeze justified criteria before inspecting final outputs; do not lower them after seeing results. A user preference may define project acceptance but does not become scientific authority by itself.

Reconstruct only the target-dependent chain: inputs, preprocessing, method, parameters and randomness, aggregation, and visual encoding. Do not expand into a full-paper reproduction unless an additional stage can change the target's conclusion. Resolve or test an unknown only when plausible choices could change the route, validity, acceptance, or claim.

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

Before independent implementation, make one bounded check for author or paper-identified code only when finding it could change the evidence basis or boundary. Prefer a pinned author-native route when it is material and usable; otherwise stop searching and declare the selected basis. Read [source-environment-audit.md](references/source-environment-audit.md) only while a source or native-environment uncertainty remains consequential.

Never fit hidden parameters to the published image, call traced pixels simulated data, select favorable random seeds after seeing results, or tune until the picture looks right. A mechanism that reproduces a calibrated trend is only mechanism-consistent unless it also passes an independent held-out prediction, negative control, or mechanism-discriminating check.

For related targets, share only controls that the paper's design truly shares. Preserve intended contrasts, validate each target separately, and propagate a shared upstream failure only to dependent targets. Validate panels jointly when the caption's claim depends on their comparison.

## 5. Validate and report without upgrading the evidence

Keep five dimensions distinct: user intent, target origin, evidence basis, validation scope, and final status. Also report operational status, validation status, and scientific-claim status separately.

Apply the scientific gates in [execution-validation.md](references/execution-validation.md): traceable generation, method validity, and claim evaluation. Apply visual-semantic fidelity as an additional gate only when the requested output must replace or faithfully reconstruct the published presentation. A crash or missing dependency does not refute the paper; claim-equivalent evidence does not prove the author's hidden workflow.

Scale evidence work to consequence. Read-only assessment creates no record. An ordinary single-target reproduction keeps only a compact summary of identity, basis, criterion, command, result, and status. A formal executable package adds a machine-bound record and clean-rerun receipt. Add seeds, repetitions, splits, controls, robustness checks, or a full audit bundle only when the study design, release risk, or user request makes them consequential. Follow [evidence-contract.md](references/evidence-contract.md) for this risk ladder.

Before a formal customer delivery or a claim of `rerunnable` or `verified`, execute the exact documented command from a clean copy and bind the receipt, source, inputs, result, criteria, and target identity by digest. Follow [delivery-contract.md](references/delivery-contract.md) whenever delivering executable work.

Default customer delivery stays concise: the primary result, actual generating source, indispensable non-regenerable inputs or configuration, minimum dependencies, and a short README with the conclusion, evidence basis, command, assumptions, and material limits. Keep detailed evidence records internal unless the user requests an audit bundle. For read-only assessment, answer directly and create no artifacts.
