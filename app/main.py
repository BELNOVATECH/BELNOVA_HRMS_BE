from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from core.database import Base, engine

# -------------------------------------------------
# 🔥 IMPORT ALL MODELS (IMPORTANT FOR TABLE CREATION)
# -------------------------------------------------
import models.department
import models.designation_model
import models.master_module
import models.master_screen
import models.master_screen_permission
from models.master_year import MasterYear
from models.master_month import MasterMonth
from models.payroll_model import Payroll

# -------------------------------------------------
# ROUTERS
# -------------------------------------------------
from route.auth_route import auth_router
from route.leave_route import router as leave_router
from route.leave_balance_route import router as balance_router
from route.candidate_applied_route import candidate_router
from route.employee_route import router as employee_router
from route.upload_route import router as upload_router
from route.department_route import router as department_route
from route.role_route import role_router
from route.job_route import router as job_route
from route.interview_schedule_route import interview_schedule_router
from route.interview_stage_route import router as interview_stage_router
from route.holiday_route import holiday_router
from route.designation_route import designation_router
from route.attendance_route import router as attendance_router
from route.payroll_route import router as payroll_router
from route.master_route import router as master_router
from route.employee_rating_route import router as employee_rating_router
from route.vw_performance_rating_route import router as vw_performance_rating_router
from route.employee_count_route import router as employee_count_router
from route.top_performer_route import router as top_performer_router
from route.average_rating_route import router as average_rating_router
from route.pending_review_route import router as pending_review_router
from route.dashboard_route import router as dashboard_router
from route.employee_activity_route import router as employee_activity_router

# -------------------------------------------------
# APP INIT
# -------------------------------------------------
app = FastAPI(
    title="HRMS Backend API",
    version="1.0"
)

# -------------------------------------------------
# ✅ CORS (FIXED & SAFE)
# -------------------------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://hrms-portal-iota.vercel.app",  # production
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],     # 🔥 REQUIRED for PUT / POST
    allow_headers=["*"],     # 🔥 REQUIRED for Authorization / JSON
)

# -------------------------------------------------
# STATIC FILES
# -------------------------------------------------
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")

# -------------------------------------------------
# CREATE TABLES (SAFE)
# -------------------------------------------------
try:
    Base.metadata.create_all(bind=engine)
    print("✅ Tables created / verified")
except Exception as e:
    print("⚠️ Skipping table creation (DB not reachable):", e)

# -------------------------------------------------
# ROUTES
# -------------------------------------------------
app.include_router(auth_router)
app.include_router(leave_router)
app.include_router(balance_router)
app.include_router(designation_router)
app.include_router(payroll_router)
app.include_router(attendance_router)
app.include_router(master_router)
app.include_router(role_router)

app.include_router(candidate_router, prefix="/candidates", tags=["Candidates"])
app.include_router(employee_router)
app.include_router(upload_router)
app.include_router(department_route)

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
    job_route,
    prefix="/job-openings",
    tags=["Job Openings"]
)

app.include_router(employee_rating_router)
app.include_router(vw_performance_rating_router)
app.include_router(employee_count_router)
app.include_router(top_performer_router)
app.include_router(average_rating_router)
app.include_router(pending_review_router)
app.include_router(dashboard_router)
app.include_router(employee_activity_router)

# -------------------------------------------------
# ROOT
# -------------------------------------------------
@app.get("/")
def root():
    return {"message": "HRMS Backend Running"}
