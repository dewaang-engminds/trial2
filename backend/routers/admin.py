from fastapi import APIRouter
from backend.models.ride import RideLog
from datetime import date

router = APIRouter(prefix="/admin", tags=["Admin"])

# Dummy data
ride_history = [
    {"employee_name": "Alice", "date": date.today(), "trip_type": "AM", "cab_id": 1},
    {"employee_name": "Bob", "date": date.today(), "trip_type": "PM", "cab_id": 1},
]


@router.get("/rides", response_model=list[RideLog])
def get_rides():
    return ride_history
