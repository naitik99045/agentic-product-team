#!/usr/bin/env python3
"""Small, dependency-free state helper for the local Agentic Product Team dashboard."""
import argparse, json
from datetime import datetime, timezone
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
STATE = ROOT / "company" / "state.json"

def load():
    return json.loads(STATE.read_text())

def save(data):
    data.setdefault("company", {})["updatedAt"] = datetime.now(timezone.utc).isoformat()
    STATE.write_text(json.dumps(data, indent=2) + "\n")

def main():
    p=argparse.ArgumentParser(description="Update Agentic Product Team dashboard state")
    sub=p.add_subparsers(dest="command", required=True)
    a=sub.add_parser("agent", help="Set an agent status")
    a.add_argument("name"); a.add_argument("status", choices=["working","idle","blocked","offline"]); a.add_argument("--task", default="")
    t=sub.add_parser("task", help="Set a task status and progress")
    t.add_argument("id"); t.add_argument("status", choices=["backlog","ready","assigned","in-progress","blocked","waiting-approval","in-review","verified","completed","cancelled"]); t.add_argument("--progress", type=int, default=None)
    r=sub.add_parser("report", help="Submit a structured work report")
    r.add_argument("agent"); r.add_argument("title"); r.add_argument("summary"); r.add_argument("--evidence", default=""); r.add_argument("--risks", default=""); r.add_argument("--next-handoff", default="")
    sub.add_parser("show", help="Print current state")
    args=p.parse_args(); data=load()
    if args.command == "show": print(json.dumps(data, indent=2)); return
    if args.command == "agent":
        for item in data.setdefault("agents", []):
            if item.get("name") == args.name:
                item.update(status=args.status, task=args.task); break
        else: data["agents"].append({"name":args.name,"status":args.status,"task":args.task})
    if args.command == "task":
        found=False
        for item in data.setdefault("tasks", []):
            if item.get("id") == args.id:
                item["status"] = args.status
                if args.progress is not None: item["progress"] = max(0, min(100, args.progress))
                found=True; break
        if not found: p.error(f"Unknown task: {args.id}")
    if args.command == "report":
        now=datetime.now().astimezone().strftime("%H:%M")
        data.setdefault("reports", []).insert(0, {"id":f"REP-{int(datetime.now().timestamp()*1000)}", "agent":args.agent, "title":args.title, "summary":args.summary, "evidence":args.evidence, "risks":args.risks, "nextHandoff":args.next_handoff, "status":"submitted", "time":now})
        data.setdefault("activity", []).insert(0, {"time":now, "agent":args.agent, "action":f"Submitted report: {args.title}", "tone":"blue"})
        data["activity"] = data["activity"][:12]
    save(data); print(f"Updated {STATE}")
if __name__ == "__main__": main()
