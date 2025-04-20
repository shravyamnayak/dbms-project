import pymysql
import os
from dotenv import load_dotenv
from pymysql.cursors import DictCursor

# Load environment variables from .env
load_dotenv()

def get_db_connection():
    return pymysql.connect(
        host="localhost",
        port=3306,
        user="root",  # or "admin" if you're using Docker or a different setup
        password=os.environ.get("MYSQL_PASSWORD", ""),  # fallback to "" if env var is not set
        database="doctors_appointment",
        cursorclass=DictCursor
    )
