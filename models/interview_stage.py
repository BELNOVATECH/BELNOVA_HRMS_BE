from sqlalchemy import Column, Integer, String, Boolean, DateTime
from datetime import datetime

from core.database import Base


class InterviewStage(Base):
    __tablename__ = "master_stage"

    id = Column(Integer, primary_key=True, index=True)
    stage_name = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    


