from pydantic import BaseModel
from typing import Literal

class TransactionCreate(BaseModel):
    description: str
    value: float
    type: Literal["income", "expense"]

class TransactionResponse(BaseModel):
    id: int
    description: str
    value: float
    type: str
    user_id: int

    class Config:
        from_attributes = True