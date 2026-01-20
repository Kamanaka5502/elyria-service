from fastapi.testclient import TestClient
from main import app
from pathlib import Path
from core.replay import verify_chain

client = TestClient(app)
LOG_PATH = Path(__file__).resolve().parent.parent / "decisions.log"

def test_manual_rate_requires_capability():
    r = client.post("/rate/manual", json={"value": 10, "source": "operator"})
    assert r.status_code == 400
    body = r.json()
    # fix KeyError
    assert body["detail"]["code"] == "POLICY_REFUSAL"

def test_manual_rate_with_capability():
    r = client.post(
        "/rate/manual",
        headers={"X-Capability": "RATE_WRITE"},
        json={"value": 10, "source": "operator"}
    )
    assert r.status_code == 200
    body = r.json()
    assert body["status"] == "applied"
    assert "decision" in body
    assert "hash" in body["decision"]
    assert "prev_hash" in body["decision"]

def test_manual_rate_rejects_missing_source():
    r = client.post(
        "/rate/manual",
        headers={"X-Capability": "RATE_WRITE"},
        json={"value": 10}
    )
    # Pydantic validation returns 422
    assert r.status_code in (400, 422)
    body = r.json()
    if r.status_code == 422:
        assert "source" in str(body)

def test_manual_rate_rejects_out_of_bounds_value():
    r = client.post(
        "/rate/manual",
        headers={"X-Capability": "RATE_WRITE"},
        json={"value": -5, "source": "operator"}
    )
    assert r.status_code in (400, 422)

def test_decision_is_logged():
    if LOG_PATH.exists():
        LOG_PATH.unlink()
    r = client.post(
        "/rate/manual",
        headers={"X-Capability": "RATE_WRITE"},
        json={"value": 10, "source": "operator"}
    )
    assert r.status_code == 200
    assert LOG_PATH.exists()
    lines = LOG_PATH.read_text().splitlines()
    assert len(lines) >= 1

def test_hash_chain_verification():
    client.post("/rate/manual", headers={"X-Capability": "RATE_WRITE"}, json={"value": 10, "source": "operator"})
    client.post("/rate/manual", headers={"X-Capability": "RATE_WRITE"}, json={"value": 20, "source": "operator"})
    assert verify_chain() is True
