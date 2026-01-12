from sqlalchemy.orm import Session, joinedload
from datetime import datetime
from fastapi import HTTPException

from models.user_model import User
from models.employee_model import Employee
from models.employee_family_member_model import EmployeeFamilyMember
from schemas.employee_schema import EmployeeCreate
from utils.hashing import hash_password   # 🔥 THIS ONE ONLY




# =========================================================
# CREATE EMPLOYEE (User → Employee → Family Members)
# =========================================================
def create_employee_service(payload: EmployeeCreate, db: Session):
    try:
        # -------------------------------
        # 1️⃣ Generate Safe Password
        # -------------------------------
        birth_year = payload.date_of_birth.year if payload.date_of_birth else datetime.utcnow().year
        raw_password = f"{payload.first_name}{birth_year}"
        hashed_password = hash_password(raw_password)

        # -------------------------------
        # 2️⃣ CREATE USER
        # -------------------------------
        user = User(
            first_name=payload.first_name,
            last_name=payload.last_name,
            email=payload.email,
            mobile=payload.mobile,
            gender_id=payload.gender_id,
            dob=payload.date_of_birth,
            role_id=payload.role_id,
            password=hashed_password,
            address=payload.present_address, 
            created_by=payload.created_by
        )
        db.add(user)
        db.flush()

        # -------------------------------
        # 3️⃣ CREATE EMPLOYEE
        # -------------------------------
        emp = Employee(
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

            user_id=user.id,
            created_by=payload.created_by

        )
        db.add(emp)
        db.flush()

        # -------------------------------
        # 4️⃣ FAMILY MEMBERS
        # -------------------------------
        for fm in payload.family_members:
            db.add(EmployeeFamilyMember(
                emp_id=emp.id,
                **fm.dict(),
                # created_by=payload.created_by
            ))

        # -------------------------------
        # 5️⃣ COMMIT ALL
        # -------------------------------
        db.commit()
        db.refresh(emp)
        return emp

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))


# =========================================================
# GET ALL EMPLOYEES
# =========================================================
def get_employees_service(db: Session):
    return (
        db.query(Employee)
        .options(joinedload(Employee.family_members))
        .all()
    )


# =========================================================
# GET EMPLOYEE BY ID
# =========================================================
def get_employee_by_id_service(emp_id: int, db: Session):
    emp = (
        db.query(Employee)
        .options(joinedload(Employee.family_members))
        .filter(Employee.id == emp_id)
        .first()
    )

    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")

    return emp


# =========================================================
# UPDATE EMPLOYEE ACTIVE STATUS
# =========================================================
def update_employee_status_service(emp_id: int, is_active: bool, db: Session):
    emp = db.query(Employee).filter(Employee.id == emp_id).first()

    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")

    emp.is_active = is_active
    emp.modified_date = datetime.utcnow()

    db.commit()
    db.refresh(emp)
    return emp
