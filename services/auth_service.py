from sqlalchemy.orm import Session
from fastapi import HTTPException
from datetime import datetime, timedelta
from jose import jwt
from passlib.context import CryptContext

from models.generated_models import (
    Users,
    MasterRole,
    t_vw_screen_permission_list
)

from utils.hashing import verify_password

SECRET_KEY = "HRMS_SECRET"
ALGORITHM = "HS256"

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


def register_user(db: Session, payload):

    # Check existing user
    existing_user = (
        db.query(Users)
        .filter(Users.email == payload.email)
        .first()
    )

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )

    # Validate password
    if not payload.password:
        raise HTTPException(
            status_code=400,
            detail="Password is required"
        )

    # bcrypt limit
    if len(payload.password.encode("utf-8")) > 72:
        raise HTTPException(
            status_code=400,
            detail="Password must be 72 characters or less"
        )

    try:
        hashed_password = pwd_context.hash(payload.password)

    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=f"Password hashing failed: {str(e)}"
        )

    # Create User
    user = Users(
        first_name=payload.first_name,
        last_name=payload.last_name,
        role_id=payload.role_id,
        mobile=payload.mobile,
        email=payload.email,
        password=hashed_password,
        gender_id=payload.gender_id,
        dob=payload.dob,
        address=payload.address,
        is_active=True
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user


def login_service(payload, db: Session):

    user = (
        db.query(Users)
        .filter(
            Users.email == payload.email,
            Users.is_active == True
        )
        .first()
    )

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    if not verify_password(payload.password, user.password):
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    role = (
        db.query(MasterRole)
        .filter(
            MasterRole.id == user.role_id,
            MasterRole.is_active == True
        )
        .first()
    )

    if not role:
        raise HTTPException(
            status_code=403,
            detail="Role not assigned"
        )

    permissions = []

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