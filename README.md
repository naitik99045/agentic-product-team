# Agentic Product Team

An Antigravity plugin that coordinates a reusable 20-role product and engineering team through staged delegation, role-specific guardrails, evidence-based handoffs, and quality gates.

## Important: you choose the team size

This plugin does **not** require all 20 agents for every task. You can invoke 2, 3, 4, or 5 named agents. Put the exact roster in your prompt and the orchestrator must honor it.

Example:

```text
Use only these 5 agents from the agentic-product-team plugin:
product-manager, system-architect, backend-developer, qa-test-automation, security-compliance.
Do not invoke any other subagents. Add a shared plan, work in dependency order,
run the requested tests, and report missing coverage.
Task: add passwordless email login to the existing application.
```

To ask for a recommendation first:

```text
Recommend no more than 5 agents from the agentic-product-team plugin for this task.
Explain why each is needed and wait for my approval before dispatching them.
Task: <describe your task>
```

## What was improved

Every agent now has a role-specific mission, preflight checklist, workflow, guardrails, evidence standard, and fixed response format. The orchestrator also enforces hard roster limits, warns about missing security or test coverage, prevents overlapping edits, and distinguishes proposed, implemented, verified, blocked, and deferred work.

These instructions improve reliability, but they do not retrain Antigravity's underlying model or guarantee error-free software. The agent still needs clear requirements, repository access, suitable tools, and human approval for important product, security, and production decisions.

## Exact agent names and responsibilities

All agents below belong to the `agentic-product-team` plugin:

- `product-manager` — product vision, MVP scope, priorities, user stories, acceptance criteria.
- `project-orchestrator` — task breakdown, dependencies, sequencing, ownership, status.
- `business-analyst` — requirements, workflows, rules, KPIs, process mapping.
- `market-researcher` — competitors, pricing, target audiences, alternatives, positioning.
- `system-architect` — system boundaries, technology choices, integrations, scalability, reliability.
- `ui-ux-designer` — user flows, wireframes, interaction design, accessibility, design systems.
- `database-architect` — schemas, indexes, migrations, consistency, retention, backup.
- `frontend-developer` — web interfaces, client state, responsive layouts, accessibility.
- `backend-developer` — APIs, domain logic, validation, persistence, server tests.
- `api-integration-engineer` — third-party APIs, payments, webhooks, retries, rate limits.
- `mobile-developer` — mobile features, platform behavior, offline states, device optimization.
- `ai-ml-engineer` — LLM pipelines, embeddings, inference, evaluation, AI safety, cost.
- `code-reviewer` — correctness, maintainability, regressions, anti-patterns, refactoring.
- `qa-test-automation` — unit, integration, contract, end-to-end, and regression tests.
- `security-compliance` — auth, authorization, secrets, vulnerabilities, privacy, compliance.
- `devops-cicd` — CI/CD, containers, environments, releases, rollback.
- `performance-cost-optimizer` — latency, throughput, queries, bundles, resource and API spend.
- `technical-writer` — README, API docs, architecture guides, runbooks, manuals.
- `growth-copywriter` — landing copy, onboarding, positioning, release notes, conversion.
- `observability-incident-triage` — telemetry, logs, metrics, alerts, incident response.

The detailed roster and ready-made 4–5 agent teams are in [`skills/team-orchestrator/references/agent-selection.md`](skills/team-orchestrator/references/agent-selection.md).

## Recommended small teams

- **Web feature:** `product-manager`, `ui-ux-designer`, `frontend-developer`, `backend-developer`, `qa-test-automation`
- **API feature:** `product-manager`, `system-architect`, `backend-developer`, `database-architect`, `qa-test-automation`
- **Authentication:** `product-manager`, `system-architect`, `backend-developer`, `security-compliance`, `qa-test-automation`
- **Payment integration:** `product-manager`, `api-integration-engineer`, `backend-developer`, `security-compliance`, `qa-test-automation`
- **AI feature:** `product-manager`, `ai-ml-engineer`, `backend-developer`, `security-compliance`, `qa-test-automation`
- **Database migration:** `business-analyst`, `system-architect`, `database-architect`, `backend-developer`, `qa-test-automation`
- **Production launch audit:** `code-reviewer`, `qa-test-automation`, `security-compliance`, `devops-cicd`, `observability-incident-triage`
- **Product discovery:** `product-manager`, `business-analyst`, `market-researcher`, `ui-ux-designer`, `project-orchestrator`

## Install from GitHub

```bash
git clone https://github.com/naitik99045/agentic-product-team.git
cd agentic-product-team
agy plugin validate --strict .
agy plugin install .
agy plugin list
```

You can also place the plugin under `.agents/plugins/` for workspace scope or `~/.gemini/config/plugins/` for global scope.

## License

MIT
