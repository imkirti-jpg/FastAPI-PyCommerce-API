from fastapi import APIRouter, Depends, Query, status
from database import get_db
from Services.carts import CartService
from sqlalchemy.orm import Session
from Schemas.carts import CartCreate, CartUpdate, CartOut, CartOutDelete, CartsOutList, CartBase ,CartOutBase
from core.security import get_current_user , check_admin_role
from fastapi.security import HTTPBearer 
from fastapi.security.http import HTTPAuthorizationCredentials

routers= APIRouter(prefix="/carts", tags=["Carts"])
auth_scheme = HTTPBearer()

@routers.get("/{cart_id}", status_code=status.HTTP_200_OK, response_model=CartOut)
def get_cart(
        cart_id: int,
        db: Session = Depends(get_db),
        token: HTTPAuthorizationCredentials = Depends(auth_scheme)):
    carts = CartService.get_cart(token, db, cart_id)
    created = CartBase.model_validate(carts, from_attributes=True)
    return CartOut(data=created)

@routers.post("/", status_code=status.HTTP_201_CREATED, response_model=CartOut)
def create_cart(
        cart: CartCreate,
        db: Session = Depends(get_db),
        token: HTTPAuthorizationCredentials = Depends(auth_scheme)):
    carts = CartService.create_cart(token, db, cart)
    created = CartBase.model_validate(carts, from_attributes=True)
    return CartOut(data=created)
    

@routers.put("/{cart_id}", status_code=status.HTTP_200_OK, response_model=CartOut)
def update_cart(
        cart_id: int,
        cart: CartUpdate,
        db: Session = Depends(get_db),
        token: HTTPAuthorizationCredentials = Depends(auth_scheme)):
    carts = CartService.update_cart(token, db, cart_id, cart)
    updated = CartBase.model_validate(carts, from_attributes=True)
    return CartOut(data=updated)

@routers.delete("/{cart_id}", status_code=status.HTTP_200_OK, response_model=CartOutDelete)
def delete_cart(
        cart_id: int,
        db: Session = Depends(get_db),
        token: HTTPAuthorizationCredentials = Depends(auth_scheme)):
    carts = CartService.delete_cart(token, db, cart_id)
    deleted = CartOutBase.model_validate(carts, from_attributes=True)
    return CartOutDelete(data=deleted)
    