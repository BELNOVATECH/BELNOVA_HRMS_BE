from sqlalchemy.orm import Session
from fastapi import HTTPException
from datetime import datetime, timedelta

from models.employee_activity_model import EmployeeActivity
from models.employee_model import Employee
from schemas.employee_activity_schema import EmployeeActivityCreate
from models.master_module import MasterModule
from models.master_screen import MasterScreen

# ---------- CREATE ----------
def create_employee_activity_service(
    payload: EmployeeActivityCreate,
    db: Session
):
    # ✅ Validate employee exists
    emp = db.query(Employee).filter(Employee.id == payload.emp_id).first()
    if not emp:
        raise HTTPException(
            status_code=400,
            detail=f"Employee with id {payload.emp_id} does not exist"
        )

    activity = EmployeeActivity(
        emp_id=payload.emp_id,
        module_id=payload.module_id,
        screen_id=payload.screen_id,
        activity_description=payload.activity_description,

        created_by=payload.created_by,
        created_date=payload.created_date or datetime.utcnow(),

        modified_by=payload.modified_by,
        modified_date=payload.modified_date,

        is_active=payload.is_active
    )

    db.add(activity)
    db.commit()
    db.refresh(activity)
    return activity


# ---------- GET (LAST 7 DAYS / CUSTOM RANGE) ----------





def get_employee_activity_service(
    db: Session,
    from_datetime: Optional[datetime] = None,
    to_datetime: Optional[datetime] = None
):
    # default → last 7 days
    if not from_datetime and not to_datetime:
        to_datetime = datetime.utcnow()
        from_datetime = to_datetime - timedelta(days=7)

    query = (
        db.query(
            EmployeeActivity.id,
            EmployeeActivity.emp_id,
            Employee.first_name.label("employee_first_name"),
            Employee.last_name.label("employee_last_name"),

            EmployeeActivity.module_id,
            MasterModule.module_name,

            EmployeeActivity.screen_id,
            MasterScreen.screen_name,

            EmployeeActivity.activity_description,
            EmployeeActivity.created_by,
            EmployeeActivity.created_date,
            EmployeeActivity.modified_by,
            EmployeeActivity.modified_date,
            EmployeeActivity.is_active,
        )
        .join(Employee, Employee.id == EmployeeActivity.emp_id)
        .join(MasterModule, MasterModule.id == EmployeeActivity.module_id)
        .join(MasterScreen, MasterScreen.id == EmployeeActivity.screen_id)
        .filter(EmployeeActivity.created_date.between(from_datetime, to_datetime))
        .order_by(EmployeeActivity.created_date.desc())
    )

    results = query.all()

    # convert SQLAlchemy rows → dict
    activities = []
    for r in results:
        activities.append({
            "id": r.id,
            "emp_id": r.emp_id,
            "employee_first_name": r.employee_first_name,
            "employee_last_name": r.employee_last_name,

            "module_id": r.module_id,
            "module_name": r.module_name,

            "screen_id": r.screen_id,
            "screen_name": r.screen_name,

            "activity_description": r.activity_description,
            "created_by": r.created_by,
            "created_date": r.created_date,
            "modified_by": r.modified_by,
            "modified_date": r.modified_date,
            "is_active": r.is_active,
        })

    return activities
