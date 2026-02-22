from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.models.transaction import Transaction
from app.schemas.transaction import TransactionCreate, TransactionResponse, FinancialSummary
from app.core.security import get_current_user
from app.models.user import User
from typing import List, Optional
from app.services.finance import calculate_summary, calculate_monthly_summary
from datetime import date
from sqlalchemy import extract

router = APIRouter(prefix="/transactions", tags=["Transactions"])

@router.post("/", response_model=TransactionResponse)
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

@router.get("/", response_model=List[TransactionResponse])
def list_transactions(
    month: Optional[int] = None,
    year: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)):

    query = db.query(Transaction).filter(
        Transaction.user_id == current_user.id
    )

    if month & year:
        query = query.filter(
            extract("month", Transaction.date) == month,
            extract("year", Transaction.date) == year
        )

    return query.all()

@router.get(
    "/summary", response_model=FinancialSummary)
def get_summary(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return calculate_summary(db, current_user.id)


@router.get(
    "/summary/month",
    response_model=FinancialSummary
)
def get_monthly_summary(
    month: int,
    year: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return calculate_monthly_summary(
        db,
        current_user.id,
        month,
        year
    )