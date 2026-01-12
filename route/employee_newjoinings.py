from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from core.database import get_db
from services.employee_services_newjoinings import get_new_joiners_in_month
from datetime import date

router = APIRouter(prefix="/employee", tags=["Employee"])

@router.get("/new-joiners")
def new_joiners(
    year: int = Query(default=date.today().year),
    month: int = Query(default=date.today().month),
    db: Session = Depends(get_db),
):
    employees = get_new_joiners_in_month(db, year, month)

    return {
        "year": year,
        "month": month,
        "new_joiners_count": len(employees),
        "employees": [
            {
                "id": e.id,
                "name": e.name,
                "join_date": e.join_date
            }
            for e in employees
        ]
    }


