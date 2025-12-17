from services.interview_schedule_service import (
    create_interview_schedule_service,
    get_interview_schedule_service,
    update_interview_schedule_service,
    delete_interview_schedule_service
)

def create_interview_schedule_controller(data, db):
    return create_interview_schedule_service(data, db)

def get_interview_schedule_controller(db):
    return get_interview_schedule_service(db)

def update_interview_schedule_controller(db, interview_id, data):
    return update_interview_schedule_service(db, interview_id, data)

def delete_interview_schedule_controller(db, interview_id):
    return delete_interview_schedule_service(db, interview_id)
