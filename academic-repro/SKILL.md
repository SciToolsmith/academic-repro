---
name: academic-repro
description: Reproduce and scientifically assess data-derived research figures, quantitative result tables, and computation-generated structures from papers. Use when Codex should rebuild the smallest credible data-to-result process, test whether a replacement preserves the paper's local claim and visual semantics, or report an evidence-bounded blocker. Do not use for author-drawn explanatory schematics, general paper summaries, or styling-only edits.
---

# Academic Repro

Reproduce the evidence behind a target, not its pixels. The goal is the smallest transparent and rerunnable process that can credibly generate the target's scientific observables and support the same narrow local argument. Exact appearance is secondary unless it carries meaning or the user explicitly requests it.

## 1. Classify by origin and evidence role

Identify the target before choosing a tool or implementation:

- **Computed result:** produced by measurement, simulation, equations, statistics, training, search, optimization, or another algorithm. This includes learned or searched architectures, optimized topologies, clustering trees, and other outputs that may look like schematics. Keep these in Academic Repro.
- **Input or condition:** parameters, scenarios, configurations, or dataset descriptions used to generate results. Treat them as inputs unless their derivation is itself the target.
- **Explanatory artifact:** an author-drawn theory, mechanism, process, or system diagram whose objects and arrows explain an idea rather than report a computational output. This is outside Academic Repro; use [diagram-handoff.md](references/diagram-handoff.md) only if reconstruction is requested.
- **Image-only evidence:** pixels without enough paper, data, or method context. Reconstruct only what is identifiable; consult [image-derived-reconstruction.md](references/image-derived-reconstruction.md).

Visual form alone never decides the route. A table may also be mixed: input columns define conditions, computed columns are reproduction targets, and qualitative literature or capability columns remain explanatory.

If the figure or table identity is uncertain, resolve it before execution using the caption, nearby text, numbering, panels, axes, units, and legends. Read [target-figure-acquisition.md](references/target-figure-acquisition.md) only when identity, extraction, or multi-target tracking is genuinely unclear.

## 2. Define the scientific target

Write a compact internal target contract:

1. its evidence role;
2. the narrow proposition it supports in the caption and nearby text;
3. the observables a replacement must preserve, such as ordering, trend, separation, threshold, error range, dependency, or mechanism;
4. whether exact values, original data, original software, or only claim-equivalent behavior are required.

Separate visible observation from the author's interpretation. Reconstruct only the target-dependent chain: inputs, preprocessing, method, parameters and randomness, aggregation, and visual encoding. Do not expand into a full paper reproduction unless those extra stages can change the target's conclusion.

Classify missing information by consequence. A missing value is important only if it can change the route, scientific claim, validity, acceptance, or rerunnability. Recover claim-defining facts from the paper, supplements, and supplied files first. Fix plausible nuisance values transparently and test sensitivity only when the conclusion depends on them. Never present an assumption as recovered fact.

## 3. Choose the strongest minimal route

Use one of four routes and state its evidence boundary:

- **Direct recompute:** run target-relevant author data, code, model, or equations when available and material to the objective.
- **Mechanism reproduction:** implement the smallest credible physical, statistical, or algorithmic mechanism that can produce the claimed behavior. The author's original software is not mandatory when the claim does not depend on it.
- **Alternative validation:** test the same proposition with an independent dataset, derivation, implementation, or method when the original case cannot be reconstructed but the claim can still be assessed.
- **Blocked:** use only when essential data, mapping, method, authority, or execution capability is unavailable and no honest route can answer the objective.

Prefer a transparent model over decorative imitation. Do not fit hidden parameters to the published image, trace curves and call them simulated results, select favorable random seeds after seeing the output, or tune until the picture looks right. When source recovery or a native environment could materially change the evidence boundary, consult [source-environment-audit.md](references/source-environment-audit.md); otherwise begin the minimal executable route.

For related targets from one experiment, keep true controls fixed and intended contrasts distinct. Share the data version, split, baseline scenario, metric definition, and randomization schedule only where the paper's design shares them. Validate each output separately. A shared upstream failure propagates to dependent targets; a target-specific failure does not invalidate independent targets. Comparative multi-panel figures may run in parts, but validate the panels jointly when the caption's argument depends on their comparison.

## 4. Validate and deliver

A reproduction passes only when all three gates hold:

1. **Credible generation:** the result comes from a transparent executable model, data process, equation, training run, or algorithm consistent with the declared route—not image fitting or manual shaping.
2. **Local-claim preservation:** replacing the published target with the reproduced one would leave its narrow local proposition supported within the declared evidence boundary.
3. **Visual-semantic preservation:** the target retains the comparison-carrying form—panels, axes, orientation, scale, units, grouping, series mapping, normalization, reference marks, or node/edge relationships where they matter. Pixel identity, palette, typography, and spacing are not acceptance criteria by default.

Set hard thresholds only when justified by the paper, an explicit user requirement, a method-validity condition, or a defensible domain rule. A convenient or previously frozen percentage without such a basis is diagnostic, not a scientific pass/fail gate. Define justified criteria before tuning and do not weaken them after seeing results. For complex validation choices, use [execution-validation.md](references/execution-validation.md).

Keep execution status, reproduction status, and paper truth separate. A run failure does not refute the paper; a claim-equivalent result does not prove the author's exact hidden workflow.

Default delivery is concise: the primary result, the actual source that generates it, required non-regenerable inputs or configuration, minimum dependencies, and a short README stating the conclusion, one run command, assumptions, and material limits. Exclude drafts, probes, logs, caches, duplicate versions, and internal validation clutter. Use [delivery-contract.md](references/delivery-contract.md) only for a formal multi-target or rights-sensitive package. For read-only feasibility or interpretation requests, answer directly and create no artifacts.
