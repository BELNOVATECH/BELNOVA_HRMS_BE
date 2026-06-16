from services.interview_schedule_service import (
    schedule_interview_service,
    get_interview_schedule_service,
    get_interview_schedule_by_id_service,
    update_interview_schedule_service,
    delete_interview_schedule_service
)


def schedule_interview_controller(
    payload,
    db
):
    return schedule_interview_service(
        payload,
        db
    )


def get_interview_schedule_controller(
    db
):
    return get_interview_schedule_service(
        db
    )


def get_interview_schedule_by_id_controller(
    interview_id,
    db
):
    return get_interview_schedule_by_id_service(
        interview_id,
        db
    )


def update_interview_schedule_controller(
    interview_id,
    payload,
    db
):
    return update_interview_schedule_service(
        interview_id,
        payload,
        db
    )


def delete_interview_schedule_controller(
    interview_id,
    db
):
    return delete_interview_schedule_service(
        interview_id,
        db
    )