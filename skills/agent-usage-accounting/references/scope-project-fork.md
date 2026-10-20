# Session Scope, Project Attribution, and Fork-Safe Rollups

**M2 project procedure — provider-neutral identity logic.** Do not assume that branching in any particular chat product maps directly to a unique log structure in Codex, Claude Code, AG or future agents. Apply this only to evidence the executing agent is authorized to access; no persistent inventory is required.

## 1. Select the accounting population

- `current-session` means the executing agent's actual current session, **if identifiable**. Do not silently switch to "all messages currently visible" when the runtime session encompasses a different set of requests.
- `project` means all **discoverable and accessible** session/call evidence satisfying a resolved repository or explicit logical-project association. A single agent may be unable to inspect every provider's private logs; name the boundary.
- Project may be selected by normalized Git remote (owner/repo or canonical URL, taking multiple remotes into account) or by an explicitly named logical project when no remote exists. Git worktree path and branch name are hints, not separate project identities.
- Repositories can be renamed/transferred or use multiple remotes. Resolve conflicts from actual metadata or ask; do not silently merge unrelated repos based only on similar folder names.

### On-demand discovery and project key

1. Resolve the requested key before broadening discovery. For a Git project, inspect the actual repository/remotes and use a verified host plus repository identity; normalize transport spelling (for example, equivalent HTTPS/SSH forms) only when that host's rules establish equivalence. Preserve host-specific case, alias, rename and fork distinctions when unverified. `origin` is a convention, not an authority when several remotes conflict.
2. A Git worktree is another checkout of a repository, not another project. Verify its common repository or equivalent canonical remote; do not assume same display folder name proves identity. Conversely, two similar names with different verified remotes remain separate until the user resolves them.
3. For a user-named logical project without a remote, use explicit Session selections or trustworthy native project membership. A title or path substring may identify candidates for inspection but cannot by itself prove membership.
4. Query only native indexes/log locations or supplied evidence actually permitted in this runtime. Freeze the discovery population and each live source's evidence cutoff for this report. Describe which providers/locations were inspected, inaccessible, or not attempted. This is an on-demand, in-memory working set, not a background scan or a stored Session receipt.

## 2. Attribution strength

Prefer, in order: call-level project/workspace evidence; session-level authoritative project assignment; verified working-directory/Git remote metadata at relevant time; other consistent contextual evidence; explicit user selection. A guessed project from a conversation title is not strong enough for unqualified accounting.

If a session touches projects A and B and its calls cannot be separated reliably, report unallocated/ambiguous usage rather than counting the entire session once in A and once in B. If one user-created logical project intentionally encompasses several repositories, record that scope explicitly.

Assign a whole-session native total to one project only if the evidence covers the same counter window and establishes that the **entire** window belongs to that project. Otherwise use proven call-level or disjoint interval usage and leave the remainder unallocated. A current working directory, one Git command or the Session's title does not retroactively assign earlier calls. A user's explicit inclusion resolves intended selection, but does not by itself make overlapping counters additive or reveal unknown per-call allocation.

## 3. Identity keys and deduplication

Prefer actual provider-qualified immutable request IDs (or trustworthy equivalent) to identify a real model call. Include provider, environment/account partition when necessary to prevent accidental collisions, and verified session identity. A session display name, file name, prompt text or equal token quantity is never sufficient alone.

First deduplicate repeated **Session selections** by verified provider-qualified Session ID, regardless of whether the user supplied it directly or it came from project discovery. Then reconcile usage within and across selected Sessions. Never add a per-Session aggregate to its constituent call records. Keep a temporary set of proven call identities or non-overlapping counter intervals for the one report; discard it after the Chat answer unless the user explicitly requests an export.

If several accessible records are copies or snapshots of that same Session, verify their counter scope and epoch before reconciliation. For comparable, monotonic cumulative snapshots, use the latest complete snapshot through the declared cutoff once; earlier copies are not additions. A later record with a shorter counter scope does not supersede a session-lifetime snapshot. If copies disagree at the same cutoff, have incompatible epochs, or cannot be ordered reliably, report the conflict and leave the affected total unavailable rather than choosing a convenient copy or summing them.

Where no immutable call ID exists, equivalent source records can only be deduplicated when the evidence establishes they are the same historical call (e.g. stable native reference/lineage, copied source with a validated identical event locus). Do **not** globally hash message text and de-duplicate that: two identical new API/model requests are separately billable/processable calls.

A provider session aggregate can only be combined with other aggregates where their scope/counter provenance establishes disjoint calls. A record may overlap another record fully or partially. If overlap cannot be resolved, use qualified partial figures; do not choose an arbitrary arithmetic subtraction.

When different providers expose distinct token units or cache conventions, report provider breakdowns and label any numeric sum heterogeneous processing volume, not shared credits/cost. An inaccessible provider contributes an **unknown** segment, never zero. A measured accessible subtotal may coexist with an unavailable full-project total.

## 4. Fork scenarios

Conceptual call graph:

```text
Shared historical requests: A → B
                               ├─ parent continuation: C
                               └─ branch continuation: D → E
```

For one verified project, all unique calls contribute: `A+B+C+D+E` **once each**. If separate logs both replay A and B as history without executing them anew, those inherited copies contribute zero extra usage. If branch D itself submits a request containing A/B context, the *new request's actual provider usage* is additional even though text repeats.

Rules:

1. Identify the fork boundary and inherited events only if provider records/verified metadata support it.
2. Treat copying history and executing a new model request as distinct operations.
3. Nested forks follow the same event-identity rule; no need for a special global lineage DB.
4. If stable call IDs are absent, a verified fork boundary plus comparable counter epochs and exact fork baseline may still support non-overlapping post-fork deltas. Without that evidence, mark overlapping portions unknown; do not sum entire parent/child totals as though independent.
5. Chat UI branches, Git branches and worktrees are different concepts. A Git branch does not prove chat-session fork lineage and vice versa.

## 5. Boundary disclosure

State at least:

```text
requested scope and project key
sources/providers the execution runtime could inspect
matched distinct sessions/calls (bounded list or counts)
known excluded/nonmatching candidates
ambiguous/unreadable/missing sources
fork/duplicate resolution method
unallocated cross-project work
confidence/coverage of combined result
```

Never claim “total for the entire project across all AI agents” unless source scope and completeness genuinely support it. A smaller, defensible “verified locally accessible subtotal” is preferable.
