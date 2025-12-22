from pydantic import BaseModel


class JobTitleCreate(BaseModel):
    designation_id: int
    department_id: int
    status_id: int
    
class JobOpeningResponse(BaseModel):
    id: int
    designation_id: int
    department_id: int
    status_id: int
    is_active: bool

    model_config = {
        "from_attributes": True
    }


class JobOpeningIsActiveUpdate(BaseModel):
    is_active: bool
