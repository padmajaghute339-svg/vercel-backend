from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import uuid
import datetime
from backend.app.database.session import get_db
from backend.app.models.models import Order, OrderItem, ProductVariant, Product
from backend.app.schemas.schemas import OrderCreate, OrderResponse

router = APIRouter()

@router.post("", response_model=OrderResponse)
def create_order(payload: OrderCreate, db: Session = Depends(get_db)):
    if not payload.items:
        raise HTTPException(status_code=400, detail="Cannot place an empty order")

    subtotal = 0.0
    db_items = []

    # Server-side authoritative price verification
    for item in payload.items:
        variant = db.query(ProductVariant).filter(ProductVariant.id == item.variant_id).first()
        if not variant:
            raise HTTPException(status_code=400, detail=f"Invalid variant ID: {item.variant_id}")

        product = db.query(Product).filter(Product.id == item.product_id).first()
        item_price = variant.price
        line_total = item_price * item.quantity
        subtotal += line_total

        db_items.append(
            OrderItem(
                id=str(uuid.uuid4()),
                product_id=product.id,
                variant_id=variant.id,
                product_name=product.name,
                variant_weight=variant.weight,
                price=item_price,
                quantity=item.quantity,
                image_key=product.image_key
            )
        )

    # Server authoritative coupon & discounts
    discount = 0.0
    if payload.coupon_code:
        code = payload.coupon_code.strip().upper()
        if code == "CRUNCH20":
            discount = round(subtotal * 0.20, 2)
        elif code == "BIKANER10":
            discount = round(subtotal * 0.10, 2)

    # Shipping rules: Free above 499 INR
    shipping = 0.0 if subtotal > 499 else 50.0
    tax = round((subtotal - discount) * 0.05, 2) # 5% GST
    total = max(0.0, round(subtotal - discount + shipping + tax, 2))

    order_number = f"CC-{str(uuid.uuid4().int)[:6]}"
    tracking_number = f"IND-EXPRESS-{str(uuid.uuid4().int)[:6]}"

    new_order = Order(
        id=str(uuid.uuid4()),
        order_number=order_number,
        status="confirmed",
        subtotal=subtotal,
        discount=discount,
        shipping=shipping,
        tax=tax,
        total=total,
        payment_method=payload.payment_method,
        tracking_number=tracking_number,
        estimated_delivery="3 to 4 Business Days",
        shipping_full_name=payload.address.full_name,
        shipping_email=payload.address.email,
        shipping_phone=payload.address.phone,
        shipping_street=payload.address.street,
        shipping_city=payload.address.city,
        shipping_state=payload.address.state,
        shipping_pincode=payload.address.pincode,
        created_at=datetime.datetime.utcnow(),
        items=db_items
    )

    db.add(new_order)
    db.commit()
    db.refresh(new_order)

    return new_order

@router.get("", response_model=List[OrderResponse])
def get_orders(db: Session = Depends(get_db)):
    return db.query(Order).order_by(Order.created_at.desc()).all()

@router.get("/{order_id}", response_model=OrderResponse)
def get_order_by_id(order_id: str, db: Session = Depends(get_db)):
    order = db.query(Order).filter(Order.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

@router.patch("/{order_id}/status", response_model=OrderResponse)
def update_order_status(order_id: str, status: str, db: Session = Depends(get_db)):
    order = db.query(Order).filter(Order.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    order.status = status
    db.commit()
    db.refresh(order)
    return order
