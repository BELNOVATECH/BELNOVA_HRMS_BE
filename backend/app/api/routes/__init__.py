from fastapi import APIRouter
from app.api.routes import auth_routes, employee_routes, project_routes,attendance_routes

router = APIRouter()

router.include_router(auth_routes.router, prefix="/auth", tags=["Authentication"])
router.include_router(employee_routes.router, prefix="/employees", tags=["Employees"])
router.include_router(attendance_routes.router, prefix="/attendance", tags=["Attendance"])


router.include_router(project_routes.router)
