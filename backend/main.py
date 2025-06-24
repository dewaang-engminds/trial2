# backend/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.routers import auth, employee, driver, admin

app = FastAPI(title="CabRoute AI")

# Allow frontend (e.g., React on localhost:3000)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this to specific domain in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routers
app.include_router(auth.router)
app.include_router(employee.router)
app.include_router(driver.router)
app.include_router(admin.router)

@app.get("/")
def root():
    return {"message": "CabRoute AI backend is running"}
