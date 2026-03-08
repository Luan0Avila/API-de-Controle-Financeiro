from fastapi import FastAPI
from app.database.session import engine
from app.database.base import Base
from app.models import user, transaction
from app.routes import transactions, auth, category


app = FastAPI(title="Controle Financeiro API")

@app.get("/")
def home():
    return {"status":"ok"}

app.include_router(transactions.router)
app.include_router(auth.router)
app.include_router(category.router)

