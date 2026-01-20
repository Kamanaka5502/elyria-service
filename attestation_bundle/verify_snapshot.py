import json
import hashlib
import sys

with open("snapshot.json", "rb") as f:
    data = f.read()

computed = hashlib.sha256(data).hexdigest()

with open("EXPECTED_HASH.txt") as f:
    expected = f.read().strip()

if computed == expected:
    print("Snapshot hash matches ✅")
    sys.exit(0)
else:
    print("Snapshot hash mismatch ❌")
    print("Expected:", expected)
    print("Computed:", computed)
    sys.exit(1)
