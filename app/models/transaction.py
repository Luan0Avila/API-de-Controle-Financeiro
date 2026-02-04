from sqlalchemy import Column, Integer, String, Float, ForeignKey
from app.database.base import Base

class Transaction(Base):
    __tablename__= "transactions"


    id = Column(Integer, primary_key=True)
    description = Column(String)
    value = Column(Float)
    type = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))