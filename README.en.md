<h1 align="center">Academic Repro</h1>

<p align="center"><strong>From published figures, tables, and computed structures back to a credible, runnable, testable research process</strong></p>
<p align="center"><a href="README.md">简体中文</a> · English · <a href="academic-repro/SKILL.md">Skill specification</a></p>

Academic Repro is a Codex Skill for reproducing the simulation, training, measurement, statistical, or algorithmic process behind an academic figure, table, or computed structure. It asks whether the generated result can replace the published target while supporting the same local paper claim. The goal is not pixel imitation, and a successful command is not proof of an entire paper.

## Install and invoke

```text
Use $skill-installer to install https://github.com/SciToolsmith/academic-repro/tree/main/academic-repro
```

```text
Use $academic-repro to reproduce Figures 1 and 6 and Table 2 from this paper; the results should replace the published targets without changing the nearby argument.
```

Enter both instructions above in a Codex conversation; they are not shell commands.

Inputs may be a paper with target images, a paper with figure or table identifiers, or target images alone. With images alone, the Skill reconstructs only content reliably identifiable from pixels and does not call that a reproduction of the original experiment.

## Core decisions

Academic Repro first asks **how the target was produced and what evidence role it has**, not merely what it looks like:

- A figure, quantitative table, model structure, or topology produced by simulation, training, search, optimization, or statistics is a computational result. It remains an Academic Repro target even when it looks schematic.
- Parameter and scenario tables are usually reproduction inputs; qualitative literature comparisons, notation tables, and capability checklists are explanatory.
- Only author-drawn theory, process, or mechanism diagrams that are not themselves computational outputs are handed to a scientific-diagram tool.
- One table may mix input, computed, and explanatory cells; classify it by column or cell group.

Use direct recomputation when original code and inputs are available. Before implementing independently, make one bounded check only when author or paper-identified code could change the route or evidence boundary. When indispensable original material is not recoverable, build the smallest credible mechanism or use independent data, derivation, or implementation for alternative validation of the local claim. When evidence remains insufficient, state the boundary or blocker. Never fit curves to the published image, cherry-pick seeds after seeing the result, or invent unreported author parameters.

## What counts as passing

A reproduction passes when all applicable scientific gates hold:

1. **Credible generation** — it comes from a transparent, runnable data, equation, model, or algorithm chain rather than image fitting.
2. **Method validity** — data handling, target quantity, comparison, experimental unit, uncertainty, and validity conditions satisfy what this study type actually requires.
3. **Claim preservation** — frozen criteria are supported and the conclusion stays within the local scope warranted by the selected evidence basis.

**Visual-semantic preservation** is an additional gate only when the user requests a replacement or faithful reconstruction. Preserve chart form, panel relations, axes, units, legend mapping, grouping, and normalization when they carry the comparison; palette, typography, spacing, and pixel identity may change.

A threshold is a hard gate only when supported by the paper, an explicit user requirement, a method-validity condition, or defensible domain knowledge. An arbitrary similarity or “benefit retention” percentage may diagnose a result but cannot by itself turn a claim-preserving replacement into a scientific failure.

Targets from one experiment share fixed controls such as data split, base scenario, checkpoint, and metric definition while retaining intended changes such as penetration, topology, noise, or method. A shared upstream failure propagates to dependent targets; a target-specific failure does not hide the others.

## Delivery

The default customer folder contains only the final figure or table, the final source that produces it, indispensable non-regenerable inputs, minimal dependency instructions, and a short README with the conclusion, exact rerun command, key assumptions, and material limitations. Search history, debug logs, working drafts, validation ledgers, and irrelevant intermediate files remain internal. A clean-copy rerun is required before formal delivery or a claim that executable work is verified and rerunnable.

Evidence effort scales with risk: read-only assessment creates no record; an ordinary single-target reproduction keeps one compact summary; only a formal machine-verifiable package binds an evidence record and clean-rerun receipt. Study-specific checks for randomness, data splits, leakage, or repeated trials are enabled only when they could change the conclusion, avoiding a universal form that wastes time and tokens.

The scientific decision workflow is operating-system independent. Bundled helpers require Python 3.10+ and currently target Linux/macOS; the complete workflow is not supported on Windows. Automatic PDF target location also needs `Pillow`, `pdfplumber`, and Poppler and currently recognizes English `Fig.`/`Figure` followed by a positive integer. Chinese labels, supplementary figures, tables, panels, and other complex labels can be supplied directly or bound with a reviewed manual label. See the [Skill specification](academic-repro/SKILL.md) for the full workflow.

## Local development and validation

```bash
git clone https://github.com/SciToolsmith/academic-repro.git
cd academic-repro
python -m pip install -r academic-repro/requirements.txt
python -m unittest discover -s tests -v
```

## License

Academic Repro is released under the [MIT License](LICENSE). Papers, datasets, third-party code, and generated artifacts retain their respective rights, access conditions, and licenses.
