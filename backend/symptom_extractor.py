import re

SYMPTOM_SYNONYMS = {
    "fever": [
    "fever",
    "temperature",
    "high temperature",
    "high fever",
    "i have fever",
    "feeling feverish",
    "running a fever",
"my temperature is high",
"having fever"
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
    "coughing",
    "i am coughing"
    "dry cough",
"persistent cough"
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
    "head pain",
    "my head hurts",
    "pain in my head"
],
    
"vomiting": [
    "vomiting",
    "vomit",
    "throwing up",
    "threw up"
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
    "stomach ache",
    "stomach hurts",
    "my stomach hurts",
    "pain in stomach",
    "pain in my stomach",
    "tummy pain",
    "stomach cramp",
    "stomach cramps"
],
    "shortness of breath": [
        "shortness of breath",
        "breathlessness"
    ],
   "chest pain": [
    "chest pain"
],

"joint pain": [
    "joint pain",
    "pain in joints",
     "body joint pain"
],


"muscle pain": [
    "muscle pain",
    "body ache",
    "muscle ache"
],

"skin rash": [
    "skin rash",
    "rash",
    "red spots",
    "red rash"
],

"chills": [
    "chills",
    "shivering"
],

"sweating": [
    "sweating",
    "excessive sweating"
],

"chest pain": [
    "chest pain"
],

"sneezing": [
    "sneezing",
    "sneeze"
],

"wheezing": [
    "wheezing",
    "wheeze"
],

"chest tightness": [
    "chest tightness",
    "tight chest"
],

"abdominal pain": [
    "abdominal pain",
    "abdomen pain"
],

"weakness": [
    "weakness",
    "weak"
],

"loss of appetite": [
    "loss of appetite",
    "no appetite"
],

"loss of smell": [
    "loss of smell",
    "can't smell"
],

"breathing difficulty": [
    "breathing difficulty",
    "difficulty breathing"
],

"dizziness": [
    "dizziness",
    "feeling dizzy"
],

"itching": [
    "itching",
    "itchy",
    "itch"
],

"high blood pressure": [
    "high blood pressure",
    "bp high"
],

"frequent urination": [
    "frequent urination",
    "urinating frequently"
],

"increased thirst": [
    "increased thirst",
    "very thirsty"
],

"blurred vision": [
    "blurred vision",
    "blurry vision"
],

"burning urination": [
    "burning urination",
    "burning while urinating",
    "pain while urinating",
    "burning sensation while urinating"
],

"lower abdominal pain": [
    "lower abdominal pain",
    "lower stomach pain"
],

"weight loss": [
    "weight loss",
    "losing weight",
    "unexpected weight loss",
    "unintentional weight loss"
],
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