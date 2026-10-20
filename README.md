# Agent Skills

A curated collection of independently installable Agent Skills. The `skills/` directory is the default installation set; each child folder can be installed on its own.

| Active Skill | Purpose |
|---|---|
| [`agent-usage-accounting`](skills/agent-usage-accounting/SKILL.md) | Account for native agent usage within evidenced current-Session or project scope. |
| [`agent-session-review`](skills/agent-session-review/SKILL.md) | Review evidenced development workflows without requiring token counters or the accounting Skill. |
| [`portfolio-packaging`](skills/portfolio-packaging/SKILL.md) | Package a mature, post-release-candidate repository for portfolio presentation. |

Install only the desired folder from `skills/` into an agent's supported Skills location. Its linked references travel with that folder. No local agent installation, plugin, network service, or other Skill is required by this repository. The `portfolio-packaging` integration policy describes optional third-party capabilities; no third-party integration source is included.

[`legacy/codex-session-review`](legacy/codex-session-review/SKILL.md) preserves the earlier Codex-specific cleaner and report workflow. It is outside `skills/` and is **not** part of default discovery or installation. Select it explicitly only when that specialized legacy behavior is needed; it is not equivalent to the active `agent-session-review`.

## Accounting scope and possible API extension

[`agent-usage-accounting`](skills/agent-usage-accounting/SKILL.md) accounts for usage only within the scope of trustworthy, accessible native session records or counters. Current evidence is bounded: full cross-session, cross-provider, and project-level coverage is not guaranteed, and missing usage must be reported as unavailable rather than invented.

**Paid API usage and billing:** This release has no implemented and validated provider-API billing/accounting integration. It is **not** an API cost tracker. A future provider-specific extension may account for actual paid API calls, usage, and billed amounts, but only after real API usage/billing evidence, appropriate access, and a funded test budget are available for independent verification. That work is deferred; no API purchase or key is required for the currently released Skills.

## License and maintenance

This collection is released under the [MIT License](LICENSE). It contains the Owner's selected Skill sources, not third-party integration packages. Optional third-party integrations retain their own upstream terms.

**Canonical maintenance source:** This public repository is the authoritative update source for all three active Skills and the opt-in historical Codex-specific package. The original source repositories are frozen historical snapshots; their README notices link here. New installations and updates should come from the respective directories in this repository. See [PROVENANCE.md](PROVENANCE.md) for historical source commits, [PROJECT_STATUS.md](PROJECT_STATUS.md) for the current status, and [AUTHORITY_HANDOFF.md](AUTHORITY_HANDOFF.md) for the completed handoff evidence.
