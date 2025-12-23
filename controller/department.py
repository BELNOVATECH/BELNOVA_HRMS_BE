from fastapi import HTTPException
from services.department_service import (
    create_department,
    get_department,
    get_all_departments
)
from models.department import DepartmentCreateRequest, DepartmentResponse
from services.department_service import update_department_is_active


def create_department_controller(request: DepartmentCreateRequest):
    row = create_department(request.department)

    return DepartmentResponse(
        id=row["id"],
        department=row["department"],
        is_active=row["is_active"]
    )


def get_department_controller(department_id: int):
    dep = get_department(department_id)
    if not dep:
        raise HTTPException(status_code=404, detail="Department not found")

    return DepartmentResponse(
        id=dep["id"],
        department=dep["department"],
        is_active=dep["is_active"]
    )


def get_all_departments_controller():
    rows = get_all_departments()

    return [
        DepartmentResponse(
            id=row["id"],
            department=row["department"],
            is_active=row["is_active"]
        )
        for row in rows
    ]
    
def update_department_is_active_controller(dept_id: int, request):
    return update_department_is_active(dept_id, request.is_active)
