from fastapi import APIRouter, Depends
from database import get_db
from Services.accounts import AccountService
from sqlalchemy.orm import Session
from fastapi.security import HTTPBearer
from Schemas.accounts import AccountOut, AccountUpdate , AccountBase
from fastapi.security import HTTPBearer
from core.security import auth_scheme , check_admin_role
from fastapi.security.http import HTTPAuthorizationCredentials

routers = APIRouter(prefix="/accounts", tags=["Accounts"])
auth_scheme = HTTPBearer()

@routers.get("/me", status_code=200, response_model=AccountOut)
def get_my_info(
        db: Session = Depends(get_db),
        token: HTTPAuthorizationCredentials = Depends(auth_scheme)):
    user = AccountService.get_my_info(db, token.credentials)
    created = AccountBase.model_validate(user, from_attributes=True)
    return AccountOut(message="User retrieved successfully", data=created)

@routers.put("/me", status_code=200, response_model=AccountOut)
def edit_my_info(
        user: AccountUpdate,
        db: Session = Depends(get_db),
        token: HTTPAuthorizationCredentials = Depends(auth_scheme)):
    updated_user = AccountService.edit_my_info(db, token.credentials, user)
    created = AccountBase.model_validate(updated_user, from_attributes=True)
    return AccountOut(message="User updated successfully", data=created)

@routers.delete("/me", status_code=200,response_model=AccountOut)
def delete_my_account(
        db: Session = Depends(get_db),
        token: HTTPAuthorizationCredentials = Depends(auth_scheme)):
    result = AccountService.Delete_my_account(db, token.credentials)
    deleted = AccountBase.model_validate(result, from_attributes=True)
    return AccountOut(message="User deleted successfully", data=deleted)