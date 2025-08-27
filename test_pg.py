import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

try:
    connection = psycopg2.connect(os.getenv("DATABASE_URL"))

    print("✅ Connection successful!")

    connection.close()
except Exception as e:
    print("❌ Connection failed:", e)


"""
try:
    conn = psycopg2.connect(
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
    )

    print("✅ Connection successful!")

    conn.close()
except Exception as e:
    print("❌ Connection failed:", e)
"""
