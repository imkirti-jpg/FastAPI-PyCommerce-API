from pydantic import BaseModel, Field
from typing import List, Optional , Annotated 
from database import Base
from sqlalchemy import Column, Integer, String, Float, Boolean, TIMESTAMP, text , ForeignKey , Enum
from sqlalchemy.dialects.postgresql import ARRAY 
from sqlalchemy.orm import relationship 
from sqlalchemy.orm import Mapped, mapped_column

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True, unique=True, nullable=False)
    username: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String, nullable=False)
    full_name: Mapped[str] = mapped_column(String, nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, server_default="True", nullable=False)
    created_at: Mapped[str] = mapped_column(TIMESTAMP(timezone=True), server_default=text("NOW()"), nullable=False)
    role: Mapped[str] = mapped_column(Enum("admin", "user", name="user_roles"), server_default="user", nullable=False)

    # Relationship with carts
    carts: Mapped[list["Cart"]] = relationship("Cart", back_populates="user", cascade="all, delete-orphan")

class Cart(Base):
    __tablename__ = "carts"
    id : Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False, unique=True, autoincrement=True)
    user_id : Mapped[int] = mapped_column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    added_at : Mapped[str] = mapped_column(TIMESTAMP(timezone=True), server_default=text("NOW()"), nullable=False)
    total_amount : Mapped[float] = mapped_column(Float, nullable=False)

    # Relationships
    user = relationship("User", back_populates="carts")

    # Relationship with cart items
    cart_items = relationship("CartItem", back_populates="cart",cascade="all, delete-orphan")

class CartItem(Base):
    __tablename__ = "cart_items"
    id = Column(Integer, primary_key=True, nullable=False, unique=True, autoincrement=True)
    cart_id = Column(Integer, ForeignKey("carts.id", ondelete="CASCADE"), nullable=False)
    product_id = Column(Integer, ForeignKey("products.id", ondelete="CASCADE"), nullable=False)
    quantity = Column(Integer, nullable=False)
    subtotal = Column(Float, nullable=False)


    # Relationships
    cart = relationship("Cart", back_populates="cart_items")
    product = relationship("Product", back_populates="cart_items")


class Catergory(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True, nullable=False, unique=True, autoincrement=True)
    name = Column(String, nullable=False, unique=True)  
    #relationship with [products] table
    products = relationship("Product", back_populates="category")

class Product(Base):
    __tablename__ = "products"
   
    id = Column(Integer, primary_key=True, nullable=False, unique=True, autoincrement=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    discount_percentage = Column(Float, nullable=False)
    rating = Column(Float, nullable=False)
    stock = Column(Integer, nullable=False)
    brand = Column(String, nullable=False)
    thumbnail = Column(String, nullable=False)
    images = Column(ARRAY(String), nullable=False)
    is_published = Column(Boolean, server_default="True", nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text("NOW()"), nullable=False)

    # Relationship with category
    category_id = Column(Integer, ForeignKey("categories.id", ondelete="CASCADE"), nullable=False)
    category = relationship("Catergory", back_populates="products")

    # Relationship with cart items
    cart_items = relationship("CartItem", back_populates="product")