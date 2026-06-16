from sqlalchemy.orm import Session, joinedload
from fastapi import HTTPException
from datetime import datetime

from models.generated_models import (
    Users,
    EmployeeRegistration,
    EmployeeFamilyMember
)

from schemas.employee_schema import EmployeeCreate
from utils.hashing import hash_password


def create_employee_service(
    payload: EmployeeCreate,
    db: Session
):

    try:

        birth_year = (
            payload.date_of_birth.year
            if payload.date_of_birth
            else datetime.now().year
        )

        raw_password = f"{payload.first_name}{birth_year}"

        hashed_password = hash_password(raw_password)

        # USER

        user = Users(
            first_name=payload.first_name,
            last_name=payload.last_name,
            email=payload.email,
            mobile=payload.mobile,
            role_id=payload.role_id,
            gender_id=payload.gender_id,
            dob=payload.date_of_birth,
            address=payload.present_address,
            password=hashed_password,
            created_by=payload.created_by,
            is_active=True
        )

        db.add(user)
        db.flush()

        # EMPLOYEE

        emp = EmployeeRegistration(

            first_name=payload.first_name,
            last_name=payload.last_name,
            email=payload.email,
            mobile=payload.mobile,

            present_address=payload.present_address,
            permanent_address=payload.permanent_address,
            father_name=payload.father_name,

            blood_group_id=payload.blood_group_id,
            gender_id=payload.gender_id,
            marital_status_id=payload.marital_status_id,

            date_of_birth=payload.date_of_birth,

            emergency_mobile=payload.emergency_mobile,
            reference_mobile=payload.reference_mobile,

            aadhaar=payload.aadhaar,

            emp_code=payload.emp_code,

            designation_id=payload.designation_id,
            department_id=payload.department_id,
            employee_type_id=payload.employee_type_id,

            manager_id=payload.manager_id,
            role_id=payload.role_id,

            work_location_id=payload.work_location_id,
            shift_id=payload.shift_id,

            hired_date=payload.hired_date,
            join_date=payload.join_date,
            probation_end_date=payload.probation_end_date,

            salary=payload.salary,
            ctc=payload.ctc,

            bank_id=payload.bank_id,
            bank_ac_no=payload.bank_ac_no,
            ifsc_code=payload.ifsc_code,

            pan=payload.pan,
            uan=payload.uan,
            esic=payload.esic,

            upload_doc=payload.upload_doc,

            password=hashed_password,

            status_id=1,
            created_by=payload.created_by
        )

        db.add(emp)
        db.flush()

        # FAMILY MEMBERS

        for fm in payload.family_members:

            family = EmployeeFamilyMember(
                emp_id=emp.id,
                relation_id=fm.relation_id,
                first_name=fm.first_name,
                last_name=fm.last_name,
                date_of_birth=fm.date_of_birth,
                occupation_id=fm.occupation_id,
                phone=fm.phone,
                email=fm.email,
                present_address=fm.present_address,
                permanent_address=fm.permanent_address,
                bank_account=fm.bank_account,
                ifsc_code=fm.ifsc_code,
                pan=fm.pan,
                aadhaar=fm.aadhaar
            )

            db.add(family)

        db.commit()
        db.refresh(emp)

        return {
            "message": "Employee Created Successfully",
            "employee_id": emp.id
        }

    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


def get_all_employees_service(
    db: Session
):
    return (
        db.query(EmployeeRegistration)
        .options(
            joinedload(EmployeeRegistration.department),
            joinedload(EmployeeRegistration.designation),
            joinedload(EmployeeRegistration.employee_family_member)
        )
        .all()
    )


def get_employee_by_id_service(
    emp_id: int,
    db: Session
):

    employee = (
        db.query(EmployeeRegistration)
        .options(
            joinedload(EmployeeRegistration.department),
            joinedload(EmployeeRegistration.designation),
            joinedload(EmployeeRegistration.employee_family_member)
        )
        .filter(EmployeeRegistration.id == emp_id)
        .first()
    )

    if not employee:
        raise HTTPException(
            status_code=404,
            detail="Employee Not Found"
        )

    return employee