from fastapi.security.http import HTTPAuthorizationCredentials
from passlib.context import CryptContext
from datetime import datetime, timedelta , timezone
from core.config import settings
from jose import JWTError, jwt
from Schemas.auth import TokenResponse
from fastapi.encoders import jsonable_encoder
from fastapi import HTTPException, Depends, status
from models import User
from sqlalchemy.orm import Session
from fastapi.security import HTTPBearer
from database import get_db
from typing import Optional

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
auth_scheme = HTTPBearer()

# Create Hash Password
def get_password_hash(password):
    password = str(password)
    return pwd_context.hash(password)


# Verify Hash Password
def verify_password(plain_password, hashed_password):
    
    return pwd_context.verify(plain_password, hashed_password)

# Create Access Token
def get_user_token(id: int, refresh_token=None):
    payload = {"id": id}

    access_token_expiry = timedelta(minutes=settings.access_token_expire_minutes)

    access_token = create_access_token(payload, access_token_expiry)

    if not refresh_token:
        refresh_token = create_refresh_token(payload)

    return TokenResponse(
        access_token=access_token,
        refresh_token=refresh_token,
        token_type='Bearer',
        expires_in=int(access_token_expiry.seconds)
    )

# Create Access Token
def create_access_token(data: dict, access_token_expiry=None):
    payload = data.copy()

    expire = datetime.now(timezone.utc) + timedelta(minutes=settings.access_token_expire_minutes)
    payload.update({"exp": expire})

    return jwt.encode(payload, settings.secret_key, settings.algorithm)



# Create Refresh Token
def create_refresh_token(data):
    return jwt.encode(data, settings.secret_key, settings.algorithm)

# Get Payload Of Token
def get_token_payload(token):
    try:
        return jwt.decode(token, settings.secret_key, algorithms=[settings.algorithm])
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
        )


def get_current_user(token):
    user = get_token_payload(token.credentials)
    return user.get('id')


def check_admin_role(
        token: HTTPAuthorizationCredentials = Depends(auth_scheme),
        db: Session = Depends(get_db)):
    user = get_token_payload(token.credentials)
    user_id = user.get('id')
    role_user = db.query(User).filter(User.id == user_id).first()
    if role_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")


    if str(role_user.role) != "admin":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Admin role required")
