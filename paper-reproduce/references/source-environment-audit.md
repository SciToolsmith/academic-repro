# Source, data, formula, and environment checks

Use this reference only when an unresolved fact about code, data, equations, or runtime can change the route, accepted claim, safety, material cost, or deliverable. Missing information alone does not justify broad discovery.

## Bind the target-producing chain

Read the caption, target-relevant paper sections, supplement and availability statements, and supplied or already-local files first. Trace only consequential input, preprocessing, method, aggregation, and visual-encoding stages. Bind the target to its entry point, input, parameters, and output before treating related author code as its implementation.

Name the unresolved fact and the decision it can change. Do not audit an entire paper, repository, computer, or software ecosystem for completeness.

## Prefer the strongest relevant authority

Use sources in this order when applicable:

1. verified user-supplied files;
2. the paper, supplement, author, publisher, or official project;
3. an institution, funder, or paper-cited repository;
4. a verified archive;
5. a clearly labelled third-party source.

Search only when local evidence is insufficient, an authority is likely to answer the named question, and the answer changes the next action. Retrieve the smallest necessary artifact after checking identity, version, access, license, format, and relevance. Public access does not imply redistribution permission.

## Gate exact routes on non-regenerable input

Track method provenance and input identity independently. Author source on a paper-defined simulation or declared substitute can support a narrower route, not exact regeneration of the published target. Exact input with translated source is a same-input independent route, not author-native recomputation.

Match data by distinguishing evidence such as variables, units, sampling, split or segment, preprocessing, version, rights, and a hash when useful. Classify it as exact original, official example, paper-defined simulation, declared substitute, or unavailable or restricted.

For an exact target that depends on an author-specific raw trace, private split, checkpoint, sample, calibration, or similar non-regenerable input, check user files, the paper and supplement or availability statement, the official author project, and any directly cited data source. If that bounded pass finds no compatible input, mark only the exact-original route blocked and stop before broad search, substitute acquisition, digitization, synthesis, porting, scaffold code, smoke tests, or packaging tests.

Offer mechanism, new-data, or image-derived work as a different evidence route; execute it only when it already answers the objective or the user chooses it. Regenerable paper-defined simulations, public benchmark inputs, and incidental presentation details bypass this gate.

## Inspect usable source and runtime

Determine which source implements each consequential stage. Hosting ownership, a matching topic, or code for another figure is insufficient; paper-identified third-party code supports direct recomputation only when evidence binds it to the target.

Inspect target-relevant entry points, dependencies, defaults, randomness, I/O, preprocessing, aggregation, plotting transforms, and unsafe effects before execution. `scripts/inspect_artifact.py` can assist without running the artifact. Use the smallest reviewed smoke test that resolves whether the chosen stage runs; it proves capability, not reproduction.

For author-workflow reproduction, preserve the author language, source path, and native runtime when the mapping is credible and a compatible environment is usable. Use an independent implementation when requested, scientifically stronger, or the native route is genuinely unavailable or unsafe. State the changed evidence boundary; never present a port as author-native.

Identify runtime from author documentation, launchers, manifests, dependencies, and syntax—not extension alone. Prefer an existing compatible environment. Use `scripts/probe_environment.py` only for a consequential live uncertainty. An installation does not prove that its license, packages, entry point, data, or operation works. An already-installed and activated proprietary runtime may be used only when no new agreement, login, payment, activation, shared license, privilege, or remote service is needed. Follow [permission-gates.md](permission-gates.md) for new authority or uncertain effects.

## Check formulas only where consequential

Verify definitions, units, shapes, indexing, signs, normalization, boundary conditions, ranges, and values only when they can change an observable or decision. When paper and code materially differ, preserve both readings; compare them if both answer the objective, ask when they answer different questions, or narrow the claim. Never choose the reading that merely looks most like the figure.

## Preserve the boundary and stop

For every substitution, state why it serves the objective, how the boundary changes, and what supports compatibility. Two implementations running does not establish equivalence.

Stop when the route is defensible, remaining gaps cannot change acceptance, an authority confirms absence or restriction, or another check cannot change the next action. Do not widen a completed bounded pass merely to recover an unavailable exact realization. Keep discarded sources, inventories, probes, and logs internal.
