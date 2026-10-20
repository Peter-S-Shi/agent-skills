# Agent Skills

Private, curated collection of independently installable Agent Skills. The `skills/` directory is the default installation set; each child folder can be installed on its own.

| Active Skill | Purpose |
|---|---|
| [`agent-usage-accounting`](skills/agent-usage-accounting/SKILL.md) | Account for native agent usage within evidenced current-Session or project scope. |
| [`agent-session-review`](skills/agent-session-review/SKILL.md) | Review evidenced development workflows without requiring token counters or the accounting Skill. |
| [`portfolio-packaging`](skills/portfolio-packaging/SKILL.md) | Package a mature, post-release-candidate repository for portfolio presentation. |

Install only the desired folder from `skills/` into an agent's supported Skills location. Its linked references travel with that folder. No local agent installation, plugin, network service, or other Skill is required by this repository. The `portfolio-packaging` integration policy describes optional third-party capabilities; no third-party integration source is included.

[`legacy/codex-session-review`](legacy/codex-session-review/SKILL.md) preserves the earlier Codex-specific cleaner and report workflow. It is outside `skills/` and is **not** part of default discovery or installation. Select it explicitly only when that specialized legacy behavior is needed; it is not equivalent to the active `agent-session-review`.

See [PROVENANCE.md](PROVENANCE.md) for the exact source commits and redistribution boundary. This private collection has no repository-wide public redistribution license. Source repositories remain unchanged until an approved authority switch; copied packages must not be updated independently in two places.
