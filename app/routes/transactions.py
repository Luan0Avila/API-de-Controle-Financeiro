from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.models.transaction import Transaction
from app.schemas.transaction import TransactionCreate
from app.core.security import get_current_user
from app.models.user import User


router = APIRouter(prefix="/transactions", tags=["Transactions"])

@router.post("/")
def create_transaction(
    transacition: TransactionCreate,
    db: Session = Depends(get_db),
    current_user: User= Depends(get_current_user)):
    new_transaction = Transaction(
        description=transacition.description, value=transacition.value,
        type=transacition.type, user_id=current_user.id #temporario
    )

    db.add(new_transaction)
    db.commit()
    db.refresh(new_transaction)
    
    return new_transaction

@router.get("/")
def list_transactions(db: Session=Depends(get_db)):
    return db.query(Transaction).all()