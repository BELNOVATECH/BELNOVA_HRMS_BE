from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from core.database import get_db
from schemas.designation_schema import DesignationCreate, DesignationRead
from controller.designation_controller import (
    create_designation_controller,
    get_designations_controller
)

designation_router = APIRouter(
    prefix="/designations",
    tags=["Designations"]
)

@designation_router.post("/", response_model=DesignationRead)
def create_designation(
    data: DesignationCreate,
    db: Session = Depends(get_db)
):
    return create_designation_controller(data, db)


@designation_router.get("/", response_model=List[DesignationRead])
def get_designations(db: Session = Depends(get_db)):
    return get_designations_controller(db)
