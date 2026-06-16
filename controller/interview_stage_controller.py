from sqlalchemy.orm import Session

from services.interview_stage_service import (
    create_interview_stage,
    get_all_interview_stages,
    get_interview_stage_by_id,
    update_interview_stage,
    update_interview_stage_is_active,
    delete_interview_stage
)


def create_interview_stage_controller(
    req,
    db: Session
):
    return create_interview_stage(
        req,
        db
    )


def get_all_interview_stages_controller(
    db: Session
):
    return get_all_interview_stages(
        db
    )


def get_interview_stage_by_id_controller(
    stage_id: int,
    db: Session
):
    return get_interview_stage_by_id(
        stage_id,
        db
    )


def update_interview_stage_controller(
    stage_id: int,
    req,
    db: Session
):
    return update_interview_stage(
        stage_id,
        req,
        db
    )


def update_interview_stage_is_active_controller(
    stage_id: int,
    req,
    db: Session
):
    return update_interview_stage_is_active(
        stage_id,
        req,
        db
    )


def delete_interview_stage_controller(
    stage_id: int,
    db: Session
):
    return delete_interview_stage(
        stage_id,
        db
    )