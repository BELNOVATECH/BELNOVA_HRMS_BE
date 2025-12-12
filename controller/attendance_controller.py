# controller/attendance_controller.py
import pandas as pd
from fastapi.responses import FileResponse
from services.attendance_service import get_attendance_service


def get_attendance_controller(db, emp_id=None, from_date=None, to_date=None, export=False):
    records = get_attendance_service(db, emp_id, from_date, to_date)

    # ---- FORMAT RECORDS ----
    formatted = []
    for r in records:
        formatted.append({
            "id": r.id,
            "emp_id": r.emp_id,
            "attendance_date": r.attendance_date.strftime("%Y-%m-%d"),
            "check_in_time": r.check_in_time.strftime("%Y-%m-%d %H:%M:%S") if r.check_in_time else None,
            "check_out_time": r.check_out_time.strftime("%Y-%m-%d %H:%M:%S") if r.check_out_time else None,
            "working_status_id": r.working_status_id,
            "working_hours": r.working_hours.total_seconds() / 3600 if r.working_hours else None,
            "remarks": r.remarks,
            "created_by": r.created_by,
        })

    # ---- EXPORT EXCEL ----
    if export:
        filename = "attendance_export.xlsx"

        df = pd.DataFrame(formatted)
        df.to_excel(filename, index=False)

        return FileResponse(
            path=filename,
            media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            filename=filename
        )

    # ---- RETURN JSON ----
    return formatted
