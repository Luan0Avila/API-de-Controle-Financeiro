from fastapi import FastAPI

app = FastAPI(title="Controle Financeiro API")

@app.get("/")
def home():
    return {"status":"ok"}