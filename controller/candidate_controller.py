from services.candidate_service import (
    create_candidate_service,
    get_candidates_service
)

async def create_candidate_controller(candidate):
    return await create_candidate_service(candidate)

async def get_candidates_controller():
    return await get_candidates_service()
