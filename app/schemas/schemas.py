from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

# Variant Schema
class ProductVariantBase(BaseModel):
    weight: str
    price: float
    original_price: Optional[float] = None
    sku: str
    in_stock: bool = True
    stock_quantity: int = 100

class ProductVariantResponse(ProductVariantBase):
    id: str

    class Config:
        from_attributes = True

# Product Schema
class ProductBase(BaseModel):
    name: str
    hindi_name: Optional[str] = None
    tagline: str
    description: str
    long_description: Optional[str] = None
    category_id: str
    flavor_profile: str = "crunchy"
    spice_level: int = 1
    crunch_index: int = 90
    is_bestseller: bool = False
    image_key: str
    bg_theme: str = "#8B0000"
    accent_color: str = "#FFB703"

class ProductResponse(ProductBase):
    id: str
    variants: List[ProductVariantResponse] = []

    class Config:
        from_attributes = True

# Category Schema
class CategoryResponse(BaseModel):
    id: str
    name: str
    description: Optional[str] = None

    class Config:
        from_attributes = True

# Cart Schemas
class CartItemCreate(BaseModel):
    product_id: str
    variant_id: str
    quantity: int = 1

class CartItemUpdate(BaseModel):
    quantity: int

class CartItemResponse(BaseModel):
    id: str
    product_id: str
    variant_id: str
    quantity: int
    product: ProductResponse
    variant: ProductVariantResponse

    class Config:
        from_attributes = True

class CartResponse(BaseModel):
    id: str
    items: List[CartItemResponse] = []
    subtotal: float = 0.0
    discount: float = 0.0
    shipping: float = 0.0
    tax: float = 0.0
    total: float = 0.0

# Order Schemas
class OrderAddressSchema(BaseModel):
    full_name: str
    email: str
    phone: str
    street: str
    city: str
    state: str
    pincode: str

class OrderItemCreate(BaseModel):
    product_id: str
    variant_id: str
    quantity: int

class OrderCreate(BaseModel):
    items: List[OrderItemCreate]
    address: OrderAddressSchema
    payment_method: str = "UPI Demo Sandbox"
    coupon_code: Optional[str] = None

class OrderItemResponse(BaseModel):
    product_name: str
    variant_weight: str
    price: float
    quantity: int
    image_key: str

    class Config:
        from_attributes = True

class OrderResponse(BaseModel):
    id: str
    order_number: str
    status: str
    subtotal: float
    discount: float
    shipping: float
    tax: float
    total: float
    payment_method: str
    tracking_number: str
    estimated_delivery: str
    created_at: datetime
    shipping_full_name: str
    shipping_city: str
    items: List[OrderItemResponse] = []

    class Config:
        from_attributes = True

# Admin Analytics Schema
class AnalyticsResponse(BaseModel):
    total_revenue: float
    total_orders: int
    total_products: int
    low_stock_count: int
    recent_orders: List[OrderResponse]
