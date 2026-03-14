from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.models.transaction import Transaction
from app.schemas.transaction import TransactionCreate, TransactionResponse, FinancialSummary
from app.core.security import get_current_user
from app.models.user import User
from typing import List, Optional
from app.services.finance import calculate_summary, calculate_monthly_summary, summary_by_category
from datetime import date
from sqlalchemy import extract
from app.services.transaction_service import TransactionService

router = APIRouter(prefix="/transactions", tags=["Transactions"])

@router.post("/", response_model=TransactionResponse)
def create_transaction(
    transaction: TransactionCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    service = TransactionService(db)

    data = transaction.model_dump()
    data["user_id"] = current_user.id

    return service.create_transaction(data)

@router.get("/", response_model=list[TransactionResponse])
def list_transactions(
    limit: int = 10,
    offset: int = 0,
    month: int | None = None,
    year: int | None = None,
    category_id: int | None = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    service = TransactionService(db)

    return service.list_transactions(
        current_user.id,
        limit,
        offset,
        month,
        year,
        category_id
    )

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

@router.get("/summary/category")
def get_summary_by_category(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return summary_by_category(db, current_user.id)