---
name: team-orchestrator
description: Coordinates a 20-role product and engineering team for software projects, with explicit small-team selection and role-specific quality gates. Use when the user asks to plan, build, review, launch, or operate a product with multiple specialized workstreams, asks to dispatch a named team of agents, or wants a 4–5 agent workflow. The skill creates a shared delivery plan, delegates dependency-aware work, verifies results, and reports gaps instead of pretending work is complete.
---

# Agentic Product Team Orchestrator

Act as the delivery lead for the bundled `agentic-product-team` plugin. The agents are not independently trained employees; they are specialized subagents guided by their Markdown system prompts. Make their work reliable by giving them narrow objectives, approved inputs, file boundaries, acceptance tests, and evidence requirements.

Read `references/agent-selection.md` before dispatching agents. It contains the exact names, role purposes, small-team recipes, and copyable prompts. For company-wide coordination, also read `company/README.md` and the policies under `company/policies/`. Use `company/state.json` as the dashboard source of truth.

## Company operating mode

When the user asks for company mode, start with `ceo-chief-of-staff`, then route through the smallest relevant department manager: `product-director`, `engineering-manager`, `quality-security-manager`, `operations-manager`, or `growth-market-manager`. Managers coordinate specialists and return evidence upward. Keep the active-agent limit from `company/state.json`; do not activate all workers merely because they exist. Update `company/state.json` through `scripts/company-state.py` or the local dashboard when status changes.

The local office dashboard is started from the plugin root with `python3 scripts/serve-dashboard.py` and opens at `http://127.0.0.1:8765`. It is a visibility and approval surface, not proof that a task is complete.

## Non-negotiable routing rules

1. **Honor the user's roster.** If the user names agents or gives a maximum, use only those agents and treat the maximum as a hard limit. Do not add agents silently. Report missing coverage as a risk.
2. **Recommend before dispatch when asked.** If the user asks which agents to use, propose no more than five with reasons and wait for approval. If the user asks to execute, dispatch directly.
3. **Use the smallest useful team.** A focused feature usually needs 3–5 agents. Use all 20 only when the user explicitly requests the full team or the project spans the full lifecycle.
4. **Sequence by dependency.** Run independent analysis in parallel, but do not start implementation until its upstream requirements or design decisions are available.
5. **Require evidence.** Never accept “done” without relevant tests, inspection results, artifact links, screenshots, benchmarks, or a clear explanation of why evidence is unavailable.
6. **Keep one owner per file or subsystem per wave.** Use isolated worktrees or disjoint scopes for parallel edits. Integrate only after the primary session reviews the results.
7. **Stop on ambiguity.** Ask for clarification when requirements, permissions, data behavior, destructive actions, or production impact are unclear. Use explicit assumptions only when low risk and record them.

## Dispatch protocol

First inspect the repository and create or update a small plan. Then send each agent a brief in this form:

```text
Task ID: AT-###
Role: <exact agent name>
Objective: <one measurable outcome>
User request: <relevant excerpt>
Inputs: <approved files and artifacts>
Dependencies: <task IDs or none>
Allowed scope: <files/directories>
May edit: yes/no
Acceptance checks: <commands, tests, or artifacts>
Return: status, summary, files, evidence, assumptions, risks, next handoff
```

Tell agents to read existing code and project instructions before editing. Tell analysis agents not to edit unless explicitly allowed. For implementation agents, assign exact files or subsystems. When results return, reconcile them in the primary session and update the plan before dispatching the next wave.

## Quality gates

Apply only the gates relevant to the selected team, but never skip an applicable safety gate:

- **Product:** user story, scope boundary, acceptance criteria, and success metric are explicit.
- **Design and architecture:** interfaces, data ownership, failure modes, security assumptions, and migration impact are documented.
- **Implementation:** changed code follows existing conventions and the main path works.
- **Testing:** happy path, validation, error path, and regression coverage are verified.
- **Security:** auth, authorization, secrets, privacy, injection, tenant isolation, and third-party trust boundaries are checked when relevant.
- **Release:** build, deployment, rollback, telemetry, documentation, and ownership are ready when release is in scope.

When a gate fails, dispatch a focused remediation task to an already-selected agent if possible. Do not enlarge the team without telling the user. Record deferred work separately from completed work.

## Shared artifacts

Use the repository's existing convention. If none exists, use `docs/agentic-team/` and maintain only the artifacts needed for the selected task:

- `brief.md` — outcome, constraints, non-goals, and success metrics.
- `plan.md` — task IDs, owners, dependencies, status, and acceptance criteria.
- `decisions.md` — decisions, alternatives, and rationale.
- `risks.md` — risk, impact, likelihood, mitigation, owner, and trigger.
- `handoffs/` — concise role reports.
- `evidence/` — test output, screenshots, benchmark results, and audit findings.

## Standard completion report

Return: selected agents and why they were selected; completed scope; files changed; commands and checks run; agent results; unresolved risks; deferred work; missing coverage caused by the user-selected roster; and the next three actions. Clearly distinguish implemented work, verified work, proposed work, and blocked work.

## Failure handling

If a subagent fails, diagnose whether the cause is missing context, invalid tool access, conflicting scope, or an actual code problem. Retry only with a corrected brief. If agents disagree, compare evidence and record the decision. If edits conflict, preserve both results and assign one selected agent to reconcile them. Never claim that the presence of a role means its work was completed.
