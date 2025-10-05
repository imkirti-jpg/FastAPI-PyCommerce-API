from pydantic import BaseModel , field_validator
from typing import List, Optional , ClassVar

class CatergoryBase(BaseModel):
    id: int
    name: str

class CatergoryCreate(CatergoryBase):
    name : str

class CatergoryUpdate(BaseModel):
    name : str

class CatergoryOut(BaseModel):
    data: CatergoryBase

    model_config = {
    "from_attributes": True
}


class Catergoriesout(BaseModel):
    data: List[CatergoryBase]

class CategoryDelete(BaseModel):
    id: int
    name: str

class Catergoryoutdelete(BaseModel):
    data: CategoryDelete