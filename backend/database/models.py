def create_tables(conn):
    cursor = conn.cursor()

    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS prompt_logs(
                                                             id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                             prompt TEXT,
                                                             attack_type TEXT,
                                                             risk_score REAL,
                                                             status TEXT,
                                                             review_status TEXT,
                                                             created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                   )
                   """)

    conn.commit()