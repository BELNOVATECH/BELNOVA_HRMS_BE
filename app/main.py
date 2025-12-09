from fastapi import FastAPI
from route.auth_route import router as auth_router
from route.leave_route import router as leave_router

app = FastAPI(title="HRMS Backend API", version="1.0")

# Include Routers
app.include_router(auth_router)
app.include_router(leave_router)

@app.get("/")
def root():
    return {"message": "HRMS Backend Running"}
