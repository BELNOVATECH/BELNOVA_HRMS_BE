from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import FileResponse
from utils.file_upload import save_resume_locally
import os

router = APIRouter(prefix="/upload", tags=["Resume Upload"])

UPLOAD_DIR = "uploads/resumes"



@router.post("/resume")
def upload_resume(file: UploadFile = File(...)):
    filename = save_resume_locally(file)

    return {
        "message": "Resume uploaded successfully",
        "file_url": f"http://localhost:8000/uploads/resumes/{filename}"
    }



@router.get("/resume/{filename}")
def get_resume(filename: str):
    file_path = os.path.join(UPLOAD_DIR, filename)

    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="Resume not found")

    return {
        "file_url": f"http://localhost:8000/uploads/resumes/{filename}"
    }



@router.get("/resume/view/{filename}")
def view_resume(filename: str):
    file_path = os.path.join(UPLOAD_DIR, filename)

    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="Resume not found")

    return FileResponse(path=file_path, filename=filename)
