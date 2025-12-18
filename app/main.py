from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

# -----------------------------
# Database
# -----------------------------
from core.database import Base, engine

# -----------------------------
# Routers
# -----------------------------
from route.auth_route import router as auth_router
from route.leave_route import router as leave_router
from route.leave_balance_route import router as balance_router
from route.candidate_applied_route import candidate_router
from route.employee_route import router as employee_router
from route.upload_route import router as upload_router
from route.department_route import router as department_route
# from route.job_route import router as job_route
from route.interview_schedule_route import interview_schedule_router
from route.interview_stage_route import router as interview_stage_router
from route.holiday_route import holiday_router
from route.attendance_route import router as attendance_router

# -----------------------------
# FastAPI App
# -----------------------------
app = FastAPI(
    title="HRMS Backend API",
    version="1.0"
)

# -----------------------------
# CORS Middleware
# -----------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------
# Static Files
# -----------------------------
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")

# -----------------------------
# API Routes
# -----------------------------
app.include_router(auth_router)
app.include_router(leave_router)
app.include_router(balance_router)
app.include_router(candidate_router, prefix="/candidates", tags=["Candidates"])
app.include_router(employee_router)
app.include_router(upload_router)
app.include_router(department_route)
# app.include_router(job_route)

app.include_router(
    interview_schedule_router,
    prefix="/interview-schedule",
    tags=["Interview Schedule"]
)

app.include_router(
    interview_stage_router,
    prefix="/interview-stage",
    tags=["Interview Stage"]
)

app.include_router(
    holiday_router,
    prefix="/holidays",
    tags=["Holiday Calendar"]
)

app.include_router(
    attendance_router,
    prefix="/attendance",
    tags=["Attendance"]
)

# -----------------------------
# Root Endpoint
# -----------------------------
@app.get("/")
def root():
    return {"message": "HRMS Backend Running"}
