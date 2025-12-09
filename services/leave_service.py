from controller.leave_controller import ApplyLeaveRequest, ApplyLeaveResponse

# Temporary leave storage
leave_list = []

# Leave ID counter per employee
leave_id_tracker = {}   # Example internal store: {1: 3, 2: 1}

def apply_leave(payload: ApplyLeaveRequest):
    # Initialize leave counter for emp_id if not exists
    if payload.emp_id not in leave_id_tracker:
        leave_id_tracker[payload.emp_id] = 1

    # Assign leave_id for this employee
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

    # Increment the leave counter only for this employee
    leave_id_tracker[payload.emp_id] += 1

    # Response payload
    return ApplyLeaveResponse(
        leave_id=new_leave["leave_id"],
        leave_status=new_leave["leave_status"],
        approved_by=new_leave["approved_by"],
        approved_on=new_leave["approved_on"]
    )


def leave_history(emp_id: int):
    history = []

    for leave in leave_list:
        if leave["emp_id"] == emp_id:
            history.append({
                "leave_id": leave["leave_id"],
                "from_date": leave["from_date"],
                "to_date": leave["to_date"],
                "session_start": leave["session_start"],
                "session_end": leave["session_end"],
                "no_of_days": leave["no_of_days"],
                "type_of_leave": leave["type_of_leave"],
                "approver": leave["approved_by"],
                "approved_by": leave["approved_by"],
                "approved_on": leave["approved_on"]
            })

    return history
