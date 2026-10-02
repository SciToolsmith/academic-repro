<h1 align="center">Paper Reproduce</h1>

<p align="center"><strong>From published figures, tables, and computed structures back to a credible, runnable, testable research process</strong></p>
<p align="center"><a href="README.md">简体中文</a> · English · <a href="paper-reproduce/SKILL.md">Skill specification</a></p>

Paper Reproduce is a Codex Skill for reproducing the simulation, training, measurement, statistical, or algorithmic process behind an academic figure, table, or computed structure. It asks whether the result still supports the same local paper claim. The default objective is local-claim equivalence, not the assumption that every omitted detail can be recovered; exact numerical or visual identity is pursued only when requested and supported by the available materials.

## Install and invoke

```text
Use $skill-installer to install https://github.com/SciToolsmith/paper-reproduce/tree/main/paper-reproduce
```

```text
Use $paper-reproduce to reproduce Figures 1 and 6 and Table 2 from this paper; the results should replace the published targets without changing the nearby argument.
```

Enter both instructions above in a Codex conversation; they are not shell commands.

Rename compatibility: existing target-manifest, evidence-record, and delivery-plan schema identifiers are retained so saved work remains readable.

Inputs may be a paper with target images, a paper with figure or table identifiers, or target images alone. With images alone, the Skill reconstructs only content reliably identifiable from pixels and does not call that a reproduction of the original experiment.

## Core decisions

Paper Reproduce first asks **how the target was produced and what evidence role it has**, not merely what it looks like:

- A figure, quantitative table, model structure, or topology produced by simulation, training, search, optimization, or statistics is a computational result. It remains a Paper Reproduce target even when it looks schematic.
- Parameter and scenario tables are usually reproduction inputs; qualitative literature comparisons, notation tables, and capability checklists are explanatory.
- Only author-drawn theory, process, or mechanism diagrams that are not themselves computational outputs are handed to a scientific-diagram tool.
- One table may mix input, computed, and explanatory cells; classify it by column or cell group.

For an author-workflow reproduction, first bind the target to its entry point, input, consequential parameters, and output. When target-relevant author source and a compatible local environment are usable, preserve the original language and native runtime by default: if `.m` source actually runs, deliver `.m` rather than rewriting it for convenience. Make a cross-language implementation primary only for an explicit portability or independence objective, a stronger scientific cross-check, or a genuine native blocker, and disclose the changed evidence boundary. Method provenance and input identity remain separate: author source on reconstructed input is not exact target recomputation.

The published image may inform presentation-only choices such as palette, typography, spacing, and line style. Encoding choices such as axis scale, normalization, binning, and smoothing can alter interpretation, so their basis must be disclosed and underlying values checked separately. Claim-defining input selection, preprocessing, parameters, splits, seeds, thresholds, or runs must not be chosen to reach the paper's number or appearance. A visible feature used for calibration cannot also serve as independent validation.

## What counts as passing

A reproduction passes when all applicable scientific gates hold:

1. **Credible generation** — it comes from a transparent, runnable data, equation, model, or algorithm chain rather than outcome-directed parameter fitting.
2. **Method validity** — data handling, target quantity, comparison, experimental unit, uncertainty, and validity conditions satisfy what this study type actually requires.
3. **Claim preservation** — frozen criteria are supported and the conclusion stays within the local scope warranted by the selected evidence basis.

**Visual-semantic preservation** is an additional gate only when the user requests a replacement or faithful reconstruction. Preserve chart form, panel relations, axes, units, legend mapping, grouping, and normalization when they carry the comparison; palette, typography, spacing, and pixel identity may change.

A threshold is a hard gate only when supported by the paper, an explicit user requirement, a method-validity condition, or defensible domain knowledge. An arbitrary similarity or “benefit retention” percentage may diagnose a result but cannot by itself turn a claim-preserving replacement into a scientific failure.

A paper's reported number is a validation reference, not an optimization objective. If a paper reports a metric above 98% and a comparable reproduction is lower, the Skill first checks the target, input or split, preprocessing, metric definition, code version, and stochastic protocol, then runs only the smallest check that can distinguish a named cause or change evidence status. It evaluates absolute level, relative improvement or ordering, qualitative trend, and mechanism separately. It does not chase the threshold indefinitely or infer fabrication from mismatch alone. Even when exact released code, data, split, and metric repeatedly miss a material claim, the bounded conclusion is that the released materials did not reproduce the claim under tested conditions—not an unsupported misconduct allegation.

Targets from one experiment share fixed controls such as data split, base scenario, checkpoint, and metric definition while retaining intended changes such as penetration, topology, noise, or method. A shared upstream failure propagates to dependent targets; a target-specific failure does not hide the others.

## Delivery

The default customer folder contains only the final figure or table, the actual source in the language used to generate it, indispensable non-regenerable inputs, minimal dependencies and required notices, and a short README. Its opening reproduction statement gives the evidence level, paper target or reported value, observed result, supported and unsupported claim components, substitutions, and material limits, followed by one exact command. Regenerable CSV/JSON, searches, debug logs, drafts, validation ledgers, evidence records, and receipts remain internal unless requested as an audit bundle or independently useful.

A single-target delivery stays flat. Several independently understandable targets are packaged as reproduction-unit folders, each with its own result and concise note; an executable unit also has its actual entrypoint and exact command, while the root README is only an index. A function, dataset, or environment declaration goes under `common/` only when at least two units actually use it, and is kept once. Inseparable coupled panels remain one unit. An optional run-all launcher cannot be the sole implementation path. If one unit is blocked by missing original data, its folder contains only a one-screen status note while completed siblings remain independently usable.

If the exact target depends on unpublished, non-regenerable author-specific raw data, a private split, checkpoint, or sample, the Skill makes one bounded authoritative check. If no compatible input is available, it stops the exact route before broad substitute searches, scaffold construction, or clean reruns. A read-only assessment ends in chat; when reproduction files or a customer folder were requested, delivery is a one-screen README naming the target, missing item, search boundary, and smallest unblocking material. Substitute-data reproduction, pixel approximation, or a future scaffold is created only when the user separately chooses that objective. Paper-defined simulations, public benchmark inputs, and incidental presentation details do not trigger this gate.

Evidence effort scales with risk: read-only assessment creates no record; an ordinary single-target reproduction keeps one compact summary; only a formal machine-verifiable package or an explicit `verified`/`rerunnable` claim binds evidence and requires a clean rerun. Checks for randomness, splits, leakage, or repeated trials are enabled only when they could change the conclusion, avoiding a universal form that wastes time and tokens.

The scientific decision workflow is operating-system independent. Bundled helpers require Python 3.10+ and currently target Linux/macOS; the complete workflow is not supported on Windows. Automatic PDF target location also needs `Pillow`, `pdfplumber`, and Poppler and currently recognizes English `Fig.`/`Figure` followed by a positive integer. Chinese labels, supplementary figures, tables, panels, and other complex labels can be supplied directly or bound with a reviewed manual label. See the [Skill specification](paper-reproduce/SKILL.md) for the full workflow.

## Local development and validation

```bash
git clone https://github.com/SciToolsmith/paper-reproduce.git
cd paper-reproduce
python -m pip install -r paper-reproduce/requirements.txt
python -m unittest discover -s tests -v
```

## License

Paper Reproduce is released under the [MIT License](LICENSE). Papers, datasets, third-party code, and generated artifacts retain their respective rights, access conditions, and licenses.
