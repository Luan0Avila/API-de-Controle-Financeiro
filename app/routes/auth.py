from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import timedelta

from app.database.session import get_db
from app.models.user import User
from app.schemas.user import UserCreate, UserLogin
from app.core.security import hash_password, verify_password, create_acess_token
from app.core.config import ACCES_TOKEN_EXPIE_MINUTES

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    exists = db.query(User).filter(User.email == User.email).first()
    if exists:
        raise HTTPException(status_code=400, detail="E-mail já cadastrado")

    new_user = User(
        email=user.email,
        password=hash_password(user.password))
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message": "Usuário criado com sucesso"}

@router.post("/login")
def login(user:UserLogin, db:Session=Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email)

    if not db_user or not verify_password(user.password, db_user.password):
        raise HTTPException(status_code=401, detail="Credenciais inválidas")

    access_token = create_acess_token(data={"sub": str(db_user.id)},
        expires_delta=timedelta(minutes=ACCES_TOKEN_EXPIE_MINUTES))

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }
