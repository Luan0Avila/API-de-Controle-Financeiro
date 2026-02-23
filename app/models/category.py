from sqlalchemy import Column,Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database.base import Base

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("user.id"))

    trasactions = relationship("Transaction", backref="category")