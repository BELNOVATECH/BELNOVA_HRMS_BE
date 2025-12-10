from fastapi import APIRouter
from models.leaves import ApplyLeaveRequest
from services.leave_service import apply_leave, leave_history

router = APIRouter(prefix="/leave", tags=["Leave Management"])

@router.post("/apply")
def apply(payload: ApplyLeaveRequest):
    return apply_leave(payload)

@router.get("/history/{emp_id}")
def get_leave_history(emp_id: int):
    return leave_history(emp_id)
