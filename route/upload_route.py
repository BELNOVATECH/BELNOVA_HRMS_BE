from fastapi import APIRouter, UploadFile, File
from utils.file_upload import save_resume_locally

router = APIRouter(prefix="/upload", tags=["Resume Upload"])


@router.post("/resume")
def upload_resume(file: UploadFile = File(...)):
    # Save file and get unique filename
    filename = save_resume_locally(file)

    # Return file URL for frontend preview
    return {
        "message": "Resume uploaded successfully",
        "file_url": f"http://localhost:8000/uploads/resumes/{filename}"
    }
