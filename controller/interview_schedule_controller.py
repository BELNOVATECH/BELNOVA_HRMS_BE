from services.interview_schedule_service import (
    create_interview_schedule_service,
    get_interview_schedule_service,
)

def create_interview_schedule_controller(data, db):
    return create_interview_schedule_service(data, db)

def get_interview_schedule_controller(db):
    return get_interview_schedule_service(db)
