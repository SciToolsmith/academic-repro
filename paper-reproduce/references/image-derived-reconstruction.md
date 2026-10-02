# Image-derived reconstruction

Use this route when the supplied image is the only reliable source for the requested artifact. It can recover visible geometry or approximate plotted values; it cannot recover the original experiment. If paper context, source data, or code later becomes available, reassess the target instead of silently upgrading a pixel-derived result into scientific recomputation.

## Scope

Image-derived work may produce calibrated data points, a partial redraw, editable vector artwork, rerunnable plotting code based on digitized values, or an appearance reconstruction. Keep each recovered value traceable to visible marks and state material uncertainty.

Do not classify a target from appearance alone. A learned architecture, searched cell, optimized topology, clustering tree, or other computational output remains a Paper Reproduce target even when it consists of boxes, nodes, and arrows. With pixels alone, such provenance may be unknown; do not hand it to a diagram skill merely because it looks schematic. Use [diagram-handoff.md](diagram-handoff.md) only when reliable context establishes that the target is an author-drawn explanatory diagram rather than a computed result.

## Four identifiability outcomes

Choose the strongest outcome the pixels support:

1. **Digitizable visible data.** Axis type, scale, units, series identity, and relevant marks are readable enough for calibration at the requested tolerance. Digitize the visible series or regions and report uncertainty from resolution, mark width, overlap, compression, or calibration. Call the values *image-derived estimates*, not original observations.
2. **Partially identifiable content.** Some panels, labels, series, boundaries, or relative trends are readable while others are occluded or ambiguous. Reconstruct only the identifiable subset. Preserve missing content as unknown; do not complete hidden scientific values by interpolation or visual guesswork.
3. **Appearance-only content.** The user explicitly wants a visual or editable reconstruction and the scientific data are not being claimed. Tracing, layout reconstruction, and styling are allowed, but label the result *appearance reconstruction*. An unqualified request to “reproduce” a scientific image is not permission to downgrade it to this category.
4. **Essentially non-identifiable content.** The requested values, coordinate mapping, series identity, or generating method cannot be identified and are essential to the objective. Stop with a precise boundary and name the smallest material that could change it: for example the paper and target reference, a higher-resolution image, readable axis metadata, source data, plotting code, or method parameters.

Pixels alone do not establish raw data, hidden exact values, preprocessing, model implementation, experimental conditions, sample identity, seed, uncertainty procedure, or the paper's claim. Low-stakes layout choices may be assumed for a redraw, but hidden scientific content may not. Never trace a curve and describe it as simulation, tune guessed parameters to resemble the image, or present a visual fit as independent evidence.

## Reconstruction and validation

Bind the source image and describe only visible panels, coordinate systems, marks, labels, and relationships. Select the smallest suitable technique: calibrated digitization, geometric measurement, tracing/vectorization, layout reconstruction, or plotting from digitized estimates. Without readable axes, restrict quantitative output to normalized or relative geometry.

Validate only identifiable properties: coordinate mapping, panel and legend structure, visible ordering, intersections, peaks, boundaries, topology, requested editability, and rerunnability. Pixel identity is required only when the user makes a measurable appearance detail part of the objective. Stop when the requested identifiable properties are preserved; further pixel chasing does not strengthen scientific evidence.

## Boundary and delivery

For digitized or partial results, state prominently:

> This result reconstructs only geometry or values observable in the supplied image, with stated uncertainty. It does not recover or validate the original data, method, experiment, or scientific conclusion.

Deliver the selected reconstruction, its actual editable or rerunnable source when useful, the derived values needed to understand it, and a short note covering uncertainty, provenance, rights, and limitations. Keep calibration experiments, overlays, traces, searches, and intermediate fits out of the customer folder. Include the source image only when rerunning truly requires it and redistribution is permitted; otherwise identify it without copying restricted pixels. Follow [delivery-contract.md](delivery-contract.md) for the minimal package.
