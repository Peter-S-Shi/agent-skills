---
name: agent-session-review
description: Review an accessible AI coding session or project workflow from native session evidence; reconstruct work, compare sessions, and recommend concrete efficiency improvements even when token counts are unavailable.
---

# Agent Session Review

Use this Skill for a natural-language request to retrospectively review the current AI coding Session or an evidence-accessible project. It is an independent workflow review, not a requirement to install or invoke `agent-usage-accounting`. Do not turn a request for token totals alone into a workflow audit.

## Scope and evidence

1. Resolve `current-session` from the executing agent's native Session context, or `project` from a verified repository identity or an explicitly named logical project. Discover candidate Sessions using only native indexes, records, or user-supplied evidence that this runtime is authorized to inspect. A title, folder name, or Git worktree is a clue, not proof of project membership. Deduplicate verified provider-qualified Session identities. Ask one narrow question if ambiguity materially changes the review.
2. State the inspected source boundary, Session selection, accessible providers, evidence cutoff, missing or ambiguous records, and what the agent cannot see. Preserve original records read-only. Do not assume one provider's files or a specific JSONL schema are available in another environment; use native tools or records actually supported here. Never claim an all-agent project review from a partial discovery set.
3. Reconstruct the observable work before diagnosing it: task framing, context inspection, decisions, implementation, tests, failures/corrections, handoffs, and completion where evidenced. For project scope, compare Session purposes and transitions as well as repeated patterns; do not collapse different task sizes into one crude score.
4. Apply the seven dimensions in [Analysis framework](references/analysis-framework.md). Resource Efficiency may use reliable native token/allowance evidence, tool/runtime repetition, or other observable resource proxies. If no trustworthy token counters exist, mark token consumption `unavailable` and still review the workflow. Never infer token cost from transcript length, equate more tokens with waste, or convert token volume to credits/currency without a valid source contract.
5. Deliver a concise, prioritized review using [Report guide](references/report-guide.md). For consequential findings, keep **Evidence → Interpretation → Impact → Recommendation** visible and grade the claim `Directly Observed`, `Strongly Supported`, or `Possible`. Preserve successful behavior and necessary discovery; do not call every retry or full test run avoidable. Compare against a prior report only when supplied, with task-size comparability caveats. Candidate long-term principles require explicit user approval before adoption.

## Output and privacy

Default to the full report in Chat, in the user's requested language or the conversation language. Without a specified output destination, create **no** report, cleaned transcript, manifest, database, hidden project file, or Git change; offer export once after the Chat answer. Save only when the user explicitly authorizes an output location and the runtime permits it. If export is requested without a location, use a genuine host-standard artifact mechanism if available; otherwise ask for a path. Derived files, if explicitly requested, are optional snapshots, not a prerequisite for later reviews.

Do not disclose raw prompts, secrets, private Session identifiers, or local absolute paths gratuitously. If native evidence is absent, ambiguous, or outside permissions, give a qualified partial review or `unavailable` for the affected claim rather than fabricating a complete workflow. This Skill has no mandatory Codex parser, cleaner, prompt generator, manifest, or fixed output directory.
