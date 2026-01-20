from core.replay import verify_chain
import sys

if verify_chain():
    print("Replay verification passed ✅")
    sys.exit(0)
else:
    print("Replay verification failed ❌")
    sys.exit(1)
