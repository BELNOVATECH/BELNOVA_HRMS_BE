from fastapi import APIRouter
from models.department import DepartmentCreateRequest, IsActiveUpdate
from controller.department import (
    create_department_controller,
    get_all_departments_controller,
    update_department_is_active_controller
)

router = APIRouter()

@router.post("/create")
def create_department(request: DepartmentCreateRequest):
    return create_department_controller(request)

@router.get("/all")
def get_all_departments():
    return get_all_departments_controller()


@router.put("/{dept_id}/is-active")
def update_department_is_active(dept_id: int, request: IsActiveUpdate):
    return update_department_is_active_controller(dept_id, request)
