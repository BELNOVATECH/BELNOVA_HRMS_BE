from services.candidate_applied_service import (
    create_candidate_applied_service,
    get_candidate_applied_service,
    update_candidate_applied_service,
)

def create_candidate_applied_controller(data, db):
    return create_candidate_applied_service(data, db)

def get_candidate_applied_controller(db):
    return get_candidate_applied_service(db)


def update_candidate_applied_controller(id, data, db):
    return update_candidate_applied_service(id, data, db)
