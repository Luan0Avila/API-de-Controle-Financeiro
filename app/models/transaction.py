from sqlalchemy import Column, Integer, String, Float, ForeignKey, Date
from app.database.base import Base
from datetime import date

class Transaction(Base):
    __tablename__= "transactions"


    id = Column(Integer, primary_key=True)
    description = Column(String)
    value = Column(Float)
    type = Column(String)
    date = Column(Date, default=date.today)
    user_id = Column(Integer, ForeignKey("users.id"))