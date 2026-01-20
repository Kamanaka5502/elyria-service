from pydantic import BaseModel

class Refusal(BaseModel):
    code: str
    message: str
    decision: dict
