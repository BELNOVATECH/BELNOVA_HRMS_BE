from sqlalchemy import Column, Integer, String, Boolean
from core.database import Base


class MasterRole(Base):
    __tablename__ = "master_role"

    id = Column(Integer, primary_key=True, index=True)
    role_name = Column(String, nullable=False, unique=True)
    is_active = Column(Boolean, default=True)
