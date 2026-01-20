from fastapi import APIRouter, HTTPException, Header
from pydantic import BaseModel, Field
from core.policy import require_intent, stamp_decision, PolicyViolation
from core.capability import require_capability

router = APIRouter(prefix="/rate", tags=["rate"])

class ManualRate(BaseModel):
    value: float = Field(..., gt=0, lt=100)
    source: str

@router.post("/manual")
def manual_rate(rate: ManualRate, x_capability: str = Header(None)):
    try:
        require_capability(x_capability)
        require_intent(rate.source)
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

    decision = stamp_decision(actor=rate.source)
    return {
        "status": "applied",
        "rate": rate.value,
        "decision": decision
    }
