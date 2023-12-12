from pydantic import BaseSettings
from dotenv import load_dotenv
import os

load_dotenv()

class PostgresDatabase(BaseSettings):
    host = os.getenv('pg_database_host')
    port = os.getenv('pg_database_port')
    user_name = os.getenv('pg_database_username')
    password = os.getenv('pg_database_password')
    db = os.getenv('pg_database')


