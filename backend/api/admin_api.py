from fastapi import APIRouter
from backend.database.db import get_connection

router = APIRouter(prefix="/admin", tags=["Admin"])


@router.get("/reviews")
def get_pending_reviews():

    conn = get_connection()
    cursor = conn.cursor()

    rows = cursor.execute("""
        SELECT id, prompt, risk_score
        FROM prompt_logs
        WHERE review_status='PENDING'
    """).fetchall()

    conn.close()

    reviews = []

    for r in rows:
        reviews.append({
            "id": r[0],
            "prompt": r[1],
            "risk_score": r[2]
        })

    return reviews


@router.post("/approve/{prompt_id}")
def approve(prompt_id: int):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE prompt_logs
        SET review_status='APPROVED', status='SAFE'
        WHERE id=?
    """, (prompt_id,))

    conn.commit()
    conn.close()

    return {"message": "Prompt approved"}


@router.post("/reject/{prompt_id}")
def reject(prompt_id: int):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE prompt_logs
        SET review_status='REJECTED', status='BLOCKED'
        WHERE id=?
    """, (prompt_id,))

    conn.commit()
    conn.close()

    return {"message": "Prompt rejected"}