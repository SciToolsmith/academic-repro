# Execution and validation

Run the smallest transparent experiment that can test the target's local paper claim. A successful command is not validation, and visual similarity is not independent scientific evidence.

## Choose the strongest minimal route

- **Direct recomputation:** use verified author data, code, and relevant environment when exact workflow recovery is required and available.
- **Mechanism reproduction:** implement the reported equations, physical mechanism, training procedure, or algorithm with explicit assumptions. This is usually sufficient for claim-equivalent reproduction.
- **Alternative validation:** use a declared substitute implementation, dataset, or experiment to test a narrower transferable claim.
- **Image-derived reconstruction:** test only digitization, geometry, appearance, or editability; do not make a mechanism claim.
- **Blocked:** stop the affected claim when a material input or method is unavailable and no credible narrower route exists.

Do not require the author's original software merely because it may have been used. Require it when its behavior is claim-defining or the user requests the native artifact. Otherwise prefer the simplest executable mechanism that preserves the evidence relationship.

## Resolve only consequential unknowns

Resolve, derive, or bound an unknown when plausible choices could change an observable or conclusion. Use a defensible documented assumption when it is consequential but not claim-defining, and fix incidental choices reproducibly. Never select parameters, seeds, runs, or inputs because they look most like the published image.

If a visible feature is used to calibrate an assumption, it cannot also serve as independent validation. Validate another observable or narrow the conclusion to a calibrated reconstruction.

## Apply three acceptance gates

A scientific target passes only when all applicable gates pass:

1. **Credible generation:** the result comes from a transparent executable chain of data, equations, simulation, training, or algorithmic computation rather than image fitting or manual shaping.
2. **Claim preservation:** replacing the published target with the reproduced result would still support the narrow proposition made by its caption and local discussion, within the declared evidence route.
3. **Visual-semantic preservation:** the figure or table retains the form needed to understand and compare the evidence.

Exact pixels, random realization, typography, and every reported value need not match unless the claim depends on them. Trends, ordering, thresholds, magnitudes, uncertainty, or robustness become material when the local argument explicitly relies on them.

## Give thresholds a scientific basis

Acceptance criteria take authority from, in order: an explicit paper claim, an explicit user requirement, a method-validity condition, or a defensible domain check. Freeze justified criteria before inspecting final outputs where practical.

A convenient or previously declared number has no scientific authority by itself. Similarity scores and arbitrary benefit-retention targets may be useful diagnostics, but missing them is not a scientific failure unless one of the authorities above makes that boundary material.

## Preserve comparison semantics

Preserve chart family, panel structure, axes and orientation, units, scale, grouping, normalization, legend mapping, and reference marks when they carry the argument. Do not change the chart family, collapse comparative panels, or reverse an axis when that changes how the evidence is read. Palette, fonts, spacing, and line widths are secondary unless explicitly requested.

For related targets, reuse controls that the experiment holds fixed and preserve the intended levels of varied factors. Isolate target-specific failures. A shared upstream failure propagates only to targets that depend on it. Panels may run separately, but validate them jointly when the caption's claim depends on their comparison.

## Stop and report honestly

Run only the smallest sensitivity check that could change acceptance. Stop when the three gates pass, remaining differences do not affect the claim, or another iteration would only chase pixels. Also stop when the next action cannot materially reduce uncertainty or when a material blocker remains.

Report execution, validation, and scientific interpretation separately. Use `supported`, `partially supported`, `unsupported`, `inconclusive`, or `not tested`; image-only work has no scientific-claim status. A crash, missing dependency, absent input, or incomplete test is inconclusive or blocked—not evidence that the paper is false.

After validation, follow [delivery-contract.md](delivery-contract.md). Deliver the primary result, the code and indispensable inputs that regenerate it, a minimal dependency declaration, and a short README with one rerun command and only interpretation-relevant assumptions or limitations. Keep searches, probes, intermediate versions, QA artifacts, raw logs, and internal records out of the customer folder unless independently useful and explicitly requested.
