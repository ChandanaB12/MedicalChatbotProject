import re

SYMPTOM_SYNONYMS = {
    "fever": [
        "fever",
        "temperature",
        "high temperature",
        "high fever"
    ],
    "body pain": [
        "body pain",
        "body ache",
        "muscle pain",
        "body aches"
    ],
    "fatigue": [
        "fatigue",
        "tired",
        "feeling tired",
        "weak"
    ],
    "cough": [
        "cough",
        "coughing"
    ],
    "runny nose": [
        "runny nose",
        "running nose"
    ],
    "sore throat": [
        "sore throat",
        "throat pain"
    ],
    "headache": [
        "headache",
        "head pain"
    ],
    "vomiting": [
        "vomiting",
        "vomit"
    ],
    "nausea": [
        "nausea",
        "feeling sick"
    ],
    "diarrhea": [
        "diarrhea",
        "loose motion",
        "loose motions"
    ],
    "stomach pain": [
        "stomach pain",
        "stomach ache"
    ],
    "shortness of breath": [
        "shortness of breath",
        "breathlessness"
    ],
    "chest pain": [
        "chest pain"
    ]
}


def extract_symptoms(user_input):

    user_input = user_input.lower()

    found = []

    for symptom, words in SYMPTOM_SYNONYMS.items():

        for word in words:

            if re.search(r"\b" + re.escape(word) + r"\b", user_input):

                if symptom not in found:
                    found.append(symptom)

    return found