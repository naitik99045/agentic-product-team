#!/usr/bin/env python3
"""Start the local Agentic Product Team office once and announce its URL to Antigravity."""
import json
import os
import subprocess
import sys
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SERVER = ROOT / "scripts" / "serve-dashboard.py"
PORT = int(os.environ.get("AGENTIC_TEAM_DASHBOARD_PORT", "8765"))
URL = f"http://127.0.0.1:{PORT}"
LOG = Path(os.environ.get("AGENTIC_TEAM_DASHBOARD_LOG", "/tmp/agentic-product-team-dashboard.log"))
PID = Path(os.environ.get("AGENTIC_TEAM_DASHBOARD_PID", "/tmp/agentic-product-team-dashboard.pid"))


def emit(message=None):
    if not message:
        print("{}")
        return
    print(json.dumps({"injectSteps": [{"systemMessage": {"systemMessage": message}}]}))


def healthy():
    try:
        with urllib.request.urlopen(URL + "/api/state", timeout=0.7) as response:
            return response.status == 200 and response.headers.get("Content-Type", "").startswith("application/json")
    except Exception:
        return False


def main():
    if os.environ.get("AGENTIC_TEAM_AUTO_START", "1").lower() in {"0", "false", "no", "off"}:
        emit()
        return
    if healthy():
        emit(f"Agentic Product Team office is already running at {URL}. Use company/state.json for live task, status, approval, and report updates.")
        return

    LOG.parent.mkdir(parents=True, exist_ok=True)
    child_env = os.environ.copy()
    child_env["PORT"] = str(PORT)
    with LOG.open("ab") as log:
        process = subprocess.Popen(
            [sys.executable, str(SERVER)],
            cwd=str(ROOT),
            env=child_env,
            stdin=subprocess.DEVNULL,
            stdout=log,
            stderr=subprocess.STDOUT,
            start_new_session=True,
        )
    PID.write_text(str(process.pid) + "\n")
    for _ in range(20):
        if healthy():
            emit(f"Agentic Product Team office started automatically at {URL}. Keep the dashboard open to watch staff, tasks, approvals, and reports.")
            return
        time.sleep(0.1)
    emit(f"The office launcher started, but {URL} is not responding yet. Check {LOG} if the dashboard does not load.")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        emit(f"The office dashboard could not start automatically: {exc}")
