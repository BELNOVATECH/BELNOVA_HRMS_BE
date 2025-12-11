# route/upload_route.py
from fastapi import APIRouter, UploadFile, File
from utils.file_upload import save_resume_locally

router = APIRouter(prefix="/upload", tags=["Resume Upload"])

@router.post("/resume")
def upload_resume(file: UploadFile = File(...)):
    saved_path = save_resume_locally(file)
    return {
        "message": "Resume uploaded successfully",
        "file_path": saved_path
    }
