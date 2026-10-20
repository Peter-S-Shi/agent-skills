# Project Status

## Current phase

**M5-P2 public publication and maintenance-authority cutover: complete (2026-10-20).** `Peter-S-Shi/agent-skills` is **Public** and is now the sole update authority for the included self-authored Skills. The collection is distributed under the [MIT License](LICENSE).

## Maintained packages

- **Default active Skills:** `agent-usage-accounting`, `agent-session-review`, and `portfolio-packaging` under `skills/`; each is independently installable.
- **Opt-in legacy package:** `legacy/codex-session-review` preserves the Codex-specific workflow, cleaner, and references. It is excluded from default installation and is not functionally equivalent to `agent-session-review`.
- **Historical provenance:** source content and pinned original commits are recorded in [PROVENANCE.md](PROVENANCE.md). The historical source repositories are no longer independent update authorities.

## Completed source handoff

- `Peter-S-Shi/agent-token-ledger` remains **Private**; its `README.md` and `PROJECT_STATUS.md` point to this repository. Its M0–M4 history and `legacy-desktop-v0.2.0` recovery tag remain intact. Handoff commit: `232e0bd1c796f65a1b6370364d23ddf0abfaf78f`.
- `Peter-S-Shi/portfolio-packaging` remains **Public** as a historical entry point. Its README directs updates to this repository. Handoff commit: `a969adc60c0ddc27080a5fce93206b5a5cbf0efc`.
- `Peter-S-Shi/codex-session-review` remains **Public** as a historical Codex-specific entry point. Its README directs opt-in legacy use here. Handoff commit: `5fc15fda79f47e56f11e38f6f31e6ff59d37d922`.
- These notices changed documentation only. None of the source Skill implementations was modified, and all three historical source repositories are now archived (without changes to their visibility), and none was deleted.

## Verification and open boundaries

M5-P1 validated active Skill structure and references, isolated package copies, and the legacy cleaner's syntax/version and synthetic discovery. PR #1 and PR #2, plus their merged `main` pushes, passed the repository's Skills CI. Those checks do **not** establish universal provider support, complete live multi-Session coverage, or full legacy cleaning behavior. Repository Public visibility and canonical files were verified using GitHub's repository/file APIs; anonymous browser access was not independently tested in this environment.

Dedicated provider paid-API usage and billing integration has not been implemented or validated. It remains deferred until funded real API usage and billing tests are available; no budget-dependent API work is part of the current release.

No agent-local Skill installation directories were changed by this release; future installation/cleanup and optional `mimic-sync` distribution require a separate user-approved rollout. Archived historical repositories remain preserved; deletion requires a separate Owner decision. See [AUTHORITY_HANDOFF.md](AUTHORITY_HANDOFF.md) for the completed release gate and preserved migration notices.
