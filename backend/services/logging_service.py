from backend.database.db import get_connection


def log_prompt(prompt, attack_type, risk_score, status, review_status=None):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO prompt_logs(prompt, attack_type, risk_score, status, review_status)
        VALUES(?,?,?,?,?)
    """, (prompt, attack_type, risk_score, status, review_status))

    conn.commit()
    conn.close()


def get_logs():

    conn = get_connection()
    cursor = conn.cursor()

    rows = cursor.execute("""
        SELECT id, prompt, attack_type, risk_score, status, review_status, created_at
        FROM prompt_logs
        ORDER BY created_at DESC
    """).fetchall()

    conn.close()

    logs = []

    for r in rows:
        logs.append({
            "id": r[0],
            "prompt": r[1],
            "attack_type": r[2],
            "risk_score": r[3],
            "status": r[4],
            "review_status": r[5],
            "created_at": r[6]
        })

    return logs


def delete_log(log_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM prompt_logs
        WHERE id=?
    """, (log_id,))

    conn.commit()
    conn.close()


def get_stats():

    conn = get_connection()
    cursor = conn.cursor()

    total = cursor.execute("""
        SELECT COUNT(*) FROM prompt_logs
    """).fetchone()[0]

    blocked = cursor.execute("""
        SELECT COUNT(*) FROM prompt_logs WHERE status='BLOCKED'
    """).fetchone()[0]

    safe = cursor.execute("""
        SELECT COUNT(*) FROM prompt_logs WHERE status='SAFE'
    """).fetchone()[0]

    review = cursor.execute("""
        SELECT COUNT(*) FROM prompt_logs WHERE status='REVIEW'
    """).fetchone()[0]

    conn.close()

    return {
        "total_prompts": total,
        "blocked_prompts": blocked,
        "safe_prompts": safe,
        "review_prompts": review
    }