from models.leaves import ApplyLeaveRequest, ApplyLeaveResponse

leave_list = []
leave_id_tracker = {}

def apply_leave(payload: ApplyLeaveRequest):
    if payload.emp_id not in leave_id_tracker:
        leave_id_tracker[payload.emp_id] = 1

    leave_id = leave_id_tracker[payload.emp_id]

    new_leave = {
        "leave_id": leave_id,
        "emp_id": payload.emp_id,
        "from_date": payload.from_date,
        "to_date": payload.to_date,
        "no_of_days": payload.no_of_days,
        "session_start": payload.session_start,
        "session_end": payload.session_end,
        "type_of_leave": payload.type_of_leave,
        "reason": payload.reason,
        "upload_files": payload.upload_files,
        "leave_status": "Pending",
        "approved_by": payload.approved_by,
        "approved_on": payload.approved_on,
    }

    leave_list.append(new_leave)
    leave_id_tracker[payload.emp_id] += 1

    return ApplyLeaveResponse(
        leave_id=new_leave["leave_id"],
        leave_status=new_leave["leave_status"],
        approved_by=new_leave["approved_by"],
        approved_on=new_leave["approved_on"]
    )


def leave_history(emp_id: int):
    return [leave for leave in leave_list if leave["emp_id"] == emp_id]
