from pydantic import BaseModel

class JobTitleCreateRequest(BaseModel):
    position: str

class JobTitleResponse(BaseModel):
    id: int
    position: str
    is_active: bool
