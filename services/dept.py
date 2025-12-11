from utils.db import get_connection
from utils.activate_checker import is_active_name   # ✅ correct function


def create_department(department: str):
    # Determine active status
    is_active = is_active_name(department)

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """INSERT INTO master_department (department, is_active)
           VALUES (%s, %s)
           RETURNING id, department, is_active""",
        (department, is_active)
    )

    dept = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()

    return dept


def get_department(dept_id: int):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM master_department WHERE id = %s", (dept_id,))
    dept = cur.fetchone()

    cur.close()
    conn.close()
    return dept


def get_all_departments():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM master_department ORDER BY id")
    departments = cur.fetchall()

    # Auto-fix incorrect is_active values
    for dept in departments:
        expected = is_active_name(dept["department"])   # ✅ correct function
        if dept["is_active"] != expected:
            cur.execute(
                "UPDATE master_department SET is_active = %s WHERE id = %s",
                (expected, dept["id"])
            )

    conn.commit()
    cur.close()
    conn.close()

    return departments
