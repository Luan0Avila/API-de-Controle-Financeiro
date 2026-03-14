from sqlalchemy.orm import Session
from sqlalchemy import extract
from app.models.transaction import Transaction

class TransactionRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(self, data: dict):
        transaction = Transaction(**data)
        self.db.add(transaction)
        self.db.commit()
        self.db.refresh(transaction)
        return transaction

    def list_by_user(
        self,
        user_id: int,
        limit: int,
        offset: int,
        month=None,
        year=None,
        category_id=None
    ):
        query = self.db.query(Transaction).filter(
            Transaction.user_id == user_id
        )

        if month and year:
            query = query.filter(
                extract("month", Transaction.date) == month,
                extract("year", Transaction.date) == year
            )

        if category_id:
            query = query.filter(
                Transaction.category_id == category_id
            )

        query = query.order_by(Transaction.date.desc())

        return query.offset(offset).limit(limit).all()