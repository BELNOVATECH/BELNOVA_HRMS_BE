from fastapi import APIRouter
from models.leave_balance import LeaveBalanceRequest
from services.leave_balance_service import leave_balance_controller

router = APIRouter(prefix="/leave", tags=["Leave Balance"])

@router.post("/balance")
def get_leave_balance(request: LeaveBalanceRequest):
    return leave_balance_controller(request.emp_id)
