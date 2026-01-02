from pydantic import BaseModel, field_serializer
from typing import Optional




class InterviewStageCreate(BaseModel):
    stage_name: str
    is_active: Optional[bool] = True



class InterviewStageUpdate(BaseModel):
    stage_name: Optional[str] = None
    is_active: Optional[bool] = None



class InterviewStageIsActiveUpdate(BaseModel):
    is_active: bool


class InterviewStageResponse(BaseModel):
    id: int
    stage_name: str
    is_active: bool

    model_config = {
        "from_attributes": True  # ✅ Pydantic v2 replacement for orm_mode
    }

   
