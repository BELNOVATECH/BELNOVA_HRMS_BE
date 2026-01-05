from pydantic import BaseModel, EmailStr
from datetime import date
from typing import Optional


class FamilyMemberCreate(BaseModel):
    relation_id: int
    first_name: str
    last_name: Optional[str] = None

    date_of_birth: date
    occupation_id: int

    phone: Optional[str] = None
    email: Optional[EmailStr] = None

    present_address: str
    permanent_address: str

    bank_account: Optional[str] = None
    ifsc_code: Optional[str] = None
    pan: Optional[str] = None
    aadhar: Optional[str] = None
