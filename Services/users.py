from sqlalchemy.orm import Session
from models import User
from Schemas.users import UserCreate, UserUpdate
from core.security import get_password_hash
from fastapi import HTTPException, status

class UserService:
    @staticmethod
    def get_all_users(db: Session):
        users = db.query(User).all()
        return users
    
    @staticmethod
    def get_user(db: Session, user_id: int):
        user = db.query(User).filter(User.id == user_id).first()
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        return user
    
    @staticmethod
    def create_user(db: Session, user : UserCreate):
        print("Password type:", type(user.password), "value:", user.password)
        print(type(user.password), user.password)

        hashed_password= get_password_hash(str(user.password))
        user.password = hashed_password
        db_user = User(**user.model_dump(exclude={'id'}))
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    
    @staticmethod
    def update_user(db: Session, user_id: int, user: UserUpdate):
        db_user = db.query(User).filter(User.id == user_id).first()
        if not db_user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        
        for key , value in user.model_dump().items():
            setattr(db_user, key, value)

        db.commit()
        db.refresh(db_user)
        return db_user
    
    @staticmethod
    def delete_user(db: Session, user_id: int):
        db_user = db.query(User).filter(User.id == user_id).first()
        if not db_user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        
        db.delete(db_user)
        db.commit()
        return db_user