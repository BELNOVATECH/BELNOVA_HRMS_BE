from pydantic import BaseModel
from datetime import date


class HolidayRead(BaseModel):
    id: int
    holiday_name: str
    holiday_date: date

    model_config = {
        "from_attributes": True
    }