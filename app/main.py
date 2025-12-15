from fastapi import FastAPI

from route.attendance_route import router as attendance_router
from route.interview_stage_route import router as interview_stage_router

from core.database import Base, engine


from models.attendance_tracker import AttendanceTracker
from models.interview_stage import InterviewStage


app = FastAPI(title="Attendance Service")


app.include_router(attendance_router)
app.include_router(interview_stage_router)


@app.get("/")
def root():
    return {"message": "Attendance service is running"}
