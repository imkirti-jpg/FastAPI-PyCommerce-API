from pydantic import BaseModel , EmailStr
from typing import List
from datetime import datetime
from Schemas.carts import CartBase


class UserBase(BaseModel):
    id: int
    username: str
    email: EmailStr
    full_name: str
    password: str
    role: str
    is_active: bool
    created_at: datetime
    carts: List[CartBase]

    model_config = {
    "from_attributes": True     
    }

class UserCreate(BaseModel):
    full_name: str
    username: str
    email: str
    password: str

    model_config = {
    "from_attributes": True 
    }

class UserUpdate(UserCreate):
    pass    

class UserOut(BaseModel):
    data: UserBase

    model_config = {
    "from_attributes": True 
    }

class Usersout(BaseModel):
    data: List[UserBase]

    model_config = {
    "from_attributes": True 
    }

class UseroutDelete(BaseModel):
    data: UserBase

    model_config = {
    "from_attributes": True 
    }
