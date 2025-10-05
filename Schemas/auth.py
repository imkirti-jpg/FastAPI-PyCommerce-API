from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import List
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

class Signup(BaseModel):
    full_name: str
    username: str
    email: str
    password: str

    model_config = {
    "from_attributes": True
    }

class UserOut(BaseModel):
    data: UserBase

    model_config = {
    "from_attributes": True
    }

# Token
class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = 'Bearer'
    expires_in: int