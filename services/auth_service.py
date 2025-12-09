from utils.hashing import hash_password, verify_password

# In-memory storage
users = []
employee_id_counter = 1  # auto-generate employee ID incrementally

def register_user(payload):
    global employee_id_counter

    # Check if email already exists
    for user in users:
        if user["email"] == payload.email:
            return {"message": "User already exists"}

    # Create new user with auto emp_id
    new_user = {
        "emp_id": employee_id_counter,  # Auto-generated
        "full_name": payload.full_name,
        "email": payload.email,
        "phone": payload.phone,
        "password": hash_password(payload.password)
    }

    users.append(new_user)
    employee_id_counter += 1  # Increment for next user

    return {
        "message": "Registration successful",
        "emp_id": new_user["emp_id"],     # return emp_id in output
        "email": new_user["email"]
    }


def login_user(payload):
    for user in users:
        if user["email"] == payload.email and verify_password(payload.password, user["password"]):
            return {
                "message": "Login successful",
                "emp_id": user["emp_id"],     # return same stored emp_id
                "email": user["email"]
            }

    return {"message": "Invalid email or password"}
