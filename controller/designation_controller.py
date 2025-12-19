from services.designation_service import (
    create_designation_service,
    get_designations_service
)

def create_designation_controller(data, db):
    return create_designation_service(data, db)


def get_designations_controller(db):
    return get_designations_service(db)
