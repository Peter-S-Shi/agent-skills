# M5-P1 Source Provenance

This collection copies only tracked, self-authored source files from the pinned commits below. Git histories were not imported. Each package retains its own relative references; the legacy package is outside the default `skills/` set.

| Destination | Authoritative source at migration | Pinned commit | Copied scope |
|---|---|---|---|
| `skills/agent-usage-accounting/` | [`Peter-S-Shi/agent-token-ledger`](https://github.com/Peter-S-Shi/agent-token-ledger) `skills/agent-usage-accounting/` | `3f0ce199ebfc73a7944d9f8a32cf1976afd5b8c5` | `SKILL.md` and four `references/` files |
| `skills/agent-session-review/` | [`Peter-S-Shi/agent-token-ledger`](https://github.com/Peter-S-Shi/agent-token-ledger) `skills/agent-session-review/` | `3f0ce199ebfc73a7944d9f8a32cf1976afd5b8c5` | `SKILL.md` and two `references/` files |
| `skills/portfolio-packaging/` | [`Peter-S-Shi/portfolio-packaging`](https://github.com/Peter-S-Shi/portfolio-packaging) | `9350ad78103c984805dcfb533fab5a2094fc7b3c` | `SKILL.md`, three `references/` files, `integrations/README.md`, and `integrations/.gitignore` |
| `legacy/codex-session-review/` | [`Peter-S-Shi/codex-session-review`](https://github.com/Peter-S-Shi/codex-session-review) | `b7c1ca32e331a424f638cea646c4395d77d154a3` | All seven tracked files; no Git metadata |
| `tools/validate_skills.py` | [`Peter-S-Shi/agent-token-ledger`](https://github.com/Peter-S-Shi/agent-token-ledger) `tools/validate_skills.py` | `3f0ce199ebfc73a7944d9f8a32cf1976afd5b8c5` | One standard-library validator |

The `portfolio-packaging/SKILL.md` description was reformatted as an equivalent YAML folded scalar so strict Skill validators can parse the source's unquoted colon; its instructions and other files were not changed. Its optional installed third-party integration was not copied. No provider Session records, local installation paths, generated outputs, or source repository history are included. The pinned source commits document historical origin, not ongoing update authority. See [PROJECT_STATUS.md](PROJECT_STATUS.md) for the maintenance-authority boundary. Public redistribution requires appropriate rights and explicit repository licensing; no locally installed third-party integration source is included.
