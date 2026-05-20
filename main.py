import os 
import mysql.connector
from dotenv import load_dotenv
load_dotenv()

db_host = os.getenv("DB_HOST")
db_user = os.getenv("DB_USER")
db_pass = os.getenv("DB_PASSWORD")

print("--- Settings checking .ENV ---")
print(f"HOST: {db_host}")
print(f"USER: {db_user}")
print(f"PASSWORD: {db_pass if db_pass else '--- EMPTY ---'}")

try:
    mydb = mysql.connector.connect(
    host=db_host,
    user=db_user,
    password=db_pass,
    database="test32"
    )

    mycursor = mydb.cursor()

    query = """
    CREATE TABLE IF NOT EXISTS tasks (
    id INT AUTO_INCRENENT PRYMARY KEY,
    title VARCHAR(255) NOT NULL,
    is_done Boolean DEFAULT FALSE
    )
"""

    mycursor.execute(query)

    print("Table 'test32' created successfully!")

except mysql.connector.Error as err:
    print(f"fall: {err}")