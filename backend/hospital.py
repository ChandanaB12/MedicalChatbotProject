def get_hospitals(specialist):

    hospitals = {
        "General Physician": [
            {
                "hospital_name": "Vijayanagara Institute of Medical Sciences (VIMS)",
                "contact_number": "08392-242355",
                "address": "Ballari, Karnataka",
                "google_maps": "https://maps.google.com"
            },
            {
                "hospital_name": "Ballari District Hospital",
                "contact_number": "08392-270000",
                "address": "Ballari, Karnataka",
                "google_maps": "https://maps.google.com"
            }
        ],

        "Pulmonologist": [
            {
                "hospital_name": "KIMS Hospital",
                "contact_number": "08392-250000",
                "address": "Ballari, Karnataka",
                "google_maps": "https://maps.google.com"
            }
        ],

        "Neurologist": [
            {
                "hospital_name": "Apollo Hospital",
                "contact_number": "080-12345678",
                "address": "Bengaluru, Karnataka",
                "google_maps": "https://maps.google.com"
            }
        ],

        "Gastroenterologist": [
            {
                "hospital_name": "Manipal Hospital",
                "contact_number": "080-22223333",
                "address": "Bengaluru, Karnataka",
                "google_maps": "https://maps.google.com"
            }
        ]
    }

    return hospitals.get(specialist, [])