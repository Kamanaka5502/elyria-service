from core.attestation import create_snapshot

snapshot = create_snapshot()
print("Overall hash:", snapshot["overall_hash"])
