from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.database import get_db

from schemas.designation_schema import (
    DesignationCreate,
    DesignationResponse,
    DesignationStatusUpdate
)
from services.designation_service import (
    create_designation_service,
    get_designations_service,
    update_designation_status_service
)

designation_router = APIRouter(
    prefix="/designations",
    tags=["Designation"]
)


@designation_router.get("/", response_model=list[DesignationResponse])
def get_designations(db: Session = Depends(get_db)):
    return get_designations_service(db)


@designation_router.post("/", response_model=DesignationResponse)
def create_designation(
    payload: DesignationCreate,
    db: Session = Depends(get_db)
):
    return create_designation_service(payload, db)


@designation_router.put(
    "/{designation_id}/status",
    response_model=DesignationResponse
)
def update_designation_status(
    designation_id: int,
    payload: DesignationStatusUpdate,
    db: Session = Depends(get_db)
):
    return update_designation_status_service(
        designation_id,
        payload.is_active,
        db
    )
