---
description: Diagnose DESIGN:OS Agent Teacher installation, plugin manifests, skill files, and local verification gates
allowed-tools: Bash, Read, Glob
---

# `design-os-pedagogy` `/doctor` Diagnostics

Run a read-only diagnostic check of the `design-os-pedagogy` installation and repository health. Do **not** modify, create, or delete any files during this check.

## Steps

1. **Run the deterministic self-check script** when inside a `design-os-pedagogy` checkout:
   ```bash
   python3 scripts/self_check.py
   ```
2. **Check installed skill locations** across active agent harnesses:
   - Claude Code: `~/.claude/skills/design-os-pedagogy/SKILL.md` or `.claude-plugin/marketplace.json`
   - OpenAI Codex: `~/.codex/skills/design-os-pedagogy/SKILL.md` or `.codex-plugin/plugin.json`
   - Gemini CLI / Antigravity: `~/.gemini/skills/design-os-pedagogy/SKILL.md`
   - Cross-agent `.agents`: `~/.agents/skills/design-os-pedagogy/SKILL.md`
3. **Report a concise health table** covering:
   - Manifest integrity (`.claude-plugin`, `.codex-plugin`, `.agents/plugins`, `.factory-plugin`)
   - Canonical skill (`skills/design-os-pedagogy/SKILL.md`)
   - Trust & privacy governance (`PRIVACY.md`, `SECURITY.md`, `LICENSE`)
   - Domain command readiness (`python3 scripts/self_check.py`)
