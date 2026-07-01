import psycopg2
import os
from dotenv import load_dotenv
key = load_dotenv()
DB_NAME = "iAnswer"
DB_USER = "postgres"
DB_PASS = os.environ["DB_PASS"]
DB_HOST = "localhost"
DB_PORT = "5432"
def create_conversation():
    cur.execute("""INSERT INTO conversations DEFAULT VALUES RETURNING id""")
    new_id = cur.fetchone()[0]
    return new_id
def add_message(content,role,conversation_id):
    cur.execute("""INSERT INTO messages (content,role,conversation_id)
                VALUES(%s,%s,%s) RETURNING content""",
                (content,role,conversation_id))
    message_sample = cur.fetchone()[0]
    return message_sample
def get_messages(conversation_id):
    cur.execute("""SELECT role,content FROM messages WHERE conversation_id = %s
                """,(conversation_id,))
    return cur.fetchall()
try:
    conn = psycopg2.connect(database=DB_NAME,
                            user=DB_USER,
                            password=DB_PASS,
                            host=DB_HOST,
                            port=DB_PORT)
    print("Database connected successfully")
except:
    print("Database not connected successfully")
cur = conn.cursor()
if __name__ == "__main__" :
    cid = create_conversation()
    add_message("Hello World","user",cid)
    print("new conversation id:", cid)
    print("message sample :", get_messages(cid))
    conn.commit()
    cur.close()
    conn.close()