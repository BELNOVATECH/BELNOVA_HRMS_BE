from pydantic import BaseModel, EmailStr, Field, validator
import re

class RegisterUser(BaseModel):
    full_name: str
    email: EmailStr
    phone: str
    password: str
    confirm_password: str

    @validator("email")
    def validate_email(cls, v):
        if not v.endswith("@gmail.com"):
            raise ValueError("Only @gmail.com email addresses are allowed")
        return v

    @validator("phone")
    def validate_phone(cls, v):
        if not re.fullmatch(r"[6-9]\d{9}", v):
            raise ValueError("Enter a valid 10-digit Indian phone number")
        return v

    @validator("password")
    def validate_password(cls, v):
        pattern = r"^[A-Z](?=.*[0-9])(?=.*[^A-Za-z0-9]).{6,}$"
        if not re.match(pattern, v):
            raise ValueError("Password must start with uppercase, contain numbers & special character, minimum 8 characters")
        return v
    

    @validator("confirm_password")
    def validate_confirm_password(cls, v, values):
        if "password" in values and v != values["password"]:
            raise ValueError("Password and Confirm Password must match")
        return v


class LoginUser(BaseModel):
    email: EmailStr
    password: str

    @validator("email")
    def validate_email(cls, v):
        if not v.endswith("@gmail.com"):
            raise ValueError("Only @gmail.com allowed")
        return v
