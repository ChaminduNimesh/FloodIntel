from app import create_app
from app.extensions import db
from app.models.shelter_model import Shelter

app = create_app()
app.app_context().push()

db.create_all()

real_shelters = [
    {"area": "Hanwella", "name": "Divisional Secretariat Seethawaka", "type": "Government/Relief Coordination", "phone": "+94362255043", "lat": 6.8973, "lng": 80.0881, "distanceKm": 1.8},
    {"area": "Hanwella", "name": "Divisional Hospital Nawagamuwa", "type": "Government Hospital", "phone": "+94112415225", "lat": 6.9221, "lng": 80.0143, "distanceKm": 3.2},
    {"area": "Hanwella", "name": "Hanwella Police Station", "type": "Police Station", "phone": "+94362255222", "lat": 6.9008, "lng": 80.0875, "distanceKm": 1.1},
    {"area": "Hanwella", "name": "Hanwella Rajasinghe Central College", "type": "Evacuation Centre (School)", "phone": "+94362255015", "lat": 6.9088, "lng": 80.0872, "distanceKm": 1.2},
    {"area": "Kaduwela", "name": "Divisional Secretariat Kaduwela", "type": "Government/Relief Coordination", "phone": "+94112561021", "lat": 6.9034, "lng": 79.9542, "distanceKm": 2.1},
    {"area": "Kaduwela", "name": "Colombo East Base Hospital, Mulleriyawa", "type": "Government Hospital", "phone": "+94112549390", "lat": 6.9249, "lng": 79.9429, "distanceKm": 2.8},
    {"area": "Kaduwela", "name": "Police Station Kaduwela", "type": "Police Station", "phone": "+94112159224", "lat": 6.9361, "lng": 79.9702, "distanceKm": 1.4},
    {"area": "Kaduwela", "name": "Kothalawala Maha Vidyalaya", "type": "Evacuation Centre (School)", "phone": "+94112539069", "lat": 6.9295, "lng": 79.9823, "distanceKm": 0.9},
    {"area": "Angoda", "name": "Divisional Secretariat Kolonnawa", "type": "Government/Relief Coordination", "phone": "+94112572281", "lat": 6.9319, "lng": 79.8904, "distanceKm": 2.5},
    {"area": "Angoda", "name": "National Institute of Infectious Diseases", "type": "Government Hospital", "phone": "+94112411590", "lat": 6.9226, "lng": 79.9182, "distanceKm": 1.6},
    {"area": "Angoda", "name": "Mulleriyawa Police Station", "type": "Police Station", "phone": "+94112578279", "lat": 6.9272, "lng": 79.9292, "distanceKm": 0.6},
]

for s in real_shelters:
    shelter = Shelter(
        area_name=s["area"], name=s["name"], type=s["type"], phone=s["phone"],
        lat=s["lat"], lng=s["lng"], distance_km=s["distanceKm"],
    )
    db.session.add(shelter)

db.session.commit()
print(f"Migrated {len(real_shelters)} real shelters")
