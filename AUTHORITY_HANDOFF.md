# M5 Authority and Publication Handoff

This is a cutover procedure, **not** a declaration that publication, repository retirement, or authority transfer has already occurred. Read [PROJECT_STATUS.md](PROJECT_STATUS.md) alongside GitHub's actual repository visibility, checks, and source READMEs.

## Release and authority gates

1. Merge the MIT/publication-preparation PR only after reviewing its precise diff, source rights, privacy-sensitive contents, Git commit metadata, and green PR CI. Verify the merge commit and the main-push CI.
2. Confirm the package content still matches the pinned sources in [PROVENANCE.md](PROVENANCE.md) (apart from the documented portfolio frontmatter normalization). If any old source advanced, review the delta before cutover; never silently overwrite either version.
3. Before changing visibility, re-check the **entire public Git history**, not only the working tree. Owner has accepted retention of the present author-email metadata. Confirm no other unapproved confidential source, secrets, or private Session data would become public.
4. Only after the release gate passes, change `Peter-S-Shi/agent-skills` from Private to Public and verify anonymous access to all three active `SKILL.md` files, the opt-in legacy package, and [LICENSE](LICENSE). Keep the original historical `agent-token-ledger` Private.
5. Publish the source-repository README migration notices below, scoped to documentation only. Verify all notices link to the now-public canonical repository and that no source Skill is being edited in parallel.
6. **Only then declare update-authority cutover complete.** Future changes to the four packages belong in `agent-skills`; source repositories remain discoverable historical snapshots. Local installed copies do not update themselves; follow a separate approved installation/cleanup pilot.
7. Repository archiving, deletion, and local Skill removal are independently gated decisions, not part of this publication handoff. Preserve `agent-token-ledger`'s `legacy-desktop-v0.2.0` recovery tag and history.

## Ready-to-publish source README notices

Insert these at the top of each source README **when the new repository is public and the switch is approved**, not before.

### `Peter-S-Shi/agent-token-ledger` (historical Private project)

> **Skills maintenance moved:** The authoritative updates for `agent-usage-accounting` and `agent-session-review` now live in [Peter-S-Shi/agent-skills](https://github.com/Peter-S-Shi/agent-skills/tree/main/skills). The copies here are historical snapshots, not separately maintained. This Private repository retains the former Agent Token Ledger application's Git history, M0–M4 migration evidence, and `legacy-desktop-v0.2.0` recovery tag.

### `Peter-S-Shi/portfolio-packaging` (public legacy entry point)

> **Maintenance moved:** The canonical `portfolio-packaging` Skill is maintained at [Peter-S-Shi/agent-skills](https://github.com/Peter-S-Shi/agent-skills/tree/main/skills/portfolio-packaging). Use that directory for new installations and updates. This repository is preserved as a historical source; any local optional third-party integrations remain outside the canonical package.

### `Peter-S-Shi/codex-session-review` (public specialist historical entry point)

> **Legacy package moved:** The original Codex-specific `codex-session-review` Skill and its cleaner are preserved at [Peter-S-Shi/agent-skills](https://github.com/Peter-S-Shi/agent-skills/tree/main/legacy/codex-session-review). It remains opt-in, is excluded from the default active Skills set, and is **not functionally equivalent** to the newer [`agent-session-review`](https://github.com/Peter-S-Shi/agent-skills/tree/main/skills/agent-session-review). This repository is retained as a historical source, not an independent update origin.

## Operational boundaries

No third-party local Skill directories are source-controlled here. `mimic-sync` may later distribute explicitly selected Skill folders after preview and owner approval; it does not decide provenance or delete obsolete target-only copies. Do not change Skill behavior, package the old desktop app, or introduce an auto-updater during the handoff.
