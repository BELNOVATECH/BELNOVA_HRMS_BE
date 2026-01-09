from sqlalchemy import select
from sqlalchemy.orm import Session
from fastapi import HTTPException
from sqlalchemy import desc

from models.candidate_applied_model import CandidateApplied
from schemas.candidate_applied_schema import CandidateAppliedCreate
from utils.date_utils import convert_date


def create_candidate_applied_service(
    data: CandidateAppliedCreate,
    db: Session
):
    dob = data.dob
    if isinstance(dob, str):
        dob = convert_date(dob)

    email_exists = (
        db.query(CandidateApplied)
        .filter(CandidateApplied.email == data.email)
        .first()
    )
    if email_exists:
        raise HTTPException(status_code=400, detail="Email already exists")

    mobile_exists = (
        db.query(CandidateApplied)
        .filter(CandidateApplied.mobile == data.mobile)
        .first()
    )
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


def update_candidate_applied_service(
    id: int,
    data,
    db: Session
):
    candidate = (
        db.query(CandidateApplied)
        .filter(CandidateApplied.id == id)
        .first()
    )

    if not candidate:
        raise HTTPException(status_code=404, detail="Candidate not found")

    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(candidate, field, value)

    db.commit()
    db.refresh(candidate)
    return candidate


def get_candidate_applied_service(db):
    return (
        db.query(CandidateApplied)
        .filter(CandidateApplied.is_active == True)
        .order_by(
            desc(CandidateApplied.modified_date),
            desc(CandidateApplied.created_date)
        )
        .all()
    )
