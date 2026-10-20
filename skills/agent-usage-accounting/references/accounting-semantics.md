# Accounting Semantics and Reconciliation

**M0 draft — domain rules, not provider-specific parser instructions.** Apply provider-native definitions first; generic labels must never silently override documented semantics.

## 1. Reporting domains

**Token processing volume** is not interchangeable with **subscription quota/credits** or **currency**. Report each only with native evidence or explicitly authorized, well-founded conversions. A percent-of-weekly-plan remaining is not a token counter. Monetary cost requires actual billable units, pricing context and relevant cache/model rules; do not calculate it as an automatic extra.

## 2. Canonical token concepts (do not presume availability)

| Concept | Interpretation | Non-additivity risk |
|---|---|---|
| `fresh_input_tokens` | Input not served from an existing cache, if inferable | Often `input - cache_read` when cache read is included in native input |
| `cache_read_tokens` | Input reused from cache when reported | May already be included in native `input_tokens` |
| `cache_write_tokens` | Cache creation/write when exposed | May overlap provider input or represent a separate billing classification |
| `output_tokens` | Model output when reported | May already include reasoning output |
| `reasoning_output_tokens` | Separately exposed internal reasoning output usage | Nullable; generally a subset, **not** an extra addition |
| `reported_total_tokens` | Provider-defined native total | Its components may use different semantics |
| `derived_total_tokens` | Arithmetic total from components whose partition is proven | Never silently replace native total with it |

Do not invent `0` for missing cache, reasoning, or system-input fields. A documented zero is a real zero; missing is unavailable.

## 3. Additive totals only after semantics verification

If native `input_tokens` includes cache reads and output is disjoint, a defensible component total may be `input_tokens + output_tokens`. If native input excludes cache reads or separately accounts for cache writes, the formula may differ. **Never use a universal formula without confirming the provider field meanings.** Preserve any mismatch between native total and component-derived total with a reconciliation note, instead of silently choosing one.

For aggregated fields, only sum mutually disjoint event/call IDs or delta intervals, and only across compatible units. Different provider/model tokenizers and visibility boundaries require a warning even when a numeric total is displayed.

If one source exposes both a session-lifetime cumulative counter and a shorter turn/current-run counter, first establish each counter's scope and epoch. The shorter counter is not an addition to the lifetime snapshot merely because its record is newer. Only a proven non-overlapping interval may be added, with the resulting cutoff stated. Otherwise use the latest valid session-scope snapshot and mark any later usage outside that cutoff as unmeasured.

## 4. Cumulative snapshots versus attributable deltas

A provider may emit repeated observations of the same session-to-date cumulative count, not independent calls:

```text
snapshot at t1 = 10,000
snapshot at t2 = 16,000
snapshot at t3 = 16,000
```

- **Latest valid cumulative snapshot:** 16,000 (as defined by that counter contract).
- **Observed interval deltas:** t1→t2 = 6,000; t2→t3 = 0.
- **Never:** 10,000 + 16,000 + 16,000 = 42,000.
- **Never:** equate sum of interval deltas (6,000) with the entire session's 16,000; the initial 10,000 is a baseline, not a time-local delta.

The first counter snapshot in each *epoch* is a baseline without a time-attributable delta. When a required comparable field regresses, create a new conceptual epoch; do not clamp a negative delta to zero, bridge the regression, or simply add full epoch snapshots unless independent evidence proves no overlap and complete coverage.

Example:

```text
epoch 0: 10,000 → 16,000  (observed delta 6,000)
epoch 1:  3,000 →  8,000  (observed delta 5,000)
```

There are 11,000 **observed positive deltas between snapshots**. That is *not* proof the session's total usage was 11,000, 24,000, or any other exact value. Report 8,000 as the latest snapshot of **epoch 1**, with its reset caveat and any attributable interval coverage separately. Do not label it a lifetime or whole-session total. The total over all epochs is unavailable unless source semantics establish it.

## 5. Identity and reconciliation

- An independent provider request/response event is the ideal atomic unit for summing true usage.
- Repeated references, duplicate file copies, overlapping selections and forked historical prefixes are *not* new calls.
- Model attribution is metadata about usage, not extra usage. Unknown model labels remain unknown; do not assign them retroactively from later model metadata.
- If a call has complete native usage and there is a noisy aggregate, avoid summing both. Use native aggregate as a reconciliation check; report gaps or mismatches.
- If one source covers all calls and another source covers some overlapping calls, do not treat the second source as additive unless independent non-overlap is demonstrated.
- Report **token-source coverage** independently from **model-attribution coverage**; model unknown does not necessarily make token usage unknown.

## 6. Quality classes

A report may state `complete`, `partial`, `unsupported`, `corrupted`, `deferred`, or `malformed` for the relevant observed evidence as appropriate. Use `complete` only within declared accessible input boundaries; partial or broken source visibility must lower the relevant coverage. Qualitative coverage must coexist with per-metric evidence grade (`measured`, `derived`, `estimated`, `unavailable`).

A combined “total” mixing exact and estimated observations must **not** be presented as a measured number. Show confirmed subtotal, estimated segments/ranges, unknown segments, and the conditions under which an all-in total could be computed.

## 7. Required cross-provider notice

If several provider-native token sources are combined: “This is heterogeneous reported token processing volume. Tokenizers, cache accounting, model semantics and subscription allowance conversion may differ. It is not a common billable cost or credit total.”
