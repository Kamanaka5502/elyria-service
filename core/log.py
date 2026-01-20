import json
from pathlib import Path
import hashlib

SERVICE_ROOT = Path(__file__).resolve().parent.parent
LOG_PATH = SERVICE_ROOT / "decisions.log"

def append_decision(entry: dict):
    previous_hash = None
    if LOG_PATH.exists() and LOG_PATH.stat().st_size > 0:
        with LOG_PATH.open("r", encoding="utf-8") as f:
            lines = f.read().splitlines()
            last_entry = json.loads(lines[-1])
            previous_hash = last_entry.get("hash")

    entry_str = json.dumps(entry, sort_keys=True)
    entry_hash = hashlib.sha256((entry_str + (previous_hash or "")).encode("utf-8")).hexdigest()
    entry["hash"] = entry_hash
    entry["prev_hash"] = previous_hash

    with LOG_PATH.open("a", encoding="utf-8") as f:
        f.write(json.dumps(entry) + "\n")
