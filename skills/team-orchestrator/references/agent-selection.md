# Agent Selection and Team Recipes

Use the exact agent names below when asking Antigravity to dispatch a team. All names belong to the `agentic-product-team` plugin.

## Company management layer

Use these management agents when the task spans departments or you want company-mode coordination:

| Agent name | Use for |
|---|---|
| `ceo-chief-of-staff` | Company goals, priorities, escalations, approvals, executive reports |
| `product-director` | Product department coordination and scope decisions |
| `engineering-manager` | Engineering sequencing, subsystem ownership, technical delivery |
| `quality-security-manager` | Verification, security, review, performance, and release gates |
| `operations-manager` | CI/CD, deployment, observability, runbooks, and incident readiness |
| `growth-market-manager` | Market research, positioning, onboarding, launch messaging, and experiments |

For company mode, start with `ceo-chief-of-staff` and add only the managers relevant to the current goal. The normal default is no more than 5 active agents.

## Exact roster

| Agent name | Use for |
|---|---|
| `product-manager` | Product vision, MVP scope, priorities, user stories, acceptance criteria |
| `project-orchestrator` | Task breakdown, dependencies, sequencing, ownership, status tracking |
| `business-analyst` | Requirements, workflows, business rules, KPIs, process mapping |
| `market-researcher` | Competitors, pricing, audience, alternatives, positioning evidence |
| `system-architect` | System boundaries, stack, integrations, scalability, reliability |
| `ui-ux-designer` | User flows, wireframes, interaction design, accessibility, design system |
| `database-architect` | Schema, indexes, migrations, consistency, retention, backup |
| `frontend-developer` | Web UI, state, responsive layouts, accessibility, client integration |
| `backend-developer` | APIs, domain logic, validation, services, server tests |
| `api-integration-engineer` | Third-party APIs, payments, webhooks, retries, rate limits |
| `mobile-developer` | iOS/Android or cross-platform features and device behavior |
| `ai-ml-engineer` | LLMs, embeddings, inference, evaluation, AI safety, model cost |
| `code-reviewer` | Correctness, maintainability, regressions, anti-patterns, refactoring |
| `qa-test-automation` | Unit, integration, contract, end-to-end, regression testing |
| `security-compliance` | Auth, authorization, secrets, vulnerabilities, privacy, compliance |
| `devops-cicd` | CI/CD, containers, environments, releases, rollback |
| `performance-cost-optimizer` | Latency, throughput, queries, bundles, resource and API spend |
| `technical-writer` | README, API docs, architecture guides, runbooks, manuals |
| `growth-copywriter` | Landing copy, onboarding, positioning, release notes, conversion |
| `observability-incident-triage` | Logs, metrics, traces, alerts, incident diagnosis, hotfix routing |

## Copy-and-paste selection prompts

Always state the limit and exact roster. Example:

```text
Use only these 5 agents from the agentic-product-team plugin:
product-manager, system-architect, backend-developer, qa-test-automation, security-compliance.
Do not invoke any other subagents. Coordinate them in dependency order, keep a shared
plan, and stop after the requested feature and its verification are complete.
Task: add passwordless email login to the existing web application.
```

If you want recommendations first:

```text
Recommend a team of no more than 5 agents from the agentic-product-team plugin for this task.
Explain why each is needed, then wait for my approval before dispatching them.
Task: <describe the task>
```

## Ready-made teams

### New web feature
`product-manager`, `ui-ux-designer`, `frontend-developer`, `backend-developer`, `qa-test-automation`

Add `security-compliance` instead of `ui-ux-designer` when the feature handles identity, permissions, payments, or sensitive data.

### API or backend feature
`product-manager`, `system-architect`, `backend-developer`, `database-architect`, `qa-test-automation`

Add `api-integration-engineer` when an external service is involved.

### Authentication or authorization
`product-manager`, `system-architect`, `backend-developer`, `security-compliance`, `qa-test-automation`

Do not mark complete without negative tests for unauthorized, expired, replayed, malformed, and cross-tenant requests where applicable.

### Payment integration
`product-manager`, `api-integration-engineer`, `backend-developer`, `security-compliance`, `qa-test-automation`

Require webhook signature validation, idempotency, retry behavior, failure-state handling, and secret redaction.

### AI feature
`product-manager`, `ai-ml-engineer`, `backend-developer`, `security-compliance`, `qa-test-automation`

Require representative evaluation cases, prompt/input boundaries, fallback behavior, data handling review, and cost assumptions.

### Database migration
`business-analyst`, `system-architect`, `database-architect`, `backend-developer`, `qa-test-automation`

Require forward migration, rollback or recovery plan, compatibility window, backup check, and verification against realistic data volume.

### Production launch audit
`code-reviewer`, `qa-test-automation`, `security-compliance`, `devops-cicd`, `observability-incident-triage`

Add `performance-cost-optimizer` if scale, latency, or spend is a launch concern.

### Product discovery only
`product-manager`, `business-analyst`, `market-researcher`, `ui-ux-designer`, `project-orchestrator`

This team should produce a decision-ready brief and backlog, not implementation code.

## Selection rules

- If the user names agents, invoke only those agents. Do not silently add extra agents; flag missing coverage instead.
- If the user gives a maximum such as “4 agents,” treat it as a hard limit.
- Prefer 3–5 agents for a focused feature. Use the full roster only for an explicit end-to-end request.
- Keep implementation ownership disjoint. Only one agent may edit a given file or subsystem in a wave.
- Always include `qa-test-automation` for code changes unless the user explicitly chooses a documentation-only task.
- Always flag the absence of `security-compliance` for auth, permissions, payments, personal data, secrets, or external trust boundaries.
- Always flag the absence of `code-reviewer` before merging substantial code.
