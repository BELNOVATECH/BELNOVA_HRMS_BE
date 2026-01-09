from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from core.database import get_db
from schemas.pending_review_schema import PendingReviewResponse
from controller.pending_review_controller import get_pending_reviews_controller

router = APIRouter(
    prefix="/pending-reviews",
    tags=["Pending Reviews"]
)

@router.get(
    "/",
    response_model=PendingReviewResponse,
    summary="Get Employees with Pending Performance Reviews"
)
def get_pending_reviews(db: Session = Depends(get_db)):
    return get_pending_reviews_controller(db)
