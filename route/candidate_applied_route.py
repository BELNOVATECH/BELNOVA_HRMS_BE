from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from core.database import get_db
from controller.candidate_applied_controller import (
    create_candidate_applied_controller,
    get_candidate_applied_controller
)
from schemas.candidate_applied_schema import CandidateAppliedCreate, CandidateAppliedRead
from typing import List

candidate_router = APIRouter()

@candidate_router.post("/", response_model=CandidateAppliedRead)
async def create_candidate(data: CandidateAppliedCreate, db: Session = Depends(get_db)):
    return create_candidate_applied_controller(data, db)

@candidate_router.get("/", response_model=List[CandidateAppliedRead])
async def get_candidates(db: Session = Depends(get_db)):
    return get_candidate_applied_controller(db)
