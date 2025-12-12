from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.database import get_db
from controller.holiday_controller import get_holidays_controller
from schemas.holiday_schema import HolidayRead
from typing import List

holiday_router = APIRouter()

@holiday_router.get("/", response_model=List[HolidayRead])
def get_holidays(db: Session = Depends(get_db)):
    return get_holidays_controller(db)
