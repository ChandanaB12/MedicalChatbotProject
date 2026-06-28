import joblib
import os

# Get the folder where this file is located
current_dir = os.path.dirname(os.path.abspath(__file__))

# Load the trained model
model_path = os.path.join(current_dir, "intent_model.pkl")
model = joblib.load(model_path)


def predict_intent(user_input):
    """
    Predict the user's intent using the trained ML model.
    """
    prediction = model.predict([user_input])
    return prediction[0]