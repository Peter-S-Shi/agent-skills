# Project Status

M5-P1 content consolidation is complete: three active independently installable Skills live under `skills/`, and the Codex-specific historical package remains under `legacy/`, outside default installation.

M5-P2 publication preparation includes an Owner-approved MIT license, public-facing documentation, and a controlled authority-handoff procedure. The Owner approved retaining the current Git history and its author metadata and intends to publish this collection. **Document preparation or merging its PR does not itself publish the repository or transfer maintenance authority.**

- **Maintenance authority before cutover:** `agent-token-ledger` remains the source for `agent-usage-accounting` and `agent-session-review`; `portfolio-packaging` remains the source for its Skill; `codex-session-review` remains the source for its legacy package.
- **Planned authority after cutover:** `Peter-S-Shi/agent-skills` is the sole update origin for all four included packages. Historical source repositories become read-only references after their migration notices are published.
- **License:** selected self-authored materials in this collection use [MIT](LICENSE); no optional third-party integration source has been imported.
- **Testing and evidence:** M5-P1 validated independent Skill structure/references, isolated copies, legacy script syntax/version/synthetic discovery, provenance, and privacy boundaries. CI checks pull requests and main pushes; these checks do not establish full live multi-Session or complete legacy-cleaner behavior. Verify each PR/main run by its actual GitHub check status, not this record.
- **Installation and distribution:** no installed agent Skill directories were changed by consolidation or publication preparation. Optional `mimic-sync` distribution and legacy opt-in installation need separate rollout decisions.

See [AUTHORITY_HANDOFF.md](AUTHORITY_HANDOFF.md) for the publication gate, cutover sequence, and exact source-repository migration notices. Public visibility, maintenance cutover, and archiving are distinct actions, not consequences of an ordinary documentation merge.
