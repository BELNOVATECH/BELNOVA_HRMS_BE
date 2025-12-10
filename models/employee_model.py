# models/employee_model.py
from sqlalchemy import Column, Integer, String, Date, DateTime, Boolean, Float, Text
from core.database import Base
from datetime import datetime

class Employee(Base):
    __tablename__ = "employee_registration"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(150), nullable=False)
    last_name = Column(String(150), nullable=True)
    address = Column(Text, nullable=True)
    civil_status_id = Column(Integer, nullable=True)
    gender_id = Column(Integer, nullable=True)
    mobile = Column(String(20), nullable=True, unique=False)
    date_of_birth = Column(Date, nullable=True)
    emergency_mobile = Column(String(20), nullable=True)
    position_id = Column(Integer, nullable=True)
    hired_date = Column(Date, nullable=True)
    pay_method_id = Column(Integer, nullable=True)
    department_id = Column(Integer, nullable=True)
    work_status_id = Column(Integer, nullable=True)
    is_active = Column(Boolean, default=True)
    created_date = Column(DateTime, default=datetime.utcnow)
    modified_date = Column(DateTime, nullable=True)
    user_id = Column(Integer, nullable=True)
    created_by = Column(Integer, nullable=True)
    modified_by = Column(Integer, nullable=True)
    manager_id = Column(Integer, nullable=True)
    email = Column(String(255), nullable=True, unique=False)
    salary = Column(Float, nullable=True)
    join_date = Column(Date, nullable=True)
    upload_doc = Column(String(255), nullable=True)
    bank_id = Column(Integer, nullable=True)
    bank_ac_no = Column(String(100), nullable=True)
    ifsc_code = Column(String(50), nullable=True)
    esic = Column(String(100), nullable=True)
    pan = Column(String(50), nullable=True)
    emp_code = Column(String(100), nullable=True, unique=True)
    uan = Column(String(100), nullable=True)
