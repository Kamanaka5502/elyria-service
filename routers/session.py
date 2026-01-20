from fastapi import APIRouter, Header, HTTPException
from datetime import datetime, UTC
from core.policy import stamp_decision
from core.capability import require_capability

router = APIRouter(prefix="/session", tags=["session"])

@router.get("/report")
def session_report(x_capability: str = Header(None)):
    try:
        require_capability(x_capability)
    except Exception as e:
        decision = stamp_decision(actor="policy")
        raise HTTPException(
            status_code=400,
            detail={
                "code": "POLICY_REFUSAL",
                "message": str(e),
                "decision": decision
            }
        )

    decision = stamp_decision(actor="session")
    return {
        "status": "active",
        "timestamp": datetime.now(UTC).isoformat(),
        "decision": decision
    }
