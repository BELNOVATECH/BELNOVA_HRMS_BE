# from sqlalchemy import (
#     Column, Integer, String, Date, DateTime,
#     Boolean, ForeignKey, Text
# )
# from sqlalchemy.orm import relationship
# from core.database import Base
# from datetime import datetime


# class EmployeeFamilyMember(Base):
#     __tablename__ = "employee_family_member"

#     id = Column(Integer, primary_key=True, index=True)

#     emp_id = Column(
#         Integer,
#         ForeignKey("employee_registration.id", ondelete="CASCADE"),
#         nullable=False
#     )

#     relation_id = Column(Integer, nullable=False)

#     first_name = Column(String(150), nullable=False)
#     last_name = Column(String(150))

#     date_of_birth = Column(Date, nullable=False)
#     occupation_id = Column(Integer, nullable=False)

#     phone = Column(String(20))
#     email = Column(String(255))

#     present_address = Column(Text, nullable=False)
#     permanent_address = Column(Text, nullable=False)

#     bank_account = Column(String(100))
#     ifsc_code = Column(String(50))
#     pan = Column(String(50))
#     aadhar = Column(String(20))

#     created_by = Column(Integer)
#     created_date = Column(DateTime, default=datetime.utcnow)

#     modified_by = Column(Integer)
#     modified_date = Column(DateTime)

#     is_active = Column(Boolean, default=True)

from sqlalchemy import (
    Column, Integer, String, Date, DateTime,
    Boolean, ForeignKey, Text
)
from sqlalchemy.orm import relationship
from datetime import datetime
from core.database import Base


class EmployeeFamilyMember(Base):
    __tablename__ = "employee_family_member"

    id = Column(Integer, primary_key=True, index=True)

    emp_id = Column(
        Integer,
        ForeignKey("employee_registration.id", ondelete="CASCADE"),
        nullable=False
    )

    relation_id = Column(Integer, nullable=False)
    first_name = Column(String(150), nullable=False)
    last_name = Column(String(150))

    date_of_birth = Column(Date, nullable=False)
    occupation_id = Column(Integer, nullable=False)

    # ✅ OPTIONAL FIELDS (NULLABLE BY DEFAULT)
    phone = Column(String(20))
    email = Column(String(255))

    present_address = Column(Text, nullable=False)
    permanent_address = Column(Text, nullable=False)

    bank_account = Column(String(100))
    ifsc_code = Column(String(50))
    pan = Column(String(50))
    aadhar = Column(String(20))

    created_by = Column(Integer)
    created_date = Column(DateTime, default=datetime.utcnow)

    modified_by = Column(Integer)
    modified_date = Column(DateTime)

    is_active = Column(Boolean, default=True)

    employee = relationship(
        "Employee",
        back_populates="family_members"
    )
