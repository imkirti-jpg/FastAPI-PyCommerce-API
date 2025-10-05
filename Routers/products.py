from fastapi import APIRouter, HTTPException, Depends, status 
from sqlalchemy.orm import Session
from database import get_db
from Services.products import ProductService
from Schemas.products import ProductCreate, ProductUpdate , ProductOut , ProductDelete , Productsout , ProductBase , ProductOutDelete
from core.security import check_admin_role , get_current_user
from models import User 

routers = APIRouter(prefix="/products", tags=["Products"])

# get all products
@routers.get("/", status_code= status.HTTP_200_OK, response_model=Productsout,dependencies=[Depends(get_current_user)])
def get_all_products(db: Session = Depends(get_db)):
    products = ProductService.get_all_products(db)
    products_data = [
        ProductBase.model_validate(p, from_attributes=True)
        for p in products
    ]
    return Productsout(data=products_data)

# get single product
@routers.get("/{product_id}", status_code=status.HTTP_200_OK, response_model=ProductOut,dependencies=[Depends(get_current_user)])
def get_product(product_id: int, db: Session= Depends(get_db)):
    product = ProductService.get_product(db, product_id)
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    product_data = ProductBase.model_validate(product,from_attributes=True)
    return ProductOut(data=product_data)

# create product
@routers.post("/", status_code=status.HTTP_201_CREATED, response_model=ProductOut, dependencies=[Depends(check_admin_role)])
def create_product(product: ProductCreate, db: Session= Depends(get_db)):
    new_product = ProductService.create_product(db, product)
    db.refresh(new_product)
    # Validate and serialize the SQLAlchemy instance
    product_data = ProductBase.model_validate(new_product, from_attributes=True)
    return ProductOut(data=product_data)

@routers.put("/{product_id}", status_code=status.HTTP_200_OK, response_model=ProductOut, dependencies=[Depends(check_admin_role)])
def update_product(product_id: int , product: ProductUpdate , db: Session = Depends(get_db)):
    updated_product = ProductService.update_product(db, product_id, product)
    if not updated_product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    db.refresh(updated_product)  # Ensure relationships are loaded
    product_data = ProductBase.model_validate(updated_product, from_attributes=True)
    return ProductOut(data=product_data)

@routers.delete("/{product_id}", status_code=status.HTTP_200_OK, response_model=ProductOutDelete, dependencies=[Depends(check_admin_role)])
def delete_product(product_id: int , db: Session = Depends(get_db)):
    deleted_product = ProductService.delete_product(db,product_id)
    if not deleted_product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found") # Ensure relationships are loaded
    deleted_product = ProductDelete.model_validate(deleted_product, from_attributes=True)
    return ProductOutDelete(message="Product Deleted",data=deleted_product)