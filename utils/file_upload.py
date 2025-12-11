# utils/file_upload.py
import os
from fastapi import UploadFile

UPLOAD_DIR = "uploads/resumes"

# Create the directory automatically if missing
os.makedirs(UPLOAD_DIR, exist_ok=True)

def save_resume_locally(file: UploadFile) -> str:
    file_location = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_location, "wb") as f:
        f.write(file.file.read())

    return file_location
