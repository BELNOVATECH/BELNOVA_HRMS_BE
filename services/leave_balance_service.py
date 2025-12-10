leave_data = {
    1: {"emp_name": "Employee 1", "leaves_taken": {"Sick": 2, "Casual": 1, "Paid": 0}},
    2: {"emp_name": "Employee 2", "leaves_taken": {"Sick": 1, "Casual": 2, "Paid": 3}},
    3: {"emp_name": "Employee 3", "leaves_taken": {"Sick": 5, "Casual": 2, "Paid": 1}},
}

SICK_TOTAL = 10
CASUAL_TOTAL = 8
PAID_TOTAL = 6


def leave_balance_controller(emp_id: int):
    emp = leave_data.get(emp_id)

    if not emp:
        return {"message": "Employee not found"}

    taken = emp["leaves_taken"]

    return {
        "emp_name": emp["emp_name"],
        "leaves": [
            {
                "type_of_leave": "Sick",
                "total_leaves": SICK_TOTAL,
                "leaves_taken": taken.get("Sick", 0),
                "leaves_remaining": SICK_TOTAL - taken.get("Sick", 0)
            },
            {
                "type_of_leave": "Casual",
                "total_leaves": CASUAL_TOTAL,
                "leaves_taken": taken.get("Casual", 0),
                "leaves_remaining": CASUAL_TOTAL - taken.get("Casual", 0)
            },
            {
                "type_of_leave": "Paid",
                "total_leaves": PAID_TOTAL,
                "leaves_taken": taken.get("Paid", 0),
                "leaves_remaining": PAID_TOTAL - taken.get("Paid", 0)
            }
        ]
    }
