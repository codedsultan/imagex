from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import settings

client = AsyncIOMotorClient(settings.MONGODB_URL)
db = client.get_default_database()

async def get_mongo_db():
    yield db
