from fastapi.testclient import TestClient
from main import app
from core.replay import verify_chain
from pathlib import Path

client = TestClient(app)
LOG_PATH = Path(__file__).resolve().parent.parent / "decisions.log"

# --- Gate tests ---
def test_gate_requires_capability():
    r = client.post("/gate", json={"signal": "test"})
    assert r.status_code == 400
    body = r.json()
    assert body["detail"]["code"] == "POLICY_REFUSAL"

def test_gate_with_capability():
    r = client.post("/gate", headers={"X-Capability": "GATE_ACCESS"}, json={"signal": "test"})
    assert r.status_code == 200
    body = r.json()
    assert body["decision"]["actor"] == "gate"

# --- Session tests ---
def test_session_requires_capability():
    r = client.get("/session/report")
    assert r.status_code == 400
    body = r.json()
    assert body["detail"]["code"] == "POLICY_REFUSAL"

def test_session_with_capability():
    r = client.get("/session/report", headers={"X-Capability": "SESSION_READ"})
    assert r.status_code == 200
    body = r.json()
    assert body["decision"]["actor"] == "session"

# --- Hash chain verification ---
def test_hash_chain_integrity():
    assert verify_chain() is True
