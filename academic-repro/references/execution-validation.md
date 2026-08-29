# Execution and validation

Run the smallest transparent experiment that can test the frozen target contract. A successful command is not validation, visual similarity is not independent scientific evidence, and packaging cannot strengthen the evidence basis.

## Keep evidence bases distinct

- **Author-native recomputation** tests whether target-relevant author material can regenerate the result under the required environment.
- **Same-input independent implementation** tests implementation robustness on materially equivalent inputs.
- **Mechanism consistency** asks whether a declared mechanism can generate the behavior; it does not identify the author's hidden process.
- **New-data replication** tests the empirical proposition on independent data.
- **Alternative-method robustness** tests whether the proposition survives a materially different defensible method.
- **Mathematical cross-check** independently checks a mathematical or numerical relationship.
- **Image-derived reconstruction** tests only visible values, geometry, topology, appearance, or editability.

Do not require author software merely because it may have been used. Require it when its behavior is claim-defining or the user requests exact native recomputation. Otherwise choose the smallest evidence basis that answers the requested question and state what that basis cannot establish.

## Resolve only consequential unknowns

Resolve, derive, or bound an unknown when plausible choices could change an observable, validity condition, or conclusion. Use a documented assumption when it is consequential but not claim-defining, and fix incidental choices reproducibly. Never select parameters, seeds, runs, or inputs because they resemble the published image.

If a visible feature calibrates an assumption, it cannot also serve as independent validation. Validate another observable, use a held-out prediction or control, or narrow the result to a calibrated reconstruction.

## Apply scientific evidence gates

A scientific target passes only when every applicable scientific gate passes:

1. **Traceable generation:** source, material inputs, command, and outputs can be traced to the target; bind environment and randomness only when they can materially affect the result. The result is computational rather than manually shaped.
2. **Method validity:** the data handling, estimand or target quantity, experimental unit, comparison, uncertainty, and validity conditions required by this type of study are defensible.
3. **Claim evaluation:** frozen criteria are evaluated against observed results and support no broader proposition than the declared evidence basis permits.

Use study-appropriate checks rather than one universal statistical form. Deterministic numerical work does not need sampling fields. For stochastic training, record repetitions, seeds, variability, splits, or leakage controls only when each item is material to the claim. Empirical studies should address the sample or experimental unit and add missingness, dependence, uncertainty, or baselines when the design makes them consequential. Explain a non-applicable item only when a reader could reasonably mistake its omission for a validity gap.

## Apply presentation fidelity only when requested

For a replacement or faithful reconstruction, also preserve the comparison-carrying visual semantics: panels, axes, orientation, scale, units, grouping, series mapping, normalization, reference marks, or node/edge relationships. Pixel identity, chart family, palette, typography, and spacing are not scientific acceptance criteria unless changing them would alter interpretation or the user explicitly requires compatibility.

When the original presentation is misleading or unnecessarily opaque, scientific assessment may use a clearer primary view and optionally provide a visually compatible replacement. Do not let presentation fidelity upgrade or downgrade the scientific evidence status.

## Give criteria an explicit authority and purpose

Each criterion has an authority—paper, method, domain rule, or user—and a purpose—scientific validity or project acceptance. Freeze justified criteria before final outputs. A convenient percentage or user preference may be a useful project threshold, but it does not carry scientific authority unless a paper claim, method condition, or defensible domain rule supports it.

Record expected and observed values or relationships, tolerances where meaningful, and the supporting output. Record independence from calibration when mechanism evidence is involved. Follow [evidence-contract.md](evidence-contract.md) when a machine-bound record is warranted.

## Treat mechanism evidence conservatively

A mechanism that reproduces a calibrated trend is `mechanism-consistent`, not generally `supported`. Upgrade a mechanism-based claim only when at least one passed criterion is independent of calibration and serves as a held-out prediction, negative control, or mechanism-discriminating test. If competing mechanisms remain observationally equivalent, say so.

## Preserve dependency logic

For related targets, reuse only controls that the experiment holds fixed and preserve intended factor levels. Isolate target-specific failures. A shared upstream failure propagates only to dependent targets. Panels may execute separately, but validate them jointly when the caption's claim depends on their comparison.

## Stop and report honestly

Run only the smallest sensitivity check that could change acceptance. Stop when the applicable gates pass, remaining differences do not affect the claim, the next iteration would only chase pixels, or a material blocker remains.

Report operational, validation, and scientific-claim status separately. Use `supported`, `mechanism-consistent`, `partially-supported`, `unsupported`, `inconclusive`, or `not-tested`; image-only and explanatory work use `not-applicable`. A crash, missing dependency, absent input, or incomplete test is inconclusive or blocked—not evidence that the paper is false.

After useful validation, follow [delivery-contract.md](delivery-contract.md). Keep only the proportional internal evidence described in the evidence contract; the customer folder remains concise.
