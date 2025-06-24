from pydantic import BaseModel
from typing import List


class Stop(BaseModel):
    name: str
    address: str
    lat: float
    lng: float


class CabAssignment(BaseModel):
    cab_id: int
    stops: List[Stop]
    eta: str
    cab_lat: float
    cab_lng: float
