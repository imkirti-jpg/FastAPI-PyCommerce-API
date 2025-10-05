from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import List, Optional
from Schemas.carts import CartBase


class AccountBase(BaseModel):
    id: int
    username: str
    email: EmailStr
    full_name: str
    role: str
    is_active: bool
    created_at: datetime
    carts: List[CartBase]

    model_config = {
        "from_attributes": True
    }

class AccountUpdate(BaseModel):
    username: str
    email: EmailStr
    full_name: str
    old_password: Optional[str] = None
    new_password: Optional[str] = None

    model_config = {
        "from_attributes": True
    }

class AccountOut(BaseModel):
    message: str
    data: AccountBase
    
    model_config = {
        "from_attributes": True
    }   
