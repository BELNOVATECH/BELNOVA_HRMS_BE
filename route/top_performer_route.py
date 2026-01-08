from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from core.database import get_db
from schemas.top_performer_schema import TopPerformerResponse
from controller.top_performer_controller import get_top_performers_controller

router = APIRouter(
    prefix="/top-performers",
    tags=["Top Performers"]
)

@router.get(
    "/",
    response_model=List[TopPerformerResponse],
    summary="Get Top Performers (Rating ≥ 4.5)"
)
def get_top_performers(db: Session = Depends(get_db)):
    return get_top_performers_controller(db)
