from fastapi import APIRouter
from backend.models.cluster import CabAssignment

router = APIRouter(prefix="/driver", tags=["Driver"])

# Dummy route (replace with DB data)
@router.get("/route", response_model=CabAssignment)
def get_driver_route():
    return {
        "cab_id": 1,
        "stops": [
            {"name": "Alice", "address": "Sector 21", "lat": 28.5, "lng": 77.1},
            {"name": "Bob", "address": "Sector 17", "lat": 28.6, "lng": 77.2},
        ],
        "eta": "08:00 AM",
        "cab_lat": 28.52,
        "cab_lng": 77.08,
    }
