#!/usr/bin/env python3
"""Run the public Agent Teacher path against a real loopback HTTP server.

The check deliberately uses only the standard library. It creates a temporary
session database, completes one authored Vietnamese fraction rehearsal, checks
replay/export, and removes the temporary directory on exit.
"""

from __future__ import annotations

import http.client
import json
import re
import subprocess
import sys
import tempfile
import time
import uuid
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CHOICES = ("explain", "tentative", "number_line", "novel_reason", "continue", "probe", "save")


def request(port: int, method: str, path: str, body: dict | None = None) -> tuple[int, dict, bytes]:
    connection = http.client.HTTPConnection("127.0.0.1", port, timeout=5)
    try:
        payload = json.dumps(body, ensure_ascii=False).encode() if body is not None else None
        headers = {"Content-Type": "application/json"} if payload is not None else {}
        connection.request(method, path, payload, headers)
        response = connection.getresponse()
        return response.status, dict(response.getheaders()), response.read()
    finally:
        connection.close()


def wait_for_server(process: subprocess.Popen[str]) -> int:
    deadline = time.monotonic() + 8
    while time.monotonic() < deadline:
        line = process.stdout.readline() if process.stdout else ""
        match = re.search(r"http://127\.0\.0\.1:(\d+)", line)
        if match:
            return int(match.group(1))
        if process.poll() is not None:
            raise RuntimeError(process.stderr.read() if process.stderr else "server exited")
    raise TimeoutError("server did not announce a listening address")


def main() -> int:
    with tempfile.TemporaryDirectory(prefix="agent-teacher-smoke-") as data_dir:
        process = subprocess.Popen(
            [sys.executable, "-B", str(ROOT / "run_rehearsal.py"), "--port", "0", "--data-dir", data_dir],
            cwd=ROOT,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        try:
            port = wait_for_server(process)
            status, _, raw = request(port, "GET", "/api/status")
            status_payload = json.loads(raw)
            assert status == 200 and status_payload["model_calls"] is False

            status, _, raw = request(port, "POST", "/api/sessions", {
                "case_id": "fraction-magnitude", "request_id": str(uuid.uuid4())
            })
            assert status == 201
            state = json.loads(raw)["session"]

            for choice in CHOICES:
                status, _, raw = request(port, f"POST", f"/api/sessions/{state['id']}/events", {
                    "revision": state["revision"],
                    "type": state["phase"],
                    "choice": choice,
                    "text": "Tôi sẽ hỏi em giải thích cách so sánh rồi thử một bài mới.",
                    "request_id": str(uuid.uuid4()),
                })
                assert status == 200, raw.decode()
                state = json.loads(raw)["session"]

            assert state["phase"] == "complete" and state["revision"] == len(CHOICES)
            status, _, raw = request(port, "GET", f"/api/sessions/{state['id']}/replay")
            replay = json.loads(raw)
            assert status == 200 and replay["matches_saved_state"] is True
            status, headers, raw = request(port, "GET", f"/api/sessions/{state['id']}/export?format=md")
            assert status == 200 and "attachment" in headers["Content-Disposition"]
            exported = raw.decode()
            assert "# Mẫu số lớn hơn" in exported
            assert "Trạng thái: complete" in exported
            print(json.dumps({
                "status": "PASS",
                "mode": status_payload["mode"],
                "case": state["case_id"],
                "revision": state["revision"],
                "replay_matches": replay["matches_saved_state"],
                "export": "markdown",
            }, ensure_ascii=False))
            return 0
        finally:
            process.terminate()
            try:
                process.wait(timeout=4)
            except subprocess.TimeoutExpired:
                process.kill()
                process.wait(timeout=4)


if __name__ == "__main__":
    raise SystemExit(main())
