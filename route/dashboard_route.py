from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from core.database import get_db
from services.dashboard_service import get_dashboard_data_service
from schemas.dashboard_schema import DashboardResponse

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)


@router.get("/summary", response_model=DashboardResponse)
def get_dashboard_summary(db: Session = Depends(get_db)):
    return get_dashboard_data_service(db)
