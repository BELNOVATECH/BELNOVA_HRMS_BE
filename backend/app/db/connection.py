import psycopg2
from psycopg2.extras import RealDictCursor
from app.core.config import settings  

def get_connection():
    connection = psycopg2.connect(
        database=settings.DB_NAME,
        user=settings.DB_USER,
        password=settings.DB_PASSWORD,
        host=settings.DB_HOST,
        port=settings.DB_PORT,
        cursor_factory=RealDictCursor
    )
    return connection