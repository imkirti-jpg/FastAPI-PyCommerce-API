from pydantic import BaseModel , field_validator
from typing import List, Optional , ClassVar
from datetime import datetime
from Schemas.catergories import CatergoryBase

class BaseConfig:
    from_attributes = True


class ProductBase(BaseModel):
    title: str
    description: str
    price: int
    discount_percentage: float

    @field_validator('discount_percentage')
    def validate_discount_percentage(cls, v):
        if not (0 <= v <= 100):
            raise ValueError('discount_percentage must be between 0 and 100')
        return v

    rating: float
    stock: int
    brand: str
    thumbnail: str
    images: List[str]
    is_published: Optional[bool] = True
    created_at: Optional[datetime] = None
    category: CatergoryBase

    model_config = {
    "from_attributes": True
}


class ProductCreate(ProductBase):
    id: ClassVar[int]
    category: ClassVar[CatergoryBase]
    category_id: int
    

    model_config = {
    "from_attributes": True
}


class ProductUpdate(ProductCreate):
    pass

# get products
class ProductOut(BaseModel):
    data: ProductBase

    model_config = {
    "from_attributes": True
}


class Productsout(BaseModel):
    data: List[ProductBase]
    
    model_config = {
    "from_attributes": True
}


# delete product
class ProductDelete(BaseModel):
    category: ClassVar[CatergoryBase]


class ProductOutDelete(BaseModel):
    message: str
    data: ProductDelete
