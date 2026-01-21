# core/conflict.py
# Conflict resolution & decision tracking module

conflict_log = {}

def record_decision(entity_id: str, decision: str) -> None:
    """Record a decision made for an entity to track potential conflicts."""
    if entity_id not in conflict_log:
        conflict_log[entity_id] = []
    conflict_log[entity_id].append(decision)
    print(f"[Conflict] Recorded decision for {entity_id}: {decision}")

def is_conflicted(entity_id: str) -> bool:
    """Return True if conflicting decisions exist for an entity."""
    if entity_id not in conflict_log:
        return False
    decisions = conflict_log[entity_id]
    return len(set(decisions)) > 1
