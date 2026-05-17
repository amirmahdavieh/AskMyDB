# create_db.py
import sqlite3
import os

# ASKMYDB/company.db
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "company.db")

conn = sqlite3.connect(DB_PATH)  # creates database file
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER,
        department TEXT,
        salary REAL
    )
""")

employees = [
    (1, "Alice Johnson",  35, "Engineering",  85000),
    (2, "Bob Smith",      45, "Marketing",    62000),
    (3, "Carol White",    52, "Engineering",  95000),
    (4, "David Brown",    29, "HR",           48000),
    (5, "Eve Davis",      41, "Finance",      73000),
    (6, "Frank Miller",   38, "Engineering",  88000),
    (7, "Grace Wilson",   60, "Management",  120000),
    (8, "Henry Moore",    33, "Marketing",    55000),
]

cursor.executemany("INSERT OR REPLACE INTO employees VALUES (?, ?, ?, ?, ?)", employees)
conn.commit()
conn.close()    