import os
import uuid
from fastapi import UploadFile

# Folder where resumes are stored
UPLOAD_DIR = "uploads/resumes"

# Create folder if it doesn't exist
os.makedirs(UPLOAD_DIR, exist_ok=True)


def save_resume_locally(file: UploadFile) -> str:
    """
    Saves uploaded resume file locally.
    Generates a unique filename to avoid overwrite.
    Returns the saved file name (not full path).
    """

    # Extract file extension
    ext = os.path.splitext(file.filename)[1]  # .pdf, .docx, .jpg, etc.

    # Generate a unique filename
    unique_filename = f"{uuid.uuid4().hex}{ext}"

    # Final file location
    file_path = os.path.join(UPLOAD_DIR, unique_filename)

    # Save file
    with open(file_path, "wb") as f:
        f.write(file.file.read())

    return unique_filename  # Return only filename
