from fastapi import APIRouter, Depends, Query, status
from database import get_db
from Services.users import UserService
from sqlalchemy.orm import Session
from Schemas.users import UserCreate, UserOut, Usersout,  UserUpdate  , UseroutDelete , UserBase
from core.security import check_admin_role

routers= APIRouter(prefix="/users", tags=["Users"])


# get all users
@routers.get("/", status_code=status.HTTP_200_OK, response_model=Usersout, dependencies=[Depends(check_admin_role)])
def get_all_users(db: Session= Depends(get_db)):
    users = UserService.get_all_users(db)
    users_data = [
        UserBase.model_validate(u, from_attributes=True)
        for u in users
    ]
    return Usersout(data=users_data)

# get single user
@routers.get("/{user_id}", status_code=status.HTTP_200_OK, response_model=UserOut, dependencies=[Depends(check_admin_role)])
def get_user(user_id: int , db: Session= Depends(get_db)):
    user = UserService.get_user(db, user_id)
    if not user:
        return {"message": "User not found"}
    user_data = UserBase.model_validate(user, from_attributes=True)
    return UserOut(data=user_data)

# create user
@routers.post("/", status_code=status.HTTP_201_CREATED, response_model=UserOut )
def create_user(user: UserCreate , db: Session= Depends(get_db)):
    new_user = UserService.create_user(db, user)
    db.refresh(new_user)
    user_data = UserBase.model_validate(new_user, from_attributes=True)
    return UserOut(data=user_data)

# update user
@routers.put("/{user_id}", status_code=status.HTTP_200_OK, response_model=UserOut, dependencies=[Depends(check_admin_role)] )
def update_user(user_id: int , user: UserUpdate , db: Session = Depends(get_db)):
    updated_user = UserService.update_user(db, user_id, user)
    if not updated_user:
        return {"message": "User not found"}
    db.refresh(updated_user)
    user_data = UserBase.model_validate(updated_user, from_attributes=True)
    return UserOut(data=user_data)

# delete user
@routers.delete("/{user_id}", status_code=status.HTTP_200_OK, response_model=UseroutDelete , dependencies=[Depends(check_admin_role)])
def delete_user(user_id: int , db: Session = Depends(get_db)):
    deleted_user = UserService.delete_user(db,user_id)
    if not deleted_user:
        return {"message": "User not found"}
    deleted_user = UserBase.model_validate(deleted_user, from_attributes=True)
    return UseroutDelete(data=deleted_user)
