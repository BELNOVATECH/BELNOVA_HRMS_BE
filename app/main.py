from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from route.auth_route import router as auth_router
from route.leave_route import router as leave_router
from route.leave_balance_route import router as balance_router
from route.candidate_route import router as candidate_router
from route.employee_route import router as employee_router
from route.upload_route import router as upload_router
from route.department_route import router as department_route
from route.job_route import router as job_route

from core.database import Base, engine
import models.employee_model


app = FastAPI(
    title="HRMS Backend API",
    version="1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],        
    allow_credentials=True,
    allow_methods=["*"],        
    allow_headers=["*"],        
)


app.include_router(auth_router)
app.include_router(leave_router)
app.include_router(balance_router)
app.include_router(candidate_router)
app.include_router(employee_router)
app.include_router(upload_router)
app.include_router(department_route)
app.include_router(job_route)


@app.get("/")
def root():
    return {"message": "HRMS Backend Running"}
