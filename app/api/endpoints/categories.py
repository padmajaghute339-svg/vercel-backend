from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from backend.app.database.session import get_db
from backend.app.models.models import Category
from backend.app.schemas.schemas import CategoryResponse

router = APIRouter()

@router.get("", response_model=List[CategoryResponse])
def get_categories(db: Session = Depends(get_db)):
    return db.query(Category).all()
