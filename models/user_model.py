from sqlalchemy import Column, Integer, String, Boolean, Date, DateTime, ForeignKey
from core.database import Base
from datetime import datetime


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)

    role_id = Column(Integer, ForeignKey("master_role.id"), nullable=False)
    gender_id = Column(Integer, nullable=True)

    mobile = Column(String, nullable=False)
    dob = Column(Date, nullable=True)

    email = Column(String, nullable=False, unique=True, index=True)
    password = Column(String, nullable=False)

    address = Column(String, nullable=True)

    created_by = Column(Integer, nullable=True)
    created_date = Column(DateTime, default=datetime.utcnow)

    modified_by = Column(Integer, nullable=True)
    modified_date = Column(DateTime, nullable=True)

    is_active = Column(Boolean, default=True)
