#!/usr/bin/env python3
"""Serve the zero-dependency company dashboard and its local JSON state API."""
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
import json, os
ROOT=Path(__file__).resolve().parents[1]
STATE=ROOT/"company"/"state.json"
class Handler(SimpleHTTPRequestHandler):
    def __init__(self,*args,**kwargs): super().__init__(*args,directory=str(ROOT),**kwargs)
    def do_GET(self):
        if self.path == "/api/state":
            raw=STATE.read_bytes(); self.send_response(200); self.send_header("Content-Type","application/json"); self.send_header("Cache-Control","no-store"); self.end_headers(); self.wfile.write(raw); return
        if self.path == "/": self.path = "/dashboard/index.html"
        return super().do_GET()
    def do_POST(self):
        if self.path != "/api/state": self.send_error(404); return
        length=int(self.headers.get("Content-Length","0")); payload=json.loads(self.rfile.read(length))
        if not isinstance(payload,dict): self.send_error(400,"JSON object required"); return
        STATE.write_text(json.dumps(payload, indent=2)+"\n")
        self.send_response(204); self.end_headers()
    def log_message(self, fmt,*args): print(fmt % args)
if __name__ == "__main__":
    port=int(os.environ.get("PORT","8765")); print(f"Agentic Product Team dashboard: http://127.0.0.1:{port}"); ThreadingHTTPServer(("127.0.0.1",port),Handler).serve_forever()
