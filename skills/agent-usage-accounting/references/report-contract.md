# Chat Report and Optional Export Contract

**M0 draft.** Report language follows the user's request/context; no mandatory English default. Keep routine accounting concise. Depth increases only when the user asks or the evidence requires qualification.

## Default current-session report

```text
Session usage — <agent/provider; session label if safe>
Project: <verified remote / named logical project / unassigned>
Scope: <native session ID label or bounded explanation>
Time window: <known range / unknown>
Evidence cutoff: <last complete source record time and scope / unknown>

Tokens:
- Provider native total: ... [measured / unavailable]
- Input: ... [grade]; cache read: ... [grade]; output: ... [grade]
- Reasoning: ... [grade or unavailable]
- Derived total: ... [grade, only if justified]

Quota / credits: <native evidence or unavailable>   (separate)
Cost: <source-backed figure or unavailable>          (separate)

Method & coverage: <source type; missing parts; counter/estimate caveats>
```

Report identity as much as needed to understand the result, not by leaking raw private IDs or local paths.
For an active session, say “recorded through” the cutoff; do not imply that subsequent calls or the entire future Session are included. Repeated reports are comparable only when they use the same frozen source range and counter semantics.

## Default project report

Start with the verified Git remote or explicitly named logical-project key and the bounded discovery sources. Report selected versus distinct Session counts, matched providers, source cutoffs, attribution/fork method, deduplicated call or interval coverage, a verified measured/derived accessible subtotal, and separately estimated, unknown and unallocated segments. Include provider-aware per-session breakdown when practical. Explicitly disclose excluded, ambiguous, missing or inaccessible sessions/providers; do not call a partial subtotal the “project total.”

If no explicit evidence-backed total is possible, this is an acceptable completion:

```text
Verified accessible subtotal: X provider-reported tokens
Estimated segments: range Y–Z where defensible
Unknown or unallocated segments: 2 sessions / scope unresolved
Full-project total: unavailable
```

A project-level blended `X+Y` presentation is allowed only as an explicitly mixed-evidence **illustrative scoped estimate**, not as a verified all-in total. Mixed provider token sums retain a comparability warning.
When a single Session appears by direct selection and project discovery, show it once. If forked histories lack reliable call identity or comparable non-overlapping interval evidence, describe the overlap without inventing a net total. State whether `complete` means only the declared accessible scope; never imply unseen providers were inspected.

## Save/export behavior

- No explicit destination → output directly in Chat only. Do not create cleaned logs, manifests, report folders or hidden caches. After finishing, ask **once**: “需要将这份报告导出为 Markdown 文档吗？” (translate appropriately).
- Explicit location authorized → save only requested artifact(s) at that location if it is writable within the runtime's permissions; announce actual path only after creation.
- User subsequently requests export with no path → use normal artifact mechanism (if supported), not an invented repo or home-directory path.
- If file output is impossible, keep Chat answer complete and state the limitation; do not promise a nonexistent attachment.
- Do not automatically publish or commit private reports to Git.
