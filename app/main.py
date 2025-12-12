from fastapi import FastAPI

# Import Routers
from route.auth_route import router as auth_router
from route.leave_route import router as leave_router
from route.leave_balance_route import router as balance_router
from route.candidate_route import router as candidate_router
from route.employee_route import router as employee_router
from route.upload_route import router as upload_router
from route.department_route import router as department_router
from route.job_route import router as job_router

# Database Import
from core.database import Base, engine
import models.employee_model


app = FastAPI(title="HRMS Backend API", version="1.0")


# Register All Routers
app.include_router(auth_router)
app.include_router(leave_router)
app.include_router(balance_router)
app.include_router(candidate_router)
app.include_router(employee_router)
app.include_router(upload_router)

# Department & Job Modules
app.include_router(department_router, prefix="/department", tags=["Department"])
app.include_router(job_router, prefix="/job", tags=["Job Titles"])


@app.get("/")
def root():
    return {"message": "HRMS Backend Running Successfully"}
