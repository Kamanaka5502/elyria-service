# Elyria Attestation Bundle

This bundle allows independent verification of Elyria's historical behavior.

## What this proves
- Decision history integrity (hash-chain)
- Deterministic replay
- Snapshot authenticity

## How to verify

1. Create a Python virtual environment
2. Install Elyria dependencies
3. From this directory, run:

    python verify_replay.py
    python verify_snapshot.py

If both commands succeed, the system behaved exactly as recorded.
No trust in the operator is required.
