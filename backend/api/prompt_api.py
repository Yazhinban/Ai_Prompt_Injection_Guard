from fastapi import APIRouter
from backend.services.security_engine import analyze_prompt
from backend.services.logging_service import log_prompt

router = APIRouter()

@router.post("/analyze_prompt")
def analyze(data: dict):

    prompt = data["prompt"]

    result = analyze_prompt(prompt)

    log_prompt(
        prompt,
        result["risk_score"],
        result["attack_type"],
        result["status"]
    )

    return result