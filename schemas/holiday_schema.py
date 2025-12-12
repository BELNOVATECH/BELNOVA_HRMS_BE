from pydantic import BaseModel
from datetime import date
# from utils.date_utils import convert_date, convert_datetime

    
class HolidayRead(BaseModel):
    id: int
    holiday_name: str
    holiday_date: date

    model_config = {"from_attributes": True}
