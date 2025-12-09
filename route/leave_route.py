from fastapi import APIRouter
from controller.leave_controller import ApplyLeaveRequest
from services.leave_service import apply_leave, leave_history

router = APIRouter(prefix="/leave", tags=["Leave Management"])

@router.post("/apply", summary="Apply Leave")
def apply(payload: ApplyLeaveRequest):
    return apply_leave(payload)


@router.get("/history/{emp_id}", summary="Leave History")
def get_leave_history(emp_id: int):
    return leave_history(emp_id)
