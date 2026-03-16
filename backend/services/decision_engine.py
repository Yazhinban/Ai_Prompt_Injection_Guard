LOW_THRESHOLD = 0.3
HIGH_THRESHOLD = 0.7


def decision_engine(score):

    if score < LOW_THRESHOLD:
        return "SAFE"

    elif score >= HIGH_THRESHOLD:
        return "BLOCKED"

    else:
        return "REVIEW"