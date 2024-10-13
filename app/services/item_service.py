from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import settings

# Initialize MongoDB connection
client = AsyncIOMotorClient(settings.MONGODB_URL)
db = client[settings.DATABASE_NAME]

# Collection for Items
item_collection = db["items"]

async def fetch_all_items():
    items = await item_collection.find().to_list(100)
    return items

async def fetch_item_by_id(item_id: str):
    item = await item_collection.find_one({"_id": item_id})
    return item

async def create_item(item_data: dict):
    result = await item_collection.insert_one(item_data)
    return str(result.inserted_id)

async def update_item(item_id: str, item_data: dict):
    await item_collection.update_one({"_id": item_id}, {"$set": item_data})
    return item_data

async def delete_item(item_id: str):
    result = await item_collection.delete_one({"_id": item_id})
    return result.deleted_count
