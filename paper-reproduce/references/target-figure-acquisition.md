# Target acquisition and evidence roles

Use this reference only when target identity or evidence role can change execution or validation. Stop acquiring context once the requested target and its local claim are unambiguous.

## Classify by origin and evidence role

Classify each target, panel, table column, or cell group before choosing a route:

- **computed result:** produced by simulation, measurement processing, statistics, training, search, inference, or optimization;
- **input or configuration:** parameters, scenarios, dataset splits, operating conditions, model settings, or fixed reference values used by a computation;
- **explanatory content:** notation, literature summaries, method capability comparisons, theory, workflow, or author-drawn mechanism descriptions;
- **image-only content:** pixels with no reliable paper, data, or method binding.

Classification follows provenance, not appearance. A schematic-looking searched architecture can be a computed result; a numeric-looking parameter table can be an input. A table may be mixed: keep input columns as conditions, recompute result columns, and leave qualitative comparison cells explanatory. Do not force the whole table into one category.

## Bind the target to its context

Preserve supplied files unchanged. Bind a paper target through its figure or table identifier, panel labels, complete caption or title, axes, units, legends, row and column headers, footnotes, and only the nearby text needed to state the local claim. Preserve page and crop provenance for extracted targets.

For multiple targets, track each one separately and preserve parent-panel relationships. Targets linked by the paper or code may share an experimental lineage; adjacency or visual similarity alone does not establish one. An unresolved target must not block an independently verified target.

Use `scripts/materialize_target_figures.py` when deterministic extraction, normalization, hashing, or replacement is useful. New workspaces use the `academic-repro.targets/v1` manifest identifier. Existing `scirepro.targets/v1` manifests remain readable; updates and derived subsets retain that identifier so older tooling can continue to open them. The normalized image is a viewing aid; the supplied or extracted source remains authoritative.

## Treat images as evidence, not hidden data

A published image can identify the intended variables, comparison layout, visible trend, ordering, scale, and other acceptance observables. It does not reveal the author's original samples, training history, simulator, or unreported parameters.

Do not tune equations, parameters, seeds, series, or model outputs to trace the target image. Do not present digitized pixels as an independent reproduction of the generating mechanism. Pixel extraction is appropriate only when the user explicitly requests digitization or image-derived reconstruction; then validate only the declared visual or geometric objective.

## Rights boundary

Local inspection does not imply redistribution permission. Include target pixels in a customer package only when permitted. Otherwise identify the source durably and deliver the independently generated result without restricted target material.
