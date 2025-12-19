from services.interview_schedule_service import (
    schedule_interview_service,
    create_interview_schedule_service,
    get_interview_schedule_service,
    update_interview_schedule_service,
    delete_interview_schedule_service
)


# NEW – schedule interview
def schedule_interview_controller(payload, db):
    return schedule_interview_service(payload, db)


# CRUD
def create_interview_schedule_controller(payload, db):
    return create_interview_schedule_service(payload, db)


def get_interview_schedule_controller(db):
    return get_interview_schedule_service(db)


def update_interview_schedule_controller(db, interview_id, payload):
    return update_interview_schedule_service(db, interview_id, payload)


def delete_interview_schedule_controller(db, interview_id):
    return delete_interview_schedule_service(db, interview_id)
