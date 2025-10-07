from sqlalchemy.orm import Session
from models import Cart
from Schemas.carts import CartCreate, CartUpdate
from fastapi import HTTPException, status
from typing import List
from core.security import get_current_user
from models import Product, CartItem
from sqlalchemy.orm import joinedload


class CartService:
    @staticmethod
    def get_cart(token ,db: Session):
        user_id = get_current_user(token)  # get the logged-in user's ID
        cart = db.query(Cart).filter(Cart.user_id == user_id).first()  # fetch single cart
        if not cart:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Cart not found"
            )
        return cart

    @staticmethod
    def create_cart(token, db: Session, cart: CartCreate):
        user_id = get_current_user(token)
        cart_dict = cart.model_dump()
        existing_cart = db.query(Cart).filter(Cart.user_id == user_id).first()
        if existing_cart:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Cart already exists for this user")

        cart_items_data = cart_dict.pop("cart_items", [])
        cart_items = []
        total_amount = 0

        for item_data in cart_items_data:
            product_id = item_data['product_id']
            quantity = item_data['quantity']

            product = db.query(Product).filter(Product.id == product_id).first()
            if not product:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                    detail=f"Product with id {product_id} not found")

            # ✅ calculate subtotal correctly
            subtotal = quantity * (product.price - (product.price * product.discount_percentage / 100))

            cart_item = CartItem(product_id=product_id, quantity=quantity, subtotal=subtotal)
            total_amount += subtotal
            cart_items.append(cart_item)

        # ✅ only valid Cart fields here
        cart_db = Cart(cart_items=cart_items, user_id=user_id, total_amount=total_amount, **cart_dict)
        # ✅ link cart items
        cart_db.cart_items = cart_items

        db.add(cart_db)
        db.commit()
        db.refresh(cart_db)
        return cart_db

    
    @staticmethod
    def update_cart(token, db: Session, cart_id: int, cart: CartUpdate):
        user_id = get_current_user(token)

        cart = db.query(Cart).filter(Cart.id == cart_id, Cart.user_id == user_id).first()
        if not cart:
            return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cart not found")

        # Delete existing cart_items
        db.query(CartItem).filter(CartItem.cart_id == cart_id).delete()

        for item in cart.cart_items:
            product_id = item.product_id
            quantity = item.quantity

            product = db.query(Product).filter(Product.id == product_id).first()
            if not product:
                return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Product with id {product_id} not found")

            subtotal = quantity * product.price * (product.discount_percentage / 100)

            cart_item = CartItem(
                cart_id=cart_id,
                product_id=product_id,
                quantity=quantity,
                subtotal=subtotal
            )
            db.add(cart_item)

        cart.total_amount = sum(item.subtotal for item in cart.cart_items)

        db.commit()
        db.refresh(cart)
        return cart
    
    @staticmethod
    def delete_cart(token, db: Session, cart_id: int):
        user_id = get_current_user(token)
        cart = (
            db.query(Cart)
            .options(joinedload(Cart.cart_items).joinedload(CartItem.product))
            .filter(Cart.id == cart_id, Cart.user_id == user_id)
            .first()
        )
        if not cart:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cart not found")

        for cart_item in cart.cart_items:
            db.delete(cart_item)

        db.delete(cart)
        db.commit()
        return  cart

