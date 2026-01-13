# services/auth_service.py

from sqlalchemy.orm import Session
from fastapi import HTTPException
from datetime import datetime, timedelta
import jwt

from models.user_model import User
from models.master_role_model import MasterRole
from models.vw_screen_permission_list import VwScreenPermissionList
from utils.hashing import verify_password

SECRET_KEY = "HRMS_SECRET"
ALGORITHM = "HS256"


def login_service(payload, db: Session):

    # 1️⃣ Find active user
    user = db.query(User).filter(
        User.email == payload.email,
        User.is_active == True
    ).first()

    if not user:
        raise HTTPException(401, "Invalid email or password")

    # 2️⃣ Verify password
    if not verify_password(payload.password, user.password):
        raise HTTPException(401, "Invalid email or password")

    # 3️⃣ Get Role
    role = db.query(MasterRole).filter(
        MasterRole.id == user.role_id,
        MasterRole.is_active == True
    ).first()

    if not role:
        raise HTTPException(403, "Role not assigned")

    # 4️⃣ Fetch permissions via VIEW (🔥 your query)
    permissions = db.query(VwScreenPermissionList).filter(
        (VwScreenPermissionList.role_id == role.id) |
        (VwScreenPermissionList.role_id == -1)
    ).all()

    # 5️⃣ Generate JWT
    token = jwt.encode(
        {
            "user_id": user.id,
            "role_id": role.id,
            "exp": datetime.utcnow() + timedelta(hours=12)
        },
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    # 6️⃣ Build response
    return {
        "user_id": user.id,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "role_id": role.id,
        "role_name": role.role_name,
        "permissions": permissions,
        "token": token
    }
