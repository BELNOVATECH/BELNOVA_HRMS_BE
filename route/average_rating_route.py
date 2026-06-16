from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from core.database import get_db
from controller.average_rating_controller import (
    get_average_rating_controller
)
from schemas.average_rating_schema import (
    AverageRatingResponse
)

router = APIRouter(
    prefix="/average-rating",
    tags=["Average Rating"]
)

@router.get(
    "/",
    response_model=AverageRatingResponse
)
def get_average_rating(
    db: Session = Depends(get_db)
):
    return get_average_rating_controller(db)