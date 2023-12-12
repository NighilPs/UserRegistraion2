from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from storage.configuration import PostgresDatabase

PostgresDatabase = PostgresDatabase()

SQLALCHEMY_DATABASE_URL = f"postgresql://{PostgresDatabase.user_name}:{PostgresDatabase.password}@{PostgresDatabase.host}/{PostgresDatabase.db}"

print(SQLALCHEMY_DATABASE_URL)
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, pool_size=50 , max_overflow=50
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
   pg_db = SessionLocal()
   try:
       yield pg_db
   finally:
       pg_db.close()
