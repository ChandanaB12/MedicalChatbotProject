from database import SessionLocal
from sqlalchemy import text

def get_hospitals(specialist):

    db = SessionLocal()

    result = db.execute(
        text("""
            SELECT hospital_name,
                   contact_number,
                   address,
                   google_maps
            FROM hospitals
            WHERE specialist = :specialist
        """),
        {"specialist": specialist}
    )

    hospitals = []

    for row in result:
        hospitals.append({
         
    "hospital_name": row.hospital_name,
    "contact_number": row.contact_number,
    "address": row.address,
    "google_maps": row.google_maps
 
        })

    db.close()

    return hospitals