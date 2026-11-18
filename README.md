# Agentic Product Team

An Antigravity plugin that coordinates a reusable 20-role product and engineering team through staged delegation, artifact-based handoffs, and quality gates.

## What it does

The plugin adds one orchestration skill and twenty custom subagents. The skill turns a natural-language product request into a delivery brief, task ledger, dependency-aware agent waves, shared artifacts, verification gates, and a final launch-readiness report.

It does **not** blindly run all twenty agents on every prompt. It routes the smallest useful set for narrow work and uses the full team only when the request needs end-to-end discovery, design, implementation, assurance, and release coordination.

## Included roles

- **Strategy and planning:** Product Manager, Project Orchestrator, Business Analyst, Market Research.
- **Architecture and design:** System Architect, UI/UX Designer, Database Architect.
- **Core development:** Frontend Developer, Backend Developer, API Integration Engineer, Mobile Developer, AI/ML Engineer.
- **Quality, security, and operations:** Code Reviewer, QA & Test Automation, Security & Compliance, DevOps & CI/CD, Performance & Cost Optimizer.
- **Launch and support:** Technical Writer, Growth & Copywriting, Observability & Incident Triage.

## Install from GitHub

After cloning this repository, install it with the Antigravity CLI:

```bash
agy plugin install ./agentic-product-team
agy plugin list
```

For a workspace-local installation, place the plugin directory under `.agents/plugins/`. For a global installation, place it under `~/.gemini/config/plugins/`.

## Validate

```bash
agy plugin validate --strict .
```

The repository also validates each bundled skill's `SKILL.md` with the Manus skill validator:

```bash
python3 /home/ubuntu/skills/skill-creator/scripts/quick_validate.py --path skills/team-orchestrator
```

## Example prompts

- `Run the full 20-agent product delivery workflow for this repository.`
- `Plan and implement this feature with dependency-aware agent waves and review gates.`
- `Audit this project for launch readiness across product, quality, security, operations, and documentation.`

## Design notes

Subagents default to `model: inherit`, `commandExecutionPolicy: sandbox`, and `mainAgent: false`. The orchestrator remains in the primary session so that planning, integration, safety decisions, and final reporting have one accountable owner.

## License

MIT
