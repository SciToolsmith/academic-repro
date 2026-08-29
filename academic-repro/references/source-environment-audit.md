# Source, data, formula, and environment checks

Use this reference only when an unresolved fact about code, data, equations, or runtime can change the reproduction route, accepted claim, safety, material cost, or required deliverable. Missing information alone is not a reason for broad discovery.

## Start from the target-producing chain

Read the caption, target-relevant paper sections, supplement and availability statements, and supplied or already-local files first. Trace only the stages that can affect the requested target: input selection, preprocessing or calibration, model or method, aggregation or statistics, and visual encoding. Bind the exact target to an entry point, input, consequential parameters, and output before treating related author code as its implementation.

Name the unresolved fact and the decision it can change. Investigate it only when the answer matters. Do not audit an entire paper, repository, computer, or software ecosystem for completeness.

## Prefer the strongest relevant authority

Use sources in this order when applicable:

1. verified user-supplied files;
2. the paper, supplement, author, publisher, or official project;
3. an institution, funder, or paper-cited repository;
4. a verified archive;
5. a clearly labelled third-party source.

Search only when local evidence is insufficient, an authoritative source is likely to answer the named question, and the answer changes the next action. Check identity, version, access terms, license, format, and relevance before retrieving the smallest necessary artifact; public access does not imply redistribution permission. Retain material source identity and rights internally.

## Check source and code minimally

Author code and its native data format are usually strongest for author-workflow recomputation, but they are not automatically required for every independent or claim-equivalent test. First determine which source actually implements each target-producing stage. Hosting ownership alone does not decide the route: a paper-identified third-party implementation may support direct recomputation when evidence shows that it produced the target; otherwise related third-party code is alternative evidence. Code from another figure does not establish this target's workflow.

Track method provenance and input identity independently. Missing exact input does not make a target-relevant author method irrelevant: native source may still be run on a paper-defined simulation or declared substitute. That supports the author method under the stated input, not exact regeneration of the published target. Conversely, exact input with a translated implementation is a same-input independent route, not author-native recomputation.

Inspect target-relevant entry points, dependencies, defaults, randomness, I/O, preprocessing, aggregation, plotting transforms, and unsafe external effects before execution. `scripts/inspect_artifact.py` can assist without running the artifact.

Use the smallest reviewed smoke test that can establish whether the chosen stage runs. A smoke test proves capability, not reproduction. Keep compatibility changes small and state whether they alter scientific behavior.

## Establish data identity

Match data by evidence, not filename or topic. Check only identity fields that can distinguish the paper case, such as variables, units, sampling, split or segment, preprocessing, version, rights, and a hash when useful.

Classify the input honestly as exact original, official example, paper-defined simulation, declared substitute, or unavailable/restricted. A substitute may support a narrower mechanism or robustness claim, but it does not become the original experiment.

## Check formulas where they affect the result

Verify only details that can change an observable or decision: definitions, units, shapes, indexing, signs, normalization, boundary conditions, ranges, and target-relevant values.

When paper and code differ materially, preserve both readings. Compare them if both answer the objective, ask when the choice changes the supported claim, or narrow/block the affected claim when neither can be justified. Never silently correct an expression or choose the interpretation that most resembles the published image.

## Preserve the native route when it serves the objective

For author-workflow reproduction, preserve the author language, source path, and native runtime by default when the target mapping is credible and a compatible existing environment is usable. This avoids an unnecessary port and keeps the delivered source aligned with the executed route. Do not translate merely because another language is familiar or its ecosystem is easier to package.

Native execution is not a universal requirement. A transparent independent implementation may be primary when the user requests portability or independence, when a materially different implementation is the scientific test, or when the native route is genuinely unavailable, unsafe, or incapable of the target operation. State the reason and changed evidence boundary; do not present a port as author-native execution.

Identify the runtime from author documentation, a launcher or manifest, dependencies, and target-relevant syntax; an extension or data format alone is insufficient. Prefer an existing compatible environment and inspect only prerequisites required by the route. Use `scripts/probe_environment.py` only to resolve a consequential live uncertainty.

A discovered installation does not prove that its license, packages, entry point, data, or target operation works. After static review, run the smallest safe target-relevant operation. An already-installed and already-activated proprietary runtime may be used when this requires no new agreement, login, payment, activation, shared license, privilege, or remote service. A failed or timed-out probe is inconclusive rather than proof of absence. Follow [permission-gates.md](permission-gates.md) before any new authority or uncertain system effect.

## Preserve the evidence boundary and stop

State the route and, for every substitution, why it serves the objective, what boundary changes, and what compatibility evidence supports it. Two implementations running does not establish equivalence.

Stop when the route is scientifically defensible, remaining gaps cannot change acceptance, the strongest relevant authority confirms absence or restriction, or another check cannot change the next action. After one bounded authoritative pass, do not widen the search merely to recover an unavailable exact realization. Use a transparent narrower route when it still answers the objective, or report the exact-original case as blocked.

Keep discarded sources, inventories, probes, and logs internal. Deliver only identities needed to rerun, dependencies, substitutions, rights, and material limits.
