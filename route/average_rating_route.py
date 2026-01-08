from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from core.database import get_db
from schemas.average_rating_schema import AverageRatingResponse
from controller.average_rating_controller import get_average_rating_controller

router = APIRouter(
    prefix="/average-rating",
    tags=["Average Rating"]
)

@router.get(
    "/",
    response_model=AverageRatingResponse,
    summary="Get Average Employee Rating with Calculation"
)
def get_average_rating(db: Session = Depends(get_db)):
    return get_average_rating_controller(db)
