from fastapi import FastAPI
from app.routes import transactions

app = FastAPI(title="Controle Financeiro API")

@app.get("/")
def home():
    return {"status":"ok"}

app.include_router(transactions.router)