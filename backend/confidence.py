def calculate_confidence(matched_count, total_symptoms):

    if total_symptoms == 0:
        return 0

    confidence = (matched_count / total_symptoms) * 100

    return round(confidence, 2)