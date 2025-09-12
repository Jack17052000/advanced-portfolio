from pydantic import BaseModel

# Schema para leer productos
class ProductBase(BaseModel):
    name: str
    stock: int = 0

class ProductCreate(ProductBase):
    pass

class ProductResponse(ProductBase):
    id: int

    class Config:
        orm_mode = True
