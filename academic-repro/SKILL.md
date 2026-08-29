---
name: academic-repro
description: Reproduce or assess computation- and data-derived research results, including figures, quantitative tables, and generated structures. Use for recomputation, independent reimplementation, mechanism checks, or bounded validation. Not for paper summaries, author-drawn explanatory diagrams, or styling-only edits.
---

# Academic Repro

Reproduce a defensible target-producing process and test its local claim—not hidden details or a reported number at any cost. Default to claim equivalence; pursue exact identity only when requested and supported. Treat mismatch as evidence, not a tuning objective.

## 1. Frame the request and target

Keep user mode separate from evidence route:

- **Assess:** explain feasibility, evidence boundaries, routes, and blockers; stay read-only unless artifacts or execution are requested.
- **Reproduce:** recover or implement the target-producing chain, run it, and evaluate declared observables.
- **Validate:** audit an existing reproduction against a frozen target; do not silently rebuild or broaden it.
- **Package:** verify and assemble useful results; packaging cannot strengthen weak evidence.

Classify the target by how it was produced:

- **Computed result:** output of measurement, simulation, equations, statistics, training, search, optimization, or another algorithm. Generated structures that resemble schematics remain computed results.
- **Input or condition:** a parameter, scenario, configuration, geometry, or dataset description; treat it as input unless its derivation is the target.
- **Explanatory artifact:** an author-drawn theory, mechanism, process, or system diagram outside Academic Repro. Read [diagram-handoff.md](references/diagram-handoff.md) only when reconstruction is requested.
- **Image-only evidence:** pixels without enough paper, data, or method context. Recover only identifiable content; read [image-derived-reconstruction.md](references/image-derived-reconstruction.md).

Visual form never decides the route. Split mixed figures or tables when their parts have different origins. Resolve identity from captions, nearby text, numbering, axes, units, and legends. Read [target-figure-acquisition.md](references/target-figure-acquisition.md) only when extraction or multi-target binding is needed.

Before tuning or final execution, freeze a compact target contract:

1. source identity, target locator, origin, and narrow local claim;
2. observables, units, acceptance criteria, and each criterion's authority;
3. requested fidelity: exact output, metric equivalence, claim equivalence, or visible reconstruction; and
4. evidence basis, material assumptions, consequential unknowns, and evidence boundary.

Keep the contract in reasoning or a short note. Separate observation from interpretation. Freeze scientific criteria and claim-defining choices; presentation may change only while values and scientific encoding remain fixed. User preference may set project acceptance, not scientific authority. Reconstruct only the target-dependent chain, and resolve an unknown only when it can change route, validity, acceptance, or claim.

## 2. Choose the evidence basis

Use the strongest minimal basis that answers the user's question:

- **Author-native recomputation:** target-relevant author material in its required environment.
- **Same-input independent implementation:** an independent implementation on the same material inputs.
- **Mechanism consistency:** whether a reported mechanism can generate the behavior.
- **New-data replication:** the same empirical proposition on independent data.
- **Alternative-method robustness:** the proposition under another defensible method.
- **Mathematical cross-check:** an independent derivation or numerical check.
- **Image-derived reconstruction:** visible values, geometry, topology, or appearance only.
- **Blocked:** no honest basis can answer the objective because a material input, mapping, method, authority, or capability is unavailable.

Keep method provenance and input identity separate. Author code on reconstructed input is not exact target recomputation; a translated implementation on exact input is not author-native recomputation. State what the selected basis cannot establish.

## 3. Select the minimal executable route

Map the target to its author entry point, input, consequential parameters, output, and native runtime before translating. For author-workflow reproduction, preserve usable target-relevant author source and runtime by default. Use a cross-language primary route only for an explicit independence or portability objective, a stronger cross-check, or a genuine native blocker. Read [source-environment-audit.md](references/source-environment-audit.md) only while source, data, formula, or runtime uncertainty can change the route.

Before implementation, gate an exact-output or author-workflow target on indispensable, non-regenerable author-specific input. Check user files, the paper and supplement or availability statement, official author source, and any directly cited data source. If no compatible input exists after this bounded pass, mark the exact route blocked and stop before substitute hunting or artifact creation. Do not digitize, synthesize, port, scaffold, smoke-test, or clean-rerun unless the user chooses a different objective. Paper-defined simulations, public benchmark inputs, and incidental presentation details bypass this gate.

Image-informed palette, typography, spacing, and line style may be inferred while values stay fixed. Scale, normalization, binning, smoothing, and other interpretation-changing encodings require evidence and checks against underlying values. Never choose claim-defining inputs, preprocessing, parameters, splits, seeds, thresholds, or runs to reach the paper's number or appearance. A calibrated feature cannot validate itself.

For related targets, share only controls the paper's design truly shares. Preserve intended contrasts, validate each target separately, and propagate a shared upstream failure only to dependent targets.

## 4. Validate without upgrading the evidence

Run the smallest transparent experiment that tests the frozen contract. Apply the gates in [execution-validation.md](references/execution-validation.md): traceable generation, method validity, and claim evaluation. Add visual-semantic fidelity only for a requested replacement or faithful reconstruction. A successful command is not scientific validation, and visual similarity is not independent evidence.

When a result misses the paper, verify comparability and run only a check that can distinguish a named cause or change status. Evaluate absolute value, relative improvement, trend, and mechanism separately; stop before threshold or pixel chasing. Mismatch alone does not establish misconduct—only what the tested route did not reproduce.

Keep user intent, target origin, evidence basis, validation scope, operational status, validation status, and scientific-claim status distinct. Scale evidence work to consequence: assessment creates no record; ordinary work keeps a compact summary; only formal executable delivery or an explicit `rerunnable` or `verified` claim requires machine-bound evidence and a clean-rerun receipt. Add study-specific checks only when they can change the conclusion. Read [evidence-contract.md](references/evidence-contract.md) when evidence must exceed the ordinary summary.

## 5. Deliver only what the result supports

For a completed target, deliver the primary result, actual generating source in the language and runtime used, indispensable inputs or configuration, minimum dependencies and notices, and a short README with one run command. Keep regenerable diagnostics, evidence records, and receipts internal unless requested or independently useful. Read [delivery-contract.md](references/delivery-contract.md) for executable or multi-target delivery.

For an exact route blocked before execution, assessment-only work ends in chat. When reproduction files or a customer folder are expected, create only a one-screen README naming the target, status, indispensable missing material, bounded sources checked, and smallest item that would unblock it. Do not add source, dependencies, commands, synthetic substitutes, or rerun receipts. Alternative-data reconstruction or a future scaffold is a separate objective and requires an explicit request.
