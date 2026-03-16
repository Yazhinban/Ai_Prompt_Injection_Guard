from fastapi import APIRouter
from backend.services.logging_service import get_logs, delete_log

router = APIRouter()

@router.get("/logs")
def logs():
    return get_logs()


@router.delete("/logs/{log_id}")
def remove_log(log_id: int):
    delete_log(log_id)
    return {"message": "Log deleted"}