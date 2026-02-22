from pydantic import BaseModel
from datetime import date
from typing import Literal

class TransactionCreate(BaseModel):
    description: str
    value: float
    type: Literal["income", "expense"]
    date: date

class TransactionResponse(BaseModel):
    id: int
    description: str
    value: float
    type: str
    date: date
    user_id: int

    class Config:
        from_attributes = True


class FinancialSummary(BaseModel):
    total_income: float
    total_expense: float
    balance: float