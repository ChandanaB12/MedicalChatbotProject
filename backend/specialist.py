def get_specialist(disease):

   specialist = {

    "Viral Infection": "General Physician",
    "Common Cold": "General Physician",
    "Dengue": "General Physician",
    "Malaria": "General Physician",
    "Typhoid": "General Physician",
    "Food Poisoning": "Gastroenterologist",
    "Migraine": "Neurologist",
    "Asthma": "Pulmonologist",
    "COVID-19": "Pulmonologist",
    "Pneumonia": "Pulmonologist",
    "Diabetes": "Endocrinologist",
    "Hypertension": "Cardiologist",
    "Influenza": "General Physician",
    "Gastritis": "Gastroenterologist",
    "Allergy": "Allergist",
    "Sinusitis": "ENT Specialist",
    "Chickenpox": "General Physician",
    "Bronchitis": "Pulmonologist",
    "Tuberculosis": "Pulmonologist",
    "Urinary Tract Infection (UTI)": "Urologist",
    "Appendicitis": "General Surgeon"

}
   return specialist.get(disease, "General Physician")

    