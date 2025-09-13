from pydantic import BaseModel, EmailStr
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

# Schemas de usuarios
class UserBase(BaseModel):
    name: str
    email: EmailStr

class UserCreate(UserBase):
    role: str = "user"
    active: bool = True

class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    role: Optional[str] = None
    active: Optional[bool] = None

class UserResponse(UserBase):
    id: int
    role: str
    active: bool

    class Config:
        orm_mode = True
