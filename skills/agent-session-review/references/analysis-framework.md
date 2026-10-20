# Evidence-Based Workflow Review

## Evidence discipline

Reconstruct the observed sequence before judging efficiency. A Session may show task definition, context inspection, planning, implementation, targeted checks, broad verification, debugging, correction, and closure, but do not force missing phases into the timeline. Separate observed actions from explanations and outcomes. Use `Directly Observed` for a source-visible event, `Strongly Supported` for a well-corroborated inference, and `Possible` for a plausible but unproven interpretation. Do not describe an agent's personality.

For important findings use **Evidence → Interpretation → Impact → Recommendation**. An impact such as extra time or tokens is only a hypothesis unless supported by timing or usage evidence. When evidence is too thin for one dimension, say `Insufficient Evidence` rather than inventing a score. Prefer specific upstream fixes over generic instructions to “be efficient.”

## Seven dimensions

| Dimension | Inspect | Boundary |
|---|---|---|
| Task Framing | Goal, non-goals, acceptance gate, permission boundaries, later scope corrections. | A changed user goal is not necessarily agent misunderstanding. |
| Context Efficiency | Targeted versus repeated unchanged file reads, rediscovery, background reloads, use of durable context. | Exploration can be necessary when facts are unknown or changed. |
| Execution Efficiency | Progress from understanding to useful action, batching, redundant tool/planning loops, in-scope autonomy. | Long work may be proportionate to complex tasks. |
| Interaction Overhead | Meaningful decisions versus avoidable “continue” prompts, repeated clarification, user-as-relay. | Do not criticize required approval or genuine user choices. |
| Verification Efficiency | Targeted tests, relevant regression, full-suite gates, repeated unchanged CI/test runs. | Reliability comes first; repeat verification may answer a new risk. |
| Rework & Failure | Reverted work, repeated known failures, corrective loops, cause and preventability. | Distinguish Necessary Discovery, Avoidable Misunderstanding, Avoidable Execution Error, Avoidable Verification Loop, Scope Change, and External/Environmental Failure. |
| Resource Efficiency | Reliable native token usage if present; repeated context/tool/test/runtime work; proportion to task outcome. | Missing counters are `unavailable`, not zero. More tokens alone do not prove waste; do not invent monetary or causal precision. |

## Comparison and prioritization

In project scope, first establish verified Session membership and the observable handoff/order. Compare purpose, task scale, constraints, evidence coverage, repeated behaviors, and whether later work reused prior context. A raw token or command-count ranking is not an efficiency ranking. If Sessions use different providers or tokenizers, describe native metrics separately and disclose comparability limits. Never sum copied history as new work without evidence of distinct execution.

Prioritize findings that are well supported, consequential, actionable, and likely to recur. Report what worked well. A previous review is a comparison baseline only if the user supplies it; use `Improved`, `Unchanged`, `Regressed`, `Newly Observed`, or `Not Comparable` where justified. A lower-token or shorter Session may simply have a smaller task. Candidate development principles remain proposals until explicitly approved.
