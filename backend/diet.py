def get_diet(disease):

    diets = {

        "Viral Infection": [
            "Drink plenty of water",
            "Eat fruits rich in Vitamin C",
            "Consume light and nutritious meals"
        ],

        "Malaria": [
            "Drink plenty of fluids",
            "Eat iron-rich foods like spinach",
            "Include fresh fruits and vegetables"
        ],

        "Common Cold": [
            "Drink warm fluids",
            "Eat citrus fruits",
            "Have soup and soft foods"
        ],

        "Migraine": [
            "Drink enough water",
            "Avoid caffeine and processed foods",
            "Eat meals on time"
        ],

                "Food Poisoning": [
            "Drink ORS and plenty of water",
            "Eat soft foods like rice and bananas",
            "Avoid oily and spicy foods"
        ],

        "COVID-19": [
            "Drink plenty of fluids",
            "Eat protein-rich foods",
            "Consume fruits rich in Vitamin C"
        ],

        "Influenza": [
            "Drink warm fluids",
            "Eat soup and light meals",
            "Increase Vitamin C intake"
        ],

        "Pneumonia": [
            "Drink plenty of water",
            "Eat protein-rich foods",
            "Consume fruits and vegetables"
        ],

        "Diabetes": [
            "Eat a balanced diet",
            "Choose whole grains and high-fiber foods",
"Limit sugary foods and sweetened beverages",
"Eat balanced meals at regular times"
            "Include whole grains and vegetables"
        ],

        "Hypertension": [
            "Reduce salt intake",
            "Eat fruits and vegetables",
            "Avoid processed foods"
            "Limit processed foods",
"Choose low-sodium meals"
        ],

        "Urinary Tract Infection (UTI)": [
            "Drink plenty of water",
            "Drink unsweetened cranberry juice (if suitable)",
            "Avoid caffeine and alcohol"
        ],

        "Gastritis": [
            "Eat soft, non-spicy foods",
            "Avoid oily and spicy foods",
            "Eat small meals frequently"
        ],

                "Typhoid": [
            "Drink plenty of clean water",
            "Eat soft and easily digestible foods",
            "Avoid spicy and oily foods"
        ],

        "Dengue": [
    "Drink plenty of fluids",
    "Drink ORS if dehydrated",
    "Eat soft, easily digestible foods",
    "Include fruits rich in Vitamin C"
],

"Asthma": [
    "Drink warm fluids",
    "Eat foods rich in Vitamin D",
    "Avoid cold foods if they trigger symptoms"
],

"Allergy": [
    "Eat fresh fruits and vegetables",
    "Drink plenty of water",
    "Avoid foods that trigger allergies"
],

"Sinusitis": [
    "Drink warm fluids",
    "Eat Vitamin C-rich foods",
    "Stay well hydrated"
],

"Chickenpox": [
    "Drink plenty of water",
    "Eat soft, easy-to-swallow foods",
    "Include fruits and vegetables"
],

"Bronchitis": [
    "Drink warm fluids",
    "Eat nutritious meals",
    "Include fruits rich in Vitamin C"
],

"Tuberculosis": [
    "Eat protein-rich foods",
    "Include milk, eggs, pulses, and vegetables",
    "Maintain a balanced, nutritious diet"
],

"Appendicitis": [
    "Do not eat or drink if surgery is suspected",
    "Follow your doctor's dietary advice after treatment"
]

    }

    return diets.get(
        disease,
        ["Maintain a balanced and healthy diet."]
    )