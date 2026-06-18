from models.generated_models import Tasks,MasterTaskType, MasterProject,MasterProjectModule


def create_task_service(payload, db):

    task = Tasks(
        title=payload.title,
        description=payload.description,
        task_type_id=payload.task_type_id,
        project_id=payload.project_id,
        emp_id=payload.emp_id,
        status_id=payload.status_id,
        due_date=payload.due_date,
        reporting_manager_id=payload.reporting_manager_id,
        task_manager_id=payload.task_manager_id,
        efforts_in_days=payload.efforts_in_days,
        created_by=payload.created_by,
        project_module_id=payload.project_module_id,
        is_active=True
    )

    db.add(task)
    db.commit()
    db.refresh(task)

    return task


def get_all_tasks_service(db):
    return db.query(Tasks).filter(
        Tasks.is_active == True
    ).all()


def get_task_by_id_service(task_id, db):
    return db.query(Tasks).filter(
        Tasks.id == task_id,
        Tasks.is_active == True
    ).first()




def get_all_task_types_service(db):
    return db.query(MasterTaskType).all()


def get_task_type_by_id_service(db, task_type_id: int):
    return (
        db.query(MasterTaskType)
        .filter(MasterTaskType.id == task_type_id)
        .first()
    )


def get_all_projects_service(db):
    return db.query(MasterProject).all()


def get_project_by_id_service(db, project_id: int):
    return (
        db.query(MasterProject)
        .filter(MasterProject.id == project_id)
        .first()
    )


def get_all_project_modules_service(db):
    return db.query(MasterProjectModule).all()


def get_project_module_by_id_service(db, module_id: int):
    return (
        db.query(MasterProjectModule)
        .filter(MasterProjectModule.id == module_id)
        .first()
    )


def get_project_modules_by_project_service(db, project_id: int):
    return (
        db.query(MasterProjectModule)
        .filter(MasterProjectModule.project_id == project_id)
        .all()
    )