# backend/database.py

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from backend.config import DATABASE_URL

# PostgreSQL async connection
engine = create_async_engine(DATABASE_URL, echo=True, future=True)

# Session factory
AsyncSessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

# Dependency for route injection
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session
