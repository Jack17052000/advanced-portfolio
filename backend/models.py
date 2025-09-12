from sqlalchemy import Column, Integer, String
from .database import Base

# Modelo de productos
class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    stock = Column(Integer, default=0)
