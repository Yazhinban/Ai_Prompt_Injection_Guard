import sqlite3

def get_connection():

    conn = sqlite3.connect("logs.db", check_same_thread=False)

    cursor = conn.cursor()

    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS logs(
                                                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                      timestamp TEXT,
                                                      prompt TEXT,
                                                      risk_score REAL,
                                                      attack_type TEXT,
                                                      status TEXT
                   )
                   """)

    conn.commit()

    return conn