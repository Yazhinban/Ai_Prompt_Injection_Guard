from fastapi import APIRouter
from backend.services.logging_service import get_stats

router = APIRouter()

@router.get("/stats")
def stats():

    return get_stats()