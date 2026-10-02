# Execution and validation

Run the smallest transparent experiment that can test the frozen target contract. A successful command is not validation, visual similarity is not independent scientific evidence, and packaging cannot strengthen the evidence basis.

## Keep evidence bases distinct

- **Author-native recomputation:** target-relevant author material in its required environment.
- **Same-input independent implementation:** implementation robustness on equivalent inputs.
- **Mechanism consistency:** whether a declared mechanism can generate the behavior, not the hidden author process.
- **New-data replication:** the proposition on independent data.
- **Alternative-method robustness:** the proposition under a different defensible method.
- **Mathematical cross-check:** an independent derivation or numerical check.
- **Image-derived reconstruction:** visible values, geometry, topology, appearance, or editability only.

For an author-workflow objective, use target-relevant author source in its native runtime when that route is usable. Choose an independent or cross-language primary route when independence or portability is the objective, it is the stronger scientific test, or the native route is genuinely blocked. State what each route cannot establish; do not silently translate and call it author-native.

## Resolve only consequential unknowns

Resolve, derive, or bound an unknown only when plausible choices could change an observable, validity condition, route, or conclusion. Classify image-informed choices before using them:

- **Presentation-only:** palette, typography, spacing, line width, and similar styling may be inferred or refined when computed values and scientific encoding remain fixed.
- **Encoding:** axes, scale, normalization, binning, smoothing, aggregation, and series mapping may alter interpretation. Infer them only from defensible evidence, disclose uncertainty, and check underlying values separately.
- **Claim-defining scientific:** input selection, preprocessing, model parameters, split, seed, threshold, and run selection must not be chosen to reach the paper's value or appearance.

Freeze claim-defining choices before final outputs. A feature used to calibrate any consequential choice cannot also validate it; use another observable, a held-out prediction, or a control, or label the result a calibrated reconstruction.

## Apply scientific evidence gates

A scientific target passes only when every applicable scientific gate passes:

1. **Traceable generation:** source, material inputs, command, and outputs can be traced to the target; bind environment and randomness only when they can materially affect the result. The result is computational rather than manually shaped.
2. **Method validity:** the data handling, estimand or target quantity, experimental unit, comparison, uncertainty, and validity conditions required by this type of study are defensible.
3. **Claim evaluation:** frozen criteria are evaluated against observed results and support no broader proposition than the declared evidence basis permits.

Use study-appropriate checks, not one universal form. Deterministic work needs no sampling fields. Record repetitions, seeds, variability, splits, leakage, missingness, dependence, uncertainty, or baselines only when the design makes them material. Explain a non-applicable item only when omission could look like a validity gap.

## Apply presentation fidelity only when requested

For a replacement or faithful reconstruction, also preserve the comparison-carrying visual semantics: panels, axes, orientation, scale, units, grouping, series mapping, normalization, reference marks, or node/edge relationships. Pixel identity, chart family, palette, typography, and spacing are not scientific acceptance criteria unless changing them would alter interpretation or the user explicitly requires compatibility.

Scientific assessment may use a clearer primary view and optionally a compatible replacement. Presentation fidelity cannot change scientific evidence status.

## Evaluate criteria and discrepancies without chasing the target

Each criterion has an authority—paper, method, domain rule, or user—and a purpose—scientific validity or project acceptance. Freeze justified criteria before final outputs. A convenient percentage or user preference may be a useful project threshold, but it does not carry scientific authority unless a paper claim, method condition, or defensible domain rule supports it.

Record expected and observed values or relationships, tolerances where meaningful, and the supporting output. Record independence from calibration when mechanism evidence is involved. Follow [evidence-contract.md](evidence-contract.md) when a machine-bound record is warranted.

The paper's reported number is a validation reference, never an optimization objective. When the result misses it:

1. check comparability of target, input identity, segment or split, preprocessing, metric definition, code version, and stochastic protocol only where each item can matter;
2. run the smallest native or declared-route check that tests the suspected mismatch;
3. add only a targeted sensitivity or repetition that can distinguish a named cause; and
4. evaluate compound claims separately: absolute level, relative improvement or ordering, qualitative trend, and proposed mechanism may have different statuses.

Report the observed result even when it is less favorable. A mismatch alone cannot establish fabrication. If exact released code, data, split, and metric repeatedly miss a material quantitative claim, report that the released materials did not reproduce it under the tested conditions; do not convert that finding into a misconduct claim. Continue only when the next check can distinguish a cause, change evidence status, or change the user's decision.

## Treat mechanism evidence conservatively

A calibrated trend is `mechanism-consistent`, not `supported`. Upgrade only after an independent held-out prediction, negative control, or mechanism-discriminating test passes. Say when competing mechanisms remain observationally equivalent.

## Preserve dependency logic

For related targets, reuse only controls that the experiment holds fixed and preserve intended factor levels. Isolate target-specific failures. A shared upstream failure propagates only to dependent targets. Panels may execute separately, but validate them jointly when the caption's claim depends on their comparison.

## Stop and report honestly

Run only the smallest sensitivity check that could change acceptance. Stop when the gates pass, remaining differences do not affect the claim, the next iteration would chase pixels or a reported threshold, or a material blocker remains.

Report operational, validation, and scientific-claim status separately. Use `supported`, `mechanism-consistent`, `partially-supported`, `unsupported`, `inconclusive`, or `not-tested`; image-only and explanatory work use `not-applicable`. A crash, missing dependency, absent input, or incomplete test is inconclusive or blocked—not evidence that the paper is false.

After useful validation, follow [delivery-contract.md](delivery-contract.md). Keep only the proportional internal evidence described in the evidence contract; the customer folder remains concise.
