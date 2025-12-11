from fastapi import APIRouter
from models.department import DepartmentCreateRequest
from controller.department import (
    create_department_controller,
    get_department_controller,
    get_all_departments_controller
)

router = APIRouter()

@router.post("/create")
def create_department(request: DepartmentCreateRequest):
    return create_department_controller(request)

@router.get("/all")
def get_all_departments():
    return get_all_departments_controller()


