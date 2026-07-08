EMERGENCY_KEYWORDS = [
    "unconscious",
    "severe bleeding",
    "seizure",
    "heart attack",
    "stroke"
]

def check_emergency(text):
    text = text.lower()

    for keyword in EMERGENCY_KEYWORDS:
        if keyword in text:
            return True

    return False