

from sqlalchemy.orm import Session
from sqlalchemy import extract
from models.employee_model import Employee

def get_new_joiners_in_month(db: Session, year: int, month: int):
    return (
        db.query(Employee)
        .filter(extract("year", Employee.join_date) == year)
        .filter(extract("month", Employee.join_date) == month)
        .all()
    );from sqlalchemy.orm import Session
from datetime import date
from models.employee_model import Employee

def get_new_joiners_in_month(db: Session, year: int, month: int):
    # Start of the month
    start_date = date(year, month, 1)

    # Start of next month
    if month == 12:
        end_date = date(year + 1, 1, 1)
    else:
        end_date = date(year, month + 1, 1)

    return (
        db.query(Employee)
        .filter(Employee.join_date >= start_date)
        .filter(Employee.join_date < end_date)
        .all()
    )
