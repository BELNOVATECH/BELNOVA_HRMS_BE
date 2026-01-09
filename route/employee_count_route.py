from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from core.database import get_db
from schemas.employee_count_schema import EmployeeCountResponse
from controller.employee_count_controller import (
    get_active_employee_count_controller
)

router = APIRouter(
    prefix="/employee-count",          
    tags=["Employee Count"]             
)

@router.get(
    "/active",
    response_model=EmployeeCountResponse,
    summary="Get Total Active Employees Count"
)
def get_active_employee_count(db: Session = Depends(get_db)):
    return get_active_employee_count_controller(db)
