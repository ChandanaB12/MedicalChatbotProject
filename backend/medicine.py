def get_medicine(disease):

    medicines = {
        "Viral Infection": [
            "Paracetamol (for fever, if prescribed)",
            "ORS / Electrolyte solution",
            "Vitamin C (if recommended by a doctor)"
        ],

        "Malaria": [
            "Take only prescribed antimalarial medicines",
            "Paracetamol for fever (if advised by a doctor)"
        ],

        "Common Cold": [
            "Paracetamol (if needed)",
            "Steam inhalation",
            "Warm fluids"
        ],

        "Migraine": [
            "Pain relief medicine only if prescribed",
            "Rest in a quiet, dark room"
        ],

                "Food Poisoning": [
            "ORS (Oral Rehydration Solution)",
            "Probiotics (if prescribed)",
            "Paracetamol (if fever is present)"
        ],

        "COVID-19": [
            "Paracetamol (if prescribed)",
            "ORS / Electrolyte solution",
            "Vitamin C (if recommended)"
        ],

        "Influenza": [
            "Paracetamol (if prescribed)",
            "Warm fluids",
            "Rest"
        ],

        "Pneumonia": [
            "Take prescribed antibiotics only",
            "Paracetamol (if prescribed)",
            "Drink plenty of fluids"
        ],

        "Diabetes": [
            "Take prescribed diabetes medication",
            "Monitor blood sugar regularly"
        ],

        "Hypertension": [
            "Take prescribed blood pressure medicine",
            "Monitor blood pressure regularly"
        ],

        "Urinary Tract Infection (UTI)": [
            "Drink plenty of water",
            "Take prescribed antibiotics",
            "Paracetamol (if prescribed)"
        ],

        "Gastritis": [
            "Antacids (if prescribed)",
            "Acid-reducing medicine (if prescribed)",
            "Avoid self-medication"
        ],

                "Typhoid": [
            "Take prescribed antibiotics only",
            "Paracetamol (if prescribed)",
            "ORS (Oral Rehydration Solution)"
        ],

        "Dengue": [
    "Paracetamol (if prescribed)",
    "ORS (Oral Rehydration Solution)",
    "Drink plenty of fluids",
    "Avoid taking medicines unless advised by a doctor"
],

"Asthma": [
    "Use prescribed inhaler",
    "Take medicines only as prescribed",
    "Seek immediate medical care if breathing worsens"
],

"Allergy": [
    "Take anti-allergy medicine only if prescribed",
    "Avoid known allergens"
],

"Sinusitis": [
    "Steam inhalation",
    "Saline nasal spray (if recommended)",
    "Take medicines only if prescribed"
],

"Chickenpox": [
    "Calamine lotion (if recommended)",
    "Paracetamol (if prescribed)",
    "Avoid scratching the rash"
],

"Bronchitis": [
    "Drink warm fluids",
    "Take medicines only if prescribed",
    "Avoid smoking"
],

"Tuberculosis": [
    "Complete the full course of prescribed TB medicines",
    "Never stop medication without consulting a doctor"
],

 "Appendicitis": [
    "Do not take painkillers without medical advice",
    "Seek immediate hospital care"
]

    }

    return medicines.get(
        disease,
        ["Consult a doctor before taking any medicine."]
    )