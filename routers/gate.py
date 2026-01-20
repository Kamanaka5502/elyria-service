from fastapi import APIRouter, HTTPException, Header
from pydantic import BaseModel
from core.policy import stamp_decision, PolicyViolation, require_intent
from core.capability import require_capability

router = APIRouter(prefix="/gate", tags=["gate"])

class GateRequest(BaseModel):
    signal: str
    strength: float | None = None

class GateResponse(BaseModel):
    accepted: bool
    reason: str
    decision: dict

@router.post("", response_model=GateResponse)
def gate(req: GateRequest, x_capability: str = Header(None)):
    try:
        require_capability(x_capability)
        require_intent(req.signal)
        if not req.signal.strip():
            raise PolicyViolation("Empty signal")
    except PolicyViolation as e:
        decision = stamp_decision(actor="policy")
        raise HTTPException(
            status_code=400,
            detail={
                "code": "POLICY_REFUSAL",
                "message": str(e),
                "decision": decision
            }
        )

    decision = stamp_decision(actor="gate")
    return GateResponse(
        accepted=True,
        reason=f"Signal '{req.signal}' accepted",
        decision=decision
    )
