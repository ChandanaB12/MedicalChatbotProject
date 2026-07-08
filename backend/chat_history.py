from datetime import datetime

# Stores chat history in memory
chat_history = []

def save_chat(symptoms, prediction):
    chat_history.append({
        "time": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
        "symptoms": symptoms,
        "prediction": prediction
    })

def get_history():
    return chat_history
 