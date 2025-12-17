from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from core.database import get_db
from controller.candidate_applied_controller import (
    create_candidate_applied_controller,
    get_candidate_applied_controller,
    update_candidate_applied_controller,
)
from schemas.candidate_applied_schema import (
    CandidateAppliedCreate,
    CandidateAppliedRead,
    CandidateAppliedUpdate,
)

candidate_router = APIRouter()


@candidate_router.post("/", response_model=CandidateAppliedRead)
def create_candidate(
    data: CandidateAppliedCreate,
    db: Session = Depends(get_db),
):
    return create_candidate_applied_controller(data, db)


@candidate_router.get("/", response_model=List[CandidateAppliedRead])
def get_candidates(db: Session = Depends(get_db)):
    return get_candidate_applied_controller(db)


@candidate_router.put("/{id}", response_model=CandidateAppliedRead)
def update_candidate(
    id: int,
    data: CandidateAppliedUpdate,
    db: Session = Depends(get_db),
):
    return update_candidate_applied_controller(id, data, db)

