attack_patterns = [
    "ignore previous instructions",
    "developer mode",
    "reveal system prompt",
    "bypass safety",
    "show hidden rules",
    "override system",
    "disable safety",
]

def calculate_risk(prompt, detected):

    prompt = prompt.lower()

    # High risk attacks
    if "reveal system prompt" in prompt:
        return 0.9

    if "bypass safety" in prompt:
        return 0.85

    # Medium risk -> REVIEW
    if "ignore previous instructions" in prompt:
        return 0.6

    if "developer mode" in prompt:
        return 0.55

    # Safe prompts
    if detected:
        return 0.4

    return 0.1


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

    elif risk_score >= 0.3:
        status = "REVIEW"

    return {
        "risk_score": risk_score,
        "attack_type": attack_type,
        "status": status
    }