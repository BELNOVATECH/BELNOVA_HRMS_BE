from fastapi import APIRouter, HTTPException
from app.api.controllers.auth_controller import fetch_all_employees

router = APIRouter()

@router.get("/")
def get_employees():
    try:
        return fetch_all_employees()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
