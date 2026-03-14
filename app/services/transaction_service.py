from app.repositories.transaction_repository import TransactionRepository

class TransactionService:

    def __init__(self, db):
        self.repo = TransactionRepository(db)

    def create_transaction(self, data):
        return self.repo.create(data)

    def list_transactions(
        self,
        user_id,
        limit,
        offset,
        month=None,
        year=None,
        category_id=None
    ):
        return self.repo.list_by_user(
            user_id,
            limit,
            offset,
            month,
            year,
            category_id
        )