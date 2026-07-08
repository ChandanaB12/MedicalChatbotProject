from disease_dataset import disease_dataset
from symptom_matcher import match_symptoms
from confidence import calculate_confidence


def predict_disease(user_symptoms):

    best_match = None
    highest_match = 0

    for disease in disease_dataset:

        matched = match_symptoms(
            user_symptoms,
            disease["symptoms"]
        )

        if len(matched) > highest_match:

            highest_match = len(matched)

            best_match = disease.copy()

            best_match["matched_symptoms"] = matched

            best_match["confidence"] = calculate_confidence(
                len(matched),
                len(disease["symptoms"])
            )

    if best_match and best_match["confidence"] >= 40:
        return best_match

    return None