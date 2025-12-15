from fastapi import FastAPI

from route.attendance_route import router as attendance_router
from core.database import Base, engine

# create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Attendance Service")

app.include_router(attendance_router)


@app.get("/")
def root():
    return {"message": "Attendance service is running"}
