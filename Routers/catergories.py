from fastapi import APIRouter, HTTPException, Depends, status 
from sqlalchemy.orm import Session
from database import get_db
from Services.catergories import CatergoryService
from Schemas.catergories import CatergoryBase, CatergoryCreate , Catergoryoutdelete , Catergoriesout , CatergoryOut, CatergoryUpdate, CategoryDelete
from typing import List
from core.security import check_admin_role , get_current_user

routers = APIRouter(prefix="/catergories", tags=["Catergories"])


# get all catergories
@routers.get("/", status_code= status.HTTP_200_OK, response_model=Catergoriesout,dependencies=[Depends(get_current_user)])
def get_all_catergories(db: Session = Depends(get_db)):
    catergories = CatergoryService.get_all_catergories(db)
    catergories_data = [CatergoryBase.model_validate(p, from_attributes=True) for p in catergories]
    return Catergoriesout(data=catergories_data)

# get single catergory
@routers.get("/{catergory_id}", status_code=status.HTTP_200_OK, response_model=CatergoryOut,dependencies=[Depends(get_current_user)])
def get_catergory(catergory_id: int, db: Session= Depends(get_db)):
    catergory = CatergoryService.get_catergory(db, catergory_id)
    if not catergory:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Catergory not found")
    catergories_data = CatergoryBase.model_validate(catergory, from_attributes=True)
    return CatergoryOut(data=catergories_data)

# create catergory
@routers.post("/", status_code=status.HTTP_201_CREATED, response_model=CatergoryOut, dependencies=[Depends(check_admin_role)])
def create_catergory(catergory: CatergoryCreate, db: Session  = Depends(get_db)):
    new_catergory = CatergoryService.create_catergory(db, catergory)
    catergorys_data = CatergoryBase.model_validate(new_catergory, from_attributes=True)
    return CatergoryOut(data=catergorys_data)  

# update catergory
@routers.put("/{catergory_id}", status_code=status.HTTP_200_OK, response_model=CatergoryUpdate, dependencies=[Depends(check_admin_role)])
def update_catergory(catergory_id: int , catergory: CatergoryUpdate , db: Session = Depends(get_db)):
    updated_catergory = CatergoryService.update_catergory(db, catergory_id, catergory)
    if not updated_catergory:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Catergory not found")
    return updated_catergory

# delete catergory
@routers.delete("/{catergory_id}", status_code=status.HTTP_200_OK, response_model=Catergoryoutdelete, dependencies=[Depends(check_admin_role)])
def delete_catergory(catergory_id: int , db: Session = Depends  (get_db)):
    deleted_catergory = CatergoryService.delete_catergory(db,catergory_id)
    if not deleted_catergory:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Catergory not found")
    catergorys_data = CategoryDelete.model_validate(deleted_catergory, from_attributes=True)
    return Catergoryoutdelete(data=catergorys_data)
