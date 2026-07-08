def match_symptoms(user_symptoms, disease_symptoms):

    # Symptom synonyms
    symptom_map = {
        "high temperature": "fever",
        "temperature": "fever",
        "cold": "common cold",
        "tummy pain": "stomach pain",
        "abdomen pain": "abdominal pain",
        "breathlessness": "shortness of breath",
        "difficulty breathing": "shortness of breath",
        "loss of taste": "loss of smell",
        "high sugar": "increased thirst",
        "pee frequently": "frequent urination",
        "weakness": "fatigue"
    }

    user_symptoms = [
        s.strip().lower()
        for s in user_symptoms.split(",")
        if s.strip()
    ]

    disease_symptoms = [
        s.lower()
        for s in disease_symptoms
    ]

    matched = []

    for symptom in user_symptoms:

        # Convert synonym to standard symptom
        symptom = symptom_map.get(symptom, symptom)

        if symptom in disease_symptoms:
            matched.append(symptom)

    return matched