import json

def load_disease_dataset():
    with open("data/medical_dataset.json", "r", encoding="utf-8") as file:
        return json.load(file)