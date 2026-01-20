from core.authority import enforce_authority, decay
from core.conflict import record_decision, is_conflicted
from datetime import datetime, UTC
from core.log import append_decision

class PolicyViolation(Exception):
    pass

def require_intent(source: str | None):
    if not source:
        raise PolicyViolation("Missing intent source")

def stamp_decision(actor: str):
    decision = {
        "actor": actor,
        "timestamp": datetime.now(UTC).isoformat()
    }
    append_decision(decision)
    return decision
