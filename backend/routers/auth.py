from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from backend.models.user import UserLogin, Role
import jwt
import os

router = APIRouter(prefix="/auth", tags=["Auth"])

JWT_SECRET = os.getenv("JWT_SECRET", "supersecret")
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")

# Temporary in-memory user DB
users = {
    "employee@example.com": {"password": "pass123", "name": "Alice", "role": "employee"},
    "driver@example.com": {"password": "pass123", "name": "Bob", "role": "driver"},
    "admin@example.com": {"password": "pass123", "name": "Carol", "role": "admin"},
}


@router.post("/login")
def login(data: UserLogin):
    user = users.get(data.email)
    if not user or user["password"] != data.password:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = jwt.encode(
        {"email": data.email, "role": user["role"]},
        JWT_SECRET,
        algorithm=JWT_ALGORITHM
    )
    return {"access_token": token, "role": user["role"]}
