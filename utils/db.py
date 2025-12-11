import psycopg2
from psycopg2.extras import RealDictCursor

def get_connection():
    return psycopg2.connect(
        host="43.243.79.183",
        database="hrms_portal",
        user="postgres",
        password="Admin@123",
        cursor_factory=RealDictCursor
    )
