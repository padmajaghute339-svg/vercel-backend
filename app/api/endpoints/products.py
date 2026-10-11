from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from backend.app.database.session import get_db
from backend.app.models.models import Product, ProductVariant
from backend.app.schemas.schemas import ProductResponse

router = APIRouter()

@router.get("", response_model=List[ProductResponse])
def get_products(
    category: Optional[str] = None,
    flavor: Optional[str] = None,
    q: Optional[str] = None,
    sort: Optional[str] = None,
    db: Session = Depends(get_db)
):
    query = db.query(Product)

    if category and category != "all":
        query = query.filter(Product.category_id == category)

    if flavor:
        query = query.filter(Product.flavor_profile == flavor)

    if q:
        search_filter = f"%{q.lower()}%"
        query = query.filter(
            (Product.name.ilike(search_filter)) |
            (Product.tagline.ilike(search_filter)) |
            (Product.description.ilike(search_filter))
        )

    products = query.all()

    # In-memory sort based on variants / bestsellers
    if sort == "bestseller":
        products.sort(key=lambda p: not p.is_bestseller)
    elif sort == "crunch":
        products.sort(key=lambda p: p.crunch_index, reverse=True)

    return products

@router.get("/{product_id}", response_model=ProductResponse)
def get_product_by_id(product_id: str, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product delicacy not found")
    return product
