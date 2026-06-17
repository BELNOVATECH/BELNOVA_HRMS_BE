# services/auth_service.py

from sqlalchemy.orm import Session
from fastapi import HTTPException
from datetime import datetime, timedelta
from jose import jwt
from passlib.context import CryptContext
from schemas.auth_schema import UserRegister
from models.generated_models import Users, MasterRole,t_vw_screen_permission_list
from utils.hashing import verify_password

SECRET_KEY = "HRMS_SECRET"
ALGORITHM = "HS256"

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

def register_user(db, payload):

    existing_user = (
        db.query(Users)
        .filter(Users.email == payload.email)
        .first()
    )

    if existing_user:
        raise Exception("Email already exists")

    hashed_password = pwd_context.hash(str(payload.password))

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

    user = db.query(Users).filter(
        Users.email == payload.email,
        Users.is_active == True
    ).first()

    if not user:
        raise HTTPException(401, "Invalid email or password")

    print("Stored Password:", repr(user.password))

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
    permissions = []

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
