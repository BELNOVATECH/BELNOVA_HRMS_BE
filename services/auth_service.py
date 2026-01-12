from sqlalchemy.orm import Session
from fastapi import HTTPException
from datetime import datetime, timedelta
import jwt

from models.user_model import User
from models.master_role_model import MasterRole
from models.master_module import MasterModule
from models.master_screen import MasterScreen
from models.master_screen_permission import MasterScreenPermission
from utils.hashing import verify_password   # 🔥 use hashing utils

SECRET_KEY = "HRMS_SECRET"
ALGORITHM = "HS256"


def login_service(payload, db: Session):

    user = db.query(User).filter(
        User.email == payload.email,
        User.is_active == True
    ).first()

    if not user:
        raise HTTPException(401, "Invalid email or password")

    # 🔥 CORRECT password check
    if not verify_password(payload.password, user.password):
        raise HTTPException(401, "Invalid email or password")

    role = db.query(MasterRole).filter(
        MasterRole.id == user.role_id,
        MasterRole.is_active == True
    ).first()

    if not role:
        raise HTTPException(403, "Role not assigned")

    permissions = (
        db.query(
            MasterModule.id.label("module_id"),
            MasterModule.module_name,
            MasterScreen.id.label("screen_id"),
            MasterScreen.screen_name,
            MasterScreenPermission.can_view,
            MasterScreenPermission.can_edit,
            MasterScreenPermission.can_delete,
            MasterScreenPermission.can_update,
            MasterScreenPermission.can_access,
        )
        .join(MasterScreen, MasterScreen.module_id == MasterModule.id)
        .join(MasterScreenPermission, MasterScreenPermission.screen_id == MasterScreen.id)
        .filter(
            MasterScreenPermission.role_id == role.id,
            MasterScreenPermission.is_active == True,
            MasterScreenPermission.can_access == True
        )
        .all()
    )

    token = jwt.encode(
        {
            "user_id": user.id,
            "role_id": role.id,
            "exp": datetime.utcnow() + timedelta(hours=12)
        },
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return {
        "user_id": user.id,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "role_id": role.id,
        "role_name": role.role_name,
        "permissions": permissions,
        "token": token
    }
