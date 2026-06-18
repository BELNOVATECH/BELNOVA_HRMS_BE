from pydantic import BaseModel
from datetime import date
from typing import Optional


class TaskCreate(BaseModel):
    title: str
    description: str
    task_type_id: int
    project_id: int
    emp_id: int
    status_id: int
    due_date: date

    reporting_manager_id: Optional[int] = None
    task_manager_id: Optional[int] = None
    efforts_in_days: Optional[int] = None

    created_by: Optional[int] = None
    project_module_id: Optional[int] = None


class TaskUpdate(TaskCreate):
    modified_by: Optional[int] = None