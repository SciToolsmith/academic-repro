# Customer delivery

The customer folder is the finished reproduction, not the investigation record. It should immediately show the result, what produced it, how to rerun it, and what it establishes. Build it from a fresh whitelist after validation.

## Completed target

Include only:

1. the requested primary result;
2. the actual generating source, in the language and runtime used;
3. configuration read by that source;
4. indispensable non-regenerable inputs or models;
5. the smallest dependency declaration;
6. required third-party notices; and
7. requested or independently useful extras.

Add a short `README.md`. Open with one compact reproduction statement: evidence level, paper target or reported value, observed result, supported and unsupported parts of the local claim, material substitutions, and limits. Then give one exact command, required inputs, and dependencies. Prefer a flat folder for one target and share only genuinely reused inputs.

Exclude drafts, duplicates, searches, caches, probes, logs, QA overlays, failed experiments, and regenerable intermediate CSV/JSON outputs. Keep formal evidence records and clean-rerun receipts internal unless an audit bundle is requested. The delivered source should produce the primary result by default; diagnostics need an option. Do not replace the executed native source with an unrelated port, disguise an image as source, add a decoy driver, or include code that does not generate the result.

## Blocked exact route

Do not manufacture a package when an indispensable, non-regenerable input blocks the exact route before execution. Assessment-only work ends in chat. When reproduction files or a customer folder were requested, deliver a one-screen `README.md` and nothing else. State the target, that exact reproduction was not run, the missing material, the bounded authoritative sources checked, and the smallest item that would unblock it. Include no source, dependency or configuration file, command, synthetic substitute, diagnostic, evidence record, or rerun receipt.

A substitute-data reproduction, image-derived approximation, or future-ready scaffold is a separate objective. Produce one only when explicitly requested; then follow the normal route and delivery rules for what actually ran.

## Clean rerun

Before claiming `rerunnable`, `verified`, or formal machine verification, copy only proposed customer files into a clean temporary directory, remove declared outputs, and execute the exact README command. Confirm that dependencies suffice; no undisclosed paths, caches, credentials, or local-only files are read; the primary result is regenerated at the documented path; and the command creates no unrelated noise.

For a formal v5 package, bind the command, environment digest, recreated outputs, hashes, and criterion checks in the internal evidence record. A small manual delivery needs only a concise verification note. If clean rerun is impossible, state what was checked and what still depends on an unavailable runtime, license, service, or input. Never call such a package self-contained or machine-verified.

## Inputs and rights

Include an input or model only when the final route reads it, it cannot be regenerated, and redistribution is permitted. A comparison crop is not a production input unless pixels are read during rerun.

For a large, private, licensed, or restricted required file, omit it and state its identity and expected location, authorized acquisition source, available integrity check, and effect on rerunning. Call a package self-contained only when every required component may be included and was verified. Do not redistribute papers, private paths, credentials, or third-party material without suitable rights.

## Optional delivery assembler

Manual assembly is default for a small delivery. Use `<skill-root>/scripts/assemble_delivery.py` when multi-target structure, shared inputs, rights checks, or automated whitelist validation justify it:

```bash
python <skill-root>/scripts/assemble_delivery.py \
  --plan /path/to/delivery-plan.json \
  --output-root /path/to/customer-deliveries
```

Use `academic-repro.delivery-plan/v5` only when machine-bound evidence is worthwhile. It binds each validated scientific target to an `academic-repro.evidence/v1` record and clean-rerun receipt. Legacy v4 plans remain accepted without that guarantee. These are internal interfaces: use script validation and tests as their reference, and never expose schema vocabulary in the customer README or require the assembler for ordinary work.

Whether assembled manually or by the helper, deliver one clean result and its real means of generation, or one concise blocked note—never process clutter.
