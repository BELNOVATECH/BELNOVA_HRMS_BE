from fastapi import APIRouter
from controller.candidate_controller import (
    create_candidate_controller,
    get_candidates_controller
)
from models.candidate_model import CandidateCreate, CandidateRead

router = APIRouter(prefix="/candidates", tags=["Candidates"])


@router.post("/", response_model=CandidateRead)
async def create_candidate(candidate: CandidateCreate):
    return await create_candidate_controller(candidate)


@router.get("/", response_model=list[CandidateRead])
async def get_candidates():
    return await get_candidates_controller()
