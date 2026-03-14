from sqlalchemy.orm import Session
from sqlalchemy import func, extract
from app.models.transaction import Transaction
from app.models.category import Category

def monthly_balance(db: Session, user_id: int, year: int):

    results = db.query(
        extract("month", Transaction.date).label("month"),
        Transaction.type,
        func.sum(Transaction.value)
    ).filter(
        Transaction.user_id == user_id,
        extract("year", Transaction.date) == year
    ).group_by(
        "month",
        Transaction.type
    ).all()

    data = {}

    for month, t_type, total in results:
        month = int(month)

        if month not in data:
            data[month] = {"income": 0, "expense": 0}

        data[month][t_type] = total

    return [
        {
            "month": month,
            "income": values["income"],
            "expense": values["expense"],
            "balance": values["income"] - values["expense"]
        }
        for month, values in sorted(data.items())
    ]


def expense_by_category(db: Session, user_id: int):

    results = db.query(
        Category.name,
        func.sum(Transaction.value)
    ).join(Transaction).filter(
        Transaction.user_id == user_id,
        Transaction.type == "expense"
    ).group_by(Category.name).all()

    return [
        {"catgory": name, "total": total}
        for name, total in results
    ]

def income_vs_expense(db: Session, user_id: int):

    income = db.query(func.sum(Transaction.value)).filter(
        Transaction.user_id == user_id,
        Transaction.type == "income"
    ).scalar() or 0

    expense = db.query(func.sum(Transaction.value)).filter(
        Transaction.user_id == user_id,
        Transaction.type == "expense"
    ).scalar() or 0

    return {
        "income": income,
        "expense": expense,
        "balance": income - expense
    }