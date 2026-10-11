from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from backend.app.database.session import get_db
from backend.app.models.models import Order, Product, ProductVariant
from backend.app.schemas.schemas import AnalyticsResponse

router = APIRouter()

@router.get("/analytics", response_model=AnalyticsResponse)
def get_analytics(db: Session = Depends(get_db)):
    total_rev = db.query(func.sum(Order.total)).scalar() or 0.0
    total_ords = db.query(Order).count()
    total_prods = db.query(Product).count()
    low_stock = db.query(ProductVariant).filter(ProductVariant.stock_quantity <= 20).count()
    recent = db.query(Order).order_by(Order.created_at.desc()).limit(10).all()

    return {
        "total_revenue": float(total_rev),
        "total_orders": total_ords,
        "total_products": total_prods,
        "low_stock_count": low_stock,
        "recent_orders": recent
    }
