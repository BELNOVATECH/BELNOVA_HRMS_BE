from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from core.database import Base

class Designation(Base):
    __tablename__ = "master_designation"

    id = Column(Integer, primary_key=True, index=True)
    designation_name = Column(String(100), nullable=False)

    # ✅ keep FK exactly as per DB
    dept_id = Column(
        Integer,
        ForeignKey("master_department.id"),
        nullable=False
    )

    is_active = Column(Boolean, default=True)
