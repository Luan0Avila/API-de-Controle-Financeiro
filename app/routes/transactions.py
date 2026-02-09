from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.models.transaction import Transaction
from app.schemas.transaction import TransactionCreate

router = APIRouter(prefix="/transactions", tags=["Transactions"])

@router.post("/")
def create_transaction(
    transacition: TransactionCreate,
    db: Session = Depends(get_db)):
    new_transaction = Transaction(
        description=transacition.description, value=transacition.value,
        type=transacition.type, user_id=1 #temporario
    )

    db.add(new_transaction)
    db.commit()
    db.refresh(new_transaction)
    
    return new_transaction

@router.get("/")
def list_transactions(db: Session=Depends(get_db)):
    return db.query(Transaction).all()