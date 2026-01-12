from sqlalchemy.orm import Session, aliased
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
    activity = EmployeeActivity(
        emp_id=payload.emp_id,
        module_id=payload.module_id,
        screen_id=payload.screen_id,
        activity_description=payload.activity_description,
        created_by=payload.created_by,
        created_date=datetime.utcnow(),
        modified_by=payload.modified_by,
        modified_date=datetime.utcnow(),
        is_active=payload.is_active
    )

    db.add(activity)
    db.commit()
    db.refresh(activity)

    return enrich_activity(activity, db)




def get_employee_activity_service(
    db: Session,
    from_datetime=None,
    to_datetime=None
):
    query = db.query(EmployeeActivity)

    if from_datetime and to_datetime:
        query = query.filter(
            EmployeeActivity.created_date.between(from_datetime, to_datetime)
        )
    else:
        last_7_days = datetime.utcnow() - timedelta(days=7)
        query = query.filter(EmployeeActivity.created_date >= last_7_days)

    activities = query.order_by(EmployeeActivity.created_date.desc()).all()

    return [enrich_activity(a, db) for a in activities]

def enrich_activity(activity: EmployeeActivity, db: Session):
    EmployeeAlias = aliased(Employee)

    emp = db.query(Employee).filter(Employee.id == activity.emp_id).first()
    creator = db.query(EmployeeAlias).filter(
        EmployeeAlias.id == activity.created_by
    ).first()

    modifier = None
    if activity.modified_by:
        modifier = db.query(EmployeeAlias).filter(
            EmployeeAlias.id == activity.modified_by
        ).first()

    module = db.query(MasterModule).filter(
        MasterModule.id == activity.module_id
    ).first()

    screen = db.query(MasterScreen).filter(
        MasterScreen.id == activity.screen_id
    ).first()

    return {
        "id": activity.id,

        "emp_id": activity.emp_id,
        "employee_first_name": emp.first_name if emp else "",
        "employee_last_name": emp.last_name if emp else "",

        "created_by": activity.created_by,
        "created_by_first_name": creator.first_name if creator else "",
        "created_by_last_name": creator.last_name if creator else "",

        "modified_by": activity.modified_by,
        "modified_by_first_name": modifier.first_name if modifier else None,
        "modified_by_last_name": modifier.last_name if modifier else None,

        "module_id": activity.module_id,
        "module_name": module.module_name if module else "",

        "screen_id": activity.screen_id,
        "screen_name": screen.screen_name if screen else "",

        "activity_description": activity.activity_description,
        "created_date": activity.created_date,
        "modified_date": activity.modified_date,
        "is_active": activity.is_active
    }
