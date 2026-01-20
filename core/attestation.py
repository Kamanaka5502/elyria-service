import json
from pathlib import Path
import hashlib

LOG_PATH = Path(__file__).resolve().parent.parent / "decisions.log"
SNAPSHOT_PATH = Path(__file__).resolve().parent.parent / "decisions.snapshot.json"

def create_snapshot():
    if not LOG_PATH.exists():
        return None
    lines = LOG_PATH.read_text().splitlines()
    snapshot = []
    for line in lines:
        entry = json.loads(line)
        snapshot.append({
            "actor": entry.get("actor"),
            "timestamp": entry.get("timestamp"),
            "hash": entry.get("hash"),
            "prev_hash": entry.get("prev_hash")
        })
    # Include overall hash
    combined = "".join(e["hash"] for e in snapshot).encode("utf-8")
    overall_hash = hashlib.sha256(combined).hexdigest()
    snapshot_dict = {
        "entries": snapshot,
        "overall_hash": overall_hash
    }
    with SNAPSHOT_PATH.open("w", encoding="utf-8") as f:
        json.dump(snapshot_dict, f, indent=2)
    return snapshot_dict
