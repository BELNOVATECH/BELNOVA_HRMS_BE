from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from psycopg2.pool import ThreadedConnectionPool
from dotenv import load_dotenv
import os

# -------------------------------------------------
# LOAD ENV
# -------------------------------------------------
load_dotenv()

# -------------------------------------------------
# SQLALCHEMY (SAFE – DOES NOT CONNECT IMMEDIATELY)
# -------------------------------------------------
DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# -------------------------------------------------
# PSYCOPG2 RAW CONNECTION (PROTECTED)
# -------------------------------------------------
PSYCOPG2_DSN = os.getenv("PSYCOPG2_DSN")

db_pool = None

try:
    if PSYCOPG2_DSN:
        db_pool = ThreadedConnectionPool(
            minconn=5,
            maxconn=20,
            dsn=PSYCOPG2_DSN
        )
        print("✅ psycopg2 pool connected")
    else:
        print("⚠️ PSYCOPG2_DSN not set")
except Exception as e:
    print("⚠️ psycopg2 pool NOT connected:", e)

def get_raw_conn():
    if not db_pool:
        raise RuntimeError("Raw DB connection not available")

    conn = db_pool.getconn()
    try:
        yield conn
    finally:
        db_pool.putconn(conn)
