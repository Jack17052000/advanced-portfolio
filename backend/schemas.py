from pydantic import BaseModel
from typing import Optional

# Schema para leer productos
class ProductBase(BaseModel):
    name: str
    stock: int = 0

class ProductCreate(ProductBase):
    pass

class ProductUpdate(BaseModel):
    name: Optional[str] = None
    stock: Optional[int] = None

class ProductResponse(ProductBase):
    id: int

    class Config:
        orm_mode = True
