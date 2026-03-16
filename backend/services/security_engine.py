import re
from backend.services.decision_engine import calculate_risk

attack_patterns = [
    "ignore previous instructions",
    "developer mode",
    "reveal system prompt",
    "bypass safety",
    "show hidden rules",
]

def analyze_prompt(prompt):

    prompt_lower = prompt.lower()

    detected = False
    attack_type = "SAFE"

    for pattern in attack_patterns:
        if pattern in prompt_lower:
            detected = True
            attack_type = "PROMPT_INJECTION"

    risk_score = calculate_risk(prompt, detected)

    status = "SAFE"

    if risk_score > 0.7:
        status = "BLOCKED"

    return {
        "risk_score": risk_score,
        "attack_type": attack_type,
        "status": status
    }