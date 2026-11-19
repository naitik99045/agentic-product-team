# Company Operating System

This directory is the durable source of truth for the Agentic Product Team plugin. The orchestrator should read company policies before starting consequential work and update the state file as work moves through the task lifecycle.

## State and task lifecycle

`state.json` is a local, human-readable dashboard state file. It is safe to edit with the helper script or the localhost dashboard. The lifecycle is:

`backlog → ready → assigned → in-progress → blocked / waiting-approval → in-review → verified → completed`

Agents must not mark a task `verified` or `completed` without evidence. Use `waiting-approval` for production, financial, legal, destructive, privacy-sensitive, or public actions.

## Operating rules

- The CEO / Chief of Staff owns priorities and escalations.
- Department managers coordinate specialists and report blockers upward.
- Specialists work only within an assigned objective and file scope.
- Every task has an owner, acceptance criteria, evidence, and next action.
- A human approval is required for irreversible or high-impact actions.
- After three materially different failed attempts, escalate instead of looping.
- The dashboard is for visibility and control; it does not claim that an agent completed work merely because its card is marked active.

## Start the local dashboard

From the repository root:

```bash
python3 scripts/serve-dashboard.py
```

Open http://127.0.0.1:8765. The dashboard reads and writes `company/state.json` through the local server. Use `python3 scripts/company-state.py --help` to update state from scripts or agent workflows.
