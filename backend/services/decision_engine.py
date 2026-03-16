import random

def calculate_risk(prompt, detected):

    base_score = random.uniform(0.05,0.4)

    if detected:
        base_score = random.uniform(0.8,0.95)

    return round(base_score,2)