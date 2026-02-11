
import sqlite3
import os

DB_PATH = "database/attendance.db"

def get_connection():
    return sqlite3.connect(DB_PATH, check_same_thread=False)

def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        role TEXT,
        department TEXT,
        salary REAL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS attendance (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        emp_id INTEGER,
        date TEXT,
        in_time TEXT,
        out_time TEXT,
        working_hours REAL,
        status TEXT,
        overtime REAL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS advances (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        emp_id INTEGER,
        amount REAL,
        date TEXT
    )
    """)

    conn.commit()
    conn.close()

create_tables()
