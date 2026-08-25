# Source, data, formula, and environment checks

Use this reference only when an unresolved fact about code, data, equations, or runtime can change the reproduction route, accepted claim, safety, material cost, or required deliverable. Missing information alone is not a reason for broad discovery.

## Start from the target-producing chain

Read the caption, target-relevant paper sections, supplement and availability statements, and supplied or already-local files first. Trace only the stages that can affect the requested target: input selection, preprocessing or calibration, model or method, aggregation or statistics, and visual encoding.

Name the unresolved fact and the decision it can change. Investigate it only when the answer matters. Do not audit an entire paper, repository, computer, or software ecosystem for completeness.

## Prefer the strongest relevant authority

Use sources in this order when applicable:

1. verified user-supplied files;
2. the paper, supplement, author, publisher, or official project;
3. an institution, funder, or paper-cited repository;
4. a verified archive;
5. a clearly labelled third-party source.

Search the network only when local evidence is insufficient, a specific authoritative source is likely to answer the question, and either finding the artifact or confirming its absence changes the next action. Use focused queries for the named artifact, not broad topic or reverse-image archaeology. Inspect metadata, identity, version, access terms, license, format, and likely relevance before downloading. Retrieve the smallest necessary artifact and remember that public access does not imply redistribution permission.

For material sources, retain internally a safe locator, version or commit, checked date, hash when useful, authority, access state, license, and redistribution boundary.

## Check source and code minimally

Author code and its native data format are usually strongest for exact recomputation, but they are not automatically required for claim-equivalent reproduction. First determine which source actually implements each target-producing stage. Missing original input does not make an independently usable author method irrelevant, and code from another figure does not establish this target's workflow.

Inspect code statically before execution. Limit review to target-relevant entry points, dependencies, defaults, randomness, input and output formats, preprocessing, aggregation, plotting transforms, network or system effects, install hooks, binaries, unsafe deserialization, and telemetry. `scripts/inspect_artifact.py` may help with deterministic non-executing inspection.

Use the smallest reviewed smoke test that can establish whether the chosen stage runs. A smoke test proves capability, not reproduction. Keep compatibility changes small and state whether they alter scientific behavior.

## Establish data identity

Match data by evidence, not filename or topic. Check only the fields needed to identify the paper case: variables and units, sampling, duration, channels or specimen/device identifiers, split or segment, preprocessing and calibration, version, hash when useful, license, and restrictions.

Classify the input honestly as exact original, official example, paper-defined simulation, declared substitute, or unavailable/restricted. A substitute may support a narrower mechanism or robustness claim, but it does not become the original experiment.

## Check formulas where they affect the result

Verify only mathematical details that can change an observable or acceptance decision: definitions, units, dimensions and shapes, indexing, signs, normalization, initial or boundary conditions, admissible ranges, and target-relevant parameter values.

When paper and code differ materially, preserve both readings. Compare them if both answer the objective, ask when the choice changes the supported claim, or narrow/block the affected claim when neither can be justified. Never silently correct an expression or choose the interpretation that most resembles the published image.

## Test only the runtime the route needs

Decide first whether native execution matters. It matters when the user requests the author workflow or artifact, or when runtime-specific behavior is claim-defining. Otherwise a transparent independent implementation may be the stronger and simpler scientific test.

Identify the native runtime from affirmative evidence such as author documentation, a launcher or manifest, dependencies, and target-relevant syntax. A filename extension or data format alone is insufficient. Prefer an existing compatible environment and inspect only the packages, functions, licenses, and hardware required by the chosen route. Use `scripts/probe_environment.py` only when a focused probe can resolve a live uncertainty.

A discovered installation does not prove that its license, packages, entry point, data, or target operation works. After static review, run the smallest safe target-relevant operation. A failed or timed-out probe is inconclusive rather than proof of absence. Follow [permission-gates.md](permission-gates.md) before any login, activation, installation, privileged action, shared license, remote execution, or binary with uncertain effects.

## Preserve the evidence boundary and stop

State whether the route is direct recomputation, mechanism reproduction, or alternative validation. For every substitution, state why it serves the objective, what evidence boundary changes, and which compatibility checks support it. Never imply equivalence merely because two implementations run.

Stop when the route is scientifically defensible, remaining gaps cannot change acceptance, the strongest relevant authority confirms absence or restriction, or another check cannot change the next action. After one bounded authoritative pass, do not widen the search merely to recover an unavailable exact realization. Use a transparent narrower route when it still answers the objective, or report the exact-original case as blocked.

Keep discarded sources, inventories, probe transcripts, and diagnostic logs internal. Deliver only source and data identities needed to rerun, actual dependencies, material substitutions, rights, and unresolved capability limits.
