from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from datetime import datetime
from typing import Optional

from core.database import get_db
from schemas.employee_activity_schema import (
    EmployeeActivityCreate,
    EmployeeActivityResponse,
    EmployeeActivityListResponse
)
from services.employee_activity_service import (
    create_employee_activity_service,
    get_employee_activity_service
)

router = APIRouter(
    prefix="/employee-activity",
    tags=["Employee Activity"]
)


# ---------- POST ----------
@router.post(
    "/",
    response_model=EmployeeActivityResponse,
    summary="Create Employee Activity"
)
def create_activity(
    payload: EmployeeActivityCreate,
    db: Session = Depends(get_db)
):
    return create_employee_activity_service(payload, db)


# ---------- GET ----------
@router.get(
    "/",
    response_model=EmployeeActivityListResponse,
    summary="Get Recent Employee Activity"
)
def get_recent_activity(
    from_datetime: Optional[datetime] = Query(None),
    to_datetime: Optional[datetime] = Query(None),
    db: Session = Depends(get_db)
):
    activities = get_employee_activity_service(
        db=db,
        from_datetime=from_datetime,
        to_datetime=to_datetime
    )

    if not activities:
        return {
            "total_records": 0,
            "activities": [],
            "message": "No recent activity found"
        }

    return {
        "total_records": len(activities),
        "activities": activities,
        "message": "Recent activities fetched successfully"
    }
