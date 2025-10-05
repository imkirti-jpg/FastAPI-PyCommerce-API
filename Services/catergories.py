from sqlalchemy.orm import Session
from models import Catergory
from Schemas.catergories import  CatergoryCreate , CatergoryUpdate
from fastapi import HTTPException, status



class CatergoryService:
    @staticmethod
    def get_catergory(db: Session, catergory_id: int):
        catergory = db.query(Catergory).filter(Catergory.id == catergory_id).first()
        if not catergory:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Catergory not found")
        return catergory
        
    @staticmethod
    def get_all_catergories(db: Session):
        catergories = db.query(Catergory).all()
        return catergories
    
    @staticmethod
    def create_catergory(db: Session, catergory: CatergoryCreate):
        db_catergory = Catergory(**catergory.model_dump(exclude={'id'}))
        existing = db.query(Catergory).filter(Catergory.name == catergory.name).first()
        if existing :
            raise HTTPException( status_code=status.HTTP_409_CONFLICT, detail="Category already exists")
        db.add(db_catergory)
        db.commit()
        db.refresh(db_catergory)
        return  db_catergory
    
    
    @staticmethod   
    def update_catergory(db: Session, catergory_id: int, catergory: CatergoryUpdate):
        db_catergory = db.query(Catergory).filter(Catergory.id == catergory_id).first()
        if not db_catergory:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Catergory not found")  
        
        for key , value in catergory.model_dump(exclude_unset=True).items():
            setattr(db_catergory, key, value)

        db.commit()
        db.refresh(db_catergory)
        return db_catergory
    
    @staticmethod
    def delete_catergory(db: Session, catergory_id: int):
        db_catergory = db.query(Catergory).filter(Catergory.id == catergory_id).first()
        if not db_catergory:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Catergory not found")
        
        db.delete(db_catergory)
        db.commit()
        return db_catergory