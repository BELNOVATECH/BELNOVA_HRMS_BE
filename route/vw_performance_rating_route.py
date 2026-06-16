from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from core.database import get_db
from services.vw_performance_rating_service import (
    get_performance_ratings_service
)

router = APIRouter(
    prefix="/performance-ratings",
    tags=["Performance Ratings"]
)

@router.get("/")
def get_performance_ratings(
    db: Session = Depends(get_db)
):
    return get_performance_ratings_service(db)