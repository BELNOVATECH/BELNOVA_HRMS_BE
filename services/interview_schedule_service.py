from sqlalchemy import select
from fastapi import HTTPException
from models.interview_schedule_model import InterviewSchedule

def create_interview_schedule_service(data, db):
    interview = InterviewSchedule(
        candidate_id=data.candidate_id,
        position_id=data.position_id,
        status_id=data.status_id,
        stage_id=data.stage_id,
        interview_date=data.interview_date,
        rating=data.rating,
        feedback=data.feedback,
        created_by=data.created_by,
    )

    db.add(interview)
    db.commit()
    db.refresh(interview)
    return interview
def update_interview_schedule_service(db, interview_id, data):
    interview = db.execute(
        select(InterviewSchedule).where(InterviewSchedule.id == interview_id)
    ).scalar_one_or_none()

    if not interview:
        raise HTTPException(status_code=404, detail="Interview not found")

    interview.candidate_id = data.candidate_id
    interview.position_id = data.position_id
    interview.status_id = data.status_id
    interview.stage_id = data.stage_id
    interview.interview_date = data.interview_date
    interview.rating = data.rating
    interview.feedback = data.feedback
    interview.created_by = data.created_by

    db.commit()
    db.refresh(interview)
    return interview

def delete_interview_schedule_service(db, interview_id):
    interview = db.execute(
        select(InterviewSchedule).where(InterviewSchedule.id == interview_id)
    ).scalar_one_or_none()

    if not interview:
        raise HTTPException(status_code=404, detail="Interview not found")

    db.delete(interview)
    db.commit()
    return {"message": "Interview deleted successfully"}


def get_interview_schedule_service(db):
    result = db.execute(select(InterviewSchedule))
    return result.scalars().all()