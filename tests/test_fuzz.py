import random
import string
from fastapi.testclient import TestClient
from main import app
from core.replay import verify_chain

client = TestClient(app)

def random_string(length=10):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def test_fuzz_rate_manual():
    for _ in range(20):
        value = random.uniform(-100, 200)  # include out-of-bounds
        source = random.choice([random_string(), None, "operator"])
        capability = random.choice(["RATE_WRITE", "INVALID", None])
        r = client.post(
            "/rate/manual",
            headers={"X-Capability": capability} if capability else {},
            json={"value": value, "source": source} if source else {"value": value}
        )
        # Assert no crash
        assert r.status_code in (200, 400, 422)

def test_fuzz_gate():
    for _ in range(20):
        signal = random.choice([random_string(), "", None])
        capability = random.choice(["GATE_ACCESS", "INVALID", None])
        payload = {"signal": signal} if signal else {}
        r = client.post(
            "/gate",
            headers={"X-Capability": capability} if capability else {},
            json=payload
        )
        assert r.status_code in (200, 400, 422)

def test_fuzz_session():
    for _ in range(20):
        capability = random.choice(["SESSION_READ", "INVALID", None])
        r = client.get(
            "/session/report",
            headers={"X-Capability": capability} if capability else {}
        )
        assert r.status_code in (200, 400)
