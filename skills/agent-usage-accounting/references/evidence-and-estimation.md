# Evidence Decision Tree and Estimation Protocol

**M0 draft.** A disciplined *attempt* at estimation is valuable; claiming precise provider usage without the necessary telemetry is not.

## 1. Begin with capabilities, not vendor assumptions

Determine what the running agent can access and explain the basis: native per-call accounting, provider aggregate, current execution runtime, documented local session log, supplied export/report, or no evidence. A Skill instruction grants no permission to access private paths, another provider's internal session store, cloud quotas, or hidden reasoning. Use only actually permitted tools and evidence. Do not promise that the whole computer can be searched or that each provider exposes the same log schema.

If supplied usage counters and local transcript content disagree, first determine whether they measure the same request set, time range and metric semantics. Do not assume the transcript is a more accurate account merely because it is longer.

## 2. Decision tree (apply per source / metric / interval)

```text
Is trustworthy provider-native per-call usage exposed?
  YES → identify unique real calls, validate semantics/scope → MEASURED
  NO  ↓
Are trustworthy cumulative counters/aggregates exposed?
  YES → validate scope and counter epochs; use latest session total
         or derive attributable deltas within comparable intervals →
         MEASURED observation + DERIVED intervals, qualified coverage
  NO  ↓
Do complete enough logged turns exist to reconstruct requests?
  YES → identify the exact model/tokenizer, known messages, context and
         tools within each real call, plus missing invisible inputs →
         can actual consumption be estimated with defensible assumptions?
           YES → ESTIMATED, with explicit method, range and omissions
           NO  → visible-content token count only (not consumption)
  NO  ↓
Can a narrowly evidenced bounded estimate be justified independently?
  YES → ESTIMATED, with explicit assumptions and defensible range
  NO  → UNAVAILABLE
```

This is a **coverage-aware tree**, not a simple ranking: native totals might cover fewer calls than a broader but poorly specified log. Preserve both and identify disjoint, overlapping and unknown regions before combining anything.

## 3. Reconstructing tokenless session logs

Do not equate the number of characters or tokens in a single final transcript with the number of tokens actually processed across a sequence of requests. A transcript commonly collapses repeated context into one copy and can omit tools, system/developer instructions, attachments, retrieval, caching, hidden reasoning, compaction, and dropped/truncated turns.

A useful, bounded method for a tokenless provider where adequate source evidence exists:

1. **Inventory observed calls.** Identify real request/response boundaries and any stable IDs. Count completed/partial turns and model/effort changes; be explicit if boundaries are ambiguous.
2. **Identify tokenizer.** Prefer the actual model's tokenizer or documented equivalent; if unavailable, do not pretend a generic character ratio is model-exact. A fallback approximation must be labeled heuristic.
3. **Reconstruct visible input per call.** Include only messages/context/tool schemas actually known to have been sent on that call. If input replay, context clipping or tool injections cannot be resolved, mark this uncertainty; avoid multiplying the full final transcript by number of turns.
4. **Reconstruct visible output per call.** Count known emitted messages and tool instructions using tokenizer where possible; state whether thinking/reasoning or omitted outputs are unobservable.
5. **Determine coverage.** For each call classify `complete visible`, `partial visible`, or `unknown`; never describe hidden provider inputs as observed.
6. **Calibrate only if supplied trustworthy paired usage.** On comparable provider/model/harness/config/call types, measure estimation error; validation examples must be independent from calibrating examples. No fabricated “±5%” band.
7. **Form a range only when justified.** Provide a method, component assumptions and an evidence-backed interval. Distinguish a range of modeled scenarios from a validated prediction or error interval; calibration examples alone do not prove a hard upper or lower bound. If no defensible bound exists, show a visible-content quantity with clear caveats (even a strict lower bound is unsafe when model transformations/omissions are unknown), or decline to estimate total consumption.
8. **Keep quota/currency separate.** A token estimate is not a subscription allowance estimate and cannot be used to invent account spend.

**Mandatory distinctions:**

- **Measured native usage:** originates from a defined provider/runtime counter over a known scope.
- **Derived usage:** arithmetic over trustworthy native usage facts (e.g. a validated delta). Never label a tokenizer guess `derived`.
- **Estimated usage:** a numerical prediction involving unobserved consumption. State assumptions and accuracy limits; only emit if justified.
- **Visible content volume:** tokens of content present in the log; *not* a proxy for all requests without a validated reconstruction.
- **Unavailable usage:** when source evidence or model semantics do not support a defensible result.

## 4. Minimum reporting fields for an estimate

```text
metric + unit
point value or range (if defensible)
evidence grade = estimated
source type / visibility
observed call boundaries and coverage
model/tokenizer assumption
input context-reconstruction assumption
omitted system/tool/hidden/compaction/cache details
calibration evidence, if any (otherwise "not calibrated")
material error/uncertainty statement, including whether any stated range is a scenario range or a validated error interval
```

When estimation cannot be justified, report `unavailable` for actual usage, and optionally show **visible text token volume** with a separate explicit label if that information is useful and supported by a known tokenizer.

## 5. AG-like tokenless-log example (illustrative)

Suppose the accessible log contains user prompts, assistant visible answers and tool activities but no token counters, no full prompt assembly, and no stable evidence about compaction or cached prefixes.

Correct answer: “Native usage: unavailable. Visible content volume: X tokens under tokenizer Y, if Y is known. Total session input tokens: not recoverable to measured precision; absent request-level context assembly, an all-in numeric estimate is not justified by this source.”

If separate known requests and sent-message payloads **are** actually logged and tokenized, a qualified estimate may be appropriate. The Skill should explain exactly which unobserved pieces could increase or change it.

**Never invent precision in order to satisfy a user request for an exact number.**

## 6. Common failure patterns

- Adding all `total_token_usage` snapshots → double counting.
- Adding `cache_read` on top of native input already inclusive of cache → double counting.
- Adding `reasoning_tokens` to output that already includes them → double counting.
- Summing a native session aggregate with its constituent per-call counters → double counting.
- Counting final visible transcript once and calling it accumulated input/output → under/over-counting with unknown direction.
- Multiplying prompt size by turn count without actual context assembly evidence → invented estimates.
- Reusing a calibration factor from a different model/provider/harness without validation → unsupported error band.
- Treating quota percentage as a token count → unit/category error.
- Assuming unseen sessions or providers have zero usage → false complete coverage.
