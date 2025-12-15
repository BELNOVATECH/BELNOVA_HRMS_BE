from sqlalchemy.orm import Session
from fastapi import HTTPException

from models.interview_stage import InterviewStage
from schemas.interview_stage_schema import (
    InterviewStageCreate,
    InterviewStageUpdate
)


def create_interview_stage(req: InterviewStageCreate, db: Session):
    stage = InterviewStage(
        stage_name=req.stage_name,
        description=req.description,
        is_active=req.is_active
    )
    db.add(stage)
    db.commit()
    db.refresh(stage)
    return stage


def get_all_interview_stages(db: Session):
    return db.query(InterviewStage).all()


def get_interview_stage_by_id(stage_id: int, db: Session):
    stage = db.query(InterviewStage).filter(InterviewStage.id == stage_id).first()
    if not stage:
        raise HTTPException(status_code=404, detail="Interview stage not found")
    return stage


def update_interview_stage(stage_id: int, req: InterviewStageUpdate, db: Session):
    stage = get_interview_stage_by_id(stage_id, db)

    if req.stage_name is not None:
        stage.stage_name = req.stage_name
    if req.description is not None:
        stage.description = req.description
    if req.is_active is not None:
        stage.is_active = req.is_active

    db.commit()
    db.refresh(stage)
    return stage


def delete_interview_stage(stage_id: int, db: Session):
    stage = get_interview_stage_by_id(stage_id, db)
    db.delete(stage)
    db.commit()
    return {"message": "Interview stage deleted successfully"}
