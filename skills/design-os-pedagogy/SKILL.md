---
name: design-os-pedagogy
description: "Use when working with DESIGN:OS Agent Teacher — Evidence-graded pedagogy library, cognitive-load curriculum tree runtime, and interactive mastery assessment engine for AI tutoring agents."
---

# DESIGN:OS Agent Teacher (`design-os-pedagogy`)

Equip AI agents to teach complex technical subjects using Bloom's revised taxonomy, worked-example fading, spaced retrieval, Socratic diagnostic probes, and verifiable learner state machines.

## When to Use

Activate this skill when the user asks to:
- `"Design a 5-stage mastery curriculum tree for distributed consensus (Raft) with prerequisite DAGs and diagnostic transfer questions."`
- `"Turn this codebase walkthrough into a worked-example fading sequence with interactive check-for-understanding probes."`
- `"Audit our onboarding tutorial for cognitive load violations, missing prerequisite links, and passive wall-of-text explanations."`

## Progressive Disclosure Routing (`What loads when`)

1. **Always Loaded**: `skills/design-os-pedagogy/SKILL.md` (this router — keeps context lean).
2. **On Demand — Prompt Recipes**: Load `docs/cookbook.md` when selecting multi-step workflows or copy-paste prompt templates.
3. **On Demand — Diagnostics**: Load `commands/doctor.md` or run `python3 scripts/self_check.py` when verifying installation or troubleshooting.
4. **On Demand — Ecosystem Discovery**: Load `llms.txt` when cross-referencing companion `DESIGN:OS` engines.

## Core Execution Workflow

1. **Inspect Context**: Read the target repository or workspace constraints before mutating files.
2. **Execute Deterministically**: Run `python3 scripts/self_check.py` or `python3 scripts/self_check.py` rather than guessing outputs freehand.
3. **Verify Quality Gates**: Run `python3 scripts/self_check.py` and confirm zero errors before reporting completion.

## Quality Bar & Anti-Scope

### It's working if...
- `python3 scripts/self_check.py` exits `0`.
- Outputs match the `DESIGN:OS` 2:1 axonometric B&W art direction and deterministic verification gates.
- Execution remains 100% local with zero external telemetry (`PRIVACY.md`).

### When NOT to use
- Pure reference API lookups where an experienced engineer just wants a one-line CLI flag answer.
- Clinical, medical, or accredited K-12 compliance grading requiring licensed human oversight.
- Automated code generation where the user wants the task finished rather than explained.
