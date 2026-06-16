from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
from typing import Optional
from datetime import datetime

from core.database import get_db

from schemas.employee_activity_schema import (
    EmployeeActivityCreate
)

from services.employee_activity_service import (
    create_employee_activity_service,
    get_employee_activity_service
)

router = APIRouter(
    prefix="/employee-activity",
    tags=["Employee Activities"]
)


@router.post("/")
def create_activity(
    payload: EmployeeActivityCreate,
    db: Session = Depends(get_db)
):

    return create_employee_activity_service(
        payload,
        db
    )


@router.get("/")
def get_activities(
    from_datetime: Optional[datetime] = None,
    to_datetime: Optional[datetime] = None,
    db: Session = Depends(get_db)
):

    return get_employee_activity_service(
        db,
        from_datetime,
        to_datetime
    )