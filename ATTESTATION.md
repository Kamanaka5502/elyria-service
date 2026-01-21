# ATTESTATION

Repository: Kamanaka5502/elyria-service  
Attestation Type: TLB VERIFIED  
Scope: Deterministic replay + snapshot integrity  

---

## Anchored Commit

Commit SHA:
a7133de

This attestation applies **only** to the commit above and its reachable tree.

---

## Declared Artifacts

Snapshot file:
attestation_bundle/snapshot.json

Expected snapshot hash (SHA-256):
90eeb214e0510a17f23679fabb8c4f1143e990ed1dc0607c742969b320433187

Decision log:
decisions.log

---

## Verification Commands

From repository root:

```bash
cd attestation_bundle
PYTHONPATH=.. python verify_replay.py
PYTHONPATH=.. python verify_snapshot.py

