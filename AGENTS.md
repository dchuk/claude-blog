# Claude Blog cross-platform instructions

This repository supports both Claude Code and OpenAI Codex. Follow the development,
security, testing, and content rules in `CLAUDE.md`.

Shared workflows live under `plugins/claude-blog/skills/`; the root `skills`
path is a compatibility link. Claude Code loads the existing `.claude-plugin`
manifest; Codex loads `plugins/claude-blog/.codex-plugin/plugin.json`. Do not
fork the skill implementations by client.

When agent definitions change, run:

```bash
python3 scripts/install_codex_agents.py --check
python3 -m unittest tests/test_codex_agents.py
```

Claude agent Markdown remains canonical. The installer generates project-scoped
Codex TOML agents without changing the source prompts.
