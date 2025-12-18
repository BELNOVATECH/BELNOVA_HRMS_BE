from sqlalchemy import select
from models.candidate_applied_model import CandidateApplied
from schemas.candidate_applied_schema import CandidateAppliedCreate
from fastapi import HTTPException
from utils.date_utils import convert_date


def create_candidate_applied_service(data: CandidateAppliedCreate, db):
    # Convert DOB if string
    dob = data.dob
    if isinstance(dob, str):
        dob = convert_date(dob)

    # Duplicate email check
    email_exists = db.execute(
        select(CandidateApplied).where(CandidateApplied.email == data.email)
    ).scalar_one_or_none()

    if email_exists:
        raise HTTPException(status_code=400, detail="Email already exists")

    # Duplicate mobile check
    mobile_exists = db.execute(
        select(CandidateApplied).where(CandidateApplied.mobile == data.mobile)
    ).scalar_one_or_none()

    if mobile_exists:
        raise HTTPException(status_code=400, detail="Mobile already exists")

    candidate = CandidateApplied(
        candidate_name=data.candidate_name,
        designation_id=data.designation_id,
        dob=dob,
        email=data.email,
        mobile=data.mobile,
        address=data.address,
        application_status_id=data.application_status_id,
        upload_resume=data.upload_resume
    )

    db.add(candidate)
    db.commit()
    db.refresh(candidate)

    return candidate


def update_candidate_applied_service(id: int, data, db):
    candidate = db.execute(
        select(CandidateApplied).where(CandidateApplied.id == id)
    ).scalar_one_or_none()

    if not candidate:
        raise HTTPException(status_code=404, detail="Candidate not found")

    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(candidate, field, value)

    db.commit()
    db.refresh(candidate)
    return candidate

def get_candidate_applied_service(db):
    result = db.execute(select(CandidateApplied))
    return result.scalars().all()