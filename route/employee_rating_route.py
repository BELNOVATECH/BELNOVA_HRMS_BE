from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from core.database import get_db
from schemas.employee_rating_schema import EmployeeRatingCreate
from controller.employee_rating_controller import create_employee_rating_controller

router = APIRouter(
    prefix="/employee-rating",
    tags=["Employee Rating"]
)

@router.post("/", summary="Create Employee Performance Rating")
def create_employee_rating(
    payload: EmployeeRatingCreate,
    db: Session = Depends(get_db)
):
    return create_employee_rating_controller(payload, db)
