from services.top_performer_service import get_top_performers_service

def get_top_performers_controller(db):
    return get_top_performers_service(db)
