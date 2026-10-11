import datetime
from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    Boolean,
    ForeignKey,
    DateTime,
    Text,
)
from sqlalchemy.orm import relationship
from backend.app.database.session import Base

class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    phone = Column(String, nullable=True)
    role = Column(String, default="customer") # "customer" or "admin"
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    addresses = relationship("Address", back_populates="user", cascade="all, delete-orphan")
    orders = relationship("Order", back_populates="user")

class Address(Base):
    __tablename__ = "addresses"

    id = Column(String, primary_key=True, index=True)
    user_id = Column(String, ForeignKey("users.id"))
    full_name = Column(String, nullable=False)
    street = Column(String, nullable=False)
    city = Column(String, nullable=False)
    state = Column(String, nullable=False)
    pincode = Column(String, nullable=False)
    phone = Column(String, nullable=False)

    user = relationship("User", back_populates="addresses")

class Category(Base):
    __tablename__ = "categories"

    id = Column(String, primary_key=True, index=True) # e.g. "namkeen", "sweets"
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)

    products = relationship("Product", back_populates="category")

class Product(Base):
    __tablename__ = "products"

    id = Column(String, primary_key=True, index=True)
    name = Column(String, nullable=False, index=True)
    hindi_name = Column(String, nullable=True)
    tagline = Column(String, nullable=False)
    description = Column(Text, nullable=False)
    long_description = Column(Text, nullable=True)
    category_id = Column(String, ForeignKey("categories.id"))
    flavor_profile = Column(String, default="crunchy") # "spicy", "sweet", "crunchy", "savory"
    spice_level = Column(Integer, default=1) # 1-5
    crunch_index = Column(Integer, default=90) # 0-100
    is_bestseller = Column(Boolean, default=False)
    image_key = Column(String, nullable=False)
    bg_theme = Column(String, default="#8B0000")
    accent_color = Column(String, default="#FFB703")

    category = relationship("Category", back_populates="products")
    variants = relationship("ProductVariant", back_populates="product", cascade="all, delete-orphan")
    reviews = relationship("Review", back_populates="product", cascade="all, delete-orphan")

class ProductVariant(Base):
    __tablename__ = "product_variants"

    id = Column(String, primary_key=True, index=True)
    product_id = Column(String, ForeignKey("products.id"))
    weight = Column(String, nullable=False) # e.g. "200g Pouch"
    price = Column(Float, nullable=False)
    original_price = Column(Float, nullable=True)
    sku = Column(String, unique=True, index=True)
    in_stock = Column(Boolean, default=True)
    stock_quantity = Column(Integer, default=100)

    product = relationship("Product", back_populates="variants")

class Cart(Base):
    __tablename__ = "carts"

    id = Column(String, primary_key=True, index=True)
    user_id = Column(String, ForeignKey("users.id"), nullable=True)
    session_id = Column(String, index=True, nullable=True)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

    items = relationship("CartItem", back_populates="cart", cascade="all, delete-orphan")

class CartItem(Base):
    __tablename__ = "cart_items"

    id = Column(String, primary_key=True, index=True)
    cart_id = Column(String, ForeignKey("carts.id"))
    product_id = Column(String, ForeignKey("products.id"))
    variant_id = Column(String, ForeignKey("product_variants.id"))
    quantity = Column(Integer, default=1)

    cart = relationship("Cart", back_populates="items")
    product = relationship("Product")
    variant = relationship("ProductVariant")

class Order(Base):
    __tablename__ = "orders"

    id = Column(String, primary_key=True, index=True)
    order_number = Column(String, unique=True, index=True, nullable=False)
    user_id = Column(String, ForeignKey("users.id"), nullable=True)
    status = Column(String, default="confirmed") # confirmed, roasted_packed, dispatched, out_for_delivery, delivered
    subtotal = Column(Float, nullable=False)
    discount = Column(Float, default=0.0)
    shipping = Column(Float, default=0.0)
    tax = Column(Float, default=0.0)
    total = Column(Float, nullable=False)
    payment_method = Column(String, nullable=False)
    tracking_number = Column(String, nullable=False)
    estimated_delivery = Column(String, nullable=False)
    
    # Shipping info snapshot
    shipping_full_name = Column(String, nullable=False)
    shipping_email = Column(String, nullable=False)
    shipping_phone = Column(String, nullable=False)
    shipping_street = Column(String, nullable=False)
    shipping_city = Column(String, nullable=False)
    shipping_state = Column(String, nullable=False)
    shipping_pincode = Column(String, nullable=False)

    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    user = relationship("User", back_populates="orders")
    items = relationship("OrderItem", back_populates="order", cascade="all, delete-orphan")

class OrderItem(Base):
    __tablename__ = "order_items"

    id = Column(String, primary_key=True, index=True)
    order_id = Column(String, ForeignKey("orders.id"))
    product_id = Column(String, nullable=False)
    variant_id = Column(String, nullable=False)
    product_name = Column(String, nullable=False)
    variant_weight = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    quantity = Column(Integer, default=1)
    image_key = Column(String, nullable=False)

    order = relationship("Order", back_populates="items")

class Review(Base):
    __tablename__ = "reviews"

    id = Column(String, primary_key=True, index=True)
    product_id = Column(String, ForeignKey("products.id"))
    author_name = Column(String, nullable=False)
    rating = Column(Integer, default=5)
    comment = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    product = relationship("Product", back_populates="reviews")
