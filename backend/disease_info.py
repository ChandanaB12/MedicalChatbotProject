DISEASE_INFO = {
    "dengue": "Dengue is a mosquito-borne viral disease. Common symptoms include high fever, rash, joint pain, and vomiting.",

    "malaria": "Malaria is caused by parasites transmitted through mosquito bites. Symptoms include fever, chills, sweating, and headache.",

    "diabetes": "Diabetes is a chronic disease that affects how the body processes blood sugar.",

    "asthma": "Asthma is a condition that causes inflammation of the airways, leading to difficulty breathing.",

    "covid": "COVID-19 is a viral respiratory infection caused by SARS-CoV-2.",

    "influenza": "Influenza is a contagious viral infection affecting the respiratory system.",

    "hypertension": "Hypertension is persistently high blood pressure and can increase the risk of heart disease."
}


def get_disease_info(text):
    text = text.lower()

    for disease in DISEASE_INFO:
        if disease in text:
            return DISEASE_INFO[disease]

    return None