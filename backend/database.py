import sqlite3
from datetime import datetime
DB_NAME="docquery.db"

def create_tables():
    conn=sqlite3.connect(DB_NAME)
    c=conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS documents(id INTEGER PRIMARY KEY, filename TEXT,total_chunks INTEGER,uploaded_at TEXT)")
    c.execute("CREATE TABLE IF NOT EXISTS query_history(id INTEGER PRIMARY KEY, question TEXT, answer TEXT, created_at TEXT)")
    conn.commit(); conn.close()
