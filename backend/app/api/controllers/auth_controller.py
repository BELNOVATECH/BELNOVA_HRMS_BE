from app.api.helpers.response_builder import response
from app.db.connection import get_connection
import bcrypt


def fetch_all_employees():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM employee_registration ORDER BY 1;")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows


def create_user(user):
    conn = get_connection()
    cur = conn.cursor()

    try:
        # Hash password
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(user.password.encode("utf-8"), salt).decode(
            "utf-8"
        )

        query = """
            SELECT * FROM fn_create_user_and_employee(
                %s, %s, %s, %s, %s,
                %s, %s, %s, %s, %s,
                %s, %s, %s, %s, %s,
                %s, %s, %s, %s, %s,
                %s, %s, %s, %s, %s,
                %s, %s
            );
        """

        cur.execute(
            query,
            (
                user.first_name,
                user.last_name,
                user.role_id,
                user.gender_id,
                user.mobile,
                user.email,
                hashed_password,
                user.created_by,
                user.civil_status_id,
                user.position_id,
                user.pay_method_id,
                user.department_id,
                user.work_status_id,
                user.salary,
                user.join_date,
                user.emp_code,
                user.dob,
                user.emergency_mobile,
                user.hired_date,
                user.manager_id,
                user.upload_doc,
                user.bank_id,
                user.bank_ac_no,
                user.ifsc_code,
                user.esic,
                user.pan,
                user.address,
            ),
        )

        result = cur.fetchone()
        conn.commit()

        if not result:
            raise Exception("Function returned no result")

        data = dict(result)

        return response(
            success=True,
            message="User and Employee created successfully",
            data={
                "user_id": data["user_id"],
                "username": data["user_name"],
                "email": data["user_email"],
                "role_name": data["role_name"],
                "employee_id": data["employee_id"],
            },
        )

    except Exception as e:
        conn.rollback()
        raise e

    finally:
        cur.close()
        conn.close()    



def login_user(login):
    conn = get_connection()
    cur = conn.cursor()

    try:
        cur.execute(
            "SELECT * FROM fn_get_user_by_email(%s);",
            (login.email.strip().lower(),)
        )
        row = cur.fetchone()

        if not row:
            return response(success=False, message="Invalid email or password")

        columns = [desc[0] for desc in cur.description]
        user = dict(zip(columns, row))

        stored_hash = user.get("password")

        # ------------------------- FIX START -------------------------
        if stored_hash is None:
            return response(success=False, message="Invalid email or password")

        # Convert memoryview / bytearray → bytes
        if isinstance(stored_hash, (memoryview, bytearray)):
            stored_hash = bytes(stored_hash)

        # Convert bytes → string
        if isinstance(stored_hash, bytes):
            stored_hash = stored_hash.decode("utf-8", errors="ignore")

        # Remove b'xxx'
        if isinstance(stored_hash, str) and stored_hash.startswith("b'") and stored_hash.endswith("'"):
            stored_hash = stored_hash[2:-1]

        # Trim whitespace/newlines
        stored_hash = stored_hash.strip()

        # bcrypt MUST receive exactly a clean 60-char hash
        if len(stored_hash) != 60 or not stored_hash.startswith("$2"):
            return response(success=False, message="Invalid email or password")
        # ------------------------- FIX END ---------------------------

        if not bcrypt.checkpw(login.password.encode("utf-8"), stored_hash.encode("utf-8")):
            return response(success=False, message="Invalid email or password")

        login_payload = {
            "user_id": user["id"],
            "email": user["email"],
            "user_name": user["user_name"],
            "role_id": user["role_id"],
            "role_name": user["role_name"],
        }

        return response(success=True, message="Login Successful", data=login_payload)

    except Exception as e:
        conn.rollback()
        raise e

    finally:
        cur.close()
        conn.close()

