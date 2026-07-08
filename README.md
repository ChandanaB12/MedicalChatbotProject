# 🩺 AI Medical Chatbot Assistant

An AI-powered healthcare chatbot developed using **React.js**, **FastAPI**, and **Python** that analyzes user symptoms, predicts possible diseases, recommends specialists, medicines, diet plans, hospitals, and generates downloadable medical reports.

## ✨ Features

- 🔐 User Registration and Login Authentication
- 🤖 AI-based Symptom Analysis
- 🩺 Disease Prediction
- 📊 Confidence Score Calculation
- 👨‍⚕️ Specialist Recommendation
- 💊 Medicine Suggestions
- 🥗 Diet Recommendations
- 🏥 Hospital Recommendations
- 🚨 Emergency Detection
- 🎤 Voice Input Support
- 📄 Downloadable PDF Medical Report
- 💬 Chat History
- 📱 Responsive User Interface

## 🛠️ Technologies Used

### Frontend
- React.js
- HTML5
- CSS3
- JavaScript

### Backend
- Python
- FastAPI

### Database
- SQLite

### Libraries & Tools
- Axios
- Pydantic
- Uvicorn
- ReportLab (PDF Generation)

### Development Tools
- Visual Studio Code
- Git
- GitHub
- Postman

## 📂 Project Structure

```
MedicalChatbotProject
│
├── backend
│   ├── main.py
│   ├── disease_predictor.py
│   ├── disease_dataset.py
│   ├── symptom_extractor.py
│   ├── symptom_matcher.py
│   ├── confidence.py
│   ├── specialist.py
│   ├── hospital.py
│   ├── medicine.py
│   ├── diet.py
│   ├── emergency.py
│   ├── auth.py
│   ├── database.py
│   ├── models.py
│   └── requirements.txt
│
├── frontend
│   ├── public
│   ├── src
│   ├── package.json
│   └── ...
│
├── README.md
└── .gitignore
```

## 🚀 Installation

### Clone the Repository

```bash
git clone https://github.com/ChandanaB12/MedicalChatbotProject.git
```

### Backend Setup

```bash
cd MedicalChatbotProject/backend
pip install -r requirements.txt
uvicorn main:app --reload
```

### Frontend Setup

```bash
cd ../frontend
npm install
npm start
```

## ▶️ How to Use

1. Register a new account or log in.
2. Enter your symptoms (for example: `fever, cough, body pain`).
3. View the predicted disease.
4. Check the confidence score.
5. View the recommended specialist.
6. Read the medicine and diet suggestions.
7. Check hospital recommendations if required.
8. Download the medical report as a PDF.

## 🔮 Future Enhancements

- Add Machine Learning-based disease prediction.
- Improve symptom matching using Natural Language Processing (NLP).
- Add multilingual support.
- Integrate real hospital APIs.
- Enable appointment booking with doctors.
- Add email notifications and reminders.
- Improve chatbot responses using Large Language Models (LLMs).

## 👩‍💻 Author

**Chandana B**

- GitHub: https://github.com/ChandanaB12
- Project: AI Medical Chatbot Assistant

## 📸 Screenshots

> *(Add screenshots of your application here after capturing them.)*

- Login Page
- Registration Page
- Home Page
- Chat Interface
- Disease Prediction Result
- PDF Medical Report