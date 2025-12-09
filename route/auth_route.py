from fastapi import APIRouter
from controller.auth_controller import RegisterUser, LoginUser
from services.auth_service import register_user, login_user

router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/register")
def register(payload: RegisterUser):
    return register_user(payload)

@router.post("/login")
def login(payload: LoginUser):
    return login_user(payload)
