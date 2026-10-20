# M5 Authority and Publication Handoff

**Status: completed on 2026-10-20.** The unified `agent-skills` repository is Public with the Owner-approved MIT license; all three former source repositories have published migration notices. This is the completed authority-transfer record, not authorization to archive or delete those repositories or modify agent-local installations. Read [PROJECT_STATUS.md](PROJECT_STATUS.md) for current facts.

## Completed release and authority gates

1. **MIT license and Git history:** Owner approved MIT and retention of existing author metadata; publication-preparation [PR #2](https://github.com/Peter-S-Shi/agent-skills/pull/2) merged at `ffcc10c9dde021f2fd4f65a652f2f64d4c646784`. Both PR and merged-main Skills CI succeeded.
2. **Source equivalence:** the M5-P1 audit matched pinned source blobs except the disclosed semantically equivalent YAML description normalization for `portfolio-packaging`. Before handoff, each source's latest main matched its pinned source commit; the only subsequent differences are documented migration notices.
3. **Visibility and license:** GitHub repository metadata confirms `Peter-S-Shi/agent-skills` is Public, with the [MIT License](LICENSE) and the three active and one opt-in legacy `SKILL.md` paths present in the main repository tree. GitHub API checks confirmed paths; unauthenticated HTTP/browser checks were not independently available in this environment. The separate historical `agent-token-ledger` stays Private.
4. **Source README notices:** all three migration notices below were published to original repository main branches. Verified commits: `agent-token-ledger@232e0bd1c796f65a1b6370364d23ddf0abfaf78f`, `portfolio-packaging@a969adc60c0ddc27080a5fce93206b5a5cbf0efc`, and `codex-session-review@5fc15fda79f47e56f11e38f6f31e6ff59d37d922`. Only documentation changed.
5. **Canonical source switch:** effective after those notices, `agent-skills` is now the sole maintained update origin for all four included packages. Historical source repositories are retained as readable/reference copies, not independently updated packages.
6. **Not included:** no agent-local Skill installation, synchronization, repository archiving, deletion, or cleanup. Preserve `agent-token-ledger`'s `legacy-desktop-v0.2.0` tag and original Git history.

## Published source README notices

The following notices now appear near the top of their corresponding source READMEs. They are preserved here as exact handoff evidence, not pending instructions.

### `Peter-S-Shi/agent-token-ledger` (historical Private project)

> **Skills maintenance moved:** The authoritative updates for `agent-usage-accounting` and `agent-session-review` now live in [Peter-S-Shi/agent-skills](https://github.com/Peter-S-Shi/agent-skills/tree/main/skills). The copies here are historical snapshots, not separately maintained. This Private repository retains the former Agent Token Ledger application's Git history, M0–M4 migration evidence, and `legacy-desktop-v0.2.0` recovery tag.

### `Peter-S-Shi/portfolio-packaging` (public legacy entry point)

> **Maintenance moved:** The canonical `portfolio-packaging` Skill is maintained at [Peter-S-Shi/agent-skills](https://github.com/Peter-S-Shi/agent-skills/tree/main/skills/portfolio-packaging). Use that directory for new installations and updates. This repository is preserved as a historical source; any local optional third-party integrations remain outside the canonical package.

### `Peter-S-Shi/codex-session-review` (public specialist historical entry point)

> **Legacy package moved:** The original Codex-specific `codex-session-review` Skill and its cleaner are preserved at [Peter-S-Shi/agent-skills](https://github.com/Peter-S-Shi/agent-skills/tree/main/legacy/codex-session-review). It remains opt-in, is excluded from the default active Skills set, and is **not functionally equivalent** to the newer [`agent-session-review`](https://github.com/Peter-S-Shi/agent-skills/tree/main/skills/agent-session-review). This repository is retained as a historical source, not an independent update origin.

## Operational boundaries

No third-party local Skill directories are source-controlled here. `mimic-sync` may later distribute explicitly selected Skill folders after preview and owner approval; it does not decide provenance or delete obsolete target-only copies. Do not change Skill behavior, package the old desktop app, or introduce an auto-updater during the handoff.
