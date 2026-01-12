from sqlalchemy.orm import Session
from datetime import date
from models.employee_model import Employee

def get_new_joiners_count(db: Session, year: int, month: int) -> int:
    start_date = date(year, month, 1)

    if month == 12:
        end_date = date(year + 1, 1, 1)
    else:
        end_date = date(year, month + 1, 1)

    return (
        db.query(Employee)
        .filter(Employee.join_date >= start_date)
        .filter(Employee.join_date < end_date)
        .count()
    )
