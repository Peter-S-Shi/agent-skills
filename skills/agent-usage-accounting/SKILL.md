---
name: agent-usage-accounting
description: Account for tokens and separately available quota or credit evidence from an AI coding session or a verified project across accessible sessions. Use for session totals, project attribution, fork-safe rollups, missing counters, and transparent estimates.
---

# Agent Usage Accounting

> **M2 scope:** Current-session rules from M1 remain in force. Project rollups are limited to discoverable, authorized evidence with defensible project attribution and non-overlapping usage. Do not claim universal provider access or whole-project coverage.

## Purpose and trigger

Answer “How much was used?” with the lightest trustworthy evidence. Supported scopes are:

- `current-session` — the active agent session, if discoverable.
- `project` — the accessible, evidence-backed portion of a verified Git repository or explicitly named logical project across one or more sessions/agents.

For project scope, a folder name, chat title, branch or worktree is a discovery clue, not proof of membership. If the user names a logical project without a Git remote, require explicit membership or trustworthy source assignment; do not infer it from similar names.

Do **not** interpret a usage-count request as authorization for comprehensive workflow review, hidden telemetry collection, network calls, or rewriting session logs. This Skill does not grant runtime permissions or guarantee that the provider exposes true token usage.

## Minimal invocation and preflight

Accept ordinary natural language. Determine scope, target project (if needed), available session evidence, provider/model context, and whether the user explicitly requested a file. Infer unambiguous values from context; ask only for missing information that blocks a correct scope decision.

Before use, load the reference(s) relevant to the task:

- [Accounting semantics](references/accounting-semantics.md) — all tasks with counters, cache, reasoning, quotas or source total reconciliation.
- [Evidence and estimation](references/evidence-and-estimation.md) — source discovery, missing usage fields, estimation, confidence.
- [Scope, project, fork](references/scope-project-fork.md) — any project or branched-session question.
- [Report contract](references/report-contract.md) — before output.

## Workflow

1. **Resolve scope and project key.** For `current-session`, identify the real active session. For `project`, resolve a verified Git remote/repository identity or the user's explicit logical project and membership boundary. Ask one narrow question if materially different projects remain plausible.
2. **Discover only accessible evidence, read-only and on demand.** Use authorized native session indexes, records or supplied selections. Deduplicate repeated selections by provider-qualified Session identity before analysis. Record the inspected discovery boundary and inaccessible providers; do not imply a scan of the whole machine.
3. **Fix source cutoffs and locate usage.** Prefer trustworthy native per-call/provider usage; distinguish call events, repeated cumulative snapshots, and aggregates. For live sources, fix complete-record cutoffs and report their time/scope. A latest snapshot after a reset describes its current counter epoch unless source semantics prove lifetime scope.
4. **Attribute and deduplicate before summing.** Follow the [project/fork reference](references/scope-project-fork.md): assign only evidenced call/interval or whole-session usage to the project, identify shared historical calls across copied/forked records, and count independently executed post-fork calls even when text repeats. Keep ambiguous cross-project usage unallocated; never add overlapping aggregates without proven disjointness.
5. **Apply the M1 evidence and accounting rules unchanged.** Validate units, provider field semantics, cache/reasoning non-additivity, and counter epochs. Tokenless logs may support a qualified estimate only with defensible reconstruction; otherwise actual usage is `unavailable`. Keep native totals separate from derived comparisons, quota/credits, and cost.
6. **Report coverage and reconciliation.** For project scope, state the resolved project key, accessible provider/source boundary, selected/deduplicated Sessions or calls, attribution and fork method, evidence cutoffs, confirmed subtotal, estimated/unknown/unallocated segments, per-metric grades, exclusions, and comparability warnings. For current-session scope, preserve the M1 report fields. A live figure is recorded **through** its cutoff. Never call an accessible subtotal the full-project total when unresolved usage may remain.
7. **Honor output mode.** Without an explicit output destination, return the report in Chat and do not create files. Then ask once whether the user wants an export. With an explicit authorized, writable location within the runtime's permissions, save the requested report there. For later export without location, use the agent's normal artifact mechanism if supported.

## Non-negotiable accounting guards

- Never sum repeated cumulative snapshots. A counter reset starts a new epoch; no negative delta or invented bridging amount.
- Never sum duplicated call records on copied/forked histories; never collapse two distinct calls merely because their text matches.
- A Git worktree or chat branch does not itself establish a new project or new model call. Without reliable call identity, lineage or non-overlapping counter intervals, an overlap remains unresolved rather than arithmetically guessed.
- Native reasoning usage may be part of output and may not be additive; unavailable is not zero.
- Token volume is not necessarily subscription quota consumption, monetary cost, or a fair cross-provider price comparator.
- Do not invent source files, model tokens, absolute filesystem paths, implied global coverage, or calibration error bands.
- Session logs are read-only. Project selection/deduplication may be kept ephemerally during the request; no required receipts, storage, shadow manifest, DB, or project-file changes without explicit user request.

## Stop/qualification gates

Pause for clarification only when user intent or project/session identity cannot be resolved without a potentially major miscount. Otherwise complete a **qualified partial** report if evidence permits. Mark missing providers, unavailable fields, ambiguous forks and ambiguous project attribution openly; do not interpolate them into an apparently exact total.
