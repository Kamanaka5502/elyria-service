_DECAY_STEP = 0.15
_MIN_AUTHORITY = 0.3

_authority = {}

def init_actor(actor: str):
    _authority.setdefault(actor, 1.0)

def decay(actor: str):
    _authority[actor] = max(
        _MIN_AUTHORITY,
        _authority.get(actor, 1.0) - _DECAY_STEP
    )

def reinforce(actor: str):
    _authority[actor] = min(
        1.0,
        _authority.get(actor, 1.0) + 0.05
    )

def authority_level(actor: str) -> float:
    return _authority.get(actor, 1.0)

def enforce_authority(actor: str):
    level = authority_level(actor)
    if level < 0.5:
        return False, {
            "code": "AUTHORITY_DEGRADED",
            "message": "Actor authority below safe threshold",
            "authority": level
        }
    return True, {"authority": level}
