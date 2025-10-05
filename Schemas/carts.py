from pydantic import BaseModel, Field
from typing import List
from datetime import datetime
from Schemas.products import ProductBase
from Schemas.catergories import CatergoryBase


class ProductBaseCart(ProductBase):
    category: CatergoryBase = Field(exclude=True)

    model_config = {    
    "from_attributes": True
    }


# Base Cart & Cart_Item
class CartItemBase(BaseModel):
    id: int
    product_id: int
    quantity: int
    subtotal: float
    product: ProductBaseCart


class CartBase(BaseModel):
    id: int
    user_id: int
    added_at: datetime
    total_amount: float
    cart_items: List[CartItemBase]

    model_config = {
    "from_attributes": True 
    }


class CartOutBase(BaseModel):
    id: int
    user_id: int
    added_at: datetime
    total_amount: float
    cart_items: List[CartItemBase]

    model_config = {
    "from_attributes": True 
    }




# Get Cart
class CartOut(BaseModel):
    data: CartBase

    model_config = {
    "from_attributes": True
    }


class CartsOutList(BaseModel):
    data: List[CartBase]


class CartsUserOutList(BaseModel):
    data: List[CartBase]

    model_config = {
    "from_attributes": True
    }



# Delete Cart
class CartOutDelete(BaseModel):
    data: CartOutBase


# Create Cart
class CartItemCreate(BaseModel):
    product_id: int
    quantity: int


class CartCreate(BaseModel):
    cart_items: List[CartItemCreate]

    model_config = {
    "from_attributes": True
    }


# Update Cart
class CartUpdate(CartCreate):
    pass


