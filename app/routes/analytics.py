from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.core.security import get_current_user
from app.models.user import User

from app.services.analytics import(
    monthly_balance,
    expense_by_category,
    income_vs_expense
)

router = APIRouter(prefix="/analytics", tags=["Analytics"])

@router.get("/monthly-balance")
def get_monthly_balance(
    year: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return monthly_balance(db, current_user.id, year)

@router.get("/expense-by-category")
def get_expense_by_category(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return expense_by_category(db, current_user.id)


@router.get("/income-vs-expense")
def get_income_vs_expense(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return income_vs_expense(db, current_user.id)