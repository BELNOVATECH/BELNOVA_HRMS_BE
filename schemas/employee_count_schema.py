from pydantic import BaseModel

class EmployeeCountResponse(BaseModel):
    total_employees: int
