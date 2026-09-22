# Xscriptor Skills

Knowledge layer for [OpenCode](https://opencode.ai) and [Claude Code](https://docs.anthropic.com/en/docs/claude-code/overview): full-stack project skills, content systems, and senior reference packs.

## Contents

| Directory | Contents | Items | How it is consumed |
|---|---|---|---|
| `web-fullstack/` | Full-stack web project skills by archetype: `portfolio/xscriptor`, `devtools/devx`, `platform/samurai` | 3 | Loaded on demand by the native `skill` tool |
| `content/` | Content systems: `linkedin` (post copies, hashtags, cadence, image generator) | 1 | Loaded on demand by the native `skill` tool |
| `senior/` | Exhaustive per-domain reference packs (language, platform, practice) | 18 | Loaded on demand by agents or the orchestrator; optional via a stable port |

```
skills/
  web-fullstack/
    portfolio/xscriptor/     SKILL.md + references/
    devtools/devx/           SKILL.md + README.md + references/
    platform/samurai/        SKILL.md + references/
  content/
    linkedin/                SKILL.md + README.md + references/ + scripts/
  senior/
    <pack>/                  SKILL.md + references/   (18 packs)
    README.md                contract, port spec, registry
```

## Senior Reference Packs

Every pack under `senior/` is a standard skill that exposes a stable, optional port:

- **Port declared in frontmatter** — `metadata` carries `port`, `port-version`, `kind`, `domain`, `consumers`, `optional`, `entrypoint`, and `stability`.
- **Three load modes** — installed agent (`skill({ name: "<pack>" })`), orchestrator (reads `SKILL.md` and only the references the task needs), and degraded mode when the pack is not installed.
- **Single source of truth** — the contract, authoring rules, and registry live in [`senior/README.md`](./senior/README.md).

Consumers are listed per pack in the registry; packs never assume they are installed.

## Installation

The installer, the agent registry, and the npm packages live in the companion repos:

- [xscriptor-ai/scripts](https://github.com/xscriptor-ai/scripts) — `install-agents.sh` for OpenCode (agents, skills, commands)
- [xscriptor-ai/packages](https://github.com/xscriptor-ai/packages) — `npx @xscriptor/ai-agents` (OpenCode and Claude Code)
- [xscriptor-ai/agents](https://github.com/xscriptor-ai/agents) — agent definitions and Claude Code mirror

## Related

- [xscriptor-ai/agents](https://github.com/xscriptor-ai/agents) — specialized and senior agents
- [xscriptor-ai/environments](https://github.com/xscriptor-ai/environments) — per-desktop environment packs
- [xscriptor-ai/research](https://github.com/xscriptor-ai/research) — research space for AI mechanisms

## License

MIT
