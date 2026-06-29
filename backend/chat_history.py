from database import SessionLocal
from models import ChatHistory

# Save chat to MySQL
def save_chat(user_id, symptoms, prediction):
    db = SessionLocal()

    chat = ChatHistory(
        user_id=user_id,
        symptoms=symptoms,
        prediction=prediction
    )

    db.add(chat)
    db.commit()
    db.close()


# Get chat history from MySQL
def get_history(user_id):
    db = SessionLocal()

    history = db.query(ChatHistory).filter(
        ChatHistory.user_id == user_id
    ).all()

    db.close()

    return history