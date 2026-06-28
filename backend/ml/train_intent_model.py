import pandas as pd
import joblib

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

# Load training data
data = pd.read_csv("intents.csv")

# Train model
model = Pipeline([
    ("vectorizer", CountVectorizer()),
    ("classifier", MultinomialNB())
])

model.fit(data["text"], data["intent"])

# Save model
joblib.dump(model, "intent_model.pkl")

print("✅ Machine Learning model trained successfully!")