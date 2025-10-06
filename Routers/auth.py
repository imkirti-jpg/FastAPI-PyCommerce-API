from fastapi import APIRouter, Depends, status, Header , HTTPException
from sqlalchemy.orm import Session
from Services.auth import AuthService
from database import get_db
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from Schemas.auth import UserOut, Signup
from core.security import verify_password, create_access_token , get_password_hash
from models import User
routers = APIRouter(prefix="/auth", tags=["Auth"])

# Login
@routers.post("/signup", status_code=status.HTTP_200_OK, response_model=UserOut)
def UserSignup(user: Signup , db: Session = Depends(get_db)):
    new_user = AuthService.signup(user, db)
    return  UserOut(data=new_user)

# Signup
@routers.post("/login", status_code=status.HTTP_200_OK)
def UserLogin(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):

    return AuthService.login(user_credentials, db)

# Refresh Token
@routers.post("/refresh-token", status_code=status.HTTP_200_OK) 
def refresh_token(token: str = Header(), db: Session = Depends(get_db)):
    return AuthService.get_refreshed_token(token,db)
