from fastapi import APIRouter, Depends
from backend.models.ride import RideRequest
from backend.models.cluster import CabAssignment
from datetime import date

router = APIRouter(prefix="/employee", tags=["Employee"])

# Dummy storage (replace with DB in real implementation)
ride_log = []
cab_data = {
    "cab_id": 1,
    "stops": [
        {"name": "Alice", "address": "Sector 21", "lat": 28.5, "lng": 77.1}
    ],
    "eta": "08:15 AM",
    "cab_lat": 28.52,
    "cab_lng": 77.08,
}


@router.post("/request-ride")
def request_ride(request: RideRequest):
    ride_log.append({
        "employee_name": "Alice",
        "trip_type": request.trip_type,
        "date": date.today(),
        "cab_id": 1
    })
    return {"message": "Ride booked successfully"}


@router.get("/my-cab", response_model=CabAssignment)
def my_cab():
    return cab_data
