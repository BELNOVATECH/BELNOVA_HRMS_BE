
from sqlalchemy import (
    Column, Integer, String, Date, DateTime,
    Boolean, Float, Text, ForeignKey
)
from sqlalchemy.orm import relationship
from core.database import Base
from datetime import datetime


class Employee(Base):
    __tablename__ = "employee_registration"

    id = Column(Integer, primary_key=True, index=True)

    first_name = Column(String(150), nullable=False)
    last_name = Column(String(150))
    email = Column(String(255))
    mobile = Column(String(20))

    present_address = Column(Text)
    permanent_address = Column(Text)

    father_name = Column(String(150))
    blood_group_id = Column(Integer)
    gender_id = Column(Integer)
    marital_status_id = Column(Integer)
    date_of_birth = Column(Date)

    emp_code = Column(String(100), unique=True)

    # ✅ FIXED
    designation_id = Column(
        Integer,
        ForeignKey("master_designation.id"),
        nullable=True
    )

    # ✅ RELATIONSHIP
    designation = relationship(
        "Designation",
        lazy="joined"
    )

    department_id = Column(Integer)
    employee_type_id = Column(Integer)
    manager_id = Column(Integer)
    role_id = Column(Integer)
    work_location_id = Column(Integer)
    shift_id = Column(Integer)

    hired_date = Column(Date)
    join_date = Column(Date)

    salary = Column(Float)
    ctc = Column(Float)

    bank_ac_no = Column(String(100))
    ifsc_code = Column(String(50))
    pan = Column(String(50))
    uan = Column(String(100))

    is_active = Column(Boolean, default=True)
    created_date = Column(DateTime, default=datetime.utcnow)
    modified_date = Column(DateTime)


