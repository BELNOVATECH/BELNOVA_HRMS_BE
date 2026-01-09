from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from core.database import get_db
from controller.auth_controller import login_controller
from schemas.auth_schema import LoginRequest, LoginResponse

auth_router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@auth_router.post("/login", response_model=LoginResponse)
def login(payload: LoginRequest, db: Session = Depends(get_db)):
    return login_controller(payload, db)
