from utils.db import get_connection
from utils.activate_checker import is_active_name


def create_job(position: str):
    is_active = is_active_name(position)

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """INSERT INTO master_position (position, is_active)
           VALUES (%s, %s)
           RETURNING id, position, is_active""",
        (position, is_active)
    )

    job = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()

    return job


def get_job(job_id: int):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM master_position WHERE id = %s", (job_id,))
    job = cur.fetchone()

    cur.close()
    conn.close()
    return job


def get_all_jobs():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM master_position ORDER BY id")
    jobs = cur.fetchall()

    # auto-update invalid values
    for job in jobs:
        expected = is_active_name(job["position"])
        if job["is_active"] != expected:
            cur.execute(
                "UPDATE master_position SET is_active = %s WHERE id = %s",
                (expected, job["id"])
            )

    conn.commit()
    cur.close()
    conn.close()

    return jobs
