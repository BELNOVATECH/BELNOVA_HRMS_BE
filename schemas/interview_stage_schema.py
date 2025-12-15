from pydantic import BaseModel, field_serializer
from datetime import datetime
from typing import Optional
from zoneinfo import ZoneInfo

IST = ZoneInfo("Asia/Kolkata")


# -------------------------
# CREATE SCHEMA
# -------------------------
class InterviewStageCreate(BaseModel):
    stage_name: str
    description: Optional[str] = None
    is_active: Optional[bool] = True


# -------------------------
# UPDATE SCHEMA
# -------------------------
class InterviewStageUpdate(BaseModel):
    stage_name: Optional[str] = None
    description: Optional[str] = None
    is_active: Optional[bool] = None


# -------------------------
# RESPONSE SCHEMA
# -------------------------
class InterviewStageResponse(BaseModel):
    id: int
    stage_name: str
    description: Optional[str]
    is_active: bool
    created_date: datetime
    modified_date: Optional[datetime]

    model_config = {
        "from_attributes": True  # ✅ Pydantic v2 replacement for orm_mode
    }

    # ✅ Convert UTC → IST safely
    @field_serializer("created_date", "modified_date")
    def convert_utc_to_ist(self, value: datetime | None):
        if value is None:
            return None
        return value.astimezone(IST)
