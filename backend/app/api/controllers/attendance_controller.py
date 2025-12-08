from app.db.connection import get_connection
from fastapi import HTTPException
from typing import List, Optional
from pydantic import BaseModel
from app.utils.date_utils import convert_date, convert_datetime
from psycopg2.extras import RealDictCursor  # <-- import

class AttendanceCreate(BaseModel):
    emp_id: int
    attendance_date: str
    check_in_time: str    
    check_out_time: str   
    working_status_id: int
    remarks: Optional[str]
    created_by: int

class AttendanceResponse(BaseModel):
    attendance_id: int
    emp_id: int
    emp_name: str
    attendance_date: str
    check_in_time: str
    check_out_time: str
    working_status_id: int
    working_status_name: Optional[str]
    working_hours: Optional[str]
    remarks: Optional[str]
    created_by: int
    created_by_name: Optional[str]

def create_attendance(att: AttendanceCreate) -> dict:
    conn = get_connection()
    cur = conn.cursor()
    try:
        # Convert strings to proper date/datetime objects
        attendance_date = convert_date(att.attendance_date)
        check_in_time = convert_datetime(att.check_in_time)
        check_out_time = convert_datetime(att.check_out_time)

        query = """SELECT * FROM fn_create_attendance_tracker(
            %s, %s, %s, %s, %s, %s, %s
        );"""
        cur.execute(query, (
            att.emp_id,
            attendance_date,
            check_in_time,
            check_out_time,
            att.working_status_id,
            att.remarks,
            att.created_by
        ))

        row = cur.fetchone()
        conn.commit()

        if not row or row[1] is None:  # row[1] is attendance_id
            raise HTTPException(
                status_code=404, 
                detail=f"Employee not found or attendance creation failed for emp_id: {att.emp_id}"
            )

        emp_id, attendance_id, emp_name = row
        message = f"Attendance created for employee: {emp_name} (ID: {emp_id}), Attendance ID: {attendance_id}"

        return {
            "emp_id": emp_id,
            "attendance_id": attendance_id,
            "message": message
        }

    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        cur.close()
        conn.close()


def get_attendance(emp_id: int = -1) -> List[AttendanceResponse]:
    conn = get_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)  # <-- return dicts
    try:
        if emp_id == -1:
            cur.execute("SELECT * FROM fn_get_attendance_list();")
        else:
            cur.execute("SELECT * FROM fn_get_attendance_list(%s);", (emp_id,))

        rows = cur.fetchall()
        if not rows:
            raise HTTPException(status_code=404, detail="No attendance found")

        response = []
        for r in rows:
            response.append(AttendanceResponse(
                attendance_id=r["attendance_id"],
                emp_id=r["emp_id"],
                emp_name=r["emp_name"],
                attendance_date=r["attendance_date"],
                check_in_time=r["check_in_time"],
                check_out_time=r["check_out_time"],
                working_status_id=r["working_status_id"],
                working_status_name=r.get("working_status_name"),
                working_hours=str(r["working_hours"]) if r.get("working_hours") else None,
                remarks=r.get("remarks"),
                created_by=r["created_by"],
                created_by_name=r.get("created_by_name")
            ))
        return response
    finally:
        cur.close()
        conn.close()
