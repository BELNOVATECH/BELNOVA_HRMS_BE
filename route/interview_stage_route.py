from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from core.database import get_db
from schemas.interview_stage_schema import (
    InterviewStageCreate,
    InterviewStageUpdate,
    InterviewStageResponse
)
from controller.interview_stage_controller import (
    create_interview_stage,
    get_all_interview_stages,
    get_interview_stage_by_id,
    update_interview_stage,
    delete_interview_stage
)

router = APIRouter(
    prefix="/interview-stage",
    tags=["Interview Stage"]
)


@router.post("/", response_model=InterviewStageResponse)
def create_stage(req: InterviewStageCreate, db: Session = Depends(get_db)):
    return create_interview_stage(req, db)


@router.get("/", response_model=list[InterviewStageResponse])
def get_all_stages(db: Session = Depends(get_db)):
    return get_all_interview_stages(db)


@router.get("/{stage_id}", response_model=InterviewStageResponse)
def get_stage(stage_id: int, db: Session = Depends(get_db)):
    return get_interview_stage_by_id(stage_id, db)


@router.put("/{stage_id}", response_model=InterviewStageResponse)
def update_stage(stage_id: int, req: InterviewStageUpdate, db: Session = Depends(get_db)):
    return update_interview_stage(stage_id, req, db)





@router.delete("/{stage_id}")
def delete_stage(stage_id: int, db: Session = Depends(get_db)):
    return delete_interview_stage(stage_id, db)
