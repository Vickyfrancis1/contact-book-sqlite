import sqlite3

conn = sqlite3.connect("contacts.db")
cur = conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS contacts (
        id INTEGER PRIMARY KEY,
        name TEXT UNIQUE,
        phone TEXT
     )
""")
conn.commit()
conn.close()

print("Database ready")