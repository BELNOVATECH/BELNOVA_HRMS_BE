from sqlalchemy.orm import Session
from sqlalchemy import text
from fastapi import HTTPException

from services.employee_validator import validate_employee


def leave_balance_controller(
    emp_id: int,
    year: int,
    limit: int,
    offset: int,
    db: Session
):
    # ✅ Validate employee
    validate_employee(emp_id, db)

    try:
        result = db.execute(
            text("""
                SELECT *
                FROM fn_leave_balance(
                    :emp_id,
                    :year,
                    :limit,
                    :offset
                )
            """),
            {
                "emp_id": emp_id,
                "year": year,
                "limit": limit,
                "offset": offset
            }
        )

        rows = result.mappings().all()

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Database error: {str(e)}"
        )

    return {
        "emp_id": emp_id,
        "year": year,
        "leaves": rows
    }
