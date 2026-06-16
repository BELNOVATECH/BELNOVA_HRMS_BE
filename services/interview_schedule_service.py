from datetime import datetime
from sqlalchemy.orm import Session
from sqlalchemy import desc
from fastapi import HTTPException

from models.generated_models import (
    CandidateApplied,
    MasterStage,
    InterviewScheduled
)


def schedule_interview_service(payload, db: Session):

    candidate = db.query(CandidateApplied).filter(
        CandidateApplied.id == payload.candidate_id,
        CandidateApplied.is_active == True
    ).first()

    if not candidate:
        raise HTTPException(
            status_code=404,
            detail="Candidate not found"
        )

    stage = db.query(MasterStage).filter(
        MasterStage.id == payload.stage_id,
        MasterStage.is_active == True
    ).first()

    if not stage:
        raise HTTPException(
            status_code=404,
            detail="Interview stage not found"
        )

    interview = InterviewScheduled(
        candidate_id=payload.candidate_id,
        designation_id=payload.designation_id,
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


def get_interview_schedule_service(db: Session):
    return (
        db.query(InterviewScheduled)
        .filter(
            InterviewScheduled.is_active == True
        )
        .order_by(
            desc(InterviewScheduled.modified_date),
            desc(InterviewScheduled.created_date)
        )
        .all()
    )


def get_interview_schedule_by_id_service(
    interview_id: int,
    db: Session
):
    interview = db.query(
        InterviewScheduled
    ).filter(
        InterviewScheduled.id == interview_id,
        InterviewScheduled.is_active == True
    ).first()

    if not interview:
        raise HTTPException(
            status_code=404,
            detail="Interview schedule not found"
        )

    return interview


def update_interview_schedule_service(
    interview_id: int,
    payload,
    db: Session
):
    interview = get_interview_schedule_by_id_service(
        interview_id,
        db
    )

    for key, value in payload.model_dump(
        exclude_unset=True
    ).items():
        setattr(interview, key, value)

    interview.modified_date = datetime.utcnow()

    db.commit()
    db.refresh(interview)

    return interview


def delete_interview_schedule_service(
    interview_id: int,
    db: Session
):
    interview = get_interview_schedule_by_id_service(
        interview_id,
        db
    )

    interview.is_active = False
    interview.modified_date = datetime.utcnow()

    db.commit()

    return {
        "message": "Interview schedule deleted successfully"
    }