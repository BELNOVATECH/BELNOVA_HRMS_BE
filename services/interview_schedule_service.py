from sqlalchemy import select
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


def get_interview_schedule_service(db):
    result = db.execute(select(InterviewSchedule))
    return result.scalars().all()