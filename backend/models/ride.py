from pydantic import BaseModel
from datetime import date
from enum import Enum


class RideType(str, Enum):
    AM = "AM"
    PM = "PM"
    BOTH = "BOTH"


class RideRequest(BaseModel):
    trip_type: RideType


class RideLog(BaseModel):
    employee_name: str
    date: date
    trip_type: RideType
    cab_id: int

