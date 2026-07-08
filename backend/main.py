from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from load_dataset import load_disease_dataset
from symptom_extractor import extract_symptoms

from ml.predict_intent import predict_intent
from emergency import check_emergency
from disease_info import get_disease_info
from chat_history import save_chat, get_history
from database import SessionLocal, engine
from models import User,  Base
from auth import RegisterUser,LoginUser
from specialist import get_specialist
from hospital import get_hospitals
from medicine import get_medicine
from diet import get_diet
from disease_predictor import predict_disease

Base.metadata.create_all(bind=engine)

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
@app.post("/register")
def register(user: RegisterUser):

    db = SessionLocal()

    existing_user = db.query(User).filter(User.email == user.email).first()

    if existing_user:
        db.close()
        return {"message": "Email already registered"}

    new_user = User(
        name=user.name,
        email=user.email,
        password=user.password
    )

    db.add(new_user)
    db.commit()
    db.close()

    return {"message": "Registration Successful"}
@app.post("/login")
def login(user: LoginUser):

    db = SessionLocal()

    existing_user = db.query(User).filter(
        User.email == user.email,
        User.password == user.password
    ).first()

    db.close()

    if existing_user:
        return {
            "message": "Login Successful",
            "user": existing_user.name
        }

    return {
        "message": "Invalid Email or Password"
    }

@app.post("/predict")
def predict(data: SymptomRequest):

    # Emergency Detection
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
    



    # Predict Intent
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
    # Validate number of symptoms
    symptom_list = extract_symptoms(data.symptom)

   
    if len(symptom_list) < 1:
      return {
        "prediction": "More Symptoms Required",
        "severity": "",
        "description": "Please enter at least 2 symptoms separated by commas for a more accurate prediction.",
        "medical_suggestion": [
            "Example: fever, cough"
        ],
        "precaution": [],
        "hospital_required": False,
        "hospital": [],
        "medicine": [],
        "diet": []
    }
   # Predict disease using modular predictor
    try:
        best_match = predict_disease(",".join(symptom_list))
    except Exception as e:
         return {
        "error": str(e)
    }

    
    # If a disease is found
    if best_match:
    try:
        specialist = get_specialist(best_match["disease"])
        hospitals = get_hospitals(specialist)
        medicines = get_medicine(best_match["disease"])
        diet = get_diet(best_match["disease"])

        save_chat(data.symptom, best_match["disease"])

        return {
            "prediction": best_match["disease"],
            "confidence": best_match["confidence"],
            "specialist": specialist,
            "severity": best_match["severity"],
            "description": best_match["description"],
            "medical_suggestion": best_match["medical_suggestion"],
            "precaution": best_match["precaution"],
            "hospital_required": best_match["hospital_required"],
            "hospital": hospitals,
            "medicine": medicines,
            "diet": diet
        }
    except Exception as e:
        return {
            "error": str(e)
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
        "hospital": [],
        "medicine": [
            "Consult a doctor before taking any medicine."
        ],
        "diet": [
            "Maintain a balanced and healthy diet."
        ]
    }

@app.get("/history")
def history():
    return get_history()