from pydantic import BaseModel

class TransactionCreate(BaseModel):
    description: str
    value: float
    type: str