# models/vw_screen_permission_model.py

from sqlalchemy import Column, Integer, String, Boolean
from core.database import Base

class VwScreenPermissionList(Base):
    __tablename__ = "vw_screen_permission_list"

    module_id = Column(Integer, primary_key=True)
    module_name = Column(String)
    screen_id = Column(Integer)
    screen_name = Column(String)
    role_id = Column(Integer)
    role_name = Column(String)
    can_view = Column(Boolean)
    can_edit = Column(Boolean)
    can_delete = Column(Boolean)
    can_update = Column(Boolean)
    can_access = Column(Boolean)
