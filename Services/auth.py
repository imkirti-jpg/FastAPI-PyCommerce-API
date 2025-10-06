from fastapi import HTTPException, Depends, status
from fastapi.security.oauth2 import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from models import User
from database import get_db
from core.security import verify_password, get_user_token, get_token_payload , get_password_hash
from core.security import get_password_hash , get_password_hash as hash_password
from Schemas.auth import Signup
from typing import cast

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


class AuthService:
    @staticmethod 
    def login(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
        user = db.query(User).filter(User.username == user_credentials.username).first()

        if not user:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Credentials")
        
        if not verify_password(user_credentials.password,user.password):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Credentials")
            
        user_id = int(user.id)  
        return get_user_token(id=user_id)
        
    @staticmethod
    def signup(user: Signup, db: Session = Depends(get_db)):
        existing_user = db.query(User).filter(User.email == user.email).first()
        if existing_user:
            raise HTTPException(status_code=400, detail="Email already registered")
        if db.query(User).filter(User.username == user.username).first():
            raise HTTPException(status_code=400, detail="Username already taken")
        hashed_password = hash_password(user.password)
        user_data = user.model_dump()
        user_data["password"] = hashed_password 
        db_user = User(id=None, **user_data)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    
    @staticmethod
    def get_refreshed_token(token: str = Depends(oauth2_scheme), db   : Session = Depends(get_db)):
        payload = get_token_payload(token)
        user_id = payload.get('id', None)
        if not user_id:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Could not validate credentials")

        user = db.query(User).filter(User.id == user_id).first()
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

        return  get_user_token(id=cast(int,user.id), refresh_token=token)