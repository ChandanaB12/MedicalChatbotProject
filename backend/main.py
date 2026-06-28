from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from load_dataset import load_disease_dataset
from symptom_extractor import extract_symptoms
from ml.predict_intent import predict_intent
from emergency import check_emergency
from disease_info import get_disease_info
from chat_history import save_chat, get_history

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class SymptomRequest(BaseModel):
    symptom: str


@app.get("/")
def home():
    return {"message": "Healthcare AI Backend Running"}

@app.post("/predict")
def predict(data: SymptomRequest):

    # Check for emergency symptoms first
    if check_emergency(data.symptom):
        save_chat(data.symptom, "Emergency")
        return {
            "prediction": "Emergency",
            "severity": "Critical",
            "description": "🚨 Your symptoms may indicate a medical emergency. Please seek immediate medical attention immediately.",
            "medical_suggestion": [
                "Call emergency services immediately.",
                "Do not delay medical care."
            ],
            "precaution": [
                "Stay calm and seek immediate help."
            ],
            "hospital_required": True,
            "hospital": [
                "Vijayanagara Institute of Medical Sciences (VIMS), Ballari",
                "Ballari District Hospital",
                "KIMS Hospital, Ballari"
            ]
        }

        # Step 1: Predict the user's intent using ML
    intent = predict_intent(data.symptom)
        # Disease Information
    disease_info = get_disease_info(data.symptom)

    if disease_info:
        return {
            "prediction": "Disease Information",
            "severity": "",
            "description": disease_info,
            "medical_suggestion": [],
            "precaution": [],
            "hospital_required": False,
            "hospital": []
        }

    print("Predicted Intent:", intent)
    # Greeting
    if intent == "greeting":
        return {
            "prediction": "Greeting",
            "severity": "",
            "description": "Hello! 👋 Welcome to the Healthcare AI Chatbot. How can I help you today?",
            "medical_suggestion": [],
            "precaution": [],
            "hospital_required": False,
            "hospital": []
        }

    # Goodbye
    if intent == "goodbye":
        return {
            "prediction": "Goodbye",
            "severity": "",
            "description": "Take care! 😊 Wishing you good health.",
            "medical_suggestion": [],
            "precaution": [],
            "hospital_required": False,
            "hospital": []
        }

    # Hospital Recommendation
    if intent == "hospital_recommendation":
        return {
            "prediction": "Hospital Recommendation",
            "severity": "",
            "description": "Recommended hospitals in Ballari:",
            "medical_suggestion": [],
            "precaution": [],
            "hospital_required": True,
            "hospital": [
                "Vijayanagara Institute of Medical Sciences (VIMS), Ballari",
                "Ballari District Hospital",
                "KIMS Hospital, Ballari"
            ]
        }

    # Load disease dataset
    disease_dataset = load_disease_dataset()

    # Extract symptoms using NLP
    symptoms = extract_symptoms(data.symptom)

    # Fallback if NLP doesn't detect symptoms
    if not symptoms:
        symptoms = [s.strip().lower() for s in data.symptom.split(",")]

        best_match = None
    max_matches = 0

    for disease in disease_dataset:

        matches = 0

        for symptom in symptoms:
            if symptom in disease["symptoms"]:
                matches += 1

        if matches > max_matches:
            max_matches = matches
            best_match = disease

    # If a disease is found, save it in chat history
    if best_match:

        save_chat(data.symptom, best_match["disease"])

        return {
            "prediction": best_match["disease"],
            "severity": best_match["severity"],
            "description": best_match["description"],
            "medical_suggestion": best_match["medical_suggestion"],
            "precaution": best_match["precaution"],
            "hospital_required": best_match["hospital_required"],
            "hospital": best_match["hospital"]
        }

    # If no disease is found
    save_chat(data.symptom, "Consult Doctor")

    return {
        "prediction": "Consult Doctor",
        "severity": "Unknown",
        "description": "Sorry, I couldn't identify the disease based on the provided symptoms.",
        "medical_suggestion": [
            "Consult a qualified healthcare professional."
        ],
        "precaution": [
            "Do not ignore persistent or worsening symptoms."
        ],
        "hospital_required": False,
        "hospital": []
    }


@app.get("/history")
def history():
    return get_history()