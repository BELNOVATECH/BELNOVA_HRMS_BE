
# from sqlalchemy import (
#     Column, Integer, String, Date, DateTime,
#     Boolean, Float, Text, ForeignKey
# )
# from sqlalchemy.orm import relationship
# from core.database import Base
# from datetime import datetime
# from sqlalchemy.orm import relationship


# class Employee(Base):
#     __tablename__ = "employee_registration"

#     id = Column(Integer, primary_key=True, index=True)

#     first_name = Column(String(150), nullable=False)
#     last_name = Column(String(150))
#     email = Column(String(255))
#     mobile = Column(String(20))

#     present_address = Column(Text)
#     permanent_address = Column(Text)

#     father_name = Column(String(150))
#     blood_group_id = Column(Integer)
#     gender_id = Column(Integer)
#     marital_status_id = Column(Integer)
#     date_of_birth = Column(Date)

#     emp_code = Column(String(100), unique=True)

#     # ✅ FIXED
#     designation_id = Column(
#         Integer,
#         ForeignKey("master_designation.id"),
#         nullable=True
#     )

#     # ✅ RELATIONSHIP
#     designation = relationship(
#         "Designation",
#         lazy="joined"
#     )

#     department_id = Column(Integer)
#     employee_type_id = Column(Integer)
#     manager_id = Column(Integer)
#     role_id = Column(Integer)
#     work_location_id = Column(Integer)
#     shift_id = Column(Integer)

#     hired_date = Column(Date)
#     join_date = Column(Date)

#     salary = Column(Float)
#     ctc = Column(Float)

#     bank_ac_no = Column(String(100))
#     ifsc_code = Column(String(50))
#     pan = Column(String(50))
#     uan = Column(String(100))

#     is_active = Column(Boolean, default=True)
#     created_date = Column(DateTime, default=datetime.utcnow)
#     modified_date = Column(DateTime)


from sqlalchemy import (
    Column, Integer, String, Date, DateTime,
    Boolean, Float, Text, ForeignKey
)
from sqlalchemy.orm import relationship
from datetime import datetime
from core.database import Base


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

    emergency_mobile = Column(String(20))
    reference_mobile = Column(String(20))
    aadhaar = Column(String(20))

    emp_code = Column(String(100), unique=True)

    designation_id = Column(Integer)
    department_id = Column(Integer)
    employee_type_id = Column(Integer)
    manager_id = Column(Integer)
    role_id = Column(Integer)
    work_location_id = Column(Integer)
    shift_id = Column(Integer)

    hired_date = Column(Date)
    join_date = Column(Date)
    probation_end_date = Column(Date)

    salary = Column(Float)
    ctc = Column(Float)
    pay_method_id = Column(Integer)   # nullable in DB

    bank_id = Column(Integer)
    bank_ac_no = Column(String(100))
    ifsc_code = Column(String(50))

    pan = Column(String(50))
    uan = Column(String(100))
    esic = Column(String(50))

    upload_doc = Column(Text)

    user_id = Column(Integer)
    created_by = Column(Integer)
    modified_by = Column(Integer)

    is_active = Column(Boolean, default=True)
    created_date = Column(DateTime, default=datetime.utcnow)
    modified_date = Column(DateTime)

    family_members = relationship(
        "EmployeeFamilyMember",
        back_populates="employee",
        cascade="all, delete-orphan"
    )
