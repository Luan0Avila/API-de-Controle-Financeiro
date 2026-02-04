from fastapi import APIRouter

router = APIRouter(prefix="/transactions", tags=["Transactions"])

@router.post("/")
def create_transaction(data: dict):
    return {"message": "Transação criada", "data": data}