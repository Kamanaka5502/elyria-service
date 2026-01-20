from collections import defaultdict
from hashlib import sha256
from datetime import datetime, UTC

_disagreements = defaultdict(list)

def submit_position(
    signal_id: str,
    actor: str,
    decision: str,
    evidence_hash: str
):
    entry = {
        "actor": actor,
        "decision": decision,
        "evidence": evidence_hash,
        "timestamp": datetime.now(UTC).isoformat()
    }
    _disagreements[signal_id].append(entry)

def disagreement_state(signal_id: str):
    positions = _disagreements.get(signal_id, [])
    if not positions:
        return None

    unique = {p["decision"] for p in positions}
    return {
        "signal": signal_id,
        "conflicted": len(unique) > 1,
        "positions": positions,
        "hash": sha256(str(positions).encode()).hexdigest()
    }
