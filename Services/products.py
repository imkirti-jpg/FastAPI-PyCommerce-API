from sqlalchemy.orm import Session
from models import Product
from Schemas.products import ProductCreate, ProductUpdate
from models import Catergory as Category
from fastapi import HTTPException, status

class ProductService:
    @staticmethod
    def get_product(db: Session, product_id: int):
        product = db.query(Product).filter(Product.id == product_id).first()
        if not product:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
        return product
        
    @staticmethod
    def get_all_products(db: Session):
        products = db.query(Product).all()
        return products
    
    @staticmethod
    def create_product(db: Session, product: ProductCreate):
        category_exists = db.query(Category).filter(Category.id == product.category_id).first()
        if not category_exists:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Category does not exist")
        db_product = Product(**product.model_dump(exclude={'id'}))
        db.add(db_product)
        db.commit()
        db.refresh(db_product)
        return db_product
    
    
    @staticmethod   
    def update_product(db: Session, product_id: int, product: ProductUpdate):
        db_product = db.query(Product).filter(Product.id == product_id).first()
        if not db_product:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")  
        
        for key , value in product.model_dump(exclude_unset=True).items():
            setattr(db_product, key, value)

        db.commit()
        db.refresh(db_product)
        return db_product
    
    @staticmethod
    def delete_product(db: Session, product_id: int):
        db_product = db.query(Product).filter(Product.id == product_id).first()
        if not db_product:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
        
        db.delete(db_product)
        db.commit()
        return db_product