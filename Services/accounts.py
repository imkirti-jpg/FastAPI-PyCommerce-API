from sqlalchemy.orm import Session
from models import User
from fastapi import HTTPException
from core.security import get_password_hash, get_token_payload , get_current_user, verify_password

class AccountService:
    @staticmethod
    def get_my_info(db: Session, token: str):
        user_id = get_token_payload(token).get("id")
        
        user = db.query(User).filter(User.id == user_id).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user

    @staticmethod
    def edit_my_info(db: Session, token: str, user):
        user_id = get_token_payload(token).get("id")
        users = db.query(User).filter(User.id == user_id).first()
        if users is None:
            raise HTTPException(status_code=404, detail="User not found")
        
        update_data = user.model_dump(exclude_unset=True)

        if update_data.get("new_password"):
            if not update_data.get("old_password"):
                raise HTTPException(status_code=400, detail="Old password is required to set a new one")
            
            if not verify_password(update_data["old_password"], users.password):
                raise HTTPException(status_code=400, detail="Old password is incorrect")
        
            update_data["password"] = get_password_hash(update_data["new_password"])

            update_data.pop("old_password", None)
            update_data.pop("new_password", None)
        
        for key, value in user.model_dump().items():
            setattr(users, key, value)

        db.commit()
        db.refresh(users)
        return users
    
    @staticmethod
    def Delete_my_account(db: Session, token: str):
        user_id = get_token_payload(token).get("id")
        user = db.query(User).filter(User.id == user_id).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        
        db.delete(user)
        db.commit()
        return user