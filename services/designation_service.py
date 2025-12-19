from sqlalchemy import select
from models.designation import Designation

def create_designation_service(data, db):
    designation = Designation(
        designation_name=data.designation_name,
        dept_id=data.dept_id,
        is_active=data.is_active
    )
    db.add(designation)
    db.commit()
    db.refresh(designation)
    return designation


def get_designations_service(db):
    result = db.execute(select(Designation))
    return result.scalars().all()
