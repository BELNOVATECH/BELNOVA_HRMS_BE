from sqlalchemy.orm import Session
from fastapi import HTTPException
from datetime import datetime

from models.candidate_applied_model import CandidateApplied
from models.interview_stage import InterviewStage
from models.interview_schedule_model import InterviewSchedule


# =================================================
# Schedule interview from applied candidate
# =================================================
def schedule_interview_service(payload, db: Session):

    candidate = db.query(CandidateApplied).filter(
        CandidateApplied.id == payload.candidate_applied_id,
        CandidateApplied.is_active == True
    ).first()

    if not candidate:
        raise HTTPException(404, "Candidate application not found")

    stage = db.query(InterviewStage).filter(
        InterviewStage.id == payload.stage_id,
        InterviewStage.is_active == True
    ).first()

    if not stage:
        raise HTTPException(404, "Interview stage not found")

    exists = db.query(InterviewSchedule).filter(
        InterviewSchedule.candidate_id == candidate.id,
        InterviewSchedule.stage_id == payload.stage_id,
        InterviewSchedule.is_active == True
    ).first()

    if exists:
        raise HTTPException(400, "Interview already scheduled for this stage")

    interview = InterviewSchedule(
        candidate_id=candidate.id,
        designation_id=payload.designation_id,   # ✅ changed
        status_id=payload.status_id,
        stage_id=payload.stage_id,
        interview_date=payload.interview_date,
        created_by=payload.created_by,
        created_date=datetime.utcnow(),
        is_active=True
    )

    db.add(interview)
    db.commit()
    db.refresh(interview)

    return interview


# =================================================
# CRUD
# =================================================
def create_interview_schedule_service(payload, db: Session):
    interview = InterviewSchedule(**payload.dict())
    db.add(interview)
    db.commit()
    db.refresh(interview)
    return interview


def get_interview_schedule_service(db: Session):
    return db.query(InterviewSchedule).filter(
        InterviewSchedule.is_active == True
    ).all()


def update_interview_schedule_service(db: Session, interview_id: int, payload):
    interview = db.query(InterviewSchedule).filter(
        InterviewSchedule.id == interview_id,
        InterviewSchedule.is_active == True
    ).first()

    if not interview:
        raise HTTPException(404, "Interview schedule not found")

    for key, value in payload.dict(exclude_unset=True).items():
        setattr(interview, key, value)

    interview.modified_date = datetime.utcnow()
    db.commit()
    db.refresh(interview)

    return interview


def delete_interview_schedule_service(db: Session, interview_id: int):
    interview = db.query(InterviewSchedule).filter(
        InterviewSchedule.id == interview_id,
        InterviewSchedule.is_active == True
    ).first()

    if not interview:
        raise HTTPException(404, "Interview schedule not found")

    interview.is_active = False
    db.commit()

    return {"message": "Interview schedule deleted successfully"}
