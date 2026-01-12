from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from core.database import get_db
from services.employee_services_newjoinings import get_new_joiners_count
from datetime import date

router = APIRouter(prefix="/employee", tags=["Employee-newjoiners"])

@router.get("/new-joiners/count")
def new_joiners_count(
    year: int = Query(default=date.today().year),
    month: int = Query(default=date.today().month),
    db: Session = Depends(get_db),
):
    count = get_new_joiners_count(db, year, month)

    return {
        "new_joiners_count": count
    }

