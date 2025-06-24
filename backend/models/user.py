from pydantic import BaseModel, EmailStr
from enum import Enum


class Role(str, Enum):
    employee = "employee"
    driver = "driver"
    admin = "admin"


class UserBase(BaseModel):
    name: str
    email: EmailStr
    role: Role


class UserCreate(UserBase):
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserOut(UserBase):
    id: int

    class Config:
        orm_mode = True
