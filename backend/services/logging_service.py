from backend.database.db import get_connection
from datetime import datetime


def log_prompt(prompt, risk_score, attack_type, status):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO logs(timestamp,prompt,risk_score,attack_type,status)
        VALUES (?,?,?,?,?)
        """,
        (
            datetime.now(),
            prompt,
            risk_score,
            attack_type,
            status
        )
    )

    conn.commit()
    conn.close()


def get_logs():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM logs ORDER BY id DESC")

    rows = cursor.fetchall()

    logs = []

    for r in rows:

        logs.append({
            "id": r[0],
            "timestamp": r[1],
            "prompt": r[2],
            "risk_score": r[3],
            "attack_type": r[4],
            "status": r[5]
        })

    conn.close()

    return logs


def delete_log(log_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM logs WHERE id=?", (log_id,))

    conn.commit()
    conn.close()


def get_stats():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM logs")
    total = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM logs WHERE status='BLOCKED'")
    blocked = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM logs WHERE status='SAFE'")
    safe = cursor.fetchone()[0]

    conn.close()

    return {
        "total_prompts": total,
        "blocked_attacks": blocked,
        "safe_prompts": safe
    }