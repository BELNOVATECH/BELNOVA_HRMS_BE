from sqlalchemy.orm import Session
from fastapi import HTTPException

from models.generated_models import MasterStage


def create_interview_stage(req, db: Session):
    stage = MasterStage(
        stage_name=req.stage_name,
        is_active=req.is_active
    )

    db.add(stage)
    db.commit()
    db.refresh(stage)

    return stage


def get_all_interview_stages(db: Session):
    return db.query(MasterStage).all()


def get_interview_stage_by_id(
    stage_id: int,
    db: Session
):
    stage = db.query(MasterStage).filter(
        MasterStage.id == stage_id
    ).first()

    if not stage:
        raise HTTPException(
            status_code=404,
            detail="Interview stage not found"
        )

    return stage


def update_interview_stage(
    stage_id: int,
    req,
    db: Session
):
    stage = get_interview_stage_by_id(
        stage_id,
        db
    )

    if req.stage_name is not None:
        stage.stage_name = req.stage_name

    if req.is_active is not None:
        stage.is_active = req.is_active

    db.commit()
    db.refresh(stage)

    return stage


def update_interview_stage_is_active(
    stage_id: int,
    req,
    db: Session
):
    stage = get_interview_stage_by_id(
        stage_id,
        db
    )

    stage.is_active = req.is_active

    db.commit()
    db.refresh(stage)

    return stage


def delete_interview_stage(
    stage_id: int,
    db: Session
):
    stage = get_interview_stage_by_id(
        stage_id,
        db
    )

    db.delete(stage)
    db.commit()

    return {
        "message": "Interview stage deleted successfully"
    }