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

## Office-life animation and reports

The floorplan uses small, non-distracting CSS animations. Staff can gently type, handle paperwork, walk, think, or take a coffee break. These are presentation cues, not claims about real runtime activity; the status and task evidence remain authoritative.

Click `＋ report` under a staff member to submit a report with a title, summary, evidence, risks, and next handoff. Reports are saved under the `reports` array in `state.json` and appear in the Delivery Notes panel. Agents can submit the same shape through the local API or by updating the state file through the provided helper workflow.


From a terminal or agent task, submit a report with:

```bash
python3 scripts/company-state.py report backend-developer "Customer API complete" \
  "Implemented the customer endpoints and validation." \
  --evidence "pytest tests/api; backend/routes/customers.py" \
  --risks "Pagination still needs a load test." \
  --next-handoff "qa-test-automation runs API regression coverage"
```

## Pixel-art office

The dashboard's main floor is an original canvas-rendered pixel office. It uses small animal coworkers, desks, rooms, plants, coffee machines, status bubbles, and activity loops. The visual layer is intentionally decorative; the JSON state, task evidence, approvals, and reports remain authoritative.
