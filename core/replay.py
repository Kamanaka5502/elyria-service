import json
from pathlib import Path
import hashlib

LOG_PATH = Path(__file__).resolve().parent.parent / "decisions.log"

def verify_chain():
    if not LOG_PATH.exists():
        return True

    lines = LOG_PATH.read_text().splitlines()
    previous_hash = None

    for line in lines:
        entry = json.loads(line)
        expected_prev = entry.get("prev_hash")
        current_hash = entry.get("hash")
        entry_copy = entry.copy()
        entry_copy.pop("hash", None)
        entry_copy.pop("prev_hash", None)
        entry_str = json.dumps(entry_copy, sort_keys=True)
        calculated_hash = hashlib.sha256((entry_str + (previous_hash or "")).encode("utf-8")).hexdigest()
        if calculated_hash != current_hash or expected_prev != previous_hash:
            return False
        previous_hash = current_hash
    return True
