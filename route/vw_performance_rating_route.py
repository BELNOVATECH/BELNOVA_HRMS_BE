from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from core.database import get_db
from schemas.vw_performance_rating_schema import VwPerformanceRatingResponse
from controller.vw_performance_rating_controller import (
    get_all_performance_ratings_controller
)

router = APIRouter(
    prefix="/performance-ratings",
    tags=["Performance Ratings"]
)

@router.get(
    "/",
    response_model=List[VwPerformanceRatingResponse],
    summary="Get All Performance Ratings"
)
def get_performance_ratings(db: Session = Depends(get_db)):
    return get_all_performance_ratings_controller(db)
