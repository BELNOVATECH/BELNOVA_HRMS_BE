from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from core.database import get_db
from controller.auth_controller import login_controller
from schemas.auth_schema import UserRegister, UserResponse,LoginRequest, LoginResponse
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from services.auth_service import register_user as register_user_service
auth_router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@auth_router.post("/register", response_model=UserResponse)
def register_user(
    payload: UserRegister,
    db: Session = Depends(get_db)
):
    try:
        return register_user_service(db, payload)

    except Exception as e:
        print("REGISTER ERROR:", str(e))   # <-- add this
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )
    
@auth_router.post("/login", response_model=LoginResponse)
def login(payload: LoginRequest, db: Session = Depends(get_db)):
    return login_controller(payload, db)
