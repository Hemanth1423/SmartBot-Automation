import psycopg2
from dotenv import load_dotenv
import os

env_path=os.path.join(os.path.dirname(__file__),'..','.env')
load_dotenv(dotenv_path=env_path)

def get_db_connection():
    return psycopg2.connect(
        # host="127.0.0.1",
        # database="smartbot",
        # user="postgres",
        # password="Sautomation@2026",  # Replace with your PostgreSQL password
        # port="5432"
        os.getenv("DATABASE_URL")
    )


def insert_contact(name: str, email: str, company: str, message: str):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO contact_messages (name, email, company, message) VALUES (%s, %s, %s, %s)",
        (name, email, company, message)
    )
    conn.commit()
    cursor.close()
    conn.close()