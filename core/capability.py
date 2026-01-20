from core.policy import PolicyViolation

VALID_CAPABILITIES = {
    "RATE_WRITE",
    "GATE_ACCESS",
    "SESSION_READ"
}

def require_capability(cap: str):
    if cap not in VALID_CAPABILITIES:
        raise PolicyViolation(f"Invalid capability: {cap}")
    return cap
