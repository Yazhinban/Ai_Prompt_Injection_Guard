from fastapi import APIRouter
from pydantic import BaseModel
from backend.services.security_engine import analyze_prompt
from backend.services.decision_engine import decision_engine
from backend.services.logging_service import log_prompt
from backend.services.llm_service import generate_response

router = APIRouter()

class PromptRequest(BaseModel):
    prompt: str


@router.post("/analyze_prompt")
def analyze(request: PromptRequest):

    prompt = request.prompt

    result = analyze_prompt(prompt)

    risk_score = result["risk_score"]
    attack_type = result["attack_type"]

    decision = decision_engine(risk_score)

    if decision == "BLOCKED":

        log_prompt(prompt, attack_type, risk_score, "BLOCKED")

        return {
            "status": "BLOCKED",
            "risk_score": risk_score,
            "attack_type": attack_type
        }

    elif decision == "REVIEW":

        log_prompt(prompt, attack_type, risk_score, "REVIEW", "PENDING")

        return {
            "status": "UNDER_REVIEW",
            "risk_score": risk_score,
            "attack_type": attack_type
        }

    else:

        response = generate_response(prompt)

        log_prompt(prompt, attack_type, risk_score, "SAFE")

        return {
            "status": "SAFE",
            "risk_score": risk_score,
            "attack_type": attack_type,
            "response": response
        }