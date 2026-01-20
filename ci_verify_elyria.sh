#!/bin/bash
set -e  # exit immediately on failure

echo "=== Elyria CI: running all tests including fuzz ==="
python -m pytest tests/ --disable-warnings

echo "=== Elyria CI: verifying hash-chain integrity ==="
python -c "from core.replay import verify_chain; assert verify_chain() is True; print('Hash-chain verified ✅')"

echo "=== Elyria CI: generating snapshot ==="
python -c "from core.attestation import create_snapshot; snapshot = create_snapshot(); print('Snapshot overall hash:', snapshot['overall_hash'])"

echo "=== Elyria CI: all checks passed ✅ ==="
