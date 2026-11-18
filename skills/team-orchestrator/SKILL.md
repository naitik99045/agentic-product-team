---
name: team-orchestrator
description: Coordinates a 20-role product and engineering team for software projects. Use when the user asks to plan, build, review, launch, or operate a product with multiple specialized workstreams, or explicitly asks to dispatch a team of agents. The skill creates a shared delivery plan, delegates dependency-aware waves, collects evidence, and closes with an integration and launch-readiness report.
---

# Agentic Product Team Orchestrator

Coordinate the bundled specialist subagents as one accountable delivery team. Do not launch every role automatically for every request. First classify the work, select the smallest useful set of roles, and expand to the full team only when the user requests a full lifecycle delivery or the scope genuinely requires it.

## Operating contract

- Keep the primary session as the delivery lead. It owns the plan, task IDs, acceptance criteria, integration decisions, and final user-facing summary.
- Use `invoke_subagent` for delegation. Prefer isolated worktrees or read-only analysis when parallel edits could conflict. Never ask two agents to edit the same files in the same wave.
- Give each subagent a short, concrete brief containing: objective, repository path, task ID, inputs, allowed files, dependencies, definition of done, expected output, and whether it may edit files.
- Require every result to include status (`done`, `blocked`, or `needs-review`), files changed, evidence or commands run, decisions made, open risks, and recommended next handoff.
- Treat claims without repository evidence as proposals, not completed work. Ask for verification when an agent reports success without tests, screenshots, metrics, or links to artifacts.
- Never expose secrets in prompts, logs, reports, commits, or generated documentation. Ask the user before destructive actions, production changes, paid services, or public releases.

## Workflow

### 1. Intake and routing

Inspect the repository and summarize the request in one delivery brief. Identify the product outcome, constraints, target users, platforms, existing stack, risk level, and requested deadline. Create a task ledger in the project's planning area when appropriate, for example `docs/agentic-team/plan.md`. If the request is narrow, route only the relevant roles.

For a full delivery, use these waves:

1. **Discovery:** Product Manager, Business Analyst, Market Research.
2. **Alignment:** System Architect, UI/UX Designer, Database Architect. Project Orchestrator turns discovery into the executable plan.
3. **Build:** Frontend Developer, Backend Developer, API Integration Engineer, Mobile Developer, AI/ML Engineer. Skip roles that do not match the product surface.
4. **Assurance:** Code Reviewer, QA & Test Automation, Security & Compliance, Performance & Cost Optimizer.
5. **Release and operate:** DevOps & CI/CD, Technical Writer, Growth & Copywriting, Observability & Incident Triage.

Run independent roles in parallel within a wave, but enforce the dependency order between waves. A role may begin with a clearly marked assumption if waiting would waste time, but it must reconcile that assumption at the next gate.

### 2. Shared artifacts and handoffs

Use a stable artifact directory such as `docs/agentic-team/` or the repository's existing planning convention. Maintain:

- `brief.md` — outcome, constraints, non-goals, and success metrics.
- `plan.md` — task ledger with IDs, owners, dependencies, status, and acceptance criteria.
- `decisions.md` — architecture and product decisions with alternatives rejected.
- `risks.md` — risk, impact, likelihood, mitigation, owner, and trigger.
- `evidence/` — test output, screenshots, benchmark results, security findings, and links.
- `handoffs/` — compact role reports when the repository needs durable traceability.

At each wave gate, synthesize results into an updated plan before starting the next wave. Resolve contradictions explicitly; do not silently choose incompatible designs. Preserve the user’s existing architecture and conventions unless the approved plan changes them.

### 3. Editing and integration policy

Assign implementation ownership by file or subsystem. Require agents to inspect current code before editing and to keep changes focused. For parallel implementation, use separate worktrees or disjoint file ownership. Before merging a workstream, run the narrowest relevant checks, then ask Code Reviewer and QA to inspect the integrated result rather than trusting isolated success.

Use this task brief shape:

```text
Task ID: AT-###
Role: <role>
Objective: <one measurable outcome>
Inputs: <approved artifacts and relevant files>
Dependencies: <task IDs or none>
Allowed scope: <files/directories>
May edit: yes/no
Definition of done: <observable checks>
Return: status, summary, files, evidence, decisions, risks, next handoff
```

### 4. Quality gates

Do not declare delivery complete until the applicable gates pass:

- **Product gate:** scope, user stories, acceptance criteria, and success metrics are coherent.
- **Architecture gate:** boundaries, data model, security assumptions, failure modes, and migration strategy are documented.
- **Implementation gate:** code follows repository conventions and the core path works.
- **Assurance gate:** tests pass; known security, accessibility, performance, and cost risks are recorded with disposition.
- **Release gate:** build/deploy path, rollback, documentation, telemetry, support ownership, and launch copy are ready.

If a gate fails, dispatch the smallest remediation task to the responsible role, then re-run only the affected checks. Keep a visible list of deferred work and do not disguise it as completion.

### 5. Final synthesis

Produce a concise delivery report with: outcome, shipped or proposed scope, files changed, commands and checks, agent contributions, unresolved risks, deferred work, launch recommendation, and the next three actions. Include links to durable artifacts. If the user asked for execution, distinguish implemented work from recommendations. If blocked by missing credentials, product decisions, or unavailable tools, state the exact unblock needed.

## Routing guide

Use the bundled agents by their exact names. Product and planning questions usually need `product-manager`, `business-analyst`, and `project-orchestrator`. New systems usually add `system-architect`, `database-architect`, and `ui-ux-designer`. Web work routes to `frontend-developer` and `backend-developer`; integrations route to `api-integration-engineer`; mobile work routes to `mobile-developer`; AI features route to `ai-ml-engineer`. Any production-facing change should normally include `code-reviewer`, `qa-test-automation`, `security-compliance`, `devops-cicd`, `observability-incident-triage`, and `technical-writer`. Add `performance-cost-optimizer` when latency, scale, or spend matters and `growth-copywriter` when the user-facing launch or onboarding experience matters.

## Failure handling

If a subagent is unavailable, continue with the nearest qualified role and mark the gap. If agents disagree, return to the artifact and acceptance criteria, ask each side for evidence, and record the decision. If parallel edits conflict, stop integration, preserve both results, and have the Project Orchestrator assign a single owner for reconciliation. Never repeatedly relaunch a failing agent without changing the brief or diagnosing the failure.
