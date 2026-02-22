from sqlalchemy.orm import Session
from sqlalchemy import func, extract
from app.models.transaction import Transaction

def calculate_summary(db: Session, user_id: int):
    income = db.query(func.sum(Transaction.value)).filter(
        Transaction.user_id == user_id,
        Transaction.type == "income"
    ).scalar() or 0

    expense = db.query(func.sum(Transaction.value)).filter(
        Transaction.user_id == user_id,
        Transaction.type == "expense"
    ).scalar() or 0
    
    balance = income - expense

    return {
        "total_income": income,
        "total_expense": expense,
        "balance": balance
    }


def calculate_monthly_summary(db: Session, user_id: int, month: int, year: int):
    income = db.query(func.sum(Transaction.value)).filter(
        Transaction.user_id == user_id,
        Transaction.type == "income",
        extract("month", Transaction.date) == month,
        extract("year", Transaction.date) == year
    ).scalar() or 0

    expense = db.query(func.sum(Transaction.value)).filter(
        Transaction.user_id == user_id,
        Transaction.type == "expense",
        extract("month", Transaction.date) == month,
        extract("year", Transaction.date) == year
    ).scalar() or 0

    balance = income - expense

    return {
        "total_income": income,
        "total_expense": expense,
        "balance": balance
    }