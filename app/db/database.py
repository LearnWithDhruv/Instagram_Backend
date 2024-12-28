from motor.motor_asyncio import AsyncIOMotorClient
from app.config import DATABASE_URL

client = AsyncIOMotorClient(DATABASE_URL)
db = client.backend

def get_collection(collection_name):
    return db[collection_name]

async def test_connection():
    try:
        db_list = await client.list_database_names()
        print("Successfully connected to MongoDB!")
        print("Databases:", db_list)
    except Exception as e:
        print("Error connecting to MongoDB:", e)